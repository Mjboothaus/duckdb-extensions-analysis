# Backlog
This file tracks potential improvements for DuckDB Extensions Analysis.

## Workflow reliability and orchestration
- GitHub Actions: keep the daily report workflow split into resumable jobs (analyse/render → publish → deploy) and keep the daily path fast.
- Compatibility testing: run phased compatibility checks via a separate manual workflow, with strict time/size limits.
- Prefect (optional, future): consider moving orchestration from GitHub Actions to Prefect 3.x+ if we need stronger retries, partitioned re-runs, fan-out/fan-in phases, or richer observability.
  - Trade-off: adds infrastructure/ops overhead (Prefect server/Cloud, agents, credentials), so it should only be adopted when GitHub Actions hardening is no longer sufficient.
