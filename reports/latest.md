# DuckDB Extensions Analysis

🦆 **Automated monitoring and analysis of DuckDB's extension ecosystem**


[Executive summary](#executive-summary) | [Jump to Summary](#summary) | [Core Extensions](#core-extensions) | [Community Extensions](#community-extensions)

---

**Running on DuckDB:** v1.5.4 (2026-06-17)
This report provides a comprehensive analysis of DuckDB extensions, including both core extensions (built into DuckDB) and community-contributed extensions.

For third-party extensions discovered outside the official registries, see: [Third-party extensions](https://mjboothaus.github.io/duckdb-extensions-analysis/third-party/).

For a lightweight monthly roundup of notable ecosystem changes, see: [What’s new](https://github.com/Mjboothaus/duckdb-extensions-analysis/blob/main/WHATS_NEW.md).

*Note:* third-party labelling is an ongoing work in progress, so the verified list is partial.

---
## Executive summary


### At a glance
- **314** total extensions tracked (**29** core, **285** community)
- **71 / 314** extensions updated in the last 7 days
- **135 / 314** extensions updated in the last 30 days
- **1** community repositories are archived
- **57** community extensions have unknown/repo issues (missing or inaccessible repositories)

### Highlights
#### Most active (last 7 days)
| Extension | Repository | Last activity |
|---|---|---|
| [ai](https://duckdb.org/community_extensions/extensions/ai.html) | [duckdb-ai](https://github.com/leonardovida/duckdb-ai) | today (2026-07-21 08:19:31 UTC) |
| [bigquery](https://duckdb.org/community_extensions/extensions/bigquery.html) | [duckdb-bigquery](https://github.com/hafenkran/duckdb-bigquery) | today (2026-07-20 17:53:38 UTC) |
| [duckhts](https://duckdb.org/community_extensions/extensions/duckhts.html) | [duckhts](https://github.com/RGenomicsETL/duckhts) | today (2026-07-21 08:16:49 UTC) |
| [ducklake_cdc](https://duckdb.org/community_extensions/extensions/ducklake_cdc.html) | [ducklake-cdc-extension](https://github.com/ekkuleivonen/ducklake-cdc-extension) | today (2026-07-21 04:28:11 UTC) |
| [firebird](https://duckdb.org/community_extensions/extensions/firebird.html) | [duckdb-firebird](https://github.com/flozer/duckdb-firebird) | today (2026-07-20 19:04:27 UTC) |

#### Most starred (community)
| Extension | Repository | Stars |
|---|---|---:|
| [duckpgq](https://duckdb.org/community_extensions/extensions/duckpgq.html) | [duckpgq-extension](https://github.com/cwida/duckpgq-extension) | 439 |
| [flock](https://duckdb.org/community_extensions/extensions/flock.html) | [flock](https://github.com/dais-polymtl/flock) | 350 |
| [gsheets](https://duckdb.org/community_extensions/extensions/gsheets.html) | [duckdb_gsheets](https://github.com/evidence-dev/duckdb_gsheets) | 346 |
| [airport](https://duckdb.org/community_extensions/extensions/airport.html) | [airport](https://github.com/Query-farm/airport) | 345 |
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
| **Total Extensions** | 314 | +9 🔼 |
| **Core Extensions** | 29 | → Stable |
| **Community Extensions** | 285 | +9 🔼 |
| **Recently Active** (≤ 30 days) | 135 (43.0%) | +20 🔼 |
| **Very Active** (≤ 7 days) | 71 (22.6%) | — |

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
| 1 | [autocomplete](https://duckdb.org/docs/current/core_extensions/autocomplete) | [duckdb/duckdb](https://github.com/duckdb/duckdb/tree/main/extension/autocomplete) | 🟢 Ongoing | 18 days ago (2026-07-02 15:48:28 UTC) | N/A (part of core DuckDB repo) | C++ | Core DuckDB extension: autocomplete |
| 2 | [avro](https://duckdb.org/docs/current/core_extensions/avro) | [duckdb-avro](https://github.com/duckdb/duckdb-avro) | 🟢 Ongoing | 5 days ago (2026-07-15 10:48:14 UTC) | 36 | C++ | Apache Avro format support |
| 3 | [aws](https://duckdb.org/docs/current/core_extensions/aws) | [duckdb-aws](https://github.com/duckdb/duckdb-aws) | 🟢 Ongoing | 4 days ago (2026-07-16 12:34:44 UTC) | 64 | C++ | AWS S3 integration |
| 4 | [azure](https://duckdb.org/docs/current/core_extensions/azure) | [duckdb-azure](https://github.com/duckdb/duckdb-azure) | 🟢 Ongoing | 7 days ago (2026-07-13 18:59:38 UTC) | 77 | C++ | Azure extension for DuckDB |
| 5 | [delta](https://duckdb.org/docs/current/core_extensions/delta) | [duckdb-delta](https://github.com/duckdb/duckdb-delta) | 🟢 Ongoing | 7 days ago (2026-07-13 19:23:42 UTC) | 227 | C++ | DuckDB extension for Delta Lake |
| 6 | [ducklake](https://duckdb.org/docs/current/core_extensions/ducklake) | [duckdb/ducklake](https://github.com/duckdb/ducklake) | 🟢 Ongoing | 33 days ago | N/A (part of core DuckDB repo) | C++ | Delta Lake support via DuckLake (different from delta extension) |
| 7 | [encodings](https://duckdb.org/docs/current/core_extensions/encodings) | [duckdb-encodings](https://github.com/duckdb/duckdb-encodings) | 🟢 Ongoing | 154 days ago (2026-02-16 11:43:18 UTC) | 15 | C++ | Character encoding support |
| 8 | [excel](https://duckdb.org/docs/current/core_extensions/excel) | [duckdb-excel](https://github.com/duckdb/duckdb-excel) | 🟢 Ongoing | 53 days ago (2026-05-28 14:57:36 UTC) | 58 | C++ | Excel extension for DuckDB |
| 9 | [fts](https://duckdb.org/docs/current/core_extensions/full_text_search) | [duckdb-fts](https://github.com/duckdb/duckdb-fts) | 🟢 Ongoing | 4 days ago (2026-07-16 14:34:43 UTC) | 40 | C++ | Full-text search functionality |
| 10 | [httpfs](https://duckdb.org/docs/current/core_extensions/httpfs/overview) | [duckdb-httpfs](https://github.com/duckdb/duckdb-httpfs) | 🟢 Ongoing | 3 days ago (2026-07-17 11:57:30 UTC) | 57 | C++ | HTTP/S3 filesystem support |
| 11 | [iceberg](https://duckdb.org/docs/current/core_extensions/iceberg/overview) | [duckdb-iceberg](https://github.com/duckdb/duckdb-iceberg) | 🟢 Ongoing | today (2026-07-20 16:46:34 UTC) | 420 | C++ | Apache Iceberg format support |
| 12 | [icu](https://duckdb.org/docs/current/core_extensions/icu) | [duckdb/duckdb](https://github.com/duckdb/duckdb/tree/main/extension/icu) | 🟢 Ongoing | 2 days ago (2026-07-19 06:10:54 UTC) | N/A (part of core DuckDB repo) | C++ | Core DuckDB extension: icu |
| 13 | [inet](https://duckdb.org/docs/current/core_extensions/inet) | [duckdb-inet](https://github.com/duckdb/duckdb-inet) | 🟢 Ongoing | 242 days ago (2025-11-20 22:54:12 UTC) | 14 | C++ | Internet address data types |
| 14 | [json](https://duckdb.org/docs/current/data/json/overview) | [duckdb/duckdb](https://github.com/duckdb/duckdb/tree/main/extension/json) | 🟢 Ongoing | 4 days ago (2026-07-16 09:25:26 UTC) | N/A (part of core DuckDB repo) | C++ | Core DuckDB extension: json |
| 15 | [lance](https://duckdb.org/docs/current/core_extensions/lance) | [lance-duckdb](https://github.com/lance-format/lance-duckdb) | 🟢 Ongoing | today (2026-07-21 07:17:23 UTC) | 123 | C++ | The lance extensions for DuckDB enable reading and writing of lance tables. |
| 16 | [motherduck](https://duckdb.org/docs/current/core_extensions/motherduck) | [duckdb/duckdb](https://github.com/duckdb/duckdb) *(Third Party - Closed source - maintained by MotherDuck Inc.)* | 🟢 Ongoing | 33 days ago | N/A (part of core DuckDB repo) | C++ | Core DuckDB extension: motherduck |
| 17 | [mysql](https://duckdb.org/docs/current/core_extensions/mysql) | [duckdb-mysql](https://github.com/duckdb/duckdb-mysql) | 🟢 Ongoing | 8 days ago (2026-07-12 16:59:53 UTC) | 98 | C++ | MySQL database connectivity |
| 18 | [odbc](https://duckdb.org/docs/current/core_extensions/odbc/overview) | [odbc-scanner](https://github.com/duckdb/odbc-scanner) | 🟢 Ongoing | 51 days ago (2026-05-30 11:58:55 UTC) | 38 | C++ | DuckDB ODBC extension |
| 19 | [parquet](https://duckdb.org/docs/current/data/parquet/overview) | [duckdb/duckdb](https://github.com/duckdb/duckdb/tree/main/extension/parquet) | 🟢 Ongoing | today (2026-07-20 10:40:22 UTC) | N/A (part of core DuckDB repo) | C++ | Core DuckDB extension: parquet |
| 20 | [postgres](https://duckdb.org/docs/current/core_extensions/postgres/overview) | [duckdb-postgres](https://github.com/duckdb/duckdb-postgres) | 🟢 Ongoing | today (2026-07-20 19:59:13 UTC) | 368 | C++ | PostgreSQL database connectivity |
| 21 | [quack](https://duckdb.org/docs/current/core_extensions/quack) | [duckdb-quack](https://github.com/duckdb/duckdb-quack) | 🟢 Ongoing | today (2026-07-20 13:50:21 UTC) | 136 | C++ | Quack remote protocol |
| 22 | [spatial](https://duckdb.org/docs/current/core_extensions/spatial/overview) | [duckdb-spatial](https://github.com/duckdb/duckdb-spatial) | 🟢 Ongoing | 10 days ago (2026-07-10 19:13:52 UTC) | 695 | C++ | Geospatial data types and functions |
| 23 | [sqlite](https://duckdb.org/docs/current/core_extensions/sqlite) | [duckdb-sqlite](https://github.com/duckdb/duckdb-sqlite) | 🟢 Ongoing | 8 days ago (2026-07-12 16:53:10 UTC) | 283 | C++ | DuckDB extension to read and write to SQLite databases |
| 24 | [tpcds](https://duckdb.org/docs/current/core_extensions/tpcds) | [duckdb/duckdb](https://github.com/duckdb/duckdb/tree/main/extension/tpcds) | 🟢 Ongoing | 4 days ago (2026-07-16 10:56:07 UTC) | N/A (part of core DuckDB repo) | C++ | Core DuckDB extension: tpcds |
| 25 | [tpch](https://duckdb.org/docs/current/core_extensions/tpch) | [duckdb/duckdb](https://github.com/duckdb/duckdb/tree/main/extension/tpch) | 🟢 Ongoing | 12 days ago (2026-07-08 12:10:49 UTC) | N/A (part of core DuckDB repo) | C++ | Core DuckDB extension: tpch |
| 26 | [ui](https://duckdb.org/docs/current/core_extensions/ui) | [duckdb-ui](https://github.com/duckdb/duckdb-ui) | 🟢 Ongoing | 33 days ago (2026-06-18 00:11:08 UTC) | 453 | C++ | Browser-based user interface for DuckDB |
| 27 | [unity_catalog](https://duckdb.org/docs/current/core_extensions/unity_catalog) | [unity_catalog](https://github.com/duckdb/unity_catalog) | 🟢 Ongoing | 8 days ago (2026-07-12 21:42:07 UTC) | 104 | C++ | Proof-of-concept extension combining the delta extension with Unity Catalog |
| 28 | [vortex](https://duckdb.org/docs/current/core_extensions/vortex) | [duckdb/duckdb](https://github.com/duckdb/duckdb) *(Third Party - Closed source - third-party extension)* | 🟢 Ongoing | 33 days ago | N/A (part of core DuckDB repo) | C++ | Core DuckDB extension: vortex |
| 29 | [vss](https://duckdb.org/docs/current/core_extensions/vss) | [duckdb-vss](https://github.com/duckdb/duckdb-vss) | 🟢 Ongoing | 27 days ago (2026-06-23 11:03:14 UTC) | 260 | C++ | Vector similarity search |

</details>

---
---
## Community Extensions

Third-party extensions maintained by the community


**Total:** 285 extensions | 🔥 Very Active (≤7d): 71 | ✅ Active (≤30d): 64 | 🟡 Stable (≤90d): 67 | 🟠 Stale (>90d): 83

<details open markdown="1">
<summary>Click to expand/collapse community extensions table</summary>

| # | Extension | Repository | Status | Activity | Last Activity | Stars | Language | Description |
|---|-----------|------------|--------|----------|---------------|-------|----------|-------------|
| 1 | [a5](https://duckdb.org/community_extensions/extensions/a5.html) | [a5](https://github.com/Query-farm/a5) | 🟢 Ongoing | 2 - ✅ Active | 27 days ago (2026-06-24 04:24:57 UTC) | 12 | C++ | A5 Geospatial Extension for DuckDB |
| 2 | [acp](https://duckdb.org/community_extensions/extensions/acp.html) | [duckdb-acp](https://github.com/sidequery/duckdb-acp) | 🟡 Archived | 4 - 🟠 Stale | 222 days ago (2025-12-11 03:36:46 UTC) | 58 | Rust | Use Claude Code & other AI agents from inside DuckDB via extension |
| 3 | [adbc](https://duckdb.org/community_extensions/extensions/adbc.html) | [duckdb-adbc-client](https://github.com/columnar-tech/duckdb-adbc-client) | 🟢 Ongoing | 2 - ✅ Active | 15 days ago (2026-07-06 03:44:53 UTC) | 41 | C++ | ADBC Client for DuckDB  |
| 4 | [adbc_scanner](https://duckdb.org/community_extensions/extensions/adbc_scanner.html) | [adbc_scanner](https://github.com/Query-farm/adbc_scanner) | 🟢 Ongoing | 1 - 🔥 Very Active | 7 days ago (2026-07-13 19:43:02 UTC) | 18 | C++ | A DuckDB ADBC Scanner Extension - adds support for using ADBC drivers with Du... |
| 5 | [agent_data](https://duckdb.org/community_extensions/extensions/agent_data.html) | [agent_data_duckdb](https://github.com/axsaucedo/agent_data_duckdb) | 🟢 Ongoing | 2 - ✅ Active | 19 days ago (2026-07-01 18:15:12 UTC) | 23 | Rust | DuckDB extension: agent_data by axsaucedo |
| 6 | [ai](https://duckdb.org/community_extensions/extensions/ai.html) | [duckdb-ai](https://github.com/leonardovida/duckdb-ai) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-07-21 08:19:31 UTC) | 6 | C++ | Enhance DuckDB with AI functions, supporting all providers as well as local m... |
| 7 | [airport](https://duckdb.org/community_extensions/extensions/airport.html) | [airport](https://github.com/Query-farm/airport) | 🟢 Ongoing | 3 - 🟡 Stable | 51 days ago (2026-05-30 13:33:18 UTC) | 345 | C++ | The Airport extension for DuckDB, enables the use of Arrow Flight with DuckDB |
| 8 | [aixchess](https://duckdb.org/community_extensions/extensions/aixchess.html) | [aix](https://github.com/thomas-daniels/aix) | 🟢 Ongoing | 4 - 🟠 Stale | 113 days ago (2026-03-29 12:16:27 UTC) | 26 | Rust | Aix: Efficiently storing and querying chess game collections |
| 9 | [altertable](https://duckdb.org/community_extensions/extensions/altertable.html) | [duckdb-altertable](https://github.com/altertable-ai/duckdb-altertable) | 🟢 Ongoing | 3 - 🟡 Stable | 42 days ago (2026-06-08 21:24:51 UTC) | 0 | C++ | Query Altertable's lakehouse directly from your local DuckDB |
| 10 | [anndata](https://duckdb.org/community_extensions/extensions/anndata.html) | [anndata-duckdb-extension](https://github.com/honicky/anndata-duckdb-extension) | 🟢 Ongoing | 2 - ✅ Active | 13 days ago (2026-07-07 16:10:59 UTC) | 9 | C++ | Attach and AnnData file in duckdb and query it with SQL.  Perform SQL over gr... |
| 11 | [anofox_forecast](https://duckdb.org/community_extensions/extensions/anofox_forecast.html) | [anofox-forecast](https://github.com/DataZooDE/anofox-forecast) | 🟢 Ongoing | 1 - 🔥 Very Active | 3 days ago (2026-07-17 19:05:02 UTC) | 35 | C++ | Statistical timeseries forecasting in DuckDB |
| 12 | [anofox_scenario](https://github.com/DataZooDE/anofox-scenario) | [anofox-scenario](https://github.com/DataZooDE/anofox-scenario) | ❓ Unknown | 1 - 🔥 Very Active | 3 days ago (2026-07-17 15:27:01 UTC) | 1 | C++ | DuckDB extension for Git-like database branching. Create isolated scenarios f... |
| 13 | [anofox_statistics](https://duckdb.org/community_extensions/extensions/anofox_statistics.html) | [anofox-statistics](https://github.com/DataZooDE/anofox-statistics) | 🟢 Ongoing | 1 - 🔥 Very Active | 2 days ago (2026-07-18 16:27:33 UTC) | 12 | C++ | A DuckDB extension for statistical regression analysis, providing OLS, Ridge,... |
| 14 | [anofox_tabfm](https://duckdb.org/community_extensions/extensions/anofox_tabfm.html) | [anofox-tabfm](https://github.com/DataZooDE/anofox-tabfm) | 🟢 Ongoing | 1 - 🔥 Very Active | 3 days ago (2026-07-17 17:22:13 UTC) | 3 | C++ | DuckDB extension for tabular foundation models — zero-shot classification & r... |
| 15 | [anofox_tabular](https://duckdb.org/community_extensions/extensions/anofox_tabular.html) | [anofox-tabular](https://github.com/DataZooDE/anofox-tabular) | 🟢 Ongoing | 1 - 🔥 Very Active | 3 days ago (2026-07-17 16:07:03 UTC) | 15 | C++ | A duckdb extension which combines data quality and data preparation tools for... |
| 16 | [arrow](https://duckdb.org/community_extensions/extensions/arrow.html) | [duckdb-extension-alias](https://github.com/duckdb/duckdb-extension-alias) | ❓ Unknown | 4 - 🟠 Stale | 287 days ago (2025-10-06 09:07:38 UTC) | 4 | C | DuckDB extension: arrow |
| 17 | [astro](https://duckdb.org/community_extensions/extensions/astro.html) | [astro-duck](https://github.com/synapticore-io/astro-duck) | 🟢 Ongoing | 3 - 🟡 Stable | 62 days ago (2026-05-19 12:22:23 UTC) | 1 | C++ | 60+ astronomical SQL functions for DuckDB: coordinate transforms, CCM89 dust... |
| 18 | [behavioral](https://duckdb.org/community_extensions/extensions/behavioral.html) | [duckdb-behavioral](https://github.com/tomtom215/duckdb-behavioral) | ❓ Unknown | 1 - 🔥 Very Active | today (2026-07-19 17:53:11 UTC) | 12 | Rust | A DuckDB Community Extension to enable Behavioral Analytics, inspired by Clic... |
| 19 | [bigquery](https://duckdb.org/community_extensions/extensions/bigquery.html) | [duckdb-bigquery](https://github.com/hafenkran/duckdb-bigquery) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-07-20 17:53:38 UTC) | 166 | C++ | Integrates DuckDB with Google BigQuery, allowing direct querying and manageme... |
| 20 | [bitfilters](https://duckdb.org/community_extensions/extensions/bitfilters.html) | [bitfilters](https://github.com/Query-farm/bitfilters) | 🟢 Ongoing | 3 - 🟡 Stable | 84 days ago (2026-04-27 17:21:05 UTC) | 7 | C++ | A high-performance DuckDB extension providing probabilistic data structures f... |
| 21 | [blockduck](https://duckdb.org/community_extensions/extensions/blockduck.html) | [BlockDuck](https://github.com/luohaha/BlockDuck) | 🟢 Ongoing | 4 - 🟠 Stale | 285 days ago (2025-10-08 16:19:04 UTC) | 10 | C++ | Live SQL Queries on Blockchain |
| 22 | [boilstream](https://duckdb.org/community_extensions/extensions/boilstream.html) | [boilstream-extension](https://github.com/dforsber/boilstream-extension) | 🟢 Ongoing | 3 - 🟡 Stable | 44 days ago (2026-06-06 11:38:11 UTC) | 10 | C++ | Secure Remote Secrets Storage for DuckDB |
| 23 | [brew](https://duckdb.org/community_extensions/extensions/brew.html) | [duckdb-brew](https://github.com/adriens/duckdb-brew) | 🟢 Ongoing | 3 - 🟡 Stable | 51 days ago (2026-05-31 08:18:52 UTC) | 1 | C++ | duckdb extension to report installed brew packages/casks/formulas with SQL |
| 24 | [bvh2sql](https://duckdb.org/community_extensions/extensions/bvh2sql.html) | [bvh2sql](https://github.com/nkwork9999/bvh2sql) | 🟢 Ongoing | 3 - 🟡 Stable | 38 days ago (2026-06-12 12:17:09 UTC) | 0 | Makefile | SQL-related extension by nkwork9999 |
| 25 | [cache_httpfs](https://duckdb.org/community_extensions/extensions/cache_httpfs.html) | [duck-read-cache-fs](https://github.com/dentiny/duck-read-cache-fs) | 🟢 Ongoing | 2 - ✅ Active | 22 days ago (2026-06-28 19:31:57 UTC) | 142 | C++ | This repository is made as read-only filesystem for remote access. |
| 26 | [cache_prewarm](https://duckdb.org/community_extensions/extensions/cache_prewarm.html) | [duckdb-cache-prewarm](https://github.com/dentiny/duckdb-cache-prewarm) | 🟢 Ongoing | 2 - ✅ Active | 26 days ago (2026-06-25 08:16:11 UTC) | 9 | C++ | DuckDB extension: cache_prewarm by dentiny |
| 27 | [capi_quack](https://duckdb.org/community_extensions/extensions/capi_quack.html) | [extension-template-c](https://github.com/duckdb/extension-template-c) | ❓ Unknown | 2 - ✅ Active | 28 days ago (2026-06-22 08:56:11 UTC) | 31 | C | (Experimental) C/C++ template for DuckDB extensions based on the C API |
| 28 | [cassandra](https://duckdb.org/community_extensions/extensions/cassandra.html) | [duckdb-cassandra](https://github.com/dioptre/duckdb-cassandra) | ❓ Unknown | 4 - 🟠 Stale | 273 days ago (2025-10-20 19:15:10 UTC) | 2 | C++ | DuckDB Connector for Cassandra |
| 29 | [celestial](https://duckdb.org/community_extensions/extensions/celestial.html) | [duckdb-celestial](https://github.com/lisa-sgs/duckdb-celestial) | 🟢 Ongoing | 2 - ✅ Active | 19 days ago (2026-07-02 07:26:25 UTC) | 2 | C++ | DuckDB extension providing astronomical coordinates utilities |
| 30 | [chaos](https://duckdb.org/community_extensions/extensions/chaos.html) | [duckdb-chaos](https://github.com/taniabogatsch/duckdb-chaos) | 🟢 Ongoing | 4 - 🟠 Stale | 158 days ago (2026-02-12 14:50:01 UTC) | 1 | C++ | DuckDB extension: chaos by taniabogatsch |
| 31 | [chess](https://duckdb.org/community_extensions/extensions/chess.html) | [duckdb-chess](https://github.com/dotneB/duckdb-chess) | ❓ Unknown | 3 - 🟡 Stable | 54 days ago (2026-05-28 05:13:34 UTC) | 3 | Rust | A DuckDB extension for parsing and analyzing chess games in PGN format. |
| 32 | [chsql](https://duckdb.org/community_extensions/extensions/chsql.html) | [clickhouse-sql](https://github.com/Query-farm/clickhouse-sql) | ❓ Unknown | 4 - 🟠 Stale | 152 days ago (2026-02-18 19:49:47 UTC) | 91 | C++ | DuckDB Community Extension implementing ClickHouse SQL Dialect macros and Cus... |
| 33 | [chsql_native](https://duckdb.org/community_extensions/extensions/chsql_native.html) | [clickhouse-native](https://github.com/Query-farm/clickhouse-native) | ❓ Unknown | 4 - 🟠 Stale | 152 days ago (2026-02-18 19:49:46 UTC) | 20 | Rust | Experimental ClickHouse Native Client and Native file reader Extension for Du... |
| 34 | [cityjson](https://duckdb.org/community_extensions/extensions/cityjson.html) | [duckdb-cityjson](https://github.com/cityjson/duckdb-cityjson) | 🟢 Ongoing | 1 - 🔥 Very Active | 2 days ago (2026-07-19 06:50:17 UTC) | 9 | C++ | (Still Experimental) DuckDB extension for CityJSON |
| 35 | [clamp](https://duckdb.org/community_extensions/extensions/clamp.html) | [duckdb_clamp](https://github.com/oglego/duckdb_clamp) | 🟢 Ongoing | 3 - 🟡 Stable | 86 days ago (2026-04-26 01:35:35 UTC) | 2 | C++ | The Clamp extension introduces range-clamping scalar functions to DuckDB. Ini... |
| 36 | [cloudfront](https://duckdb.org/community_extensions/extensions/cloudfront.html) | [duckdb-cloudfront](https://github.com/midwork-finds-jobs/duckdb-cloudfront) | 🟢 Ongoing | 4 - 🟠 Stale | 165 days ago (2026-02-05 15:32:51 UTC) | 1 | C++ | DuckDB module which provides custom authentication methods on top of httpfs m... |
| 37 | [cloudfs](https://duckdb.org/community_extensions/extensions/cloudfs.html) | [cloudfs](https://github.com/trouchet/cloudfs) | 🟢 Ongoing | 1 - 🔥 Very Active | 7 days ago (2026-07-13 19:21:32 UTC) | 2 | C++ | A duckdb-based cloud filesystem query engine |
| 38 | [cozip](https://duckdb.org/community_extensions/extensions/cozip.html) | [cozip_reader](https://github.com/asterisk-labs/cozip_reader) | 🟢 Ongoing | 3 - 🟡 Stable | 67 days ago (2026-05-15 05:12:11 UTC) | 6 | C++ | Read Cloud-Optimized ZIP files |
| 39 | [crawler](https://duckdb.org/community_extensions/extensions/crawler.html) | [duckdb-crawler](https://github.com/midwork-finds-jobs/duckdb-crawler) | 🟢 Ongoing | 4 - 🟠 Stale | 109 days ago (2026-04-03 04:32:07 UTC) | 12 | C++ | DuckDB extension: crawler by midwork-finds-jobs |
| 40 | [cronjob](https://duckdb.org/community_extensions/extensions/cronjob.html) | [cronjob](https://github.com/Query-farm/cronjob) | 🟢 Ongoing | 4 - 🟠 Stale | 113 days ago (2026-03-29 21:04:33 UTC) | 51 | C++ | DuckDB CronJob Extension |
| 41 | [crypto](https://duckdb.org/community_extensions/extensions/crypto.html) | [crypto](https://github.com/Query-farm/crypto) | 🟢 Ongoing | 3 - 🟡 Stable | 89 days ago (2026-04-22 13:25:10 UTC) | 29 | C++ | DuckDB Extension for cryptographic hash functions and HMAC |
| 42 | [curl_httpfs](https://duckdb.org/community_extensions/extensions/curl_httpfs.html) | [duckdb-curl-filesystem](https://github.com/dentiny/duckdb-curl-filesystem) | 🟢 Ongoing | 2 - ✅ Active | 29 days ago (2026-06-22 05:55:58 UTC) | 10 | C++ | Filesystem built upon libcurl. |
| 43 | [cwiqduck](https://duckdb.org/community_extensions/extensions/cwiqduck.html) | [cwiqduck](https://github.com/cwiq-os/cwiqduck) | 🟢 Ongoing | 3 - 🟡 Stable | 33 days ago (2026-06-18 04:35:52 UTC) | 3 | C++ | DuckDB extensions for CWIQ |
| 44 | [dash](https://duckdb.org/community_extensions/extensions/dash.html) | [dash](https://github.com/gropaul/dash) | 🟢 Ongoing | 1 - 🔥 Very Active | 6 days ago (2026-07-14 14:51:09 UTC) | 75 | C++ | Local GUI and Data Canvas as a DuckDB extension |
| 45 | [datadog](https://duckdb.org/community_extensions/extensions/datadog.html) | [duckdb-datadog](https://github.com/smithclay/duckdb-datadog) | 🟢 Ongoing | 1 - 🔥 Very Active | 5 days ago (2026-07-16 05:07:54 UTC) | 2 | C++ | ingest logs (and soon metrics and traces) from datadog into duckdb |
| 46 | [datasketches](https://duckdb.org/community_extensions/extensions/datasketches.html) | [datasketches](https://github.com/Query-farm/datasketches) | 🟢 Ongoing | 2 - ✅ Active | 14 days ago (2026-07-06 20:29:05 UTC) | 47 | C++ | Integrates DuckDB with the high-performance Apache DataSketches library. This... |
| 47 | [dazzleduck](https://duckdb.org/community_extensions/extensions/dazzleduck.html) | [dazzleduck-sql-duckdb](https://github.com/dazzleduck-web/dazzleduck-sql-duckdb) | ❓ Unknown | 4 - 🟠 Stale | 130 days ago (2026-03-12 22:24:42 UTC) | 1 | C++ | DuckDB extension: dazzleduck by dazzleduck-web |
| 48 | [dbn](https://duckdb.org/community_extensions/extensions/dbn.html) | [duckdb-dbn](https://github.com/tbeason/duckdb-dbn) | 🟢 Ongoing | 3 - 🟡 Stable | 41 days ago (2026-06-09 19:42:19 UTC) | 1 | C++ | DuckDB extension for reading Databento Binary Encoding (DBN) files |
| 49 | [decimal_arithmetic](https://duckdb.org/community_extensions/extensions/decimal_arithmetic.html) | [duckdb-decimal-arithmetic](https://github.com/duckdb/duckdb-decimal-arithmetic) | 🟢 Ongoing | 2 - ✅ Active | 11 days ago (2026-07-09 10:55:37 UTC) | 4 | C++ | DuckDB extension: decimal_arithmetic |
| 50 | [deferred_columns](https://duckdb.org/community_extensions/extensions/deferred_columns.html) | [deferred-columns](https://github.com/iwinalbert/deferred-columns) | 🟢 Ongoing | 2 - ✅ Active | 8 days ago (2026-07-12 17:08:25 UTC) | 2 | C++ | DuckDB extension: deferred_columns by iwinalbert |
| 51 | [delta_classic](https://duckdb.org/community_extensions/extensions/delta_classic.html) | [delta_classic](https://github.com/djouallah/delta_classic) | 🟢 Ongoing | 3 - 🟡 Stable | 31 days ago (2026-06-19 15:04:33 UTC) | 5 | C++ | DuckDB extension to attach a directory of Delta tables as a database |
| 52 | [delta_export](https://duckdb.org/community_extensions/extensions/delta_export.html) | [delta_export](https://github.com/djouallah/delta_export) | 🟢 Ongoing | 4 - 🟠 Stale | 130 days ago (2026-03-13 07:02:40 UTC) | 7 | C++ | DuckDB extension to export Delta Lake metadata from DuckLake |
| 53 | [dicom](https://duckdb.org/community_extensions/extensions/dicom.html) | [duck-dicom](https://github.com/nmontesg/duck-dicom) | 🟢 Ongoing | 1 - 🔥 Very Active | 6 days ago (2026-07-14 13:47:47 UTC) | 0 | C++ | A DuckDB extension to import medical imaging data |
| 54 | [dns](https://duckdb.org/community_extensions/extensions/dns.html) | [duckdb-dns](https://github.com/tobilg/duckdb-dns) | 🟢 Ongoing | 2 - ✅ Active | 23 days ago (2026-06-27 14:09:48 UTC) | 16 | Rust | DNS (Reverse) Lookup Extension for DuckDB |
| 55 | [dplyr](https://duckdb.org/community_extensions/extensions/dplyr.html) | [libdplyr](https://github.com/mrchypark/libdplyr) | 🟢 Ongoing | 1 - 🔥 Very Active | 6 days ago (2026-07-14 14:31:49 UTC) | 15 | Rust | DuckDB extension: dplyr by mrchypark |
| 56 | [dqtest](https://duckdb.org/community_extensions/extensions/dqtest.html) | [duckdb-dataquality-extension](https://github.com/vhe74/duckdb-dataquality-extension) | 🟢 Ongoing | 4 - 🟠 Stale | 167 days ago (2026-02-03 18:35:04 UTC) | 5 | C++ | Duckdb extension to run data quality tests |
| 57 | [dryrun](https://duckdb.org/community_extensions/extensions/dryrun.html) | [duckdb-dryrun](https://github.com/aleda145/duckdb-dryrun) | 🟢 Ongoing | 2 - ✅ Active | 29 days ago (2026-06-21 19:06:20 UTC) | 0 | C++ | dry run before execute |
| 58 | [dta](https://duckdb.org/community_extensions/extensions/dta.html) | [duckdb-dta](https://github.com/codedthinking/duckdb-dta) | 🟢 Ongoing | 2 - ✅ Active | 10 days ago (2026-07-10 08:57:32 UTC) | 0 | C++ | DuckDB extension for reading and writing .dta files (formats 117-121) |
| 59 | [duck_block_utils](https://duckdb.org/community_extensions/extensions/duck_block_utils.html) | [duckdb_duck_block_utils](https://github.com/teaguesterling/duckdb_duck_block_utils) | 🟢 Ongoing | 1 - 🔥 Very Active | 6 days ago (2026-07-15 04:38:18 UTC) | 1 | C++ | A collection of utility functions to work with doc block-style structures and... |
| 60 | [duck_delta_share](https://duckdb.org/community_extensions/extensions/duck_delta_share.html) | [duck_delta_share](https://github.com/cwiq-os/duck_delta_share) | 🟢 Ongoing | 3 - 🟡 Stable | 71 days ago (2026-05-10 23:39:27 UTC) | 5 | C++ | DuckDB extension for enabling Delta Sharing client capabilities.  |
| 61 | [duck_dggs](https://duckdb.org/community_extensions/extensions/duck_dggs.html) | [duckdb-dggs](https://github.com/am2222/duckdb-dggs) | 🟢 Ongoing | 2 - ✅ Active | 24 days ago (2026-06-26 20:37:37 UTC) | 1 | C++ | A DuckDB extension for discrete global grid systems (DGGS) powered by DGGRID v8. |
| 62 | [duck_diff](https://duckdb.org/community_extensions/extensions/duck_diff.html) | [duck_diff](https://github.com/avaitla/duck_diff) | 🟢 Ongoing | 3 - 🟡 Stable | 33 days ago (2026-06-17 13:19:07 UTC) | 5 | C++ | DuckDB extension: duck_diff by avaitla |
| 63 | [duck_geoarrow](https://duckdb.org/community_extensions/extensions/duck_geoarrow.html) | [duck_geoarrow](https://github.com/am2222/duck_geoarrow) | 🟢 Ongoing | 4 - 🟠 Stale | 96 days ago (2026-04-15 13:13:55 UTC) | 7 | C++ | This extension, Duck_Geoarrow, provides functions to convert between WKB (Wel... |
| 64 | [duck_hunt](https://duckdb.org/community_extensions/extensions/duck_hunt.html) | [duck_hunt](https://github.com/teaguesterling/duck_hunt) | 🟢 Ongoing | 2 - ✅ Active | 11 days ago (2026-07-10 03:06:12 UTC) | 4 | C++ | Tools for working with unit test suite results |
| 65 | [duck_lineage](https://duckdb.org/community_extensions/extensions/duck_lineage.html) | [duck_lineage](https://github.com/ilum-cloud/duck_lineage) | 🟢 Ongoing | 3 - 🟡 Stable | 55 days ago (2026-05-26 23:21:55 UTC) | 78 | Python | A extension for DuckDB, which captures lineage events for executed queries |
| 66 | [duck_lk](https://duckdb.org/community_extensions/extensions/duck_lk.html) | [duck-lk](https://github.com/nrminor/duck-lk) | 🟢 Ongoing | 4 - 🟠 Stale | 94 days ago (2026-04-18 03:05:52 UTC) | 0 | Rust | Interact with tables from your LabKey LIMS natively in DuckDB |
| 67 | [duck_tails](https://duckdb.org/community_extensions/extensions/duck_tails.html) | [duck_tails](https://github.com/teaguesterling/duck_tails) | 🟢 Ongoing | 2 - ✅ Active | 11 days ago (2026-07-09 17:05:02 UTC) | 19 | C++ | A DuckDB extension for exploring and reading git history. |
| 68 | [duckdb_delta_sharing](https://duckdb.org/community_extensions/extensions/duckdb_delta_sharing.html) | [duckdb-delta-sharing](https://github.com/prequel-co/duckdb-delta-sharing) | 🟢 Ongoing | 2 - ✅ Active | 20 days ago (2026-06-30 17:34:12 UTC) | 3 | C++ | An extension for using DuckDB as a delta sharing client |
| 69 | [duckdb_geoip_rs](https://duckdb.org/community_extensions/extensions/duckdb_geoip_rs.html) | [duckdb-geoip-rs](https://github.com/william-billaud/duckdb-geoip-rs) | 🟢 Ongoing | 2 - ✅ Active | 23 days ago (2026-06-27 17:37:35 UTC) | 6 | Rust | Database connectivity extension by william-billaud |
| 70 | [duckdb_mcp](https://duckdb.org/community_extensions/extensions/duckdb_mcp.html) | [duckdb_mcp](https://github.com/teaguesterling/duckdb_mcp) | 🟢 Ongoing | 2 - ✅ Active | 12 days ago (2026-07-08 14:44:52 UTC) | 60 | C++ | A simple MCP server extension for DuckDB |
| 71 | [duckdb_midi](https://github.com/nkwork9999/duckdb-midi) | [duckdb-midi](https://github.com/nkwork9999/duckdb-midi) | ❓ Unknown | 3 - 🟡 Stable | 38 days ago (2026-06-12 12:18:36 UTC) | 0 | C++ | Database connectivity extension by nkwork9999 |
| 72 | [duckdb_opendalfs](https://github.com/dentiny/duckdb-opendal-filesystem) | [duckdb-opendal-filesystem](https://github.com/dentiny/duckdb-opendal-filesystem) | ❓ Unknown | 1 - 🔥 Very Active | today (2026-07-20 07:09:05 UTC) | 2 | C++ | Database connectivity extension by dentiny |
| 73 | [duckdbi](https://duckdb.org/community_extensions/extensions/duckdbi.html) | [DuckDBI](https://github.com/nkwork9999/DuckDBI) | 🟢 Ongoing | 4 - 🟠 Stale | 128 days ago (2026-03-14 11:04:19 UTC) | 4 | C++ | Database connectivity extension by nkwork9999 |
| 74 | [duckgl](https://duckdb.org/community_extensions/extensions/duckgl.html) | [duckgl](https://github.com/nkwork9999/duckgl) | 🟢 Ongoing | 4 - 🟠 Stale | 138 days ago (2026-03-04 16:41:20 UTC) | 7 | C++ | DuckDB extension: duckgl by nkwork9999 |
| 75 | [duckherder](https://duckdb.org/community_extensions/extensions/duckherder.html) | [duckdb-distributed-execution](https://github.com/dentiny/duckdb-distributed-execution) | ❓ Unknown | 4 - 🟠 Stale | 132 days ago (2026-03-10 09:36:00 UTC) | 59 | C++ | Distributed execution for duckdb queries. |
| 76 | [duckhog](https://duckdb.org/community_extensions/extensions/duckhog.html) | [duckhog](https://github.com/PostHog/duckhog) | ❓ Unknown | 2 - ✅ Active | 25 days ago (2026-06-26 00:52:18 UTC) | 10 | C++ | duckdb extension to connect to posthog managed data warehouse  |
| 77 | [duckhts](https://duckdb.org/community_extensions/extensions/duckhts.html) | [duckhts](https://github.com/RGenomicsETL/duckhts) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-07-21 08:16:49 UTC) | 16 | C | 'htslib' based 'Duckdb' Extenstion for High Throughput Sequencing File Formats |
| 78 | [ducklake_cdc](https://duckdb.org/community_extensions/extensions/ducklake_cdc.html) | [ducklake-cdc-extension](https://github.com/ekkuleivonen/ducklake-cdc-extension) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-07-21 04:28:11 UTC) | 15 | C++ | The missing operational layer for DuckLake’s change feed. |
| 79 | [ducklink](https://duckdb.org/community_extensions/extensions/ducklink.html) | [ducklink-extension](https://github.com/tegmentum/ducklink-extension) | 🟢 Ongoing | 1 - 🔥 Very Active | 2 days ago (2026-07-18 14:41:02 UTC) | 2 | Rust | Run duckdb:extension WebAssembly components inside DuckDB (community extension) |
| 80 | [ducknng](https://github.com/sounkou-bioinfo/ducknng) | [ducknng](https://github.com/sounkou-bioinfo/ducknng) | ❓ Unknown | 2 - ✅ Active | 11 days ago (2026-07-10 05:29:17 UTC) | 3 | C | ducknng: a 'DuckDB' Binding To The 'NNG' Scalability Protocols Library And an... |
| 81 | [duckorch](https://duckdb.org/community_extensions/extensions/duckorch.html) | [duck-orch](https://github.com/nkwork9999/duck-orch) | 🟢 Ongoing | 3 - 🟡 Stable | 36 days ago (2026-06-14 11:27:19 UTC) | 2 | Rust | DuckDB extension: duckorch by nkwork9999 |
| 82 | [duckpgq](https://duckdb.org/community_extensions/extensions/duckpgq.html) | [duckpgq-extension](https://github.com/cwida/duckpgq-extension) | 🟢 Ongoing | 1 - 🔥 Very Active | 6 days ago (2026-07-14 12:53:24 UTC) | 439 | C++ | DuckDB extension that adds support for SQL/PGQ and graph algorithms |
| 83 | [ducksmiles](https://duckdb.org/community_extensions/extensions/ducksmiles.html) | [duckSMILES](https://github.com/nkwork9999/duckSMILES) | 🟢 Ongoing | 3 - 🟡 Stable | 37 days ago (2026-06-14 04:01:17 UTC) | 3 | Rust | DuckDB extension: ducksmiles by nkwork9999 |
| 84 | [ducksync](https://duckdb.org/community_extensions/extensions/ducksync.html) | [ducksync](https://github.com/danjsiegel/ducksync) | 🟢 Ongoing | 1 - 🔥 Very Active | 2 days ago (2026-07-18 14:20:56 UTC) | 7 | C++ | DuckDB extension: ducksync by danjsiegel |
| 85 | [duckthink](https://duckdb.org/community_extensions/extensions/duckthink.html) | [duckthink](https://github.com/pedro-filardi/duckthink) | 🟢 Ongoing | 2 - ✅ Active | 14 days ago (2026-07-06 15:22:58 UTC) | 0 | C++ | ASK() — natural-language SQL for DuckDB, grounded in your dbt Semantic Layer |
| 86 | [ducktinycc](https://duckdb.org/community_extensions/extensions/ducktinycc.html) | [DuckTinyCC](https://github.com/sounkou-bioinfo/DuckTinyCC) | 🟢 Ongoing | 3 - 🟡 Stable | 69 days ago (2026-05-13 06:09:08 UTC) | 3 | C | 'C' Scripting in 'Duckdb' using 'TinyCC' |
| 87 | [duckton](https://duckdb.org/community_extensions/extensions/duckton.html) | [duckton](https://github.com/Angelerator/duckton) | 🟢 Ongoing | 2 - ✅ Active | 25 days ago (2026-06-25 22:07:12 UTC) | 5 | Rust | Duckton — a peer-to-peer distributed DuckDB compute grid over QUIC: broadcast... |
| 88 | [eeagrid](https://duckdb.org/community_extensions/extensions/eeagrid.html) | [duckdb-eeagrid](https://github.com/ahuarte47/duckdb-eeagrid) | 🟢 Ongoing | 3 - 🟡 Stable | 32 days ago (2026-06-18 21:26:30 UTC) | 0 | C++ | Functions for transforming XY coordinates to and from the EEA Reference Grid... |
| 89 | [eenddb](https://duckdb.org/community_extensions/extensions/eenddb.html) | [eenddb](https://github.com/Dtenwolde/eenddb) | 🟢 Ongoing | 4 - 🟠 Stale | 111 days ago (2026-03-31 09:31:58 UTC) | 5 | C++ | Database connectivity extension by Dtenwolde |
| 90 | [elasticsearch](https://duckdb.org/community_extensions/extensions/elasticsearch.html) | [duckdb-elasticsearch](https://github.com/tlinhart/duckdb-elasticsearch) | ❓ Unknown | 3 - 🟡 Stable | 82 days ago (2026-04-29 13:01:51 UTC) | 21 | C++ | Query Elasticsearch data directly from DuckDB |
| 91 | [erpl_idoc](https://duckdb.org/community_extensions/extensions/erpl_idoc.html) | [erpl-idoc](https://github.com/DataZooDE/erpl-idoc) | 🟢 Ongoing | 1 - 🔥 Very Active | 2 days ago (2026-07-18 16:21:04 UTC) | 2 | C++ | Read & write SAP IDoc files (flat + IDoc-XML) as SQL in DuckDB — a community... |
| 92 | [erpl_web](https://duckdb.org/community_extensions/extensions/erpl_web.html) | [erpl-web](https://github.com/DataZooDE/erpl-web) | 🟢 Ongoing | 1 - 🔥 Very Active | 2 days ago (2026-07-18 16:27:52 UTC) | 28 | C++ | ERPL is a DuckDB extension to connect to API based ecosystems via standard in... |
| 93 | [eurostat](https://duckdb.org/community_extensions/extensions/eurostat.html) | [duckdb-eurostat](https://github.com/ahuarte47/duckdb-eurostat) | 🟢 Ongoing | 2 - ✅ Active | 8 days ago (2026-07-12 10:29:36 UTC) | 32 | C++ | DuckDB extension for reading data from EUROSTAT database using SQL  |
| 94 | [evalexpr_rhai](https://duckdb.org/community_extensions/extensions/evalexpr_rhai.html) | [evalexpr_rhai](https://github.com/Query-farm/evalexpr_rhai) | 🟢 Ongoing | 3 - 🟡 Stable | 89 days ago (2026-04-23 01:40:35 UTC) | 26 | C++ | A DuckDB extension to evaluate the Rhai scripting language as part of SQL. |
| 95 | [events](https://duckdb.org/community_extensions/extensions/events.html) | [events](https://github.com/Query-farm/events) | 🟢 Ongoing | 4 - 🟠 Stale | 96 days ago (2026-04-15 12:59:21 UTC) | 3 | C++ | Capture database events and deliver JSON notifications to external programs v... |
| 96 | [faiss](https://duckdb.org/community_extensions/extensions/faiss.html) | [duckdb-faiss-ext](https://github.com/duckdb-faiss-ext/duckdb-faiss-ext) | ❓ Unknown | 4 - 🟠 Stale | 133 days ago (2026-03-09 11:54:02 UTC) | 31 | Go | DuckDB wrapper for FAISS - Experimental |
| 97 | [fakeit](https://duckdb.org/community_extensions/extensions/fakeit.html) | [duckdb-fakeit](https://github.com/tobilg/duckdb-fakeit) | 🟢 Ongoing | 2 - ✅ Active | 23 days ago (2026-06-27 13:59:35 UTC) | 15 | Rust | DuckDB extension: fakeit by tobilg |
| 98 | [file_dialog](https://duckdb.org/community_extensions/extensions/file_dialog.html) | [duckdb-ext-file-dialog](https://github.com/yutannihilation/duckdb-ext-file-dialog) | ❓ Unknown | 2 - ✅ Active | 28 days ago (2026-06-22 11:44:00 UTC) | 15 | Rust | A DuckDB extension to choose file interactively using native file open dialogs |
| 99 | [finance](https://duckdb.org/community_extensions/extensions/finance.html) | [duckdb-finance](https://github.com/leonardovida/duckdb-finance) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-07-19 09:21:15 UTC) | 5 | C++ | SQL-native quant finance for DuckDB |
| 100 | [finetype](https://duckdb.org/community_extensions/extensions/finetype.html) | [finetype](https://github.com/meridian-online/finetype) | 🟢 Ongoing | 1 - 🔥 Very Active | 2 days ago (2026-07-19 00:39:08 UTC) | 2 | Rust | 👓 Precision format detection for text data. Semantic type inference with tran... |
| 101 | [fire_duck_ext](https://duckdb.org/community_extensions/extensions/fire_duck_ext.html) | [fire_duck_ext](https://github.com/BorisBesky/fire_duck_ext) | 🟢 Ongoing | 2 - ✅ Active | 22 days ago (2026-06-29 05:40:05 UTC) | 3 | C++ | duckdb extension for firestore |
| 102 | [firebird](https://duckdb.org/community_extensions/extensions/firebird.html) | [duckdb-firebird](https://github.com/flozer/duckdb-firebird) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-07-20 19:04:27 UTC) | 4 | C++ | DuckDB extension: firebird by flozer |
| 103 | [fit](https://duckdb.org/community_extensions/extensions/fit.html) | [duckdb-fit-extension](https://github.com/antoriche/duckdb-fit-extension) | 🟢 Ongoing | 4 - 🟠 Stale | 217 days ago (2025-12-15 19:16:40 UTC) | 3 | C++ | DuckDB extension: fit by antoriche |
| 104 | [fivetran](https://duckdb.org/community_extensions/extensions/fivetran.html) | [duckdb_sparse_variant](https://github.com/fivetran/duckdb_sparse_variant) | 🟢 Ongoing | 3 - 🟡 Stable | 63 days ago (2026-05-19 07:42:06 UTC) | 0 | C++ | A DuckDB extension providing sparse VARIANT encoding for STRUCTs and an optim... |
| 105 | [flock](https://duckdb.org/community_extensions/extensions/flock.html) | [flock](https://github.com/dais-polymtl/flock) | 🟢 Ongoing | 1 - 🔥 Very Active | 5 days ago (2026-07-15 15:16:41 UTC) | 350 | C++ | Beyond Quacking: Deep Integration of Language Models and RAG into DuckDB (VLD... |
| 106 | [fsquery](https://duckdb.org/community_extensions/extensions/fsquery.html) | [fsquery](https://github.com/halgari/fsquery) | 🟢 Ongoing | 4 - 🟠 Stale | 126 days ago (2026-03-16 16:09:24 UTC) | 1 | C++ | An extension that allows DuckDB to enumerate and stat files on the disk |
| 107 | [func_apply](https://duckdb.org/community_extensions/extensions/func_apply.html) | [duckdb_func_apply](https://github.com/teaguesterling/duckdb_func_apply) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-07-19 20:51:43 UTC) | 3 | C++ | An exension to allow dynamic function application |
| 108 | [fuzzycomplete](https://duckdb.org/community_extensions/extensions/fuzzycomplete.html) | [fuzzycomplete](https://github.com/Query-farm/fuzzycomplete) | 🟢 Ongoing | 4 - 🟠 Stale | 113 days ago (2026-03-29 21:04:37 UTC) | 28 | C++ | DuckDB Extension for fuzzy string matching based autocompletion |
| 109 | [gaggle](https://duckdb.org/community_extensions/extensions/gaggle.html) | [gaggle](https://github.com/CogitatorTech/gaggle) | 🟢 Ongoing | 2 - ✅ Active | 11 days ago (2026-07-09 12:19:44 UTC) | 17 | Rust | A DuckDB extension for working with Kaggle datasets |
| 110 | [gcs](https://duckdb.org/community_extensions/extensions/gcs.html) | [duckdb-gcs](https://github.com/northpolesec/duckdb-gcs) | 🟢 Ongoing | 1 - 🔥 Very Active | 6 days ago (2026-07-14 13:46:44 UTC) | 25 | C++ | A GCS-native extension for DuckDB |
| 111 | [gdx](https://duckdb.org/community_extensions/extensions/gdx.html) | [duckdb-gdx](https://github.com/chrispahm/duckdb-gdx) | ❓ Unknown | 2 - ✅ Active | 15 days ago (2026-07-05 19:28:29 UTC) | 1 | C++ | DuckDB extension: gdx by chrispahm |
| 112 | [geography](https://duckdb.org/community_extensions/extensions/geography.html) | [duckdb-geography](https://github.com/paleolimbot/duckdb-geography) | ❓ Unknown | 4 - 🟠 Stale | 130 days ago (2026-03-12 16:05:00 UTC) | 46 | C++ | Geospatial data extension by paleolimbot |
| 113 | [geosilo](https://duckdb.org/community_extensions/extensions/geosilo.html) | [geosilo](https://github.com/Query-farm/geosilo) | 🟢 Ongoing | 3 - 🟡 Stable | 84 days ago (2026-04-27 16:21:07 UTC) | 25 | C++ | DuckDB extension for compact geometry encoding using delta-encoded coordinate... |
| 114 | [geotiff](https://duckdb.org/community_extensions/extensions/geotiff.html) | [duckdb-geotiff](https://github.com/babaknaimi/duckdb-geotiff) | ❓ Unknown | 4 - 🟠 Stale | 335 days ago (2025-08-20 05:12:15 UTC) | 2 | C++ | Duckdb extension to read GeoTiffs directly with duckdb database |
| 115 | [ggsql](https://duckdb.org/community_extensions/extensions/ggsql.html) | [ggsql-duckdb](https://github.com/posit-dev/ggsql-duckdb) | 🟢 Ongoing | 2 - ✅ Active | 28 days ago (2026-06-23 06:14:05 UTC) | 24 | Rust | A DuckDB extension adding support for ggsql  |
| 116 | [gh](https://duckdb.org/community_extensions/extensions/gh.html) | [duckdb-gh](https://github.com/carlopi/duckdb-gh) | 🟢 Ongoing | 3 - 🟡 Stable | 82 days ago (2026-04-29 14:21:02 UTC) | 4 | C++ | DuckDB extension: gh by carlopi |
| 117 | [gorz](https://duckdb.org/community_extensions/extensions/gorz.html) | [duckdb-gorz](https://github.com/gorfather/duckdb-gorz) | 🟢 Ongoing | 1 - 🔥 Very Active | 6 days ago (2026-07-14 12:35:33 UTC) | 0 | C++ | DuckDB extension: read/write GORpipe .gorz / .gord genomic files as native ta... |
| 118 | [gsheets](https://duckdb.org/community_extensions/extensions/gsheets.html) | [duckdb_gsheets](https://github.com/evidence-dev/duckdb_gsheets) | 🟢 Ongoing | 4 - 🟠 Stale | 150 days ago (2026-02-21 04:11:04 UTC) | 346 | C++ | DuckDB extension to read and write Google Sheets using SQL |
| 119 | [h3](https://duckdb.org/community_extensions/extensions/h3.html) | [h3-duckdb](https://github.com/isaacbrodsky/h3-duckdb) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-07-21 06:12:57 UTC) | 249 | C++ | Bindings for H3 to DuckDB |
| 120 | [h5db](https://duckdb.org/community_extensions/extensions/h5db.html) | [h5db](https://github.com/jokasimr/h5db) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-07-19 09:44:22 UTC) | 3 | C++ | Duckdb extension for reading HDF5 files. |
| 121 | [harbor](https://duckdb.org/community_extensions/extensions/harbor.html) | [duckdb-harbor](https://github.com/shreeve/duckdb-harbor) | 🟢 Ongoing | 1 - 🔥 Very Active | 2 days ago (2026-07-18 10:03:55 UTC) | 0 | C++ | HTTP server for DuckDB UI, JSON /sql, and CLI |
| 122 | [hashfuncs](https://duckdb.org/community_extensions/extensions/hashfuncs.html) | [hashfuncs](https://github.com/Query-farm/hashfuncs) | 🟢 Ongoing | 3 - 🟡 Stable | 37 days ago (2026-06-13 16:28:43 UTC) | 12 | C++ | A DuckDB extension that supplies non-cryptographic hash functions. |
| 123 | [hdf5](https://duckdb.org/community_extensions/extensions/hdf5.html) | [duckdb-hdf5](https://github.com/Berrysoft/duckdb-hdf5) | ❓ Unknown | 3 - 🟡 Stable | 89 days ago (2026-04-23 01:30:36 UTC) | 12 | Rust | HDF5 plugin for duckdb |
| 124 | [hdfs](https://duckdb.org/community_extensions/extensions/hdfs.html) | [duckdb-hdfs](https://github.com/casperhart/duckdb-hdfs) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-07-21 01:26:22 UTC) | 0 | Rust | DuckDB extension: hdfs by casperhart |
| 125 | [hedged_request_fs](https://duckdb.org/community_extensions/extensions/hedged_request_fs.html) | [duckdb-hedged-request](https://github.com/dentiny/duckdb-hedged-request) | 🟢 Ongoing | 2 - ✅ Active | 29 days ago (2026-06-22 06:09:39 UTC) | 1 | C++ | DuckDB extension: hedged_request_fs by dentiny |
| 126 | [highs](https://duckdb.org/community_extensions/extensions/highs.html) | [HiGHS-duckdb](https://github.com/fhk/HiGHS-duckdb) | ❓ Unknown | 4 - 🟠 Stale | 146 days ago (2026-02-25 02:07:48 UTC) | 1 | C++ | Run the solver in the database! |
| 127 | [hive_metastore](https://duckdb.org/community_extensions/extensions/hive_metastore.html) | [duckdb-hive-metastore](https://github.com/ilum-cloud/duckdb-hive-metastore) | 🟢 Ongoing | 3 - 🟡 Stable | 59 days ago (2026-05-22 17:49:59 UTC) | 4 | C++ | DuckDB extension allowing to connect to Apache Hive Metastore and query the d... |
| 128 | [hnsw_acorn](https://duckdb.org/community_extensions/extensions/hnsw_acorn.html) | [duckdb-hnsw-acorn](https://github.com/cigrainger/duckdb-hnsw-acorn) | 🟢 Ongoing | 4 - 🟠 Stale | 115 days ago (2026-03-28 07:49:47 UTC) | 64 | C++ | ACORN-1 pre-filtered HNSW search for DuckDB |
| 129 | [holtfs](https://duckdb.org/community_extensions/extensions/holtfs.html) | [duckdb-holtfs](https://github.com/feichai0017/duckdb-holtfs) | 🟢 Ongoing | 3 - 🟡 Stable | 55 days ago (2026-05-27 06:55:19 UTC) | 0 | C++ | DuckDB extension for planning scans through Holt-backed metadata indexes |
| 130 | [hostfs](https://duckdb.org/community_extensions/extensions/hostfs.html) | [hostFS](https://github.com/gropaul/hostFS) | ❓ Unknown | 4 - 🟠 Stale | 292 days ago (2025-10-01 21:02:13 UTC) | 31 | C++ | DuckDB extension: hostfs by gropaul |
| 131 | [html_query](https://duckdb.org/community_extensions/extensions/html_query.html) | [duckdb_html_query](https://github.com/midwork-finds-jobs/duckdb_html_query) | ❓ Unknown | 4 - 🟠 Stale | 165 days ago (2026-02-05 15:33:13 UTC) | 2 | Rust | Filter HTML inside duckdb |
| 132 | [html_readability](https://duckdb.org/community_extensions/extensions/html_readability.html) | [duckdb-html-readability](https://github.com/midwork-finds-jobs/duckdb-html-readability) | ❓ Unknown | 4 - 🟠 Stale | 165 days ago (2026-02-05 15:33:16 UTC) | 0 | Rust | DuckDB extension to parse html to readable text |
| 133 | [http_client](https://duckdb.org/community_extensions/extensions/http_client.html) | [httpclient](https://github.com/Query-farm/httpclient) | 🟢 Ongoing | 4 - 🟠 Stale | 96 days ago (2026-04-15 14:08:54 UTC) | 80 | C++ | DuckDB HTTP GET/POST Client in a Community Extension |
| 134 | [http_request](https://duckdb.org/community_extensions/extensions/http_request.html) | [duckdb_http_request](https://github.com/midwork-finds-jobs/duckdb_http_request) | ❓ Unknown | 4 - 🟠 Stale | 153 days ago (2026-02-17 13:03:03 UTC) | 4 | C++ | Uses the native duckdb httputil to make extra requests in SELECT |
| 135 | [http_stats](https://duckdb.org/community_extensions/extensions/http_stats.html) | [duckdb-http-stats](https://github.com/tlinhart/duckdb-http-stats) | 🟢 Ongoing | 4 - 🟠 Stale | 115 days ago (2026-03-27 13:58:03 UTC) | 1 | C++ | Better HTTP statistics for DuckDB |
| 136 | [httpd_log](https://duckdb.org/community_extensions/extensions/httpd_log.html) | [duckdb-httpd-log](https://github.com/saygox/duckdb-httpd-log) | ❓ Unknown | 4 - 🟠 Stale | 190 days ago (2026-01-12 06:14:58 UTC) | 0 | C++ | duckdb extension |
| 137 | [httpfs_timeout_retry](https://duckdb.org/community_extensions/extensions/httpfs_timeout_retry.html) | [duckdb-httpfs-timeout-retry](https://github.com/dentiny/duckdb-httpfs-timeout-retry) | 🟢 Ongoing | 2 - ✅ Active | 29 days ago (2026-06-22 06:44:26 UTC) | 0 | C++ | Web/HTTP functionality extension by dentiny |
| 138 | [httpserver](https://duckdb.org/community_extensions/extensions/httpserver.html) | [httpserver](https://github.com/Query-farm/httpserver) | 🟢 Ongoing | 2 - ✅ Active | 13 days ago (2026-07-07 18:42:03 UTC) | 284 | C++ | DuckDB HTTP API Server and Query Interface in a  Community Extension |
| 139 | [infera](https://duckdb.org/community_extensions/extensions/infera.html) | [infera](https://github.com/CogitatorTech/infera) | 🟢 Ongoing | 2 - ✅ Active | 12 days ago (2026-07-09 07:40:25 UTC) | 133 | Rust | A DuckDB extension for in-database inference |
| 140 | [inflector](https://duckdb.org/community_extensions/extensions/inflector.html) | [inflector](https://github.com/Query-farm/inflector) | 🟢 Ongoing | 3 - 🟡 Stable | 60 days ago (2026-05-21 12:33:21 UTC) | 8 | C++ | Powerful string case transformation and inflection capabilities directly to y... |
| 141 | [ion](https://duckdb.org/community_extensions/extensions/ion.html) | [duckdb-ion](https://github.com/kestra-io/duckdb-ion) | 🟢 Ongoing | 4 - 🟠 Stale | 132 days ago (2026-03-10 15:49:39 UTC) | 4 | C++ | AWS Ion extension for DuckDB |
| 142 | [json_schema](https://duckdb.org/community_extensions/extensions/json_schema.html) | [json_schema](https://github.com/Query-farm/json_schema) | 🟢 Ongoing | 3 - 🟡 Stable | 37 days ago (2026-06-13 19:24:53 UTC) | 3 | C++ | A DuckDB extension that bring support for validating JSON data using JSON sch... |
| 143 | [jsonata](https://duckdb.org/community_extensions/extensions/jsonata.html) | [jsonata](https://github.com/Query-farm/jsonata) | 🟢 Ongoing | 3 - 🟡 Stable | 35 days ago (2026-06-15 15:43:11 UTC) | 6 | C++ | The JSONata extension for DuckDB enables expressive, JSON-focused querying an... |
| 144 | [jwt](https://duckdb.org/community_extensions/extensions/jwt.html) | [duckdb_jwt](https://github.com/GalvinGao/duckdb_jwt) | ❓ Unknown | 4 - 🟠 Stale | over a year ago (2025-07-09 00:13:56 UTC) | 0 | C++ | DuckDB extension: jwt by GalvinGao |
| 145 | [keboola](https://duckdb.org/community_extensions/extensions/keboola.html) | [duckdb-extension](https://github.com/keboola/duckdb-extension) | 🟢 Ongoing | 2 - ✅ Active | 12 days ago (2026-07-08 11:43:04 UTC) | 0 | C++ | DuckDB extension for Keboola Storage — query and write Keboola tables using s... |
| 146 | [lastra](https://duckdb.org/community_extensions/extensions/lastra.html) | [duckdb-lastra](https://github.com/QTSurfer/duckdb-lastra) | 🟢 Ongoing | 3 - 🟡 Stable | 70 days ago (2026-05-11 12:15:36 UTC) | 0 | C++ | DuckDB extension for reading Lastra columnar time series files natively |
| 147 | [latency_injection_fs](https://duckdb.org/community_extensions/extensions/latency_injection_fs.html) | [duckdb-filesystem-latency-injection](https://github.com/dentiny/duckdb-filesystem-latency-injection) | 🟢 Ongoing | 2 - ✅ Active | 29 days ago (2026-06-22 06:39:42 UTC) | 0 | C++ | DuckDB extension: latency_injection_fs by dentiny |
| 148 | [laterite_ags4](https://duckdb.org/community_extensions/extensions/laterite_ags4.html) | [laterite-duckdb](https://github.com/niko86/laterite-duckdb) | 🟢 Ongoing | 1 - 🔥 Very Active | 4 days ago (2026-07-16 09:36:11 UTC) | 0 | Rust | DuckDB extension: laterite_ags4 by niko86 |
| 149 | [ldbc_data_gen](https://duckdb.org/community_extensions/extensions/ldbc_data_gen.html) | [ldbc-data-gen](https://github.com/Dtenwolde/ldbc-data-gen) | 🟢 Ongoing | 1 - 🔥 Very Active | 4 days ago (2026-07-16 14:20:37 UTC) | 0 | C++ | Database connectivity extension by Dtenwolde |
| 150 | [level_pivot](https://duckdb.org/community_extensions/extensions/level_pivot.html) | [duckdb-level-pivot](https://github.com/halgari/duckdb-level-pivot) | 🟢 Ongoing | 3 - 🟡 Stable | 88 days ago (2026-04-23 16:05:04 UTC) | 0 | C++ | DuckDB extension: level_pivot by halgari |
| 151 | [lindel](https://duckdb.org/community_extensions/extensions/lindel.html) | [lindel](https://github.com/Query-farm/lindel) | 🟢 Ongoing | 3 - 🟡 Stable | 83 days ago (2026-04-28 20:32:34 UTC) | 66 | C++ | DuckDB Extension Linearization/Delinearization, Z-Order, Hilbert and Morton C... |
| 152 | [llm](https://duckdb.org/community_extensions/extensions/llm.html) | [duckdb-llm](https://github.com/midwork-finds-jobs/duckdb-llm) | 🟢 Ongoing | 4 - 🟠 Stale | 153 days ago (2026-02-17 14:09:08 UTC) | 3 | C++ | DuckDB extension: llm by midwork-finds-jobs |
| 153 | [loki](https://duckdb.org/community_extensions/extensions/loki.html) | [duckdb-loki](https://github.com/prochac/duckdb-loki) | 🟢 Ongoing | 2 - ✅ Active | 14 days ago (2026-07-06 19:54:26 UTC) | 0 | C++ | DuckDB extension: loki by prochac |
| 154 | [lpts](https://duckdb.org/community_extensions/extensions/lpts.html) | [lpts](https://github.com/cwida/lpts) | 🟢 Ongoing | 2 - ✅ Active | 12 days ago (2026-07-08 11:31:09 UTC) | 7 | C++ | Logical Plan To SQL DuckDB Extension |
| 155 | [lsh](https://duckdb.org/community_extensions/extensions/lsh.html) | [lsh](https://github.com/princeton-ddss/lsh) | ❓ Unknown | 4 - 🟠 Stale | 95 days ago (2026-04-16 17:00:45 UTC) | 14 | Rust | DuckDB community extension for locality-sensitive hashing (LSH) |
| 156 | [lttb](https://duckdb.org/community_extensions/extensions/lttb.html) | [duckdb-lttb](https://github.com/reformovo/duckdb-lttb) | 🟢 Ongoing | 2 - ✅ Active | 20 days ago (2026-07-01 07:47:53 UTC) | 2 | C++ | A simple lttb algorithm extension for DuckDB |
| 157 | [lua](https://duckdb.org/community_extensions/extensions/lua.html) | [duckdb-lua](https://github.com/isaacbrodsky/duckdb-lua) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-07-20 02:44:13 UTC) | 12 | C++ | DuckDB extension to evaluate Lua expressions. |
| 158 | [magic](https://duckdb.org/community_extensions/extensions/magic.html) | [duckdb-magic](https://github.com/carlopi/duckdb-magic) | 🟢 Ongoing | 2 - ✅ Active | 29 days ago (2026-06-22 07:17:42 UTC) | 8 | C++ | Auto-detect file types via `libmagic` (`file` utility) |
| 159 | [marisa](https://duckdb.org/community_extensions/extensions/marisa.html) | [marisa](https://github.com/Query-farm/marisa) | 🟢 Ongoing | 3 - 🟡 Stable | 37 days ago (2026-06-13 16:28:44 UTC) | 14 | C++ | The Marisa extension by Query.Farm integrates the fast, space-efficient MARIS... |
| 160 | [markdown](https://duckdb.org/community_extensions/extensions/markdown.html) | [duckdb_markdown](https://github.com/teaguesterling/duckdb_markdown) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-07-20 18:56:41 UTC) | 27 | C++ | Heirarchical markdown parsing for DuckDB |
| 161 | [maxmind](https://duckdb.org/community_extensions/extensions/maxmind.html) | [duckdb-maxmind](https://github.com/marselester/duckdb-maxmind) | 🟢 Ongoing | 2 - ✅ Active | 21 days ago (2026-06-29 21:07:08 UTC) | 7 | Zig | DuckDB MaxMind extension written in Zig. |
| 162 | [miint](https://duckdb.org/community_extensions/extensions/miint.html) | [duckdb-miint](https://github.com/the-miint/duckdb-miint) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-07-20 12:57:32 UTC) | 5 | C | DuckDB extension: miint by the-miint |
| 163 | [minijinja](https://duckdb.org/community_extensions/extensions/minijinja.html) | [minijinja](https://github.com/Query-farm/minijinja) | 🟢 Ongoing | 3 - 🟡 Stable | 37 days ago (2026-06-13 16:50:06 UTC) | 6 | C++ | DuckDB extension: minijinja |
| 164 | [miniplot](https://duckdb.org/community_extensions/extensions/miniplot.html) | [miniplot](https://github.com/nkwork9999/miniplot) | 🟢 Ongoing | 4 - 🟠 Stale | 248 days ago (2025-11-15 02:42:43 UTC) | 23 | C++ | DuckDB extension: miniplot by nkwork9999 |
| 165 | [mlpack](https://duckdb.org/community_extensions/extensions/mlpack.html) | [duckdb-mlpack](https://github.com/eddelbuettel/duckdb-mlpack) | 🟢 Ongoing | 1 - 🔥 Very Active | 7 days ago (2026-07-13 14:39:58 UTC) | 19 | C++ | Bringing mlpack to duckdb |
| 166 | [monetary](https://duckdb.org/community_extensions/extensions/monetary.html) | [monetary](https://github.com/fyffee/monetary) | ❓ Unknown | 4 - 🟠 Stale | 172 days ago (2026-01-29 11:29:01 UTC) | 0 | C++ | DuckDB extension: monetary by fyffee |
| 167 | [mongo](https://duckdb.org/community_extensions/extensions/mongo.html) | [duckdb-mongo](https://github.com/stephaniewang526/duckdb-mongo) | 🟢 Ongoing | 2 - ✅ Active | 10 days ago (2026-07-10 16:29:53 UTC) | 54 | C++ | Integrates DuckDB with MongoDB, enabling direct SQL queries over MongoDB coll... |
| 168 | [mooncake](https://duckdb.org/community_extensions/extensions/mooncake.html) | [duckdb_mooncake](https://github.com/Mooncake-Labs/duckdb_mooncake) | ❓ Unknown | 4 - 🟠 Stale | 268 days ago (2025-10-26 07:13:05 UTC) | 10 | C++ | Read Iceberg tables written by moonlink in real time |
| 169 | [mpduck](https://duckdb.org/community_extensions/extensions/mpduck.html) | [mpduck](https://github.com/MatthewMooreZA/mpduck) | 🟢 Ongoing | 4 - 🟠 Stale | 98 days ago (2026-04-13 17:59:29 UTC) | 1 | C++ | DuckDB extension to read and write Prophet model point files. |
| 170 | [msolap](https://duckdb.org/community_extensions/extensions/msolap.html) | [duckdb-msolap-extension](https://github.com/Hugoberry/duckdb-msolap-extension) | ❓ Unknown | 4 - 🟠 Stale | 299 days ago (2025-09-24 16:33:46 UTC) | 14 | C++ | DuckDB extension: msolap by Hugoberry |
| 171 | [mssql](https://duckdb.org/community_extensions/extensions/mssql.html) | [mssql-extension](https://github.com/hugr-lab/mssql-extension) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-07-20 13:33:31 UTC) | 122 | C++ | DuckDB extension for Microsoft SQL Server (TDS + TLS), with catalog integrati... |
| 172 | [nanoarrow](https://duckdb.org/community_extensions/extensions/nanoarrow.html) | [duckdb-nanoarrow](https://github.com/paleolimbot/duckdb-nanoarrow) | ❓ Unknown | 4 - 🟠 Stale | 130 days ago (2026-03-12 13:57:38 UTC) | 75 | C++ | DuckDB extension: nanoarrow by paleolimbot |
| 173 | [nanodbc](https://duckdb.org/community_extensions/extensions/nanodbc.html) | [duckdb-nanodbc-extension](https://github.com/Hugoberry/duckdb-nanodbc-extension) | ❓ Unknown | 3 - 🟡 Stable | 80 days ago (2026-05-01 13:18:55 UTC) | 52 | C++ | Database connectivity extension by Hugoberry |
| 174 | [nats_js](https://duckdb.org/community_extensions/extensions/nats_js.html) | [duckdb-nats-jetstream](https://github.com/brannn/duckdb-nats-jetstream) | ❓ Unknown | 4 - 🟠 Stale | 113 days ago (2026-03-30 05:12:16 UTC) | 21 | C++ | DuckDB extension for querying NATS JetStream message streams with SQL |
| 175 | [netquack](https://duckdb.org/community_extensions/extensions/netquack.html) | [duckdb-netquack](https://github.com/hatamiarash7/duckdb-netquack) | ❓ Unknown | 3 - 🟡 Stable | 59 days ago (2026-05-22 16:42:00 UTC) | 41 | C++ | DuckDB extension for parsing, extracting, and analyzing domains, URIs, and pa... |
| 176 | [nsv](https://duckdb.org/community_extensions/extensions/nsv.html) | [nsv-duckdb](https://github.com/nsv-format/nsv-duckdb) | 🟢 Ongoing | 3 - 🟡 Stable | 43 days ago (2026-06-07 19:12:56 UTC) | 0 | Rust | A DuckDB extension for NSV processing |
| 177 | [oast](https://duckdb.org/community_extensions/extensions/oast.html) | [duckdb-oast](https://github.com/hrbrmstr/duckdb-oast) | 🟢 Ongoing | 4 - 🟠 Stale | 160 days ago (2026-02-10 12:00:32 UTC) | 4 | C | A DuckDB extension for validating, decoding, and extracting OAST (Out-of-Band... |
| 178 | [observefs](https://duckdb.org/community_extensions/extensions/observefs.html) | [duckdb-filesystem-observability](https://github.com/dentiny/duckdb-filesystem-observability) | 🟢 Ongoing | 2 - ✅ Active | 29 days ago (2026-06-22 06:15:49 UTC) | 16 | C++ | Provides observability for duckdb filesystem. |
| 179 | [ofquack](https://duckdb.org/community_extensions/extensions/ofquack.html) | [ofquack](https://github.com/krokozyab/ofquack) | ❓ Unknown | 4 - 🟠 Stale | over a year ago (2025-04-22 12:24:17 UTC) | 6 | C++ | Oracle Fusion DuckDB extension  |
| 180 | [onager](https://duckdb.org/community_extensions/extensions/onager.html) | [onager](https://github.com/CogitatorTech/onager) | 🟢 Ongoing | 2 - ✅ Active | 9 days ago (2026-07-11 14:45:24 UTC) | 149 | Rust | A DuckDB extension for graph data analytics |
| 181 | [onelake](https://duckdb.org/community_extensions/extensions/onelake.html) | [duckdb_onelake](https://github.com/datumnova/duckdb_onelake) | ❓ Unknown | 4 - 🟠 Stale | 231 days ago (2025-12-01 10:28:22 UTC) | 19 | C++ | DuckDB extension: onelake by datumnova |
| 182 | [open_prompt](https://duckdb.org/community_extensions/extensions/open_prompt.html) | [openprompt](https://github.com/Query-farm/openprompt) | 🟢 Ongoing | 4 - 🟠 Stale | 118 days ago (2026-03-24 20:13:01 UTC) | 60 | C++ | DuckDB Community Extension to prompt LLMs from SQL |
| 183 | [osmium](https://duckdb.org/community_extensions/extensions/osmium.html) | [duckdb-osmium](https://github.com/jake-low/duckdb-osmium) | 🟢 Ongoing | 2 - ✅ Active | 11 days ago (2026-07-10 04:46:15 UTC) | 23 | C++ | DuckDB extension for reading OpenStreetMap PBF files using libosmium |
| 184 | [otlp](https://duckdb.org/community_extensions/extensions/otlp.html) | [duckdb-otlp](https://github.com/smithclay/duckdb-otlp) | 🟢 Ongoing | 2 - ✅ Active | 26 days ago (2026-06-24 18:33:02 UTC) | 75 | Python | stream, store, and query OpenTelemetry metrics, logs, and traces (OTLP) in du... |
| 185 | [overture](https://duckdb.org/community_extensions/extensions/overture.html) | [duckdb-overture](https://github.com/cubilica/duckdb-overture) | 🟢 Ongoing | 4 - 🟠 Stale | 97 days ago (2026-04-14 16:46:56 UTC) | 4 | C++ | DuckDB extension: overture by cubilica |
| 186 | [pac](https://duckdb.org/community_extensions/extensions/pac.html) | [privacy](https://github.com/cwida/privacy) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-07-21 08:05:05 UTC) | 18 | C++ | Automatic query privatization in DuckDB |
| 187 | [paimon](https://duckdb.org/community_extensions/extensions/paimon.html) | [duckdb-paimon](https://github.com/polardb/duckdb-paimon) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-07-19 15:15:19 UTC) | 40 | C++ | DuckDB extension for accessing Apache Paimon. 🦆 |
| 188 | [parser_tools](https://duckdb.org/community_extensions/extensions/parser_tools.html) | [duckdb_extension_parser_tools](https://github.com/hotdata-dev/duckdb_extension_parser_tools) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-07-20 22:07:52 UTC) | 27 | C++ | Parse sql - with sql! |
| 189 | [pbi_scanner](https://duckdb.org/community_extensions/extensions/pbi_scanner.html) | [pbi_scanner](https://github.com/crazy-treyn/pbi_scanner) | 🟢 Ongoing | 3 - 🟡 Stable | 33 days ago (2026-06-17 19:07:44 UTC) | 15 | C++ | DuckDB extension that enables querying Power BI Semantic Models with DAX. |
| 190 | [pbix](https://duckdb.org/community_extensions/extensions/pbix.html) | [duckdb-pbix-extension](https://github.com/Hugoberry/duckdb-pbix-extension) | 🟢 Ongoing | 4 - 🟠 Stale | 269 days ago (2025-10-24 13:47:34 UTC) | 38 | C++ | Duckdb extension for parsing the metadata and contents of the embedded data m... |
| 191 | [pcap_duckdb](https://duckdb.org/community_extensions/extensions/pcap_duckdb.html) | [pcap_duckdb](https://github.com/siara-in/pcap_duckdb) | 🟢 Ongoing | 3 - 🟡 Stable | 47 days ago (2026-06-04 05:10:33 UTC) | 1 | C++ | Database connectivity extension by siara-in |
| 192 | [pcap_reader](https://duckdb.org/community_extensions/extensions/pcap_reader.html) | [pcap](https://github.com/Query-farm/pcap) | ❓ Unknown | 3 - 🟡 Stable | 63 days ago (2026-05-18 22:26:34 UTC) | 13 | Rust | DuckDB PCAP Reader Extension made in Rust |
| 193 | [pdal](https://duckdb.org/community_extensions/extensions/pdal.html) | [duckdb-pdal](https://github.com/ahuarte47/duckdb-pdal) | 🟢 Ongoing | 2 - ✅ Active | 8 days ago (2026-07-12 09:53:43 UTC) | 26 | C++ | DuckDB extension for manipulating point cloud data using SQL |
| 194 | [pdf](https://duckdb.org/community_extensions/extensions/pdf.html) | [duckdb-pdf](https://github.com/asubbarao/duckdb-pdf) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-07-21 07:54:04 UTC) | 3 | C++ | Read and extract content from PDF files in DuckDB — Poppler (text/words/lines... |
| 195 | [pfc](https://duckdb.org/community_extensions/extensions/pfc.html) | [pfc-duckdb](https://github.com/ImpossibleForge/pfc-duckdb) | 🟢 Ongoing | 3 - 🟡 Stable | 62 days ago (2026-05-19 17:32:55 UTC) | 1 | C++ | DuckDB extension to read PFC-JSONL compressed log files with block-level time... |
| 196 | [pic2vec](https://duckdb.org/community_extensions/extensions/pic2vec.html) | [pic2vec](https://github.com/nkwork9999/pic2vec) | 🟢 Ongoing | 3 - 🟡 Stable | 38 days ago (2026-06-12 16:13:03 UTC) | 0 | C++ | DuckDB extension: pic2vec by nkwork9999 |
| 197 | [pivot_table](https://duckdb.org/community_extensions/extensions/pivot_table.html) | [pivot_table](https://github.com/Alex-Monahan/pivot_table) | ❓ Unknown | 4 - 🟠 Stale | 94 days ago (2026-04-17 15:20:58 UTC) | 20 | C++ | Full spreadsheet-style pivot table through SQL macros. Just specify values, r... |
| 198 | [plinking_duck](https://duckdb.org/community_extensions/extensions/plinking_duck.html) | [plinking_duck](https://github.com/teaguesterling/plinking_duck) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-07-20 20:24:07 UTC) | 4 | C++ | DuckDB tools for Plink2  |
| 199 | [poached](https://duckdb.org/community_extensions/extensions/poached.html) | [poached](https://github.com/sidequery/poached) | 🟢 Ongoing | 4 - 🟠 Stale | 206 days ago (2025-12-26 21:13:19 UTC) | 11 | C++ | A DuckDB extension that exposes SQL parsing functionality for building IDEs,... |
| 200 | [polyglot](https://duckdb.org/community_extensions/extensions/polyglot.html) | [duckdb-polyglot](https://github.com/tobilg/duckdb-polyglot) | ❓ Unknown | 3 - 🟡 Stable | 45 days ago (2026-06-05 21:14:53 UTC) | 23 | Rust | Use other SQL dialects in DuckDB  |
| 201 | [protoduck](https://duckdb.org/community_extensions/extensions/protoduck.html) | [protoduck](https://github.com/fcsnk/protoduck) | ❓ Unknown | 1 - 🔥 Very Active | 4 days ago (2026-07-17 06:47:06 UTC) | 1 | Rust | DuckDB extension: protoduck by fcsnk |
| 202 | [prql](https://duckdb.org/community_extensions/extensions/prql.html) | [duckdb-prql](https://github.com/ywelsch/duckdb-prql) | 🟢 Ongoing | 3 - 🟡 Stable | 53 days ago (2026-05-28 11:18:16 UTC) | 327 | C++ | PRQL as a DuckDB extension |
| 203 | [psql](https://duckdb.org/community_extensions/extensions/psql.html) | [duckdb-psql](https://github.com/ywelsch/duckdb-psql) | 🟢 Ongoing | 4 - 🟠 Stale | 97 days ago (2026-04-14 18:55:40 UTC) | 106 | C++ | A piped SQL for DuckDB |
| 204 | [pst](https://duckdb.org/community_extensions/extensions/pst.html) | [duckdb-pst](https://github.com/intellekthq/duckdb-pst) | 🟢 Ongoing | 2 - ✅ Active | 25 days ago (2026-06-25 21:06:08 UTC) | 10 | C++ | In-place querying of Microsoft PST files, directly from storage, with SQL. |
| 205 | [psyduck](https://duckdb.org/community_extensions/extensions/psyduck.html) | [psyduck](https://github.com/Ian-Fogelman/psyduck) | 🟢 Ongoing | 4 - 🟠 Stale | 218 days ago (2025-12-14 15:10:39 UTC) | 7 | C++ | Pysduck a DuckDB community extension about Pokémon. |
| 206 | [pyroscope](https://duckdb.org/community_extensions/extensions/pyroscope.html) | [pyroscope](https://github.com/Query-farm/pyroscope) | ❓ Unknown | 4 - 🟠 Stale | 152 days ago (2026-02-18 19:49:53 UTC) | 21 | Rust | DuckDB Pyroscope Extension for Continuous Profiling |
| 207 | [quack_oauth](https://duckdb.org/community_extensions/extensions/quack_oauth.html) | [quack-oauth](https://github.com/DataZooDE/quack-oauth) | 🟢 Ongoing | 1 - 🔥 Very Active | 2 days ago (2026-07-18 16:21:06 UTC) | 21 | C++ | Extensions providing OAuth and OpenID primitives for authentication and autho... |
| 208 | [quackfix](https://duckdb.org/community_extensions/extensions/quackfix.html) | [QuackFIX](https://github.com/hyehudai/QuackFIX) | ❓ Unknown | 4 - 🟠 Stale | 207 days ago (2025-12-25 10:36:24 UTC) | 16 | C++ | Fix log extension for duckdb |
| 209 | [quackformers](https://duckdb.org/community_extensions/extensions/quackformers.html) | [quackformers](https://github.com/martin-conur/quackformers) | ❓ Unknown | 3 - 🟡 Stable | 63 days ago (2026-05-18 14:26:14 UTC) | 13 | Rust | DuckDB NLP extension. |
| 210 | [quackscale](https://duckdb.org/community_extensions/extensions/quackscale.html) | [quackscale](https://github.com/Query-farm/quackscale) | 🟢 Ongoing | 3 - 🟡 Stable | 48 days ago (2026-06-02 17:02:27 UTC) | 22 | Shell | DuckDB WireGuard Extension with Quack & Ducklake over Tailscale, Headscale & Co |
| 211 | [quackstats](https://duckdb.org/community_extensions/extensions/quackstats.html) | [quackstats](https://github.com/jasadams/quackstats) | ❓ Unknown | 4 - 🟠 Stale | 169 days ago (2026-02-01 12:01:35 UTC) | 2 | Rust | DuckDB extension for time series forecasting and seasonality detection |
| 212 | [quackstore](https://duckdb.org/community_extensions/extensions/quackstore.html) | [QuackStore](https://github.com/coginiti-dev/QuackStore) | 🟢 Ongoing | 3 - 🟡 Stable | 76 days ago (2026-05-05 13:29:19 UTC) | 117 | C++ | DuckDB extension: quackstore by coginiti-dev |
| 213 | [query_condition_cache](https://duckdb.org/community_extensions/extensions/query_condition_cache.html) | [duckdb-query-condition-cache](https://github.com/dentiny/duckdb-query-condition-cache) | 🟢 Ongoing | 1 - 🔥 Very Active | 2 days ago (2026-07-18 15:47:10 UTC) | 10 | C++ | DuckDB extension: query_condition_cache by dentiny |
| 214 | [query_limiter](https://duckdb.org/community_extensions/extensions/query_limiter.html) | [duckdb-query-limiter](https://github.com/dentiny/duckdb-query-limiter) | 🟢 Ongoing | 2 - ✅ Active | 12 days ago (2026-07-08 21:33:44 UTC) | 0 | C++ | DuckDB extension: query_limiter by dentiny |
| 215 | [quickjs](https://duckdb.org/community_extensions/extensions/quickjs.html) | [quickjs](https://github.com/Query-farm/quickjs) | 🟢 Ongoing | 3 - 🟡 Stable | 37 days ago (2026-06-13 18:53:30 UTC) | 14 | C++ | DuckDB extension: quickjs by quackscience |
| 216 | [qvd](https://duckdb.org/community_extensions/extensions/qvd.html) | [DuckDB-QVD-Extension](https://github.com/snouhaud/DuckDB-QVD-Extension) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-07-20 09:07:07 UTC) | 0 | Rust | An DuckDB extension to add QVD files read and write |
| 217 | [radio](https://duckdb.org/community_extensions/extensions/radio.html) | [radio](https://github.com/Query-farm/radio) | 🟢 Ongoing | 4 - 🟠 Stale | 113 days ago (2026-03-29 21:04:47 UTC) | 43 | C++ | Radio is a DuckDB extension by Query.Farm that brings real-time event streams... |
| 218 | [rapidfuzz](https://duckdb.org/community_extensions/extensions/rapidfuzz.html) | [rapidfuzz](https://github.com/Query-farm/rapidfuzz) | 🟢 Ongoing | 4 - 🟠 Stale | 113 days ago (2026-03-29 21:04:48 UTC) | 18 | C++ | DuckDB Community Extension adding RapidFuzz algorithms for search, deduplicat... |
| 219 | [raquet](https://duckdb.org/community_extensions/extensions/raquet.html) | [duckdb-raquet](https://github.com/CartoDB/duckdb-raquet) | 🟢 Ongoing | 1 - 🔥 Very Active | 5 days ago (2026-07-15 14:35:34 UTC) | 14 | C++ | DuckDB extension for reading Raquet format (raster data in Parquet with QUADB... |
| 220 | [raster](https://duckdb.org/community_extensions/extensions/raster.html) | [duckdb-raster](https://github.com/ahuarte47/duckdb-raster) | 🟢 Ongoing | 3 - 🟡 Stable | 32 days ago (2026-06-18 22:36:29 UTC) | 52 | C++ | DuckDB Extension for reading and writing raster files using SQL. |
| 221 | [rate_limit_fs](https://duckdb.org/community_extensions/extensions/rate_limit_fs.html) | [duckdb-rate-limit-filesystem](https://github.com/dentiny/duckdb-rate-limit-filesystem) | 🟢 Ongoing | 2 - ✅ Active | 29 days ago (2026-06-22 06:53:00 UTC) | 1 | C++ | DuckDB extension: rate_limit_fs by dentiny |
| 222 | [rawduck](https://duckdb.org/community_extensions/extensions/rawduck.html) | [rawduck](https://github.com/quackscience/rawduck) | 🟢 Ongoing | 1 - 🔥 Very Active | 5 days ago (2026-07-15 09:20:03 UTC) | 20 | C++ | Experimental RawMergeTree-like Extension for DuckDB |
| 223 | [rdf](https://duckdb.org/community_extensions/extensions/rdf.html) | [duck_rdf](https://github.com/nonodename/duck_rdf) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-07-19 23:50:30 UTC) | 25 | C++ | RDF file extension for DuckDB. Reads and writes supported |
| 224 | [read_dbf](https://duckdb.org/community_extensions/extensions/read_dbf.html) | [duckdb-dbf](https://github.com/tocharan/duckdb-dbf) | 🟢 Ongoing | 4 - 🟠 Stale | 145 days ago (2026-02-25 17:13:20 UTC) | 3 | C++ | Database connectivity extension by tocharan |
| 225 | [read_lines](https://duckdb.org/community_extensions/extensions/read_lines.html) | [duckdb_read_lines](https://github.com/teaguesterling/duckdb_read_lines) | 🟢 Ongoing | 2 - ✅ Active | 13 days ago (2026-07-08 06:09:20 UTC) | 4 | C++ | Simple parsers for fast extraction from line-based files  |
| 226 | [read_stat](https://duckdb.org/community_extensions/extensions/read_stat.html) | [duckdb-read-stat](https://github.com/dylanmeysmans/duckdb-read-stat) | 🟢 Ongoing | 3 - 🟡 Stable | 31 days ago (2026-06-19 23:25:46 UTC) | 34 | C | Read data sets from SAS, Stata, and SPSS from DuckDB with ReadStat |
| 227 | [redis](https://duckdb.org/community_extensions/extensions/redis.html) | [redis](https://github.com/Query-farm/redis) | 🟢 Ongoing | 4 - 🟠 Stale | 113 days ago (2026-03-29 21:04:49 UTC) | 13 | C++ | DuckDB Redis Client community extension |
| 228 | [robust](https://duckdb.org/community_extensions/extensions/robust.html) | [robust](https://github.com/robust-sql/robust) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-07-20 01:26:38 UTC) | 5 | C++ | A DuckDB extension implementing Predicate Transfer to reduce cardinality expl... |
| 229 | [rrd](https://duckdb.org/community_extensions/extensions/rrd.html) | [duckdb-rrd](https://github.com/VertexStudio/duckdb-rrd) | 🟢 Ongoing | 2 - ✅ Active | 17 days ago (2026-07-03 18:31:26 UTC) | 0 | Rust | DuckDB extension: rrd by VertexStudio |
| 230 | [rusty_quack](https://duckdb.org/community_extensions/extensions/rusty_quack.html) | [extension-template-rs](https://github.com/duckdb/extension-template-rs) | ❓ Unknown | 2 - ✅ Active | 28 days ago (2026-06-23 05:38:14 UTC) | 111 | Rust | (Experimental) Template for Rust-based DuckDB extensions |
| 231 | [rusty_sheet](https://duckdb.org/community_extensions/extensions/rusty_sheet.html) | [rusty-sheet](https://github.com/redraiment/rusty-sheet) | 🟢 Ongoing | 4 - 🟠 Stale | 158 days ago (2026-02-13 02:27:56 UTC) | 73 | Rust | An Excel/WPS/OpenDocument Spreadsheets file reader for DuckDB |
| 232 | [salesforce](https://duckdb.org/community_extensions/extensions/salesforce.html) | [duckdb-salesforce](https://github.com/flozer/duckdb-salesforce) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-07-20 12:11:10 UTC) | 2 | C++ | DuckDB extension: salesforce by flozer |
| 233 | [sazgar](https://duckdb.org/community_extensions/extensions/sazgar.html) | [Sazgar](https://github.com/Angelerator/Sazgar) | ❓ Unknown | 3 - 🟡 Stable | 60 days ago (2026-05-22 04:56:10 UTC) | 13 | HTML | DuckDB extension for system monitoring & intelligent SQL routing. 25+ functio... |
| 234 | [scalarfs](https://duckdb.org/community_extensions/extensions/scalarfs.html) | [duckdb_scalarfs](https://github.com/teaguesterling/duckdb_scalarfs) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-07-19 16:36:35 UTC) | 8 | C++ | A collection of simple virtual filesystems for treating scalar values as files. |
| 235 | [scrooge](https://duckdb.org/community_extensions/extensions/scrooge.html) | [Scrooge-McDuck](https://github.com/pdet/Scrooge-McDuck) | 🟢 Ongoing | 3 - 🟡 Stable | 77 days ago (2026-05-04 14:27:57 UTC) | 162 | C++ | DuckDB extension: scrooge by pdet |
| 236 | [se3](https://duckdb.org/community_extensions/extensions/se3.html) | [se3](https://github.com/jokasimr/se3) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-07-19 09:45:05 UTC) | 0 | C++ | Duckdb extension for efficient rotation / translation operations on points in... |
| 237 | [semantic_views](https://duckdb.org/community_extensions/extensions/semantic_views.html) | [duckdb-semantic-views](https://github.com/anentropic/duckdb-semantic-views) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-07-21 00:05:53 UTC) | 10 | Rust | Semantic Views for DuckDB. |
| 238 | [sheetreader](https://duckdb.org/community_extensions/extensions/sheetreader.html) | [sheetreader-duckdb](https://github.com/polydbms/sheetreader-duckdb) | 🟢 Ongoing | 4 - 🟠 Stale | 127 days ago (2026-03-15 11:03:07 UTC) | 58 | C++ | DuckDB extension: sheetreader by polydbms |
| 239 | [shellfs](https://duckdb.org/community_extensions/extensions/shellfs.html) | [shellfs](https://github.com/Query-farm/shellfs) | 🟢 Ongoing | 3 - 🟡 Stable | 36 days ago (2026-06-15 00:30:23 UTC) | 95 | C++ | DuckDB extension allowing shell commands to be used for input and output. |
| 240 | [sistat](https://duckdb.org/community_extensions/extensions/sistat.html) | [duckdb-sistat](https://github.com/fklezin/duckdb-sistat) | 🟢 Ongoing | 4 - 🟠 Stale | 133 days ago (2026-03-09 09:09:46 UTC) | 3 | C++ | DuckDB extension to query Slovenia's SiStat open data directly using SQL. No... |
| 241 | [sitemap](https://duckdb.org/community_extensions/extensions/sitemap.html) | [duckdb-sitemap](https://github.com/midwork-finds-jobs/duckdb-sitemap) | 🟢 Ongoing | 4 - 🟠 Stale | 153 days ago (2026-02-17 14:13:12 UTC) | 1 | C++ | DuckDB extension for parsing XML sitemaps from websites |
| 242 | [sitting_duck](https://duckdb.org/community_extensions/extensions/sitting_duck.html) | [sitting_duck](https://github.com/teaguesterling/sitting_duck) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-07-19 23:18:26 UTC) | 20 | C | Sitting Duck is a DuckDB extension that makes Abstract Syntax Trees (ASTs) fr... |
| 243 | [slack](https://github.com/dentiny/duckdb-slack) | [duckdb-slack](https://github.com/dentiny/duckdb-slack) | ❓ Unknown | 4 - 🟠 Stale | 151 days ago (2026-02-19 18:08:54 UTC) | 0 | C++ | DuckDB extension: slack by dentiny |
| 244 | [snowflake](https://duckdb.org/community_extensions/extensions/snowflake.html) | [duckdb-snowflake](https://github.com/iqea-ai/duckdb-snowflake) | 🟢 Ongoing | 1 - 🔥 Very Active | 4 days ago (2026-07-17 08:17:29 UTC) | 58 | C++ | A powerful DuckDB extension that enables seamless querying of Snowflake datab... |
| 245 | [splink_udfs](https://duckdb.org/community_extensions/extensions/splink_udfs.html) | [splink_udfs](https://github.com/moj-analytical-services/splink_udfs) | ❓ Unknown | 4 - 🟠 Stale | 164 days ago (2026-02-06 11:01:11 UTC) | 5 | C++ | DuckDB extension: splink_udfs by moj-analytical-services |
| 246 | [splunk](https://duckdb.org/community_extensions/extensions/splunk.html) | [duckdb-splunk](https://github.com/smithclay/duckdb-splunk) | 🟢 Ongoing | 1 - 🔥 Very Active | 4 days ago (2026-07-16 15:53:00 UTC) | 1 | C++ | read logs from splunk into duckdb |
| 247 | [spxlsx](https://duckdb.org/community_extensions/extensions/spxlsx.html) | [spxlsx](https://github.com/paulmupeters/spxlsx) | 🟢 Ongoing | 2 - ✅ Active | 20 days ago (2026-06-30 20:34:53 UTC) | 2 | C++ | Duckdb extension to read sharepoint lists and excel |
| 248 | [sshfs](https://duckdb.org/community_extensions/extensions/sshfs.html) | [duckdb-sshfs](https://github.com/midwork-finds-jobs/duckdb-sshfs) | 🟢 Ongoing | 3 - 🟡 Stable | 44 days ago (2026-06-06 19:02:46 UTC) | 11 | C++ | DuckDB sshfs extension - Read and write files through ssh inside DuckDB |
| 249 | [st_read_multi](https://duckdb.org/community_extensions/extensions/st_read_multi.html) | [duckdb-ext-st-read-multi](https://github.com/yutannihilation/duckdb-ext-st-read-multi) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-07-20 13:54:23 UTC) | 10 | Rust | A DuckDB extension to import multiple geospatial files with `ST_Read_Multi()` |
| 250 | [stats_duck](https://duckdb.org/community_extensions/extensions/stats_duck.html) | [the-stats-duck](https://github.com/KoliStat/the-stats-duck) | 🟢 Ongoing | 2 - ✅ Active | 12 days ago (2026-07-08 11:57:59 UTC) | 53 | C++ | A statistical computing toolkit for DuckDB. |
| 251 | [stochastic](https://duckdb.org/community_extensions/extensions/stochastic.html) | [stochastic](https://github.com/Query-farm/stochastic) | 🟢 Ongoing | 3 - 🟡 Stable | 37 days ago (2026-06-13 16:28:47 UTC) | 25 | C++ | A DuckDB extension that add comprehensive statistical distribution functions... |
| 252 | [substrait](https://duckdb.org/community_extensions/extensions/substrait.html) | [duckdb-substrait-extension](https://github.com/substrait-io/duckdb-substrait-extension) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-07-20 17:03:45 UTC) | 66 | C++ | DuckDB extension: substrait by substrait-io |
| 253 | [sudan](https://duckdb.org/community_extensions/extensions/sudan.html) | [duckdb-sudan-](https://github.com/Osman-Geomatics93/duckdb-sudan-) | 🟢 Ongoing | 4 - 🟠 Stale | 151 days ago (2026-02-19 11:49:28 UTC) | 0 | Jupyter Notebook | DuckDB extension: sudan by Osman-Geomatics93 |
| 254 | [system_stats](https://duckdb.org/community_extensions/extensions/system_stats.html) | [system_stats](https://github.com/dentiny/system_stats) | 🟢 Ongoing | 2 - ✅ Active | 29 days ago (2026-06-22 06:20:24 UTC) | 3 | C++ | DuckDB extension: system_stats by dentiny |
| 255 | [table_guard](https://duckdb.org/community_extensions/extensions/table_guard.html) | [duckdb-table-guard](https://github.com/yoogoc/duckdb-table-guard) | 🟢 Ongoing | 3 - 🟡 Stable | 67 days ago (2026-05-14 09:52:13 UTC) | 2 | C++ | A DuckDB extension for table-level access control |
| 256 | [table_inspector](https://duckdb.org/community_extensions/extensions/table_inspector.html) | [duckdb-table-inspector](https://github.com/dentiny/duckdb-table-inspector) | 🟢 Ongoing | 2 - ✅ Active | 28 days ago (2026-06-22 19:34:34 UTC) | 2 | C++ | DuckDB extension: table_inspector by dentiny |
| 257 | [talib](https://duckdb.org/community_extensions/extensions/talib.html) | [atm_talib](https://github.com/neuesql/atm_talib) | 🟢 Ongoing | 4 - 🟠 Stale | 91 days ago (2026-04-21 06:06:51 UTC) | 5 | C++ | A duckdb TA-Lib to add technical analysis in Financial Markets with SQL easily |
| 258 | [tarfs](https://duckdb.org/community_extensions/extensions/tarfs.html) | [duckdb_tarfs](https://github.com/Maxxen/duckdb_tarfs) | ❓ Unknown | 4 - 🟠 Stale | over a year ago (2024-08-26 11:01:47 UTC) | 12 | C++ | DuckDB extension: tarfs by Maxxen |
| 259 | [tera](https://duckdb.org/community_extensions/extensions/tera.html) | [tera](https://github.com/Query-farm/tera) | 🟢 Ongoing | 3 - 🟡 Stable | 37 days ago (2026-06-13 16:50:05 UTC) | 9 | C++ | DuckDB extension: tera |
| 260 | [textplot](https://duckdb.org/community_extensions/extensions/textplot.html) | [textplot](https://github.com/Query-farm/textplot) | 🟢 Ongoing | 3 - 🟡 Stable | 37 days ago (2026-06-13 16:28:45 UTC) | 25 | C++ | A DuckDB community extension that enables text-based data visualization direc... |
| 261 | [three_d](https://duckdb.org/community_extensions/extensions/three_d.html) | [duckdb-3d-extension](https://github.com/cityjson/duckdb-3d-extension) | 🟢 Ongoing | 1 - 🔥 Very Active | 2 days ago (2026-07-19 06:50:20 UTC) | 1 | C++ | (Still Experimental) DuckDB extension to process 3D geomerty |
| 262 | [title_mapper](https://duckdb.org/community_extensions/extensions/title_mapper.html) | [duckdb-title-mapper](https://github.com/martin-conur/duckdb-title-mapper) | ❓ Unknown | 3 - 🟡 Stable | 56 days ago (2026-05-25 21:56:26 UTC) | 3 | Rust | DuckDB extension: title_mapper by martin-conur |
| 263 | [tpch_rust](https://duckdb.org/community_extensions/extensions/tpch_rust.html) | [duckdb-tpch-rust](https://github.com/guillesd/duckdb-tpch-rust) | ❓ Unknown | 3 - 🟡 Stable | 42 days ago (2026-06-08 15:40:17 UTC) | 0 | Rust | DuckDB extension to generate tpch tables using tpch-rs |
| 264 | [tributary](https://duckdb.org/community_extensions/extensions/tributary.html) | [tributary](https://github.com/Query-farm/tributary) | ❓ Unknown | 4 - 🟠 Stale | 113 days ago (2026-03-29 21:04:53 UTC) | 57 | C++ | A DuckDB Extension for Kafka |
| 265 | [tsid](https://duckdb.org/community_extensions/extensions/tsid.html) | [tsid](https://github.com/Query-farm/tsid) | 🟢 Ongoing | 4 - 🟠 Stale | 113 days ago (2026-03-29 21:04:54 UTC) | 6 | C++ | TSID Extension for DuckDB  |
| 266 | [ulid](https://duckdb.org/community_extensions/extensions/ulid.html) | [duckdb_ulid](https://github.com/Maxxen/duckdb_ulid) | ❓ Unknown | 4 - 🟠 Stale | over a year ago (2024-07-09 09:35:50 UTC) | 25 | C++ | DuckDB extension: ulid by Maxxen |
| 267 | [urlpattern](https://duckdb.org/community_extensions/extensions/urlpattern.html) | [duckdb_urlpattern](https://github.com/teaguesterling/duckdb_urlpattern) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-07-19 19:38:59 UTC) | 8 | C++ | An implementation of URLPattern for DuckDB |
| 268 | [us_address_standardizer](https://duckdb.org/community_extensions/extensions/us_address_standardizer.html) | [duckdb-address-standardizer](https://github.com/ericmanning/duckdb-address-standardizer) | 🟢 Ongoing | 3 - 🟡 Stable | 61 days ago (2026-05-20 14:50:54 UTC) | 3 | C | DuckDB extension for parsing and standardizing (USA) postal addresses using P... |
| 269 | [valhalla_routing](https://duckdb.org/community_extensions/extensions/valhalla_routing.html) | [duckdb-valhalla-routing](https://github.com/midwork-finds-jobs/duckdb-valhalla-routing) | 🟢 Ongoing | 4 - 🟠 Stale | 153 days ago (2026-02-17 11:36:12 UTC) | 7 | Makefile | WIP: Attempt to package valhalla routing engine to duckdb |
| 270 | [vindex](https://duckdb.org/community_extensions/extensions/vindex.html) | [duckdb-vector-index](https://github.com/Icemap/duckdb-vector-index) | 🟢 Ongoing | 1 - 🔥 Very Active | 4 days ago (2026-07-16 10:06:50 UTC) | 8 | C++ | A DuckDB extension providing HNSW, IVF, DiskANN, and SPANN vector indexes wit... |
| 271 | [waddle](https://duckdb.org/community_extensions/extensions/waddle.html) | [extension-template](https://github.com/duckdb/extension-template) | 🟢 Ongoing | 2 - ✅ Active | 28 days ago (2026-06-22 10:58:32 UTC) | 286 | Python | Template for DuckDB extensions to help you develop, test and deploy a custom... |
| 272 | [warc](https://duckdb.org/community_extensions/extensions/warc.html) | [duckdb_warc](https://github.com/midwork-finds-jobs/duckdb_warc) | ❓ Unknown | 4 - 🟠 Stale | 165 days ago (2026-02-05 15:33:27 UTC) | 6 | Rust | DuckDB extension for parsing WARC files |
| 273 | [web_archive](https://duckdb.org/community_extensions/extensions/web_archive.html) | [duckdb-web-archive](https://github.com/midwork-finds-jobs/duckdb-web-archive) | 🟢 Ongoing | 2 - ✅ Active | 23 days ago (2026-06-27 17:30:16 UTC) | 21 | C++ | DuckDB extension to fetch pages from Wayback Machine & Common Crawl |
| 274 | [web_search](https://duckdb.org/community_extensions/extensions/web_search.html) | [duckdb-web-search](https://github.com/midwork-finds-jobs/duckdb-web-search) | 🟢 Ongoing | 4 - 🟠 Stale | 91 days ago (2026-04-20 21:51:13 UTC) | 0 | C++ | Web/HTTP functionality extension by midwork-finds-jobs |
| 275 | [webbed](https://duckdb.org/community_extensions/extensions/webbed.html) | [duckdb_webbed](https://github.com/teaguesterling/duckdb_webbed) | 🟢 Ongoing | 1 - 🔥 Very Active | 2 days ago (2026-07-19 06:56:10 UTC) | 66 | C++ | A comprehensive XML and HTML processing extension for DuckDB that enables SQL... |
| 276 | [webdavfs](https://duckdb.org/community_extensions/extensions/webdavfs.html) | [duckdb-webdavfs](https://github.com/midwork-finds-jobs/duckdb-webdavfs) | ❓ Unknown | 3 - 🟡 Stable | 87 days ago (2026-04-25 03:42:47 UTC) | 1 | C++ | DuckDB WebDAVfs Extension - WebDAV filesystem support for DuckDB |
| 277 | [webmacro](https://duckdb.org/community_extensions/extensions/webmacro.html) | [webmacro](https://github.com/Query-farm/webmacro) | 🟢 Ongoing | 4 - 🟠 Stale | 118 days ago (2026-03-24 20:13:18 UTC) | 15 | C++ | DuckDB WebMacro: Share and Load your SQL Macros via gists |
| 278 | [whisper](https://duckdb.org/community_extensions/extensions/whisper.html) | [duckdb-whisper](https://github.com/tobilg/duckdb-whisper) | 🟢 Ongoing | 2 - ✅ Active | 23 days ago (2026-06-27 15:19:59 UTC) | 10 | C++ | Use whisper.cpp within DuckDB to translate / transpile speech to text |
| 279 | [wireduck](https://duckdb.org/community_extensions/extensions/wireduck.html) | [wireduck](https://github.com/hyehudai/wireduck) | 🟢 Ongoing | 4 - 🟠 Stale | 300 days ago (2025-09-23 21:22:03 UTC) | 48 | C++ | Duckdb extension to read pcap files |
| 280 | [yaml](https://duckdb.org/community_extensions/extensions/yaml.html) | [duckdb_yaml](https://github.com/teaguesterling/duckdb_yaml) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-07-20 18:43:24 UTC) | 21 | C++ |  A DuckDB to read and work with YAML files in a similar way to JSON files (al... |
| 281 | [yardstick](https://duckdb.org/community_extensions/extensions/yardstick.html) | [yardstick](https://github.com/sidequery/yardstick) | 🟢 Ongoing | 2 - ✅ Active | 17 days ago (2026-07-03 19:43:26 UTC) | 58 | Rust | An implementation of Measures in SQL as a DuckDB extension |
| 282 | [zarr](https://duckdb.org/community_extensions/extensions/zarr.html) | [duckdb-zarr](https://github.com/xqlsystems/duckdb-zarr) | 🟢 Ongoing | 1 - 🔥 Very Active | 7 days ago (2026-07-13 17:25:10 UTC) | 19 | Rust | DuckDB extension: zarr by xqlsystems |
| 283 | [zeek](https://duckdb.org/community_extensions/extensions/zeek.html) | [zeek-duckdb](https://github.com/ynadji/zeek-duckdb) | 🟢 Ongoing | 4 - 🟠 Stale | 97 days ago (2026-04-14 22:02:22 UTC) | 3 | C++ | read_zeek table function to read Zeek TSV logs into DuckDB |
| 284 | [zim](https://duckdb.org/community_extensions/extensions/zim.html) | [duckdb_zim](https://github.com/teaguesterling/duckdb_zim) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-07-20 17:20:36 UTC) | 3 | C++ | DuckDB extension for working with zim files |
| 285 | [zipfs](https://duckdb.org/community_extensions/extensions/zipfs.html) | [duckdb-zipfs](https://github.com/isaacbrodsky/duckdb-zipfs) | 🟢 Ongoing | 2 - ✅ Active | 12 days ago (2026-07-08 22:35:07 UTC) | 65 | C++ | DuckDB extension to read files within zip archives. |

</details>
## Appendix: DuckDB Release Information

### Current Release Context

DuckDB follows **semantic versioning** with regular releases. For complete and up-to-date release information, see the official [**DuckDB Release Calendar**](https://duckdb.org/release_calendar.html).

### Upcoming Releases

|| Version | Planned Date | LTS |
||---------|-------------|-----|
|| v1.5.5 📅 | 2026-07-22 |  |

### Recent Releases

|| Version | Release Date | Codename | Named After | LTS | Status |
||---------|--------------|----------|-------------|-----|--------|
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
|| **v1.2.2** | 2025-04-08 | – | – |  | Active |

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

<p class="fine-print">Last updated: 2026-07-21</p>
