-- ============================================================
-- VIGIE — SCHEMA COMMUN (contrat entre sources et moteur)
-- Style Supabase, meme conventions que SENTINELLE_COMPLET.md.
-- Idempotent : peut etre relance sans risque.
--
-- ⚠️ ATTENTION SECURITE (ajoute le 19/08/2026, a traiter avant toute
-- connexion Supabase reelle, pas avant) : les policies ci-dessous
-- donnent un acces complet ("using (true) with check (true)") au role
-- anon -- correct pour un prototype de developpement isole, mais PAS
-- pour une instance connectee a de vraies donnees. Avant production :
-- corriger les droits anon, ajouter une authentification, separer
-- lecture/ecriture, limiter les champs exposes, journaliser les
-- modifications. Aucune cle API ne doit jamais etre placee dans
-- l'HTML/JS cote client ni committee dans le depot.
-- ============================================================

-- ─── 1. EVENEMENTS (table unique, toute source y ecrit) ──────
-- Une alerte RF et un signalement agent produisent la MEME forme
-- de ligne. C'est le contrat : le volet materiel et le volet
-- logiciel n'ont besoin de se parler QUE via cette table.

create table if not exists public.evenements (
  id bigint generated always as identity primary key,
  source_type text not null,        -- 'rf_drone' | 'agent_terrain' | 'flux_anomalie'
  source_id text,                    -- identifiant du capteur/agent emetteur
  titre text not null,
  description text,
  latitude double precision,
  longitude double precision,
  horodatage timestamp default now(),

  -- rempli par le moteur de classification (src/classification)
  nature text,                       -- 'incident_confirme' | 'fausse_alerte' | 'anomalie' | 'a_verifier'
  criticite integer,                 -- 0-100, meme logique de garde-fou que Sentinelle
  justification text,

  statut text default 'nouveau',     -- 'nouveau' | 'a_verifier' | 'confirme' | 'rejete' | 'clos'
  date_peremption timestamp,

  -- Ajoute le 19/08/2026 : distingue la PROVENANCE de la preuve, separement
  -- de `nature` (le jugement IA) et de `statut` (l'etat du traitement).
  -- Empeche qu'une donnee de test (simule/externe) soit un jour confondue
  -- avec une vraie observation togolaise (mesure).
  statut_preuve text default 'non_disponible'  -- 'mesure' | 'rapporte' | 'simule' | 'externe' | 'non_disponible'
);

comment on column public.evenements.statut_preuve is
  'Provenance de la preuve : mesure (obtenue par l''equipe, protocole consigne), '
  'rapporte (source externe publiee, non reproduite), simule (donnee de test), '
  'externe (autre contexte, ex. FAA/RFUAV, jamais un signalement togolais), '
  'non_disponible (non obtenu/verifie). Ne jamais laisser vide silencieusement.';

-- Si la table existait deja avant le 19/08/2026 (ancien schema sans ce
-- champ), cette ligne l'ajoute sans rien casser :
alter table public.evenements add column if not exists statut_preuve text default 'non_disponible';

alter table public.evenements enable row level security;
grant all on public.evenements to anon;
grant all on public.evenements_id_seq to anon;

drop policy if exists "anon_all_evenements" on public.evenements;
create policy "anon_all_evenements" on public.evenements
  for all to anon using (true) with check (true);

-- ─── 2. CORRELATIONS (Bloc "recoupement", meme pattern que ─────
--        moteur_connexions.py de Sentinelle : lien entre 2 objets,
--        cree seulement si score >= seuil strict)

create table if not exists public.correlations (
  id bigint generated always as identity primary key,
  evenement_a_id bigint references public.evenements(id) on delete cascade,
  evenement_b_id bigint references public.evenements(id) on delete cascade,
  raison text,
  score_lien integer default 0,      -- seuil recommande >= 60, comme Sentinelle
  type_lien text,                    -- 'meme_zone' | 'meme_creneau' | 'recurrence'
  date_creation timestamp default now(),
  unique (evenement_a_id, evenement_b_id)
);

alter table public.correlations enable row level security;
grant all on public.correlations to anon;
grant all on public.correlations_id_seq to anon;

drop policy if exists "anon_all_correlations" on public.correlations;
create policy "anon_all_correlations" on public.correlations
  for all to anon using (true) with check (true);

-- ─── 3. SUIVI QUALITE PAR SOURCE (meme principe que ─────────────
--        qualite_sources dans Sentinelle : chaque verdict humain
--        remonte vers la source pour juger sa fiabilite dans le
--        temps -- CA, c'est la lecon tiree de Sentinelle : cette
--        boucle doit exister DES LE DEPART, pas ajoutee apres coup.

create table if not exists public.sources_signal (
  source_id text primary key,
  source_type text,
  nb_emis integer default 0,
  nb_confirmes integer default 0,
  nb_rejetes integer default 0
);

alter table public.sources_signal enable row level security;
grant all on public.sources_signal to anon;

drop policy if exists "anon_all_sources_signal" on public.sources_signal;
create policy "anon_all_sources_signal" on public.sources_signal
  for all to anon using (true) with check (true);

create or replace view public.fiabilite_sources as
select
  s.source_id,
  s.source_type,
  s.nb_emis,
  s.nb_confirmes,
  s.nb_rejetes,
  case
    when (s.nb_confirmes + s.nb_rejetes) = 0 then null
    else round(100.0 * s.nb_confirmes / (s.nb_confirmes + s.nb_rejetes), 1)
  end as taux_fiabilite_pct
from public.sources_signal s
order by taux_fiabilite_pct desc nulls last;

-- ============================================================
-- FIN — "Success. No rows returned" attendu
-- ============================================================
