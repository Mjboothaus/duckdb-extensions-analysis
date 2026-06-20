# Great Docs
This repository publishes two separate GitHub Pages surfaces:
- The main **report UI** (generated from `reports/latest.md`) is published at the Pages root.
- Great Docs is used for **project documentation** and is published under `/docs/`.

## Public URLs
- Report site (root): https://mjboothaus.github.io/duckdb-extensions-analysis/
- Project docs (Great Docs): https://mjboothaus.github.io/duckdb-extensions-analysis/docs/

## Local usage
This project uses `uv`.

### Build
- `just docs-build`

Output:
- `great-docs/_site/`

### Preview
- `just docs-preview`

Note: Great Docs requires **Quarto** to be installed on your machine.

### Quality checks
- `just docs-lint`
- `just docs-check-links`
- `just docs-check-links-strict`

## GitHub Pages integration
The existing report publishing workflow (`.github/workflows/daily-extensions-report.yml`) also builds Great Docs and copies it into `_site/docs/` before deploying.

This avoids conflicts with the report UI, which remains published at `/`.
