# What’s new
This file is a lightweight, monthly roundup of notable developments in the DuckDB ecosystem that may affect extensions (and therefore what this repository monitors), plus a short note on relevant changes in this repo.

## Live reports
- Main report (Core & Community): https://mjboothaus.github.io/duckdb-extensions-analysis/
- Third-party extensions (work in progress): https://mjboothaus.github.io/duckdb-extensions-analysis/third-party/
- Compatibility testing (experimental, on-demand): https://mjboothaus.github.io/duckdb-extensions-analysis/compatibility/

## 2026-05
### DuckDB: Quack (client/server) lands
- 2026-05-12: DuckDB announced **Quack**, a remote protocol/extension that turns DuckDB into a client/server database (beta).
  - Overview: https://duckdb.org/quack/
  - Announcement: https://duckdb.org/2026/05/12/quack-remote-protocol
- 2026-05-20: DuckDB **v1.5.3** shipped with Quack as a **core extension** (autoinstall/autoload on first use).
  - Blog: https://duckdb.org/2026/05/20/announcing-duckdb-153
  - Release tag: https://github.com/duckdb/duckdb/releases/tag/v1.5.3

Why this matters here: new core extensions and extension delivery changes can affect discovery, installation health, and compatibility signals.

### DuckDB 1.5.x patch cadence
- DuckDB v1.5.1 (2026-03-23), v1.5.2 (2026-04-13), v1.5.3 (2026-05-20)
  - Release calendar: https://duckdb.org/release_calendar

## 2026-04
### DuckLake v1.0
- 2026-04-13: DuckLake **v1.0** released (production-ready spec with backwards compatibility).
  - Announcement: https://ducklake.select/2026/04/13/ducklake-10/
  - DuckLake release calendar + compatibility matrix: https://ducklake.select/release_calendar.html

Why this matters here: DuckLake is a core extension (`ducklake`) and it is increasingly part of the “extension ecosystem surface area” (especially as it intersects with Quack).

## 2026-03
### DuckDB v1.5.0 (Variegata)
- 2026-03-09: DuckDB **v1.5.0** released (codename: Variegata).
  - Release calendar entry: https://duckdb.org/release_calendar

## Recent changes in this repo
- Fixed core extension discovery + documentation links (moved to `docs/current`) so core extensions no longer disappear from the published report.
- Added an executive summary to the main report for a faster “at a glance” view.
- Added an experimental, on-demand compatibility testing report (published separately): https://mjboothaus.github.io/duckdb-extensions-analysis/compatibility/
- Improved release-date accuracy by deriving newly released DuckDB versions from the GitHub Releases publish date when the upstream CSV lags.

---
If you spot a noteworthy ecosystem change that should be tracked here, please open an issue or PR with a link to the upstream announcement/release notes.