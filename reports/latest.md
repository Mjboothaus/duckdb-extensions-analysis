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
- **335** total extensions tracked (**29** core, **306** community)
- **75 / 335** extensions updated in the last 7 days
- **178 / 335** extensions updated in the last 30 days
- **1** community repositories are archived
- **109** community extensions have unknown/repo issues (missing or inaccessible repositories)

### Highlights
#### Most active (last 7 days)
| Extension | Repository | Last activity |
|---|---|---|
| [duckpgq](https://duckdb.org/community_extensions/extensions/duckpgq.html) | [duckpgq-extension](https://github.com/cwida/duckpgq-extension) | today (2026-08-07 07:14:48 UTC) |
| [anofox_forecast](https://duckdb.org/community_extensions/extensions/anofox_forecast.html) | [anofox-forecast](https://github.com/DataZooDE/anofox-forecast) | today (2026-08-07 06:51:56 UTC) |
| [anofox_scenario](https://duckdb.org/community_extensions/extensions/anofox_scenario.html) | [anofox-scenario](https://github.com/DataZooDE/anofox-scenario) | today (2026-08-07 06:51:47 UTC) |
| [anofox_similarity](https://duckdb.org/community_extensions/extensions/anofox_similarity.html) | [anofox-similarity](https://github.com/DataZooDE/anofox-similarity) | today (2026-08-07 06:51:50 UTC) |
| [anofox_statistics](https://duckdb.org/community_extensions/extensions/anofox_statistics.html) | [anofox-statistics](https://github.com/DataZooDE/anofox-statistics) | today (2026-08-07 06:53:07 UTC) |

#### Most starred (community)
| Extension | Repository | Stars |
|---|---|---:|
| [duckpgq](https://duckdb.org/community_extensions/extensions/duckpgq.html) | [duckpgq-extension](https://github.com/cwida/duckpgq-extension) | 471 |
| [flock](https://duckdb.org/community_extensions/extensions/flock.html) | [flock](https://github.com/dais-polymtl/flock) | 353 |
| [gsheets](https://duckdb.org/community_extensions/extensions/gsheets.html) | [duckdb_gsheets](https://github.com/evidence-dev/duckdb_gsheets) | 348 |
| [airport](https://duckdb.org/community_extensions/extensions/airport.html) | [airport](https://github.com/Query-farm/airport) | 346 |
| [prql](https://duckdb.org/community_extensions/extensions/prql.html) | [duckdb-prql](https://github.com/ywelsch/duckdb-prql) | 327 |

### How to read the report
- **Status** is a repository signal (ongoing / archived / unknown).
- **Activity** is based on the last git push; quiet projects can still be healthy.
- Use the tables below to drill into **Core Extensions** and **Community Extensions**.

---
## Summary

### 📊 Quick Stats (with trends)

| **Metric** | **Current** | **Change** |
|------------|-------------|------------|
| **Total Extensions** | 335 | +9 🔼 |
| **Core Extensions** | 29 | → Stable |
| **Community Extensions** | 306 | +9 🔼 |
| **Recently Active** (≤ 30 days) | 178 (53.1%) | +20 🔼 |
| **Very Active** (≤ 7 days) | 75 (22.4%) | — |

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
| 1 | [autocomplete](https://duckdb.org/docs/current/core_extensions/autocomplete) | [duckdb/duckdb](https://github.com/duckdb/duckdb/tree/main/extension/autocomplete) | 🟢 Ongoing | 3 days ago (2026-08-04 06:52:47 UTC) | N/A (part of core DuckDB repo) | C++ | Core DuckDB extension: autocomplete |
| 2 | [avro](https://duckdb.org/docs/current/core_extensions/avro) | [duckdb-avro](https://github.com/duckdb/duckdb-avro) | 🟢 Ongoing | today (2026-08-06 07:08:37 UTC) | 36 | C++ | Apache Avro format support |
| 3 | [aws](https://duckdb.org/docs/current/core_extensions/aws) | [duckdb-aws](https://github.com/duckdb/duckdb-aws) | 🟢 Ongoing | 14 days ago (2026-07-23 08:47:01 UTC) | 64 | C++ | AWS S3 integration |
| 4 | [azure](https://duckdb.org/docs/current/core_extensions/azure) | [duckdb-azure](https://github.com/duckdb/duckdb-azure) | 🟢 Ongoing | 15 days ago (2026-07-22 16:59:11 UTC) | 77 | C++ | Azure extension for DuckDB |
| 5 | [delta](https://duckdb.org/docs/current/core_extensions/delta) | [duckdb-delta](https://github.com/duckdb/duckdb-delta) | 🟢 Ongoing | 24 days ago (2026-07-13 19:23:42 UTC) | 228 | C++ | DuckDB extension for Delta Lake |
| 6 | [ducklake](https://duckdb.org/docs/current/core_extensions/ducklake) | [duckdb/ducklake](https://github.com/duckdb/ducklake) | 🟢 Ongoing | 15 days ago | N/A (part of core DuckDB repo) | C++ | Delta Lake support via DuckLake (different from delta extension) |
| 7 | [encodings](https://duckdb.org/docs/current/core_extensions/encodings) | [duckdb-encodings](https://github.com/duckdb/duckdb-encodings) | 🟢 Ongoing | 171 days ago (2026-02-16 11:43:18 UTC) | 15 | C++ | Character encoding support |
| 8 | [excel](https://duckdb.org/docs/current/core_extensions/excel) | [duckdb-excel](https://github.com/duckdb/duckdb-excel) | 🟢 Ongoing | 70 days ago (2026-05-28 14:57:36 UTC) | 60 | C++ | Excel extension for DuckDB |
| 9 | [fts](https://duckdb.org/docs/current/core_extensions/full_text_search) | [duckdb-fts](https://github.com/duckdb/duckdb-fts) | 🟢 Ongoing | 2 days ago (2026-08-04 08:38:35 UTC) | 41 | C++ | Full-text search functionality |
| 10 | [httpfs](https://duckdb.org/docs/current/core_extensions/httpfs/overview) | [duckdb-httpfs](https://github.com/duckdb/duckdb-httpfs) | 🟢 Ongoing | today (2026-08-06 14:52:52 UTC) | 59 | C++ | HTTP/S3 filesystem support |
| 11 | [iceberg](https://duckdb.org/docs/current/core_extensions/iceberg/overview) | [duckdb-iceberg](https://github.com/duckdb/duckdb-iceberg) | 🟢 Ongoing | today (2026-08-06 14:45:12 UTC) | 422 | C++ | Apache Iceberg format support |
| 12 | [icu](https://duckdb.org/docs/current/core_extensions/icu) | [duckdb/duckdb](https://github.com/duckdb/duckdb/tree/main/extension/icu) | 🟢 Ongoing | today (2026-08-05 15:18:32 UTC) | N/A (part of core DuckDB repo) | C++ | Core DuckDB extension: icu |
| 13 | [inet](https://duckdb.org/docs/current/core_extensions/inet) | [duckdb-inet](https://github.com/duckdb/duckdb-inet) | 🟢 Ongoing | 259 days ago (2025-11-20 22:54:12 UTC) | 14 | C++ | Internet address data types |
| 14 | [json](https://duckdb.org/docs/current/data/json/overview) | [duckdb/duckdb](https://github.com/duckdb/duckdb/tree/main/extension/json) | 🟢 Ongoing | 2 days ago (2026-08-04 16:55:44 UTC) | N/A (part of core DuckDB repo) | C++ | Core DuckDB extension: json |
| 15 | [lance](https://duckdb.org/docs/current/core_extensions/lance) | [lance-duckdb](https://github.com/lance-format/lance-duckdb) | 🟢 Ongoing | 6 days ago (2026-08-01 01:40:17 UTC) | 125 | C++ | The lance extensions for DuckDB enable reading and writing of lance tables. |
| 16 | [motherduck](https://duckdb.org/docs/current/core_extensions/motherduck) | [duckdb/duckdb](https://github.com/duckdb/duckdb) *(Third Party - Closed source - maintained by MotherDuck Inc.)* | 🟢 Ongoing | 15 days ago | N/A (part of core DuckDB repo) | C++ | Core DuckDB extension: motherduck |
| 17 | [mysql](https://duckdb.org/docs/current/core_extensions/mysql) | [duckdb-mysql](https://github.com/duckdb/duckdb-mysql) | 🟢 Ongoing | today (2026-08-05 17:16:44 UTC) | 98 | C++ | MySQL database connectivity |
| 18 | [odbc](https://duckdb.org/docs/current/core_extensions/odbc/overview) | [odbc-scanner](https://github.com/duckdb/odbc-scanner) | 🟢 Ongoing | 68 days ago (2026-05-30 11:58:55 UTC) | 38 | C++ | DuckDB ODBC extension |
| 19 | [parquet](https://duckdb.org/docs/current/data/parquet/overview) | [duckdb/duckdb](https://github.com/duckdb/duckdb/tree/main/extension/parquet) | 🟢 Ongoing | today (2026-08-05 14:57:22 UTC) | N/A (part of core DuckDB repo) | C++ | Core DuckDB extension: parquet |
| 20 | [postgres](https://duckdb.org/docs/current/core_extensions/postgres/overview) | [duckdb-postgres](https://github.com/duckdb/duckdb-postgres) | 🟢 Ongoing | today (2026-08-06 19:59:57 UTC) | 370 | C++ | PostgreSQL database connectivity |
| 21 | [quack](https://duckdb.org/docs/current/core_extensions/quack) | [duckdb-quack](https://github.com/duckdb/duckdb-quack) | 🟢 Ongoing | 17 days ago (2026-07-20 13:50:21 UTC) | 144 | C++ | Quack remote protocol |
| 22 | [spatial](https://duckdb.org/docs/current/core_extensions/spatial/overview) | [duckdb-spatial](https://github.com/duckdb/duckdb-spatial) | 🟢 Ongoing | 3 days ago (2026-08-03 08:18:04 UTC) | 699 | C++ | Geospatial data types and functions |
| 23 | [sqlite](https://duckdb.org/docs/current/core_extensions/sqlite) | [duckdb-sqlite](https://github.com/duckdb/duckdb-sqlite) | 🟢 Ongoing | 25 days ago (2026-07-12 16:53:10 UTC) | 288 | C++ | DuckDB extension to read and write to SQLite databases |
| 24 | [tpcds](https://duckdb.org/docs/current/core_extensions/tpcds) | [duckdb/duckdb](https://github.com/duckdb/duckdb/tree/main/extension/tpcds) | 🟢 Ongoing | 3 days ago (2026-08-04 06:52:47 UTC) | N/A (part of core DuckDB repo) | C++ | Core DuckDB extension: tpcds |
| 25 | [tpch](https://duckdb.org/docs/current/core_extensions/tpch) | [duckdb/duckdb](https://github.com/duckdb/duckdb/tree/main/extension/tpch) | 🟢 Ongoing | 3 days ago (2026-08-04 06:52:47 UTC) | N/A (part of core DuckDB repo) | C++ | Core DuckDB extension: tpch |
| 26 | [ui](https://duckdb.org/docs/current/core_extensions/ui) | [duckdb-ui](https://github.com/duckdb/duckdb-ui) | 🟢 Ongoing | 7 days ago (2026-07-30 20:41:06 UTC) | 459 | C++ | Browser-based user interface for DuckDB |
| 27 | [unity_catalog](https://duckdb.org/docs/current/core_extensions/unity_catalog) | [unity_catalog](https://github.com/duckdb/unity_catalog) | 🟢 Ongoing | 9 days ago (2026-07-28 07:37:41 UTC) | 107 | C++ | Proof-of-concept extension combining the delta extension with Unity Catalog |
| 28 | [vortex](https://duckdb.org/docs/current/core_extensions/vortex) | [duckdb/duckdb](https://github.com/duckdb/duckdb) *(Third Party - Closed source - third-party extension)* | 🟢 Ongoing | 15 days ago | N/A (part of core DuckDB repo) | C++ | Core DuckDB extension: vortex |
| 29 | [vss](https://duckdb.org/docs/current/core_extensions/vss) | [duckdb-vss](https://github.com/duckdb/duckdb-vss) | 🟢 Ongoing | 44 days ago (2026-06-23 11:03:14 UTC) | 264 | C++ | Vector similarity search |

</details>

---
---
## Community Extensions

Third-party extensions maintained by the community


**Total:** 306 extensions | 🔥 Very Active (≤7d): 75 | ✅ Active (≤30d): 103 | 🟡 Stable (≤90d): 52 | 🟠 Stale (>90d): 76

<details open markdown="1">
<summary>Click to expand/collapse community extensions table</summary>

| # | Extension | Repository | Status | Activity | Last Activity | Stars | Language | Description |
|---|-----------|------------|--------|----------|---------------|-------|----------|-------------|
| 1 | [a5](https://duckdb.org/community_extensions/extensions/a5.html) | [a5](https://github.com/Query-farm/a5) | 🟢 Ongoing | 2 - ✅ Active | 13 days ago (2026-07-25 04:26:43 UTC) | 12 | C++ | A5 Geospatial Extension for DuckDB |
| 2 | [acp](https://duckdb.org/community_extensions/extensions/acp.html) | [duckdb-acp](https://github.com/sidequery/duckdb-acp) | 🟡 Archived | 4 - 🟠 Stale | 239 days ago (2025-12-11 03:36:46 UTC) | 57 | Rust | Use Claude Code & other AI agents from inside DuckDB via extension |
| 3 | [adbc](https://duckdb.org/community_extensions/extensions/adbc.html) | [duckdb-adbc-client](https://github.com/columnar-tech/duckdb-adbc-client) | 🟢 Ongoing | 2 - ✅ Active | 14 days ago (2026-07-23 16:18:38 UTC) | 42 | C++ | ADBC Client for DuckDB  |
| 4 | [adbc_scanner](https://duckdb.org/community_extensions/extensions/adbc_scanner.html) | [adbc_scanner](https://github.com/Query-farm/adbc_scanner) | 🟢 Ongoing | 2 - ✅ Active | 8 days ago (2026-07-29 13:22:05 UTC) | 18 | C++ | A DuckDB ADBC Scanner Extension - adds support for using ADBC drivers with Du... |
| 5 | [agent_data](https://duckdb.org/community_extensions/extensions/agent_data.html) | [agent_data_duckdb](https://github.com/axsaucedo/agent_data_duckdb) | 🟢 Ongoing | 1 - 🔥 Very Active | 6 days ago (2026-08-01 03:42:26 UTC) | 23 | Rust | DuckDB extension: agent_data by axsaucedo |
| 6 | [ai](https://duckdb.org/community_extensions/extensions/ai.html) | [duckdb-ai](https://github.com/leonardovida/duckdb-ai) | ❓ Unknown | 1 - 🔥 Very Active | 6 days ago (2026-07-31 10:35:20 UTC) | 7 | C++ | Enhance DuckDB with AI functions, supporting all providers as well as local m... |
| 7 | [airport](https://duckdb.org/community_extensions/extensions/airport.html) | [airport](https://github.com/Query-farm/airport) | 🟢 Ongoing | 2 - ✅ Active | 13 days ago (2026-07-25 04:26:50 UTC) | 346 | C++ | The Airport extension for DuckDB, enables the use of Arrow Flight with DuckDB |
| 8 | [aixchess](https://duckdb.org/community_extensions/extensions/aixchess.html) | [aix](https://github.com/thomas-daniels/aix) | 🟢 Ongoing | 4 - 🟠 Stale | 130 days ago (2026-03-29 12:16:27 UTC) | 26 | Rust | Aix: Efficiently storing and querying chess game collections |
| 9 | [altertable](https://duckdb.org/community_extensions/extensions/altertable.html) | [duckdb-altertable](https://github.com/altertable-ai/duckdb-altertable) | 🟢 Ongoing | 1 - 🔥 Very Active | 7 days ago (2026-07-30 07:54:49 UTC) | 0 | C++ | Query Altertable's lakehouse directly from your local DuckDB |
| 10 | [anndata](https://duckdb.org/community_extensions/extensions/anndata.html) | [anndata-duckdb-extension](https://github.com/honicky/anndata-duckdb-extension) | ❓ Unknown | 2 - ✅ Active | 30 days ago (2026-07-07 16:10:59 UTC) | 9 | C++ | Attach and AnnData file in duckdb and query it with SQL.  Perform SQL over gr... |
| 11 | [anofox_forecast](https://duckdb.org/community_extensions/extensions/anofox_forecast.html) | [anofox-forecast](https://github.com/DataZooDE/anofox-forecast) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-08-07 06:51:56 UTC) | 36 | C++ | Statistical timeseries forecasting in DuckDB |
| 12 | [anofox_scenario](https://duckdb.org/community_extensions/extensions/anofox_scenario.html) | [anofox-scenario](https://github.com/DataZooDE/anofox-scenario) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-08-07 06:51:47 UTC) | 2 | C++ | DuckDB extension for Git-like database branching. Create isolated scenarios f... |
| 13 | [anofox_similarity](https://duckdb.org/community_extensions/extensions/anofox_similarity.html) | [anofox-similarity](https://github.com/DataZooDE/anofox-similarity) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-08-07 06:51:50 UTC) | 2 | C++ | DuckDB extension for multi-modal product similarity for manufacturing supply... |
| 14 | [anofox_statistics](https://duckdb.org/community_extensions/extensions/anofox_statistics.html) | [anofox-statistics](https://github.com/DataZooDE/anofox-statistics) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-08-07 06:53:07 UTC) | 14 | C++ | A DuckDB extension for statistical regression analysis, providing OLS, Ridge,... |
| 15 | [anofox_tabfm](https://duckdb.org/community_extensions/extensions/anofox_tabfm.html) | [anofox-tabfm](https://github.com/DataZooDE/anofox-tabfm) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-08-07 06:52:02 UTC) | 4 | C++ | DuckDB extension for tabular foundation models — zero-shot classification & r... |
| 16 | [anofox_tabular](https://duckdb.org/community_extensions/extensions/anofox_tabular.html) | [anofox-tabular](https://github.com/DataZooDE/anofox-tabular) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-08-07 06:51:59 UTC) | 16 | C++ | A duckdb extension which combines data quality and data preparation tools for... |
| 17 | [anofox_visualization](https://duckdb.org/community_extensions/extensions/anofox_visualization.html) | [anofox-visualization](https://github.com/DataZooDE/anofox-visualization) | 🟢 Ongoing | 1 - 🔥 Very Active | 6 days ago (2026-07-31 21:50:15 UTC) | 2 | Rust | Charts & dashboards for DuckDB — the grammar of graphics, straight from SQL.... |
| 18 | [arrow](https://duckdb.org/community_extensions/extensions/arrow.html) | [duckdb-extension-alias](https://github.com/duckdb/duckdb-extension-alias) | ❓ Unknown | 4 - 🟠 Stale | 304 days ago (2025-10-06 09:07:38 UTC) | 4 | C | DuckDB extension: arrow |
| 19 | [astro](https://duckdb.org/community_extensions/extensions/astro.html) | [astro-duck](https://github.com/synapticore-io/astro-duck) | 🟢 Ongoing | 3 - 🟡 Stable | 79 days ago (2026-05-19 12:22:23 UTC) | 2 | C++ | 60+ astronomical SQL functions for DuckDB: coordinate transforms, CCM89 dust... |
| 20 | [behavioral](https://duckdb.org/community_extensions/extensions/behavioral.html) | [duckdb-behavioral](https://github.com/tomtom215/duckdb-behavioral) | 🟢 Ongoing | 2 - ✅ Active | 10 days ago (2026-07-27 18:44:41 UTC) | 12 | Rust | A DuckDB Community Extension to enable Behavioral Analytics, inspired by Clic... |
| 21 | [bigquery](https://duckdb.org/community_extensions/extensions/bigquery.html) | [duckdb-bigquery](https://github.com/hafenkran/duckdb-bigquery) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-08-06 20:05:03 UTC) | 167 | C++ | Integrates DuckDB with Google BigQuery, allowing direct querying and manageme... |
| 22 | [bitfilters](https://duckdb.org/community_extensions/extensions/bitfilters.html) | [bitfilters](https://github.com/Query-farm/bitfilters) | 🟢 Ongoing | 2 - ✅ Active | 13 days ago (2026-07-25 04:26:45 UTC) | 8 | C++ | A high-performance DuckDB extension providing probabilistic data structures f... |
| 23 | [blockduck](https://duckdb.org/community_extensions/extensions/blockduck.html) | [BlockDuck](https://github.com/luohaha/BlockDuck) | 🟢 Ongoing | 4 - 🟠 Stale | 302 days ago (2025-10-08 16:19:04 UTC) | 10 | C++ | Live SQL Queries on Blockchain |
| 24 | [boilstream](https://duckdb.org/community_extensions/extensions/boilstream.html) | [boilstream-extension](https://github.com/dforsber/boilstream-extension) | 🟢 Ongoing | 3 - 🟡 Stable | 61 days ago (2026-06-06 11:38:11 UTC) | 10 | C++ | Secure Remote Secrets Storage for DuckDB |
| 25 | [brew](https://duckdb.org/community_extensions/extensions/brew.html) | [duckdb-brew](https://github.com/adriens/duckdb-brew) | 🟢 Ongoing | 3 - 🟡 Stable | 67 days ago (2026-05-31 08:18:52 UTC) | 1 | C++ | duckdb extension to report installed brew packages/casks/formulas with SQL |
| 26 | [bvh2sql](https://duckdb.org/community_extensions/extensions/bvh2sql.html) | [bvh2sql](https://github.com/nkwork9999/bvh2sql) | 🟢 Ongoing | 3 - 🟡 Stable | 55 days ago (2026-06-12 12:17:09 UTC) | 0 | Makefile | SQL-related extension by nkwork9999 |
| 27 | [cache_httpfs](https://duckdb.org/community_extensions/extensions/cache_httpfs.html) | [duck-read-cache-fs](https://github.com/dentiny/duck-read-cache-fs) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-08-06 22:55:34 UTC) | 143 | C++ | This repository is made as read-only filesystem for remote access. |
| 28 | [cache_prewarm](https://duckdb.org/community_extensions/extensions/cache_prewarm.html) | [duckdb-cache-prewarm](https://github.com/dentiny/duckdb-cache-prewarm) | 🟢 Ongoing | 2 - ✅ Active | 10 days ago (2026-07-28 05:02:52 UTC) | 9 | C++ | DuckDB extension: cache_prewarm by dentiny |
| 29 | [capi_quack](https://duckdb.org/community_extensions/extensions/capi_quack.html) | [extension-template-c](https://github.com/duckdb/extension-template-c) | ❓ Unknown | 2 - ✅ Active | 13 days ago (2026-07-24 09:22:27 UTC) | 31 | C | (Experimental) C/C++ template for DuckDB extensions based on the C API |
| 30 | [cassandra](https://duckdb.org/community_extensions/extensions/cassandra.html) | [duckdb-cassandra](https://github.com/dioptre/duckdb-cassandra) | ❓ Unknown | 4 - 🟠 Stale | 290 days ago (2025-10-20 19:15:10 UTC) | 2 | C++ | DuckDB Connector for Cassandra |
| 31 | [celestial](https://duckdb.org/community_extensions/extensions/celestial.html) | [duckdb-celestial](https://github.com/lisa-sgs/duckdb-celestial) | ❓ Unknown | 1 - 🔥 Very Active | today (2026-08-06 12:40:03 UTC) | 2 | C++ | DuckDB extension providing astronomical coordinates utilities |
| 32 | [chaos](https://duckdb.org/community_extensions/extensions/chaos.html) | [duckdb-chaos](https://github.com/taniabogatsch/duckdb-chaos) | 🟢 Ongoing | 4 - 🟠 Stale | 175 days ago (2026-02-12 14:50:01 UTC) | 1 | C++ | DuckDB extension: chaos by taniabogatsch |
| 33 | [chess](https://duckdb.org/community_extensions/extensions/chess.html) | [duckdb-chess](https://github.com/dotneB/duckdb-chess) | ❓ Unknown | 3 - 🟡 Stable | 71 days ago (2026-05-28 05:13:34 UTC) | 3 | Rust | A DuckDB extension for parsing and analyzing chess games in PGN format. |
| 34 | [chsql](https://duckdb.org/community_extensions/extensions/chsql.html) | [clickhouse-sql](https://github.com/Query-farm/clickhouse-sql) | ❓ Unknown | 4 - 🟠 Stale | 169 days ago (2026-02-18 19:49:47 UTC) | 93 | C++ | DuckDB Community Extension implementing ClickHouse SQL Dialect macros and Cus... |
| 35 | [chsql_native](https://duckdb.org/community_extensions/extensions/chsql_native.html) | [clickhouse-native](https://github.com/Query-farm/clickhouse-native) | ❓ Unknown | 4 - 🟠 Stale | 169 days ago (2026-02-18 19:49:46 UTC) | 20 | Rust | Experimental ClickHouse Native Client and Native file reader Extension for Du... |
| 36 | [cityjson](https://duckdb.org/community_extensions/extensions/cityjson.html) | [duckdb-cityjson](https://github.com/cityjson/duckdb-cityjson) | 🟢 Ongoing | 2 - ✅ Active | 9 days ago (2026-07-28 09:32:35 UTC) | 9 | C++ | (Still Experimental) DuckDB extension for CityJSON |
| 37 | [clamp](https://duckdb.org/community_extensions/extensions/clamp.html) | [duckdb_clamp](https://github.com/oglego/duckdb_clamp) | 🟢 Ongoing | 4 - 🟠 Stale | 103 days ago (2026-04-26 01:35:35 UTC) | 2 | C++ | The Clamp extension introduces range-clamping scalar functions to DuckDB. Ini... |
| 38 | [cloudfront](https://duckdb.org/community_extensions/extensions/cloudfront.html) | [duckdb-cloudfront](https://github.com/midwork-finds-jobs/duckdb-cloudfront) | 🟢 Ongoing | 4 - 🟠 Stale | 182 days ago (2026-02-05 15:32:51 UTC) | 1 | C++ | DuckDB module which provides custom authentication methods on top of httpfs m... |
| 39 | [cloudfs](https://duckdb.org/community_extensions/extensions/cloudfs.html) | [cloudfs](https://github.com/trouchet/cloudfs) | ❓ Unknown | 1 - 🔥 Very Active | 7 days ago (2026-07-31 01:28:12 UTC) | 2 | C++ | A duckdb-based cloud filesystem query engine |
| 40 | [cog](https://duckdb.org/community_extensions/extensions/cog.html) | [duckdb-cog](https://github.com/st-layer/duckdb-cog) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-08-06 08:48:58 UTC) | 2 | Rust | GDAL-free COG raster access for DuckDB. Query Cloud-Optimized GeoTIFFs in pla... |
| 41 | [cozip](https://duckdb.org/community_extensions/extensions/cozip.html) | [cozip_reader](https://github.com/asterisk-labs/cozip_reader) | 🟢 Ongoing | 3 - 🟡 Stable | 84 days ago (2026-05-15 05:12:11 UTC) | 7 | C++ | Read Cloud-Optimized ZIP files |
| 42 | [crawler](https://duckdb.org/community_extensions/extensions/crawler.html) | [duckdb-crawler](https://github.com/midwork-finds-jobs/duckdb-crawler) | 🟢 Ongoing | 4 - 🟠 Stale | 126 days ago (2026-04-03 04:32:07 UTC) | 12 | C++ | DuckDB extension: crawler by midwork-finds-jobs |
| 43 | [cronjob](https://duckdb.org/community_extensions/extensions/cronjob.html) | [cronjob](https://github.com/Query-farm/cronjob) | 🟢 Ongoing | 2 - ✅ Active | 11 days ago (2026-07-26 22:19:07 UTC) | 52 | C++ | DuckDB CronJob Extension |
| 44 | [crypto](https://duckdb.org/community_extensions/extensions/crypto.html) | [crypto](https://github.com/Query-farm/crypto) | 🟢 Ongoing | 2 - ✅ Active | 13 days ago (2026-07-25 04:26:47 UTC) | 30 | C++ | DuckDB Extension for cryptographic hash functions and HMAC |
| 45 | [curl_httpfs](https://duckdb.org/community_extensions/extensions/curl_httpfs.html) | [duckdb-curl-filesystem](https://github.com/dentiny/duckdb-curl-filesystem) | 🟢 Ongoing | 2 - ✅ Active | 12 days ago (2026-07-25 18:56:13 UTC) | 12 | C++ | Filesystem built upon libcurl. |
| 46 | [cwiqduck](https://duckdb.org/community_extensions/extensions/cwiqduck.html) | [cwiqduck](https://github.com/cwiq-os/cwiqduck) | 🟢 Ongoing | 3 - 🟡 Stable | 50 days ago (2026-06-18 04:35:52 UTC) | 3 | C++ | DuckDB extensions for CWIQ |
| 47 | [dash](https://duckdb.org/community_extensions/extensions/dash.html) | [dash](https://github.com/gropaul/dash) | 🟢 Ongoing | 1 - 🔥 Very Active | 6 days ago (2026-07-31 20:26:31 UTC) | 76 | C++ | Local GUI and Data Canvas as a DuckDB extension |
| 48 | [datadog](https://duckdb.org/community_extensions/extensions/datadog.html) | [duckdb-datadog](https://github.com/smithclay/duckdb-datadog) | ❓ Unknown | 1 - 🔥 Very Active | today (2026-08-06 21:14:01 UTC) | 2 | C++ | ingest logs and metrics (and soon traces) from datadog into duckdb |
| 49 | [datasketches](https://duckdb.org/community_extensions/extensions/datasketches.html) | [datasketches](https://github.com/Query-farm/datasketches) | 🟢 Ongoing | 2 - ✅ Active | 13 days ago (2026-07-25 04:26:48 UTC) | 48 | C++ | Integrates DuckDB with the high-performance Apache DataSketches library. This... |
| 50 | [dazzleduck](https://duckdb.org/community_extensions/extensions/dazzleduck.html) | [dazzleduck-sql-duckdb](https://github.com/dazzleduck-web/dazzleduck-sql-duckdb) | ❓ Unknown | 4 - 🟠 Stale | 147 days ago (2026-03-12 22:24:42 UTC) | 1 | C++ | DuckDB extension: dazzleduck by dazzleduck-web |
| 51 | [dbn](https://duckdb.org/community_extensions/extensions/dbn.html) | [duckdb-dbn](https://github.com/tbeason/duckdb-dbn) | ❓ Unknown | 3 - 🟡 Stable | 58 days ago (2026-06-09 19:42:19 UTC) | 1 | C++ | DuckDB extension for reading Databento Binary Encoding (DBN) files |
| 52 | [decimal_arithmetic](https://duckdb.org/community_extensions/extensions/decimal_arithmetic.html) | [duckdb-decimal-arithmetic](https://github.com/duckdb/duckdb-decimal-arithmetic) | 🟢 Ongoing | 2 - ✅ Active | 28 days ago (2026-07-09 10:55:37 UTC) | 4 | C++ | DuckDB extension: decimal_arithmetic |
| 53 | [deferred_columns](https://duckdb.org/community_extensions/extensions/deferred_columns.html) | [deferred-columns](https://github.com/iwinalbert/deferred-columns) | ❓ Unknown | 2 - ✅ Active | 25 days ago (2026-07-12 17:08:25 UTC) | 3 | C++ | DuckDB extension: deferred_columns by iwinalbert |
| 54 | [delta_classic](https://duckdb.org/community_extensions/extensions/delta_classic.html) | [delta_classic](https://github.com/djouallah/delta_classic) | 🟢 Ongoing | 3 - 🟡 Stable | 48 days ago (2026-06-19 15:04:33 UTC) | 5 | C++ | DuckDB extension to attach a directory of Delta tables as a database |
| 55 | [delta_export](https://duckdb.org/community_extensions/extensions/delta_export.html) | [delta_export](https://github.com/djouallah/delta_export) | 🟢 Ongoing | 2 - ✅ Active | 14 days ago (2026-07-24 01:30:50 UTC) | 7 | C++ | DuckDB extension to export Delta Lake metadata from DuckLake |
| 56 | [dicom](https://duckdb.org/community_extensions/extensions/dicom.html) | [duck-dicom](https://github.com/nmontesg/duck-dicom) | ❓ Unknown | 2 - ✅ Active | 23 days ago (2026-07-14 13:47:47 UTC) | 0 | C++ | A DuckDB extension to import medical imaging data |
| 57 | [dns](https://duckdb.org/community_extensions/extensions/dns.html) | [duckdb-dns](https://github.com/tobilg/duckdb-dns) | ❓ Unknown | 3 - 🟡 Stable | 40 days ago (2026-06-27 14:09:48 UTC) | 16 | Rust | DNS (Reverse) Lookup Extension for DuckDB |
| 58 | [dplyr](https://duckdb.org/community_extensions/extensions/dplyr.html) | [libdplyr](https://github.com/mrchypark/libdplyr) | ❓ Unknown | 2 - ✅ Active | 23 days ago (2026-07-14 14:31:49 UTC) | 15 | Rust | DuckDB extension: dplyr by mrchypark |
| 59 | [dqtest](https://duckdb.org/community_extensions/extensions/dqtest.html) | [duckdb-dataquality-extension](https://github.com/vhe74/duckdb-dataquality-extension) | ❓ Unknown | 4 - 🟠 Stale | 184 days ago (2026-02-03 18:35:04 UTC) | 5 | C++ | Duckdb extension to run data quality tests |
| 60 | [dryrun](https://duckdb.org/community_extensions/extensions/dryrun.html) | [duckdb-dryrun](https://github.com/aleda145/duckdb-dryrun) | ❓ Unknown | 3 - 🟡 Stable | 46 days ago (2026-06-21 19:06:20 UTC) | 0 | C++ | dry run before execute |
| 61 | [dta](https://duckdb.org/community_extensions/extensions/dta.html) | [duckdb-dta](https://github.com/codedthinking/duckdb-dta) | 🟢 Ongoing | 2 - ✅ Active | 27 days ago (2026-07-10 08:57:32 UTC) | 1 | C++ | DuckDB extension for reading and writing .dta files (formats 117-121) |
| 62 | [duck_block_utils](https://duckdb.org/community_extensions/extensions/duck_block_utils.html) | [duckdb_duck_block_utils](https://github.com/teaguesterling/duckdb_duck_block_utils) | 🟢 Ongoing | 2 - ✅ Active | 11 days ago (2026-07-26 20:43:06 UTC) | 1 | C++ | A collection of utility functions to work with doc block-style structures and... |
| 63 | [duck_delta_share](https://duckdb.org/community_extensions/extensions/duck_delta_share.html) | [duck_delta_share](https://github.com/cwiq-os/duck_delta_share) | 🟢 Ongoing | 3 - 🟡 Stable | 88 days ago (2026-05-10 23:39:27 UTC) | 5 | C++ | DuckDB extension for enabling Delta Sharing client capabilities.  |
| 64 | [duck_dggs](https://duckdb.org/community_extensions/extensions/duck_dggs.html) | [duckdb-dggs](https://github.com/am2222/duckdb-dggs) | ❓ Unknown | 3 - 🟡 Stable | 41 days ago (2026-06-26 20:37:37 UTC) | 1 | C++ | A DuckDB extension for discrete global grid systems (DGGS) powered by DGGRID v8. |
| 65 | [duck_diff](https://duckdb.org/community_extensions/extensions/duck_diff.html) | [duck_diff](https://github.com/avaitla/duck_diff) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-08-06 06:03:03 UTC) | 5 | HTML | Diff any two database tables |
| 66 | [duck_geoarrow](https://duckdb.org/community_extensions/extensions/duck_geoarrow.html) | [duck_geoarrow](https://github.com/am2222/duck_geoarrow) | ❓ Unknown | 4 - 🟠 Stale | 113 days ago (2026-04-15 13:13:55 UTC) | 7 | C++ | This extension, Duck_Geoarrow, provides functions to convert between WKB (Wel... |
| 67 | [duck_hunt](https://duckdb.org/community_extensions/extensions/duck_hunt.html) | [duck_hunt](https://github.com/teaguesterling/duck_hunt) | 🟢 Ongoing | 2 - ✅ Active | 12 days ago (2026-07-25 19:45:57 UTC) | 4 | C++ | Tools for working with unit test suite results |
| 68 | [duck_lineage](https://duckdb.org/community_extensions/extensions/duck_lineage.html) | [duck_lineage](https://github.com/ilum-cloud/duck_lineage) | 🟢 Ongoing | 3 - 🟡 Stable | 72 days ago (2026-05-26 23:21:55 UTC) | 78 | Python | A extension for DuckDB, which captures lineage events for executed queries |
| 69 | [duck_lk](https://duckdb.org/community_extensions/extensions/duck_lk.html) | [duck-lk](https://github.com/nrminor/duck-lk) | ❓ Unknown | 4 - 🟠 Stale | 111 days ago (2026-04-18 03:05:52 UTC) | 0 | Rust | Interact with tables from your LabKey LIMS natively in DuckDB |
| 70 | [duck_tails](https://duckdb.org/community_extensions/extensions/duck_tails.html) | [duck_tails](https://github.com/teaguesterling/duck_tails) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-08-07 05:01:31 UTC) | 20 | C++ | A DuckDB extension for exploring and reading git history. |
| 71 | [duckdb_delta_sharing](https://duckdb.org/community_extensions/extensions/duckdb_delta_sharing.html) | [duckdb-delta-sharing](https://github.com/prequel-co/duckdb-delta-sharing) | 🟢 Ongoing | 3 - 🟡 Stable | 37 days ago (2026-06-30 17:34:12 UTC) | 3 | C++ | An extension for using DuckDB as a delta sharing client |
| 72 | [duckdb_geoip_rs](https://duckdb.org/community_extensions/extensions/duckdb_geoip_rs.html) | [duckdb-geoip-rs](https://github.com/william-billaud/duckdb-geoip-rs) | 🟢 Ongoing | 2 - ✅ Active | 10 days ago (2026-07-27 19:41:57 UTC) | 8 | Rust | Database connectivity extension by william-billaud |
| 73 | [duckdb_mcp](https://duckdb.org/community_extensions/extensions/duckdb_mcp.html) | [duckdb_mcp](https://github.com/teaguesterling/duckdb_mcp) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-08-06 04:06:15 UTC) | 62 | C++ | A simple MCP server extension for DuckDB |
| 74 | [duckdb_midi](https://github.com/nkwork9999/duckdb-midi) | [duckdb-midi](https://github.com/nkwork9999/duckdb-midi) | ❓ Unknown | 3 - 🟡 Stable | 55 days ago (2026-06-12 12:18:36 UTC) | 0 | C++ | Database connectivity extension by nkwork9999 |
| 75 | [duckdb_opendalfs](https://duckdb.org/community_extensions/extensions/duckdb_opendalfs.html) | [duckdb-opendal-filesystem](https://github.com/dentiny/duckdb-opendal-filesystem) | 🟢 Ongoing | 1 - 🔥 Very Active | 3 days ago (2026-08-03 08:42:36 UTC) | 5 | C++ | Database connectivity extension by dentiny |
| 76 | [duckdbi](https://duckdb.org/community_extensions/extensions/duckdbi.html) | [DuckDBI](https://github.com/nkwork9999/DuckDBI) | ❓ Unknown | 4 - 🟠 Stale | 145 days ago (2026-03-14 11:04:19 UTC) | 4 | C++ | Database connectivity extension by nkwork9999 |
| 77 | [duckgl](https://duckdb.org/community_extensions/extensions/duckgl.html) | [duckgl](https://github.com/nkwork9999/duckgl) | 🟢 Ongoing | 4 - 🟠 Stale | 155 days ago (2026-03-04 16:41:20 UTC) | 7 | C++ | DuckDB extension: duckgl by nkwork9999 |
| 78 | [duckgql](https://duckdb.org/community_extensions/extensions/duckgql.html) | [duckdb-gql](https://github.com/rahul-iyer/duckdb-gql) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-08-06 05:48:53 UTC) | 32 | C++ | An extension to run graph queries and algorithms using ISO GQL |
| 79 | [duckherder](https://duckdb.org/community_extensions/extensions/duckherder.html) | [duckdb-distributed-execution](https://github.com/dentiny/duckdb-distributed-execution) | ❓ Unknown | 4 - 🟠 Stale | 149 days ago (2026-03-10 09:36:00 UTC) | 60 | C++ | Distributed execution for duckdb queries. |
| 80 | [duckhog](https://duckdb.org/community_extensions/extensions/duckhog.html) | [duckhog](https://github.com/PostHog/duckhog) | ❓ Unknown | 3 - 🟡 Stable | 42 days ago (2026-06-26 00:52:18 UTC) | 11 | C++ | duckdb extension to connect to posthog managed data warehouse  |
| 81 | [duckhts](https://duckdb.org/community_extensions/extensions/duckhts.html) | [duckhts](https://github.com/RGenomicsETL/duckhts) | 🟢 Ongoing | 1 - 🔥 Very Active | 2 days ago (2026-08-04 23:29:09 UTC) | 16 | C | 'htslib' based 'Duckdb' Extenstion for High Throughput Sequencing File Formats |
| 82 | [ducklake_cdc](https://duckdb.org/community_extensions/extensions/ducklake_cdc.html) | [ducklake-cdc-extension](https://github.com/ekkuleivonen/ducklake-cdc-extension) | ❓ Unknown | 2 - ✅ Active | 10 days ago (2026-07-27 09:15:02 UTC) | 15 | C++ | The missing operational layer for DuckLake’s change feed. |
| 83 | [ducklink](https://duckdb.org/community_extensions/extensions/ducklink.html) | [ducklink-extension](https://github.com/tegmentum/ducklink-extension) | ❓ Unknown | 2 - ✅ Active | 13 days ago (2026-07-24 10:41:04 UTC) | 2 | Rust | Run duckdb:extension WebAssembly components inside DuckDB (community extension) |
| 84 | [ducknng](https://github.com/RGenomicsETL/ducknng) | [ducknng](https://github.com/RGenomicsETL/ducknng) | ❓ Unknown | 1 - 🔥 Very Active | 3 days ago (2026-08-03 20:30:24 UTC) | 3 | C | ducknng: a 'DuckDB' Binding To The 'NNG' Scalability Protocols Library And an... |
| 85 | [duckorch](https://duckdb.org/community_extensions/extensions/duckorch.html) | [duck-orch](https://github.com/nkwork9999/duck-orch) | 🟢 Ongoing | 3 - 🟡 Stable | 53 days ago (2026-06-14 11:27:19 UTC) | 2 | Rust | DuckDB extension: duckorch by nkwork9999 |
| 86 | [duckpgq](https://duckdb.org/community_extensions/extensions/duckpgq.html) | [duckpgq-extension](https://github.com/cwida/duckpgq-extension) | ❓ Unknown | 1 - 🔥 Very Active | today (2026-08-07 07:14:48 UTC) | 471 | C++ | DuckDB extension that adds support for SQL/PGQ and graph algorithms |
| 87 | [ducksmiles](https://duckdb.org/community_extensions/extensions/ducksmiles.html) | [duckSMILES](https://github.com/nkwork9999/duckSMILES) | ❓ Unknown | 3 - 🟡 Stable | 54 days ago (2026-06-14 04:01:17 UTC) | 3 | Rust | DuckDB extension: ducksmiles by nkwork9999 |
| 88 | [ducksync](https://duckdb.org/community_extensions/extensions/ducksync.html) | [ducksync](https://github.com/danjsiegel/ducksync) | 🟢 Ongoing | 1 - 🔥 Very Active | 5 days ago (2026-08-01 23:45:35 UTC) | 7 | C++ | DuckDB extension: ducksync by danjsiegel |
| 89 | [duckthink](https://duckdb.org/community_extensions/extensions/duckthink.html) | [duckthink](https://github.com/pedro-filardi/duckthink) | ❓ Unknown | 3 - 🟡 Stable | 31 days ago (2026-07-06 15:22:58 UTC) | 0 | C++ | ASK() — natural-language SQL for DuckDB, grounded in your dbt Semantic Layer |
| 90 | [ducktinycc](https://duckdb.org/community_extensions/extensions/ducktinycc.html) | [DuckTinyCC](https://github.com/sounkou-bioinfo/DuckTinyCC) | 🟢 Ongoing | 3 - 🟡 Stable | 86 days ago (2026-05-13 06:09:08 UTC) | 3 | C | 'C' Scripting in 'Duckdb' using 'TinyCC' |
| 91 | [duckton](https://duckdb.org/community_extensions/extensions/duckton.html) | [duckton](https://github.com/Angelerator/duckton) | ❓ Unknown | 3 - 🟡 Stable | 42 days ago (2026-06-25 22:07:12 UTC) | 5 | Rust | Duckton — a peer-to-peer distributed DuckDB compute grid over QUIC: broadcast... |
| 92 | [eeagrid](https://duckdb.org/community_extensions/extensions/eeagrid.html) | [duckdb-eeagrid](https://github.com/ahuarte47/duckdb-eeagrid) | 🟢 Ongoing | 2 - ✅ Active | 13 days ago (2026-07-24 12:56:58 UTC) | 0 | C++ | Functions for transforming XY coordinates to and from the EEA Reference Grid... |
| 93 | [eenddb](https://duckdb.org/community_extensions/extensions/eenddb.html) | [eenddb](https://github.com/Dtenwolde/eenddb) | 🟢 Ongoing | 4 - 🟠 Stale | 128 days ago (2026-03-31 09:31:58 UTC) | 5 | C++ | Database connectivity extension by Dtenwolde |
| 94 | [elasticsearch](https://duckdb.org/community_extensions/extensions/elasticsearch.html) | [duckdb-elasticsearch](https://github.com/tlinhart/duckdb-elasticsearch) | ❓ Unknown | 4 - 🟠 Stale | 99 days ago (2026-04-29 13:01:51 UTC) | 21 | C++ | Query Elasticsearch data directly from DuckDB |
| 95 | [erpl_idoc](https://duckdb.org/community_extensions/extensions/erpl_idoc.html) | [erpl-idoc](https://github.com/DataZooDE/erpl-idoc) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-08-07 06:51:36 UTC) | 2 | C++ | Read & write SAP IDoc files (flat + IDoc-XML) as SQL in DuckDB — a community... |
| 96 | [erpl_tunnel](https://duckdb.org/community_extensions/extensions/erpl_tunnel.html) | [erpl-tunnel](https://github.com/DataZooDE/erpl-tunnel) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-08-07 06:51:30 UTC) | 1 | C++ | Zero-dependency DuckDB extension: tunnel raw TCP (quack, SAP RFC, HTTP) over... |
| 97 | [erpl_web](https://duckdb.org/community_extensions/extensions/erpl_web.html) | [erpl-web](https://github.com/DataZooDE/erpl-web) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-08-07 06:53:27 UTC) | 29 | C++ | ERPL is a DuckDB extension to connect to API based ecosystems via standard in... |
| 98 | [eurostat](https://duckdb.org/community_extensions/extensions/eurostat.html) | [duckdb-eurostat](https://github.com/ahuarte47/duckdb-eurostat) | 🟢 Ongoing | 1 - 🔥 Very Active | 3 days ago (2026-08-03 17:06:16 UTC) | 34 | C++ | DuckDB extension for reading data from EUROSTAT database using SQL  |
| 99 | [evalexpr_rhai](https://duckdb.org/community_extensions/extensions/evalexpr_rhai.html) | [evalexpr_rhai](https://github.com/Query-farm/evalexpr_rhai) | 🟢 Ongoing | 2 - ✅ Active | 13 days ago (2026-07-25 04:26:51 UTC) | 26 | C++ | A DuckDB extension to evaluate the Rhai scripting language as part of SQL. |
| 100 | [events](https://duckdb.org/community_extensions/extensions/events.html) | [events](https://github.com/Query-farm/events) | ❓ Unknown | 2 - ✅ Active | 13 days ago (2026-07-25 04:26:52 UTC) | 3 | C++ | Capture database events and deliver JSON notifications to external programs v... |
| 101 | [faiss](https://duckdb.org/community_extensions/extensions/faiss.html) | [duckdb-faiss-ext](https://github.com/duckdb-faiss-ext/duckdb-faiss-ext) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-08-06 00:47:40 UTC) | 31 | Go | DuckDB wrapper for FAISS - Experimental |
| 102 | [fakeit](https://duckdb.org/community_extensions/extensions/fakeit.html) | [duckdb-fakeit](https://github.com/tobilg/duckdb-fakeit) | ❓ Unknown | 3 - 🟡 Stable | 40 days ago (2026-06-27 13:59:35 UTC) | 15 | Rust | DuckDB extension: fakeit by tobilg |
| 103 | [file_dialog](https://duckdb.org/community_extensions/extensions/file_dialog.html) | [duckdb-ext-file-dialog](https://github.com/yutannihilation/duckdb-ext-file-dialog) | ❓ Unknown | 2 - ✅ Active | 10 days ago (2026-07-27 11:44:02 UTC) | 15 | Rust | A DuckDB extension to choose file interactively using native file open dialogs |
| 104 | [finance](https://duckdb.org/community_extensions/extensions/finance.html) | [duckdb-finance](https://github.com/leonardovida/duckdb-finance) | ❓ Unknown | 1 - 🔥 Very Active | 6 days ago (2026-07-31 09:20:37 UTC) | 6 | C++ | SQL-native quant finance for DuckDB |
| 105 | [finetype](https://duckdb.org/community_extensions/extensions/finetype.html) | [finetype](https://github.com/meridian-online/finetype) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-08-06 06:35:13 UTC) | 2 | Rust | 👓 Precision format detection for text data. Semantic type inference with tran... |
| 106 | [fire_duck_ext](https://duckdb.org/community_extensions/extensions/fire_duck_ext.html) | [fire_duck_ext](https://github.com/BorisBesky/fire_duck_ext) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-08-07 07:02:31 UTC) | 3 | C++ | duckdb extension for firestore |
| 107 | [firebird](https://duckdb.org/community_extensions/extensions/firebird.html) | [duckdb-firebird](https://github.com/flozer/duckdb-firebird) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-08-06 09:13:26 UTC) | 4 | C++ | DuckDB extension: firebird by flozer |
| 108 | [fit](https://duckdb.org/community_extensions/extensions/fit.html) | [duckdb-fit-extension](https://github.com/antoriche/duckdb-fit-extension) | 🟢 Ongoing | 1 - 🔥 Very Active | 3 days ago (2026-08-04 01:57:08 UTC) | 3 | C++ | DuckDB extension: fit by antoriche |
| 109 | [fivetran](https://duckdb.org/community_extensions/extensions/fivetran.html) | [duckdb_sparse_variant](https://github.com/fivetran/duckdb_sparse_variant) | 🟢 Ongoing | 3 - 🟡 Stable | 79 days ago (2026-05-19 07:42:06 UTC) | 0 | C++ | A DuckDB extension providing sparse VARIANT encoding for STRUCTs and an optim... |
| 110 | [flock](https://duckdb.org/community_extensions/extensions/flock.html) | [flock](https://github.com/dais-polymtl/flock) | 🟢 Ongoing | 2 - ✅ Active | 11 days ago (2026-07-26 19:00:52 UTC) | 353 | C++ | Beyond Quacking: Deep Integration of Language Models and RAG into DuckDB (VLD... |
| 111 | [fsquery](https://duckdb.org/community_extensions/extensions/fsquery.html) | [fsquery](https://github.com/halgari/fsquery) | ❓ Unknown | 4 - 🟠 Stale | 143 days ago (2026-03-16 16:09:24 UTC) | 2 | C++ | An extension that allows DuckDB to enumerate and stat files on the disk |
| 112 | [func_apply](https://duckdb.org/community_extensions/extensions/func_apply.html) | [duckdb_func_apply](https://github.com/teaguesterling/duckdb_func_apply) | 🟢 Ongoing | 2 - ✅ Active | 12 days ago (2026-07-25 19:36:36 UTC) | 3 | C++ | An exension to allow dynamic function application |
| 113 | [fuzzycomplete](https://duckdb.org/community_extensions/extensions/fuzzycomplete.html) | [fuzzycomplete](https://github.com/Query-farm/fuzzycomplete) | 🟢 Ongoing | 2 - ✅ Active | 12 days ago (2026-07-25 14:27:13 UTC) | 29 | C++ | DuckDB Extension for fuzzy string matching based autocompletion |
| 114 | [gaggle](https://duckdb.org/community_extensions/extensions/gaggle.html) | [gaggle](https://github.com/CogitatorTech/gaggle) | 🟢 Ongoing | 2 - ✅ Active | 15 days ago (2026-07-22 14:49:44 UTC) | 17 | Rust | A DuckDB extension for working with Kaggle datasets |
| 115 | [gcs](https://duckdb.org/community_extensions/extensions/gcs.html) | [duckdb-gcs](https://github.com/northpolesec/duckdb-gcs) | 🟢 Ongoing | 2 - ✅ Active | 13 days ago (2026-07-24 18:57:51 UTC) | 28 | C++ | A GCS-native extension for DuckDB |
| 116 | [gdrive](https://duckdb.org/community_extensions/extensions/gdrive.html) | [duckdb-gdrive](https://github.com/DataZooDE/duckdb-gdrive) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-08-07 06:51:39 UTC) | 2 | C++ | Query Google Drive files directly from DuckDB via a gdrive:// filesystem |
| 117 | [gdx](https://duckdb.org/community_extensions/extensions/gdx.html) | [duckdb-gdx](https://github.com/chrispahm/duckdb-gdx) | ❓ Unknown | 2 - ✅ Active | 10 days ago (2026-07-27 09:45:36 UTC) | 1 | C++ | DuckDB extension: gdx by chrispahm |
| 118 | [geography](https://duckdb.org/community_extensions/extensions/geography.html) | [duckdb-geography](https://github.com/paleolimbot/duckdb-geography) | ❓ Unknown | 1 - 🔥 Very Active | 3 days ago (2026-08-03 14:14:08 UTC) | 46 | C++ | Geospatial data extension by paleolimbot |
| 119 | [geosilo](https://duckdb.org/community_extensions/extensions/geosilo.html) | [geosilo](https://github.com/Query-farm/geosilo) | 🟢 Ongoing | 2 - ✅ Active | 13 days ago (2026-07-25 04:26:53 UTC) | 25 | C++ | DuckDB extension for compact geometry encoding using delta-encoded coordinate... |
| 120 | [geotiff](https://duckdb.org/community_extensions/extensions/geotiff.html) | [duckdb-geotiff](https://github.com/babaknaimi/duckdb-geotiff) | ❓ Unknown | 4 - 🟠 Stale | 352 days ago (2025-08-20 05:12:15 UTC) | 2 | C++ | Duckdb extension to read GeoTiffs directly with duckdb database |
| 121 | [ggsql](https://duckdb.org/community_extensions/extensions/ggsql.html) | [ggsql-duckdb](https://github.com/posit-dev/ggsql-duckdb) | 🟢 Ongoing | 3 - 🟡 Stable | 45 days ago (2026-06-23 06:14:05 UTC) | 27 | Rust | A DuckDB extension adding support for ggsql  |
| 122 | [gh](https://duckdb.org/community_extensions/extensions/gh.html) | [duckdb-gh](https://github.com/carlopi/duckdb-gh) | 🟢 Ongoing | 4 - 🟠 Stale | 99 days ago (2026-04-29 14:21:02 UTC) | 4 | C++ | DuckDB extension: gh by carlopi |
| 123 | [gorz](https://duckdb.org/community_extensions/extensions/gorz.html) | [duckdb-gorz](https://github.com/gorfather/duckdb-gorz) | 🟢 Ongoing | 2 - ✅ Active | 23 days ago (2026-07-14 12:35:33 UTC) | 0 | C++ | DuckDB extension: read/write GORpipe .gorz / .gord genomic files as native ta... |
| 124 | [gpudb](https://duckdb.org/community_extensions/extensions/gpudb.html) | [duckdbgpumetaldbram](https://github.com/singhpratech/duckdbgpumetaldbram) | 🟢 Ongoing | 1 - 🔥 Very Active | 3 days ago (2026-08-03 12:51:20 UTC) | 12 | C++ | GPU-accelerated DuckDB extension on NVIDIA CUDA + Apple Silicon Metal — first... |
| 125 | [gsheets](https://duckdb.org/community_extensions/extensions/gsheets.html) | [duckdb_gsheets](https://github.com/evidence-dev/duckdb_gsheets) | 🟢 Ongoing | 4 - 🟠 Stale | 167 days ago (2026-02-21 04:11:04 UTC) | 348 | C++ | DuckDB extension to read and write Google Sheets using SQL |
| 126 | [h3](https://duckdb.org/community_extensions/extensions/h3.html) | [h3-duckdb](https://github.com/isaacbrodsky/h3-duckdb) | 🟢 Ongoing | 2 - ✅ Active | 15 days ago (2026-07-22 18:16:17 UTC) | 250 | C | Bindings for H3 to DuckDB |
| 127 | [h5db](https://duckdb.org/community_extensions/extensions/h5db.html) | [h5db](https://github.com/jokasimr/h5db) | 🟢 Ongoing | 2 - ✅ Active | 15 days ago (2026-07-22 16:21:57 UTC) | 3 | C++ | Duckdb extension for reading HDF5 files. |
| 128 | [harbor](https://duckdb.org/community_extensions/extensions/harbor.html) | [duckdb-harbor](https://github.com/shreeve/duckdb-harbor) | 🟢 Ongoing | 2 - ✅ Active | 19 days ago (2026-07-18 10:03:55 UTC) | 1 | C++ | HTTP server for DuckDB UI, JSON /sql, and CLI |
| 129 | [hashfuncs](https://duckdb.org/community_extensions/extensions/hashfuncs.html) | [hashfuncs](https://github.com/Query-farm/hashfuncs) | 🟢 Ongoing | 2 - ✅ Active | 13 days ago (2026-07-25 04:26:54 UTC) | 13 | C++ | A DuckDB extension that supplies non-cryptographic hash functions. |
| 130 | [hdf5](https://duckdb.org/community_extensions/extensions/hdf5.html) | [duckdb-hdf5](https://github.com/Berrysoft/duckdb-hdf5) | ❓ Unknown | 4 - 🟠 Stale | 106 days ago (2026-04-23 01:30:36 UTC) | 12 | Rust | HDF5 plugin for duckdb |
| 131 | [hdfs](https://duckdb.org/community_extensions/extensions/hdfs.html) | [duckdb-hdfs](https://github.com/casperhart/duckdb-hdfs) | ❓ Unknown | 2 - ✅ Active | 17 days ago (2026-07-21 01:26:22 UTC) | 0 | Rust | DuckDB extension: hdfs by casperhart |
| 132 | [hedged_request_fs](https://duckdb.org/community_extensions/extensions/hedged_request_fs.html) | [duckdb-hedged-request](https://github.com/dentiny/duckdb-hedged-request) | 🟢 Ongoing | 2 - ✅ Active | 12 days ago (2026-07-25 19:38:35 UTC) | 1 | C++ | DuckDB extension: hedged_request_fs by dentiny |
| 133 | [hex9](https://duckdb.org/community_extensions/extensions/hex9.html) | [duckdb-hex9](https://github.com/MrBenGriffin/duckdb-hex9) | 🟢 Ongoing | 2 - ✅ Active | 9 days ago (2026-07-28 09:59:07 UTC) | 0 | C++ | duckdb community wrapper for libhex9 |
| 134 | [highs](https://duckdb.org/community_extensions/extensions/highs.html) | [HiGHS-duckdb](https://github.com/fhk/HiGHS-duckdb) | ❓ Unknown | 4 - 🟠 Stale | 163 days ago (2026-02-25 02:07:48 UTC) | 1 | C++ | Run the solver in the database! |
| 135 | [hive_metastore](https://duckdb.org/community_extensions/extensions/hive_metastore.html) | [duckdb-hive-metastore](https://github.com/ilum-cloud/duckdb-hive-metastore) | 🟢 Ongoing | 3 - 🟡 Stable | 76 days ago (2026-05-22 17:49:59 UTC) | 4 | C++ | DuckDB extension allowing to connect to Apache Hive Metastore and query the d... |
| 136 | [hnsw_acorn](https://duckdb.org/community_extensions/extensions/hnsw_acorn.html) | [duckdb-hnsw-acorn](https://github.com/cigrainger/duckdb-hnsw-acorn) | ❓ Unknown | 4 - 🟠 Stale | 131 days ago (2026-03-28 07:49:47 UTC) | 64 | C++ | ACORN-1 pre-filtered HNSW search for DuckDB |
| 137 | [holtfs](https://duckdb.org/community_extensions/extensions/holtfs.html) | [duckdb-holtfs](https://github.com/feichai0017/duckdb-holtfs) | 🟢 Ongoing | 3 - 🟡 Stable | 72 days ago (2026-05-27 06:55:19 UTC) | 0 | C++ | DuckDB extension for planning scans through Holt-backed metadata indexes |
| 138 | [hostfs](https://duckdb.org/community_extensions/extensions/hostfs.html) | [hostFS](https://github.com/gropaul/hostFS) | ❓ Unknown | 4 - 🟠 Stale | 309 days ago (2025-10-01 21:02:13 UTC) | 31 | C++ | DuckDB extension: hostfs by gropaul |
| 139 | [html_query](https://duckdb.org/community_extensions/extensions/html_query.html) | [duckdb_html_query](https://github.com/midwork-finds-jobs/duckdb_html_query) | ❓ Unknown | 4 - 🟠 Stale | 182 days ago (2026-02-05 15:33:13 UTC) | 2 | Rust | Filter HTML inside duckdb |
| 140 | [html_readability](https://duckdb.org/community_extensions/extensions/html_readability.html) | [duckdb-html-readability](https://github.com/midwork-finds-jobs/duckdb-html-readability) | ❓ Unknown | 4 - 🟠 Stale | 182 days ago (2026-02-05 15:33:16 UTC) | 0 | Rust | DuckDB extension to parse html to readable text |
| 141 | [http_client](https://duckdb.org/community_extensions/extensions/http_client.html) | [httpclient](https://github.com/Query-farm/httpclient) | 🟢 Ongoing | 2 - ✅ Active | 11 days ago (2026-07-26 22:19:20 UTC) | 80 | C++ | DuckDB HTTP GET/POST Client in a Community Extension |
| 142 | [http_request](https://duckdb.org/community_extensions/extensions/http_request.html) | [duckdb_http_request](https://github.com/midwork-finds-jobs/duckdb_http_request) | ❓ Unknown | 4 - 🟠 Stale | 170 days ago (2026-02-17 13:03:03 UTC) | 4 | C++ | Uses the native duckdb httputil to make extra requests in SELECT |
| 143 | [http_stats](https://duckdb.org/community_extensions/extensions/http_stats.html) | [duckdb-http-stats](https://github.com/tlinhart/duckdb-http-stats) | ❓ Unknown | 4 - 🟠 Stale | 132 days ago (2026-03-27 13:58:03 UTC) | 1 | C++ | Better HTTP statistics for DuckDB |
| 144 | [httpd_log](https://duckdb.org/community_extensions/extensions/httpd_log.html) | [duckdb-httpd-log](https://github.com/saygox/duckdb-httpd-log) | ❓ Unknown | 4 - 🟠 Stale | 207 days ago (2026-01-12 06:14:58 UTC) | 0 | C++ | duckdb extension |
| 145 | [httpfs_timeout_retry](https://duckdb.org/community_extensions/extensions/httpfs_timeout_retry.html) | [duckdb-httpfs-timeout-retry](https://github.com/dentiny/duckdb-httpfs-timeout-retry) | 🟢 Ongoing | 2 - ✅ Active | 12 days ago (2026-07-25 21:48:10 UTC) | 0 | C++ | Web/HTTP functionality extension by dentiny |
| 146 | [httpserver](https://duckdb.org/community_extensions/extensions/httpserver.html) | [httpserver](https://github.com/Query-farm/httpserver) | 🟢 Ongoing | 2 - ✅ Active | 11 days ago (2026-07-26 22:19:21 UTC) | 284 | C++ | DuckDB HTTP API Server and Query Interface in a  Community Extension |
| 147 | [infera](https://duckdb.org/community_extensions/extensions/infera.html) | [infera](https://github.com/CogitatorTech/infera) | 🟢 Ongoing | 2 - ✅ Active | 15 days ago (2026-07-22 14:50:26 UTC) | 134 | Rust | A DuckDB extension for in-database inference |
| 148 | [inflector](https://duckdb.org/community_extensions/extensions/inflector.html) | [inflector](https://github.com/Query-farm/inflector) | 🟢 Ongoing | 2 - ✅ Active | 13 days ago (2026-07-25 04:26:57 UTC) | 9 | C++ | Powerful string case transformation and inflection capabilities directly to y... |
| 149 | [ion](https://duckdb.org/community_extensions/extensions/ion.html) | [duckdb-ion](https://github.com/kestra-io/duckdb-ion) | 🟢 Ongoing | 4 - 🟠 Stale | 149 days ago (2026-03-10 15:49:39 UTC) | 4 | C++ | AWS Ion extension for DuckDB |
| 150 | [json_schema](https://duckdb.org/community_extensions/extensions/json_schema.html) | [json_schema](https://github.com/Query-farm/json_schema) | 🟢 Ongoing | 2 - ✅ Active | 13 days ago (2026-07-25 04:26:58 UTC) | 4 | C++ | A DuckDB extension that bring support for validating JSON data using JSON sch... |
| 151 | [jsonata](https://duckdb.org/community_extensions/extensions/jsonata.html) | [jsonata](https://github.com/Query-farm/jsonata) | 🟢 Ongoing | 2 - ✅ Active | 13 days ago (2026-07-25 04:26:59 UTC) | 7 | C++ | The JSONata extension for DuckDB enables expressive, JSON-focused querying an... |
| 152 | [jwt](https://duckdb.org/community_extensions/extensions/jwt.html) | [duckdb_jwt](https://github.com/GalvinGao/duckdb_jwt) | ❓ Unknown | 4 - 🟠 Stale | over a year ago (2025-07-09 00:13:56 UTC) | 0 | C++ | DuckDB extension: jwt by GalvinGao |
| 153 | [keboola](https://duckdb.org/community_extensions/extensions/keboola.html) | [duckdb-extension](https://github.com/keboola/duckdb-extension) | 🟢 Ongoing | 2 - ✅ Active | 29 days ago (2026-07-08 11:43:04 UTC) | 0 | C++ | DuckDB extension for Keboola Storage — query and write Keboola tables using s... |
| 154 | [lastra](https://duckdb.org/community_extensions/extensions/lastra.html) | [duckdb-lastra](https://github.com/QTSurfer/duckdb-lastra) | ❓ Unknown | 3 - 🟡 Stable | 87 days ago (2026-05-11 12:15:36 UTC) | 0 | C++ | DuckDB extension for reading Lastra columnar time series files natively |
| 155 | [latency_injection_fs](https://duckdb.org/community_extensions/extensions/latency_injection_fs.html) | [duckdb-filesystem-latency-injection](https://github.com/dentiny/duckdb-filesystem-latency-injection) | 🟢 Ongoing | 2 - ✅ Active | 12 days ago (2026-07-25 19:33:32 UTC) | 0 | C++ | DuckDB extension: latency_injection_fs by dentiny |
| 156 | [laterite_ags4](https://duckdb.org/community_extensions/extensions/laterite_ags4.html) | [laterite-duckdb](https://github.com/niko86/laterite-duckdb) | 🟢 Ongoing | 1 - 🔥 Very Active | 4 days ago (2026-08-03 01:04:23 UTC) | 0 | Rust | DuckDB extension: laterite_ags4 by niko86 |
| 157 | [ldbc_data_gen](https://duckdb.org/community_extensions/extensions/ldbc_data_gen.html) | [ldbc-data-gen](https://github.com/Dtenwolde/ldbc-data-gen) | 🟢 Ongoing | 1 - 🔥 Very Active | 2 days ago (2026-08-04 11:07:46 UTC) | 0 | C++ | Database connectivity extension by Dtenwolde |
| 158 | [level_pivot](https://duckdb.org/community_extensions/extensions/level_pivot.html) | [duckdb-level-pivot](https://github.com/halgari/duckdb-level-pivot) | 🟢 Ongoing | 4 - 🟠 Stale | 105 days ago (2026-04-23 16:05:04 UTC) | 0 | C++ | DuckDB extension: level_pivot by halgari |
| 159 | [lindel](https://duckdb.org/community_extensions/extensions/lindel.html) | [lindel](https://github.com/Query-farm/lindel) | 🟢 Ongoing | 2 - ✅ Active | 13 days ago (2026-07-25 04:27:01 UTC) | 66 | C++ | DuckDB Extension Linearization/Delinearization, Z-Order, Hilbert and Morton C... |
| 160 | [llm](https://duckdb.org/community_extensions/extensions/llm.html) | [duckdb-llm](https://github.com/midwork-finds-jobs/duckdb-llm) | 🟢 Ongoing | 4 - 🟠 Stale | 170 days ago (2026-02-17 14:09:08 UTC) | 3 | C++ | DuckDB extension: llm by midwork-finds-jobs |
| 161 | [loki](https://duckdb.org/community_extensions/extensions/loki.html) | [duckdb-loki](https://github.com/prochac/duckdb-loki) | ❓ Unknown | 1 - 🔥 Very Active | 5 days ago (2026-08-01 13:39:52 UTC) | 0 | C++ | DuckDB extension: loki by prochac |
| 162 | [lpts](https://duckdb.org/community_extensions/extensions/lpts.html) | [lpts](https://github.com/cwida/lpts) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-08-06 10:40:19 UTC) | 8 | C++ | Logical Plan To SQL DuckDB Extension |
| 163 | [lsh](https://duckdb.org/community_extensions/extensions/lsh.html) | [lsh](https://github.com/princeton-ddss/lsh) | ❓ Unknown | 4 - 🟠 Stale | 112 days ago (2026-04-16 17:00:45 UTC) | 14 | Rust | DuckDB community extension for locality-sensitive hashing (LSH) |
| 164 | [lttb](https://duckdb.org/community_extensions/extensions/lttb.html) | [duckdb-lttb](https://github.com/reformovo/duckdb-lttb) | ❓ Unknown | 3 - 🟡 Stable | 36 days ago (2026-07-01 07:47:53 UTC) | 2 | C++ | A simple lttb algorithm extension for DuckDB |
| 165 | [lua](https://duckdb.org/community_extensions/extensions/lua.html) | [duckdb-lua](https://github.com/isaacbrodsky/duckdb-lua) | 🟢 Ongoing | 2 - ✅ Active | 15 days ago (2026-07-22 23:18:11 UTC) | 12 | C++ | DuckDB extension to evaluate Lua expressions. |
| 166 | [luajit](https://duckdb.org/community_extensions/extensions/luajit.html) | [duckdb-luajit](https://github.com/alitrack/duckdb-luajit) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-08-07 01:33:54 UTC) | 2 | C | DuckDB extension for in-process JIT-compiled Lua UDFs via LuaJIT — self-conta... |
| 167 | [magic](https://duckdb.org/community_extensions/extensions/magic.html) | [duckdb-magic](https://github.com/carlopi/duckdb-magic) | ❓ Unknown | 3 - 🟡 Stable | 45 days ago (2026-06-22 07:17:42 UTC) | 8 | C++ | Auto-detect file types via `libmagic` (`file` utility) |
| 168 | [marisa](https://duckdb.org/community_extensions/extensions/marisa.html) | [marisa](https://github.com/Query-farm/marisa) | 🟢 Ongoing | 2 - ✅ Active | 13 days ago (2026-07-25 04:27:03 UTC) | 14 | C++ | The Marisa extension by Query.Farm integrates the fast, space-efficient MARIS... |
| 169 | [markdown](https://duckdb.org/community_extensions/extensions/markdown.html) | [duckdb_markdown](https://github.com/teaguesterling/duckdb_markdown) | 🟢 Ongoing | 2 - ✅ Active | 11 days ago (2026-07-26 20:44:09 UTC) | 28 | C++ | Heirarchical markdown parsing for DuckDB |
| 170 | [maxmind](https://duckdb.org/community_extensions/extensions/maxmind.html) | [duckdb-maxmind](https://github.com/marselester/duckdb-maxmind) | 🟢 Ongoing | 3 - 🟡 Stable | 38 days ago (2026-06-29 21:07:08 UTC) | 7 | Zig | DuckDB MaxMind extension written in Zig. |
| 171 | [miint](https://duckdb.org/community_extensions/extensions/miint.html) | [duckdb-miint](https://github.com/the-miint/duckdb-miint) | 🟢 Ongoing | 1 - 🔥 Very Active | 5 days ago (2026-08-01 16:16:33 UTC) | 6 | C++ | DuckDB extension: miint by the-miint |
| 172 | [minijinja](https://duckdb.org/community_extensions/extensions/minijinja.html) | [minijinja](https://github.com/Query-farm/minijinja) | 🟢 Ongoing | 2 - ✅ Active | 13 days ago (2026-07-25 04:27:04 UTC) | 6 | C++ | DuckDB extension: minijinja |
| 173 | [miniplot](https://duckdb.org/community_extensions/extensions/miniplot.html) | [miniplot](https://github.com/nkwork9999/miniplot) | 🟢 Ongoing | 4 - 🟠 Stale | 265 days ago (2025-11-15 02:42:43 UTC) | 23 | C++ | DuckDB extension: miniplot by nkwork9999 |
| 174 | [ml](https://github.com/alitrack/duckdb-ml) | [duckdb-ml](https://github.com/alitrack/duckdb-ml) | ❓ Unknown | 1 - 🔥 Very Active | 6 days ago (2026-07-31 09:31:53 UTC) | 5 | Rust | DuckDB extension: ml by alitrack |
| 175 | [mlpack](https://duckdb.org/community_extensions/extensions/mlpack.html) | [duckdb-mlpack](https://github.com/eddelbuettel/duckdb-mlpack) | 🟢 Ongoing | 1 - 🔥 Very Active | 7 days ago (2026-07-30 15:15:13 UTC) | 20 | C++ | Bringing mlpack to duckdb |
| 176 | [monetary](https://duckdb.org/community_extensions/extensions/monetary.html) | [monetary](https://github.com/fyffee/monetary) | ❓ Unknown | 4 - 🟠 Stale | 189 days ago (2026-01-29 11:29:01 UTC) | 0 | C++ | DuckDB extension: monetary by fyffee |
| 177 | [mongo](https://duckdb.org/community_extensions/extensions/mongo.html) | [duckdb-mongo](https://github.com/stephaniewang526/duckdb-mongo) | ❓ Unknown | 1 - 🔥 Very Active | today (2026-08-06 18:22:48 UTC) | 57 | C++ | Integrates DuckDB with MongoDB, enabling direct SQL queries over MongoDB coll... |
| 178 | [mooncake](https://duckdb.org/community_extensions/extensions/mooncake.html) | [duckdb_mooncake](https://github.com/Mooncake-Labs/duckdb_mooncake) | ❓ Unknown | 4 - 🟠 Stale | 284 days ago (2025-10-26 07:13:05 UTC) | 10 | C++ | Read Iceberg tables written by moonlink in real time |
| 179 | [motorsport_telemetry](https://duckdb.org/community_extensions/extensions/motorsport_telemetry.html) | [duckdb_motorsport_telemetry](https://github.com/tobi/duckdb_motorsport_telemetry) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-08-07 01:05:42 UTC) | 7 | Rust | Fast DuckDB extension and Rust parsers for Cosworth PDS, MoTeC LD, and VBOX V... |
| 180 | [mpduck](https://duckdb.org/community_extensions/extensions/mpduck.html) | [mpduck](https://github.com/MatthewMooreZA/mpduck) | ❓ Unknown | 4 - 🟠 Stale | 115 days ago (2026-04-13 17:59:29 UTC) | 1 | C++ | DuckDB extension to read and write Prophet model point files. |
| 181 | [msolap](https://duckdb.org/community_extensions/extensions/msolap.html) | [duckdb-msolap-extension](https://github.com/Hugoberry/duckdb-msolap-extension) | ❓ Unknown | 4 - 🟠 Stale | 316 days ago (2025-09-24 16:33:46 UTC) | 14 | C++ | DuckDB extension: msolap by Hugoberry |
| 182 | [mssql](https://duckdb.org/community_extensions/extensions/mssql.html) | [mssql-extension](https://github.com/hugr-lab/mssql-extension) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-08-07 07:00:22 UTC) | 123 | C++ | DuckDB extension for Microsoft SQL Server (TDS + TLS), with catalog integrati... |
| 183 | [nanoarrow](https://duckdb.org/community_extensions/extensions/nanoarrow.html) | [duckdb-nanoarrow](https://github.com/paleolimbot/duckdb-nanoarrow) | ❓ Unknown | 2 - ✅ Active | 8 days ago (2026-07-29 15:49:02 UTC) | 75 | C++ | DuckDB extension: nanoarrow by paleolimbot |
| 184 | [nanodbc](https://duckdb.org/community_extensions/extensions/nanodbc.html) | [duckdb-nanodbc-extension](https://github.com/Hugoberry/duckdb-nanodbc-extension) | ❓ Unknown | 4 - 🟠 Stale | 97 days ago (2026-05-01 13:18:55 UTC) | 52 | C++ | Database connectivity extension by Hugoberry |
| 185 | [nats_js](https://duckdb.org/community_extensions/extensions/nats_js.html) | [duckdb-nats-jetstream](https://github.com/brannn/duckdb-nats-jetstream) | ❓ Unknown | 4 - 🟠 Stale | 130 days ago (2026-03-30 05:12:16 UTC) | 21 | C++ | DuckDB extension for querying NATS JetStream message streams with SQL |
| 186 | [netquack](https://duckdb.org/community_extensions/extensions/netquack.html) | [duckdb-netquack](https://github.com/hatamiarash7/duckdb-netquack) | ❓ Unknown | 2 - ✅ Active | 13 days ago (2026-07-25 07:00:30 UTC) | 42 | C++ | DuckDB extension for parsing, extracting, and analyzing domains, URIs, and pa... |
| 187 | [nsv](https://duckdb.org/community_extensions/extensions/nsv.html) | [nsv-duckdb](https://github.com/nsv-format/nsv-duckdb) | 🟢 Ongoing | 3 - 🟡 Stable | 60 days ago (2026-06-07 19:12:56 UTC) | 0 | Rust | A DuckDB extension for NSV processing |
| 188 | [oast](https://duckdb.org/community_extensions/extensions/oast.html) | [duckdb-oast](https://github.com/hrbrmstr/duckdb-oast) | 🟢 Ongoing | 4 - 🟠 Stale | 177 days ago (2026-02-10 12:00:32 UTC) | 4 | C | A DuckDB extension for validating, decoding, and extracting OAST (Out-of-Band... |
| 189 | [observefs](https://duckdb.org/community_extensions/extensions/observefs.html) | [duckdb-filesystem-observability](https://github.com/dentiny/duckdb-filesystem-observability) | 🟢 Ongoing | 2 - ✅ Active | 12 days ago (2026-07-25 19:13:57 UTC) | 16 | C++ | Provides observability for duckdb filesystem. |
| 190 | [ofquack](https://duckdb.org/community_extensions/extensions/ofquack.html) | [ofquack](https://github.com/krokozyab/ofquack) | ❓ Unknown | 4 - 🟠 Stale | over a year ago (2025-04-22 12:24:17 UTC) | 6 | C++ | Oracle Fusion DuckDB extension  |
| 191 | [onager](https://duckdb.org/community_extensions/extensions/onager.html) | [onager](https://github.com/CogitatorTech/onager) | 🟢 Ongoing | 1 - 🔥 Very Active | 7 days ago (2026-07-30 17:34:19 UTC) | 148 | Rust | A DuckDB extension for graph data analytics |
| 192 | [onelake](https://duckdb.org/community_extensions/extensions/onelake.html) | [duckdb_onelake](https://github.com/datumnova/duckdb_onelake) | ❓ Unknown | 4 - 🟠 Stale | 248 days ago (2025-12-01 10:28:22 UTC) | 19 | C++ | DuckDB extension: onelake by datumnova |
| 193 | [open_prompt](https://duckdb.org/community_extensions/extensions/open_prompt.html) | [openprompt](https://github.com/Query-farm/openprompt) | 🟢 Ongoing | 2 - ✅ Active | 11 days ago (2026-07-26 22:19:22 UTC) | 61 | C++ | DuckDB Community Extension to prompt LLMs from SQL |
| 194 | [opendal](https://duckdb.org/community_extensions/extensions/opendal.html) | [duckdb-opendal](https://github.com/chitralverma/duckdb-opendal) | 🟢 Ongoing | 2 - ✅ Active | 8 days ago (2026-07-30 06:07:47 UTC) | 0 | Rust | extension to bring together duckdb and opendal |
| 195 | [orc](https://duckdb.org/community_extensions/extensions/orc.html) | [duckdb_orc](https://github.com/alitrack/duckdb_orc) | 🟢 Ongoing | 2 - ✅ Active | 23 days ago (2026-07-15 01:20:53 UTC) | 4 | Rust | A DuckDB extension for reading Apache ORC files, written in pure Rust. |
| 196 | [osmium](https://duckdb.org/community_extensions/extensions/osmium.html) | [duckdb-osmium](https://github.com/jake-low/duckdb-osmium) | 🟢 Ongoing | 2 - ✅ Active | 13 days ago (2026-07-24 19:44:27 UTC) | 26 | C++ | DuckDB extension for reading OpenStreetMap PBF files using libosmium |
| 197 | [otlp](https://duckdb.org/community_extensions/extensions/otlp.html) | [duckdb-otlp](https://github.com/smithclay/duckdb-otlp) | 🟢 Ongoing | 1 - 🔥 Very Active | 3 days ago (2026-08-03 13:38:24 UTC) | 77 | Python | stream, store, and query OpenTelemetry metrics, logs, and traces (OTLP) in du... |
| 198 | [overture](https://duckdb.org/community_extensions/extensions/overture.html) | [duckdb-overture](https://github.com/cubilica/duckdb-overture) | ❓ Unknown | 4 - 🟠 Stale | 114 days ago (2026-04-14 16:46:56 UTC) | 4 | C++ | DuckDB extension: overture by cubilica |
| 199 | [pac](https://duckdb.org/community_extensions/extensions/pac.html) | [privacy](https://github.com/cwida/privacy) | 🟢 Ongoing | 2 - ✅ Active | 15 days ago (2026-07-22 12:26:16 UTC) | 19 | C++ | Automatic query privatization in DuckDB |
| 200 | [paimon](https://duckdb.org/community_extensions/extensions/paimon.html) | [duckdb-paimon](https://github.com/polardb/duckdb-paimon) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-08-07 02:37:56 UTC) | 41 | C++ | DuckDB extension for accessing Apache Paimon. 🦆 |
| 201 | [parser_tools](https://duckdb.org/community_extensions/extensions/parser_tools.html) | [duckdb_extension_parser_tools](https://github.com/hotdata-dev/duckdb_extension_parser_tools) | 🟢 Ongoing | 2 - ✅ Active | 17 days ago (2026-07-20 22:07:52 UTC) | 27 | C++ | Parse sql - with sql! |
| 202 | [pbi_scanner](https://duckdb.org/community_extensions/extensions/pbi_scanner.html) | [pbi_scanner](https://github.com/crazy-treyn/pbi_scanner) | 🟢 Ongoing | 3 - 🟡 Stable | 50 days ago (2026-06-17 19:07:44 UTC) | 15 | C++ | DuckDB extension that enables querying Power BI Semantic Models with DAX. |
| 203 | [pbix](https://duckdb.org/community_extensions/extensions/pbix.html) | [duckdb-pbix-extension](https://github.com/Hugoberry/duckdb-pbix-extension) | 🟢 Ongoing | 4 - 🟠 Stale | 286 days ago (2025-10-24 13:47:34 UTC) | 38 | C++ | Duckdb extension for parsing the metadata and contents of the embedded data m... |
| 204 | [pcap_duckdb](https://duckdb.org/community_extensions/extensions/pcap_duckdb.html) | [pcap_duckdb](https://github.com/siara-in/pcap_duckdb) | ❓ Unknown | 3 - 🟡 Stable | 64 days ago (2026-06-04 05:10:33 UTC) | 1 | C++ | Database connectivity extension by siara-in |
| 205 | [pcap_reader](https://duckdb.org/community_extensions/extensions/pcap_reader.html) | [pcap](https://github.com/Query-farm/pcap) | ❓ Unknown | 3 - 🟡 Stable | 80 days ago (2026-05-18 22:26:34 UTC) | 13 | Rust | DuckDB PCAP Reader Extension made in Rust |
| 206 | [pdal](https://duckdb.org/community_extensions/extensions/pdal.html) | [duckdb-pdal](https://github.com/ahuarte47/duckdb-pdal) | 🟢 Ongoing | 1 - 🔥 Very Active | 3 days ago (2026-08-03 10:00:30 UTC) | 27 | C++ | DuckDB extension for manipulating point cloud data using SQL |
| 207 | [pdf](https://duckdb.org/community_extensions/extensions/pdf.html) | [duckdb-pdf](https://github.com/asubbarao/duckdb-pdf) | 🟢 Ongoing | 2 - ✅ Active | 8 days ago (2026-07-29 23:43:07 UTC) | 3 | C++ | Read and extract content from PDF files in DuckDB — Poppler (text/words/lines... |
| 208 | [petgraph_ext](https://duckdb.org/community_extensions/extensions/petgraph_ext.html) | [duckdb_petgraph](https://github.com/alitrack/duckdb_petgraph) | 🟢 Ongoing | 2 - ✅ Active | 8 days ago (2026-07-29 23:37:31 UTC) | 4 | Rust | DuckDB extension: petgraph_ext by alitrack |
| 209 | [pfc](https://duckdb.org/community_extensions/extensions/pfc.html) | [pfc-duckdb](https://github.com/ImpossibleForge/pfc-duckdb) | 🟢 Ongoing | 3 - 🟡 Stable | 79 days ago (2026-05-19 17:32:55 UTC) | 1 | C++ | DuckDB extension to read PFC-JSONL compressed log files with block-level time... |
| 210 | [pic2vec](https://duckdb.org/community_extensions/extensions/pic2vec.html) | [pic2vec](https://github.com/nkwork9999/pic2vec) | 🟢 Ongoing | 3 - 🟡 Stable | 55 days ago (2026-06-12 16:13:03 UTC) | 0 | C++ | DuckDB extension: pic2vec by nkwork9999 |
| 211 | [pivot_table](https://duckdb.org/community_extensions/extensions/pivot_table.html) | [pivot_table](https://github.com/Alex-Monahan/pivot_table) | ❓ Unknown | 4 - 🟠 Stale | 111 days ago (2026-04-17 15:20:58 UTC) | 20 | C++ | Full spreadsheet-style pivot table through SQL macros. Just specify values, r... |
| 212 | [plinking_duck](https://duckdb.org/community_extensions/extensions/plinking_duck.html) | [plinking_duck](https://github.com/teaguesterling/plinking_duck) | 🟢 Ongoing | 1 - 🔥 Very Active | 7 days ago (2026-07-30 23:32:01 UTC) | 4 | C++ | DuckDB tools for Plink2  |
| 213 | [poached](https://duckdb.org/community_extensions/extensions/poached.html) | [poached](https://github.com/sidequery/poached) | ❓ Unknown | 4 - 🟠 Stale | 223 days ago (2025-12-26 21:13:19 UTC) | 11 | C++ | A DuckDB extension that exposes SQL parsing functionality for building IDEs,... |
| 214 | [polyglot](https://duckdb.org/community_extensions/extensions/polyglot.html) | [duckdb-polyglot](https://github.com/tobilg/duckdb-polyglot) | ❓ Unknown | 3 - 🟡 Stable | 62 days ago (2026-06-05 21:14:53 UTC) | 24 | Rust | Use other SQL dialects in DuckDB  |
| 215 | [prometheus](https://duckdb.org/community_extensions/extensions/prometheus.html) | [duckdb-prometheus](https://github.com/botan/duckdb-prometheus) | 🟢 Ongoing | 2 - ✅ Active | 15 days ago (2026-07-22 15:04:54 UTC) | 4 | Rust | Query Prometheus-compatible HTTP APIs directly from DuckDB |
| 216 | [protoduck](https://duckdb.org/community_extensions/extensions/protoduck.html) | [protoduck](https://github.com/fcsnk/protoduck) | ❓ Unknown | 2 - ✅ Active | 21 days ago (2026-07-17 06:47:06 UTC) | 1 | Rust | DuckDB extension: protoduck by fcsnk |
| 217 | [prql](https://duckdb.org/community_extensions/extensions/prql.html) | [duckdb-prql](https://github.com/ywelsch/duckdb-prql) | 🟢 Ongoing | 3 - 🟡 Stable | 70 days ago (2026-05-28 11:18:16 UTC) | 327 | C++ | PRQL as a DuckDB extension |
| 218 | [psql](https://duckdb.org/community_extensions/extensions/psql.html) | [duckdb-psql](https://github.com/ywelsch/duckdb-psql) | 🟢 Ongoing | 4 - 🟠 Stale | 114 days ago (2026-04-14 18:55:40 UTC) | 107 | C++ | A piped SQL for DuckDB |
| 219 | [pst](https://duckdb.org/community_extensions/extensions/pst.html) | [duckdb-pst](https://github.com/intellekthq/duckdb-pst) | 🟢 Ongoing | 1 - 🔥 Very Active | 3 days ago (2026-08-03 16:43:10 UTC) | 10 | C++ | In-place querying of Microsoft PST files, directly from storage, with SQL. |
| 220 | [psyduck](https://duckdb.org/community_extensions/extensions/psyduck.html) | [psyduck](https://github.com/Ian-Fogelman/psyduck) | 🟢 Ongoing | 4 - 🟠 Stale | 235 days ago (2025-12-14 15:10:39 UTC) | 7 | C++ | Pysduck a DuckDB community extension about Pokémon. |
| 221 | [pyroscope](https://duckdb.org/community_extensions/extensions/pyroscope.html) | [pyroscope](https://github.com/Query-farm/pyroscope) | ❓ Unknown | 4 - 🟠 Stale | 169 days ago (2026-02-18 19:49:53 UTC) | 21 | Rust | DuckDB Pyroscope Extension for Continuous Profiling |
| 222 | [python_udf](https://duckdb.org/community_extensions/extensions/python_udf.html) | [duckdb-python](https://github.com/alitrack/duckdb-python) | 🟢 Ongoing | 1 - 🔥 Very Active | 6 days ago (2026-07-31 08:04:02 UTC) | 5 | Rust | DuckDB extension: embed Python inside DuckDB for SQL-native Python UDFs (scal... |
| 223 | [quack_oauth](https://duckdb.org/community_extensions/extensions/quack_oauth.html) | [quack-oauth](https://github.com/DataZooDE/quack-oauth) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-08-07 06:51:33 UTC) | 22 | C++ | Extensions providing OAuth and OpenID primitives for authentication and autho... |
| 224 | [quackapi](https://duckdb.org/community_extensions/extensions/quackapi.html) | [quackapi](https://github.com/asubbarao/quackapi) | 🟢 Ongoing | 2 - ✅ Active | 8 days ago (2026-07-30 06:45:33 UTC) | 2 | C++ | FastAPI-class web framework inside DuckDB — CREATE ROUTE turns SQL into typed... |
| 225 | [quackfix](https://duckdb.org/community_extensions/extensions/quackfix.html) | [QuackFIX](https://github.com/hyehudai/QuackFIX) | ❓ Unknown | 4 - 🟠 Stale | 224 days ago (2025-12-25 10:36:24 UTC) | 16 | C++ | Fix log extension for duckdb |
| 226 | [quackformers](https://duckdb.org/community_extensions/extensions/quackformers.html) | [quackformers](https://github.com/martin-conur/quackformers) | ❓ Unknown | 2 - ✅ Active | 9 days ago (2026-07-28 20:31:37 UTC) | 13 | Rust | DuckDB NLP extension. |
| 227 | [quackiso](https://duckdb.org/community_extensions/extensions/quackiso.html) | [quackiso](https://github.com/tempoloss/quackiso) | 🟢 Ongoing | 1 - 🔥 Very Active | 3 days ago (2026-08-03 11:50:31 UTC) | 1 | Rust | Query ISO 20022 (camt/pacs/pain) financial messages as SQL in DuckDB |
| 228 | [quackscale](https://duckdb.org/community_extensions/extensions/quackscale.html) | [quackscale](https://github.com/Query-farm/quackscale) | 🟢 Ongoing | 1 - 🔥 Very Active | 6 days ago (2026-07-31 17:20:33 UTC) | 22 | Shell | DuckDB WireGuard Extension with Quack & Ducklake over Tailscale, Headscale & Co |
| 229 | [quackstats](https://duckdb.org/community_extensions/extensions/quackstats.html) | [quackstats](https://github.com/jasadams/quackstats) | ❓ Unknown | 4 - 🟠 Stale | 186 days ago (2026-02-01 12:01:35 UTC) | 3 | Rust | DuckDB extension for time series forecasting and seasonality detection |
| 230 | [quackstore](https://duckdb.org/community_extensions/extensions/quackstore.html) | [QuackStore](https://github.com/coginiti-dev/QuackStore) | 🟢 Ongoing | 4 - 🟠 Stale | 93 days ago (2026-05-05 13:29:19 UTC) | 117 | C++ | DuckDB extension: quackstore by coginiti-dev |
| 231 | [query_condition_cache](https://duckdb.org/community_extensions/extensions/query_condition_cache.html) | [duckdb-query-condition-cache](https://github.com/dentiny/duckdb-query-condition-cache) | 🟢 Ongoing | 2 - ✅ Active | 12 days ago (2026-07-25 22:03:25 UTC) | 15 | C++ | DuckDB extension: query_condition_cache by dentiny |
| 232 | [query_limiter](https://duckdb.org/community_extensions/extensions/query_limiter.html) | [duckdb-query-limiter](https://github.com/dentiny/duckdb-query-limiter) | 🟢 Ongoing | 2 - ✅ Active | 12 days ago (2026-07-25 19:10:55 UTC) | 0 | C++ | DuckDB extension: query_limiter by dentiny |
| 233 | [quickjs](https://duckdb.org/community_extensions/extensions/quickjs.html) | [quickjs](https://github.com/Query-farm/quickjs) | 🟢 Ongoing | 2 - ✅ Active | 13 days ago (2026-07-25 04:27:07 UTC) | 14 | C++ | DuckDB extension: quickjs by quackscience |
| 234 | [qvd](https://duckdb.org/community_extensions/extensions/qvd.html) | [DuckDB-QVD-Extension](https://github.com/snouhaud/DuckDB-QVD-Extension) | 🟢 Ongoing | 2 - ✅ Active | 14 days ago (2026-07-23 19:51:08 UTC) | 0 | Rust | An DuckDB extension to add QVD files read and write |
| 235 | [radio](https://duckdb.org/community_extensions/extensions/radio.html) | [radio](https://github.com/Query-farm/radio) | 🟢 Ongoing | 2 - ✅ Active | 12 days ago (2026-07-25 14:27:12 UTC) | 43 | C++ | Radio is a DuckDB extension by Query.Farm that brings real-time event streams... |
| 236 | [rapidfuzz](https://duckdb.org/community_extensions/extensions/rapidfuzz.html) | [rapidfuzz](https://github.com/Query-farm/rapidfuzz) | 🟢 Ongoing | 2 - ✅ Active | 11 days ago (2026-07-26 22:19:23 UTC) | 18 | C++ | DuckDB Community Extension adding RapidFuzz algorithms for search, deduplicat... |
| 237 | [raquet](https://duckdb.org/community_extensions/extensions/raquet.html) | [duckdb-raquet](https://github.com/CartoDB/duckdb-raquet) | 🟢 Ongoing | 2 - ✅ Active | 22 days ago (2026-07-15 14:35:34 UTC) | 14 | C++ | DuckDB extension for reading Raquet format (raster data in Parquet with QUADB... |
| 238 | [raster](https://duckdb.org/community_extensions/extensions/raster.html) | [duckdb-raster](https://github.com/ahuarte47/duckdb-raster) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-08-05 23:58:28 UTC) | 52 | C++ | DuckDB Extension for reading and writing raster files using SQL. |
| 239 | [rate_limit_fs](https://duckdb.org/community_extensions/extensions/rate_limit_fs.html) | [duckdb-rate-limit-filesystem](https://github.com/dentiny/duckdb-rate-limit-filesystem) | 🟢 Ongoing | 2 - ✅ Active | 12 days ago (2026-07-25 21:35:54 UTC) | 1 | C++ | DuckDB extension: rate_limit_fs by dentiny |
| 240 | [rawduck](https://duckdb.org/community_extensions/extensions/rawduck.html) | [rawduck](https://github.com/quackscience/rawduck) | ❓ Unknown | 1 - 🔥 Very Active | 6 days ago (2026-07-31 12:07:29 UTC) | 27 | C++ | Experimental RawMergeTree-like Extension for DuckDB |
| 241 | [rdf](https://duckdb.org/community_extensions/extensions/rdf.html) | [duck_rdf](https://github.com/nonodename/duck_rdf) | 🟢 Ongoing | 1 - 🔥 Very Active | 4 days ago (2026-08-03 02:16:46 UTC) | 28 | C++ | RDF file extension for DuckDB. Reads and writes supported |
| 242 | [read_dbf](https://duckdb.org/community_extensions/extensions/read_dbf.html) | [duckdb-dbf](https://github.com/tocharan/duckdb-dbf) | 🟢 Ongoing | 4 - 🟠 Stale | 162 days ago (2026-02-25 17:13:20 UTC) | 3 | C++ | Database connectivity extension by tocharan |
| 243 | [read_lines](https://duckdb.org/community_extensions/extensions/read_lines.html) | [duckdb_read_lines](https://github.com/teaguesterling/duckdb_read_lines) | 🟢 Ongoing | 2 - ✅ Active | 12 days ago (2026-07-25 19:36:30 UTC) | 4 | C++ | Simple parsers for fast extraction from line-based files  |
| 244 | [read_stat](https://duckdb.org/community_extensions/extensions/read_stat.html) | [duckdb-read-stat](https://github.com/dylanmeysmans/duckdb-read-stat) | ❓ Unknown | 3 - 🟡 Stable | 48 days ago (2026-06-19 23:25:46 UTC) | 34 | C | Read data sets from SAS, Stata, and SPSS from DuckDB with ReadStat |
| 245 | [redis](https://duckdb.org/community_extensions/extensions/redis.html) | [redis](https://github.com/Query-farm/redis) | 🟢 Ongoing | 2 - ✅ Active | 11 days ago (2026-07-26 22:19:24 UTC) | 13 | C++ | DuckDB Redis Client community extension |
| 246 | [robust](https://duckdb.org/community_extensions/extensions/robust.html) | [robust](https://github.com/robust-sql/robust) | ❓ Unknown | 2 - ✅ Active | 18 days ago (2026-07-20 01:26:38 UTC) | 5 | C++ | A DuckDB extension implementing Predicate Transfer to reduce cardinality expl... |
| 247 | [rrd](https://duckdb.org/community_extensions/extensions/rrd.html) | [duckdb-rrd](https://github.com/VertexStudio/duckdb-rrd) | ❓ Unknown | 3 - 🟡 Stable | 34 days ago (2026-07-03 18:31:26 UTC) | 0 | Rust | DuckDB extension: rrd by VertexStudio |
| 248 | [rusty_quack](https://duckdb.org/community_extensions/extensions/rusty_quack.html) | [extension-template-rs](https://github.com/duckdb/extension-template-rs) | ❓ Unknown | 2 - ✅ Active | 15 days ago (2026-07-23 06:05:55 UTC) | 112 | Rust | (Experimental) Template for Rust-based DuckDB extensions |
| 249 | [rusty_sheet](https://duckdb.org/community_extensions/extensions/rusty_sheet.html) | [rusty-sheet](https://github.com/redraiment/rusty-sheet) | 🟢 Ongoing | 4 - 🟠 Stale | 175 days ago (2026-02-13 02:27:56 UTC) | 75 | Rust | An Excel/WPS/OpenDocument Spreadsheets file reader for DuckDB |
| 250 | [salesforce](https://duckdb.org/community_extensions/extensions/salesforce.html) | [duckdb-salesforce](https://github.com/flozer/duckdb-salesforce) | ❓ Unknown | 1 - 🔥 Very Active | 3 days ago (2026-08-03 11:35:23 UTC) | 2 | C++ | DuckDB extension: salesforce by flozer |
| 251 | [sazgar](https://duckdb.org/community_extensions/extensions/sazgar.html) | [Sazgar](https://github.com/Angelerator/Sazgar) | ❓ Unknown | 3 - 🟡 Stable | 77 days ago (2026-05-22 04:56:10 UTC) | 13 | HTML | DuckDB extension for system monitoring & intelligent SQL routing. 25+ functio... |
| 252 | [scalarfs](https://duckdb.org/community_extensions/extensions/scalarfs.html) | [duckdb_scalarfs](https://github.com/teaguesterling/duckdb_scalarfs) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-08-07 01:44:38 UTC) | 8 | C++ | A collection of simple virtual filesystems for treating scalar values as files. |
| 253 | [scrooge](https://duckdb.org/community_extensions/extensions/scrooge.html) | [Scrooge-McDuck](https://github.com/pdet/Scrooge-McDuck) | ❓ Unknown | 4 - 🟠 Stale | 94 days ago (2026-05-04 14:27:57 UTC) | 162 | C++ | DuckDB extension: scrooge by pdet |
| 254 | [se3](https://duckdb.org/community_extensions/extensions/se3.html) | [se3](https://github.com/jokasimr/se3) | 🟢 Ongoing | 2 - ✅ Active | 18 days ago (2026-07-19 09:45:05 UTC) | 0 | C++ | Duckdb extension for efficient rotation / translation operations on points in... |
| 255 | [semantic_views](https://duckdb.org/community_extensions/extensions/semantic_views.html) | [duckdb-semantic-views](https://github.com/anentropic/duckdb-semantic-views) | ❓ Unknown | 1 - 🔥 Very Active | today (2026-08-07 06:10:27 UTC) | 10 | Rust | Semantic Views for DuckDB. |
| 256 | [sheetreader](https://duckdb.org/community_extensions/extensions/sheetreader.html) | [sheetreader-duckdb](https://github.com/polydbms/sheetreader-duckdb) | ❓ Unknown | 4 - 🟠 Stale | 144 days ago (2026-03-15 11:03:07 UTC) | 58 | C++ | DuckDB extension: sheetreader by polydbms |
| 257 | [shellfs](https://duckdb.org/community_extensions/extensions/shellfs.html) | [shellfs](https://github.com/Query-farm/shellfs) | 🟢 Ongoing | 2 - ✅ Active | 13 days ago (2026-07-25 04:27:09 UTC) | 95 | C++ | DuckDB extension allowing shell commands to be used for input and output. |
| 258 | [sistat](https://duckdb.org/community_extensions/extensions/sistat.html) | [duckdb-sistat](https://github.com/fklezin/duckdb-sistat) | ❓ Unknown | 4 - 🟠 Stale | 150 days ago (2026-03-09 09:09:46 UTC) | 3 | C++ | DuckDB extension to query Slovenia's SiStat open data directly using SQL. No... |
| 259 | [sitemap](https://duckdb.org/community_extensions/extensions/sitemap.html) | [duckdb-sitemap](https://github.com/midwork-finds-jobs/duckdb-sitemap) | 🟢 Ongoing | 4 - 🟠 Stale | 170 days ago (2026-02-17 14:13:12 UTC) | 1 | C++ | DuckDB extension for parsing XML sitemaps from websites |
| 260 | [sitting_duck](https://duckdb.org/community_extensions/extensions/sitting_duck.html) | [sitting_duck](https://github.com/teaguesterling/sitting_duck) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-08-05 22:16:35 UTC) | 21 | C | Sitting Duck is a DuckDB extension that makes Abstract Syntax Trees (ASTs) fr... |
| 261 | [slack](https://github.com/dentiny/duckdb-slack) | [duckdb-slack](https://github.com/dentiny/duckdb-slack) | ❓ Unknown | 4 - 🟠 Stale | 168 days ago (2026-02-19 18:08:54 UTC) | 0 | C++ | DuckDB extension: slack by dentiny |
| 262 | [snowflake](https://duckdb.org/community_extensions/extensions/snowflake.html) | [duckdb-snowflake](https://github.com/iqea-ai/duckdb-snowflake) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-08-07 05:15:55 UTC) | 58 | C++ | A powerful DuckDB extension that enables seamless querying of Snowflake datab... |
| 263 | [splink_udfs](https://duckdb.org/community_extensions/extensions/splink_udfs.html) | [splink_udfs](https://github.com/moj-analytical-services/splink_udfs) | ❓ Unknown | 4 - 🟠 Stale | 181 days ago (2026-02-06 11:01:11 UTC) | 5 | C++ | DuckDB extension: splink_udfs by moj-analytical-services |
| 264 | [splunk](https://duckdb.org/community_extensions/extensions/splunk.html) | [duckdb-splunk](https://github.com/smithclay/duckdb-splunk) | ❓ Unknown | 1 - 🔥 Very Active | 3 days ago (2026-08-03 16:07:52 UTC) | 1 | C++ | read logs from splunk into duckdb |
| 265 | [spxlsx](https://duckdb.org/community_extensions/extensions/spxlsx.html) | [spxlsx](https://github.com/paulmupeters/spxlsx) | 🟢 Ongoing | 3 - 🟡 Stable | 37 days ago (2026-06-30 20:34:53 UTC) | 2 | C++ | Duckdb extension to read sharepoint lists and excel |
| 266 | [sshfs](https://duckdb.org/community_extensions/extensions/sshfs.html) | [duckdb-sshfs](https://github.com/midwork-finds-jobs/duckdb-sshfs) | 🟢 Ongoing | 3 - 🟡 Stable | 61 days ago (2026-06-06 19:02:46 UTC) | 12 | C++ | DuckDB sshfs extension - Read and write files through ssh inside DuckDB |
| 267 | [st_read_multi](https://duckdb.org/community_extensions/extensions/st_read_multi.html) | [duckdb-ext-st-read-multi](https://github.com/yutannihilation/duckdb-ext-st-read-multi) | 🟢 Ongoing | 2 - ✅ Active | 10 days ago (2026-07-27 13:54:12 UTC) | 10 | Rust | A DuckDB extension to import multiple geospatial files with `ST_Read_Multi()` |
| 268 | [stac](https://duckdb.org/community_extensions/extensions/stac.html) | [duckdb-stac](https://github.com/ahuarte47/duckdb-stac) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-08-06 21:00:54 UTC) | 16 | C++ | DuckDB extension for reading data from SpatioTemporal Asset Catalogs (STAC) u... |
| 269 | [stats_duck](https://duckdb.org/community_extensions/extensions/stats_duck.html) | [the-stats-duck](https://github.com/KoliStat/the-stats-duck) | ❓ Unknown | 1 - 🔥 Very Active | today (2026-08-06 19:42:41 UTC) | 55 | C++ | A statistical computing toolkit for DuckDB. |
| 270 | [stochastic](https://duckdb.org/community_extensions/extensions/stochastic.html) | [stochastic](https://github.com/Query-farm/stochastic) | 🟢 Ongoing | 2 - ✅ Active | 13 days ago (2026-07-25 04:27:10 UTC) | 26 | C++ | A DuckDB extension that add comprehensive statistical distribution functions... |
| 271 | [substrait](https://duckdb.org/community_extensions/extensions/substrait.html) | [duckdb-substrait-extension](https://github.com/substrait-io/duckdb-substrait-extension) | 🟢 Ongoing | 1 - 🔥 Very Active | 2 days ago (2026-08-04 16:03:30 UTC) | 67 | C++ | DuckDB extension: substrait by substrait-io |
| 272 | [sudan](https://duckdb.org/community_extensions/extensions/sudan.html) | [duckdb-sudan-](https://github.com/Osman-Geomatics93/duckdb-sudan-) | ❓ Unknown | 4 - 🟠 Stale | 168 days ago (2026-02-19 11:49:28 UTC) | 0 | Jupyter Notebook | DuckDB extension: sudan by Osman-Geomatics93 |
| 273 | [system_stats](https://duckdb.org/community_extensions/extensions/system_stats.html) | [system_stats](https://github.com/dentiny/system_stats) | 🟢 Ongoing | 2 - ✅ Active | 12 days ago (2026-07-25 22:00:06 UTC) | 3 | C++ | DuckDB extension: system_stats by dentiny |
| 274 | [table_guard](https://duckdb.org/community_extensions/extensions/table_guard.html) | [duckdb-table-guard](https://github.com/yoogoc/duckdb-table-guard) | 🟢 Ongoing | 3 - 🟡 Stable | 84 days ago (2026-05-14 09:52:13 UTC) | 2 | C++ | A DuckDB extension for table-level access control |
| 275 | [table_inspector](https://duckdb.org/community_extensions/extensions/table_inspector.html) | [duckdb-table-inspector](https://github.com/dentiny/duckdb-table-inspector) | 🟢 Ongoing | 2 - ✅ Active | 10 days ago (2026-07-27 17:46:08 UTC) | 2 | C++ | DuckDB extension: table_inspector by dentiny |
| 276 | [talib](https://duckdb.org/community_extensions/extensions/talib.html) | [atm_talib](https://github.com/neuesql/atm_talib) | 🟢 Ongoing | 4 - 🟠 Stale | 108 days ago (2026-04-21 06:06:51 UTC) | 5 | C++ | A duckdb TA-Lib to add technical analysis in Financial Markets with SQL easily |
| 277 | [tarfs](https://duckdb.org/community_extensions/extensions/tarfs.html) | [duckdb_tarfs](https://github.com/Maxxen/duckdb_tarfs) | ❓ Unknown | 4 - 🟠 Stale | over a year ago (2024-08-26 11:01:47 UTC) | 12 | C++ | DuckDB extension: tarfs by Maxxen |
| 278 | [tera](https://duckdb.org/community_extensions/extensions/tera.html) | [tera](https://github.com/Query-farm/tera) | 🟢 Ongoing | 2 - ✅ Active | 13 days ago (2026-07-25 04:27:11 UTC) | 9 | C++ | DuckDB extension: tera |
| 279 | [textplot](https://duckdb.org/community_extensions/extensions/textplot.html) | [textplot](https://github.com/Query-farm/textplot) | 🟢 Ongoing | 2 - ✅ Active | 13 days ago (2026-07-25 04:27:12 UTC) | 25 | C++ | A DuckDB community extension that enables text-based data visualization direc... |
| 280 | [three_d](https://duckdb.org/community_extensions/extensions/three_d.html) | [duckdb-3d-extension](https://github.com/cityjson/duckdb-3d-extension) | ❓ Unknown | 2 - ✅ Active | 9 days ago (2026-07-28 13:04:41 UTC) | 1 | C++ | (Still Experimental) DuckDB extension to process 3D geomerty |
| 281 | [title_mapper](https://duckdb.org/community_extensions/extensions/title_mapper.html) | [duckdb-title-mapper](https://github.com/martin-conur/duckdb-title-mapper) | ❓ Unknown | 3 - 🟡 Stable | 73 days ago (2026-05-25 21:56:26 UTC) | 3 | Rust | DuckDB extension: title_mapper by martin-conur |
| 282 | [toml](https://duckdb.org/community_extensions/extensions/toml.html) | [duckdb-toml](https://github.com/vergenzt/duckdb-toml) | 🟢 Ongoing | 2 - ✅ Active | 14 days ago (2026-07-24 05:08:13 UTC) | 0 | C++ | Parse TOML format in DuckDB |
| 283 | [tpch_rust](https://duckdb.org/community_extensions/extensions/tpch_rust.html) | [duckdb-tpch-rust](https://github.com/guillesd/duckdb-tpch-rust) | ❓ Unknown | 3 - 🟡 Stable | 59 days ago (2026-06-08 15:40:17 UTC) | 0 | Rust | DuckDB extension to generate tpch tables using tpch-rs |
| 284 | [tributary](https://duckdb.org/community_extensions/extensions/tributary.html) | [tributary](https://github.com/Query-farm/tributary) | ❓ Unknown | 2 - ✅ Active | 11 days ago (2026-07-26 22:19:25 UTC) | 57 | C++ | A DuckDB Extension for Kafka |
| 285 | [trino_parity](https://duckdb.org/community_extensions/extensions/trino_parity.html) | [duckdb-trino-parity-extension](https://github.com/brikk/duckdb-trino-parity-extension) | 🟢 Ongoing | 1 - 🔥 Very Active | 7 days ago (2026-07-30 14:28:56 UTC) | 0 | C++ | An extension adding functions to duckdb to exactly match Trino function behav... |
| 286 | [tsid](https://duckdb.org/community_extensions/extensions/tsid.html) | [tsid](https://github.com/Query-farm/tsid) | 🟢 Ongoing | 2 - ✅ Active | 11 days ago (2026-07-26 22:19:26 UTC) | 6 | C++ | TSID Extension for DuckDB  |
| 287 | [ulid](https://duckdb.org/community_extensions/extensions/ulid.html) | [duckdb_ulid](https://github.com/Maxxen/duckdb_ulid) | ❓ Unknown | 4 - 🟠 Stale | over a year ago (2024-07-09 09:35:50 UTC) | 25 | C++ | DuckDB extension: ulid by Maxxen |
| 288 | [urlpattern](https://duckdb.org/community_extensions/extensions/urlpattern.html) | [duckdb_urlpattern](https://github.com/teaguesterling/duckdb_urlpattern) | 🟢 Ongoing | 2 - ✅ Active | 9 days ago (2026-07-28 20:10:15 UTC) | 8 | C++ | An implementation of URLPattern for DuckDB |
| 289 | [us_address_standardizer](https://duckdb.org/community_extensions/extensions/us_address_standardizer.html) | [duckdb-address-standardizer](https://github.com/ericmanning/duckdb-address-standardizer) | 🟢 Ongoing | 3 - 🟡 Stable | 78 days ago (2026-05-20 14:50:54 UTC) | 3 | C | DuckDB extension for parsing and standardizing (USA) postal addresses using P... |
| 290 | [valhalla_routing](https://duckdb.org/community_extensions/extensions/valhalla_routing.html) | [duckdb-valhalla-routing](https://github.com/midwork-finds-jobs/duckdb-valhalla-routing) | 🟢 Ongoing | 4 - 🟠 Stale | 170 days ago (2026-02-17 11:36:12 UTC) | 8 | Makefile | WIP: Attempt to package valhalla routing engine to duckdb |
| 291 | [vindex](https://duckdb.org/community_extensions/extensions/vindex.html) | [duckdb-vector-index](https://github.com/Icemap/duckdb-vector-index) | ❓ Unknown | 2 - ✅ Active | 21 days ago (2026-07-16 10:06:50 UTC) | 8 | C++ | A DuckDB extension providing HNSW, IVF, DiskANN, and SPANN vector indexes wit... |
| 292 | [waddle](https://duckdb.org/community_extensions/extensions/waddle.html) | [extension-template](https://github.com/duckdb/extension-template) | ❓ Unknown | 3 - 🟡 Stable | 45 days ago (2026-06-22 10:58:32 UTC) | 287 | Python | Template for DuckDB extensions to help you develop, test and deploy a custom... |
| 293 | [warc](https://duckdb.org/community_extensions/extensions/warc.html) | [duckdb_warc](https://github.com/midwork-finds-jobs/duckdb_warc) | ❓ Unknown | 4 - 🟠 Stale | 182 days ago (2026-02-05 15:33:27 UTC) | 6 | Rust | DuckDB extension for parsing WARC files |
| 294 | [web_archive](https://duckdb.org/community_extensions/extensions/web_archive.html) | [duckdb-web-archive](https://github.com/midwork-finds-jobs/duckdb-web-archive) | 🟢 Ongoing | 3 - 🟡 Stable | 40 days ago (2026-06-27 17:30:16 UTC) | 22 | C++ | DuckDB extension to fetch pages from Wayback Machine & Common Crawl |
| 295 | [web_search](https://duckdb.org/community_extensions/extensions/web_search.html) | [duckdb-web-search](https://github.com/midwork-finds-jobs/duckdb-web-search) | 🟢 Ongoing | 4 - 🟠 Stale | 108 days ago (2026-04-20 21:51:13 UTC) | 0 | C++ | Web/HTTP functionality extension by midwork-finds-jobs |
| 296 | [webbed](https://duckdb.org/community_extensions/extensions/webbed.html) | [duckdb_webbed](https://github.com/teaguesterling/duckdb_webbed) | 🟢 Ongoing | 2 - ✅ Active | 11 days ago (2026-07-27 03:12:40 UTC) | 68 | C++ | A comprehensive XML and HTML processing extension for DuckDB that enables SQL... |
| 297 | [webdavfs](https://duckdb.org/community_extensions/extensions/webdavfs.html) | [duckdb-webdavfs](https://github.com/midwork-finds-jobs/duckdb-webdavfs) | ❓ Unknown | 4 - 🟠 Stale | 104 days ago (2026-04-25 03:42:47 UTC) | 1 | C++ | DuckDB WebDAVfs Extension - WebDAV filesystem support for DuckDB |
| 298 | [webmacro](https://duckdb.org/community_extensions/extensions/webmacro.html) | [webmacro](https://github.com/Query-farm/webmacro) | 🟢 Ongoing | 2 - ✅ Active | 11 days ago (2026-07-26 22:19:27 UTC) | 15 | C++ | DuckDB WebMacro: Share and Load your SQL Macros via gists |
| 299 | [whisper](https://duckdb.org/community_extensions/extensions/whisper.html) | [duckdb-whisper](https://github.com/tobilg/duckdb-whisper) | 🟢 Ongoing | 3 - 🟡 Stable | 40 days ago (2026-06-27 15:19:59 UTC) | 10 | C++ | Use whisper.cpp within DuckDB to translate / transpile speech to text |
| 300 | [wireduck](https://duckdb.org/community_extensions/extensions/wireduck.html) | [wireduck](https://github.com/hyehudai/wireduck) | ❓ Unknown | 4 - 🟠 Stale | 317 days ago (2025-09-23 21:22:03 UTC) | 48 | C++ | Duckdb extension to read pcap files |
| 301 | [yaml](https://duckdb.org/community_extensions/extensions/yaml.html) | [duckdb_yaml](https://github.com/teaguesterling/duckdb_yaml) | 🟢 Ongoing | 2 - ✅ Active | 12 days ago (2026-07-25 19:36:24 UTC) | 21 | C++ |  A DuckDB to read and work with YAML files in a similar way to JSON files (al... |
| 302 | [yardstick](https://duckdb.org/community_extensions/extensions/yardstick.html) | [yardstick](https://github.com/sidequery/yardstick) | ❓ Unknown | 3 - 🟡 Stable | 34 days ago (2026-07-03 19:43:26 UTC) | 58 | Rust | An implementation of Measures in SQL as a DuckDB extension |
| 303 | [zarr](https://duckdb.org/community_extensions/extensions/zarr.html) | [duckdb-zarr](https://github.com/xqlsystems/duckdb-zarr) | 🟢 Ongoing | 1 - 🔥 Very Active | 2 days ago (2026-08-04 21:04:02 UTC) | 29 | Rust | Query Zarr stores with SQL directly from DuckDB |
| 304 | [zeek](https://duckdb.org/community_extensions/extensions/zeek.html) | [zeek-duckdb](https://github.com/ynadji/zeek-duckdb) | 🟢 Ongoing | 4 - 🟠 Stale | 114 days ago (2026-04-14 22:02:22 UTC) | 3 | C++ | read_zeek table function to read Zeek TSV logs into DuckDB |
| 305 | [zim](https://duckdb.org/community_extensions/extensions/zim.html) | [duckdb_zim](https://github.com/teaguesterling/duckdb_zim) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-08-06 16:26:29 UTC) | 4 | C++ | DuckDB extension for working with zim files |
| 306 | [zipfs](https://duckdb.org/community_extensions/extensions/zipfs.html) | [duckdb-zipfs](https://github.com/isaacbrodsky/duckdb-zipfs) | 🟢 Ongoing | 2 - ✅ Active | 15 days ago (2026-07-22 17:04:46 UTC) | 66 | C++ | DuckDB extension to read files within zip archives. |

</details>
## Appendix: DuckDB Release Information

### Current Release Context

DuckDB follows **semantic versioning** with regular releases. For complete and up-to-date release information, see the official [**DuckDB Release Calendar**](https://duckdb.org/release_calendar.html).

### Upcoming Releases

|| Version | Planned Date | LTS |
||---------|-------------|-----|

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

<p class="fine-print">Last updated: 2026-08-07</p>
