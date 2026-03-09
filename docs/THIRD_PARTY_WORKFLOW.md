# Third-party extensions workflow

This document describes the simplest end-to-end workflow to label and publish third-party DuckDB extensions (outside the official core/community registries).

## What gets published
GitHub Actions publishes the third-party page from the committed CSV at:
- `labels/third_party_extension_labels.csv`

The CI workflow imports that CSV into its DuckDB snapshot, then renders and deploys the third-party report to GitHub Pages.

## Local labelling workflow (recommended)
These commands use the separate third-party labelling database so your interactive work is not overwritten by the daily bot commits.

### 1) Ensure you have the third-party DB
The default DB path is:
- `data/third_party_extensions.duckdb`

If you already have it, you can skip to labelling.

If you need to (re)create/populate it, load the latest validated/promoted discovery outputs into the third-party DB:

```bash
just thirdparty-load-db data/discovery/validated_extension_candidates_YYYYMMDD.json data/discovery/promoted_candidates_YYYYMMDD.json "notes about this run"
```

### 2) Label candidates (promoted + incremental)
Label a small batch at a time (for example, 20):

```bash
just thirdparty-label-loop-promoted-incremental 20
```

Notes:
- This mode focuses on “promoted” candidates.
- `-incremental` only shows new/changed candidates since your last labels.

### 3) Export labels to the committed CSV
After labelling, export all labels from the third-party DB into the committed CSV:

```bash
just thirdparty-label-export-committed
```

This step ensures the CSV reflects what is currently stored in `data/third_party_extensions.duckdb`.

### 4) Commit + push
Check what changed:

```bash
git status
```

Commit and push the updated CSV:

```bash
git add labels/third_party_extension_labels.csv

git commit -m "Update third-party labels" -m "Co-Authored-By: Oz <oz-agent@warp.dev>"

git push
```

If `git push` is rejected (the daily workflow bot often advances `main`), rebase and retry:

```bash
git fetch origin main

git rebase origin/main

git push
```

### 5) Trigger the GitHub Action
Manually trigger the daily workflow (this regenerates reports and redeploys Pages):

```bash
gh workflow run "Daily DuckDB Extensions Report" --ref main
```

(Optional) Watch the run:

```bash
gh run list --workflow daily-extensions-report.yml --limit 5
# then:
# gh run watch <run_id>
```

### 6) Verify the published page
Third-party page:
- https://mjboothaus.github.io/duckdb-extensions-analysis/third-party/

Main report:
- https://mjboothaus.github.io/duckdb-extensions-analysis/

## Useful extras
### Stats
To see coverage stats for promoted candidates:

```bash
just thirdparty-label-stats
```

### Render locally (optional)
If you want to render the third-party report locally without waiting for CI:

```bash
just thirdparty-report-verified
uv run python scripts/build_report_site.py --input reports/third_party_extensions_verified.md --out-dir /tmp/duckdb-third-party --out-file index.html
```
