-- ============================================================
-- VIGIE — SCHEMA COMMUN (contrat entre sources et moteur)
-- Style Supabase, meme conventions que SENTINELLE_COMPLET.md.
-- Idempotent : peut etre relance sans risque.
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

  statut text default 'nouveau',     -- 'nouveau' | 'confirme' | 'rejete' | 'traite'
  date_peremption timestamp
);

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
