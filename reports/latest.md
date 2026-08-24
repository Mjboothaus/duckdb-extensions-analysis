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
- **348** total extensions tracked (**29** core, **319** community)
- **54 / 348** extensions updated in the last 7 days
- **183 / 348** extensions updated in the last 30 days
- **1** community repositories are archived
- **99** community extensions have unknown/repo issues (missing or inaccessible repositories)

### Highlights
#### Most active (last 7 days)
| Extension | Repository | Last activity |
|---|---|---|
| [ai](https://duckdb.org/community_extensions/extensions/ai.html) | [duckdb-ai](https://github.com/leonardovida/duckdb-ai) | today (2026-08-23 19:59:40 UTC) |
| [anofox_forecast](https://duckdb.org/community_extensions/extensions/anofox_forecast.html) | [anofox-forecast](https://github.com/DataZooDE/anofox-forecast) | today (2026-08-23 19:20:30 UTC) |
| [anofox_tabfm](https://duckdb.org/community_extensions/extensions/anofox_tabfm.html) | [anofox-tabfm](https://github.com/DataZooDE/anofox-tabfm) | today (2026-08-23 11:02:49 UTC) |
| [cityjson](https://duckdb.org/community_extensions/extensions/cityjson.html) | [duckdb-cityjson](https://github.com/cityjson/duckdb-cityjson) | today (2026-08-23 18:54:50 UTC) |
| [clamp](https://duckdb.org/community_extensions/extensions/clamp.html) | [duckdb_clamp](https://github.com/oglego/duckdb_clamp) | today (2026-08-23 10:56:21 UTC) |

#### Most starred (community)
| Extension | Repository | Stars |
|---|---|---:|
| [duckpgq](https://duckdb.org/community_extensions/extensions/duckpgq.html) | [duckpgq-extension](https://github.com/cwida/duckpgq-extension) | 481 |
| [flock](https://duckdb.org/community_extensions/extensions/flock.html) | [flock](https://github.com/dais-polymtl/flock) | 355 |
| [gsheets](https://duckdb.org/community_extensions/extensions/gsheets.html) | [duckdb_gsheets](https://github.com/evidence-dev/duckdb_gsheets) | 349 |
| [airport](https://duckdb.org/community_extensions/extensions/airport.html) | [airport](https://github.com/Query-farm/airport) | 347 |
| [prql](https://duckdb.org/community_extensions/extensions/prql.html) | [duckdb-prql](https://github.com/ywelsch/duckdb-prql) | 329 |

### How to read the report
- **Status** is a repository signal (ongoing / archived / unknown).
- **Activity** is based on the last git push; quiet projects can still be healthy.
- Use the tables below to drill into **Core Extensions** and **Community Extensions**.

---
## Summary

### 📊 Quick Stats (with trends)

| **Metric** | **Current** | **Change** |
|------------|-------------|------------|
| **Total Extensions** | 348 | +9 🔼 |
| **Core Extensions** | 29 | → Stable |
| **Community Extensions** | 319 | +9 🔼 |
| **Recently Active** (≤ 30 days) | 183 (52.6%) | +20 🔼 |
| **Very Active** (≤ 7 days) | 54 (15.5%) | — |

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
| 1 | [autocomplete](https://duckdb.org/docs/current/core_extensions/autocomplete) | [duckdb/duckdb](https://github.com/duckdb/duckdb/tree/main/extension/autocomplete) | 🟢 Ongoing | 5 days ago (2026-08-18 19:25:47 UTC) | N/A (part of core DuckDB repo) | C++ | Core DuckDB extension: autocomplete |
| 2 | [avro](https://duckdb.org/docs/current/core_extensions/avro) | [duckdb-avro](https://github.com/duckdb/duckdb-avro) | 🟢 Ongoing | 2 days ago (2026-08-21 07:36:21 UTC) | 35 | C++ | Apache Avro format support |
| 3 | [aws](https://duckdb.org/docs/current/core_extensions/aws) | [duckdb-aws](https://github.com/duckdb/duckdb-aws) | 🟢 Ongoing | 11 days ago (2026-08-12 19:42:49 UTC) | 65 | C++ | AWS S3 integration |
| 4 | [azure](https://duckdb.org/docs/current/core_extensions/azure) | [duckdb-azure](https://github.com/duckdb/duckdb-azure) | 🟢 Ongoing | 11 days ago (2026-08-12 15:20:48 UTC) | 78 | C++ | Azure extension for DuckDB |
| 5 | [delta](https://duckdb.org/docs/current/core_extensions/delta) | [duckdb-delta](https://github.com/duckdb/duckdb-delta) | 🟢 Ongoing | 2 days ago (2026-08-21 15:20:03 UTC) | 228 | C++ | DuckDB extension for Delta Lake |
| 6 | [ducklake](https://duckdb.org/docs/current/core_extensions/ducklake) | [duckdb/ducklake](https://github.com/duckdb/ducklake) | 🟢 Ongoing | 32 days ago | N/A (part of core DuckDB repo) | C++ | Delta Lake support via DuckLake (different from delta extension) |
| 7 | [encodings](https://duckdb.org/docs/current/core_extensions/encodings) | [duckdb-encodings](https://github.com/duckdb/duckdb-encodings) | 🟢 Ongoing | 188 days ago (2026-02-16 11:43:18 UTC) | 15 | C++ | Character encoding support |
| 8 | [excel](https://duckdb.org/docs/current/core_extensions/excel) | [duckdb-excel](https://github.com/duckdb/duckdb-excel) | 🟢 Ongoing | 87 days ago (2026-05-28 14:57:36 UTC) | 61 | C++ | Excel extension for DuckDB |
| 9 | [fts](https://duckdb.org/docs/current/core_extensions/full_text_search) | [duckdb-fts](https://github.com/duckdb/duckdb-fts) | 🟢 Ongoing | 5 days ago (2026-08-18 09:27:04 UTC) | 42 | C++ | Full-text search functionality |
| 10 | [httpfs](https://duckdb.org/docs/current/core_extensions/httpfs/overview) | [duckdb-httpfs](https://github.com/duckdb/duckdb-httpfs) | 🟢 Ongoing | 3 days ago (2026-08-20 13:53:39 UTC) | 59 | C++ | HTTP/S3 filesystem support |
| 11 | [iceberg](https://duckdb.org/docs/current/core_extensions/iceberg/overview) | [duckdb-iceberg](https://github.com/duckdb/duckdb-iceberg) | 🟢 Ongoing | 2 days ago (2026-08-21 08:55:46 UTC) | 428 | C++ | Apache Iceberg format support |
| 12 | [icu](https://duckdb.org/docs/current/core_extensions/icu) | [duckdb/duckdb](https://github.com/duckdb/duckdb/tree/main/extension/icu) | 🟢 Ongoing | 5 days ago (2026-08-18 16:39:49 UTC) | N/A (part of core DuckDB repo) | C++ | Core DuckDB extension: icu |
| 13 | [inet](https://duckdb.org/docs/current/core_extensions/inet) | [duckdb-inet](https://github.com/duckdb/duckdb-inet) | 🟢 Ongoing | 276 days ago (2025-11-20 22:54:12 UTC) | 14 | C++ | Internet address data types |
| 14 | [json](https://duckdb.org/docs/current/data/json/overview) | [duckdb/duckdb](https://github.com/duckdb/duckdb/tree/main/extension/json) | 🟢 Ongoing | 3 days ago (2026-08-20 09:13:52 UTC) | N/A (part of core DuckDB repo) | C++ | Core DuckDB extension: json |
| 15 | [lance](https://duckdb.org/docs/current/core_extensions/lance) | [lance-duckdb](https://github.com/lance-format/lance-duckdb) | 🟢 Ongoing | 23 days ago (2026-08-01 01:40:17 UTC) | 125 | C++ | The lance extensions for DuckDB enable reading and writing of lance tables. |
| 16 | [motherduck](https://duckdb.org/docs/current/core_extensions/motherduck) | [duckdb/duckdb](https://github.com/duckdb/duckdb) *(Third Party - Closed source - maintained by MotherDuck Inc.)* | 🟢 Ongoing | 32 days ago | N/A (part of core DuckDB repo) | C++ | Core DuckDB extension: motherduck |
| 17 | [mysql](https://duckdb.org/docs/current/core_extensions/mysql) | [duckdb-mysql](https://github.com/duckdb/duckdb-mysql) | 🟢 Ongoing | 3 days ago (2026-08-20 23:34:36 UTC) | 101 | C++ | MySQL database connectivity |
| 18 | [odbc](https://duckdb.org/docs/current/core_extensions/odbc/overview) | [odbc-scanner](https://github.com/duckdb/odbc-scanner) | 🟢 Ongoing | 85 days ago (2026-05-30 11:58:55 UTC) | 38 | C++ | DuckDB ODBC extension |
| 19 | [parquet](https://duckdb.org/docs/current/data/parquet/overview) | [duckdb/duckdb](https://github.com/duckdb/duckdb/tree/main/extension/parquet) | 🟢 Ongoing | 3 days ago (2026-08-20 12:52:45 UTC) | N/A (part of core DuckDB repo) | C++ | Core DuckDB extension: parquet |
| 20 | [postgres](https://duckdb.org/docs/current/core_extensions/postgres/overview) | [duckdb-postgres](https://github.com/duckdb/duckdb-postgres) | 🟢 Ongoing | 2 days ago (2026-08-21 10:13:49 UTC) | 370 | C++ | PostgreSQL database connectivity |
| 21 | [quack](https://duckdb.org/docs/current/core_extensions/quack) | [duckdb-quack](https://github.com/duckdb/duckdb-quack) | 🟢 Ongoing | 3 days ago (2026-08-20 15:51:27 UTC) | 161 | C++ | Quack remote protocol |
| 22 | [spatial](https://duckdb.org/docs/current/core_extensions/spatial/overview) | [duckdb-spatial](https://github.com/duckdb/duckdb-spatial) | 🟢 Ongoing | 8 days ago (2026-08-15 19:25:05 UTC) | 702 | C++ | Geospatial data types and functions |
| 23 | [sqlite](https://duckdb.org/docs/current/core_extensions/sqlite) | [duckdb-sqlite](https://github.com/duckdb/duckdb-sqlite) | 🟢 Ongoing | 3 days ago (2026-08-20 14:39:41 UTC) | 290 | C++ | DuckDB extension to read and write to SQLite databases |
| 24 | [tpcds](https://duckdb.org/docs/current/core_extensions/tpcds) | [duckdb/duckdb](https://github.com/duckdb/duckdb/tree/main/extension/tpcds) | 🟢 Ongoing | 13 days ago (2026-08-10 15:14:35 UTC) | N/A (part of core DuckDB repo) | C++ | Core DuckDB extension: tpcds |
| 25 | [tpch](https://duckdb.org/docs/current/core_extensions/tpch) | [duckdb/duckdb](https://github.com/duckdb/duckdb/tree/main/extension/tpch) | 🟢 Ongoing | 4 days ago (2026-08-19 08:30:16 UTC) | N/A (part of core DuckDB repo) | C++ | Core DuckDB extension: tpch |
| 26 | [ui](https://duckdb.org/docs/current/core_extensions/ui) | [duckdb-ui](https://github.com/duckdb/duckdb-ui) | 🟢 Ongoing | 24 days ago (2026-07-30 20:41:06 UTC) | 462 | C++ | Browser-based user interface for DuckDB |
| 27 | [unity_catalog](https://duckdb.org/docs/current/core_extensions/unity_catalog) | [unity_catalog](https://github.com/duckdb/unity_catalog) | 🟢 Ongoing | 2 days ago (2026-08-22 06:39:11 UTC) | 108 | C++ | Proof-of-concept extension combining the delta extension with Unity Catalog |
| 28 | [vortex](https://duckdb.org/docs/current/core_extensions/vortex) | [duckdb/duckdb](https://github.com/duckdb/duckdb) *(Third Party - Closed source - third-party extension)* | 🟢 Ongoing | 32 days ago | N/A (part of core DuckDB repo) | C++ | Core DuckDB extension: vortex |
| 29 | [vss](https://duckdb.org/docs/current/core_extensions/vss) | [duckdb-vss](https://github.com/duckdb/duckdb-vss) | 🟢 Ongoing | 61 days ago (2026-06-23 11:03:14 UTC) | 263 | C++ | Vector similarity search |

</details>

---
---
## Community Extensions

Third-party extensions maintained by the community


**Total:** 319 extensions | 🔥 Very Active (≤7d): 54 | ✅ Active (≤30d): 129 | 🟡 Stable (≤90d): 54 | 🟠 Stale (>90d): 82

<details open markdown="1">
<summary>Click to expand/collapse community extensions table</summary>

| # | Extension | Repository | Status | Activity | Last Activity | Stars | Language | Description |
|---|-----------|------------|--------|----------|---------------|-------|----------|-------------|
| 1 | [a5](https://duckdb.org/community_extensions/extensions/a5.html) | [a5](https://github.com/Query-farm/a5) | 🟢 Ongoing | 2 - ✅ Active | 30 days ago (2026-07-25 04:26:43 UTC) | 15 | C++ | A5 Geospatial Extension for DuckDB |
| 2 | [acp](https://duckdb.org/community_extensions/extensions/acp.html) | [duckdb-acp](https://github.com/sidequery/duckdb-acp) | 🟡 Archived | 4 - 🟠 Stale | 256 days ago (2025-12-11 03:36:46 UTC) | 57 | Rust | Use Claude Code & other AI agents from inside DuckDB via extension |
| 3 | [adbc](https://duckdb.org/community_extensions/extensions/adbc.html) | [duckdb-adbc-client](https://github.com/columnar-tech/duckdb-adbc-client) | 🟢 Ongoing | 1 - 🔥 Very Active | 2 days ago (2026-08-21 15:40:26 UTC) | 45 | C++ | ADBC Client for DuckDB  |
| 4 | [adbc_scanner](https://duckdb.org/community_extensions/extensions/adbc_scanner.html) | [adbc_scanner](https://github.com/Query-farm/adbc_scanner) | 🟢 Ongoing | 2 - ✅ Active | 12 days ago (2026-08-11 22:38:01 UTC) | 19 | C++ | A DuckDB ADBC Scanner Extension - adds support for using ADBC drivers with Du... |
| 5 | [agent_data](https://duckdb.org/community_extensions/extensions/agent_data.html) | [agent_data_duckdb](https://github.com/axsaucedo/agent_data_duckdb) | 🟢 Ongoing | 2 - ✅ Active | 23 days ago (2026-08-01 03:42:26 UTC) | 24 | Rust | DuckDB extension: agent_data by axsaucedo |
| 6 | [ai](https://duckdb.org/community_extensions/extensions/ai.html) | [duckdb-ai](https://github.com/leonardovida/duckdb-ai) | ❓ Unknown | 1 - 🔥 Very Active | today (2026-08-23 19:59:40 UTC) | 8 | C++ | Enhance DuckDB with AI functions, supporting all providers as well as local m... |
| 7 | [airport](https://duckdb.org/community_extensions/extensions/airport.html) | [airport](https://github.com/Query-farm/airport) | 🟢 Ongoing | 2 - ✅ Active | 30 days ago (2026-07-25 04:26:50 UTC) | 347 | C++ | The Airport extension for DuckDB, enables the use of Arrow Flight with DuckDB |
| 8 | [aixchess](https://duckdb.org/community_extensions/extensions/aixchess.html) | [aix](https://github.com/thomas-daniels/aix) | 🟢 Ongoing | 4 - 🟠 Stale | 147 days ago (2026-03-29 12:16:27 UTC) | 27 | Rust | Aix: Efficiently storing and querying chess game collections |
| 9 | [altertable](https://duckdb.org/community_extensions/extensions/altertable.html) | [duckdb-altertable](https://github.com/altertable-ai/duckdb-altertable) | 🟢 Ongoing | 1 - 🔥 Very Active | 2 days ago (2026-08-21 20:15:30 UTC) | 0 | C++ | Query Altertable's lakehouse directly from your local DuckDB |
| 10 | [anndata](https://duckdb.org/community_extensions/extensions/anndata.html) | [anndata-duckdb-extension](https://github.com/honicky/anndata-duckdb-extension) | 🟢 Ongoing | 1 - 🔥 Very Active | 3 days ago (2026-08-20 07:12:50 UTC) | 9 | C++ | Attach and AnnData file in duckdb and query it with SQL.  Perform SQL over gr... |
| 11 | [anofox_forecast](https://duckdb.org/community_extensions/extensions/anofox_forecast.html) | [anofox-forecast](https://github.com/DataZooDE/anofox-forecast) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-08-23 19:20:30 UTC) | 37 | C++ | Statistical timeseries forecasting in DuckDB |
| 12 | [anofox_optimize](https://duckdb.org/community_extensions/extensions/anofox_optimize.html) | [anofox-optimize](https://github.com/DataZooDE/anofox-optimize) | 🟢 Ongoing | 2 - ✅ Active | 9 days ago (2026-08-14 09:05:47 UTC) | 2 | C++ | Combinatorial decision algorithms as DuckDB functions — bin packing, knapsack... |
| 13 | [anofox_scenario](https://duckdb.org/community_extensions/extensions/anofox_scenario.html) | [anofox-scenario](https://github.com/DataZooDE/anofox-scenario) | 🟢 Ongoing | 2 - ✅ Active | 15 days ago (2026-08-09 00:30:24 UTC) | 2 | C++ | DuckDB extension for Git-like database branching. Create isolated scenarios f... |
| 14 | [anofox_similarity](https://duckdb.org/community_extensions/extensions/anofox_similarity.html) | [anofox-similarity](https://github.com/DataZooDE/anofox-similarity) | 🟢 Ongoing | 2 - ✅ Active | 15 days ago (2026-08-09 00:16:19 UTC) | 2 | C++ | DuckDB extension for multi-modal product similarity for manufacturing supply... |
| 15 | [anofox_statistics](https://duckdb.org/community_extensions/extensions/anofox_statistics.html) | [anofox-statistics](https://github.com/DataZooDE/anofox-statistics) | 🟢 Ongoing | 2 - ✅ Active | 8 days ago (2026-08-15 09:51:24 UTC) | 14 | C++ | A DuckDB extension for statistical regression analysis, providing OLS, Ridge,... |
| 16 | [anofox_tabfm](https://duckdb.org/community_extensions/extensions/anofox_tabfm.html) | [anofox-tabfm](https://github.com/DataZooDE/anofox-tabfm) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-08-23 11:02:49 UTC) | 4 | C++ | DuckDB extension for tabular foundation models — zero-shot classification & r... |
| 17 | [anofox_tabular](https://duckdb.org/community_extensions/extensions/anofox_tabular.html) | [anofox-tabular](https://github.com/DataZooDE/anofox-tabular) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-08-22 14:01:09 UTC) | 17 | C++ | A duckdb extension which combines data quality and data preparation tools for... |
| 18 | [anofox_visualization](https://duckdb.org/community_extensions/extensions/anofox_visualization.html) | [anofox-visualization](https://github.com/DataZooDE/anofox-visualization) | 🟢 Ongoing | 2 - ✅ Active | 14 days ago (2026-08-10 05:39:54 UTC) | 4 | Rust | Charts & dashboards for DuckDB — the grammar of graphics, straight from SQL.... |
| 19 | [arrow](https://duckdb.org/community_extensions/extensions/arrow.html) | [duckdb-extension-alias](https://github.com/duckdb/duckdb-extension-alias) | ❓ Unknown | 4 - 🟠 Stale | 321 days ago (2025-10-06 09:07:38 UTC) | 4 | C | DuckDB extension: arrow |
| 20 | [astro](https://duckdb.org/community_extensions/extensions/astro.html) | [astro-duck](https://github.com/synapticore-io/astro-duck) | 🟢 Ongoing | 4 - 🟠 Stale | 96 days ago (2026-05-19 12:22:23 UTC) | 2 | C++ | 60+ astronomical SQL functions for DuckDB: coordinate transforms, CCM89 dust... |
| 21 | [azure_wasm](https://github.com/HynekBlaha/duckdb-azure-wasm) | [duckdb-azure-wasm](https://github.com/HynekBlaha/duckdb-azure-wasm) | ❓ Unknown | 1 - 🔥 Very Active | 5 days ago (2026-08-18 09:37:10 UTC) | 0 | C++ | Cloud platform integration extension by HynekBlaha |
| 22 | [behavioral](https://duckdb.org/community_extensions/extensions/behavioral.html) | [duckdb-behavioral](https://github.com/tomtom215/duckdb-behavioral) | 🟢 Ongoing | 2 - ✅ Active | 27 days ago (2026-07-27 18:44:41 UTC) | 12 | Rust | A DuckDB Community Extension to enable Behavioral Analytics, inspired by Clic... |
| 23 | [bigquery](https://duckdb.org/community_extensions/extensions/bigquery.html) | [duckdb-bigquery](https://github.com/hafenkran/duckdb-bigquery) | 🟢 Ongoing | 2 - ✅ Active | 14 days ago (2026-08-09 12:09:53 UTC) | 167 | C++ | Integrates DuckDB with Google BigQuery, allowing direct querying and manageme... |
| 24 | [bitfilters](https://duckdb.org/community_extensions/extensions/bitfilters.html) | [bitfilters](https://github.com/Query-farm/bitfilters) | 🟢 Ongoing | 2 - ✅ Active | 11 days ago (2026-08-12 15:50:29 UTC) | 9 | C++ | A high-performance DuckDB extension providing probabilistic data structures f... |
| 25 | [blockduck](https://duckdb.org/community_extensions/extensions/blockduck.html) | [BlockDuck](https://github.com/luohaha/BlockDuck) | 🟢 Ongoing | 4 - 🟠 Stale | 319 days ago (2025-10-08 16:19:04 UTC) | 10 | C++ | Live SQL Queries on Blockchain |
| 26 | [boilstream](https://duckdb.org/community_extensions/extensions/boilstream.html) | [boilstream-extension](https://github.com/dforsber/boilstream-extension) | 🟢 Ongoing | 2 - ✅ Active | 14 days ago (2026-08-09 16:01:21 UTC) | 10 | C++ | Secure Remote Secrets Storage for DuckDB |
| 27 | [brew](https://duckdb.org/community_extensions/extensions/brew.html) | [duckdb-brew](https://github.com/adriens/duckdb-brew) | 🟢 Ongoing | 3 - 🟡 Stable | 84 days ago (2026-05-31 08:18:52 UTC) | 1 | C++ | duckdb extension to report installed brew packages/casks/formulas with SQL |
| 28 | [bvh2sql](https://duckdb.org/community_extensions/extensions/bvh2sql.html) | [bvh2sql](https://github.com/nkwork9999/bvh2sql) | 🟢 Ongoing | 3 - 🟡 Stable | 72 days ago (2026-06-12 12:17:09 UTC) | 0 | Makefile | SQL-related extension by nkwork9999 |
| 29 | [cache_httpfs](https://duckdb.org/community_extensions/extensions/cache_httpfs.html) | [duck-read-cache-fs](https://github.com/dentiny/duck-read-cache-fs) | 🟢 Ongoing | 2 - ✅ Active | 17 days ago (2026-08-06 22:55:34 UTC) | 146 | C++ | This repository is made as read-only filesystem for remote access. |
| 30 | [cache_prewarm](https://duckdb.org/community_extensions/extensions/cache_prewarm.html) | [duckdb-cache-prewarm](https://github.com/dentiny/duckdb-cache-prewarm) | 🟢 Ongoing | 2 - ✅ Active | 27 days ago (2026-07-28 05:02:52 UTC) | 9 | C++ | DuckDB extension: cache_prewarm by dentiny |
| 31 | [capi_quack](https://duckdb.org/community_extensions/extensions/capi_quack.html) | [extension-template-c](https://github.com/duckdb/extension-template-c) | ❓ Unknown | 2 - ✅ Active | 30 days ago (2026-07-24 09:22:27 UTC) | 31 | C | (Experimental) C/C++ template for DuckDB extensions based on the C API |
| 32 | [cassandra](https://duckdb.org/community_extensions/extensions/cassandra.html) | [duckdb-cassandra](https://github.com/dioptre/duckdb-cassandra) | ❓ Unknown | 4 - 🟠 Stale | 307 days ago (2025-10-20 19:15:10 UTC) | 2 | C++ | DuckDB Connector for Cassandra |
| 33 | [celestial](https://duckdb.org/community_extensions/extensions/celestial.html) | [duckdb-celestial](https://github.com/lisa-sgs/duckdb-celestial) | 🟢 Ongoing | 2 - ✅ Active | 17 days ago (2026-08-06 12:40:03 UTC) | 2 | C++ | DuckDB extension providing astronomical coordinates utilities |
| 34 | [chaos](https://duckdb.org/community_extensions/extensions/chaos.html) | [duckdb-chaos](https://github.com/taniabogatsch/duckdb-chaos) | 🟢 Ongoing | 4 - 🟠 Stale | 192 days ago (2026-02-12 14:50:01 UTC) | 1 | C++ | DuckDB extension: chaos by taniabogatsch |
| 35 | [chess](https://duckdb.org/community_extensions/extensions/chess.html) | [duckdb-chess](https://github.com/dotneB/duckdb-chess) | ❓ Unknown | 3 - 🟡 Stable | 88 days ago (2026-05-28 05:13:34 UTC) | 3 | Rust | A DuckDB extension for parsing and analyzing chess games in PGN format. |
| 36 | [chsql](https://duckdb.org/community_extensions/extensions/chsql.html) | [clickhouse-sql](https://github.com/Query-farm/clickhouse-sql) | ❓ Unknown | 4 - 🟠 Stale | 186 days ago (2026-02-18 19:49:47 UTC) | 94 | C++ | DuckDB Community Extension implementing ClickHouse SQL Dialect macros and Cus... |
| 37 | [chsql_native](https://duckdb.org/community_extensions/extensions/chsql_native.html) | [clickhouse-native](https://github.com/Query-farm/clickhouse-native) | ❓ Unknown | 4 - 🟠 Stale | 186 days ago (2026-02-18 19:49:46 UTC) | 21 | Rust | Experimental ClickHouse Native Client and Native file reader Extension for Du... |
| 38 | [cityjson](https://duckdb.org/community_extensions/extensions/cityjson.html) | [duckdb-cityjson](https://github.com/cityjson/duckdb-cityjson) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-08-23 18:54:50 UTC) | 10 | C++ | (Experimental) DuckDB extension for CityJSON |
| 39 | [clamp](https://duckdb.org/community_extensions/extensions/clamp.html) | [duckdb_clamp](https://github.com/oglego/duckdb_clamp) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-08-23 10:56:21 UTC) | 2 | C++ | The Clamp extension introduces range-clamping scalar functions to DuckDB. Ini... |
| 40 | [cloudfront](https://duckdb.org/community_extensions/extensions/cloudfront.html) | [duckdb-cloudfront](https://github.com/midwork-finds-jobs/duckdb-cloudfront) | 🟢 Ongoing | 4 - 🟠 Stale | 199 days ago (2026-02-05 15:32:51 UTC) | 1 | C++ | DuckDB module which provides custom authentication methods on top of httpfs m... |
| 41 | [cloudfs](https://duckdb.org/community_extensions/extensions/cloudfs.html) | [cloudfs](https://github.com/trouchet/cloudfs) | ❓ Unknown | 2 - ✅ Active | 24 days ago (2026-07-31 01:28:12 UTC) | 2 | C++ | A duckdb-based cloud filesystem query engine |
| 42 | [cloudwatch](https://duckdb.org/community_extensions/extensions/cloudwatch.html) | [duckdb-cloudwatch](https://github.com/smithclay/duckdb-cloudwatch) | 🟢 Ongoing | 2 - ✅ Active | 12 days ago (2026-08-11 17:17:46 UTC) | 1 | C++ | query cloudwatch telemetry (metrics, logs) from duckdb  |
| 43 | [cog](https://duckdb.org/community_extensions/extensions/cog.html) | [duckdb-cog](https://github.com/st-layer/duckdb-cog) | 🟢 Ongoing | 2 - ✅ Active | 11 days ago (2026-08-13 03:35:19 UTC) | 3 | Rust | GDAL-free COG raster access for DuckDB. Query Cloud-Optimized GeoTIFFs in pla... |
| 44 | [cozip](https://duckdb.org/community_extensions/extensions/cozip.html) | [cozip_reader](https://github.com/asterisk-labs/cozip_reader) | 🟢 Ongoing | 4 - 🟠 Stale | 101 days ago (2026-05-15 05:12:11 UTC) | 7 | C++ | Read Cloud-Optimized ZIP files |
| 45 | [crawler](https://duckdb.org/community_extensions/extensions/crawler.html) | [duckdb-crawler](https://github.com/midwork-finds-jobs/duckdb-crawler) | 🟢 Ongoing | 4 - 🟠 Stale | 143 days ago (2026-04-03 04:32:07 UTC) | 13 | C++ | DuckDB extension: crawler by midwork-finds-jobs |
| 46 | [cronjob](https://duckdb.org/community_extensions/extensions/cronjob.html) | [cronjob](https://github.com/Query-farm/cronjob) | 🟢 Ongoing | 2 - ✅ Active | 28 days ago (2026-07-26 22:19:07 UTC) | 54 | C++ | DuckDB CronJob Extension |
| 47 | [crypto](https://duckdb.org/community_extensions/extensions/crypto.html) | [crypto](https://github.com/Query-farm/crypto) | 🟢 Ongoing | 2 - ✅ Active | 30 days ago (2026-07-25 04:26:47 UTC) | 30 | C++ | DuckDB Extension for cryptographic hash functions and HMAC |
| 48 | [curl_httpfs](https://duckdb.org/community_extensions/extensions/curl_httpfs.html) | [duckdb-curl-filesystem](https://github.com/dentiny/duckdb-curl-filesystem) | 🟢 Ongoing | 2 - ✅ Active | 29 days ago (2026-07-25 18:56:13 UTC) | 13 | C++ | Filesystem built upon libcurl. |
| 49 | [cwiqduck](https://duckdb.org/community_extensions/extensions/cwiqduck.html) | [cwiqduck](https://github.com/cwiq-os/cwiqduck) | 🟢 Ongoing | 3 - 🟡 Stable | 67 days ago (2026-06-18 04:35:52 UTC) | 3 | C++ | DuckDB extensions for CWIQ |
| 50 | [dash](https://duckdb.org/community_extensions/extensions/dash.html) | [dash](https://github.com/gropaul/dash) | 🟢 Ongoing | 2 - ✅ Active | 10 days ago (2026-08-13 07:33:12 UTC) | 97 | C++ | Local GUI and Data Canvas as a DuckDB extension |
| 51 | [datadog](https://duckdb.org/community_extensions/extensions/datadog.html) | [duckdb-datadog](https://github.com/smithclay/duckdb-datadog) | 🟢 Ongoing | 2 - ✅ Active | 12 days ago (2026-08-11 17:17:28 UTC) | 2 | C++ | ingest logs and metrics (and soon traces) from datadog into duckdb |
| 52 | [datasketches](https://duckdb.org/community_extensions/extensions/datasketches.html) | [datasketches](https://github.com/Query-farm/datasketches) | 🟢 Ongoing | 2 - ✅ Active | 30 days ago (2026-07-25 04:26:48 UTC) | 49 | C++ | Integrates DuckDB with the high-performance Apache DataSketches library. This... |
| 53 | [dazzleduck](https://duckdb.org/community_extensions/extensions/dazzleduck.html) | [dazzleduck-sql-duckdb](https://github.com/dazzleduck-web/dazzleduck-sql-duckdb) | ❓ Unknown | 4 - 🟠 Stale | 164 days ago (2026-03-12 22:24:42 UTC) | 1 | C++ | DuckDB extension: dazzleduck by dazzleduck-web |
| 54 | [dbn](https://duckdb.org/community_extensions/extensions/dbn.html) | [duckdb-dbn](https://github.com/tbeason/duckdb-dbn) | ❓ Unknown | 3 - 🟡 Stable | 75 days ago (2026-06-09 19:42:19 UTC) | 1 | C++ | DuckDB extension for reading Databento Binary Encoding (DBN) files |
| 55 | [decimal_arithmetic](https://duckdb.org/community_extensions/extensions/decimal_arithmetic.html) | [duckdb-decimal-arithmetic](https://github.com/duckdb/duckdb-decimal-arithmetic) | 🟢 Ongoing | 3 - 🟡 Stable | 45 days ago (2026-07-09 10:55:37 UTC) | 4 | C++ | DuckDB extension: decimal_arithmetic |
| 56 | [deferred_columns](https://duckdb.org/community_extensions/extensions/deferred_columns.html) | [deferred-columns](https://github.com/iwinalbert/deferred-columns) | ❓ Unknown | 3 - 🟡 Stable | 42 days ago (2026-07-12 17:08:25 UTC) | 3 | C++ | DuckDB extension: deferred_columns by iwinalbert |
| 57 | [delta_classic](https://duckdb.org/community_extensions/extensions/delta_classic.html) | [delta_classic](https://github.com/djouallah/delta_classic) | 🟢 Ongoing | 3 - 🟡 Stable | 65 days ago (2026-06-19 15:04:33 UTC) | 5 | C++ | DuckDB extension to attach a directory of Delta tables as a database |
| 58 | [delta_export](https://duckdb.org/community_extensions/extensions/delta_export.html) | [delta_export](https://github.com/djouallah/delta_export) | 🟢 Ongoing | 3 - 🟡 Stable | 31 days ago (2026-07-24 01:30:50 UTC) | 7 | C++ | DuckDB extension to export Delta Lake metadata from DuckLake |
| 59 | [dicom](https://duckdb.org/community_extensions/extensions/dicom.html) | [duck-dicom](https://github.com/nmontesg/duck-dicom) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-08-22 09:51:55 UTC) | 0 | C++ | A DuckDB extension to import medical imaging data |
| 60 | [dns](https://duckdb.org/community_extensions/extensions/dns.html) | [duckdb-dns](https://github.com/tobilg/duckdb-dns) | 🟢 Ongoing | 2 - ✅ Active | 16 days ago (2026-08-07 11:04:08 UTC) | 16 | Rust | DNS (Reverse) Lookup Extension for DuckDB |
| 61 | [dplyr](https://duckdb.org/community_extensions/extensions/dplyr.html) | [libdplyr](https://github.com/mrchypark/libdplyr) | ❓ Unknown | 3 - 🟡 Stable | 40 days ago (2026-07-14 14:31:49 UTC) | 15 | Rust | DuckDB extension: dplyr by mrchypark |
| 62 | [dqtest](https://duckdb.org/community_extensions/extensions/dqtest.html) | [duckdb-dataquality-extension](https://github.com/vhe74/duckdb-dataquality-extension) | ❓ Unknown | 4 - 🟠 Stale | 201 days ago (2026-02-03 18:35:04 UTC) | 5 | C++ | Duckdb extension to run data quality tests |
| 63 | [dryrun](https://duckdb.org/community_extensions/extensions/dryrun.html) | [duckdb-dryrun](https://github.com/aleda145/duckdb-dryrun) | ❓ Unknown | 3 - 🟡 Stable | 63 days ago (2026-06-21 19:06:20 UTC) | 0 | C++ | dry run before execute |
| 64 | [dta](https://duckdb.org/community_extensions/extensions/dta.html) | [duckdb-dta](https://github.com/codedthinking/duckdb-dta) | 🟢 Ongoing | 3 - 🟡 Stable | 44 days ago (2026-07-10 08:57:32 UTC) | 1 | C++ | DuckDB extension for reading and writing .dta files (formats 117-121) |
| 65 | [duck_block_utils](https://duckdb.org/community_extensions/extensions/duck_block_utils.html) | [duckdb_duck_block_utils](https://github.com/teaguesterling/duckdb_duck_block_utils) | 🟢 Ongoing | 2 - ✅ Active | 13 days ago (2026-08-10 18:35:13 UTC) | 1 | C++ | A collection of utility functions to work with doc block-style structures and... |
| 66 | [duck_delta_share](https://duckdb.org/community_extensions/extensions/duck_delta_share.html) | [duck_delta_share](https://github.com/cwiq-os/duck_delta_share) | 🟢 Ongoing | 4 - 🟠 Stale | 105 days ago (2026-05-10 23:39:27 UTC) | 5 | C++ | DuckDB extension for enabling Delta Sharing client capabilities.  |
| 67 | [duck_dggs](https://duckdb.org/community_extensions/extensions/duck_dggs.html) | [duckdb-dggs](https://github.com/am2222/duckdb-dggs) | ❓ Unknown | 3 - 🟡 Stable | 58 days ago (2026-06-26 20:37:37 UTC) | 1 | C++ | A DuckDB extension for discrete global grid systems (DGGS) powered by DGGRID v8. |
| 68 | [duck_diff](https://duckdb.org/community_extensions/extensions/duck_diff.html) | [duck_diff](https://github.com/avaitla/duck_diff) | 🟢 Ongoing | 1 - 🔥 Very Active | 6 days ago (2026-08-17 22:32:33 UTC) | 6 | HTML | Diff any two database tables |
| 69 | [duck_geoarrow](https://duckdb.org/community_extensions/extensions/duck_geoarrow.html) | [duck_geoarrow](https://github.com/am2222/duck_geoarrow) | ❓ Unknown | 1 - 🔥 Very Active | 3 days ago (2026-08-21 01:12:24 UTC) | 7 | C++ | This extension, Duck_Geoarrow, provides functions to convert between WKB (Wel... |
| 70 | [duck_hunt](https://duckdb.org/community_extensions/extensions/duck_hunt.html) | [duck_hunt](https://github.com/teaguesterling/duck_hunt) | 🟢 Ongoing | 1 - 🔥 Very Active | 5 days ago (2026-08-19 03:33:25 UTC) | 5 | C++ | Tools for working with unit test suite results |
| 71 | [duck_lineage](https://duckdb.org/community_extensions/extensions/duck_lineage.html) | [duck_lineage](https://github.com/ilum-cloud/duck_lineage) | 🟢 Ongoing | 3 - 🟡 Stable | 89 days ago (2026-05-26 23:21:55 UTC) | 78 | Python | A extension for DuckDB, which captures lineage events for executed queries |
| 72 | [duck_lk](https://duckdb.org/community_extensions/extensions/duck_lk.html) | [duck-lk](https://github.com/nrminor/duck-lk) | ❓ Unknown | 4 - 🟠 Stale | 128 days ago (2026-04-18 03:05:52 UTC) | 0 | Rust | Interact with tables from your LabKey LIMS natively in DuckDB |
| 73 | [duck_tails](https://duckdb.org/community_extensions/extensions/duck_tails.html) | [duck_tails](https://github.com/teaguesterling/duck_tails) | 🟢 Ongoing | 2 - ✅ Active | 16 days ago (2026-08-07 19:05:15 UTC) | 22 | C++ | A DuckDB extension for exploring and reading git history. |
| 74 | [duckdb_delta_sharing](https://duckdb.org/community_extensions/extensions/duckdb_delta_sharing.html) | [duckdb-delta-sharing](https://github.com/prequel-co/duckdb-delta-sharing) | 🟢 Ongoing | 1 - 🔥 Very Active | 3 days ago (2026-08-20 19:40:35 UTC) | 4 | C++ | An extension for using DuckDB as a delta sharing client |
| 75 | [duckdb_geoip_rs](https://duckdb.org/community_extensions/extensions/duckdb_geoip_rs.html) | [duckdb-geoip-rs](https://github.com/william-billaud/duckdb-geoip-rs) | 🟢 Ongoing | 2 - ✅ Active | 27 days ago (2026-07-27 19:41:57 UTC) | 8 | Rust | Database connectivity extension by william-billaud |
| 76 | [duckdb_mcp](https://duckdb.org/community_extensions/extensions/duckdb_mcp.html) | [duckdb_mcp](https://github.com/teaguesterling/duckdb_mcp) | 🟢 Ongoing | 2 - ✅ Active | 18 days ago (2026-08-06 04:06:15 UTC) | 63 | C++ | A simple MCP server extension for DuckDB |
| 77 | [duckdb_midi](https://github.com/nkwork9999/duckdb-midi) | [duckdb-midi](https://github.com/nkwork9999/duckdb-midi) | ❓ Unknown | 3 - 🟡 Stable | 72 days ago (2026-06-12 12:18:36 UTC) | 0 | C++ | Database connectivity extension by nkwork9999 |
| 78 | [duckdb_opendalfs](https://duckdb.org/community_extensions/extensions/duckdb_opendalfs.html) | [duckdb-opendal-filesystem](https://github.com/dentiny/duckdb-opendal-filesystem) | 🟢 Ongoing | 2 - ✅ Active | 20 days ago (2026-08-03 08:42:36 UTC) | 5 | C++ | Database connectivity extension by dentiny |
| 79 | [duckdb_rdkit](https://duckdb.org/community_extensions/extensions/duckdb_rdkit.html) | [duckdb_rdkit](https://github.com/bodowd/duckdb_rdkit) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-08-22 17:45:05 UTC) | 14 | C++ | Database connectivity extension by bodowd |
| 80 | [duckdbi](https://duckdb.org/community_extensions/extensions/duckdbi.html) | [DuckDBI](https://github.com/nkwork9999/DuckDBI) | ❓ Unknown | 4 - 🟠 Stale | 162 days ago (2026-03-14 11:04:19 UTC) | 4 | C++ | Database connectivity extension by nkwork9999 |
| 81 | [duckgl](https://duckdb.org/community_extensions/extensions/duckgl.html) | [duckgl](https://github.com/nkwork9999/duckgl) | 🟢 Ongoing | 4 - 🟠 Stale | 172 days ago (2026-03-04 16:41:20 UTC) | 7 | C++ | DuckDB extension: duckgl by nkwork9999 |
| 82 | [duckgql](https://duckdb.org/community_extensions/extensions/duckgql.html) | [duckdb-gql](https://github.com/rahul-iyer/duckdb-gql) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-08-23 18:07:31 UTC) | 47 | C++ | An extension to run graph queries and algorithms using ISO GQL |
| 83 | [duckherder](https://duckdb.org/community_extensions/extensions/duckherder.html) | [duckdb-distributed-execution](https://github.com/dentiny/duckdb-distributed-execution) | ❓ Unknown | 4 - 🟠 Stale | 166 days ago (2026-03-10 09:36:00 UTC) | 60 | C++ | Distributed execution for duckdb queries. |
| 84 | [duckhog](https://duckdb.org/community_extensions/extensions/duckhog.html) | [duckhog](https://github.com/PostHog/duckhog) | ❓ Unknown | 3 - 🟡 Stable | 59 days ago (2026-06-26 00:52:18 UTC) | 12 | C++ | duckdb extension to connect to posthog managed data warehouse  |
| 85 | [duckhts](https://duckdb.org/community_extensions/extensions/duckhts.html) | [duckhts](https://github.com/RGenomicsETL/duckhts) | 🟢 Ongoing | 2 - ✅ Active | 8 days ago (2026-08-15 16:38:50 UTC) | 16 | C | 'htslib' based 'Duckdb' Extenstion for High Throughput Sequencing File Formats |
| 86 | [ducklake_cdc](https://duckdb.org/community_extensions/extensions/ducklake_cdc.html) | [ducklake-cdc-extension](https://github.com/elei-io/ducklake-cdc-extension) | ❓ Unknown | 2 - ✅ Active | 10 days ago (2026-08-14 04:14:25 UTC) | 16 | C++ | The missing operational layer for DuckLake’s change feed. |
| 87 | [ducklink](https://duckdb.org/community_extensions/extensions/ducklink.html) | [ducklink-extension](https://github.com/tegmentum/ducklink-extension) | ❓ Unknown | 2 - ✅ Active | 30 days ago (2026-07-24 10:41:04 UTC) | 2 | Rust | Run duckdb:extension WebAssembly components inside DuckDB (community extension) |
| 88 | [ducknng](https://github.com/RGenomicsETL/ducknng) | [ducknng](https://github.com/RGenomicsETL/ducknng) | ❓ Unknown | 1 - 🔥 Very Active | 7 days ago (2026-08-16 12:23:02 UTC) | 3 | C | ducknng: a 'DuckDB' Binding To The 'NNG' Scalability Protocols Library And an... |
| 89 | [duckorch](https://duckdb.org/community_extensions/extensions/duckorch.html) | [duck-orch](https://github.com/nkwork9999/duck-orch) | 🟢 Ongoing | 2 - ✅ Active | 16 days ago (2026-08-08 02:49:04 UTC) | 2 | Rust | DuckDB extension: duckorch by nkwork9999 |
| 90 | [duckpgq](https://duckdb.org/community_extensions/extensions/duckpgq.html) | [duckpgq-extension](https://github.com/cwida/duckpgq-extension) | ❓ Unknown | 1 - 🔥 Very Active | 6 days ago (2026-08-17 15:28:10 UTC) | 481 | C++ | DuckDB extension that adds support for SQL/PGQ and graph algorithms |
| 91 | [ducksmiles](https://duckdb.org/community_extensions/extensions/ducksmiles.html) | [duckSMILES](https://github.com/nkwork9999/duckSMILES) | ❓ Unknown | 2 - ✅ Active | 16 days ago (2026-08-07 13:51:26 UTC) | 3 | Rust | DuckDB extension: ducksmiles by nkwork9999 |
| 92 | [ducksync](https://duckdb.org/community_extensions/extensions/ducksync.html) | [ducksync](https://github.com/danjsiegel/ducksync) | 🟢 Ongoing | 2 - ✅ Active | 22 days ago (2026-08-01 23:45:35 UTC) | 7 | C++ | DuckDB extension: ducksync by danjsiegel |
| 93 | [duckthink](https://duckdb.org/community_extensions/extensions/duckthink.html) | [duckthink](https://github.com/pedro-filardi/duckthink) | ❓ Unknown | 3 - 🟡 Stable | 48 days ago (2026-07-06 15:22:58 UTC) | 0 | C++ | ASK() — natural-language SQL for DuckDB, grounded in your dbt Semantic Layer |
| 94 | [ducktinycc](https://duckdb.org/community_extensions/extensions/ducktinycc.html) | [DuckTinyCC](https://github.com/sounkou-bioinfo/DuckTinyCC) | 🟢 Ongoing | 2 - ✅ Active | 8 days ago (2026-08-15 17:55:49 UTC) | 3 | C | 'C' Scripting in 'Duckdb' using 'TinyCC' |
| 95 | [duckton](https://duckdb.org/community_extensions/extensions/duckton.html) | [duckton](https://github.com/Angelerator/duckton) | ❓ Unknown | 3 - 🟡 Stable | 59 days ago (2026-06-25 22:07:12 UTC) | 5 | Rust | Duckton — a peer-to-peer distributed DuckDB compute grid over QUIC: broadcast... |
| 96 | [eeagrid](https://duckdb.org/community_extensions/extensions/eeagrid.html) | [duckdb-eeagrid](https://github.com/ahuarte47/duckdb-eeagrid) | 🟢 Ongoing | 2 - ✅ Active | 30 days ago (2026-07-24 12:56:58 UTC) | 0 | C++ | Functions for transforming XY coordinates to and from the EEA Reference Grid... |
| 97 | [eenddb](https://duckdb.org/community_extensions/extensions/eenddb.html) | [eenddb](https://github.com/Dtenwolde/eenddb) | 🟢 Ongoing | 4 - 🟠 Stale | 145 days ago (2026-03-31 09:31:58 UTC) | 5 | C++ | Database connectivity extension by Dtenwolde |
| 98 | [elasticsearch](https://duckdb.org/community_extensions/extensions/elasticsearch.html) | [duckdb-elasticsearch](https://github.com/tlinhart/duckdb-elasticsearch) | ❓ Unknown | 4 - 🟠 Stale | 116 days ago (2026-04-29 13:01:51 UTC) | 22 | C++ | Query Elasticsearch data directly from DuckDB |
| 99 | [erpl_idoc](https://duckdb.org/community_extensions/extensions/erpl_idoc.html) | [erpl-idoc](https://github.com/DataZooDE/erpl-idoc) | 🟢 Ongoing | 2 - ✅ Active | 15 days ago (2026-08-09 00:08:08 UTC) | 2 | C++ | Read & write SAP IDoc files (flat + IDoc-XML) as SQL in DuckDB — a community... |
| 100 | [erpl_tunnel](https://duckdb.org/community_extensions/extensions/erpl_tunnel.html) | [erpl-tunnel](https://github.com/DataZooDE/erpl-tunnel) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-08-22 12:26:01 UTC) | 3 | C++ | Zero-dependency DuckDB extension: tunnel raw TCP (quack, SAP RFC, HTTP) over... |
| 101 | [erpl_web](https://duckdb.org/community_extensions/extensions/erpl_web.html) | [erpl-web](https://github.com/DataZooDE/erpl-web) | 🟢 Ongoing | 2 - ✅ Active | 13 days ago (2026-08-10 11:28:29 UTC) | 30 | C++ | ERPL is a DuckDB extension to connect to API based ecosystems via standard in... |
| 102 | [eurostat](https://duckdb.org/community_extensions/extensions/eurostat.html) | [duckdb-eurostat](https://github.com/ahuarte47/duckdb-eurostat) | 🟢 Ongoing | 2 - ✅ Active | 20 days ago (2026-08-03 17:06:16 UTC) | 34 | C++ | DuckDB extension for reading data from EUROSTAT database using SQL  |
| 103 | [evalexpr_rhai](https://duckdb.org/community_extensions/extensions/evalexpr_rhai.html) | [evalexpr_rhai](https://github.com/Query-farm/evalexpr_rhai) | 🟢 Ongoing | 2 - ✅ Active | 30 days ago (2026-07-25 04:26:51 UTC) | 26 | C++ | A DuckDB extension to evaluate the Rhai scripting language as part of SQL. |
| 104 | [events](https://duckdb.org/community_extensions/extensions/events.html) | [events](https://github.com/Query-farm/events) | ❓ Unknown | 2 - ✅ Active | 30 days ago (2026-07-25 04:26:52 UTC) | 3 | C++ | Capture database events and deliver JSON notifications to external programs v... |
| 105 | [faiss](https://duckdb.org/community_extensions/extensions/faiss.html) | [duckdb-faiss-ext](https://github.com/duckdb-faiss-ext/duckdb-faiss-ext) | 🟢 Ongoing | 2 - ✅ Active | 18 days ago (2026-08-06 00:47:40 UTC) | 31 | Go | DuckDB wrapper for FAISS - Experimental |
| 106 | [fakeit](https://duckdb.org/community_extensions/extensions/fakeit.html) | [duckdb-fakeit](https://github.com/tobilg/duckdb-fakeit) | 🟢 Ongoing | 2 - ✅ Active | 16 days ago (2026-08-07 10:54:19 UTC) | 15 | Rust | DuckDB extension: fakeit by tobilg |
| 107 | [file_dialog](https://duckdb.org/community_extensions/extensions/file_dialog.html) | [duckdb-ext-file-dialog](https://github.com/yutannihilation/duckdb-ext-file-dialog) | ❓ Unknown | 2 - ✅ Active | 27 days ago (2026-07-27 11:44:02 UTC) | 15 | Rust | A DuckDB extension to choose file interactively using native file open dialogs |
| 108 | [finance](https://duckdb.org/community_extensions/extensions/finance.html) | [duckdb-finance](https://github.com/leonardovida/duckdb-finance) | ❓ Unknown | 1 - 🔥 Very Active | today (2026-08-23 20:15:33 UTC) | 6 | C++ | SQL-native quant finance for DuckDB |
| 109 | [finetype](https://duckdb.org/community_extensions/extensions/finetype.html) | [finetype](https://github.com/meridian-online/finetype) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-08-23 10:36:48 UTC) | 4 | Rust | 👓 Precision format detection for text data. Semantic type inference with tran... |
| 110 | [fire_duck_ext](https://duckdb.org/community_extensions/extensions/fire_duck_ext.html) | [fire_duck_ext](https://github.com/BorisBesky/fire_duck_ext) | 🟢 Ongoing | 2 - ✅ Active | 15 days ago (2026-08-08 08:37:48 UTC) | 3 | C++ | duckdb extension for firestore |
| 111 | [firebird](https://duckdb.org/community_extensions/extensions/firebird.html) | [duckdb-firebird](https://github.com/flozer/duckdb-firebird) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-08-23 07:06:36 UTC) | 4 | C++ | DuckDB extension: firebird by flozer |
| 112 | [fit](https://duckdb.org/community_extensions/extensions/fit.html) | [duckdb-fit-extension](https://github.com/antoriche/duckdb-fit-extension) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-08-23 23:32:07 UTC) | 4 | C++ | DuckDB extension: fit by antoriche |
| 113 | [fivetran](https://duckdb.org/community_extensions/extensions/fivetran.html) | [duckdb_sparse_variant](https://github.com/fivetran/duckdb_sparse_variant) | 🟢 Ongoing | 4 - 🟠 Stale | 96 days ago (2026-05-19 07:42:06 UTC) | 0 | C++ | A DuckDB extension providing sparse VARIANT encoding for STRUCTs and an optim... |
| 114 | [flock](https://duckdb.org/community_extensions/extensions/flock.html) | [flock](https://github.com/dais-polymtl/flock) | 🟢 Ongoing | 2 - ✅ Active | 28 days ago (2026-07-26 19:00:52 UTC) | 355 | C++ | Beyond Quacking: Deep Integration of Language Models and RAG into DuckDB (VLD... |
| 115 | [fsquery](https://duckdb.org/community_extensions/extensions/fsquery.html) | [fsquery](https://github.com/halgari/fsquery) | ❓ Unknown | 4 - 🟠 Stale | 160 days ago (2026-03-16 16:09:24 UTC) | 2 | C++ | An extension that allows DuckDB to enumerate and stat files on the disk |
| 116 | [func_apply](https://duckdb.org/community_extensions/extensions/func_apply.html) | [duckdb_func_apply](https://github.com/teaguesterling/duckdb_func_apply) | 🟢 Ongoing | 2 - ✅ Active | 29 days ago (2026-07-25 19:36:36 UTC) | 3 | C++ | An exension to allow dynamic function application |
| 117 | [fuzzycomplete](https://duckdb.org/community_extensions/extensions/fuzzycomplete.html) | [fuzzycomplete](https://github.com/Query-farm/fuzzycomplete) | 🟢 Ongoing | 2 - ✅ Active | 29 days ago (2026-07-25 14:27:13 UTC) | 29 | C++ | DuckDB Extension for fuzzy string matching based autocompletion |
| 118 | [gaggle](https://duckdb.org/community_extensions/extensions/gaggle.html) | [gaggle](https://github.com/CogitatorTech/gaggle) | 🟢 Ongoing | 3 - 🟡 Stable | 32 days ago (2026-07-22 14:49:44 UTC) | 18 | Rust | A DuckDB extension for working with Kaggle datasets |
| 119 | [gcloud_observability](https://duckdb.org/community_extensions/extensions/gcloud_observability.html) | [duckdb-gcloud-observability](https://github.com/smithclay/duckdb-gcloud-observability) | 🟢 Ongoing | 2 - ✅ Active | 12 days ago (2026-08-11 20:28:26 UTC) | 0 | C++ | ingest logs and metrics (and soon traces) from google cloud observability int... |
| 120 | [gcs](https://duckdb.org/community_extensions/extensions/gcs.html) | [duckdb-gcs](https://github.com/northpolesec/duckdb-gcs) | 🟢 Ongoing | 2 - ✅ Active | 30 days ago (2026-07-24 18:57:51 UTC) | 29 | C++ | A GCS-native extension for DuckDB |
| 121 | [gdrive](https://duckdb.org/community_extensions/extensions/gdrive.html) | [duckdb-gdrive](https://github.com/DataZooDE/duckdb-gdrive) | 🟢 Ongoing | 2 - ✅ Active | 15 days ago (2026-08-09 05:13:30 UTC) | 2 | C++ | Query Google Drive files directly from DuckDB via a gdrive:// filesystem |
| 122 | [gdx](https://duckdb.org/community_extensions/extensions/gdx.html) | [duckdb-gdx](https://github.com/chrispahm/duckdb-gdx) | ❓ Unknown | 2 - ✅ Active | 27 days ago (2026-07-27 09:45:36 UTC) | 1 | C++ | DuckDB extension: gdx by chrispahm |
| 123 | [geography](https://duckdb.org/community_extensions/extensions/geography.html) | [duckdb-geography](https://github.com/paleolimbot/duckdb-geography) | ❓ Unknown | 2 - ✅ Active | 20 days ago (2026-08-03 14:14:08 UTC) | 46 | C++ | Geospatial data extension by paleolimbot |
| 124 | [geosilo](https://duckdb.org/community_extensions/extensions/geosilo.html) | [geosilo](https://github.com/Query-farm/geosilo) | 🟢 Ongoing | 2 - ✅ Active | 30 days ago (2026-07-25 04:26:53 UTC) | 25 | C++ | DuckDB extension for compact geometry encoding using delta-encoded coordinate... |
| 125 | [geotiff](https://duckdb.org/community_extensions/extensions/geotiff.html) | [duckdb-geotiff](https://github.com/babaknaimi/duckdb-geotiff) | ❓ Unknown | 4 - 🟠 Stale | over a year ago (2025-08-20 05:12:15 UTC) | 2 | C++ | Duckdb extension to read GeoTiffs directly with duckdb database |
| 126 | [ggsql](https://duckdb.org/community_extensions/extensions/ggsql.html) | [ggsql-duckdb](https://github.com/posit-dev/ggsql-duckdb) | 🟢 Ongoing | 3 - 🟡 Stable | 62 days ago (2026-06-23 06:14:05 UTC) | 27 | Rust | A DuckDB extension adding support for ggsql  |
| 127 | [gh](https://duckdb.org/community_extensions/extensions/gh.html) | [duckdb-gh](https://github.com/carlopi/duckdb-gh) | 🟢 Ongoing | 4 - 🟠 Stale | 116 days ago (2026-04-29 14:21:02 UTC) | 4 | C++ | DuckDB extension: gh by carlopi |
| 128 | [gorz](https://duckdb.org/community_extensions/extensions/gorz.html) | [duckdb-gorz](https://github.com/gorfather/duckdb-gorz) | 🟢 Ongoing | 3 - 🟡 Stable | 40 days ago (2026-07-14 12:35:33 UTC) | 0 | C++ | DuckDB extension: read/write GORpipe .gorz / .gord genomic files as native ta... |
| 129 | [gpudb](https://duckdb.org/community_extensions/extensions/gpudb.html) | [duckdbgpumetaldbram](https://github.com/singhpratech/duckdbgpumetaldbram) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-08-22 18:19:22 UTC) | 15 | C++ | GPU-accelerated DuckDB extension on NVIDIA CUDA + Apple Silicon Metal — first... |
| 130 | [gsheets](https://duckdb.org/community_extensions/extensions/gsheets.html) | [duckdb_gsheets](https://github.com/evidence-dev/duckdb_gsheets) | 🟢 Ongoing | 4 - 🟠 Stale | 184 days ago (2026-02-21 04:11:04 UTC) | 349 | C++ | DuckDB extension to read and write Google Sheets using SQL |
| 131 | [h3](https://duckdb.org/community_extensions/extensions/h3.html) | [h3-duckdb](https://github.com/isaacbrodsky/h3-duckdb) | 🟢 Ongoing | 3 - 🟡 Stable | 32 days ago (2026-07-22 18:16:17 UTC) | 250 | C | Bindings for H3 to DuckDB |
| 132 | [h5db](https://duckdb.org/community_extensions/extensions/h5db.html) | [h5db](https://github.com/jokasimr/h5db) | 🟢 Ongoing | 3 - 🟡 Stable | 32 days ago (2026-07-22 16:21:57 UTC) | 4 | C++ | Duckdb extension for reading HDF5 files. |
| 133 | [harbor](https://duckdb.org/community_extensions/extensions/harbor.html) | [duckdb-harbor](https://github.com/shreeve/duckdb-harbor) | 🟢 Ongoing | 1 - 🔥 Very Active | 4 days ago (2026-08-19 20:14:38 UTC) | 1 | Rust | harbor-ng — HTTP /sql for DuckDB: SQL in, NDJSON out, no driver (Rust, C exte... |
| 134 | [hashfuncs](https://duckdb.org/community_extensions/extensions/hashfuncs.html) | [hashfuncs](https://github.com/Query-farm/hashfuncs) | 🟢 Ongoing | 2 - ✅ Active | 30 days ago (2026-07-25 04:26:54 UTC) | 13 | C++ | A DuckDB extension that supplies non-cryptographic hash functions. |
| 135 | [hdf5](https://duckdb.org/community_extensions/extensions/hdf5.html) | [duckdb-hdf5](https://github.com/Berrysoft/duckdb-hdf5) | ❓ Unknown | 4 - 🟠 Stale | 123 days ago (2026-04-23 01:30:36 UTC) | 12 | Rust | HDF5 plugin for duckdb |
| 136 | [hdfs](https://duckdb.org/community_extensions/extensions/hdfs.html) | [duckdb-hdfs](https://github.com/casperhart/duckdb-hdfs) | ❓ Unknown | 3 - 🟡 Stable | 34 days ago (2026-07-21 01:26:22 UTC) | 0 | Rust | DuckDB extension: hdfs by casperhart |
| 137 | [hedged_request_fs](https://duckdb.org/community_extensions/extensions/hedged_request_fs.html) | [duckdb-hedged-request](https://github.com/dentiny/duckdb-hedged-request) | 🟢 Ongoing | 2 - ✅ Active | 29 days ago (2026-07-25 19:38:35 UTC) | 1 | C++ | DuckDB extension: hedged_request_fs by dentiny |
| 138 | [hex9](https://duckdb.org/community_extensions/extensions/hex9.html) | [duckdb-hex9](https://github.com/MrBenGriffin/duckdb-hex9) | 🟢 Ongoing | 2 - ✅ Active | 26 days ago (2026-07-28 09:59:07 UTC) | 0 | C++ | duckdb community wrapper for libhex9 |
| 139 | [highs](https://duckdb.org/community_extensions/extensions/highs.html) | [HiGHS-duckdb](https://github.com/fhk/HiGHS-duckdb) | ❓ Unknown | 4 - 🟠 Stale | 180 days ago (2026-02-25 02:07:48 UTC) | 1 | C++ | Run the solver in the database! |
| 140 | [hive_metastore](https://duckdb.org/community_extensions/extensions/hive_metastore.html) | [duckdb-hive-metastore](https://github.com/ilum-cloud/duckdb-hive-metastore) | 🟢 Ongoing | 4 - 🟠 Stale | 93 days ago (2026-05-22 17:49:59 UTC) | 4 | C++ | DuckDB extension allowing to connect to Apache Hive Metastore and query the d... |
| 141 | [hnsw_acorn](https://duckdb.org/community_extensions/extensions/hnsw_acorn.html) | [duckdb-hnsw-acorn](https://github.com/cigrainger/duckdb-hnsw-acorn) | ❓ Unknown | 4 - 🟠 Stale | 148 days ago (2026-03-28 07:49:47 UTC) | 65 | C++ | ACORN-1 pre-filtered HNSW search for DuckDB |
| 142 | [holtfs](https://duckdb.org/community_extensions/extensions/holtfs.html) | [duckdb-holtfs](https://github.com/feichai0017/duckdb-holtfs) | 🟢 Ongoing | 2 - ✅ Active | 13 days ago (2026-08-10 08:13:26 UTC) | 0 | C++ | DuckDB extension for planning scans through Holt-backed metadata indexes |
| 143 | [hostfs](https://duckdb.org/community_extensions/extensions/hostfs.html) | [hostFS](https://github.com/gropaul/hostFS) | ❓ Unknown | 4 - 🟠 Stale | 326 days ago (2025-10-01 21:02:13 UTC) | 31 | C++ | DuckDB extension: hostfs by gropaul |
| 144 | [html_query](https://duckdb.org/community_extensions/extensions/html_query.html) | [duckdb_html_query](https://github.com/midwork-finds-jobs/duckdb_html_query) | ❓ Unknown | 4 - 🟠 Stale | 199 days ago (2026-02-05 15:33:13 UTC) | 2 | Rust | Filter HTML inside duckdb |
| 145 | [html_readability](https://duckdb.org/community_extensions/extensions/html_readability.html) | [duckdb-html-readability](https://github.com/midwork-finds-jobs/duckdb-html-readability) | ❓ Unknown | 4 - 🟠 Stale | 199 days ago (2026-02-05 15:33:16 UTC) | 0 | Rust | DuckDB extension to parse html to readable text |
| 146 | [http_client](https://duckdb.org/community_extensions/extensions/http_client.html) | [httpclient](https://github.com/Query-farm/httpclient) | 🟢 Ongoing | 2 - ✅ Active | 28 days ago (2026-07-26 22:19:20 UTC) | 80 | C++ | DuckDB HTTP GET/POST Client in a Community Extension |
| 147 | [http_request](https://duckdb.org/community_extensions/extensions/http_request.html) | [duckdb_http_request](https://github.com/midwork-finds-jobs/duckdb_http_request) | ❓ Unknown | 4 - 🟠 Stale | 187 days ago (2026-02-17 13:03:03 UTC) | 4 | C++ | Uses the native duckdb httputil to make extra requests in SELECT |
| 148 | [http_stats](https://duckdb.org/community_extensions/extensions/http_stats.html) | [duckdb-http-stats](https://github.com/tlinhart/duckdb-http-stats) | ❓ Unknown | 4 - 🟠 Stale | 149 days ago (2026-03-27 13:58:03 UTC) | 1 | C++ | Better HTTP statistics for DuckDB |
| 149 | [httpd_log](https://duckdb.org/community_extensions/extensions/httpd_log.html) | [duckdb-httpd-log](https://github.com/saygox/duckdb-httpd-log) | ❓ Unknown | 4 - 🟠 Stale | 224 days ago (2026-01-12 06:14:58 UTC) | 0 | C++ | duckdb extension |
| 150 | [httpfs_timeout_retry](https://duckdb.org/community_extensions/extensions/httpfs_timeout_retry.html) | [duckdb-httpfs-timeout-retry](https://github.com/dentiny/duckdb-httpfs-timeout-retry) | 🟢 Ongoing | 2 - ✅ Active | 29 days ago (2026-07-25 21:48:10 UTC) | 0 | C++ | Web/HTTP functionality extension by dentiny |
| 151 | [httpserver](https://duckdb.org/community_extensions/extensions/httpserver.html) | [httpserver](https://github.com/Query-farm/httpserver) | 🟢 Ongoing | 2 - ✅ Active | 28 days ago (2026-07-26 22:19:21 UTC) | 284 | C++ | DuckDB HTTP API Server and Query Interface in a  Community Extension |
| 152 | [huggingface](https://duckdb.org/community_extensions/extensions/huggingface.html) | [duckdb-huggingface](https://github.com/dentiny/duckdb-huggingface) | 🟢 Ongoing | 2 - ✅ Active | 10 days ago (2026-08-13 08:21:05 UTC) | 0 | C++ | DuckDB extension: huggingface by dentiny |
| 153 | [infera](https://duckdb.org/community_extensions/extensions/infera.html) | [infera](https://github.com/CogitatorTech/infera) | 🟢 Ongoing | 3 - 🟡 Stable | 32 days ago (2026-07-22 14:50:26 UTC) | 135 | Rust | A DuckDB extension for in-database inference |
| 154 | [inflector](https://duckdb.org/community_extensions/extensions/inflector.html) | [inflector](https://github.com/Query-farm/inflector) | 🟢 Ongoing | 2 - ✅ Active | 30 days ago (2026-07-25 04:26:57 UTC) | 9 | C++ | Powerful string case transformation and inflection capabilities directly to y... |
| 155 | [interlis](https://duckdb.org/community_extensions/extensions/interlis.html) | [duckdb-interlis](https://github.com/edigonzales/duckdb-interlis) | 🟢 Ongoing | 2 - ✅ Active | 10 days ago (2026-08-13 10:33:07 UTC) | 0 | C++ | Mirror of https://codeberg.org/edigonzales/duckdb-interlis. Please do not ope... |
| 156 | [ion](https://duckdb.org/community_extensions/extensions/ion.html) | [duckdb-ion](https://github.com/kestra-io/duckdb-ion) | 🟢 Ongoing | 4 - 🟠 Stale | 166 days ago (2026-03-10 15:49:39 UTC) | 4 | C++ | AWS Ion extension for DuckDB |
| 157 | [json_schema](https://duckdb.org/community_extensions/extensions/json_schema.html) | [json_schema](https://github.com/Query-farm/json_schema) | 🟢 Ongoing | 2 - ✅ Active | 30 days ago (2026-07-25 04:26:58 UTC) | 4 | C++ | A DuckDB extension that bring support for validating JSON data using JSON sch... |
| 158 | [jsonata](https://duckdb.org/community_extensions/extensions/jsonata.html) | [jsonata](https://github.com/Query-farm/jsonata) | 🟢 Ongoing | 2 - ✅ Active | 30 days ago (2026-07-25 04:26:59 UTC) | 7 | C++ | The JSONata extension for DuckDB enables expressive, JSON-focused querying an... |
| 159 | [jsono](https://duckdb.org/community_extensions/extensions/jsono.html) | [duckdb-jsono](https://github.com/Flamefork/duckdb-jsono) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-08-22 07:35:03 UTC) | 0 | C++ | A DuckDB extension for analytics-optimized JSON storage and querying |
| 160 | [jwt](https://duckdb.org/community_extensions/extensions/jwt.html) | [duckdb_jwt](https://github.com/GalvinGao/duckdb_jwt) | ❓ Unknown | 4 - 🟠 Stale | over a year ago (2025-07-09 00:13:56 UTC) | 0 | C++ | DuckDB extension: jwt by GalvinGao |
| 161 | [keboola](https://duckdb.org/community_extensions/extensions/keboola.html) | [duckdb-extension](https://github.com/keboola/duckdb-extension) | 🟢 Ongoing | 3 - 🟡 Stable | 46 days ago (2026-07-08 11:43:04 UTC) | 0 | C++ | DuckDB extension for Keboola Storage — query and write Keboola tables using s... |
| 162 | [lastra](https://duckdb.org/community_extensions/extensions/lastra.html) | [duckdb-lastra](https://github.com/QTSurfer/duckdb-lastra) | ❓ Unknown | 2 - ✅ Active | 13 days ago (2026-08-10 11:58:17 UTC) | 0 | C++ | DuckDB extension for reading Lastra columnar time series files natively |
| 163 | [latency_injection_fs](https://duckdb.org/community_extensions/extensions/latency_injection_fs.html) | [duckdb-filesystem-latency-injection](https://github.com/dentiny/duckdb-filesystem-latency-injection) | 🟢 Ongoing | 2 - ✅ Active | 29 days ago (2026-07-25 19:33:32 UTC) | 0 | C++ | DuckDB extension: latency_injection_fs by dentiny |
| 164 | [laterite_ags4](https://duckdb.org/community_extensions/extensions/laterite_ags4.html) | [laterite-duckdb](https://github.com/niko86/laterite-duckdb) | 🟢 Ongoing | 1 - 🔥 Very Active | 4 days ago (2026-08-19 21:56:38 UTC) | 0 | Rust | DuckDB extension: laterite_ags4 by niko86 |
| 165 | [ldbc_data_gen](https://duckdb.org/community_extensions/extensions/ldbc_data_gen.html) | [ldbc-data-gen](https://github.com/Dtenwolde/ldbc-data-gen) | 🟢 Ongoing | 2 - ✅ Active | 19 days ago (2026-08-04 11:07:46 UTC) | 0 | C++ | Database connectivity extension by Dtenwolde |
| 166 | [level_pivot](https://duckdb.org/community_extensions/extensions/level_pivot.html) | [duckdb-level-pivot](https://github.com/halgari/duckdb-level-pivot) | 🟢 Ongoing | 4 - 🟠 Stale | 122 days ago (2026-04-23 16:05:04 UTC) | 0 | C++ | DuckDB extension: level_pivot by halgari |
| 167 | [lindel](https://duckdb.org/community_extensions/extensions/lindel.html) | [lindel](https://github.com/Query-farm/lindel) | 🟢 Ongoing | 2 - ✅ Active | 30 days ago (2026-07-25 04:27:01 UTC) | 66 | C++ | DuckDB Extension Linearization/Delinearization, Z-Order, Hilbert and Morton C... |
| 168 | [livetennis](https://duckdb.org/community_extensions/extensions/livetennis.html) | [duckdb-livetennis](https://github.com/livetennisapi/duckdb-livetennis) | 🟢 Ongoing | 1 - 🔥 Very Active | 7 days ago (2026-08-16 12:00:52 UTC) | 0 | C++ | DuckDB community extension for the Live Tennis API: live scores, fixtures and... |
| 169 | [llm](https://duckdb.org/community_extensions/extensions/llm.html) | [duckdb-llm](https://github.com/midwork-finds-jobs/duckdb-llm) | 🟢 Ongoing | 4 - 🟠 Stale | 187 days ago (2026-02-17 14:09:08 UTC) | 3 | C++ | DuckDB extension: llm by midwork-finds-jobs |
| 170 | [loki](https://duckdb.org/community_extensions/extensions/loki.html) | [duckdb-loki](https://github.com/prochac/duckdb-loki) | ❓ Unknown | 2 - ✅ Active | 22 days ago (2026-08-01 13:39:52 UTC) | 0 | C++ | DuckDB extension: loki by prochac |
| 171 | [lpts](https://duckdb.org/community_extensions/extensions/lpts.html) | [lpts](https://github.com/cwida/lpts) | 🟢 Ongoing | 1 - 🔥 Very Active | 7 days ago (2026-08-16 14:05:33 UTC) | 8 | C++ | Logical Plan To SQL DuckDB Extension |
| 172 | [lsh](https://duckdb.org/community_extensions/extensions/lsh.html) | [lsh](https://github.com/princeton-ddss/lsh) | ❓ Unknown | 4 - 🟠 Stale | 129 days ago (2026-04-16 17:00:45 UTC) | 14 | Rust | DuckDB community extension for locality-sensitive hashing (LSH) |
| 173 | [lttb](https://duckdb.org/community_extensions/extensions/lttb.html) | [duckdb-lttb](https://github.com/reformovo/duckdb-lttb) | ❓ Unknown | 3 - 🟡 Stable | 53 days ago (2026-07-01 07:47:53 UTC) | 2 | C++ | A simple lttb algorithm extension for DuckDB |
| 174 | [lua](https://duckdb.org/community_extensions/extensions/lua.html) | [duckdb-lua](https://github.com/isaacbrodsky/duckdb-lua) | 🟢 Ongoing | 3 - 🟡 Stable | 32 days ago (2026-07-22 23:18:11 UTC) | 12 | C++ | DuckDB extension to evaluate Lua expressions. |
| 175 | [luajit](https://duckdb.org/community_extensions/extensions/luajit.html) | [duckdb-luajit](https://github.com/alitrack/duckdb-luajit) | 🟢 Ongoing | 2 - ✅ Active | 15 days ago (2026-08-08 11:53:27 UTC) | 4 | C | DuckDB extension for in-process JIT-compiled Lua UDFs via LuaJIT — self-conta... |
| 176 | [magic](https://duckdb.org/community_extensions/extensions/magic.html) | [duckdb-magic](https://github.com/carlopi/duckdb-magic) | ❓ Unknown | 3 - 🟡 Stable | 62 days ago (2026-06-22 07:17:42 UTC) | 8 | C++ | Auto-detect file types via `libmagic` (`file` utility) |
| 177 | [marisa](https://duckdb.org/community_extensions/extensions/marisa.html) | [marisa](https://github.com/Query-farm/marisa) | 🟢 Ongoing | 2 - ✅ Active | 30 days ago (2026-07-25 04:27:03 UTC) | 14 | C++ | The Marisa extension by Query.Farm integrates the fast, space-efficient MARIS... |
| 178 | [markdown](https://duckdb.org/community_extensions/extensions/markdown.html) | [duckdb_markdown](https://github.com/teaguesterling/duckdb_markdown) | 🟢 Ongoing | 1 - 🔥 Very Active | 4 days ago (2026-08-19 22:08:17 UTC) | 28 | C++ | Heirarchical markdown parsing for DuckDB |
| 179 | [maxmind](https://duckdb.org/community_extensions/extensions/maxmind.html) | [duckdb-maxmind](https://github.com/marselester/duckdb-maxmind) | 🟢 Ongoing | 3 - 🟡 Stable | 55 days ago (2026-06-29 21:07:08 UTC) | 7 | Zig | DuckDB MaxMind extension written in Zig. |
| 180 | [miint](https://duckdb.org/community_extensions/extensions/miint.html) | [duckdb-miint](https://github.com/the-miint/duckdb-miint) | 🟢 Ongoing | 1 - 🔥 Very Active | 3 days ago (2026-08-20 17:21:36 UTC) | 6 | C++ | DuckDB extension: miint by the-miint |
| 181 | [minijinja](https://duckdb.org/community_extensions/extensions/minijinja.html) | [minijinja](https://github.com/Query-farm/minijinja) | 🟢 Ongoing | 2 - ✅ Active | 30 days ago (2026-07-25 04:27:04 UTC) | 6 | C++ | DuckDB extension: minijinja |
| 182 | [miniplot](https://duckdb.org/community_extensions/extensions/miniplot.html) | [miniplot](https://github.com/nkwork9999/miniplot) | 🟢 Ongoing | 4 - 🟠 Stale | 282 days ago (2025-11-15 02:42:43 UTC) | 24 | C++ | DuckDB extension: miniplot by nkwork9999 |
| 183 | [ml](https://duckdb.org/community_extensions/extensions/ml.html) | [duckdb-ml](https://github.com/alitrack/duckdb-ml) | 🟢 Ongoing | 1 - 🔥 Very Active | 6 days ago (2026-08-18 06:28:03 UTC) | 6 | Rust | DuckDB extension: ml by alitrack |
| 184 | [mlpack](https://duckdb.org/community_extensions/extensions/mlpack.html) | [duckdb-mlpack](https://github.com/eddelbuettel/duckdb-mlpack) | 🟢 Ongoing | 2 - ✅ Active | 24 days ago (2026-07-30 15:15:13 UTC) | 20 | C++ | Bringing mlpack to duckdb |
| 185 | [monetary](https://duckdb.org/community_extensions/extensions/monetary.html) | [monetary](https://github.com/fyffee/monetary) | ❓ Unknown | 4 - 🟠 Stale | 206 days ago (2026-01-29 11:29:01 UTC) | 0 | C++ | DuckDB extension: monetary by fyffee |
| 186 | [mongo](https://duckdb.org/community_extensions/extensions/mongo.html) | [duckdb-mongo](https://github.com/stephaniewang526/duckdb-mongo) | ❓ Unknown | 2 - ✅ Active | 17 days ago (2026-08-06 18:22:48 UTC) | 57 | C++ | Integrates DuckDB with MongoDB, enabling direct SQL queries over MongoDB coll... |
| 187 | [mooncake](https://duckdb.org/community_extensions/extensions/mooncake.html) | [duckdb_mooncake](https://github.com/Mooncake-Labs/duckdb_mooncake) | ❓ Unknown | 4 - 🟠 Stale | 301 days ago (2025-10-26 07:13:05 UTC) | 10 | C++ | Read Iceberg tables written by moonlink in real time |
| 188 | [motorsport_telemetry](https://duckdb.org/community_extensions/extensions/motorsport_telemetry.html) | [duckdb_motorsport_telemetry](https://github.com/tobi/duckdb_motorsport_telemetry) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-08-24 03:46:12 UTC) | 7 | Rust | Fast DuckDB extension and Rust parsers for Cosworth PDS, MoTeC LD, and VBOX V... |
| 189 | [mpduck](https://duckdb.org/community_extensions/extensions/mpduck.html) | [mpduck](https://github.com/MatthewMooreZA/mpduck) | ❓ Unknown | 4 - 🟠 Stale | 132 days ago (2026-04-13 17:59:29 UTC) | 1 | C++ | DuckDB extension to read and write Prophet model point files. |
| 190 | [msolap](https://duckdb.org/community_extensions/extensions/msolap.html) | [duckdb-msolap-extension](https://github.com/Hugoberry/duckdb-msolap-extension) | ❓ Unknown | 4 - 🟠 Stale | 333 days ago (2025-09-24 16:33:46 UTC) | 14 | C++ | DuckDB extension: msolap by Hugoberry |
| 191 | [mssql](https://duckdb.org/community_extensions/extensions/mssql.html) | [mssql-extension](https://github.com/hugr-lab/mssql-extension) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-08-23 19:09:45 UTC) | 126 | C++ | DuckDB extension for Microsoft SQL Server (TDS + TLS), with catalog integrati... |
| 192 | [nanoarrow](https://duckdb.org/community_extensions/extensions/nanoarrow.html) | [duckdb-nanoarrow](https://github.com/paleolimbot/duckdb-nanoarrow) | ❓ Unknown | 1 - 🔥 Very Active | 6 days ago (2026-08-18 03:20:54 UTC) | 76 | C++ | DuckDB extension: nanoarrow by paleolimbot |
| 193 | [nanodbc](https://duckdb.org/community_extensions/extensions/nanodbc.html) | [duckdb-nanodbc-extension](https://github.com/Hugoberry/duckdb-nanodbc-extension) | ❓ Unknown | 4 - 🟠 Stale | 114 days ago (2026-05-01 13:18:55 UTC) | 52 | C++ | Database connectivity extension by Hugoberry |
| 194 | [nats_js](https://duckdb.org/community_extensions/extensions/nats_js.html) | [duckdb-nats-jetstream](https://github.com/brannn/duckdb-nats-jetstream) | ❓ Unknown | 4 - 🟠 Stale | 147 days ago (2026-03-30 05:12:16 UTC) | 22 | C++ | DuckDB extension for querying NATS JetStream message streams with SQL |
| 195 | [netquack](https://duckdb.org/community_extensions/extensions/netquack.html) | [duckdb-netquack](https://github.com/hatamiarash7/duckdb-netquack) | ❓ Unknown | 2 - ✅ Active | 29 days ago (2026-07-25 07:00:30 UTC) | 42 | C++ | DuckDB extension for parsing, extracting, and analyzing domains, URIs, and pa... |
| 196 | [nsv](https://duckdb.org/community_extensions/extensions/nsv.html) | [nsv-duckdb](https://github.com/nsv-format/nsv-duckdb) | 🟢 Ongoing | 3 - 🟡 Stable | 77 days ago (2026-06-07 19:12:56 UTC) | 0 | Rust | A DuckDB extension for NSV processing |
| 197 | [oast](https://duckdb.org/community_extensions/extensions/oast.html) | [duckdb-oast](https://github.com/hrbrmstr/duckdb-oast) | 🟢 Ongoing | 4 - 🟠 Stale | 194 days ago (2026-02-10 12:00:32 UTC) | 4 | C | A DuckDB extension for validating, decoding, and extracting OAST (Out-of-Band... |
| 198 | [observefs](https://duckdb.org/community_extensions/extensions/observefs.html) | [duckdb-filesystem-observability](https://github.com/dentiny/duckdb-filesystem-observability) | 🟢 Ongoing | 2 - ✅ Active | 29 days ago (2026-07-25 19:13:57 UTC) | 16 | C++ | Provides observability for duckdb filesystem. |
| 199 | [ofquack](https://duckdb.org/community_extensions/extensions/ofquack.html) | [ofquack](https://github.com/krokozyab/ofquack) | ❓ Unknown | 1 - 🔥 Very Active | today (2026-08-23 13:00:58 UTC) | 6 | C++ | Oracle Fusion DuckDB extension  |
| 200 | [onager](https://duckdb.org/community_extensions/extensions/onager.html) | [onager](https://github.com/CogitatorTech/onager) | 🟢 Ongoing | 2 - ✅ Active | 24 days ago (2026-07-30 17:34:19 UTC) | 148 | Rust | A DuckDB extension for graph data analytics |
| 201 | [onelake](https://duckdb.org/community_extensions/extensions/onelake.html) | [duckdb_onelake](https://github.com/datumnova/duckdb_onelake) | ❓ Unknown | 4 - 🟠 Stale | 265 days ago (2025-12-01 10:28:22 UTC) | 19 | C++ | DuckDB extension: onelake by datumnova |
| 202 | [open_prompt](https://duckdb.org/community_extensions/extensions/open_prompt.html) | [openprompt](https://github.com/Query-farm/openprompt) | 🟢 Ongoing | 2 - ✅ Active | 28 days ago (2026-07-26 22:19:22 UTC) | 61 | C++ | DuckDB Community Extension to prompt LLMs from SQL |
| 203 | [opendal](https://duckdb.org/community_extensions/extensions/opendal.html) | [duckdb-opendal](https://github.com/chitralverma/duckdb-opendal) | 🟢 Ongoing | 1 - 🔥 Very Active | 4 days ago (2026-08-20 06:07:50 UTC) | 0 | Rust | extension to bring together duckdb and opendal |
| 204 | [orc](https://duckdb.org/community_extensions/extensions/orc.html) | [duckdb_orc](https://github.com/alitrack/duckdb_orc) | 🟢 Ongoing | 3 - 🟡 Stable | 40 days ago (2026-07-15 01:20:53 UTC) | 4 | Rust | A DuckDB extension for reading Apache ORC files, written in pure Rust. |
| 205 | [osmium](https://duckdb.org/community_extensions/extensions/osmium.html) | [duckdb-osmium](https://github.com/jake-low/duckdb-osmium) | 🟢 Ongoing | 2 - ✅ Active | 9 days ago (2026-08-15 04:34:39 UTC) | 27 | C++ | DuckDB extension for reading OpenStreetMap PBF files using libosmium |
| 206 | [otlp](https://duckdb.org/community_extensions/extensions/otlp.html) | [duckdb-otlp](https://github.com/smithclay/duckdb-otlp) | 🟢 Ongoing | 2 - ✅ Active | 20 days ago (2026-08-03 13:38:24 UTC) | 79 | Python | stream, store, and query OpenTelemetry metrics, logs, and traces (OTLP) in du... |
| 207 | [overture](https://duckdb.org/community_extensions/extensions/overture.html) | [duckdb-overture](https://github.com/cubilica/duckdb-overture) | ❓ Unknown | 4 - 🟠 Stale | 131 days ago (2026-04-14 16:46:56 UTC) | 4 | C++ | DuckDB extension: overture by cubilica |
| 208 | [pac](https://duckdb.org/community_extensions/extensions/pac.html) | [privacy](https://github.com/cwida/privacy) | 🟢 Ongoing | 3 - 🟡 Stable | 32 days ago (2026-07-22 12:26:16 UTC) | 19 | C++ | Automatic query privatization in DuckDB |
| 209 | [paimon](https://duckdb.org/community_extensions/extensions/paimon.html) | [duckdb-paimon](https://github.com/polardb/duckdb-paimon) | 🟢 Ongoing | 2 - ✅ Active | 13 days ago (2026-08-11 04:30:34 UTC) | 44 | C++ | DuckDB extension for accessing Apache Paimon. 🦆 |
| 210 | [parser_tools](https://duckdb.org/community_extensions/extensions/parser_tools.html) | [duckdb_extension_parser_tools](https://github.com/hotdata-dev/duckdb_extension_parser_tools) | 🟢 Ongoing | 3 - 🟡 Stable | 34 days ago (2026-07-20 22:07:52 UTC) | 27 | C++ | Parse sql - with sql! |
| 211 | [pbi_scanner](https://duckdb.org/community_extensions/extensions/pbi_scanner.html) | [pbi_scanner](https://github.com/crazy-treyn/pbi_scanner) | 🟢 Ongoing | 3 - 🟡 Stable | 67 days ago (2026-06-17 19:07:44 UTC) | 15 | C++ | DuckDB extension that enables querying Power BI Semantic Models with DAX. |
| 212 | [pbix](https://duckdb.org/community_extensions/extensions/pbix.html) | [duckdb-pbix-extension](https://github.com/Hugoberry/duckdb-pbix-extension) | 🟢 Ongoing | 4 - 🟠 Stale | 303 days ago (2025-10-24 13:47:34 UTC) | 38 | C++ | Duckdb extension for parsing the metadata and contents of the embedded data m... |
| 213 | [pcap_duckdb](https://duckdb.org/community_extensions/extensions/pcap_duckdb.html) | [pcap_duckdb](https://github.com/siara-in/pcap_duckdb) | ❓ Unknown | 3 - 🟡 Stable | 81 days ago (2026-06-04 05:10:33 UTC) | 1 | C++ | Database connectivity extension by siara-in |
| 214 | [pcap_reader](https://duckdb.org/community_extensions/extensions/pcap_reader.html) | [pcap](https://github.com/Query-farm/pcap) | ❓ Unknown | 4 - 🟠 Stale | 97 days ago (2026-05-18 22:26:34 UTC) | 13 | Rust | DuckDB PCAP Reader Extension made in Rust |
| 215 | [pdal](https://duckdb.org/community_extensions/extensions/pdal.html) | [duckdb-pdal](https://github.com/ahuarte47/duckdb-pdal) | 🟢 Ongoing | 1 - 🔥 Very Active | 7 days ago (2026-08-17 06:08:23 UTC) | 27 | C++ | DuckDB extension for manipulating point cloud data using SQL |
| 216 | [pdf](https://duckdb.org/community_extensions/extensions/pdf.html) | [duckdb-pdf](https://github.com/asubbarao/duckdb-pdf) | 🟢 Ongoing | 2 - ✅ Active | 25 days ago (2026-07-29 23:43:07 UTC) | 5 | C++ | Read and extract content from PDF files in DuckDB — Poppler (text/words/lines... |
| 217 | [petgraph_ext](https://duckdb.org/community_extensions/extensions/petgraph_ext.html) | [duckdb_petgraph](https://github.com/alitrack/duckdb_petgraph) | 🟢 Ongoing | 2 - ✅ Active | 25 days ago (2026-07-29 23:37:31 UTC) | 4 | Rust | DuckDB extension: petgraph_ext by alitrack |
| 218 | [pfc](https://duckdb.org/community_extensions/extensions/pfc.html) | [pfc-duckdb](https://github.com/ImpossibleForge/pfc-duckdb) | 🟢 Ongoing | 4 - 🟠 Stale | 96 days ago (2026-05-19 17:32:55 UTC) | 1 | C++ | DuckDB extension to read PFC-JSONL compressed log files with block-level time... |
| 219 | [pic2vec](https://duckdb.org/community_extensions/extensions/pic2vec.html) | [pic2vec](https://github.com/nkwork9999/pic2vec) | 🟢 Ongoing | 3 - 🟡 Stable | 72 days ago (2026-06-12 16:13:03 UTC) | 0 | C++ | DuckDB extension: pic2vec by nkwork9999 |
| 220 | [pivot_table](https://duckdb.org/community_extensions/extensions/pivot_table.html) | [pivot_table](https://github.com/Alex-Monahan/pivot_table) | ❓ Unknown | 4 - 🟠 Stale | 128 days ago (2026-04-17 15:20:58 UTC) | 20 | C++ | Full spreadsheet-style pivot table through SQL macros. Just specify values, r... |
| 221 | [plinking_duck](https://duckdb.org/community_extensions/extensions/plinking_duck.html) | [plinking_duck](https://github.com/teaguesterling/plinking_duck) | 🟢 Ongoing | 2 - ✅ Active | 24 days ago (2026-07-30 23:32:01 UTC) | 4 | C++ | DuckDB tools for Plink2  |
| 222 | [poached](https://duckdb.org/community_extensions/extensions/poached.html) | [poached](https://github.com/sidequery/poached) | ❓ Unknown | 4 - 🟠 Stale | 240 days ago (2025-12-26 21:13:19 UTC) | 11 | C++ | A DuckDB extension that exposes SQL parsing functionality for building IDEs,... |
| 223 | [polyglot](https://duckdb.org/community_extensions/extensions/polyglot.html) | [duckdb-polyglot](https://github.com/tobilg/duckdb-polyglot) | 🟢 Ongoing | 2 - ✅ Active | 16 days ago (2026-08-07 15:12:07 UTC) | 25 | Rust | Use other SQL dialects in DuckDB  |
| 224 | [prometheus](https://duckdb.org/community_extensions/extensions/prometheus.html) | [duckdb-prometheus](https://github.com/botan/duckdb-prometheus) | 🟢 Ongoing | 3 - 🟡 Stable | 32 days ago (2026-07-22 15:04:54 UTC) | 4 | Rust | Query Prometheus-compatible HTTP APIs directly from DuckDB |
| 225 | [protoduck](https://duckdb.org/community_extensions/extensions/protoduck.html) | [protoduck](https://github.com/fcsnk/protoduck) | ❓ Unknown | 3 - 🟡 Stable | 38 days ago (2026-07-17 06:47:06 UTC) | 1 | Rust | DuckDB extension: protoduck by fcsnk |
| 226 | [prql](https://duckdb.org/community_extensions/extensions/prql.html) | [duckdb-prql](https://github.com/ywelsch/duckdb-prql) | 🟢 Ongoing | 3 - 🟡 Stable | 87 days ago (2026-05-28 11:18:16 UTC) | 329 | C++ | PRQL as a DuckDB extension |
| 227 | [psql](https://duckdb.org/community_extensions/extensions/psql.html) | [duckdb-psql](https://github.com/ywelsch/duckdb-psql) | 🟢 Ongoing | 4 - 🟠 Stale | 131 days ago (2026-04-14 18:55:40 UTC) | 106 | C++ | A piped SQL for DuckDB |
| 228 | [pst](https://duckdb.org/community_extensions/extensions/pst.html) | [duckdb-pst](https://github.com/intellekthq/duckdb-pst) | 🟢 Ongoing | 2 - ✅ Active | 20 days ago (2026-08-03 16:43:10 UTC) | 10 | C++ | In-place querying of Microsoft PST files, directly from storage, with SQL. |
| 229 | [psyduck](https://duckdb.org/community_extensions/extensions/psyduck.html) | [psyduck](https://github.com/Ian-Fogelman/psyduck) | 🟢 Ongoing | 4 - 🟠 Stale | 252 days ago (2025-12-14 15:10:39 UTC) | 7 | C++ | Pysduck a DuckDB community extension about Pokémon. |
| 230 | [pyroscope](https://duckdb.org/community_extensions/extensions/pyroscope.html) | [pyroscope](https://github.com/Query-farm/pyroscope) | ❓ Unknown | 4 - 🟠 Stale | 186 days ago (2026-02-18 19:49:53 UTC) | 21 | Rust | DuckDB Pyroscope Extension for Continuous Profiling |
| 231 | [python_udf](https://duckdb.org/community_extensions/extensions/python_udf.html) | [duckdb-python](https://github.com/alitrack/duckdb-python) | 🟢 Ongoing | 2 - ✅ Active | 23 days ago (2026-07-31 08:04:02 UTC) | 6 | Rust | DuckDB extension: embed Python inside DuckDB for SQL-native Python UDFs (scal... |
| 232 | [quack_oauth](https://duckdb.org/community_extensions/extensions/quack_oauth.html) | [quack-oauth](https://github.com/DataZooDE/quack-oauth) | 🟢 Ongoing | 2 - ✅ Active | 14 days ago (2026-08-10 05:39:50 UTC) | 24 | C++ | Extensions providing OAuth and OpenID primitives for authentication and autho... |
| 233 | [quackapi](https://duckdb.org/community_extensions/extensions/quackapi.html) | [quackapi](https://github.com/asubbarao/quackapi) | 🟢 Ongoing | 2 - ✅ Active | 25 days ago (2026-07-30 06:45:33 UTC) | 2 | C++ | FastAPI-class web framework inside DuckDB — CREATE ROUTE turns SQL into typed... |
| 234 | [quackfix](https://duckdb.org/community_extensions/extensions/quackfix.html) | [QuackFIX](https://github.com/hyehudai/QuackFIX) | ❓ Unknown | 4 - 🟠 Stale | 241 days ago (2025-12-25 10:36:24 UTC) | 16 | C++ | Fix log extension for duckdb |
| 235 | [quackformers](https://duckdb.org/community_extensions/extensions/quackformers.html) | [quackformers](https://github.com/martin-conur/quackformers) | ❓ Unknown | 2 - ✅ Active | 16 days ago (2026-08-08 01:34:18 UTC) | 13 | Rust | DuckDB NLP extension. |
| 236 | [quackiso](https://duckdb.org/community_extensions/extensions/quackiso.html) | [quackiso](https://github.com/tempoloss/quackiso) | 🟢 Ongoing | 1 - 🔥 Very Active | 2 days ago (2026-08-22 01:07:39 UTC) | 4 | Rust | Query ISO 20022 (camt/pacs/pain) financial messages as SQL in DuckDB |
| 237 | [quackscale](https://duckdb.org/community_extensions/extensions/quackscale.html) | [quackscale](https://github.com/Query-farm/quackscale) | 🟢 Ongoing | 2 - ✅ Active | 23 days ago (2026-07-31 17:20:33 UTC) | 24 | Shell | DuckDB WireGuard Extension with Quack & Ducklake over Tailscale, Headscale & Co |
| 238 | [quackstats](https://duckdb.org/community_extensions/extensions/quackstats.html) | [quackstats](https://github.com/jasadams/quackstats) | ❓ Unknown | 4 - 🟠 Stale | 203 days ago (2026-02-01 12:01:35 UTC) | 3 | Rust | DuckDB extension for time series forecasting and seasonality detection |
| 239 | [quackstore](https://duckdb.org/community_extensions/extensions/quackstore.html) | [QuackStore](https://github.com/coginiti-dev/QuackStore) | 🟢 Ongoing | 4 - 🟠 Stale | 110 days ago (2026-05-05 13:29:19 UTC) | 117 | C++ | DuckDB extension: quackstore by coginiti-dev |
| 240 | [query_condition_cache](https://duckdb.org/community_extensions/extensions/query_condition_cache.html) | [duckdb-query-condition-cache](https://github.com/dentiny/duckdb-query-condition-cache) | 🟢 Ongoing | 2 - ✅ Active | 29 days ago (2026-07-25 22:03:25 UTC) | 17 | C++ | DuckDB extension: query_condition_cache by dentiny |
| 241 | [query_limiter](https://duckdb.org/community_extensions/extensions/query_limiter.html) | [duckdb-query-limiter](https://github.com/dentiny/duckdb-query-limiter) | 🟢 Ongoing | 2 - ✅ Active | 29 days ago (2026-07-25 19:10:55 UTC) | 0 | C++ | DuckDB extension: query_limiter by dentiny |
| 242 | [quickjs](https://duckdb.org/community_extensions/extensions/quickjs.html) | [quickjs](https://github.com/Query-farm/quickjs) | 🟢 Ongoing | 2 - ✅ Active | 30 days ago (2026-07-25 04:27:07 UTC) | 14 | C++ | DuckDB extension: quickjs by quackscience |
| 243 | [qvd](https://duckdb.org/community_extensions/extensions/qvd.html) | [DuckDB-QVD-Extension](https://github.com/snouhaud/DuckDB-QVD-Extension) | 🟢 Ongoing | 3 - 🟡 Stable | 31 days ago (2026-07-23 19:51:08 UTC) | 0 | Rust | An DuckDB extension to add QVD files read and write |
| 244 | [radio](https://duckdb.org/community_extensions/extensions/radio.html) | [radio](https://github.com/Query-farm/radio) | 🟢 Ongoing | 2 - ✅ Active | 29 days ago (2026-07-25 14:27:12 UTC) | 43 | C++ | Radio is a DuckDB extension by Query.Farm that brings real-time event streams... |
| 245 | [rapidfuzz](https://duckdb.org/community_extensions/extensions/rapidfuzz.html) | [rapidfuzz](https://github.com/Query-farm/rapidfuzz) | 🟢 Ongoing | 2 - ✅ Active | 28 days ago (2026-07-26 22:19:23 UTC) | 18 | C++ | DuckDB Community Extension adding RapidFuzz algorithms for search, deduplicat... |
| 246 | [raquet](https://duckdb.org/community_extensions/extensions/raquet.html) | [duckdb-raquet](https://github.com/CartoDB/duckdb-raquet) | 🟢 Ongoing | 3 - 🟡 Stable | 39 days ago (2026-07-15 14:35:34 UTC) | 14 | C++ | DuckDB extension for reading Raquet format (raster data in Parquet with QUADB... |
| 247 | [raster](https://duckdb.org/community_extensions/extensions/raster.html) | [duckdb-raster](https://github.com/ahuarte47/duckdb-raster) | 🟢 Ongoing | 1 - 🔥 Very Active | 2 days ago (2026-08-21 15:17:01 UTC) | 53 | C | DuckDB Extension for reading and writing raster files using SQL. |
| 248 | [rate_limit_fs](https://duckdb.org/community_extensions/extensions/rate_limit_fs.html) | [duckdb-rate-limit-filesystem](https://github.com/dentiny/duckdb-rate-limit-filesystem) | 🟢 Ongoing | 2 - ✅ Active | 29 days ago (2026-07-25 21:35:54 UTC) | 1 | C++ | DuckDB extension: rate_limit_fs by dentiny |
| 249 | [rawduck](https://duckdb.org/community_extensions/extensions/rawduck.html) | [rawduck](https://github.com/quackscience/rawduck) | ❓ Unknown | 1 - 🔥 Very Active | today (2026-08-22 17:50:45 UTC) | 30 | C++ | Experimental RawMergeTree-like Extension for DuckDB |
| 250 | [rdf](https://duckdb.org/community_extensions/extensions/rdf.html) | [duck_rdf](https://github.com/nonodename/duck_rdf) | 🟢 Ongoing | 1 - 🔥 Very Active | 3 days ago (2026-08-20 17:30:07 UTC) | 29 | C++ | RDF file extension for DuckDB. Reads, writes & sparql supported |
| 251 | [read_dbf](https://duckdb.org/community_extensions/extensions/read_dbf.html) | [duckdb-dbf](https://github.com/tocharan/duckdb-dbf) | 🟢 Ongoing | 4 - 🟠 Stale | 179 days ago (2026-02-25 17:13:20 UTC) | 3 | C++ | Database connectivity extension by tocharan |
| 252 | [read_lines](https://duckdb.org/community_extensions/extensions/read_lines.html) | [duckdb_read_lines](https://github.com/teaguesterling/duckdb_read_lines) | 🟢 Ongoing | 1 - 🔥 Very Active | 4 days ago (2026-08-19 22:08:46 UTC) | 4 | C++ | Simple parsers for fast extraction from line-based files  |
| 253 | [read_stat](https://duckdb.org/community_extensions/extensions/read_stat.html) | [duckdb-read-stat](https://github.com/dylanmeysmans/duckdb-read-stat) | ❓ Unknown | 3 - 🟡 Stable | 65 days ago (2026-06-19 23:25:46 UTC) | 35 | C | Read data sets from SAS, Stata, and SPSS from DuckDB with ReadStat |
| 254 | [redis](https://duckdb.org/community_extensions/extensions/redis.html) | [redis](https://github.com/Query-farm/redis) | 🟢 Ongoing | 2 - ✅ Active | 28 days ago (2026-07-26 22:19:24 UTC) | 13 | C++ | DuckDB Redis Client community extension |
| 255 | [robust](https://duckdb.org/community_extensions/extensions/robust.html) | [robust](https://github.com/robust-sql/robust) | ❓ Unknown | 2 - ✅ Active | 16 days ago (2026-08-08 01:57:04 UTC) | 5 | C++ | A DuckDB extension implementing Predicate Transfer to reduce cardinality expl... |
| 256 | [rocket](https://duckdb.org/community_extensions/extensions/rocket.html) | [duckdb-rocket](https://github.com/maxdemarzi/duckdb-rocket) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-08-22 21:56:21 UTC) | 1 | Python | Training-free time-series classification in DuckDB: RocketPFN via a ROCKET fe... |
| 257 | [rrd](https://duckdb.org/community_extensions/extensions/rrd.html) | [duckdb-rrd](https://github.com/VertexStudio/duckdb-rrd) | ❓ Unknown | 3 - 🟡 Stable | 51 days ago (2026-07-03 18:31:26 UTC) | 0 | Rust | DuckDB extension: rrd by VertexStudio |
| 258 | [rusty_quack](https://duckdb.org/community_extensions/extensions/rusty_quack.html) | [extension-template-rs](https://github.com/duckdb/extension-template-rs) | ❓ Unknown | 3 - 🟡 Stable | 32 days ago (2026-07-23 06:05:55 UTC) | 112 | Rust | (Experimental) Template for Rust-based DuckDB extensions |
| 259 | [rusty_sheet](https://duckdb.org/community_extensions/extensions/rusty_sheet.html) | [rusty-sheet](https://github.com/redraiment/rusty-sheet) | 🟢 Ongoing | 4 - 🟠 Stale | 192 days ago (2026-02-13 02:27:56 UTC) | 77 | Rust | An Excel/WPS/OpenDocument Spreadsheets file reader for DuckDB |
| 260 | [salesforce](https://duckdb.org/community_extensions/extensions/salesforce.html) | [duckdb-salesforce](https://github.com/flozer/duckdb-salesforce) | ❓ Unknown | 1 - 🔥 Very Active | today (2026-08-23 05:46:59 UTC) | 2 | C++ | DuckDB extension: salesforce by flozer |
| 261 | [sazgar](https://duckdb.org/community_extensions/extensions/sazgar.html) | [Sazgar](https://github.com/Angelerator/Sazgar) | ❓ Unknown | 4 - 🟠 Stale | 94 days ago (2026-05-22 04:56:10 UTC) | 13 | HTML | DuckDB extension for system monitoring & intelligent SQL routing. 25+ functio... |
| 262 | [scalarfs](https://duckdb.org/community_extensions/extensions/scalarfs.html) | [duckdb_scalarfs](https://github.com/teaguesterling/duckdb_scalarfs) | 🟢 Ongoing | 2 - ✅ Active | 17 days ago (2026-08-07 01:44:38 UTC) | 9 | C++ | A collection of simple virtual filesystems for treating scalar values as files. |
| 263 | [scrooge](https://duckdb.org/community_extensions/extensions/scrooge.html) | [Scrooge-McDuck](https://github.com/pdet/Scrooge-McDuck) | ❓ Unknown | 4 - 🟠 Stale | 111 days ago (2026-05-04 14:27:57 UTC) | 162 | C++ | DuckDB extension: scrooge by pdet |
| 264 | [se3](https://duckdb.org/community_extensions/extensions/se3.html) | [se3](https://github.com/jokasimr/se3) | 🟢 Ongoing | 3 - 🟡 Stable | 35 days ago (2026-07-19 09:45:05 UTC) | 0 | C++ | Duckdb extension for efficient rotation / translation operations on points in... |
| 265 | [semantic_views](https://duckdb.org/community_extensions/extensions/semantic_views.html) | [duckdb-semantic-views](https://github.com/anentropic/duckdb-semantic-views) | 🟢 Ongoing | 1 - 🔥 Very Active | 2 days ago (2026-08-21 12:13:45 UTC) | 11 | Rust | Semantic Views for DuckDB. |
| 266 | [sheetreader](https://duckdb.org/community_extensions/extensions/sheetreader.html) | [sheetreader-duckdb](https://github.com/polydbms/sheetreader-duckdb) | ❓ Unknown | 4 - 🟠 Stale | 161 days ago (2026-03-15 11:03:07 UTC) | 58 | C++ | DuckDB extension: sheetreader by polydbms |
| 267 | [shellfs](https://duckdb.org/community_extensions/extensions/shellfs.html) | [shellfs](https://github.com/Query-farm/shellfs) | 🟢 Ongoing | 2 - ✅ Active | 30 days ago (2026-07-25 04:27:09 UTC) | 95 | C++ | DuckDB extension allowing shell commands to be used for input and output. |
| 268 | [sistat](https://duckdb.org/community_extensions/extensions/sistat.html) | [duckdb-sistat](https://github.com/fklezin/duckdb-sistat) | ❓ Unknown | 4 - 🟠 Stale | 167 days ago (2026-03-09 09:09:46 UTC) | 3 | C++ | DuckDB extension to query Slovenia's SiStat open data directly using SQL. No... |
| 269 | [sitemap](https://duckdb.org/community_extensions/extensions/sitemap.html) | [duckdb-sitemap](https://github.com/midwork-finds-jobs/duckdb-sitemap) | 🟢 Ongoing | 4 - 🟠 Stale | 187 days ago (2026-02-17 14:13:12 UTC) | 1 | C++ | DuckDB extension for parsing XML sitemaps from websites |
| 270 | [sitting_duck](https://duckdb.org/community_extensions/extensions/sitting_duck.html) | [sitting_duck](https://github.com/teaguesterling/sitting_duck) | 🟢 Ongoing | 2 - ✅ Active | 9 days ago (2026-08-15 06:38:56 UTC) | 29 | C | Sitting Duck is a DuckDB extension that makes Abstract Syntax Trees (ASTs) fr... |
| 271 | [slack](https://github.com/dentiny/duckdb-slack) | [duckdb-slack](https://github.com/dentiny/duckdb-slack) | ❓ Unknown | 4 - 🟠 Stale | 185 days ago (2026-02-19 18:08:54 UTC) | 0 | C++ | DuckDB extension: slack by dentiny |
| 272 | [snowflake](https://duckdb.org/community_extensions/extensions/snowflake.html) | [duckdb-snowflake](https://github.com/iqea-ai/duckdb-snowflake) | 🟢 Ongoing | 2 - ✅ Active | 16 days ago (2026-08-07 09:09:54 UTC) | 59 | C++ | A powerful DuckDB extension that enables seamless querying of Snowflake datab... |
| 273 | [splink_udfs](https://duckdb.org/community_extensions/extensions/splink_udfs.html) | [splink_udfs](https://github.com/moj-analytical-services/splink_udfs) | ❓ Unknown | 4 - 🟠 Stale | 198 days ago (2026-02-06 11:01:11 UTC) | 5 | C++ | DuckDB extension: splink_udfs by moj-analytical-services |
| 274 | [splunk](https://duckdb.org/community_extensions/extensions/splunk.html) | [duckdb-splunk](https://github.com/smithclay/duckdb-splunk) | 🟢 Ongoing | 2 - ✅ Active | 20 days ago (2026-08-03 16:07:52 UTC) | 1 | C++ | read logs from splunk into duckdb |
| 275 | [spxlsx](https://duckdb.org/community_extensions/extensions/spxlsx.html) | [spxlsx](https://github.com/paulmupeters/spxlsx) | 🟢 Ongoing | 1 - 🔥 Very Active | 3 days ago (2026-08-20 13:21:28 UTC) | 2 | C++ | Duckdb extension to read sharepoint lists and excel |
| 276 | [sshfs](https://duckdb.org/community_extensions/extensions/sshfs.html) | [duckdb-sshfs](https://github.com/midwork-finds-jobs/duckdb-sshfs) | 🟢 Ongoing | 3 - 🟡 Stable | 78 days ago (2026-06-06 19:02:46 UTC) | 12 | C++ | DuckDB sshfs extension - Read and write files through ssh inside DuckDB |
| 277 | [st_read_multi](https://duckdb.org/community_extensions/extensions/st_read_multi.html) | [duckdb-ext-st-read-multi](https://github.com/yutannihilation/duckdb-ext-st-read-multi) | 🟢 Ongoing | 1 - 🔥 Very Active | 6 days ago (2026-08-17 13:53:58 UTC) | 10 | Rust | A DuckDB extension to import multiple geospatial files with `ST_Read_Multi()` |
| 278 | [stac](https://duckdb.org/community_extensions/extensions/stac.html) | [duckdb-stac](https://github.com/ahuarte47/duckdb-stac) | 🟢 Ongoing | 2 - ✅ Active | 13 days ago (2026-08-10 16:54:05 UTC) | 22 | C++ | DuckDB extension for reading data from SpatioTemporal Asset Catalogs (STAC) u... |
| 279 | [stats_duck](https://duckdb.org/community_extensions/extensions/stats_duck.html) | [the-stats-duck](https://github.com/KoliStat/the-stats-duck) | 🟢 Ongoing | 1 - 🔥 Very Active | 4 days ago (2026-08-19 20:32:18 UTC) | 57 | C++ | A statistical computing toolkit for DuckDB. |
| 280 | [stochastic](https://duckdb.org/community_extensions/extensions/stochastic.html) | [stochastic](https://github.com/Query-farm/stochastic) | 🟢 Ongoing | 2 - ✅ Active | 30 days ago (2026-07-25 04:27:10 UTC) | 27 | C++ | A DuckDB extension that add comprehensive statistical distribution functions... |
| 281 | [substrait](https://duckdb.org/community_extensions/extensions/substrait.html) | [duckdb-substrait-extension](https://github.com/substrait-io/duckdb-substrait-extension) | 🟢 Ongoing | 2 - ✅ Active | 16 days ago (2026-08-07 10:01:51 UTC) | 68 | C++ | DuckDB extension: substrait by substrait-io |
| 282 | [sudan](https://duckdb.org/community_extensions/extensions/sudan.html) | [duckdb-sudan-](https://github.com/Osman-Geomatics93/duckdb-sudan-) | ❓ Unknown | 4 - 🟠 Stale | 185 days ago (2026-02-19 11:49:28 UTC) | 0 | Jupyter Notebook | DuckDB extension: sudan by Osman-Geomatics93 |
| 283 | [superhuman_docs](https://duckdb.org/community_extensions/extensions/superhuman_docs.html) | [duckdb-superhuman-docs](https://github.com/its-felix/duckdb-superhuman-docs) | 🟢 Ongoing | 2 - ✅ Active | 18 days ago (2026-08-05 22:27:19 UTC) | 0 | Rust | DuckDB extension: superhuman_docs by its-felix |
| 284 | [system_stats](https://duckdb.org/community_extensions/extensions/system_stats.html) | [system_stats](https://github.com/dentiny/system_stats) | 🟢 Ongoing | 2 - ✅ Active | 29 days ago (2026-07-25 22:00:06 UTC) | 4 | C++ | DuckDB extension: system_stats by dentiny |
| 285 | [table_guard](https://duckdb.org/community_extensions/extensions/table_guard.html) | [duckdb-table-guard](https://github.com/yoogoc/duckdb-table-guard) | 🟢 Ongoing | 4 - 🟠 Stale | 101 days ago (2026-05-14 09:52:13 UTC) | 2 | C++ | A DuckDB extension for table-level access control |
| 286 | [table_inspector](https://duckdb.org/community_extensions/extensions/table_inspector.html) | [duckdb-table-inspector](https://github.com/dentiny/duckdb-table-inspector) | 🟢 Ongoing | 2 - ✅ Active | 27 days ago (2026-07-27 17:46:08 UTC) | 2 | C++ | DuckDB extension: table_inspector by dentiny |
| 287 | [talib](https://duckdb.org/community_extensions/extensions/talib.html) | [atm_talib](https://github.com/neuesql/atm_talib) | 🟢 Ongoing | 2 - ✅ Active | 13 days ago (2026-08-10 20:51:26 UTC) | 5 | C++ | A duckdb TA-Lib to add technical analysis in Financial Markets with SQL easily |
| 288 | [tarfs](https://duckdb.org/community_extensions/extensions/tarfs.html) | [duckdb_tarfs](https://github.com/Maxxen/duckdb_tarfs) | ❓ Unknown | 4 - 🟠 Stale | over a year ago (2024-08-26 11:01:47 UTC) | 12 | C++ | DuckDB extension: tarfs by Maxxen |
| 289 | [tera](https://duckdb.org/community_extensions/extensions/tera.html) | [tera](https://github.com/Query-farm/tera) | 🟢 Ongoing | 2 - ✅ Active | 30 days ago (2026-07-25 04:27:11 UTC) | 8 | C++ | DuckDB extension: tera |
| 290 | [textplot](https://duckdb.org/community_extensions/extensions/textplot.html) | [textplot](https://github.com/Query-farm/textplot) | 🟢 Ongoing | 2 - ✅ Active | 30 days ago (2026-07-25 04:27:12 UTC) | 27 | C++ | A DuckDB community extension that enables text-based data visualization direc... |
| 291 | [three_d](https://duckdb.org/community_extensions/extensions/three_d.html) | [duckdb-3d](https://github.com/cityjson/duckdb-3d) | ❓ Unknown | 1 - 🔥 Very Active | today (2026-08-23 18:55:10 UTC) | 3 | C++ | (Experimental) DuckDB extension to process 3D geomerty |
| 292 | [title_mapper](https://duckdb.org/community_extensions/extensions/title_mapper.html) | [duckdb-title-mapper](https://github.com/martin-conur/duckdb-title-mapper) | 🟢 Ongoing | 2 - ✅ Active | 8 days ago (2026-08-16 00:22:39 UTC) | 3 | Rust | DuckDB extension: title_mapper by martin-conur |
| 293 | [toml](https://duckdb.org/community_extensions/extensions/toml.html) | [duckdb-toml](https://github.com/vergenzt/duckdb-toml) | 🟢 Ongoing | 3 - 🟡 Stable | 31 days ago (2026-07-24 05:08:13 UTC) | 0 | C++ | Parse TOML format in DuckDB |
| 294 | [tpch_rust](https://duckdb.org/community_extensions/extensions/tpch_rust.html) | [duckdb-tpch-rust](https://github.com/guillesd/duckdb-tpch-rust) | ❓ Unknown | 3 - 🟡 Stable | 76 days ago (2026-06-08 15:40:17 UTC) | 0 | Rust | DuckDB extension to generate tpch tables using tpch-rs |
| 295 | [tributary](https://duckdb.org/community_extensions/extensions/tributary.html) | [tributary](https://github.com/Query-farm/tributary) | ❓ Unknown | 2 - ✅ Active | 28 days ago (2026-07-26 22:19:25 UTC) | 57 | C++ | A DuckDB Extension for Kafka |
| 296 | [trino_parity](https://duckdb.org/community_extensions/extensions/trino_parity.html) | [duckdb-trino-parity-extension](https://github.com/brikk/duckdb-trino-parity-extension) | 🟢 Ongoing | 2 - ✅ Active | 24 days ago (2026-07-30 14:28:56 UTC) | 0 | C++ | An extension adding functions to duckdb to exactly match Trino function behav... |
| 297 | [tsfile](https://duckdb.org/community_extensions/extensions/tsfile.html) | [tsfile-duckdb](https://github.com/ColinLeeo/tsfile-duckdb) | 🟢 Ongoing | 2 - ✅ Active | 18 days ago (2026-08-06 02:18:53 UTC) | 0 | C++ | DuckDB extension: tsfile by ColinLeeo |
| 298 | [tsid](https://duckdb.org/community_extensions/extensions/tsid.html) | [tsid](https://github.com/Query-farm/tsid) | 🟢 Ongoing | 2 - ✅ Active | 28 days ago (2026-07-26 22:19:26 UTC) | 6 | C++ | TSID Extension for DuckDB  |
| 299 | [turbovec](https://github.com/alitrack/duckdb_turbovec) | [duckdb_turbovec](https://github.com/alitrack/duckdb_turbovec) | ❓ Unknown | 2 - ✅ Active | 26 days ago (2026-07-28 21:52:38 UTC) | 7 | Rust | DuckDB extension: turbovec by alitrack |
| 300 | [ulid](https://duckdb.org/community_extensions/extensions/ulid.html) | [duckdb_ulid](https://github.com/Maxxen/duckdb_ulid) | ❓ Unknown | 4 - 🟠 Stale | over a year ago (2024-07-09 09:35:50 UTC) | 25 | C++ | DuckDB extension: ulid by Maxxen |
| 301 | [urlpattern](https://duckdb.org/community_extensions/extensions/urlpattern.html) | [duckdb_urlpattern](https://github.com/teaguesterling/duckdb_urlpattern) | 🟢 Ongoing | 2 - ✅ Active | 26 days ago (2026-07-28 20:10:15 UTC) | 8 | C++ | An implementation of URLPattern for DuckDB |
| 302 | [us_address_standardizer](https://duckdb.org/community_extensions/extensions/us_address_standardizer.html) | [duckdb-address-standardizer](https://github.com/ericmanning/duckdb-address-standardizer) | 🟢 Ongoing | 4 - 🟠 Stale | 95 days ago (2026-05-20 14:50:54 UTC) | 3 | C | DuckDB extension for parsing and standardizing (USA) postal addresses using P... |
| 303 | [valhalla_routing](https://duckdb.org/community_extensions/extensions/valhalla_routing.html) | [duckdb-valhalla-routing](https://github.com/midwork-finds-jobs/duckdb-valhalla-routing) | 🟢 Ongoing | 4 - 🟠 Stale | 187 days ago (2026-02-17 11:36:12 UTC) | 8 | Makefile | WIP: Attempt to package valhalla routing engine to duckdb |
| 304 | [vindex](https://duckdb.org/community_extensions/extensions/vindex.html) | [duckdb-vector-index](https://github.com/Icemap/duckdb-vector-index) | ❓ Unknown | 3 - 🟡 Stable | 38 days ago (2026-07-16 10:06:50 UTC) | 9 | C++ | A DuckDB extension providing HNSW, IVF, DiskANN, and SPANN vector indexes wit... |
| 305 | [waddle](https://duckdb.org/community_extensions/extensions/waddle.html) | [extension-template](https://github.com/duckdb/extension-template) | ❓ Unknown | 3 - 🟡 Stable | 62 days ago (2026-06-22 10:58:32 UTC) | 290 | Python | Template for DuckDB extensions to help you develop, test and deploy a custom... |
| 306 | [warc](https://duckdb.org/community_extensions/extensions/warc.html) | [duckdb_warc](https://github.com/midwork-finds-jobs/duckdb_warc) | ❓ Unknown | 4 - 🟠 Stale | 199 days ago (2026-02-05 15:33:27 UTC) | 7 | Rust | DuckDB extension for parsing WARC files |
| 307 | [web_archive](https://duckdb.org/community_extensions/extensions/web_archive.html) | [duckdb-web-archive](https://github.com/midwork-finds-jobs/duckdb-web-archive) | 🟢 Ongoing | 3 - 🟡 Stable | 57 days ago (2026-06-27 17:30:16 UTC) | 22 | C++ | DuckDB extension to fetch pages from Wayback Machine & Common Crawl |
| 308 | [web_search](https://duckdb.org/community_extensions/extensions/web_search.html) | [duckdb-web-search](https://github.com/midwork-finds-jobs/duckdb-web-search) | 🟢 Ongoing | 4 - 🟠 Stale | 125 days ago (2026-04-20 21:51:13 UTC) | 0 | C++ | Web/HTTP functionality extension by midwork-finds-jobs |
| 309 | [webbed](https://duckdb.org/community_extensions/extensions/webbed.html) | [duckdb_webbed](https://github.com/teaguesterling/duckdb_webbed) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-08-23 01:10:50 UTC) | 70 | C++ | A comprehensive XML and HTML processing extension for DuckDB that enables SQL... |
| 310 | [webdavfs](https://duckdb.org/community_extensions/extensions/webdavfs.html) | [duckdb-webdavfs](https://github.com/midwork-finds-jobs/duckdb-webdavfs) | ❓ Unknown | 4 - 🟠 Stale | 121 days ago (2026-04-25 03:42:47 UTC) | 1 | C++ | DuckDB WebDAVfs Extension - WebDAV filesystem support for DuckDB |
| 311 | [webmacro](https://duckdb.org/community_extensions/extensions/webmacro.html) | [webmacro](https://github.com/Query-farm/webmacro) | 🟢 Ongoing | 2 - ✅ Active | 28 days ago (2026-07-26 22:19:27 UTC) | 15 | C++ | DuckDB WebMacro: Share and Load your SQL Macros via gists |
| 312 | [whisper](https://duckdb.org/community_extensions/extensions/whisper.html) | [duckdb-whisper](https://github.com/tobilg/duckdb-whisper) | 🟢 Ongoing | 2 - ✅ Active | 16 days ago (2026-08-07 11:33:05 UTC) | 11 | C++ | Use whisper.cpp within DuckDB to translate / transpile speech to text |
| 313 | [wireduck](https://duckdb.org/community_extensions/extensions/wireduck.html) | [wireduck](https://github.com/hyehudai/wireduck) | ❓ Unknown | 4 - 🟠 Stale | 334 days ago (2025-09-23 21:22:03 UTC) | 48 | C++ | Duckdb extension to read pcap files |
| 314 | [yaml](https://duckdb.org/community_extensions/extensions/yaml.html) | [duckdb_yaml](https://github.com/teaguesterling/duckdb_yaml) | 🟢 Ongoing | 2 - ✅ Active | 29 days ago (2026-07-25 19:36:24 UTC) | 21 | C++ |  A DuckDB to read and work with YAML files in a similar way to JSON files (al... |
| 315 | [yardstick](https://duckdb.org/community_extensions/extensions/yardstick.html) | [yardstick](https://github.com/sidequery/yardstick) | ❓ Unknown | 3 - 🟡 Stable | 51 days ago (2026-07-03 19:43:26 UTC) | 58 | Rust | An implementation of Measures in SQL as a DuckDB extension |
| 316 | [zarr](https://duckdb.org/community_extensions/extensions/zarr.html) | [duckdb-zarr](https://github.com/xqlsystems/duckdb-zarr) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-08-22 21:00:31 UTC) | 41 | Rust | Query Zarr stores with SQL directly from DuckDB |
| 317 | [zeek](https://duckdb.org/community_extensions/extensions/zeek.html) | [zeek-duckdb](https://github.com/ynadji/zeek-duckdb) | 🟢 Ongoing | 4 - 🟠 Stale | 131 days ago (2026-04-14 22:02:22 UTC) | 3 | C++ | read_zeek table function to read Zeek TSV logs into DuckDB |
| 318 | [zim](https://duckdb.org/community_extensions/extensions/zim.html) | [duckdb_zim](https://github.com/teaguesterling/duckdb_zim) | 🟢 Ongoing | 1 - 🔥 Very Active | 4 days ago (2026-08-19 15:53:31 UTC) | 5 | C++ | DuckDB extension for working with zim files |
| 319 | [zipfs](https://duckdb.org/community_extensions/extensions/zipfs.html) | [duckdb-zipfs](https://github.com/isaacbrodsky/duckdb-zipfs) | 🟢 Ongoing | 3 - 🟡 Stable | 32 days ago (2026-07-22 17:04:46 UTC) | 68 | C++ | DuckDB extension to read files within zip archives. |

</details>
## Appendix: DuckDB Release Information

### Current Release Context

DuckDB follows **semantic versioning** with regular releases. For complete and up-to-date release information, see the official [**DuckDB Release Calendar**](https://duckdb.org/release_calendar.html).

### Upcoming Releases

|| Version | Planned Date | LTS |
||---------|-------------|-----|
|| v1.5.6 📅 | 2026-09-16 |  |

### Recent Releases

|| Version | Release Date | Codename | Named After | LTS | Status |
||---------|--------------|----------|-------------|-----|--------|
|| **v1.5.5** | 2026-07-22 | – | – |  | Active |
|| **v1.5.4** | 2026-06-17 | – | – |  | Active |
|| **v1.4.5** | 2026-06-17 | – | – | ✓ | Active |
|| **v1.5.3** | 2026-05-20 | – | – |  | Active |
|| **v1.5.2** | 2026-04-13 | – | – |  | Active |
|| **v1.5.1** | 2026-03-23 | – | – |  | Active |
|| **v1.5.0** | 2026-03-09 | Variegata | *Paradise shelduck* |  | Active |
|| **v1.4.4** | 2026-01-27 | – | – | ✓ | Active |
|| **v1.4.3** | 2025-12-09 | – | – | ✓ | Active |
|| **v1.4.2** | 2025-11-12 | – | – | ✓ | Active |
|| **v1.4.1** | 2025-10-07 | – | – | ✓ | Active |
|| **v1.4.0** | 2025-09-16 | Andium | *Andean teal* | ✓ | Active |
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

<p class="fine-print">Last updated: 2026-08-24</p>
