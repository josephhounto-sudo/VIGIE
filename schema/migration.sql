-- ============================================================
-- VIGIE — CONTRAT DE DONNEES SECURISE PAR DEFAUT
--
-- Aucune politique d'acces client n'est creee ici. Les tables restent
-- inaccessibles aux roles anon/authenticated tant qu'un modele d'identite,
-- de roles et de retention n'a pas ete valide avec l'institution partenaire.
-- Les traitements de confiance devront utiliser un role serveur non expose.
-- Sur une base deja peuplee avec l'ancien schema, faire une sauvegarde et
-- auditer les valeurs et doublons avant execution : les contraintes sont
-- volontairement plus strictes et peuvent reveler des donnees incompatibles.
-- ============================================================

create table if not exists public.evenements (
  id bigint generated always as identity primary key,
  source_type text not null,
  source_id text,
  titre text not null,
  description text,
  latitude double precision,
  longitude double precision,
  horodatage timestamptz not null default now(),
  nature text not null default 'a_verifier',
  criticite integer not null default 20,
  justification text,
  statut text not null default 'nouveau',
  date_peremption timestamptz,
  statut_preuve text not null default 'non_disponible'
);

alter table public.evenements
  add column if not exists statut_preuve text not null default 'non_disponible';

do $$
begin
  alter table public.evenements add constraint evenements_source_type_check
    check (source_type in ('rf_drone', 'remote_id', 'agent_terrain', 'flux_anomalie', 'test_faa_import'));
exception when duplicate_object then null;
end $$;

do $$
begin
  alter table public.evenements add constraint evenements_latitude_check
    check (latitude is null or latitude between -90 and 90);
exception when duplicate_object then null;
end $$;

do $$
begin
  alter table public.evenements add constraint evenements_longitude_check
    check (longitude is null or longitude between -180 and 180);
exception when duplicate_object then null;
end $$;

do $$
begin
  alter table public.evenements add constraint evenements_criticite_check
    check (criticite between 0 and 100);
exception when duplicate_object then null;
end $$;

do $$
begin
  alter table public.evenements add constraint evenements_nature_check
    check (nature in ('fausse_alerte_probable', 'anomalie', 'a_verifier'));
exception when duplicate_object then null;
end $$;

do $$
begin
  alter table public.evenements add constraint evenements_statut_check
    check (statut in ('nouveau', 'a_verifier', 'confirme', 'rejete', 'clos'));
exception when duplicate_object then null;
end $$;

do $$
begin
  alter table public.evenements add constraint evenements_preuve_check
    check (statut_preuve in ('mesure', 'rapporte', 'simule', 'externe', 'non_disponible'));
exception when duplicate_object then null;
end $$;

comment on column public.evenements.statut_preuve is
  'Provenance de la preuve, distincte du classement et du verdict humain.';

create index if not exists evenements_horodatage_idx on public.evenements (horodatage desc);
create index if not exists evenements_statut_idx on public.evenements (statut);
create index if not exists evenements_source_idx on public.evenements (source_type, source_id);

create table if not exists public.correlations (
  id bigint generated always as identity primary key,
  evenement_a_id bigint not null references public.evenements(id) on delete cascade,
  evenement_b_id bigint not null references public.evenements(id) on delete cascade,
  raison text not null,
  score_lien integer not null default 0,
  type_lien text not null,
  date_creation timestamptz not null default now(),
  constraint correlations_evenements_distincts check (evenement_a_id <> evenement_b_id),
  constraint correlations_score_check check (score_lien between 0 and 100),
  constraint correlations_type_check check (type_lien in ('meme_zone', 'proximite_forte'))
);

create unique index if not exists correlations_paire_unique_idx
  on public.correlations (
    least(evenement_a_id, evenement_b_id),
    greatest(evenement_a_id, evenement_b_id)
  );

create index if not exists correlations_date_idx on public.correlations (date_creation desc);

create table if not exists public.decisions (
  id bigint generated always as identity primary key,
  evenement_id bigint references public.evenements(id) on delete restrict,
  correlation_id bigint references public.correlations(id) on delete restrict,
  verdict text not null,
  justification text not null,
  acteur_id text not null,
  date_creation timestamptz not null default now(),
  constraint decisions_cible_unique check (
    (evenement_id is not null and correlation_id is null)
    or (evenement_id is null and correlation_id is not null)
  ),
  constraint decisions_verdict_check check (verdict in ('confirme', 'corrige', 'rejete'))
);

create index if not exists decisions_evenement_idx on public.decisions (evenement_id, date_creation desc);
create index if not exists decisions_correlation_idx on public.decisions (correlation_id, date_creation desc);

create table if not exists public.sources_signal (
  source_id text primary key,
  source_type text not null,
  nb_emis integer not null default 0 check (nb_emis >= 0),
  nb_confirmes integer not null default 0 check (nb_confirmes >= 0),
  nb_rejetes integer not null default 0 check (nb_rejetes >= 0)
);

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

alter table public.evenements enable row level security;
alter table public.correlations enable row level security;
alter table public.decisions enable row level security;
alter table public.sources_signal enable row level security;

revoke all on public.evenements from anon, authenticated;
revoke all on public.correlations from anon, authenticated;
revoke all on public.decisions from anon, authenticated;
revoke all on public.sources_signal from anon, authenticated;
revoke all on public.evenements_id_seq from anon, authenticated;
revoke all on public.correlations_id_seq from anon, authenticated;
revoke all on public.decisions_id_seq from anon, authenticated;

drop policy if exists "anon_all_evenements" on public.evenements;
drop policy if exists "anon_all_correlations" on public.correlations;
drop policy if exists "anon_all_sources_signal" on public.sources_signal;

-- Aucune policy permissive par defaut : acces refuse jusqu'a definition
-- explicite des roles du pilote.
