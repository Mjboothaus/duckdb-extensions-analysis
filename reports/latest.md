# DuckDB Extensions Analysis

🦆 **Automated monitoring and analysis of DuckDB's extension ecosystem**


[Executive summary](#executive-summary) | [Jump to Summary](#summary) | [Core Extensions](#core-extensions) | [Community Extensions](#community-extensions)

---

**Running on DuckDB:** v1.5.5 (2026-07-22)
This report provides a comprehensive analysis of DuckDB extensions, including both core extensions (built into DuckDB) and community-contributed extensions.

For third-party extensions discovered outside the official registries, see: [Third-party extensions](https://mjboothaus.github.io/duckdb-extensions-analysis/third-party/).

For a lightweight monthly roundup of notable ecosystem changes, see: [What’s new](https://github.com/Mjboothaus/duckdb-extensions-analysis/blob/main/WHATS_NEW.md).

*Note:* third-party labelling is an ongoing work in progress, so the verified list is partial.

---
## Executive summary


### At a glance
- **379** total extensions tracked (**29** core, **350** community)
- **112 / 379** extensions updated in the last 7 days
- **204 / 379** extensions updated in the last 30 days
- **1** community repositories are archived
- **87** community extensions have unknown/repo issues (missing or inaccessible repositories)

### Highlights
#### Most active (last 7 days)
| Extension | Repository | Last activity |
|---|---|---|
| [mssql](https://duckdb.org/community_extensions/extensions/mssql.html) | [mssql-extension](https://github.com/hugr-lab/mssql-extension) | today (2026-09-25 11:13:34 UTC) |
| [adbc_scanner](https://duckdb.org/community_extensions/extensions/adbc_scanner.html) | [adbc_scanner](https://github.com/Query-farm/adbc_scanner) | today (2026-09-25 03:03:10 UTC) |
| [ai](https://duckdb.org/community_extensions/extensions/ai.html) | [duckdb-ai](https://github.com/leonardovida/duckdb-ai) | today (2026-09-25 09:43:18 UTC) |
| [anndata](https://duckdb.org/community_extensions/extensions/anndata.html) | [anndata-duckdb-extension](https://github.com/honicky/anndata-duckdb-extension) | today (2026-09-24 12:34:10 UTC) |
| [anofox_forecast](https://duckdb.org/community_extensions/extensions/anofox_forecast.html) | [anofox-forecast](https://github.com/DataZooDE/anofox-forecast) | today (2026-09-25 03:25:07 UTC) |

#### Most starred (community)
| Extension | Repository | Stars |
|---|---|---:|
| [duckpgq](https://duckdb.org/community_extensions/extensions/duckpgq.html) | [duckpgq-extension](https://github.com/cwida/duckpgq-extension) | 499 |
| [flock](https://duckdb.org/community_extensions/extensions/flock.html) | [flock](https://github.com/dais-polymtl/flock) | 359 |
| [gsheets](https://duckdb.org/community_extensions/extensions/gsheets.html) | [duckdb_gsheets](https://github.com/evidence-dev/duckdb_gsheets) | 354 |
| [airport](https://duckdb.org/community_extensions/extensions/airport.html) | [airport](https://github.com/Query-farm/airport) | 350 |
| [prql](https://duckdb.org/community_extensions/extensions/prql.html) | [duckdb-prql](https://github.com/ywelsch/duckdb-prql) | 332 |

### How to read the report
- **Status** is a repository signal (ongoing / archived / unknown).
- **Activity** is based on the last git push; quiet projects can still be healthy.
- Use the tables below to drill into **Core Extensions** and **Community Extensions**.

---
## Summary

### 📊 Quick Stats (with trends)

| **Metric** | **Current** | **Change** |
|------------|-------------|------------|
| **Total Extensions** | 379 | +9 🔼 |
| **Core Extensions** | 29 | → Stable |
| **Community Extensions** | 350 | +9 🔼 |
| **Recently Active** (≤ 30 days) | 204 (53.8%) | +20 🔼 |
| **Very Active** (≤ 7 days) | 112 (29.6%) | — |

*Changes since previous analysis*


### 🆕 Recent Additions

laterite_ags4, rawduck, qvd, tpch_rust, zim, dbn, duckton, salesforce, cache_httpfs, curl_httpfs *and 4 more*



### 🗑️ Removed

latency_injection, encoding, jemalloc



---
## Core Extensions

Core extensions maintained by the DuckDB team and distributed via the official extension repository

**Total:** 29 extensions

<details open markdown="1">
<summary>Click to expand/collapse core extensions table</summary>

| # | Extension | Repository | Status | Last Activity | Stars | Language | Description |
|---|-----------|------------|--------|---------------|-------|----------|-------------|
| 1 | [autocomplete](https://duckdb.org/docs/current/core_extensions/autocomplete) | [duckdb/duckdb](https://github.com/duckdb/duckdb/tree/main/extension/autocomplete) | 🟢 Ongoing | 4 days ago (2026-09-21 07:02:11 UTC) | N/A (part of core DuckDB repo) | C++ | Core DuckDB extension: autocomplete |
| 2 | [avro](https://duckdb.org/docs/current/core_extensions/avro) | [duckdb-avro](https://github.com/duckdb/duckdb-avro) | 🟢 Ongoing | today (2026-09-25 10:55:31 UTC) | 35 | C++ | Apache Avro format support |
| 3 | [aws](https://duckdb.org/docs/current/core_extensions/aws) | [duckdb-aws](https://github.com/duckdb/duckdb-aws) | 🟢 Ongoing | 2 days ago (2026-09-22 14:38:44 UTC) | 65 | C++ | AWS S3 integration |
| 4 | [azure](https://duckdb.org/docs/current/core_extensions/azure) | [duckdb-azure](https://github.com/duckdb/duckdb-azure) | 🟢 Ongoing | 10 days ago (2026-09-14 18:53:45 UTC) | 79 | C++ | Azure extension for DuckDB |
| 5 | [delta](https://duckdb.org/docs/current/core_extensions/delta) | [duckdb-delta](https://github.com/duckdb/duckdb-delta) | 🟢 Ongoing | today (2026-09-23 16:31:09 UTC) | 231 | C++ | DuckDB extension for Delta Lake |
| 6 | [ducklake](https://duckdb.org/docs/current/core_extensions/ducklake) | [duckdb/ducklake](https://github.com/duckdb/ducklake) | 🟢 Ongoing | 65 days ago | N/A (part of core DuckDB repo) | C++ | Delta Lake support via DuckLake (different from delta extension) |
| 7 | [encodings](https://duckdb.org/docs/current/core_extensions/encodings) | [duckdb-encodings](https://github.com/duckdb/duckdb-encodings) | 🟢 Ongoing | 28 days ago (2026-08-28 07:10:44 UTC) | 16 | C++ | Character encoding support |
| 8 | [excel](https://duckdb.org/docs/current/core_extensions/excel) | [duckdb-excel](https://github.com/duckdb/duckdb-excel) | 🟢 Ongoing | today (2026-09-25 10:38:52 UTC) | 62 | C++ | Excel extension for DuckDB |
| 9 | [fts](https://duckdb.org/docs/current/core_extensions/full_text_search) | [duckdb-fts](https://github.com/duckdb/duckdb-fts) | 🟢 Ongoing | 4 days ago (2026-09-21 09:16:27 UTC) | 44 | C++ | Full-text search functionality |
| 10 | [httpfs](https://duckdb.org/docs/current/core_extensions/httpfs/overview) | [duckdb-httpfs](https://github.com/duckdb/duckdb-httpfs) | 🟢 Ongoing | today (2026-09-25 10:52:58 UTC) | 60 | C++ | HTTP/S3 filesystem support |
| 11 | [iceberg](https://duckdb.org/docs/current/core_extensions/iceberg/overview) | [duckdb-iceberg](https://github.com/duckdb/duckdb-iceberg) | 🟢 Ongoing | today (2026-09-25 07:02:56 UTC) | 441 | C++ | Apache Iceberg format support |
| 12 | [icu](https://duckdb.org/docs/current/core_extensions/icu) | [duckdb/duckdb](https://github.com/duckdb/duckdb/tree/main/extension/icu) | 🟢 Ongoing | 2 days ago (2026-09-23 04:18:44 UTC) | N/A (part of core DuckDB repo) | C++ | Core DuckDB extension: icu |
| 13 | [inet](https://duckdb.org/docs/current/core_extensions/inet) | [duckdb-inet](https://github.com/duckdb/duckdb-inet) | 🟢 Ongoing | 18 days ago (2026-09-07 05:59:39 UTC) | 13 | C++ | Internet address data types |
| 14 | [json](https://duckdb.org/docs/current/data/json/overview) | [duckdb/duckdb](https://github.com/duckdb/duckdb/tree/main/extension/json) | 🟢 Ongoing | 2 days ago (2026-09-23 04:18:44 UTC) | N/A (part of core DuckDB repo) | C++ | Core DuckDB extension: json |
| 15 | [lance](https://duckdb.org/docs/current/core_extensions/lance) | [lance-duckdb](https://github.com/lance-format/lance-duckdb) | 🟢 Ongoing | today (2026-09-25 08:57:40 UTC) | 127 | C++ | The lance extensions for DuckDB enable reading and writing of lance tables. |
| 16 | [motherduck](https://duckdb.org/docs/current/core_extensions/motherduck) | [duckdb/duckdb](https://github.com/duckdb/duckdb) *(Third Party - Closed source - maintained by MotherDuck Inc.)* | 🟢 Ongoing | 65 days ago | N/A (part of core DuckDB repo) | C++ | Core DuckDB extension: motherduck |
| 17 | [mysql](https://duckdb.org/docs/current/core_extensions/mysql) | [duckdb-mysql](https://github.com/duckdb/duckdb-mysql) | 🟢 Ongoing | today (2026-09-25 09:55:24 UTC) | 102 | C++ | MySQL database connectivity |
| 18 | [odbc](https://duckdb.org/docs/current/core_extensions/odbc/overview) | [odbc-scanner](https://github.com/duckdb/odbc-scanner) | 🟢 Ongoing | 6 days ago (2026-09-19 11:12:52 UTC) | 40 | C++ | DuckDB ODBC extension |
| 19 | [parquet](https://duckdb.org/docs/current/data/parquet/overview) | [duckdb/duckdb](https://github.com/duckdb/duckdb/tree/main/extension/parquet) | 🟢 Ongoing | 2 days ago (2026-09-22 15:57:51 UTC) | N/A (part of core DuckDB repo) | C++ | Core DuckDB extension: parquet |
| 20 | [postgres](https://duckdb.org/docs/current/core_extensions/postgres/overview) | [duckdb-postgres](https://github.com/duckdb/duckdb-postgres) | 🟢 Ongoing | today (2026-09-24 08:07:54 UTC) | 372 | C++ | PostgreSQL database connectivity |
| 21 | [quack](https://duckdb.org/docs/current/core_extensions/quack) | [duckdb-quack](https://github.com/duckdb/duckdb-quack) | 🟢 Ongoing | today (2026-09-25 10:53:16 UTC) | 183 | C++ | Quack remote protocol |
| 22 | [spatial](https://duckdb.org/docs/current/core_extensions/spatial/overview) | [duckdb-spatial](https://github.com/duckdb/duckdb-spatial) | 🟢 Ongoing | 2 days ago (2026-09-22 15:54:05 UTC) | 712 | C++ | Geospatial data types and functions |
| 23 | [sqlite](https://duckdb.org/docs/current/core_extensions/sqlite) | [duckdb-sqlite](https://github.com/duckdb/duckdb-sqlite) | 🟢 Ongoing | today (2026-09-25 09:54:44 UTC) | 291 | C++ | DuckDB extension to read and write to SQLite databases |
| 24 | [tpcds](https://duckdb.org/docs/current/core_extensions/tpcds) | [duckdb/duckdb](https://github.com/duckdb/duckdb/tree/main/extension/tpcds) | 🟢 Ongoing | 4 days ago (2026-09-21 07:02:11 UTC) | N/A (part of core DuckDB repo) | C++ | Core DuckDB extension: tpcds |
| 25 | [tpch](https://duckdb.org/docs/current/core_extensions/tpch) | [duckdb/duckdb](https://github.com/duckdb/duckdb/tree/main/extension/tpch) | 🟢 Ongoing | 4 days ago (2026-09-21 07:02:11 UTC) | N/A (part of core DuckDB repo) | C++ | Core DuckDB extension: tpch |
| 26 | [ui](https://duckdb.org/docs/current/core_extensions/ui) | [duckdb-ui](https://github.com/duckdb/duckdb-ui) | 🟢 Ongoing | 56 days ago (2026-07-30 20:41:06 UTC) | 469 | C++ | Browser-based user interface for DuckDB |
| 27 | [unity_catalog](https://duckdb.org/docs/current/core_extensions/unity_catalog) | [unity_catalog](https://github.com/duckdb/unity_catalog) | 🟢 Ongoing | 7 days ago (2026-09-17 15:42:38 UTC) | 110 | C++ | Proof-of-concept extension combining the delta extension with Unity Catalog |
| 28 | [vortex](https://duckdb.org/docs/current/core_extensions/vortex) | [duckdb/duckdb](https://github.com/duckdb/duckdb) *(Third Party - Closed source - third-party extension)* | 🟢 Ongoing | 65 days ago | N/A (part of core DuckDB repo) | C++ | Core DuckDB extension: vortex |
| 29 | [vss](https://duckdb.org/docs/current/core_extensions/vss) | [duckdb-vss](https://github.com/duckdb/duckdb-vss) | 🟢 Ongoing | today (2026-09-25 10:39:38 UTC) | 267 | C++ | Vector similarity search |

</details>

---
---
## Community Extensions

Third-party extensions maintained by the community


**Total:** 350 extensions | 🔥 Very Active (≤7d): 112 | ✅ Active (≤30d): 92 | 🟡 Stable (≤90d): 58 | 🟠 Stale (>90d): 88

<details open markdown="1">
<summary>Click to expand/collapse community extensions table</summary>

| # | Extension | Repository | Status | Activity | Last Activity | Stars | Language | Description |
|---|-----------|------------|--------|----------|---------------|-------|----------|-------------|
| 1 | [a5](https://duckdb.org/community_extensions/extensions/a5.html) | [a5](https://github.com/Query-farm/a5) | 🟢 Ongoing | 2 - ✅ Active | 20 days ago (2026-09-04 20:18:14 UTC) | 17 | C++ | A5 Geospatial Extension for DuckDB |
| 2 | [acp](https://duckdb.org/community_extensions/extensions/acp.html) | [duckdb-acp](https://github.com/sidequery/duckdb-acp) | 🟡 Archived | 4 - 🟠 Stale | 288 days ago (2025-12-11 03:36:46 UTC) | 58 | Rust | Use Claude Code & other AI agents from inside DuckDB via extension |
| 3 | [adbc](https://duckdb.org/community_extensions/extensions/adbc.html) | [duckdb-adbc-client](https://github.com/columnar-tech/duckdb-adbc-client) | 🟢 Ongoing | 1 - 🔥 Very Active | 2 days ago (2026-09-22 18:01:24 UTC) | 48 | C++ | ADBC Client for DuckDB  |
| 4 | [adbc_scanner](https://duckdb.org/community_extensions/extensions/adbc_scanner.html) | [adbc_scanner](https://github.com/Query-farm/adbc_scanner) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-09-25 03:03:10 UTC) | 23 | C++ | A DuckDB ADBC Scanner Extension - adds support for using ADBC drivers with Du... |
| 5 | [agent_data](https://duckdb.org/community_extensions/extensions/agent_data.html) | [agent_data_duckdb](https://github.com/axsaucedo/agent_data_duckdb) | 🟢 Ongoing | 3 - 🟡 Stable | 55 days ago (2026-08-01 03:42:26 UTC) | 25 | Rust | DuckDB extension: agent_data by axsaucedo |
| 6 | [ai](https://duckdb.org/community_extensions/extensions/ai.html) | [duckdb-ai](https://github.com/leonardovida/duckdb-ai) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-09-25 09:43:18 UTC) | 12 | C++ | Enhance DuckDB with AI functions, supporting all providers as well as local m... |
| 7 | [airport](https://duckdb.org/community_extensions/extensions/airport.html) | [airport](https://github.com/Query-farm/airport) | 🟢 Ongoing | 2 - ✅ Active | 20 days ago (2026-09-04 20:18:25 UTC) | 350 | C++ | The Airport extension for DuckDB, enables the use of Arrow Flight with DuckDB |
| 8 | [aixchess](https://duckdb.org/community_extensions/extensions/aixchess.html) | [aix](https://github.com/thomas-daniels/aix) | 🟢 Ongoing | 4 - 🟠 Stale | 179 days ago (2026-03-29 12:16:27 UTC) | 28 | Rust | Aix: Efficiently storing and querying chess game collections |
| 9 | [altertable](https://duckdb.org/community_extensions/extensions/altertable.html) | [duckdb-altertable](https://github.com/altertable-ai/duckdb-altertable) | 🟢 Ongoing | 2 - ✅ Active | 22 days ago (2026-09-02 21:34:26 UTC) | 1 | C++ | Query Altertable's lakehouse directly from your local DuckDB |
| 10 | [anndata](https://duckdb.org/community_extensions/extensions/anndata.html) | [anndata-duckdb-extension](https://github.com/honicky/anndata-duckdb-extension) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-09-24 12:34:10 UTC) | 11 | C++ | Attach and AnnData file in duckdb and query it with SQL.  Perform SQL over gr... |
| 11 | [anofox_forecast](https://duckdb.org/community_extensions/extensions/anofox_forecast.html) | [anofox-forecast](https://github.com/DataZooDE/anofox-forecast) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-09-25 03:25:07 UTC) | 39 | C++ | Statistical timeseries forecasting in DuckDB |
| 12 | [anofox_optimize](https://duckdb.org/community_extensions/extensions/anofox_optimize.html) | [anofox-optimize](https://github.com/DataZooDE/anofox-optimize) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-09-23 15:43:48 UTC) | 3 | C++ | Combinatorial decision algorithms as DuckDB functions — bin packing, knapsack... |
| 13 | [anofox_scenario](https://duckdb.org/community_extensions/extensions/anofox_scenario.html) | [anofox-scenario](https://github.com/DataZooDE/anofox-scenario) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-09-23 15:43:53 UTC) | 4 | C++ | DuckDB extension for Git-like database branching. Create isolated scenarios f... |
| 14 | [anofox_similarity](https://duckdb.org/community_extensions/extensions/anofox_similarity.html) | [anofox-similarity](https://github.com/DataZooDE/anofox-similarity) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-09-24 03:41:34 UTC) | 3 | C++ | DuckDB extension for multi-modal product similarity for manufacturing supply... |
| 15 | [anofox_statistics](https://duckdb.org/community_extensions/extensions/anofox_statistics.html) | [anofox-statistics](https://github.com/DataZooDE/anofox-statistics) | 🟢 Ongoing | 1 - 🔥 Very Active | 6 days ago (2026-09-18 19:42:48 UTC) | 15 | C++ | A DuckDB extension for statistical regression analysis, providing OLS, Ridge,... |
| 16 | [anofox_tabfm](https://duckdb.org/community_extensions/extensions/anofox_tabfm.html) | [anofox-tabfm](https://github.com/DataZooDE/anofox-tabfm) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-09-25 09:46:28 UTC) | 9 | C++ | DuckDB extension for tabular foundation models — zero-shot classification & r... |
| 17 | [anofox_tabular](https://duckdb.org/community_extensions/extensions/anofox_tabular.html) | [anofox-tabular](https://github.com/DataZooDE/anofox-tabular) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-09-25 03:25:11 UTC) | 19 | C++ | A duckdb extension which combines data quality and data preparation tools for... |
| 18 | [anofox_visualization](https://duckdb.org/community_extensions/extensions/anofox_visualization.html) | [anofox-visualization](https://github.com/DataZooDE/anofox-visualization) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-09-24 03:41:41 UTC) | 5 | Rust | Charts & dashboards for DuckDB — the grammar of graphics, straight from SQL.... |
| 19 | [apart](https://duckdb.org/community_extensions/extensions/apart.html) | [apart](https://github.com/jokasimr/apart) | 🟢 Ongoing | 2 - ✅ Active | 11 days ago (2026-09-13 15:56:34 UTC) | 0 | C++ | DuckDB extension for evaluating oblique decision trees. |
| 20 | [arrow](https://duckdb.org/community_extensions/extensions/arrow.html) | [duckdb-extension-alias](https://github.com/duckdb/duckdb-extension-alias) | ❓ Unknown | 4 - 🟠 Stale | 354 days ago (2025-10-06 09:07:38 UTC) | 4 | C | DuckDB extension: arrow |
| 21 | [astro](https://duckdb.org/community_extensions/extensions/astro.html) | [astro-duck](https://github.com/synapticore-io/astro-duck) | 🟢 Ongoing | 4 - 🟠 Stale | 128 days ago (2026-05-19 12:22:23 UTC) | 4 | C++ | 60+ astronomical SQL functions for DuckDB: coordinate transforms, CCM89 dust... |
| 22 | [azure_wasm](https://github.com/HynekBlaha/duckdb-azure-wasm) | [duckdb-azure-wasm](https://github.com/HynekBlaha/duckdb-azure-wasm) | ❓ Unknown | 3 - 🟡 Stable | 38 days ago (2026-08-18 09:37:10 UTC) | 0 | C++ | Cloud platform integration extension by HynekBlaha |
| 23 | [behavioral](https://duckdb.org/community_extensions/extensions/behavioral.html) | [duckdb-behavioral](https://github.com/tomtom215/duckdb-behavioral) | 🟢 Ongoing | 3 - 🟡 Stable | 31 days ago (2026-08-24 18:45:09 UTC) | 15 | Rust | A DuckDB Community Extension to enable Behavioral Analytics, inspired by Clic... |
| 24 | [bigquery](https://duckdb.org/community_extensions/extensions/bigquery.html) | [duckdb-bigquery](https://github.com/hafenkran/duckdb-bigquery) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-09-23 16:21:39 UTC) | 171 | C++ | Integrates DuckDB with Google BigQuery, allowing direct querying and manageme... |
| 25 | [bitfilters](https://duckdb.org/community_extensions/extensions/bitfilters.html) | [bitfilters](https://github.com/Query-farm/bitfilters) | 🟢 Ongoing | 2 - ✅ Active | 20 days ago (2026-09-04 20:18:32 UTC) | 10 | C++ | A high-performance DuckDB extension providing probabilistic data structures f... |
| 26 | [blockduck](https://duckdb.org/community_extensions/extensions/blockduck.html) | [BlockDuck](https://github.com/luohaha/BlockDuck) | 🟢 Ongoing | 4 - 🟠 Stale | 351 days ago (2025-10-08 16:19:04 UTC) | 11 | C++ | Live SQL Queries on Blockchain |
| 27 | [boilstream](https://duckdb.org/community_extensions/extensions/boilstream.html) | [boilstream-extension](https://github.com/dforsber/boilstream-extension) | 🟢 Ongoing | 2 - ✅ Active | 12 days ago (2026-09-13 07:04:56 UTC) | 11 | C++ | Secure Remote Secrets Storage for DuckDB |
| 28 | [brew](https://duckdb.org/community_extensions/extensions/brew.html) | [duckdb-brew](https://github.com/adriens/duckdb-brew) | 🟢 Ongoing | 4 - 🟠 Stale | 117 days ago (2026-05-31 08:18:52 UTC) | 2 | C++ | duckdb extension to report installed brew packages/casks/formulas with SQL |
| 29 | [bvh2sql](https://duckdb.org/community_extensions/extensions/bvh2sql.html) | [bvh2sql](https://github.com/nkwork9999/bvh2sql) | 🟢 Ongoing | 4 - 🟠 Stale | 104 days ago (2026-06-12 12:17:09 UTC) | 1 | Makefile | SQL-related extension by nkwork9999 |
| 30 | [cache_httpfs](https://duckdb.org/community_extensions/extensions/cache_httpfs.html) | [duck-read-cache-fs](https://github.com/dentiny/duck-read-cache-fs) | 🟢 Ongoing | 1 - 🔥 Very Active | 3 days ago (2026-09-22 04:13:42 UTC) | 152 | C++ | This repository is made as read-only filesystem for remote access. |
| 31 | [cache_prewarm](https://duckdb.org/community_extensions/extensions/cache_prewarm.html) | [duckdb-cache-prewarm](https://github.com/dentiny/duckdb-cache-prewarm) | 🟢 Ongoing | 1 - 🔥 Very Active | 3 days ago (2026-09-22 10:47:23 UTC) | 11 | C++ | DuckDB extension: cache_prewarm by dentiny |
| 32 | [capi_quack](https://duckdb.org/community_extensions/extensions/capi_quack.html) | [extension-template-c](https://github.com/duckdb/extension-template-c) | ❓ Unknown | 3 - 🟡 Stable | 63 days ago (2026-07-24 09:22:27 UTC) | 32 | C | (Experimental) C/C++ template for DuckDB extensions based on the C API |
| 33 | [cassandra](https://duckdb.org/community_extensions/extensions/cassandra.html) | [duckdb-cassandra](https://github.com/dioptre/duckdb-cassandra) | ❓ Unknown | 4 - 🟠 Stale | 339 days ago (2025-10-20 19:15:10 UTC) | 2 | C++ | DuckDB Connector for Cassandra |
| 34 | [celestial](https://duckdb.org/community_extensions/extensions/celestial.html) | [duckdb-celestial](https://github.com/lisa-sgs/duckdb-celestial) | 🟢 Ongoing | 3 - 🟡 Stable | 49 days ago (2026-08-06 12:40:03 UTC) | 3 | C++ | DuckDB extension providing astronomical coordinates utilities |
| 35 | [chaos](https://duckdb.org/community_extensions/extensions/chaos.html) | [duckdb-chaos](https://github.com/taniabogatsch/duckdb-chaos) | 🟢 Ongoing | 4 - 🟠 Stale | 224 days ago (2026-02-12 14:50:01 UTC) | 2 | C++ | DuckDB extension: chaos by taniabogatsch |
| 36 | [chess](https://duckdb.org/community_extensions/extensions/chess.html) | [duckdb-chess](https://github.com/dotneB/duckdb-chess) | ❓ Unknown | 4 - 🟠 Stale | 120 days ago (2026-05-28 05:13:34 UTC) | 3 | Rust | A DuckDB extension for parsing and analyzing chess games in PGN format. |
| 37 | [chsql](https://duckdb.org/community_extensions/extensions/chsql.html) | [clickhouse-sql](https://github.com/Query-farm/clickhouse-sql) | ❓ Unknown | 2 - ✅ Active | 20 days ago (2026-09-04 12:02:56 UTC) | 94 | C++ | DuckDB Community Extension implementing ClickHouse SQL Dialect macros and Cus... |
| 38 | [chsql_native](https://duckdb.org/community_extensions/extensions/chsql_native.html) | [clickhouse-native](https://github.com/Query-farm/clickhouse-native) | 🟢 Ongoing | 2 - ✅ Active | 20 days ago (2026-09-04 12:03:09 UTC) | 22 | Rust | Experimental ClickHouse Native Client and Native file reader Extension for Du... |
| 39 | [cityjson](https://duckdb.org/community_extensions/extensions/cityjson.html) | [duckdb-cityjson](https://github.com/cityjson/duckdb-cityjson) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-09-25 09:15:43 UTC) | 11 | C++ | (Experimental) DuckDB extension for CityJSON |
| 40 | [clamp](https://duckdb.org/community_extensions/extensions/clamp.html) | [duckdb_clamp](https://github.com/oglego/duckdb_clamp) | 🟢 Ongoing | 2 - ✅ Active | 25 days ago (2026-08-30 19:46:00 UTC) | 2 | C++ | The Clamp extension introduces range-clamping scalar functions to DuckDB. Ini... |
| 41 | [cloudfront](https://duckdb.org/community_extensions/extensions/cloudfront.html) | [duckdb-cloudfront](https://github.com/midwork-finds-jobs/duckdb-cloudfront) | 🟢 Ongoing | 4 - 🟠 Stale | 231 days ago (2026-02-05 15:32:51 UTC) | 2 | C++ | DuckDB module which provides custom authentication methods on top of httpfs m... |
| 42 | [cloudfs](https://duckdb.org/community_extensions/extensions/cloudfs.html) | [cloudfs](https://github.com/trouchet/cloudfs) | ❓ Unknown | 1 - 🔥 Very Active | 3 days ago (2026-09-21 19:00:26 UTC) | 3 | C++ | A duckdb-based cloud filesystem query engine |
| 43 | [cloudwatch](https://duckdb.org/community_extensions/extensions/cloudwatch.html) | [duckdb-cloudwatch](https://github.com/smithclay/duckdb-cloudwatch) | 🟢 Ongoing | 3 - 🟡 Stable | 44 days ago (2026-08-11 17:17:46 UTC) | 2 | C++ | query cloudwatch telemetry (metrics, logs) from duckdb  |
| 44 | [cog](https://duckdb.org/community_extensions/extensions/cog.html) | [duckdb-cog](https://github.com/st-layer/duckdb-cog) | 🟢 Ongoing | 2 - ✅ Active | 30 days ago (2026-08-26 09:35:50 UTC) | 4 | Rust | GDAL-free COG raster access for DuckDB. Query Cloud-Optimized GeoTIFFs in pla... |
| 45 | [compression_fs](https://github.com/dentiny/duckdb-compression-filesystem) | [duckdb-compression-filesystem](https://github.com/dentiny/duckdb-compression-filesystem) | ❓ Unknown | 2 - ✅ Active | 12 days ago (2026-09-13 01:49:16 UTC) | 1 | C++ | DuckDB extension: compression_fs by dentiny |
| 46 | [cozip](https://duckdb.org/community_extensions/extensions/cozip.html) | [cozip_reader](https://github.com/asterisk-labs/cozip_reader) | 🟢 Ongoing | 2 - ✅ Active | 10 days ago (2026-09-15 04:21:41 UTC) | 8 | C++ | Read Cloud-Optimized ZIP files |
| 47 | [crawler](https://duckdb.org/community_extensions/extensions/crawler.html) | [duckdb-crawler](https://github.com/midwork-finds-jobs/duckdb-crawler) | 🟢 Ongoing | 1 - 🔥 Very Active | 3 days ago (2026-09-22 08:29:58 UTC) | 16 | C++ | DuckDB extension: crawler by midwork-finds-jobs |
| 48 | [cronjob](https://duckdb.org/community_extensions/extensions/cronjob.html) | [cronjob](https://github.com/Query-farm/cronjob) | 🟢 Ongoing | 2 - ✅ Active | 20 days ago (2026-09-04 20:18:47 UTC) | 55 | C++ | DuckDB CronJob Extension |
| 49 | [crypto](https://duckdb.org/community_extensions/extensions/crypto.html) | [crypto](https://github.com/Query-farm/crypto) | 🟢 Ongoing | 2 - ✅ Active | 20 days ago (2026-09-04 20:18:52 UTC) | 31 | C++ | DuckDB Extension for cryptographic hash functions and HMAC |
| 50 | [curl_httpfs](https://duckdb.org/community_extensions/extensions/curl_httpfs.html) | [duckdb-curl-filesystem](https://github.com/dentiny/duckdb-curl-filesystem) | 🟢 Ongoing | 1 - 🔥 Very Active | 3 days ago (2026-09-22 08:46:10 UTC) | 13 | C++ | Filesystem built upon libcurl. |
| 51 | [cwiqduck](https://duckdb.org/community_extensions/extensions/cwiqduck.html) | [cwiqduck](https://github.com/cwiq-os/cwiqduck) | 🟢 Ongoing | 4 - 🟠 Stale | 99 days ago (2026-06-18 04:35:52 UTC) | 3 | C++ | DuckDB extensions for CWIQ |
| 52 | [dash](https://duckdb.org/community_extensions/extensions/dash.html) | [dash](https://github.com/gropaul/dash) | 🟢 Ongoing | 2 - ✅ Active | 21 days ago (2026-09-04 08:50:15 UTC) | 106 | C++ | Local GUI and Data Canvas as a DuckDB extension |
| 53 | [datadog](https://duckdb.org/community_extensions/extensions/datadog.html) | [duckdb-datadog](https://github.com/smithclay/duckdb-datadog) | 🟢 Ongoing | 3 - 🟡 Stable | 44 days ago (2026-08-11 17:17:28 UTC) | 3 | C++ | ingest logs and metrics (and soon traces) from datadog into duckdb |
| 54 | [datasketches](https://duckdb.org/community_extensions/extensions/datasketches.html) | [datasketches](https://github.com/Query-farm/datasketches) | 🟢 Ongoing | 2 - ✅ Active | 11 days ago (2026-09-13 18:44:42 UTC) | 53 | C++ | Integrates DuckDB with the high-performance Apache DataSketches library. This... |
| 55 | [dazzleduck](https://duckdb.org/community_extensions/extensions/dazzleduck.html) | [dazzleduck-sql-duckdb](https://github.com/dazzleduck-web/dazzleduck-sql-duckdb) | ❓ Unknown | 4 - 🟠 Stale | 196 days ago (2026-03-12 22:24:42 UTC) | 1 | C++ | DuckDB extension: dazzleduck by dazzleduck-web |
| 56 | [dbn](https://duckdb.org/community_extensions/extensions/dbn.html) | [duckdb-dbn](https://github.com/tbeason/duckdb-dbn) | ❓ Unknown | 2 - ✅ Active | 16 days ago (2026-09-08 20:19:45 UTC) | 1 | C++ | DuckDB extension for reading Databento Binary Encoding (DBN) files |
| 57 | [decimal_arithmetic](https://duckdb.org/community_extensions/extensions/decimal_arithmetic.html) | [duckdb-decimal-arithmetic](https://github.com/duckdb/duckdb-decimal-arithmetic) | 🟢 Ongoing | 3 - 🟡 Stable | 78 days ago (2026-07-09 10:55:37 UTC) | 6 | C++ | DuckDB extension: decimal_arithmetic |
| 58 | [deferred_columns](https://duckdb.org/community_extensions/extensions/deferred_columns.html) | [deferred-columns](https://github.com/iwinalbert/deferred-columns) | ❓ Unknown | 3 - 🟡 Stable | 74 days ago (2026-07-12 17:08:25 UTC) | 3 | C++ | DuckDB extension: deferred_columns by iwinalbert |
| 59 | [delta_classic](https://duckdb.org/community_extensions/extensions/delta_classic.html) | [delta_classic](https://github.com/djouallah/delta_classic) | 🟢 Ongoing | 4 - 🟠 Stale | 97 days ago (2026-06-19 15:04:33 UTC) | 6 | C++ | DuckDB extension to attach a directory of Delta tables as a database |
| 60 | [delta_export](https://duckdb.org/community_extensions/extensions/delta_export.html) | [delta_export](https://github.com/djouallah/delta_export) | 🟢 Ongoing | 2 - ✅ Active | 11 days ago (2026-09-14 10:06:15 UTC) | 10 | C++ | DuckDB extension to export Delta Lake metadata from DuckLake |
| 61 | [dicom](https://duckdb.org/community_extensions/extensions/dicom.html) | [duck-dicom](https://github.com/nmontesg/duck-dicom) | 🟢 Ongoing | 1 - 🔥 Very Active | 6 days ago (2026-09-19 07:32:22 UTC) | 1 | C++ | A DuckDB extension to import medical imaging data |
| 62 | [dns](https://duckdb.org/community_extensions/extensions/dns.html) | [duckdb-dns](https://github.com/tobilg/duckdb-dns) | 🟢 Ongoing | 3 - 🟡 Stable | 49 days ago (2026-08-07 11:04:08 UTC) | 18 | Rust | DNS (Reverse) Lookup Extension for DuckDB |
| 63 | [documentdb](https://duckdb.org/community_extensions/extensions/documentdb.html) | [duckdb-documentdb](https://github.com/documentdb/duckdb-documentdb) | 🟢 Ongoing | 2 - ✅ Active | 25 days ago (2026-08-31 04:51:48 UTC) | 1 | C++ | Integrates DuckDB with DocumentDB, enabling direct SQL queries over DocumentD... |
| 64 | [dplyr](https://duckdb.org/community_extensions/extensions/dplyr.html) | [libdplyr](https://github.com/mrchypark/libdplyr) | 🟢 Ongoing | 2 - ✅ Active | 26 days ago (2026-08-30 05:20:46 UTC) | 16 | Rust | DuckDB extension: dplyr by mrchypark |
| 65 | [dq](https://duckdb.org/community_extensions/extensions/dq.html) | [duckdb_dq](https://github.com/alitrack/duckdb_dq) | 🟢 Ongoing | 2 - ✅ Active | 25 days ago (2026-08-31 06:11:56 UTC) | 4 | Rust | Data quality assertion framework for DuckDB — SQL-native expect_* rules, prof... |
| 66 | [dqtest](https://duckdb.org/community_extensions/extensions/dqtest.html) | [duckdb-dataquality-extension](https://github.com/vhe74/duckdb-dataquality-extension) | ❓ Unknown | 4 - 🟠 Stale | 233 days ago (2026-02-03 18:35:04 UTC) | 5 | C++ | Duckdb extension to run data quality tests |
| 67 | [dryrun](https://duckdb.org/community_extensions/extensions/dryrun.html) | [duckdb-dryrun](https://github.com/aleda145/duckdb-dryrun) | ❓ Unknown | 4 - 🟠 Stale | 95 days ago (2026-06-21 19:06:20 UTC) | 0 | C++ | dry run before execute |
| 68 | [dta](https://duckdb.org/community_extensions/extensions/dta.html) | [duckdb-dta](https://github.com/codedthinking/duckdb-dta) | 🟢 Ongoing | 3 - 🟡 Stable | 77 days ago (2026-07-10 08:57:32 UTC) | 2 | C++ | DuckDB extension for reading and writing .dta files (formats 117-121) |
| 69 | [duck_block_utils](https://duckdb.org/community_extensions/extensions/duck_block_utils.html) | [duckdb_duck_block_utils](https://github.com/teaguesterling/duckdb_duck_block_utils) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-09-24 19:48:40 UTC) | 2 | C++ | A collection of utility functions to work with doc block-style structures and... |
| 70 | [duck_delta_share](https://duckdb.org/community_extensions/extensions/duck_delta_share.html) | [duck_delta_share](https://github.com/cwiq-os/duck_delta_share) | 🟢 Ongoing | 4 - 🟠 Stale | 137 days ago (2026-05-10 23:39:27 UTC) | 6 | C++ | DuckDB extension for enabling Delta Sharing client capabilities.  |
| 71 | [duck_dggs](https://duckdb.org/community_extensions/extensions/duck_dggs.html) | [duckdb-dggs](https://github.com/am2222/duckdb-dggs) | 🟢 Ongoing | 1 - 🔥 Very Active | 2 days ago (2026-09-22 21:17:20 UTC) | 2 | C++ | A DuckDB extension for discrete global grid systems (DGGS) powered by DGGRID v8. |
| 72 | [duck_diff](https://duckdb.org/community_extensions/extensions/duck_diff.html) | [duck_diff](https://github.com/avaitla/duck_diff) | 🟢 Ongoing | 3 - 🟡 Stable | 38 days ago (2026-08-17 22:32:33 UTC) | 8 | HTML | Diff any two database tables |
| 73 | [duck_geoarrow](https://duckdb.org/community_extensions/extensions/duck_geoarrow.html) | [duck_geoarrow](https://github.com/am2222/duck_geoarrow) | 🟢 Ongoing | 1 - 🔥 Very Active | 2 days ago (2026-09-22 20:08:53 UTC) | 9 | C++ | This extension, Duck_Geoarrow, provides functions to convert between WKB (Wel... |
| 74 | [duck_hunt](https://duckdb.org/community_extensions/extensions/duck_hunt.html) | [duck_hunt](https://github.com/teaguesterling/duck_hunt) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-09-23 15:53:03 UTC) | 8 | C++ | Tools for working with unit test suite results |
| 75 | [duck_lineage](https://duckdb.org/community_extensions/extensions/duck_lineage.html) | [duck_lineage](https://github.com/ilum-cloud/duck_lineage) | 🟢 Ongoing | 1 - 🔥 Very Active | 7 days ago (2026-09-17 17:04:51 UTC) | 80 | Python | A extension for DuckDB, which captures lineage events for executed queries |
| 76 | [duck_lk](https://duckdb.org/community_extensions/extensions/duck_lk.html) | [duck-lk](https://github.com/nrminor/duck-lk) | ❓ Unknown | 4 - 🟠 Stale | 160 days ago (2026-04-18 03:05:52 UTC) | 0 | Rust | Interact with tables from your LabKey LIMS natively in DuckDB |
| 77 | [duck_tails](https://duckdb.org/community_extensions/extensions/duck_tails.html) | [duck_tails](https://github.com/teaguesterling/duck_tails) | 🟢 Ongoing | 1 - 🔥 Very Active | 4 days ago (2026-09-21 01:28:12 UTC) | 26 | C++ | A DuckDB extension for exploring and reading git history. |
| 78 | [duckdb_delta_sharing](https://duckdb.org/community_extensions/extensions/duckdb_delta_sharing.html) | [duckdb-delta-sharing](https://github.com/prequel-co/duckdb-delta-sharing) | 🟢 Ongoing | 2 - ✅ Active | 22 days ago (2026-09-02 18:56:13 UTC) | 5 | C++ | An extension for using DuckDB as a delta sharing client |
| 79 | [duckdb_geoip_rs](https://duckdb.org/community_extensions/extensions/duckdb_geoip_rs.html) | [duckdb-geoip-rs](https://github.com/william-billaud/duckdb-geoip-rs) | 🟢 Ongoing | 3 - 🟡 Stable | 59 days ago (2026-07-27 19:41:57 UTC) | 10 | Rust | Database connectivity extension by william-billaud |
| 80 | [duckdb_mcp](https://duckdb.org/community_extensions/extensions/duckdb_mcp.html) | [duckdb_mcp](https://github.com/teaguesterling/duckdb_mcp) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-09-24 16:21:09 UTC) | 66 | C++ | A simple MCP server extension for DuckDB |
| 81 | [duckdb_midi](https://github.com/nkwork9999/duckdb-midi) | [duckdb-midi](https://github.com/nkwork9999/duckdb-midi) | ❓ Unknown | 4 - 🟠 Stale | 104 days ago (2026-06-12 12:18:36 UTC) | 0 | C++ | Database connectivity extension by nkwork9999 |
| 82 | [duckdb_opendalfs](https://duckdb.org/community_extensions/extensions/duckdb_opendalfs.html) | [duckdb-opendal-filesystem](https://github.com/dentiny/duckdb-opendal-filesystem) | 🟢 Ongoing | 3 - 🟡 Stable | 53 days ago (2026-08-03 08:42:36 UTC) | 7 | C++ | Database connectivity extension by dentiny |
| 83 | [duckdb_rdkit](https://duckdb.org/community_extensions/extensions/duckdb_rdkit.html) | [duckdb_rdkit](https://github.com/bodowd/duckdb_rdkit) | 🟢 Ongoing | 3 - 🟡 Stable | 33 days ago (2026-08-22 17:45:05 UTC) | 15 | C++ | Database connectivity extension by bodowd |
| 84 | [duckdb_rphonetic](https://duckdb.org/community_extensions/extensions/duckdb_rphonetic.html) | [duckdb_rphonetic](https://github.com/guizmaii-opensource/duckdb_rphonetic) | 🟢 Ongoing | 2 - ✅ Active | 22 days ago (2026-09-03 08:41:18 UTC) | 1 | Rust | DuckDB extension bringing various phonetic algorithms |
| 85 | [duckdbi](https://duckdb.org/community_extensions/extensions/duckdbi.html) | [DuckDBI](https://github.com/nkwork9999/DuckDBI) | ❓ Unknown | 4 - 🟠 Stale | 195 days ago (2026-03-14 11:04:19 UTC) | 5 | C++ | Database connectivity extension by nkwork9999 |
| 86 | [duckflight](https://duckdb.org/community_extensions/extensions/duckflight.html) | [duckflight-extension](https://github.com/sidequery/duckflight-extension) | 🟢 Ongoing | 1 - 🔥 Very Active | 3 days ago (2026-09-21 23:19:42 UTC) | 12 | Python | A Postgres wire protocol + Arrow Flight server for DuckDB as an extension |
| 87 | [duckfn_quantstats](https://github.com/shijianjs/duckfn-quantstats) | [duckfn-quantstats](https://github.com/shijianjs/duckfn-quantstats) | ❓ Unknown | 1 - 🔥 Very Active | 2 days ago (2026-09-23 10:32:48 UTC) | 0 | Rust | A DuckDB extension that wraps https://crates.io/crates/quantstats-rs. |
| 88 | [duckgl](https://duckdb.org/community_extensions/extensions/duckgl.html) | [duckgl](https://github.com/nkwork9999/duckgl) | 🟢 Ongoing | 4 - 🟠 Stale | 204 days ago (2026-03-04 16:41:20 UTC) | 8 | C++ | DuckDB extension: duckgl by nkwork9999 |
| 89 | [duckgql](https://duckdb.org/community_extensions/extensions/duckgql.html) | [duckdb-gql](https://github.com/rahul-iyer/duckdb-gql) | 🟢 Ongoing | 2 - ✅ Active | 19 days ago (2026-09-05 21:06:25 UTC) | 52 | C++ | An extension to run graph queries and algorithms using ISO GQL |
| 90 | [duckherder](https://duckdb.org/community_extensions/extensions/duckherder.html) | [duckdb-distributed-execution](https://github.com/dentiny/duckdb-distributed-execution) | 🟢 Ongoing | 1 - 🔥 Very Active | 3 days ago (2026-09-22 08:40:31 UTC) | 64 | C++ | Distributed execution for duckdb queries. |
| 91 | [duckhog](https://duckdb.org/community_extensions/extensions/duckhog.html) | [duckhog](https://github.com/PostHog/duckhog) | ❓ Unknown | 4 - 🟠 Stale | 91 days ago (2026-06-26 00:52:18 UTC) | 13 | C++ | duckdb extension to connect to posthog managed data warehouse  |
| 92 | [duckhts](https://duckdb.org/community_extensions/extensions/duckhts.html) | [duckhts](https://github.com/RGenomicsETL/duckhts) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-09-24 21:44:08 UTC) | 18 | C | 'htslib' based 'Duckdb' Extenstion for High Throughput Sequencing File Formats |
| 93 | [ducklake_cdc](https://duckdb.org/community_extensions/extensions/ducklake_cdc.html) | [ducklake-cdc-extension](https://github.com/elei-io/ducklake-cdc-extension) | 🟢 Ongoing | 2 - ✅ Active | 17 days ago (2026-09-07 15:12:39 UTC) | 18 | C++ | The missing operational layer for DuckLake’s change feed. |
| 94 | [ducklink](https://duckdb.org/community_extensions/extensions/ducklink.html) | [ducklink-extension](https://github.com/tegmentum/ducklink-extension) | ❓ Unknown | 1 - 🔥 Very Active | today (2026-09-24 19:15:39 UTC) | 2 | Rust | Run duckdb:extension WebAssembly components inside DuckDB (community extension) |
| 95 | [ducknng](https://github.com/RGenomicsETL/ducknng) | [ducknng](https://github.com/RGenomicsETL/ducknng) | ❓ Unknown | 1 - 🔥 Very Active | 2 days ago (2026-09-22 15:25:13 UTC) | 3 | C | ducknng: a 'DuckDB' Binding To The 'NNG' Scalability Protocols Library And an... |
| 96 | [duckorch](https://duckdb.org/community_extensions/extensions/duckorch.html) | [duck-orch](https://github.com/nkwork9999/duck-orch) | 🟢 Ongoing | 2 - ✅ Active | 20 days ago (2026-09-05 05:19:02 UTC) | 3 | Rust | DuckDB extension: duckorch by nkwork9999 |
| 97 | [duckpgq](https://duckdb.org/community_extensions/extensions/duckpgq.html) | [duckpgq-extension](https://github.com/cwida/duckpgq-extension) | ❓ Unknown | 2 - ✅ Active | 8 days ago (2026-09-17 10:06:45 UTC) | 499 | C++ | DuckDB extension that adds support for SQL/PGQ and graph algorithms |
| 98 | [duckrouting](https://duckdb.org/community_extensions/extensions/duckrouting.html) | [duckrouting](https://github.com/am2222/duckrouting) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-09-24 11:48:04 UTC) | 3 | C++ | BOOSTGraph algorithms for duckdb |
| 99 | [ducksmiles](https://duckdb.org/community_extensions/extensions/ducksmiles.html) | [duckSMILES](https://github.com/nkwork9999/duckSMILES) | 🟢 Ongoing | 2 - ✅ Active | 19 days ago (2026-09-05 12:51:09 UTC) | 3 | Rust | DuckDB extension: ducksmiles by nkwork9999 |
| 100 | [ducksync](https://duckdb.org/community_extensions/extensions/ducksync.html) | [ducksync](https://github.com/danjsiegel/ducksync) | 🟢 Ongoing | 2 - ✅ Active | 16 days ago (2026-09-09 01:47:15 UTC) | 8 | C++ | DuckDB extension: ducksync by danjsiegel |
| 101 | [duckthink](https://duckdb.org/community_extensions/extensions/duckthink.html) | [duckthink](https://github.com/pedro-filardi/duckthink) | ❓ Unknown | 3 - 🟡 Stable | 80 days ago (2026-07-06 15:22:58 UTC) | 0 | C++ | ASK() — natural-language SQL for DuckDB, grounded in your dbt Semantic Layer |
| 102 | [ducktinycc](https://duckdb.org/community_extensions/extensions/ducktinycc.html) | [DuckTinyCC](https://github.com/sounkou-bioinfo/DuckTinyCC) | 🟢 Ongoing | 3 - 🟡 Stable | 40 days ago (2026-08-15 17:55:49 UTC) | 4 | C | 'C' Scripting in 'Duckdb' using 'TinyCC' |
| 103 | [duckton](https://duckdb.org/community_extensions/extensions/duckton.html) | [duckton](https://github.com/Angelerator/duckton) | ❓ Unknown | 4 - 🟠 Stale | 91 days ago (2026-06-25 22:07:12 UTC) | 5 | Rust | Duckton — a peer-to-peer distributed DuckDB compute grid over QUIC: broadcast... |
| 104 | [dynamodb](https://duckdb.org/community_extensions/extensions/dynamodb.html) | [duckdb-dynamodb](https://github.com/lukaswelsch/duckdb-dynamodb) | 🟢 Ongoing | 2 - ✅ Active | 22 days ago (2026-09-03 08:40:58 UTC) | 4 | C++ | Database connectivity extension by lukaswelsch |
| 105 | [eeagrid](https://duckdb.org/community_extensions/extensions/eeagrid.html) | [duckdb-eeagrid](https://github.com/ahuarte47/duckdb-eeagrid) | 🟢 Ongoing | 2 - ✅ Active | 25 days ago (2026-08-31 08:18:04 UTC) | 2 | C++ | Functions for transforming XY coordinates to and from the EEA Reference Grid... |
| 106 | [eenddb](https://duckdb.org/community_extensions/extensions/eenddb.html) | [eenddb](https://github.com/Dtenwolde/eenddb) | 🟢 Ongoing | 4 - 🟠 Stale | 178 days ago (2026-03-31 09:31:58 UTC) | 6 | C++ | Database connectivity extension by Dtenwolde |
| 107 | [elasticsearch](https://duckdb.org/community_extensions/extensions/elasticsearch.html) | [duckdb-elasticsearch](https://github.com/tlinhart/duckdb-elasticsearch) | ❓ Unknown | 4 - 🟠 Stale | 148 days ago (2026-04-29 13:01:51 UTC) | 23 | C++ | Query Elasticsearch data directly from DuckDB |
| 108 | [erpl_idoc](https://duckdb.org/community_extensions/extensions/erpl_idoc.html) | [erpl-idoc](https://github.com/DataZooDE/erpl-idoc) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-09-23 15:44:10 UTC) | 3 | C++ | Read & write SAP IDoc files (flat + IDoc-XML) as SQL in DuckDB — a community... |
| 109 | [erpl_tunnel](https://duckdb.org/community_extensions/extensions/erpl_tunnel.html) | [erpl-tunnel](https://github.com/DataZooDE/erpl-tunnel) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-09-23 16:45:17 UTC) | 4 | C++ | Zero-dependency DuckDB extension: tunnel raw TCP (quack, SAP RFC, HTTP) over... |
| 110 | [erpl_web](https://duckdb.org/community_extensions/extensions/erpl_web.html) | [erpl-web](https://github.com/DataZooDE/erpl-web) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-09-25 03:25:18 UTC) | 31 | C++ | ERPL is a DuckDB extension to connect to API based ecosystems via standard in... |
| 111 | [eurostat](https://duckdb.org/community_extensions/extensions/eurostat.html) | [duckdb-eurostat](https://github.com/ahuarte47/duckdb-eurostat) | 🟢 Ongoing | 2 - ✅ Active | 21 days ago (2026-09-04 06:45:32 UTC) | 35 | C++ | DuckDB extension for reading data from EUROSTAT database using SQL  |
| 112 | [evalexpr_rhai](https://duckdb.org/community_extensions/extensions/evalexpr_rhai.html) | [evalexpr_rhai](https://github.com/Query-farm/evalexpr_rhai) | 🟢 Ongoing | 2 - ✅ Active | 20 days ago (2026-09-04 20:19:10 UTC) | 27 | C++ | A DuckDB extension to evaluate the Rhai scripting language as part of SQL. |
| 113 | [events](https://duckdb.org/community_extensions/extensions/events.html) | [events](https://github.com/Query-farm/events) | ❓ Unknown | 2 - ✅ Active | 20 days ago (2026-09-04 20:19:17 UTC) | 3 | C++ | Capture database events and deliver JSON notifications to external programs v... |
| 114 | [faiss](https://duckdb.org/community_extensions/extensions/faiss.html) | [duckdb-faiss-ext](https://github.com/duckdb-faiss-ext/duckdb-faiss-ext) | 🟢 Ongoing | 3 - 🟡 Stable | 50 days ago (2026-08-06 00:47:40 UTC) | 32 | Go | DuckDB wrapper for FAISS - Experimental |
| 115 | [fakeit](https://duckdb.org/community_extensions/extensions/fakeit.html) | [duckdb-fakeit](https://github.com/tobilg/duckdb-fakeit) | 🟢 Ongoing | 3 - 🟡 Stable | 49 days ago (2026-08-07 10:54:19 UTC) | 17 | Rust | DuckDB extension: fakeit by tobilg |
| 116 | [file_dialog](https://duckdb.org/community_extensions/extensions/file_dialog.html) | [duckdb-ext-file-dialog](https://github.com/yutannihilation/duckdb-ext-file-dialog) | 🟢 Ongoing | 2 - ✅ Active | 30 days ago (2026-08-25 12:15:56 UTC) | 18 | Rust | A DuckDB extension to choose file interactively using native file open dialogs |
| 117 | [finance](https://duckdb.org/community_extensions/extensions/finance.html) | [duckdb-finance](https://github.com/leonardovida/duckdb-finance) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-09-25 09:42:09 UTC) | 8 | C++ | SQL-native quant finance for DuckDB |
| 118 | [finetype](https://duckdb.org/community_extensions/extensions/finetype.html) | [finetype](https://github.com/meridian-online/finetype) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-09-24 03:00:44 UTC) | 5 | Rust | 👓 Precision format detection for text data. Semantic type inference with tran... |
| 119 | [fire_duck_ext](https://duckdb.org/community_extensions/extensions/fire_duck_ext.html) | [fire_duck_ext](https://github.com/BorisBesky/fire_duck_ext) | 🟢 Ongoing | 2 - ✅ Active | 8 days ago (2026-09-17 03:51:10 UTC) | 4 | C++ | duckdb extension for firestore |
| 120 | [firebird](https://duckdb.org/community_extensions/extensions/firebird.html) | [duckdb-firebird](https://github.com/flozer/duckdb-firebird) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-09-24 11:57:24 UTC) | 5 | C++ | DuckDB extension: firebird by flozer |
| 121 | [fit](https://duckdb.org/community_extensions/extensions/fit.html) | [duckdb-fit-extension](https://github.com/antoriche/duckdb-fit-extension) | 🟢 Ongoing | 3 - 🟡 Stable | 32 days ago (2026-08-23 23:32:07 UTC) | 6 | C++ | DuckDB extension: fit by antoriche |
| 122 | [fivetran](https://duckdb.org/community_extensions/extensions/fivetran.html) | [duckdb_sparse_variant](https://github.com/fivetran/duckdb_sparse_variant) | 🟢 Ongoing | 4 - 🟠 Stale | 129 days ago (2026-05-19 07:42:06 UTC) | 1 | C++ | A DuckDB extension providing sparse VARIANT encoding for STRUCTs and an optim... |
| 123 | [flock](https://duckdb.org/community_extensions/extensions/flock.html) | [flock](https://github.com/dais-polymtl/flock) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-09-25 04:45:50 UTC) | 359 | C++ | Beyond Quacking: Deep Integration of Language Models and RAG into DuckDB (VLD... |
| 124 | [fsquery](https://duckdb.org/community_extensions/extensions/fsquery.html) | [fsquery](https://github.com/halgari/fsquery) | ❓ Unknown | 4 - 🟠 Stale | 192 days ago (2026-03-16 16:09:24 UTC) | 2 | C++ | An extension that allows DuckDB to enumerate and stat files on the disk |
| 125 | [func_apply](https://duckdb.org/community_extensions/extensions/func_apply.html) | [duckdb_func_apply](https://github.com/teaguesterling/duckdb_func_apply) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-09-25 04:29:44 UTC) | 5 | C++ | An exension to allow dynamic function application |
| 126 | [fusion_scanner](https://duckdb.org/community_extensions/extensions/fusion_scanner.html) | [ofquack](https://github.com/krokozyab/ofquack) | 🟢 Ongoing | 2 - ✅ Active | 27 days ago (2026-08-29 07:11:52 UTC) | 7 | C++ | DuckDB extension for querying Oracle Fusion Cloud data directly with SQL |
| 127 | [fuzzycomplete](https://duckdb.org/community_extensions/extensions/fuzzycomplete.html) | [fuzzycomplete](https://github.com/Query-farm/fuzzycomplete) | 🟢 Ongoing | 2 - ✅ Active | 20 days ago (2026-09-04 20:19:22 UTC) | 30 | C++ | DuckDB Extension for fuzzy string matching based autocompletion |
| 128 | [gaggle](https://duckdb.org/community_extensions/extensions/gaggle.html) | [gaggle](https://github.com/CogitatorTech/gaggle) | 🟢 Ongoing | 3 - 🟡 Stable | 64 days ago (2026-07-22 14:49:44 UTC) | 19 | Rust | A DuckDB extension for working with Kaggle datasets |
| 129 | [gatekeeper](https://duckdb.org/community_extensions/extensions/gatekeeper.html) | [duckdb-gatekeeper](https://github.com/nozzle/duckdb-gatekeeper) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-09-23 21:34:11 UTC) | 3 | Python | A DuckDB extension that enforces catalog, schema, and/or table-level access c... |
| 130 | [gcloud_observability](https://duckdb.org/community_extensions/extensions/gcloud_observability.html) | [duckdb-gcloud-observability](https://github.com/smithclay/duckdb-gcloud-observability) | 🟢 Ongoing | 3 - 🟡 Stable | 44 days ago (2026-08-11 20:28:26 UTC) | 1 | C++ | ingest logs and metrics (and soon traces) from google cloud observability int... |
| 131 | [gcs](https://duckdb.org/community_extensions/extensions/gcs.html) | [duckdb-gcs](https://github.com/northpolesec/duckdb-gcs) | 🟢 Ongoing | 2 - ✅ Active | 23 days ago (2026-09-01 13:30:24 UTC) | 32 | C++ | A GCS-native extension for DuckDB |
| 132 | [gdrive](https://duckdb.org/community_extensions/extensions/gdrive.html) | [duckdb-gdrive](https://github.com/DataZooDE/duckdb-gdrive) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-09-24 03:41:37 UTC) | 5 | C++ | Query Google Drive files directly from DuckDB via a gdrive:// filesystem |
| 133 | [gdx](https://duckdb.org/community_extensions/extensions/gdx.html) | [duckdb-gdx](https://github.com/chrispahm/duckdb-gdx) | ❓ Unknown | 3 - 🟡 Stable | 60 days ago (2026-07-27 09:45:36 UTC) | 1 | C++ | DuckDB extension: gdx by chrispahm |
| 134 | [geography](https://duckdb.org/community_extensions/extensions/geography.html) | [duckdb-geography](https://github.com/paleolimbot/duckdb-geography) | 🟢 Ongoing | 2 - ✅ Active | 20 days ago (2026-09-04 21:54:45 UTC) | 48 | C++ | Geospatial data extension by paleolimbot |
| 135 | [geosilo](https://duckdb.org/community_extensions/extensions/geosilo.html) | [geosilo](https://github.com/Query-farm/geosilo) | 🟢 Ongoing | 2 - ✅ Active | 19 days ago (2026-09-05 16:23:30 UTC) | 25 | C++ | DuckDB extension for compact geometry encoding using delta-encoded coordinate... |
| 136 | [geotiff](https://duckdb.org/community_extensions/extensions/geotiff.html) | [duckdb-geotiff](https://github.com/babaknaimi/duckdb-geotiff) | ❓ Unknown | 4 - 🟠 Stale | over a year ago (2025-08-20 05:12:15 UTC) | 3 | C++ | Duckdb extension to read GeoTiffs directly with duckdb database |
| 137 | [ggsql](https://duckdb.org/community_extensions/extensions/ggsql.html) | [ggsql-duckdb](https://github.com/posit-dev/ggsql-duckdb) | 🟢 Ongoing | 4 - 🟠 Stale | 94 days ago (2026-06-23 06:14:05 UTC) | 32 | Rust | A DuckDB extension adding support for ggsql  |
| 138 | [gh](https://duckdb.org/community_extensions/extensions/gh.html) | [duckdb-gh](https://github.com/carlopi/duckdb-gh) | 🟢 Ongoing | 4 - 🟠 Stale | 148 days ago (2026-04-29 14:21:02 UTC) | 5 | C++ | DuckDB extension: gh by carlopi |
| 139 | [gorz](https://duckdb.org/community_extensions/extensions/gorz.html) | [duckdb-gorz](https://github.com/gorfather/duckdb-gorz) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-09-24 15:54:55 UTC) | 1 | C++ | DuckDB extension: read/write GORpipe .gorz / .gord genomic files as native ta... |
| 140 | [gpudb](https://duckdb.org/community_extensions/extensions/gpudb.html) | [duckdbgpumetaldbram](https://github.com/singhpratech/duckdbgpumetaldbram) | 🟢 Ongoing | 1 - 🔥 Very Active | 2 days ago (2026-09-22 17:28:14 UTC) | 25 | C++ | GPU-accelerated plain DuckDB SQL — Apple Silicon Metal + NVIDIA CUDA. The fir... |
| 141 | [gridpin_ext](https://duckdb.org/community_extensions/extensions/gridpin_ext.html) | [duckdb-gridpin](https://github.com/gridpin/duckdb-gridpin) | 🟢 Ongoing | 3 - 🟡 Stable | 36 days ago (2026-08-20 10:11:29 UTC) | 1 | Rust | DuckDB extension for offline geocoding with GridPin |
| 142 | [gsheets](https://duckdb.org/community_extensions/extensions/gsheets.html) | [duckdb_gsheets](https://github.com/evidence-dev/duckdb_gsheets) | 🟢 Ongoing | 4 - 🟠 Stale | 216 days ago (2026-02-21 04:11:04 UTC) | 354 | C++ | DuckDB extension to read and write Google Sheets using SQL |
| 143 | [h3](https://duckdb.org/community_extensions/extensions/h3.html) | [h3-duckdb](https://github.com/isaacbrodsky/h3-duckdb) | 🟢 Ongoing | 1 - 🔥 Very Active | 4 days ago (2026-09-20 20:46:50 UTC) | 252 | C | Bindings for H3 to DuckDB |
| 144 | [h5db](https://duckdb.org/community_extensions/extensions/h5db.html) | [h5db](https://github.com/jokasimr/h5db) | 🟢 Ongoing | 2 - ✅ Active | 14 days ago (2026-09-10 13:12:34 UTC) | 6 | C++ | Duckdb extension for reading HDF5 files. |
| 145 | [harbor](https://duckdb.org/community_extensions/extensions/harbor.html) | [duckdb-harbor](https://github.com/shreeve/duckdb-harbor) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-09-24 05:13:39 UTC) | 12 | Rust | Many clients, one DuckDB — Harbor serves your database over plain HTTP (one s... |
| 146 | [hashfuncs](https://duckdb.org/community_extensions/extensions/hashfuncs.html) | [hashfuncs](https://github.com/Query-farm/hashfuncs) | 🟢 Ongoing | 2 - ✅ Active | 20 days ago (2026-09-04 20:19:32 UTC) | 14 | C++ | A DuckDB extension that supplies non-cryptographic hash functions. |
| 147 | [hdf5](https://duckdb.org/community_extensions/extensions/hdf5.html) | [duckdb-hdf5](https://github.com/Berrysoft/duckdb-hdf5) | ❓ Unknown | 4 - 🟠 Stale | 155 days ago (2026-04-23 01:30:36 UTC) | 12 | Rust | HDF5 plugin for duckdb |
| 148 | [hdfs](https://duckdb.org/community_extensions/extensions/hdfs.html) | [duckdb-hdfs](https://github.com/casperhart/duckdb-hdfs) | ❓ Unknown | 3 - 🟡 Stable | 66 days ago (2026-07-21 01:26:22 UTC) | 0 | Rust | DuckDB extension: hdfs by casperhart |
| 149 | [healthkit_export](https://github.com/Mjboothaus/duckdb-healthkit-export) | [duckdb-healthkit-export](https://github.com/Mjboothaus/duckdb-healthkit-export) | ❓ Unknown | 1 - 🔥 Very Active | 6 days ago (2026-09-19 04:26:54 UTC) | 1 | C | HealthKit export.zip → DuckDB SQL |
| 150 | [hedged_request_fs](https://duckdb.org/community_extensions/extensions/hedged_request_fs.html) | [duckdb-hedged-request](https://github.com/dentiny/duckdb-hedged-request) | 🟢 Ongoing | 1 - 🔥 Very Active | 3 days ago (2026-09-22 04:34:25 UTC) | 2 | C++ | DuckDB extension: hedged_request_fs by dentiny |
| 151 | [hex9](https://duckdb.org/community_extensions/extensions/hex9.html) | [duckdb-hex9](https://github.com/MrBenGriffin/duckdb-hex9) | 🟢 Ongoing | 3 - 🟡 Stable | 59 days ago (2026-07-28 09:59:07 UTC) | 1 | C++ | duckdb community wrapper for libhex9 |
| 152 | [highs](https://duckdb.org/community_extensions/extensions/highs.html) | [HiGHS-duckdb](https://github.com/fhk/HiGHS-duckdb) | ❓ Unknown | 4 - 🟠 Stale | 212 days ago (2026-02-25 02:07:48 UTC) | 2 | C++ | Run the solver in the database! |
| 153 | [hive_metastore](https://duckdb.org/community_extensions/extensions/hive_metastore.html) | [duckdb-hive-metastore](https://github.com/ilum-cloud/duckdb-hive-metastore) | 🟢 Ongoing | 1 - 🔥 Very Active | 4 days ago (2026-09-20 18:00:00 UTC) | 5 | C++ | DuckDB extension allowing to connect to Apache Hive Metastore and query the d... |
| 154 | [hnsw_acorn](https://duckdb.org/community_extensions/extensions/hnsw_acorn.html) | [duckdb-hnsw-acorn](https://github.com/cigrainger/duckdb-hnsw-acorn) | ❓ Unknown | 4 - 🟠 Stale | 181 days ago (2026-03-28 07:49:47 UTC) | 67 | C++ | ACORN-1 pre-filtered HNSW search for DuckDB |
| 155 | [holtfs](https://duckdb.org/community_extensions/extensions/holtfs.html) | [duckdb-holtfs](https://github.com/feichai0017/duckdb-holtfs) | 🟢 Ongoing | 3 - 🟡 Stable | 46 days ago (2026-08-10 08:13:26 UTC) | 1 | C++ | DuckDB extension for planning scans through Holt-backed metadata indexes |
| 156 | [hostfs](https://duckdb.org/community_extensions/extensions/hostfs.html) | [hostFS](https://github.com/gropaul/hostFS) | ❓ Unknown | 4 - 🟠 Stale | 358 days ago (2025-10-01 21:02:13 UTC) | 32 | C++ | DuckDB extension: hostfs by gropaul |
| 157 | [html_query](https://duckdb.org/community_extensions/extensions/html_query.html) | [duckdb_html_query](https://github.com/midwork-finds-jobs/duckdb_html_query) | ❓ Unknown | 4 - 🟠 Stale | 231 days ago (2026-02-05 15:33:13 UTC) | 2 | Rust | Filter HTML inside duckdb |
| 158 | [html_readability](https://duckdb.org/community_extensions/extensions/html_readability.html) | [duckdb-html-readability](https://github.com/midwork-finds-jobs/duckdb-html-readability) | ❓ Unknown | 4 - 🟠 Stale | 231 days ago (2026-02-05 15:33:16 UTC) | 0 | Rust | DuckDB extension to parse html to readable text |
| 159 | [http_client](https://duckdb.org/community_extensions/extensions/http_client.html) | [httpclient](https://github.com/Query-farm/httpclient) | 🟢 Ongoing | 2 - ✅ Active | 16 days ago (2026-09-08 21:41:11 UTC) | 80 | C++ | DuckDB HTTP GET/POST Client in a Community Extension |
| 160 | [http_request](https://duckdb.org/community_extensions/extensions/http_request.html) | [duckdb_http_request](https://github.com/midwork-finds-jobs/duckdb_http_request) | ❓ Unknown | 4 - 🟠 Stale | 219 days ago (2026-02-17 13:03:03 UTC) | 4 | C++ | Uses the native duckdb httputil to make extra requests in SELECT |
| 161 | [http_stats](https://duckdb.org/community_extensions/extensions/http_stats.html) | [duckdb-http-stats](https://github.com/tlinhart/duckdb-http-stats) | ❓ Unknown | 4 - 🟠 Stale | 181 days ago (2026-03-27 13:58:03 UTC) | 1 | C++ | Better HTTP statistics for DuckDB |
| 162 | [httpd_log](https://duckdb.org/community_extensions/extensions/httpd_log.html) | [duckdb-httpd-log](https://github.com/saygox/duckdb-httpd-log) | ❓ Unknown | 4 - 🟠 Stale | 256 days ago (2026-01-12 06:14:58 UTC) | 1 | C++ | duckdb extension |
| 163 | [httpfs_timeout_retry](https://duckdb.org/community_extensions/extensions/httpfs_timeout_retry.html) | [duckdb-httpfs-timeout-retry](https://github.com/dentiny/duckdb-httpfs-timeout-retry) | 🟢 Ongoing | 1 - 🔥 Very Active | 3 days ago (2026-09-22 04:37:09 UTC) | 1 | C++ | Web/HTTP functionality extension by dentiny |
| 164 | [httpserver](https://duckdb.org/community_extensions/extensions/httpserver.html) | [httpserver](https://github.com/Query-farm/httpserver) | 🟢 Ongoing | 2 - ✅ Active | 20 days ago (2026-09-04 20:19:43 UTC) | 285 | C++ | DuckDB HTTP API Server and Query Interface in a  Community Extension |
| 165 | [huggingface](https://duckdb.org/community_extensions/extensions/huggingface.html) | [duckdb-huggingface](https://github.com/dentiny/duckdb-huggingface) | 🟢 Ongoing | 1 - 🔥 Very Active | 3 days ago (2026-09-22 07:21:20 UTC) | 1 | C++ | DuckDB extension: huggingface by dentiny |
| 166 | [infera](https://duckdb.org/community_extensions/extensions/infera.html) | [infera](https://github.com/CogitatorTech/infera) | 🟢 Ongoing | 3 - 🟡 Stable | 64 days ago (2026-07-22 14:50:26 UTC) | 137 | Rust | A DuckDB extension for in-database inference |
| 167 | [inflector](https://duckdb.org/community_extensions/extensions/inflector.html) | [inflector](https://github.com/Query-farm/inflector) | 🟢 Ongoing | 2 - ✅ Active | 20 days ago (2026-09-04 20:19:54 UTC) | 10 | C++ | Powerful string case transformation and inflection capabilities directly to y... |
| 168 | [interlis](https://duckdb.org/community_extensions/extensions/interlis.html) | [duckdb-interlis](https://github.com/edigonzales/duckdb-interlis) | 🟢 Ongoing | 2 - ✅ Active | 24 days ago (2026-08-31 19:55:29 UTC) | 0 | C++ | DuckDB extension: interlis by edigonzales |
| 169 | [ion](https://duckdb.org/community_extensions/extensions/ion.html) | [duckdb-ion](https://github.com/kestra-io/duckdb-ion) | 🟢 Ongoing | 1 - 🔥 Very Active | 4 days ago (2026-09-21 08:37:28 UTC) | 5 | C++ | AWS Ion extension for DuckDB |
| 170 | [jev](https://github.com/judoaseeta/duckdb-jev) | [duckdb-jev](https://github.com/judoaseeta/duckdb-jev) | ❓ Unknown | 1 - 🔥 Very Active | 4 days ago (2026-09-21 01:58:17 UTC) | 0 | C++ | Ask your DuckDB tables questions in plain language. A DuckDB port of pg-jev,... |
| 171 | [json_schema](https://duckdb.org/community_extensions/extensions/json_schema.html) | [json_schema](https://github.com/Query-farm/json_schema) | 🟢 Ongoing | 2 - ✅ Active | 20 days ago (2026-09-04 20:20:08 UTC) | 5 | C++ | A DuckDB extension that bring support for validating JSON data using JSON sch... |
| 172 | [jsonata](https://duckdb.org/community_extensions/extensions/jsonata.html) | [jsonata](https://github.com/Query-farm/jsonata) | 🟢 Ongoing | 2 - ✅ Active | 20 days ago (2026-09-04 20:20:13 UTC) | 8 | C++ | The JSONata extension for DuckDB enables expressive, JSON-focused querying an... |
| 173 | [jsono](https://duckdb.org/community_extensions/extensions/jsono.html) | [duckdb-jsono](https://github.com/Flamefork/duckdb-jsono) | 🟢 Ongoing | 2 - ✅ Active | 21 days ago (2026-09-04 08:06:41 UTC) | 1 | C++ | A DuckDB extension for analytics-optimized JSON storage and querying |
| 174 | [jwt](https://duckdb.org/community_extensions/extensions/jwt.html) | [duckdb_jwt](https://github.com/GalvinGao/duckdb_jwt) | ❓ Unknown | 4 - 🟠 Stale | over a year ago (2025-07-09 00:13:56 UTC) | 0 | C++ | DuckDB extension: jwt by GalvinGao |
| 175 | [keboola](https://duckdb.org/community_extensions/extensions/keboola.html) | [duckdb-extension](https://github.com/keboola/duckdb-extension) | 🟢 Ongoing | 3 - 🟡 Stable | 78 days ago (2026-07-08 11:43:04 UTC) | 1 | C++ | DuckDB extension for Keboola Storage — query and write Keboola tables using s... |
| 176 | [lance_conversion](https://github.com/dentiny/duckdb_lance_conversion) | [duckdb_lance_conversion](https://github.com/dentiny/duckdb_lance_conversion) | ❓ Unknown | 1 - 🔥 Very Active | today (2026-09-25 06:15:16 UTC) | 0 | Rust | DuckDB extension: lance_conversion by dentiny |
| 177 | [lastra](https://duckdb.org/community_extensions/extensions/lastra.html) | [duckdb-lastra](https://github.com/QTSurfer/duckdb-lastra) | ❓ Unknown | 3 - 🟡 Stable | 45 days ago (2026-08-10 11:58:17 UTC) | 1 | C++ | DuckDB extension for reading Lastra columnar time series files natively |
| 178 | [latency_injection_fs](https://duckdb.org/community_extensions/extensions/latency_injection_fs.html) | [duckdb-filesystem-latency-injection](https://github.com/dentiny/duckdb-filesystem-latency-injection) | 🟢 Ongoing | 1 - 🔥 Very Active | 3 days ago (2026-09-22 07:24:18 UTC) | 1 | C++ | DuckDB extension: latency_injection_fs by dentiny |
| 179 | [laterite_ags4](https://duckdb.org/community_extensions/extensions/laterite_ags4.html) | [laterite-duckdb](https://github.com/niko86/laterite-duckdb) | 🟢 Ongoing | 2 - ✅ Active | 17 days ago (2026-09-08 01:02:48 UTC) | 2 | Rust | DuckDB extension: laterite_ags4 by niko86 |
| 180 | [ldbc_data_gen](https://duckdb.org/community_extensions/extensions/ldbc_data_gen.html) | [ldbc-data-gen](https://github.com/Dtenwolde/ldbc-data-gen) | 🟢 Ongoing | 3 - 🟡 Stable | 52 days ago (2026-08-04 11:07:46 UTC) | 1 | C++ | Database connectivity extension by Dtenwolde |
| 181 | [lerobot](https://duckdb.org/community_extensions/extensions/lerobot.html) | [duckdb-lerobot](https://github.com/AstroVela/duckdb-lerobot) | 🟢 Ongoing | 1 - 🔥 Very Active | 6 days ago (2026-09-18 13:37:54 UTC) | 2 | C++ | DuckDB and Vane extension for LeRobot datasets |
| 182 | [level_pivot](https://duckdb.org/community_extensions/extensions/level_pivot.html) | [duckdb-level-pivot](https://github.com/halgari/duckdb-level-pivot) | 🟢 Ongoing | 4 - 🟠 Stale | 154 days ago (2026-04-23 16:05:04 UTC) | 0 | C++ | DuckDB extension: level_pivot by halgari |
| 183 | [lindel](https://duckdb.org/community_extensions/extensions/lindel.html) | [lindel](https://github.com/Query-farm/lindel) | 🟢 Ongoing | 2 - ✅ Active | 20 days ago (2026-09-04 20:20:19 UTC) | 67 | C++ | DuckDB Extension Linearization/Delinearization, Z-Order, Hilbert and Morton C... |
| 184 | [livetennis](https://duckdb.org/community_extensions/extensions/livetennis.html) | [duckdb-livetennis](https://github.com/livetennisapi/duckdb-livetennis) | 🟢 Ongoing | 1 - 🔥 Very Active | 4 days ago (2026-09-20 18:07:30 UTC) | 1 | C++ | DuckDB community extension for the Live Tennis API: live scores, fixtures and... |
| 185 | [llm](https://duckdb.org/community_extensions/extensions/llm.html) | [duckdb-llm](https://github.com/midwork-finds-jobs/duckdb-llm) | 🟢 Ongoing | 4 - 🟠 Stale | 219 days ago (2026-02-17 14:09:08 UTC) | 4 | C++ | DuckDB extension: llm by midwork-finds-jobs |
| 186 | [loki](https://duckdb.org/community_extensions/extensions/loki.html) | [duckdb-loki](https://github.com/prochac/duckdb-loki) | ❓ Unknown | 3 - 🟡 Stable | 54 days ago (2026-08-01 13:39:52 UTC) | 0 | C++ | DuckDB extension: loki by prochac |
| 187 | [lpts](https://duckdb.org/community_extensions/extensions/lpts.html) | [lpts](https://github.com/cwida/lpts) | 🟢 Ongoing | 1 - 🔥 Very Active | 3 days ago (2026-09-21 14:41:05 UTC) | 10 | C++ | Logical Plan To SQL DuckDB Extension |
| 188 | [lsh](https://duckdb.org/community_extensions/extensions/lsh.html) | [lsh](https://github.com/princeton-ddss/lsh) | ❓ Unknown | 4 - 🟠 Stale | 161 days ago (2026-04-16 17:00:45 UTC) | 14 | Rust | DuckDB community extension for locality-sensitive hashing (LSH) |
| 189 | [lttb](https://duckdb.org/community_extensions/extensions/lttb.html) | [duckdb-lttb](https://github.com/reformovo/duckdb-lttb) | ❓ Unknown | 3 - 🟡 Stable | 86 days ago (2026-07-01 07:47:53 UTC) | 3 | C++ | A simple lttb algorithm extension for DuckDB |
| 190 | [lua](https://duckdb.org/community_extensions/extensions/lua.html) | [duckdb-lua](https://github.com/isaacbrodsky/duckdb-lua) | 🟢 Ongoing | 1 - 🔥 Very Active | 4 days ago (2026-09-20 17:49:06 UTC) | 13 | C | DuckDB extension to evaluate Lua expressions. |
| 191 | [luajit](https://duckdb.org/community_extensions/extensions/luajit.html) | [duckdb-luajit](https://github.com/alitrack/duckdb-luajit) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-09-24 08:27:18 UTC) | 8 | C | DuckDB extension for in-process JIT-compiled Lua UDFs via LuaJIT — self-conta... |
| 192 | [magic](https://duckdb.org/community_extensions/extensions/magic.html) | [duckdb-magic](https://github.com/carlopi/duckdb-magic) | ❓ Unknown | 4 - 🟠 Stale | 95 days ago (2026-06-22 07:17:42 UTC) | 8 | C++ | Auto-detect file types via `libmagic` (`file` utility) |
| 193 | [marc21](https://duckdb.org/community_extensions/extensions/marc21.html) | [duckdb-marc21](https://github.com/mgbilby/duckdb-marc21) | 🟢 Ongoing | 2 - ✅ Active | 18 days ago (2026-09-06 21:53:28 UTC) | 3 | C++ | MARC21 Cataloging Toolkit for DuckDB |
| 194 | [marisa](https://duckdb.org/community_extensions/extensions/marisa.html) | [marisa](https://github.com/Query-farm/marisa) | 🟢 Ongoing | 2 - ✅ Active | 20 days ago (2026-09-04 20:20:24 UTC) | 16 | C++ | The Marisa extension by Query.Farm integrates the fast, space-efficient MARIS... |
| 195 | [markdown](https://duckdb.org/community_extensions/extensions/markdown.html) | [duckdb_markdown](https://github.com/teaguesterling/duckdb_markdown) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-09-25 04:20:13 UTC) | 31 | C++ | Heirarchical markdown parsing for DuckDB |
| 196 | [maxmind](https://duckdb.org/community_extensions/extensions/maxmind.html) | [duckdb-maxmind](https://github.com/marselester/duckdb-maxmind) | 🟢 Ongoing | 3 - 🟡 Stable | 87 days ago (2026-06-29 21:07:08 UTC) | 9 | Zig | DuckDB MaxMind extension written in Zig. |
| 197 | [miint](https://duckdb.org/community_extensions/extensions/miint.html) | [duckdb-miint](https://github.com/the-miint/duckdb-miint) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-09-25 02:48:02 UTC) | 8 | C++ | DuckDB extension: miint by the-miint |
| 198 | [minijinja](https://duckdb.org/community_extensions/extensions/minijinja.html) | [minijinja](https://github.com/Query-farm/minijinja) | 🟢 Ongoing | 2 - ✅ Active | 20 days ago (2026-09-04 20:20:29 UTC) | 7 | C++ | DuckDB extension: minijinja |
| 199 | [miniplot](https://duckdb.org/community_extensions/extensions/miniplot.html) | [miniplot](https://github.com/nkwork9999/miniplot) | 🟢 Ongoing | 4 - 🟠 Stale | 314 days ago (2025-11-15 02:42:43 UTC) | 25 | C++ | DuckDB extension: miniplot by nkwork9999 |
| 200 | [ml](https://duckdb.org/community_extensions/extensions/ml.html) | [duckdb-ml](https://github.com/alitrack/duckdb-ml) | 🟢 Ongoing | 3 - 🟡 Stable | 38 days ago (2026-08-18 06:28:03 UTC) | 8 | Rust | DuckDB extension: ml by alitrack |
| 201 | [mlpack](https://duckdb.org/community_extensions/extensions/mlpack.html) | [duckdb-mlpack](https://github.com/eddelbuettel/duckdb-mlpack) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-09-24 19:42:09 UTC) | 21 | C++ | Bringing mlpack to duckdb |
| 202 | [mmcif](https://duckdb.org/community_extensions/extensions/mmcif.html) | [duckdb-mmcif](https://github.com/i-VRESSE/duckdb-mmcif) | 🟢 Ongoing | 1 - 🔥 Very Active | 7 days ago (2026-09-18 08:05:46 UTC) | 1 | C++ | Read/write protein structure mmcif files with duckdb |
| 203 | [monetary](https://duckdb.org/community_extensions/extensions/monetary.html) | [monetary](https://github.com/fyffee/monetary) | ❓ Unknown | 4 - 🟠 Stale | 238 days ago (2026-01-29 11:29:01 UTC) | 0 | C++ | DuckDB extension: monetary by fyffee |
| 204 | [mongo](https://duckdb.org/community_extensions/extensions/mongo.html) | [duckdb-mongo](https://github.com/stephaniewang526/duckdb-mongo) | 🟢 Ongoing | 2 - ✅ Active | 24 days ago (2026-08-31 15:34:19 UTC) | 59 | C++ | Integrates DuckDB with MongoDB, enabling direct SQL queries and writes over M... |
| 205 | [mooncake](https://duckdb.org/community_extensions/extensions/mooncake.html) | [duckdb_mooncake](https://github.com/Mooncake-Labs/duckdb_mooncake) | ❓ Unknown | 4 - 🟠 Stale | 334 days ago (2025-10-26 07:13:05 UTC) | 10 | C++ | Read Iceberg tables written by moonlink in real time |
| 206 | [motorsport_telemetry](https://duckdb.org/community_extensions/extensions/motorsport_telemetry.html) | [duckdb_motorsport_telemetry](https://github.com/tobi/duckdb_motorsport_telemetry) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-09-24 03:43:50 UTC) | 9 | Rust | Fast DuckDB extension and Rust parsers for Cosworth PDS, MoTeC LD, and VBOX V... |
| 207 | [mpduck](https://duckdb.org/community_extensions/extensions/mpduck.html) | [mpduck](https://github.com/MatthewMooreZA/mpduck) | ❓ Unknown | 1 - 🔥 Very Active | 4 days ago (2026-09-20 12:45:27 UTC) | 1 | C++ | DuckDB extension to read and write Prophet model point files. |
| 208 | [msolap](https://duckdb.org/community_extensions/extensions/msolap.html) | [duckdb-msolap-extension](https://github.com/Hugoberry/duckdb-msolap-extension) | ❓ Unknown | 4 - 🟠 Stale | 365 days ago (2025-09-24 16:33:46 UTC) | 14 | C++ | DuckDB extension: msolap by Hugoberry |
| 209 | [mssql](https://duckdb.org/community_extensions/extensions/mssql.html) | [mssql-extension](https://github.com/hugr-lab/mssql-extension) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-09-25 11:13:34 UTC) | 134 | C++ | DuckDB extension for Microsoft SQL Server (TDS + TLS), with catalog integrati... |
| 210 | [mssql_ducklake](https://duckdb.org/community_extensions/extensions/mssql_ducklake.html) | [mssql-ducklake](https://github.com/hugr-lab/mssql-ducklake) | 🟢 Ongoing | 1 - 🔥 Very Active | 7 days ago (2026-09-17 17:33:06 UTC) | 10 | C++ | DuckLake metadata catalog on SQL Server — bridge extension between ducklake a... |
| 211 | [nanoarrow](https://duckdb.org/community_extensions/extensions/nanoarrow.html) | [duckdb-nanoarrow](https://github.com/duckdb/duckdb-nanoarrow) | ❓ Unknown | 1 - 🔥 Very Active | 4 days ago (2026-09-21 08:43:48 UTC) | 81 | C++ | DuckDB extension: nanoarrow by paleolimbot |
| 212 | [nanodbc](https://duckdb.org/community_extensions/extensions/nanodbc.html) | [duckdb-nanodbc-extension](https://github.com/Hugoberry/duckdb-nanodbc-extension) | ❓ Unknown | 4 - 🟠 Stale | 146 days ago (2026-05-01 13:18:55 UTC) | 53 | C++ | Database connectivity extension by Hugoberry |
| 213 | [nats_js](https://duckdb.org/community_extensions/extensions/nats_js.html) | [duckdb-nats-jetstream](https://github.com/brannn/duckdb-nats-jetstream) | ❓ Unknown | 4 - 🟠 Stale | 179 days ago (2026-03-30 05:12:16 UTC) | 22 | C++ | DuckDB extension for querying NATS JetStream message streams with SQL |
| 214 | [netquack](https://duckdb.org/community_extensions/extensions/netquack.html) | [duckdb-netquack](https://github.com/hatamiarash7/duckdb-netquack) | ❓ Unknown | 1 - 🔥 Very Active | today (2026-09-25 08:49:04 UTC) | 44 | C++ | DuckDB extension for parsing, extracting, and analyzing domains, URIs, and pa... |
| 215 | [nsv](https://duckdb.org/community_extensions/extensions/nsv.html) | [nsv-duckdb](https://github.com/nsv-format/nsv-duckdb) | 🟢 Ongoing | 1 - 🔥 Very Active | 3 days ago (2026-09-21 21:01:55 UTC) | 1 | Rust | A DuckDB extension for NSV processing |
| 216 | [oast](https://duckdb.org/community_extensions/extensions/oast.html) | [duckdb-oast](https://github.com/hrbrmstr/duckdb-oast) | 🟢 Ongoing | 4 - 🟠 Stale | 226 days ago (2026-02-10 12:00:32 UTC) | 5 | C | A DuckDB extension for validating, decoding, and extracting OAST (Out-of-Band... |
| 217 | [observefs](https://duckdb.org/community_extensions/extensions/observefs.html) | [duckdb-filesystem-observability](https://github.com/dentiny/duckdb-filesystem-observability) | 🟢 Ongoing | 1 - 🔥 Very Active | 3 days ago (2026-09-22 08:15:20 UTC) | 18 | C++ | Provides observability for duckdb filesystem. |
| 218 | [ofquack](https://duckdb.org/community_extensions/extensions/ofquack.html) | [ofquack](https://github.com/krokozyab/ofquack) | ❓ Unknown | 2 - ✅ Active | 27 days ago (2026-08-29 07:11:52 UTC) | 7 | C++ | DuckDB extension for querying Oracle Fusion Cloud data directly with SQL |
| 219 | [onager](https://duckdb.org/community_extensions/extensions/onager.html) | [onager](https://github.com/CogitatorTech/onager) | 🟢 Ongoing | 3 - 🟡 Stable | 56 days ago (2026-07-30 17:34:19 UTC) | 150 | Rust | A DuckDB extension for graph data analytics |
| 220 | [onelake](https://duckdb.org/community_extensions/extensions/onelake.html) | [duckdb_onelake](https://github.com/datumnova/duckdb_onelake) | ❓ Unknown | 4 - 🟠 Stale | 298 days ago (2025-12-01 10:28:22 UTC) | 19 | C++ | DuckDB extension: onelake by datumnova |
| 221 | [open_prompt](https://duckdb.org/community_extensions/extensions/open_prompt.html) | [openprompt](https://github.com/Query-farm/openprompt) | 🟢 Ongoing | 2 - ✅ Active | 20 days ago (2026-09-04 20:20:33 UTC) | 62 | C++ | DuckDB Community Extension to prompt LLMs from SQL |
| 222 | [opendal](https://duckdb.org/community_extensions/extensions/opendal.html) | [duckdb-opendal](https://github.com/chitralverma/duckdb-opendal) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-09-24 06:06:01 UTC) | 2 | Rust | extension to bring together duckdb and opendal |
| 223 | [oracle_scanner](https://duckdb.org/community_extensions/extensions/oracle_scanner.html) | [quack-oracle](https://github.com/krokozyab/quack-oracle) | 🟢 Ongoing | 2 - ✅ Active | 17 days ago (2026-09-07 15:22:02 UTC) | 3 | C++ | DuckDB extension speaking Oracle TNS/TTC natively without Oracle Client |
| 224 | [orc](https://duckdb.org/community_extensions/extensions/orc.html) | [duckdb_orc](https://github.com/alitrack/duckdb_orc) | 🟢 Ongoing | 2 - ✅ Active | 22 days ago (2026-09-02 12:43:15 UTC) | 4 | Rust | A DuckDB extension for reading Apache ORC files, written in pure Rust. |
| 225 | [osmium](https://duckdb.org/community_extensions/extensions/osmium.html) | [duckdb-osmium](https://github.com/jake-low/duckdb-osmium) | 🟢 Ongoing | 2 - ✅ Active | 21 days ago (2026-09-04 05:03:43 UTC) | 28 | C++ | DuckDB extension for reading OpenStreetMap PBF files using libosmium |
| 226 | [ossie](https://duckdb.org/community_extensions/extensions/ossie.html) | [duckdb-ossie](https://github.com/iqea-ai/duckdb-ossie) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-09-24 21:01:10 UTC) | 5 | C++ | DuckDB extension: ossie by iqea-ai |
| 227 | [otlp](https://duckdb.org/community_extensions/extensions/otlp.html) | [duckdb-otlp](https://github.com/smithclay/duckdb-otlp) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-09-24 22:03:34 UTC) | 87 | C++ | stream, store, and query OpenTelemetry metrics, logs, and traces (OTLP) in du... |
| 228 | [overture](https://duckdb.org/community_extensions/extensions/overture.html) | [duckdb-overture](https://github.com/cubilica/duckdb-overture) | ❓ Unknown | 4 - 🟠 Stale | 163 days ago (2026-04-14 16:46:56 UTC) | 4 | C++ | DuckDB extension: overture by cubilica |
| 229 | [pac](https://duckdb.org/community_extensions/extensions/pac.html) | [privacy](https://github.com/cwida/privacy) | 🟢 Ongoing | 2 - ✅ Active | 8 days ago (2026-09-17 10:58:56 UTC) | 21 | C++ | Automatic query privatization in DuckDB |
| 230 | [paimon](https://duckdb.org/community_extensions/extensions/paimon.html) | [duckdb-paimon](https://github.com/polardb/duckdb-paimon) | 🟢 Ongoing | 2 - ✅ Active | 11 days ago (2026-09-14 10:06:29 UTC) | 47 | C++ | DuckDB extension for accessing Apache Paimon. 🦆 |
| 231 | [panduck](https://duckdb.org/community_extensions/extensions/panduck.html) | [duckdb_panduck](https://github.com/teaguesterling/duckdb_panduck) | 🟢 Ongoing | 1 - 🔥 Very Active | 2 days ago (2026-09-22 18:50:30 UTC) | 3 | C++ | Native in-process document conversion and AST extraction for DuckDB (DOCX, EP... |
| 232 | [parser_tools](https://duckdb.org/community_extensions/extensions/parser_tools.html) | [duckdb_extension_parser_tools](https://github.com/hotdata-dev/duckdb_extension_parser_tools) | 🟢 Ongoing | 3 - 🟡 Stable | 66 days ago (2026-07-20 22:07:52 UTC) | 29 | C++ | Parse sql - with sql! |
| 233 | [pbi_scanner](https://duckdb.org/community_extensions/extensions/pbi_scanner.html) | [pbi_scanner](https://github.com/crazy-treyn/pbi_scanner) | 🟢 Ongoing | 4 - 🟠 Stale | 99 days ago (2026-06-17 19:07:44 UTC) | 16 | C++ | DuckDB extension that enables querying Power BI Semantic Models with DAX. |
| 234 | [pbix](https://duckdb.org/community_extensions/extensions/pbix.html) | [duckdb-pbix-extension](https://github.com/Hugoberry/duckdb-pbix-extension) | 🟢 Ongoing | 4 - 🟠 Stale | 335 days ago (2025-10-24 13:47:34 UTC) | 39 | C++ | Duckdb extension for parsing the metadata and contents of the embedded data m... |
| 235 | [pcap_duckdb](https://duckdb.org/community_extensions/extensions/pcap_duckdb.html) | [pcap_duckdb](https://github.com/siara-in/pcap_duckdb) | ❓ Unknown | 4 - 🟠 Stale | 113 days ago (2026-06-04 05:10:33 UTC) | 1 | C++ | Database connectivity extension by siara-in |
| 236 | [pcap_reader](https://duckdb.org/community_extensions/extensions/pcap_reader.html) | [pcap](https://github.com/Query-farm/pcap) | ❓ Unknown | 4 - 🟠 Stale | 129 days ago (2026-05-18 22:26:34 UTC) | 14 | Rust | DuckDB PCAP Reader Extension made in Rust |
| 237 | [pdal](https://duckdb.org/community_extensions/extensions/pdal.html) | [duckdb-pdal](https://github.com/ahuarte47/duckdb-pdal) | 🟢 Ongoing | 2 - ✅ Active | 21 days ago (2026-09-04 06:44:21 UTC) | 29 | C++ | DuckDB extension for manipulating point cloud data using SQL |
| 238 | [pdf](https://duckdb.org/community_extensions/extensions/pdf.html) | [duckdb-pdf](https://github.com/asubbarao/duckdb-pdf) | 🟢 Ongoing | 1 - 🔥 Very Active | 2 days ago (2026-09-22 18:57:59 UTC) | 10 | C++ | Read and extract content from PDF files in DuckDB — Poppler (text/words/lines... |
| 239 | [petgraph_ext](https://duckdb.org/community_extensions/extensions/petgraph_ext.html) | [duckdb_petgraph](https://github.com/alitrack/duckdb_petgraph) | 🟢 Ongoing | 3 - 🟡 Stable | 57 days ago (2026-07-29 23:37:31 UTC) | 5 | Rust | DuckDB extension: petgraph_ext by alitrack |
| 240 | [pfc](https://duckdb.org/community_extensions/extensions/pfc.html) | [pfc-duckdb](https://github.com/ImpossibleForge/pfc-duckdb) | 🟢 Ongoing | 4 - 🟠 Stale | 128 days ago (2026-05-19 17:32:55 UTC) | 2 | C++ | DuckDB extension to read PFC-JSONL compressed log files with block-level time... |
| 241 | [pic2vec](https://duckdb.org/community_extensions/extensions/pic2vec.html) | [pic2vec](https://github.com/nkwork9999/pic2vec) | 🟢 Ongoing | 4 - 🟠 Stale | 104 days ago (2026-06-12 16:13:03 UTC) | 1 | C++ | DuckDB extension: pic2vec by nkwork9999 |
| 242 | [pintail](https://duckdb.org/community_extensions/extensions/pintail.html) | [duckdb-pintail](https://github.com/tshelianthus/duckdb-pintail) | 🟢 Ongoing | 3 - 🟡 Stable | 34 days ago (2026-08-21 16:37:19 UTC) | 3 | C++ | Lightweight geospatial indexing for DuckDB — Geohash encoding, decoding, boun... |
| 243 | [pivot_table](https://duckdb.org/community_extensions/extensions/pivot_table.html) | [pivot_table](https://github.com/Alex-Monahan/pivot_table) | ❓ Unknown | 4 - 🟠 Stale | 160 days ago (2026-04-17 15:20:58 UTC) | 21 | C++ | Full spreadsheet-style pivot table through SQL macros. Just specify values, r... |
| 244 | [plinking_duck](https://duckdb.org/community_extensions/extensions/plinking_duck.html) | [plinking_duck](https://github.com/teaguesterling/plinking_duck) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-09-25 04:29:47 UTC) | 6 | C++ | DuckDB tools for Plink2  |
| 245 | [poached](https://duckdb.org/community_extensions/extensions/poached.html) | [poached](https://github.com/sidequery/poached) | ❓ Unknown | 4 - 🟠 Stale | 272 days ago (2025-12-26 21:13:19 UTC) | 12 | C++ | A DuckDB extension that exposes SQL parsing functionality for building IDEs,... |
| 246 | [polyglot](https://duckdb.org/community_extensions/extensions/polyglot.html) | [duckdb-polyglot](https://github.com/tobilg/duckdb-polyglot) | 🟢 Ongoing | 3 - 🟡 Stable | 48 days ago (2026-08-07 15:12:07 UTC) | 26 | Rust | Use other SQL dialects in DuckDB  |
| 247 | [pql](https://github.com/Guepard-Corp/duckdb-pql) | [duckdb-pql](https://github.com/Guepard-Corp/duckdb-pql) | ❓ Unknown | 1 - 🔥 Very Active | 2 days ago (2026-09-22 21:20:15 UTC) | 0 | C++ | DuckDB is an analytical in-process SQL database management system |
| 248 | [prometheus](https://duckdb.org/community_extensions/extensions/prometheus.html) | [duckdb-prometheus](https://github.com/botan/duckdb-prometheus) | 🟢 Ongoing | 3 - 🟡 Stable | 64 days ago (2026-07-22 15:04:54 UTC) | 6 | Rust | Query Prometheus-compatible HTTP APIs directly from DuckDB |
| 249 | [protoduck](https://duckdb.org/community_extensions/extensions/protoduck.html) | [protoduck](https://github.com/fcsnk/protoduck) | 🟢 Ongoing | 2 - ✅ Active | 8 days ago (2026-09-17 07:10:59 UTC) | 1 | Rust | DuckDB extension: protoduck by fcsnk |
| 250 | [prql](https://duckdb.org/community_extensions/extensions/prql.html) | [duckdb-prql](https://github.com/ywelsch/duckdb-prql) | 🟢 Ongoing | 4 - 🟠 Stale | 119 days ago (2026-05-28 11:18:16 UTC) | 332 | C++ | PRQL as a DuckDB extension |
| 251 | [psql](https://duckdb.org/community_extensions/extensions/psql.html) | [duckdb-psql](https://github.com/ywelsch/duckdb-psql) | 🟢 Ongoing | 4 - 🟠 Stale | 163 days ago (2026-04-14 18:55:40 UTC) | 107 | C++ | A piped SQL for DuckDB |
| 252 | [pst](https://duckdb.org/community_extensions/extensions/pst.html) | [duckdb-pst](https://github.com/intellekthq/duckdb-pst) | 🟢 Ongoing | 2 - ✅ Active | 27 days ago (2026-08-28 18:01:12 UTC) | 12 | C++ | In-place querying of Microsoft PST files, directly from storage, with SQL. |
| 253 | [psyduck](https://duckdb.org/community_extensions/extensions/psyduck.html) | [psyduck](https://github.com/Ian-Fogelman/psyduck) | 🟢 Ongoing | 4 - 🟠 Stale | 284 days ago (2025-12-14 15:10:39 UTC) | 8 | C++ | Pysduck a DuckDB community extension about Pokémon. |
| 254 | [px](https://duckdb.org/community_extensions/extensions/px.html) | [duckdb-px](https://github.com/toppyy/duckdb-px) | 🟢 Ongoing | 1 - 🔥 Very Active | 2 days ago (2026-09-22 16:57:38 UTC) | 0 | C++ | Duckdb extension for querying .px-files |
| 255 | [pyroscope](https://duckdb.org/community_extensions/extensions/pyroscope.html) | [pyroscope](https://github.com/Query-farm/pyroscope) | ❓ Unknown | 4 - 🟠 Stale | 218 days ago (2026-02-18 19:49:53 UTC) | 21 | Rust | DuckDB Pyroscope Extension for Continuous Profiling |
| 256 | [python_udf](https://duckdb.org/community_extensions/extensions/python_udf.html) | [duckdb-python](https://github.com/alitrack/duckdb-python) | 🟢 Ongoing | 3 - 🟡 Stable | 56 days ago (2026-07-31 08:04:02 UTC) | 8 | Rust | DuckDB extension: embed Python inside DuckDB for SQL-native Python UDFs (scal... |
| 257 | [quack_flamegraph](https://duckdb.org/community_extensions/extensions/quack_flamegraph.html) | [quack-flamegraph](https://github.com/kevintruong/quack-flamegraph) | 🟢 Ongoing | 3 - 🟡 Stable | 31 days ago (2026-08-24 16:44:51 UTC) | 1 | Python | duckdb extension for query flamegraph  |
| 258 | [quack_oauth](https://duckdb.org/community_extensions/extensions/quack_oauth.html) | [quack-oauth](https://github.com/DataZooDE/quack-oauth) | 🟢 Ongoing | 2 - ✅ Active | 8 days ago (2026-09-16 19:33:45 UTC) | 27 | C++ | Extensions providing OAuth and OpenID primitives for authentication and autho... |
| 259 | [quackapi](https://duckdb.org/community_extensions/extensions/quackapi.html) | [quackapi](https://github.com/asubbarao/quackapi) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-09-23 17:55:15 UTC) | 4 | C++ | FastAPI-class web framework inside DuckDB — CREATE ROUTE turns SQL into typed... |
| 260 | [quackfix](https://duckdb.org/community_extensions/extensions/quackfix.html) | [QuackFIX](https://github.com/hyehudai/QuackFIX) | ❓ Unknown | 4 - 🟠 Stale | 274 days ago (2025-12-25 10:36:24 UTC) | 16 | C++ | Fix log extension for duckdb |
| 261 | [quackformers](https://duckdb.org/community_extensions/extensions/quackformers.html) | [quackformers](https://github.com/martin-conur/quackformers) | ❓ Unknown | 1 - 🔥 Very Active | 4 days ago (2026-09-20 16:11:05 UTC) | 14 | Rust | DuckDB NLP extension. |
| 262 | [quackhole](https://duckdb.org/community_extensions/extensions/quackhole.html) | [quackhole](https://github.com/smithclay/quackhole) | 🟢 Ongoing | 2 - ✅ Active | 20 days ago (2026-09-04 13:11:35 UTC) | 8 | JavaScript | connect duckdb any duckdb, no VPN needed |
| 263 | [quackiso](https://duckdb.org/community_extensions/extensions/quackiso.html) | [quackiso](https://github.com/tempoloss/quackiso) | 🟢 Ongoing | 2 - ✅ Active | 30 days ago (2026-08-25 15:47:12 UTC) | 5 | Rust | Query ISO 20022 (camt/pacs/pain) financial messages as SQL in DuckDB |
| 264 | [quackscale](https://duckdb.org/community_extensions/extensions/quackscale.html) | [quackscale](https://github.com/Query-farm/quackscale) | 🟢 Ongoing | 2 - ✅ Active | 30 days ago (2026-08-26 08:18:46 UTC) | 24 | C++ | DuckDB WireGuard Extension with Quack & Ducklake over Tailscale, Headscale & Co |
| 265 | [quackstats](https://duckdb.org/community_extensions/extensions/quackstats.html) | [quackstats](https://github.com/jasadams/quackstats) | ❓ Unknown | 4 - 🟠 Stale | 235 days ago (2026-02-01 12:01:35 UTC) | 3 | Rust | DuckDB extension for time series forecasting and seasonality detection |
| 266 | [quackstore](https://duckdb.org/community_extensions/extensions/quackstore.html) | [QuackStore](https://github.com/coginiti-dev/QuackStore) | 🟢 Ongoing | 4 - 🟠 Stale | 142 days ago (2026-05-05 13:29:19 UTC) | 118 | C++ | DuckDB extension: quackstore by coginiti-dev |
| 267 | [query_condition_cache](https://duckdb.org/community_extensions/extensions/query_condition_cache.html) | [duckdb-query-condition-cache](https://github.com/dentiny/duckdb-query-condition-cache) | 🟢 Ongoing | 1 - 🔥 Very Active | 3 days ago (2026-09-22 07:26:20 UTC) | 19 | C++ | Predicate cache for DuckDB. |
| 268 | [query_limiter](https://duckdb.org/community_extensions/extensions/query_limiter.html) | [duckdb-query-limiter](https://github.com/dentiny/duckdb-query-limiter) | 🟢 Ongoing | 1 - 🔥 Very Active | 3 days ago (2026-09-22 07:44:57 UTC) | 1 | C++ | DuckDB extension: query_limiter by dentiny |
| 269 | [quickjs](https://duckdb.org/community_extensions/extensions/quickjs.html) | [quickjs](https://github.com/Query-farm/quickjs) | 🟢 Ongoing | 2 - ✅ Active | 20 days ago (2026-09-04 20:20:37 UTC) | 15 | C++ | DuckDB extension: quickjs by quackscience |
| 270 | [qvd](https://duckdb.org/community_extensions/extensions/qvd.html) | [DuckDB-QVD-Extension](https://github.com/snouhaud/DuckDB-QVD-Extension) | 🟢 Ongoing | 3 - 🟡 Stable | 63 days ago (2026-07-23 19:51:08 UTC) | 1 | Rust | An DuckDB extension to add QVD files read and write |
| 271 | [radio](https://duckdb.org/community_extensions/extensions/radio.html) | [radio](https://github.com/Query-farm/radio) | 🟢 Ongoing | 2 - ✅ Active | 12 days ago (2026-09-12 13:20:33 UTC) | 43 | C++ | Radio is a DuckDB extension by Query.Farm that brings real-time event streams... |
| 272 | [rapidfuzz](https://duckdb.org/community_extensions/extensions/rapidfuzz.html) | [rapidfuzz](https://github.com/Query-farm/rapidfuzz) | 🟢 Ongoing | 2 - ✅ Active | 20 days ago (2026-09-04 20:20:48 UTC) | 19 | C++ | DuckDB Community Extension adding RapidFuzz algorithms for search, deduplicat... |
| 273 | [raquet](https://duckdb.org/community_extensions/extensions/raquet.html) | [duckdb-raquet](https://github.com/CartoDB/duckdb-raquet) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-09-23 15:29:14 UTC) | 16 | C++ | DuckDB extension for reading Raquet format (raster data in Parquet with QUADB... |
| 274 | [raster](https://duckdb.org/community_extensions/extensions/raster.html) | [duckdb-raster](https://github.com/ahuarte47/duckdb-raster) | 🟢 Ongoing | 2 - ✅ Active | 16 days ago (2026-09-08 23:26:01 UTC) | 58 | C | DuckDB Extension for reading and writing raster files using SQL. |
| 275 | [rate_limit_fs](https://duckdb.org/community_extensions/extensions/rate_limit_fs.html) | [duckdb-rate-limit-filesystem](https://github.com/dentiny/duckdb-rate-limit-filesystem) | 🟢 Ongoing | 1 - 🔥 Very Active | 3 days ago (2026-09-22 07:47:03 UTC) | 2 | C++ | DuckDB extension: rate_limit_fs by dentiny |
| 276 | [rawduck](https://duckdb.org/community_extensions/extensions/rawduck.html) | [rawduck](https://github.com/quackscience/rawduck) | 🟢 Ongoing | 2 - ✅ Active | 25 days ago (2026-08-30 18:02:39 UTC) | 36 | C++ | Experimental RawMergeTree-like Extension for DuckDB |
| 277 | [rdf](https://duckdb.org/community_extensions/extensions/rdf.html) | [duck_rdf](https://github.com/nonodename/duck_rdf) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-09-24 21:14:08 UTC) | 38 | C++ | RDF file extension for DuckDB. Reads, writes & sparql supported |
| 278 | [read_dbf](https://duckdb.org/community_extensions/extensions/read_dbf.html) | [duckdb-dbf](https://github.com/tocharan/duckdb-dbf) | 🟢 Ongoing | 4 - 🟠 Stale | 211 days ago (2026-02-25 17:13:20 UTC) | 4 | C++ | Database connectivity extension by tocharan |
| 279 | [read_lines](https://duckdb.org/community_extensions/extensions/read_lines.html) | [duckdb_read_lines](https://github.com/teaguesterling/duckdb_read_lines) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-09-24 20:19:06 UTC) | 6 | C++ | Simple parsers for fast extraction from line-based files  |
| 280 | [read_stat](https://duckdb.org/community_extensions/extensions/read_stat.html) | [duckdb-read-stat](https://github.com/dylanmeysmans/duckdb-read-stat) | 🟢 Ongoing | 1 - 🔥 Very Active | 3 days ago (2026-09-22 04:00:19 UTC) | 35 | C | Read data sets from SAS, Stata, and SPSS from DuckDB with ReadStat |
| 281 | [redis](https://duckdb.org/community_extensions/extensions/redis.html) | [redis](https://github.com/Query-farm/redis) | 🟢 Ongoing | 2 - ✅ Active | 20 days ago (2026-09-04 20:20:55 UTC) | 17 | C++ | DuckDB Redis Client community extension |
| 282 | [robust](https://duckdb.org/community_extensions/extensions/robust.html) | [robust](https://github.com/robust-sql/robust) | ❓ Unknown | 2 - ✅ Active | 28 days ago (2026-08-28 01:01:14 UTC) | 7 | C++ | A DuckDB extension implementing Predicate Transfer to reduce cardinality expl... |
| 283 | [rocket](https://duckdb.org/community_extensions/extensions/rocket.html) | [duckdb-rocket](https://github.com/maxdemarzi/duckdb-rocket) | 🟢 Ongoing | 3 - 🟡 Stable | 33 days ago (2026-08-22 21:56:21 UTC) | 2 | Python | Training-free time-series classification in DuckDB: RocketPFN via a ROCKET fe... |
| 284 | [rrd](https://duckdb.org/community_extensions/extensions/rrd.html) | [duckdb-rrd](https://github.com/VertexStudio/duckdb-rrd) | ❓ Unknown | 3 - 🟡 Stable | 83 days ago (2026-07-03 18:31:26 UTC) | 0 | Rust | DuckDB extension: rrd by VertexStudio |
| 285 | [rusty_quack](https://duckdb.org/community_extensions/extensions/rusty_quack.html) | [extension-template-rs](https://github.com/duckdb/extension-template-rs) | ❓ Unknown | 3 - 🟡 Stable | 64 days ago (2026-07-23 06:05:55 UTC) | 115 | Rust | (Experimental) Template for Rust-based DuckDB extensions |
| 286 | [rusty_sheet](https://duckdb.org/community_extensions/extensions/rusty_sheet.html) | [rusty-sheet](https://github.com/redraiment/rusty-sheet) | 🟢 Ongoing | 4 - 🟠 Stale | 224 days ago (2026-02-13 02:27:56 UTC) | 79 | Rust | An Excel/WPS/OpenDocument Spreadsheets file reader for DuckDB |
| 287 | [s2raster](https://github.com/alitrack/duckdb-s2raster) | [duckdb-s2raster](https://github.com/alitrack/duckdb-s2raster) | ❓ Unknown | 2 - ✅ Active | 25 days ago (2026-08-31 06:31:52 UTC) | 1 | Rust | DuckDB extension: s2raster by alitrack |
| 288 | [salesforce](https://duckdb.org/community_extensions/extensions/salesforce.html) | [duckdb-salesforce](https://github.com/flozer/duckdb-salesforce) | 🟢 Ongoing | 1 - 🔥 Very Active | 3 days ago (2026-09-21 11:35:44 UTC) | 2 | C++ | Query Salesforce directly from DuckDB — read-only federated analytics over th... |
| 289 | [sazgar](https://duckdb.org/community_extensions/extensions/sazgar.html) | [Sazgar](https://github.com/Angelerator/Sazgar) | ❓ Unknown | 4 - 🟠 Stale | 126 days ago (2026-05-22 04:56:10 UTC) | 13 | HTML | DuckDB extension for system monitoring & intelligent SQL routing. 25+ functio... |
| 290 | [scalarfs](https://duckdb.org/community_extensions/extensions/scalarfs.html) | [duckdb_scalarfs](https://github.com/teaguesterling/duckdb_scalarfs) | 🟢 Ongoing | 1 - 🔥 Very Active | 4 days ago (2026-09-20 21:13:46 UTC) | 10 | C++ | A collection of simple virtual filesystems for treating scalar values as files. |
| 291 | [scrooge](https://duckdb.org/community_extensions/extensions/scrooge.html) | [Scrooge-McDuck](https://github.com/pdet/Scrooge-McDuck) | ❓ Unknown | 4 - 🟠 Stale | 143 days ago (2026-05-04 14:27:57 UTC) | 162 | C++ | DuckDB extension: scrooge by pdet |
| 292 | [se3](https://duckdb.org/community_extensions/extensions/se3.html) | [se3](https://github.com/jokasimr/se3) | 🟢 Ongoing | 3 - 🟡 Stable | 68 days ago (2026-07-19 09:45:05 UTC) | 1 | C++ | Duckdb extension for efficient rotation / translation operations on points in... |
| 293 | [semantic_profile](https://github.com/patricktrainer/duckdb-semantic-profile) | [duckdb-semantic-profile](https://github.com/patricktrainer/duckdb-semantic-profile) | ❓ Unknown | 1 - 🔥 Very Active | today (2026-09-24 16:11:25 UTC) | 0 | Rust | what is this? |
| 294 | [semantic_views](https://duckdb.org/community_extensions/extensions/semantic_views.html) | [duckdb-semantic-views](https://github.com/anentropic/duckdb-semantic-views) | 🟢 Ongoing | 1 - 🔥 Very Active | 6 days ago (2026-09-18 12:13:55 UTC) | 16 | Rust | Semantic Views for DuckDB. |
| 295 | [sheetreader](https://duckdb.org/community_extensions/extensions/sheetreader.html) | [sheetreader-duckdb](https://github.com/polydbms/sheetreader-duckdb) | ❓ Unknown | 4 - 🟠 Stale | 194 days ago (2026-03-15 11:03:07 UTC) | 58 | C++ | DuckDB extension: sheetreader by polydbms |
| 296 | [shellfs](https://duckdb.org/community_extensions/extensions/shellfs.html) | [shellfs](https://github.com/Query-farm/shellfs) | 🟢 Ongoing | 2 - ✅ Active | 20 days ago (2026-09-04 20:21:00 UTC) | 96 | C++ | DuckDB extension allowing shell commands to be used for input and output. |
| 297 | [sistat](https://duckdb.org/community_extensions/extensions/sistat.html) | [duckdb-sistat](https://github.com/fklezin/duckdb-sistat) | ❓ Unknown | 4 - 🟠 Stale | 200 days ago (2026-03-09 09:09:46 UTC) | 3 | C++ | DuckDB extension to query Slovenia's SiStat open data directly using SQL. No... |
| 298 | [sitemap](https://duckdb.org/community_extensions/extensions/sitemap.html) | [duckdb-sitemap](https://github.com/midwork-finds-jobs/duckdb-sitemap) | 🟢 Ongoing | 4 - 🟠 Stale | 219 days ago (2026-02-17 14:13:12 UTC) | 2 | C++ | DuckDB extension for parsing XML sitemaps from websites |
| 299 | [sitting_duck](https://duckdb.org/community_extensions/extensions/sitting_duck.html) | [sitting_duck](https://github.com/teaguesterling/sitting_duck) | 🟢 Ongoing | 1 - 🔥 Very Active | 2 days ago (2026-09-22 23:54:42 UTC) | 32 | C | Sitting Duck is a DuckDB extension that makes Abstract Syntax Trees (ASTs) fr... |
| 300 | [slack](https://github.com/dentiny/duckdb-slack) | [duckdb-slack](https://github.com/dentiny/duckdb-slack) | ❓ Unknown | 4 - 🟠 Stale | 217 days ago (2026-02-19 18:08:54 UTC) | 0 | C++ | DuckDB extension: slack by dentiny |
| 301 | [snowflake](https://duckdb.org/community_extensions/extensions/snowflake.html) | [duckdb-snowflake](https://github.com/iqea-ai/duckdb-snowflake) | 🟢 Ongoing | 1 - 🔥 Very Active | 2 days ago (2026-09-22 16:31:38 UTC) | 63 | C++ | A powerful DuckDB extension that enables seamless querying of Snowflake datab... |
| 302 | [splink_udfs](https://duckdb.org/community_extensions/extensions/splink_udfs.html) | [splink_udfs](https://github.com/moj-analytical-services/splink_udfs) | ❓ Unknown | 1 - 🔥 Very Active | 2 days ago (2026-09-22 16:21:47 UTC) | 6 | C++ | DuckDB extension: splink_udfs by moj-analytical-services |
| 303 | [splunk](https://duckdb.org/community_extensions/extensions/splunk.html) | [duckdb-splunk](https://github.com/smithclay/duckdb-splunk) | 🟢 Ongoing | 3 - 🟡 Stable | 52 days ago (2026-08-03 16:07:52 UTC) | 2 | C++ | read logs from splunk into duckdb |
| 304 | [spxlsx](https://duckdb.org/community_extensions/extensions/spxlsx.html) | [spxlsx](https://github.com/paulmupeters/spxlsx) | 🟢 Ongoing | 1 - 🔥 Very Active | 5 days ago (2026-09-19 20:58:46 UTC) | 5 | C++ | Duckdb extension to read sharepoint lists and excel |
| 305 | [sshfs](https://duckdb.org/community_extensions/extensions/sshfs.html) | [duckdb-sshfs](https://github.com/midwork-finds-jobs/duckdb-sshfs) | 🟢 Ongoing | 2 - ✅ Active | 10 days ago (2026-09-14 17:59:02 UTC) | 13 | C++ | DuckDB sshfs extension - Read and write files through ssh inside DuckDB |
| 306 | [st_read_multi](https://duckdb.org/community_extensions/extensions/st_read_multi.html) | [duckdb-ext-st-read-multi](https://github.com/yutannihilation/duckdb-ext-st-read-multi) | 🟢 Ongoing | 3 - 🟡 Stable | 38 days ago (2026-08-17 13:53:58 UTC) | 12 | Rust | A DuckDB extension to import multiple geospatial files with `ST_Read_Multi()` |
| 307 | [stac](https://duckdb.org/community_extensions/extensions/stac.html) | [duckdb-stac](https://github.com/ahuarte47/duckdb-stac) | 🟢 Ongoing | 2 - ✅ Active | 18 days ago (2026-09-07 06:38:13 UTC) | 24 | C++ | DuckDB extension for reading data from SpatioTemporal Asset Catalogs (STAC) u... |
| 308 | [stats_duck](https://duckdb.org/community_extensions/extensions/stats_duck.html) | [the-stats-duck](https://github.com/KoliStat/the-stats-duck) | 🟢 Ongoing | 1 - 🔥 Very Active | 3 days ago (2026-09-21 21:58:44 UTC) | 59 | C++ | A statistical computing toolkit for DuckDB. |
| 309 | [stochastic](https://duckdb.org/community_extensions/extensions/stochastic.html) | [stochastic](https://github.com/Query-farm/stochastic) | 🟢 Ongoing | 2 - ✅ Active | 20 days ago (2026-09-04 20:21:05 UTC) | 28 | C++ | A DuckDB extension that add comprehensive statistical distribution functions... |
| 310 | [storage_compat](https://duckdb.org/community_extensions/extensions/storage_compat.html) | [duckdb-storage-compat](https://github.com/carlopi/duckdb-storage-compat) | 🟢 Ongoing | 3 - 🟡 Stable | 36 days ago (2026-08-20 10:01:09 UTC) | 1 | C++ | DuckDB extension: storage_compat by carlopi |
| 311 | [substrait](https://duckdb.org/community_extensions/extensions/substrait.html) | [duckdb-substrait-extension](https://github.com/substrait-io/duckdb-substrait-extension) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-09-25 07:49:10 UTC) | 69 | C++ | DuckDB extension: substrait by substrait-io |
| 312 | [subtoken](https://duckdb.org/community_extensions/extensions/subtoken.html) | [subtoken](https://github.com/meridian-online/subtoken) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-09-25 09:10:20 UTC) | 0 | Python | A DuckDB scalar that embeds text with a bundled static model — no API key, no... |
| 313 | [sudan](https://duckdb.org/community_extensions/extensions/sudan.html) | [duckdb-sudan-](https://github.com/Osman-Geomatics93/duckdb-sudan-) | ❓ Unknown | 4 - 🟠 Stale | 217 days ago (2026-02-19 11:49:28 UTC) | 0 | Jupyter Notebook | DuckDB extension: sudan by Osman-Geomatics93 |
| 314 | [superhuman_docs](https://duckdb.org/community_extensions/extensions/superhuman_docs.html) | [duckdb-superhuman-docs](https://github.com/its-felix/duckdb-superhuman-docs) | 🟢 Ongoing | 3 - 🟡 Stable | 50 days ago (2026-08-05 22:27:19 UTC) | 2 | Rust | DuckDB extension: superhuman_docs by its-felix |
| 315 | [system_stats](https://duckdb.org/community_extensions/extensions/system_stats.html) | [system_stats](https://github.com/dentiny/system_stats) | 🟢 Ongoing | 1 - 🔥 Very Active | 3 days ago (2026-09-22 03:58:03 UTC) | 5 | C++ | DuckDB extension: system_stats by dentiny |
| 316 | [table_guard](https://duckdb.org/community_extensions/extensions/table_guard.html) | [duckdb-table-guard](https://github.com/yoogoc/duckdb-table-guard) | 🟢 Ongoing | 4 - 🟠 Stale | 134 days ago (2026-05-14 09:52:13 UTC) | 3 | C++ | A DuckDB extension for table-level access control |
| 317 | [table_inspector](https://duckdb.org/community_extensions/extensions/table_inspector.html) | [duckdb-table-inspector](https://github.com/dentiny/duckdb-table-inspector) | 🟢 Ongoing | 1 - 🔥 Very Active | 3 days ago (2026-09-22 07:53:39 UTC) | 4 | C++ | DuckDB extension: table_inspector by dentiny |
| 318 | [talib](https://duckdb.org/community_extensions/extensions/talib.html) | [atm_talib](https://github.com/neuesql/atm_talib) | 🟢 Ongoing | 2 - ✅ Active | 16 days ago (2026-09-08 22:39:27 UTC) | 8 | C++ | A duckdb TA-Lib to add technical analysis in Financial Markets with SQL easily |
| 319 | [tarfs](https://duckdb.org/community_extensions/extensions/tarfs.html) | [duckdb_tarfs](https://github.com/Maxxen/duckdb_tarfs) | ❓ Unknown | 4 - 🟠 Stale | over a year ago (2024-08-26 11:01:47 UTC) | 12 | C++ | DuckDB extension: tarfs by Maxxen |
| 320 | [tera](https://duckdb.org/community_extensions/extensions/tera.html) | [tera](https://github.com/Query-farm/tera) | 🟢 Ongoing | 2 - ✅ Active | 20 days ago (2026-09-04 20:21:10 UTC) | 9 | C++ | DuckDB extension: tera |
| 321 | [textplot](https://duckdb.org/community_extensions/extensions/textplot.html) | [textplot](https://github.com/Query-farm/textplot) | 🟢 Ongoing | 2 - ✅ Active | 20 days ago (2026-09-04 20:18:08 UTC) | 28 | C++ | A DuckDB community extension that enables text-based data visualization direc... |
| 322 | [three_d](https://duckdb.org/community_extensions/extensions/three_d.html) | [duckdb-3d](https://github.com/cityjson/duckdb-3d) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-09-24 08:15:13 UTC) | 4 | C++ | (Experimental) DuckDB extension to process 3D geomerty |
| 323 | [title_mapper](https://duckdb.org/community_extensions/extensions/title_mapper.html) | [duckdb-title-mapper](https://github.com/martin-conur/duckdb-title-mapper) | 🟢 Ongoing | 3 - 🟡 Stable | 40 days ago (2026-08-16 00:22:39 UTC) | 4 | Rust | DuckDB extension: title_mapper by martin-conur |
| 324 | [toml](https://duckdb.org/community_extensions/extensions/toml.html) | [duckdb-toml](https://github.com/vergenzt/duckdb-toml) | 🟢 Ongoing | 3 - 🟡 Stable | 63 days ago (2026-07-24 05:08:13 UTC) | 1 | C++ | Parse TOML format in DuckDB |
| 325 | [tpch_rust](https://duckdb.org/community_extensions/extensions/tpch_rust.html) | [duckdb-tpch-rust](https://github.com/guillesd/duckdb-tpch-rust) | ❓ Unknown | 4 - 🟠 Stale | 108 days ago (2026-06-08 15:40:17 UTC) | 0 | Rust | DuckDB extension to generate tpch tables using tpch-rs |
| 326 | [tributary](https://duckdb.org/community_extensions/extensions/tributary.html) | [tributary](https://github.com/Query-farm/tributary) | ❓ Unknown | 2 - ✅ Active | 19 days ago (2026-09-05 17:19:31 UTC) | 57 | C++ | A DuckDB Extension for Kafka |
| 327 | [trino_parity](https://duckdb.org/community_extensions/extensions/trino_parity.html) | [duckdb-trino-parity-extension](https://github.com/brikk/duckdb-trino-parity-extension) | 🟢 Ongoing | 2 - ✅ Active | 19 days ago (2026-09-05 13:04:57 UTC) | 1 | C++ | An extension adding functions to duckdb to exactly match Trino function behav... |
| 328 | [tsfile](https://duckdb.org/community_extensions/extensions/tsfile.html) | [tsfile-duckdb](https://github.com/TimechoLab/tsfile-duckdb) | 🟢 Ongoing | 2 - ✅ Active | 15 days ago (2026-09-10 10:09:53 UTC) | 6 | C++ | DuckDB extension: tsfile by TimechoLab |
| 329 | [tsid](https://duckdb.org/community_extensions/extensions/tsid.html) | [tsid](https://github.com/Query-farm/tsid) | 🟢 Ongoing | 2 - ✅ Active | 20 days ago (2026-09-04 20:21:19 UTC) | 7 | C++ | TSID Extension for DuckDB  |
| 330 | [turbovec](https://github.com/alitrack/duckdb_turbovec) | [duckdb_turbovec](https://github.com/alitrack/duckdb_turbovec) | ❓ Unknown | 3 - 🟡 Stable | 58 days ago (2026-07-28 21:52:38 UTC) | 7 | Rust | DuckDB extension: turbovec by alitrack |
| 331 | [ulid](https://duckdb.org/community_extensions/extensions/ulid.html) | [duckdb_ulid](https://github.com/Maxxen/duckdb_ulid) | ❓ Unknown | 4 - 🟠 Stale | over a year ago (2024-07-09 09:35:50 UTC) | 25 | C++ | DuckDB extension: ulid by Maxxen |
| 332 | [urlpattern](https://duckdb.org/community_extensions/extensions/urlpattern.html) | [duckdb_urlpattern](https://github.com/teaguesterling/duckdb_urlpattern) | 🟢 Ongoing | 1 - 🔥 Very Active | 4 days ago (2026-09-21 01:28:16 UTC) | 9 | C++ | An implementation of URLPattern for DuckDB |
| 333 | [us_address_standardizer](https://duckdb.org/community_extensions/extensions/us_address_standardizer.html) | [duckdb-address-standardizer](https://github.com/ericmanning/duckdb-address-standardizer) | 🟢 Ongoing | 1 - 🔥 Very Active | 6 days ago (2026-09-18 23:45:24 UTC) | 4 | C | DuckDB extension for parsing and standardizing (USA) postal addresses using P... |
| 334 | [valhalla_routing](https://duckdb.org/community_extensions/extensions/valhalla_routing.html) | [duckdb-valhalla-routing](https://github.com/midwork-finds-jobs/duckdb-valhalla-routing) | 🟢 Ongoing | 4 - 🟠 Stale | 219 days ago (2026-02-17 11:36:12 UTC) | 9 | Makefile | WIP: Attempt to package valhalla routing engine to duckdb |
| 335 | [vindex](https://duckdb.org/community_extensions/extensions/vindex.html) | [duckdb-vector-index](https://github.com/Icemap/duckdb-vector-index) | ❓ Unknown | 3 - 🟡 Stable | 71 days ago (2026-07-16 10:06:50 UTC) | 11 | C++ | A DuckDB extension providing HNSW, IVF, DiskANN, and SPANN vector indexes wit... |
| 336 | [waddle](https://duckdb.org/community_extensions/extensions/waddle.html) | [extension-template](https://github.com/duckdb/extension-template) | 🟢 Ongoing | 4 - 🟠 Stale | 95 days ago (2026-06-22 10:58:32 UTC) | 290 | Python | Template for DuckDB extensions to help you develop, test and deploy a custom... |
| 337 | [warc](https://duckdb.org/community_extensions/extensions/warc.html) | [duckdb_warc](https://github.com/midwork-finds-jobs/duckdb_warc) | ❓ Unknown | 4 - 🟠 Stale | 231 days ago (2026-02-05 15:33:27 UTC) | 7 | Rust | DuckDB extension for parsing WARC files |
| 338 | [web_archive](https://duckdb.org/community_extensions/extensions/web_archive.html) | [duckdb-web-archive](https://github.com/midwork-finds-jobs/duckdb-web-archive) | 🟢 Ongoing | 3 - 🟡 Stable | 89 days ago (2026-06-27 17:30:16 UTC) | 23 | C++ | DuckDB extension to fetch pages from Wayback Machine & Common Crawl |
| 339 | [web_search](https://duckdb.org/community_extensions/extensions/web_search.html) | [duckdb-web-search](https://github.com/midwork-finds-jobs/duckdb-web-search) | 🟢 Ongoing | 4 - 🟠 Stale | 157 days ago (2026-04-20 21:51:13 UTC) | 0 | C++ | Web/HTTP functionality extension by midwork-finds-jobs |
| 340 | [webbed](https://duckdb.org/community_extensions/extensions/webbed.html) | [duckdb_webbed](https://github.com/teaguesterling/duckdb_webbed) | 🟢 Ongoing | 1 - 🔥 Very Active | 4 days ago (2026-09-21 03:45:35 UTC) | 76 | C++ | A comprehensive XML and HTML processing extension for DuckDB that enables SQL... |
| 341 | [webdavfs](https://duckdb.org/community_extensions/extensions/webdavfs.html) | [duckdb-webdavfs](https://github.com/midwork-finds-jobs/duckdb-webdavfs) | 🟢 Ongoing | 2 - ✅ Active | 10 days ago (2026-09-14 17:59:01 UTC) | 1 | C++ | DuckDB WebDAVfs Extension - WebDAV filesystem support for DuckDB |
| 342 | [webmacro](https://duckdb.org/community_extensions/extensions/webmacro.html) | [webmacro](https://github.com/Query-farm/webmacro) | 🟢 Ongoing | 2 - ✅ Active | 20 days ago (2026-09-04 20:21:23 UTC) | 16 | C++ | DuckDB WebMacro: Share and Load your SQL Macros via gists |
| 343 | [whisper](https://duckdb.org/community_extensions/extensions/whisper.html) | [duckdb-whisper](https://github.com/tobilg/duckdb-whisper) | 🟢 Ongoing | 3 - 🟡 Stable | 48 days ago (2026-08-07 11:33:05 UTC) | 12 | C++ | Use whisper.cpp within DuckDB to translate / transpile speech to text |
| 344 | [wireduck](https://duckdb.org/community_extensions/extensions/wireduck.html) | [wireduck](https://github.com/hyehudai/wireduck) | ❓ Unknown | 4 - 🟠 Stale | over a year ago (2025-09-23 21:22:03 UTC) | 48 | C++ | Duckdb extension to read pcap files |
| 345 | [yaml](https://duckdb.org/community_extensions/extensions/yaml.html) | [duckdb_yaml](https://github.com/teaguesterling/duckdb_yaml) | 🟢 Ongoing | 1 - 🔥 Very Active | 4 days ago (2026-09-21 01:28:18 UTC) | 22 | C++ |  A DuckDB to read and work with YAML files in a similar way to JSON files (al... |
| 346 | [yardstick](https://duckdb.org/community_extensions/extensions/yardstick.html) | [yardstick](https://github.com/sidequery/yardstick) | 🟢 Ongoing | 2 - ✅ Active | 10 days ago (2026-09-14 17:22:22 UTC) | 58 | Rust | A DuckDB extension implementing Measures in SQL |
| 347 | [zarr](https://duckdb.org/community_extensions/extensions/zarr.html) | [duckdb-zarr](https://github.com/xqlsystems/duckdb-zarr) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-09-25 04:04:09 UTC) | 59 | Rust | Query Zarr stores with SQL directly from DuckDB |
| 348 | [zeek](https://duckdb.org/community_extensions/extensions/zeek.html) | [zeek-duckdb](https://github.com/ynadji/zeek-duckdb) | 🟢 Ongoing | 4 - 🟠 Stale | 163 days ago (2026-04-14 22:02:22 UTC) | 5 | C++ | read_zeek table function to read Zeek TSV logs into DuckDB |
| 349 | [zim](https://duckdb.org/community_extensions/extensions/zim.html) | [duckdb_zim](https://github.com/teaguesterling/duckdb_zim) | 🟢 Ongoing | 1 - 🔥 Very Active | 4 days ago (2026-09-21 01:28:05 UTC) | 7 | C++ | DuckDB extension for working with zim files |
| 350 | [zipfs](https://duckdb.org/community_extensions/extensions/zipfs.html) | [duckdb-zipfs](https://github.com/isaacbrodsky/duckdb-zipfs) | 🟢 Ongoing | 1 - 🔥 Very Active | 2 days ago (2026-09-23 02:08:34 UTC) | 69 | C++ | DuckDB extension to read files within zip archives. |

</details>
## Appendix: DuckDB Release Information

### Current Release Context

DuckDB follows **semantic versioning** with regular releases. For complete and up-to-date release information, see the official [**DuckDB Release Calendar**](https://duckdb.org/release_calendar.html).

### Upcoming Releases

|| Version | Planned Date | LTS |
||---------|-------------|-----|
|| v2.0.1 📅 | 2026-11-16 |  |
|| v2.0.0 📅 | 2026-10-21 |  |
|| v1.5.6 📅 | 2026-09-28 |  |

### Recent Releases

|| Version | Release Date | Codename | Named After | LTS | Status |
||---------|--------------|----------|-------------|-----|--------|
|| **v1.5.5** | 2026-07-22 | – | – |  | Active |
|| **v1.5.4** | 2026-06-17 | – | – |  | Active |
|| **v1.4.5** | 2026-06-17 | – | – | ✓ | Active |
|| **v1.5.3** | 2026-05-20 | – | – |  | Active |
|| **v1.5.2** | 2026-04-13 | – | – |  | Active |
|| **v1.5.1** | 2026-03-23 | – | – |  | Active |
|| **v1.5.0** | 2026-03-09 | Variegata | *Paradise shelduck* |  | EOL |
|| **v1.4.4** | 2026-01-27 | – | – | ✓ | Active |
|| **v1.4.3** | 2025-12-09 | – | – | ✓ | Active |
|| **v1.4.2** | 2025-11-12 | – | – | ✓ | Active |
|| **v1.4.1** | 2025-10-07 | – | – | ✓ | Active |
|| **v1.4.0** | 2025-09-16 | Andium | *Andean teal* | ✓ | EOL |
|| **v1.3.2** | 2025-07-08 | – | – |  | Active |
|| **v1.3.1** | 2025-06-16 | – | – |  | Active |
|| **v1.3.0** | 2025-05-21 | Ossivalis | *Goldeneye duck* |  | EOL |

### Historical Releases (Pre‑1.0)

See full table in the repository: [Historical Pre‑1.0 Releases](https://github.com/Mjboothaus/duckdb-extensions-analysis/blob/main/docs/HISTORICAL_PRE_1_0_RELEASES.md)

**Note:** For releases prior to v0.5.0, please refer to the [official DuckDB documentation](https://duckdb.org/docs/installation/) for historical version information.

### Key Milestones

- **🎉 v1.0.0** (June 2024): First stable release - "Snow duck"
- **📈 v0.10.0** (Feb 2024): Last pre-1.0 feature release
- **🦆 v0.5.0** (Sept 2022): First release with duck codenames
- **🚀 Project Started**: 2019 (first release v0.1.0)

### LTS Support

- **v1.4.0 (Andium)**: September 2025 → September 2026
- Previous LTS releases have ended or will end as new LTS versions are released

### Release Resources

- **📅 Release Calendar**: [duckdb.org/release_calendar.html](https://duckdb.org/release_calendar.html)
- **📊 Release Data (CSV)**: [duckdb.org/data/duckdb-releases.csv](https://duckdb.org/data/duckdb-releases.csv)
- **📦 GitHub Releases**: [https://github.com/duckdb/duckdb/releases](https://github.com/duckdb/duckdb/releases)
- **📰 Release Notes**: [duckdb.org/news/](https://duckdb.org/news/)
- **🛠️ Development Roadmap**: [duckdb.org/roadmap.html](https://duckdb.org/roadmap.html)

<p class="fine-print">Data sourced from the official <a href="https://duckdb.org/data/duckdb-releases.csv">DuckDB releases CSV</a>. For the most current information, see the <a href="https://duckdb.org/release_calendar.html">release calendar</a>.</p>
## Appendix: DuckDB version compatibility (experimental)
This section summarises *on-demand* compatibility checks that attempt to `INSTALL` and `LOAD` extensions across a small set of DuckDB versions.

_No compatibility testing results were recorded for this run._

## Data quality and limitations

📖 **[Full documentation](https://github.com/Mjboothaus/duckdb-extensions-analysis/blob/main/docs/DATA_QUALITY_LIMITATIONS.md)**

**Short version:**

- Sources: DuckDB docs (core), community-extensions registry, GitHub API (repo metadata), DuckDB releases CSV + release calendar.
- This report reflects what those sources provide. Where data is missing or closed, we show that clearly.

**Known issues (what "NOT FOUND" etc. usually means):**

- Closed source: Some extensions (e.g. MotherDuck, Vortex) have no public repo.
- Moved/renamed: Upstream URLs changed after registration.
- Private: Repositories are not public yet.
- Metadata errors: Incorrect URLs in upstream data.

**Other caveats:**

- Truncated names: A few registry entries truncate repo names (e.g. query-farm/airpor). We correct known cases; some may remain until fixed upstream.
- Activity signal: "Last Activity" = last git push; stable projects may be quiet but healthy.
- Stars: Popularity signal, not usage or quality.
- Install check: Verifies INSTALL succeeds; does not exercise functionality.

**Report issues:**

- Report issues to [this analysis tool repo](https://github.com/Mjboothaus/duckdb-extensions-analysis/issues) or directly to the specific extension's repository.
- Reporting issues here helps improve the analysis tool for everyone!

<p class="fine-print">Last updated: 2026-09-25</p>
