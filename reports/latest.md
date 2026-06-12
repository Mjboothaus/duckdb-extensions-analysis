# DuckDB Extensions Analysis

🦆 **Automated monitoring and analysis of DuckDB's extension ecosystem**


[Executive summary](#executive-summary) | [Jump to Summary](#summary) | [Core Extensions](#core-extensions) | [Community Extensions](#community-extensions)

---

**Running on DuckDB:** v1.5.3 (2026-05-20)
This report provides a comprehensive analysis of DuckDB extensions, including both core extensions (built into DuckDB) and community-contributed extensions.

For third-party extensions discovered outside the official registries, see: [Third-party extensions](https://mjboothaus.github.io/duckdb-extensions-analysis/third-party/).

For a lightweight monthly roundup of notable ecosystem changes, see: [What’s new](https://github.com/Mjboothaus/duckdb-extensions-analysis/blob/main/WHATS_NEW.md).

*Note:* third-party labelling is an ongoing work in progress, so the verified list is partial.

---
## Executive summary


### At a glance
- **284** total extensions tracked (**29** core, **255** community)
- **53 / 284** extensions updated in the last 7 days
- **126 / 284** extensions updated in the last 30 days
- **1** community repositories are archived
- **60** community extensions have unknown/repo issues (missing or inaccessible repositories)

### Highlights
#### Most active (last 7 days)
| Extension | Repository | Last activity |
|---|---|---|
| [finetype](https://duckdb.org/community_extensions/extensions/finetype.html) | [finetype](https://github.com/meridian-online/finetype) | today (2026-06-12 07:41:06 UTC) |
| [anofox_statistics](https://duckdb.org/community_extensions/extensions/anofox_statistics.html) | [anofox-statistics](https://github.com/DataZooDE/anofox-statistics) | today (2026-06-12 07:16:07 UTC) |
| [anofox_tabular](https://duckdb.org/community_extensions/extensions/anofox_tabular.html) | [anofox-tabular](https://github.com/DataZooDE/anofox-tabular) | today (2026-06-12 06:38:25 UTC) |
| [behavioral](https://duckdb.org/community_extensions/extensions/behavioral.html) | [duckdb-behavioral](https://github.com/tomtom215/duckdb-behavioral) | today (2026-06-12 06:26:26 UTC) |
| [duckdb_delta_sharing](https://duckdb.org/community_extensions/extensions/duckdb_delta_sharing.html) | [duckdb-delta-sharing](https://github.com/prequel-co/duckdb-delta-sharing) | today (2026-06-11 19:52:08 UTC) |

#### Most starred (community)
| Extension | Repository | Stars |
|---|---|---:|
| [duckpgq](https://duckdb.org/community_extensions/extensions/duckpgq.html) | [duckpgq-extension](https://github.com/cwida/duckpgq-extension) | 416 |
| [gsheets](https://duckdb.org/community_extensions/extensions/gsheets.html) | [duckdb_gsheets](https://github.com/evidence-dev/duckdb_gsheets) | 345 |
| [flock](https://duckdb.org/community_extensions/extensions/flock.html) | [flock](https://github.com/dais-polymtl/flock) | 342 |
| [airport](https://duckdb.org/community_extensions/extensions/airport.html) | [airport](https://github.com/Query-farm/airport) | 340 |
| [prql](https://duckdb.org/community_extensions/extensions/prql.html) | [duckdb-prql](https://github.com/ywelsch/duckdb-prql) | 326 |

### How to read the report
- **Status** is a repository signal (ongoing / archived / unknown).
- **Activity** is based on the last git push; quiet projects can still be healthy.
- Use the tables below to drill into **Core Extensions** and **Community Extensions**.

---
## Summary

### 📊 Quick Stats (with trends)

| **Metric** | **Current** | **Change** |
|------------|-------------|------------|
| **Total Extensions** | 284 | +6 🔼 |
| **Core Extensions** | 29 | → Stable |
| **Community Extensions** | 255 | +6 🔼 |
| **Recently Active** (≤ 30 days) | 126 (44.4%) | +6 🔼 |
| **Very Active** (≤ 7 days) | 53 (18.7%) | — |

*Changes since previous analysis*


### 🆕 Recent Additions

flock, h5db, gsheets, quackscale, robust, firebird, dta, cache_httpfs, pcap_duckdb, lpts *and 1 more*



### 🗑️ Removed

encoding, jemalloc, latency_injection



---
## Core Extensions

Core extensions maintained by the DuckDB team and distributed via the official extension repository

**Total:** 29 extensions

<details open markdown="1">
<summary>Click to expand/collapse core extensions table</summary>

| # | Extension | Repository | Status | Last Activity | Stars | Language | Description |
|---|-----------|------------|--------|---------------|-------|----------|-------------|
| 1 | [autocomplete](https://duckdb.org/docs/current/core_extensions/autocomplete) | [duckdb/duckdb](https://github.com/duckdb/duckdb/tree/main/extension/autocomplete) | 🟢 Ongoing | 2 days ago (2026-06-09 20:22:09 UTC) | N/A (part of core DuckDB repo) | C++ | Core DuckDB extension: autocomplete |
| 2 | [avro](https://duckdb.org/docs/current/core_extensions/avro) | [duckdb-avro](https://github.com/duckdb/duckdb-avro) | 🟢 Ongoing | today (2026-06-11 08:43:02 UTC) | 36 | C++ | Apache Avro format support |
| 3 | [aws](https://duckdb.org/docs/current/core_extensions/aws) | [duckdb-aws](https://github.com/duckdb/duckdb-aws) | 🟢 Ongoing | today (2026-06-11 09:22:37 UTC) | 64 | C++ | AWS S3 integration |
| 4 | [azure](https://duckdb.org/docs/current/core_extensions/azure) | [duckdb-azure](https://github.com/duckdb/duckdb-azure) | 🟢 Ongoing | 42 days ago (2026-05-01 07:37:45 UTC) | 77 | C++ | Azure extension for DuckDB |
| 5 | [delta](https://duckdb.org/docs/current/core_extensions/delta) | [duckdb-delta](https://github.com/duckdb/duckdb-delta) | 🟢 Ongoing | 22 days ago (2026-05-20 15:43:17 UTC) | 226 | C++ | DuckDB extension for Delta Lake |
| 6 | [ducklake](https://duckdb.org/docs/current/core_extensions/ducklake) | [duckdb/ducklake](https://github.com/duckdb/ducklake) | 🟢 Ongoing | 22 days ago | N/A (part of core DuckDB repo) | C++ | Delta Lake support via DuckLake (different from delta extension) |
| 7 | [encodings](https://duckdb.org/docs/current/core_extensions/encodings) | [duckdb-encodings](https://github.com/duckdb/duckdb-encodings) | 🟢 Ongoing | 115 days ago (2026-02-16 11:43:18 UTC) | 15 | C++ | Character encoding support |
| 8 | [excel](https://duckdb.org/docs/current/core_extensions/excel) | [duckdb-excel](https://github.com/duckdb/duckdb-excel) | 🟢 Ongoing | 14 days ago (2026-05-28 14:57:36 UTC) | 55 | C++ | Excel extension for DuckDB |
| 9 | [fts](https://duckdb.org/docs/current/core_extensions/full_text_search) | [duckdb-fts](https://github.com/duckdb/duckdb-fts) | 🟢 Ongoing | today (2026-06-11 13:01:03 UTC) | 38 | C++ | Full-text search functionality |
| 10 | [httpfs](https://duckdb.org/docs/current/core_extensions/httpfs/overview) | [duckdb-httpfs](https://github.com/duckdb/duckdb-httpfs) | 🟢 Ongoing | today (2026-06-11 08:38:32 UTC) | 55 | C++ | HTTP/S3 filesystem support |
| 11 | [iceberg](https://duckdb.org/docs/current/core_extensions/iceberg/overview) | [duckdb-iceberg](https://github.com/duckdb/duckdb-iceberg) | 🟢 Ongoing | today (2026-06-11 15:07:03 UTC) | 412 | C++ | Apache Iceberg format support |
| 12 | [icu](https://duckdb.org/docs/current/core_extensions/icu) | [duckdb/duckdb](https://github.com/duckdb/duckdb/tree/main/extension/icu) | 🟢 Ongoing | 3 days ago (2026-06-08 15:49:58 UTC) | N/A (part of core DuckDB repo) | C++ | Core DuckDB extension: icu |
| 13 | [inet](https://duckdb.org/docs/current/core_extensions/inet) | [duckdb-inet](https://github.com/duckdb/duckdb-inet) | 🟢 Ongoing | 203 days ago (2025-11-20 22:54:12 UTC) | 14 | C++ | Internet address data types |
| 14 | [json](https://duckdb.org/docs/current/data/json/overview) | [duckdb/duckdb](https://github.com/duckdb/duckdb/tree/main/extension/json) | 🟢 Ongoing | 2 days ago (2026-06-09 10:58:06 UTC) | N/A (part of core DuckDB repo) | C++ | Core DuckDB extension: json |
| 15 | [lance](https://duckdb.org/docs/current/core_extensions/lance) | [lance-duckdb](https://github.com/lance-format/lance-duckdb) | 🟢 Ongoing | today (2026-06-10 15:35:14 UTC) | 117 | C++ | The lance extensions for DuckDB enable reading and writing of lance tables. |
| 16 | [motherduck](https://duckdb.org/docs/current/core_extensions/motherduck.html) | [duckdb/duckdb](https://github.com/duckdb/duckdb) *(Third Party - Closed source - maintained by MotherDuck Inc.)* | 🟢 Ongoing | 22 days ago | N/A (part of core DuckDB repo) | C++ | Core DuckDB extension: motherduck |
| 17 | [mysql](https://duckdb.org/docs/current/core_extensions/mysql) | [duckdb-mysql](https://github.com/duckdb/duckdb-mysql) | 🟢 Ongoing | 2 days ago (2026-06-09 17:54:58 UTC) | 97 | C++ | MySQL database connectivity |
| 18 | [odbc](https://duckdb.org/docs/current/core_extensions/odbc/overview) | [odbc-scanner](https://github.com/duckdb/odbc-scanner) | 🟢 Ongoing | 12 days ago (2026-05-30 11:58:55 UTC) | 38 | C++ | DuckDB ODBC extension |
| 19 | [parquet](https://duckdb.org/docs/current/data/parquet/overview) | [duckdb/duckdb](https://github.com/duckdb/duckdb/tree/main/extension/parquet) | 🟢 Ongoing | today (2026-06-11 13:37:03 UTC) | N/A (part of core DuckDB repo) | C++ | Core DuckDB extension: parquet |
| 20 | [postgres](https://duckdb.org/docs/current/core_extensions/postgres/overview) | [duckdb-postgres](https://github.com/duckdb/duckdb-postgres) | 🟢 Ongoing | 2 days ago (2026-06-09 18:17:22 UTC) | 358 | C++ | PostgreSQL database connectivity |
| 21 | [quack](https://duckdb.org/docs/current/core_extensions/quack) | [duckdb-quack](https://github.com/duckdb/duckdb-quack) | 🟢 Ongoing | today (2026-06-10 13:01:45 UTC) | 105 | C++ | Quack remote protocol |
| 22 | [spatial](https://duckdb.org/docs/current/core_extensions/spatial/overview) | [duckdb-spatial](https://github.com/duckdb/duckdb-spatial) | 🟢 Ongoing | 30 days ago (2026-05-12 17:37:14 UTC) | 684 | C++ | Geospatial data types and functions |
| 23 | [sqlite](https://duckdb.org/docs/current/core_extensions/sqlite) | [duckdb-sqlite](https://github.com/duckdb/duckdb-sqlite) | 🟢 Ongoing | 14 days ago (2026-05-28 21:00:20 UTC) | 276 | C++ | DuckDB extension to read and write to SQLite databases |
| 24 | [tpcds](https://duckdb.org/docs/current/core_extensions/tpcds) | [duckdb/duckdb](https://github.com/duckdb/duckdb/tree/main/extension/tpcds) | 🟢 Ongoing | 4 days ago (2026-06-07 08:25:36 UTC) | N/A (part of core DuckDB repo) | C++ | Core DuckDB extension: tpcds |
| 25 | [tpch](https://duckdb.org/docs/current/core_extensions/tpch) | [duckdb/duckdb](https://github.com/duckdb/duckdb/tree/main/extension/tpch) | 🟢 Ongoing | 4 days ago (2026-06-07 08:25:36 UTC) | N/A (part of core DuckDB repo) | C++ | Core DuckDB extension: tpch |
| 26 | [ui](https://duckdb.org/docs/current/core_extensions/ui) | [duckdb-ui](https://github.com/duckdb/duckdb-ui) | 🟢 Ongoing | 8 days ago (2026-06-03 23:22:43 UTC) | 449 | C++ | Browser-based user interface for DuckDB |
| 27 | [unity_catalog](https://duckdb.org/docs/current/core_extensions/unity_catalog) | [unity_catalog](https://github.com/duckdb/unity_catalog) | 🟢 Ongoing | 35 days ago (2026-05-07 12:01:13 UTC) | 103 | C++ | Proof-of-concept extension combining the delta extension with Unity Catalog |
| 28 | [vortex](https://duckdb.org/docs/current/core_extensions/vortex) | [duckdb/duckdb](https://github.com/duckdb/duckdb) *(Third Party - Closed source - third-party extension)* | 🟢 Ongoing | 22 days ago | N/A (part of core DuckDB repo) | C++ | Core DuckDB extension: vortex |
| 29 | [vss](https://duckdb.org/docs/current/core_extensions/vss) | [duckdb-vss](https://github.com/duckdb/duckdb-vss) | 🟢 Ongoing | 9 days ago (2026-06-02 08:10:39 UTC) | 260 | C++ | Vector similarity search |

</details>

---
---
## Community Extensions

Third-party extensions maintained by the community


**Total:** 255 extensions | 🔥 Very Active (≤7d): 54 | ✅ Active (≤30d): 73 | 🟡 Stable (≤90d): 70 | 🟠 Stale (>90d): 58

<details open markdown="1">
<summary>Click to expand/collapse community extensions table</summary>

| # | Extension | Repository | Status | Activity | Last Activity | Stars | Language | Description |
|---|-----------|------------|--------|----------|---------------|-------|----------|-------------|
| 1 | [a5](https://duckdb.org/community_extensions/extensions/a5.html) | [a5](https://github.com/Query-farm/a5) | 🟢 Ongoing | 1 - 🔥 Very Active | 2 days ago (2026-06-10 01:36:20 UTC) | 12 | C++ | A5 Geospatial Extension for DuckDB |
| 2 | [acp](https://duckdb.org/community_extensions/extensions/acp.html) | [duckdb-acp](https://github.com/sidequery/duckdb-acp) | 🟡 Archived | 4 - 🟠 Stale | 183 days ago (2025-12-11 03:36:46 UTC) | 58 | Rust | Use Claude Code & other AI agents from inside DuckDB via extension |
| 3 | [adbc_scanner](https://duckdb.org/community_extensions/extensions/adbc_scanner.html) | [adbc_scanner](https://github.com/Query-farm/adbc_scanner) | 🟢 Ongoing | 2 - ✅ Active | 10 days ago (2026-06-01 21:54:18 UTC) | 15 | C++ | A DuckDB ADBC Scanner Extension - adds support for using ADBC drivers with Du... |
| 4 | [agent_data](https://duckdb.org/community_extensions/extensions/agent_data.html) | [agent_data_duckdb](https://github.com/axsaucedo/agent_data_duckdb) | 🟢 Ongoing | 1 - 🔥 Very Active | 2 days ago (2026-06-09 13:34:22 UTC) | 18 | Python | DuckDB extension: agent_data by axsaucedo |
| 5 | [airport](https://duckdb.org/community_extensions/extensions/airport.html) | [airport](https://github.com/Query-farm/airport) | 🟢 Ongoing | 2 - ✅ Active | 12 days ago (2026-05-30 13:33:18 UTC) | 340 | C++ | The Airport extension for DuckDB, enables the use of Arrow Flight with DuckDB |
| 6 | [aixchess](https://duckdb.org/community_extensions/extensions/aixchess.html) | [aix](https://github.com/thomas-daniels/aix) | 🟢 Ongoing | 3 - 🟡 Stable | 74 days ago (2026-03-29 12:16:27 UTC) | 25 | Rust | Aix: Efficiently storing and querying chess game collections |
| 7 | [altertable](https://duckdb.org/community_extensions/extensions/altertable.html) | [duckdb-altertable](https://github.com/altertable-ai/duckdb-altertable) | 🟢 Ongoing | 1 - 🔥 Very Active | 3 days ago (2026-06-08 21:24:51 UTC) | 0 | C++ | Query Altertable's lakehouse directly from your local DuckDB |
| 8 | [anndata](https://duckdb.org/community_extensions/extensions/anndata.html) | [anndata-duckdb-extension](https://github.com/honicky/anndata-duckdb-extension) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-06-10 07:41:02 UTC) | 9 | C++ | Attach and AnnData file in duckdb and query it with SQL.  Perform SQL over gr... |
| 9 | [anofox_forecast](https://duckdb.org/community_extensions/extensions/anofox_forecast.html) | [anofox-forecast](https://github.com/DataZooDE/anofox-forecast) | 🟢 Ongoing | 2 - ✅ Active | 20 days ago (2026-05-22 13:30:21 UTC) | 35 | C++ | Statistical timeseries forecasting in DuckDB |
| 10 | [anofox_statistics](https://duckdb.org/community_extensions/extensions/anofox_statistics.html) | [anofox-statistics](https://github.com/DataZooDE/anofox-statistics) | ❓ Unknown | 1 - 🔥 Very Active | today (2026-06-12 07:16:07 UTC) | 9 | C++ | A DuckDB extension for statistical regression analysis, providing OLS, Ridge,... |
| 11 | [anofox_tabular](https://duckdb.org/community_extensions/extensions/anofox_tabular.html) | [anofox-tabular](https://github.com/DataZooDE/anofox-tabular) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-06-12 06:38:25 UTC) | 14 | C++ | A duckdb extension which combines data quality and data preparation tools for... |
| 12 | [arrow](https://duckdb.org/community_extensions/extensions/arrow.html) | [duckdb-extension-alias](https://github.com/duckdb/duckdb-extension-alias) | ❓ Unknown | 4 - 🟠 Stale | 248 days ago (2025-10-06 09:07:38 UTC) | 4 | C | DuckDB extension: arrow |
| 13 | [astro](https://duckdb.org/community_extensions/extensions/astro.html) | [astro-duck](https://github.com/synapticore-io/astro-duck) | 🟢 Ongoing | 2 - ✅ Active | 23 days ago (2026-05-19 12:22:23 UTC) | 1 | C++ | 60+ astronomical SQL functions for DuckDB: coordinate transforms, CCM89 dust... |
| 14 | [behavioral](https://duckdb.org/community_extensions/extensions/behavioral.html) | [duckdb-behavioral](https://github.com/tomtom215/duckdb-behavioral) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-06-12 06:26:26 UTC) | 11 | Rust | A DuckDB Community Extension to enable Behavioral Analytics, inspired by Clic... |
| 15 | [bigquery](https://duckdb.org/community_extensions/extensions/bigquery.html) | [duckdb-bigquery](https://github.com/hafenkran/duckdb-bigquery) | 🟢 Ongoing | 1 - 🔥 Very Active | 2 days ago (2026-06-10 07:35:03 UTC) | 162 | C++ | Integrates DuckDB with Google BigQuery, allowing direct querying and manageme... |
| 16 | [bitfilters](https://duckdb.org/community_extensions/extensions/bitfilters.html) | [bitfilters](https://github.com/Query-farm/bitfilters) | 🟢 Ongoing | 3 - 🟡 Stable | 45 days ago (2026-04-27 17:21:05 UTC) | 7 | C++ | A high-performance DuckDB extension providing probabilistic data structures f... |
| 17 | [blockduck](https://duckdb.org/community_extensions/extensions/blockduck.html) | [BlockDuck](https://github.com/luohaha/BlockDuck) | 🟢 Ongoing | 4 - 🟠 Stale | 246 days ago (2025-10-08 16:19:04 UTC) | 10 | C++ | Live SQL Queries on Blockchain |
| 18 | [boilstream](https://duckdb.org/community_extensions/extensions/boilstream.html) | [boilstream-extension](https://github.com/dforsber/boilstream-extension) | 🟢 Ongoing | 1 - 🔥 Very Active | 5 days ago (2026-06-06 11:38:11 UTC) | 10 | C++ | Secure Remote Secrets Storage for DuckDB |
| 19 | [brew](https://duckdb.org/community_extensions/extensions/brew.html) | [duckdb-brew](https://github.com/adriens/duckdb-brew) | 🟢 Ongoing | 2 - ✅ Active | 11 days ago (2026-05-31 08:18:52 UTC) | 1 | C++ | duckdb extension to report installed brew packages/casks/formulas with SQL |
| 20 | [bvh2sql](https://duckdb.org/community_extensions/extensions/bvh2sql.html) | [bvh2sql](https://github.com/nkwork9999/bvh2sql) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-06-10 11:29:23 UTC) | 0 | Makefile | SQL-related extension by nkwork9999 |
| 21 | [cache_httpfs](https://duckdb.org/community_extensions/extensions/cache_httpfs.html) | [duck-read-cache-fs](https://github.com/dentiny/duck-read-cache-fs) | 🟢 Ongoing | 1 - 🔥 Very Active | 3 days ago (2026-06-08 18:15:37 UTC) | 141 | C++ | This repository is made as read-only filesystem for remote access. |
| 22 | [cache_prewarm](https://duckdb.org/community_extensions/extensions/cache_prewarm.html) | [duckdb-cache-prewarm](https://github.com/dentiny/duckdb-cache-prewarm) | 🟢 Ongoing | 2 - ✅ Active | 17 days ago (2026-05-25 09:13:59 UTC) | 8 | C++ | DuckDB extension: cache_prewarm by dentiny |
| 23 | [capi_quack](https://duckdb.org/community_extensions/extensions/capi_quack.html) | [extension-template-c](https://github.com/duckdb/extension-template-c) | ❓ Unknown | 3 - 🟡 Stable | 77 days ago (2026-03-26 12:21:42 UTC) | 30 | C | (Experimental) C/C++ template for DuckDB extensions based on the C API |
| 24 | [cassandra](https://duckdb.org/community_extensions/extensions/cassandra.html) | [duckdb-cassandra](https://github.com/dioptre/duckdb-cassandra) | ❓ Unknown | 4 - 🟠 Stale | 234 days ago (2025-10-20 19:15:10 UTC) | 2 | C++ | DuckDB Connector for Cassandra |
| 25 | [celestial](https://duckdb.org/community_extensions/extensions/celestial.html) | [duckdb-celestial](https://github.com/lisa-sgs/duckdb-celestial) | 🟢 Ongoing | 3 - 🟡 Stable | 90 days ago (2026-03-13 14:47:49 UTC) | 2 | C++ | DuckDB extension providing astronomical coordinates utilities |
| 26 | [chaos](https://duckdb.org/community_extensions/extensions/chaos.html) | [duckdb-chaos](https://github.com/taniabogatsch/duckdb-chaos) | 🟢 Ongoing | 4 - 🟠 Stale | 119 days ago (2026-02-12 14:50:01 UTC) | 1 | C++ | DuckDB extension: chaos by taniabogatsch |
| 27 | [chess](https://duckdb.org/community_extensions/extensions/chess.html) | [duckdb-chess](https://github.com/dotneB/duckdb-chess) | ❓ Unknown | 2 - ✅ Active | 15 days ago (2026-05-28 05:13:34 UTC) | 3 | Rust | A DuckDB extension for parsing and analyzing chess games in PGN format. |
| 28 | [chsql](https://duckdb.org/community_extensions/extensions/chsql.html) | [clickhouse-sql](https://github.com/Query-farm/clickhouse-sql) | ❓ Unknown | 4 - 🟠 Stale | 113 days ago (2026-02-18 19:49:47 UTC) | 91 | C++ | DuckDB Community Extension implementing ClickHouse SQL Dialect macros and Cus... |
| 29 | [chsql_native](https://duckdb.org/community_extensions/extensions/chsql_native.html) | [clickhouse-native](https://github.com/Query-farm/clickhouse-native) | ❓ Unknown | 4 - 🟠 Stale | 113 days ago (2026-02-18 19:49:46 UTC) | 20 | Rust | Experimental ClickHouse Native Client and Native file reader Extension for Du... |
| 30 | [cityjson](https://duckdb.org/community_extensions/extensions/cityjson.html) | [duckdb-cityjson](https://github.com/cityjson/duckdb-cityjson) | 🟢 Ongoing | 3 - 🟡 Stable | 41 days ago (2026-05-01 11:22:55 UTC) | 9 | C++ | Data format handling extension by cityjson |
| 31 | [clamp](https://duckdb.org/community_extensions/extensions/clamp.html) | [duckdb_clamp](https://github.com/oglego/duckdb_clamp) | 🟢 Ongoing | 3 - 🟡 Stable | 47 days ago (2026-04-26 01:35:35 UTC) | 2 | C++ | The Clamp extension introduces range-clamping scalar functions to DuckDB. Ini... |
| 32 | [cloudfront](https://duckdb.org/community_extensions/extensions/cloudfront.html) | [duckdb-cloudfront](https://github.com/midwork-finds-jobs/duckdb-cloudfront) | 🟢 Ongoing | 4 - 🟠 Stale | 126 days ago (2026-02-05 15:32:51 UTC) | 1 | C++ | DuckDB module which provides custom authentication methods on top of httpfs m... |
| 33 | [cozip](https://duckdb.org/community_extensions/extensions/cozip.html) | [cozip_reader](https://github.com/asterisk-labs/cozip_reader) | 🟢 Ongoing | 2 - ✅ Active | 28 days ago (2026-05-15 05:12:11 UTC) | 6 | C++ | Read Cloud-Optimized ZIP files |
| 34 | [crawler](https://duckdb.org/community_extensions/extensions/crawler.html) | [duckdb-crawler](https://github.com/midwork-finds-jobs/duckdb-crawler) | 🟢 Ongoing | 3 - 🟡 Stable | 70 days ago (2026-04-03 04:32:07 UTC) | 11 | C++ | DuckDB extension: crawler by midwork-finds-jobs |
| 35 | [cronjob](https://duckdb.org/community_extensions/extensions/cronjob.html) | [cronjob](https://github.com/Query-farm/cronjob) | 🟢 Ongoing | 3 - 🟡 Stable | 74 days ago (2026-03-29 21:04:33 UTC) | 50 | C++ | DuckDB CronJob Extension |
| 36 | [crypto](https://duckdb.org/community_extensions/extensions/crypto.html) | [crypto](https://github.com/Query-farm/crypto) | 🟢 Ongoing | 3 - 🟡 Stable | 50 days ago (2026-04-22 13:25:10 UTC) | 28 | C++ | DuckDB Extension for cryptographic hash functions and HMAC |
| 37 | [curl_httpfs](https://duckdb.org/community_extensions/extensions/curl_httpfs.html) | [duckdb-curl-filesystem](https://github.com/dentiny/duckdb-curl-filesystem) | 🟢 Ongoing | 2 - ✅ Active | 18 days ago (2026-05-24 10:09:45 UTC) | 8 | C++ | Filesystem built upon libcurl. |
| 38 | [cwiqduck](https://duckdb.org/community_extensions/extensions/cwiqduck.html) | [cwiqduck](https://github.com/cwiq-os/cwiqduck) | 🟢 Ongoing | 1 - 🔥 Very Active | 3 days ago (2026-06-09 02:28:38 UTC) | 3 | C++ | DuckDB extensions for CWIQ |
| 39 | [dash](https://duckdb.org/community_extensions/extensions/dash.html) | [dash](https://github.com/gropaul/dash) | 🟢 Ongoing | 2 - ✅ Active | 18 days ago (2026-05-24 20:40:00 UTC) | 67 | C++ | Local GUI and Data Canvas as a DuckDB extension |
| 40 | [datasketches](https://duckdb.org/community_extensions/extensions/datasketches.html) | [datasketches](https://github.com/Query-farm/datasketches) | 🟢 Ongoing | 3 - 🟡 Stable | 45 days ago (2026-04-27 17:17:18 UTC) | 47 | C++ | Integrates DuckDB with the high-performance Apache DataSketches library. This... |
| 41 | [dazzleduck](https://duckdb.org/community_extensions/extensions/dazzleduck.html) | [dazzleduck-sql-duckdb](https://github.com/dazzleduck-web/dazzleduck-sql-duckdb) | ❓ Unknown | 4 - 🟠 Stale | 91 days ago (2026-03-12 22:24:42 UTC) | 1 | C++ | DuckDB extension: dazzleduck by dazzleduck-web |
| 42 | [decimal_arithmetic](https://duckdb.org/community_extensions/extensions/decimal_arithmetic.html) | [duckdb-decimal-arithmetic](https://github.com/duckdb/duckdb-decimal-arithmetic) | 🟢 Ongoing | 2 - ✅ Active | 9 days ago (2026-06-02 11:19:37 UTC) | 2 | C++ | DuckDB extension: decimal_arithmetic |
| 43 | [delta_classic](https://duckdb.org/community_extensions/extensions/delta_classic.html) | [delta_classic](https://github.com/djouallah/delta_classic) | 🟢 Ongoing | 4 - 🟠 Stale | 91 days ago (2026-03-13 00:57:38 UTC) | 5 | C++ | DuckDB extension to attach a directory of Delta tables as a database |
| 44 | [delta_export](https://duckdb.org/community_extensions/extensions/delta_export.html) | [delta_export](https://github.com/djouallah/delta_export) | 🟢 Ongoing | 4 - 🟠 Stale | 91 days ago (2026-03-13 07:02:40 UTC) | 7 | C++ | DuckDB extension to export Delta Lake metadata from DuckLake |
| 45 | [dicom](https://duckdb.org/community_extensions/extensions/dicom.html) | [duck-dicom](https://github.com/nmontesg/duck-dicom) | 🟢 Ongoing | 1 - 🔥 Very Active | 4 days ago (2026-06-07 20:06:19 UTC) | 0 | C++ | A DuckDB extension to import medical imaging data |
| 46 | [dns](https://duckdb.org/community_extensions/extensions/dns.html) | [duckdb-dns](https://github.com/tobilg/duckdb-dns) | 🟢 Ongoing | 1 - 🔥 Very Active | 6 days ago (2026-06-05 16:58:49 UTC) | 16 | Rust | DNS (Reverse) Lookup Extension for DuckDB |
| 47 | [dplyr](https://duckdb.org/community_extensions/extensions/dplyr.html) | [libdplyr](https://github.com/mrchypark/libdplyr) | 🟢 Ongoing | 2 - ✅ Active | 29 days ago (2026-05-14 03:14:54 UTC) | 14 | Rust | DuckDB extension: dplyr by mrchypark |
| 48 | [dqtest](https://duckdb.org/community_extensions/extensions/dqtest.html) | [duckdb-dataquality-extension](https://github.com/vhe74/duckdb-dataquality-extension) | ❓ Unknown | 4 - 🟠 Stale | 128 days ago (2026-02-03 18:35:04 UTC) | 5 | C++ | Duckdb extension to run data quality tests |
| 49 | [dta](https://duckdb.org/community_extensions/extensions/dta.html) | [duckdb-dta](https://github.com/codedthinking/duckdb-dta) | 🟢 Ongoing | 2 - ✅ Active | 10 days ago (2026-06-01 10:35:57 UTC) | 0 | C++ | DuckDB extension for reading and writing .dta files (formats 117-121) |
| 50 | [duck_block_utils](https://duckdb.org/community_extensions/extensions/duck_block_utils.html) | [duckdb_duck_block_utils](https://github.com/teaguesterling/duckdb_duck_block_utils) | 🟢 Ongoing | 2 - ✅ Active | 11 days ago (2026-05-31 20:28:51 UTC) | 1 | C++ | A collection of utility functions to work with doc block-style structures and... |
| 51 | [duck_delta_share](https://duckdb.org/community_extensions/extensions/duck_delta_share.html) | [duck_delta_share](https://github.com/cwiq-os/duck_delta_share) | 🟢 Ongoing | 3 - 🟡 Stable | 32 days ago (2026-05-10 23:39:27 UTC) | 5 | C++ | DuckDB extension for enabling Delta Sharing client capabilities.  |
| 52 | [duck_dggs](https://duckdb.org/community_extensions/extensions/duck_dggs.html) | [duckdb-dggs](https://github.com/am2222/duckdb-dggs) | 🟢 Ongoing | 3 - 🟡 Stable | 40 days ago (2026-05-02 18:08:43 UTC) | 1 | C++ | A DuckDB extension for discrete global grid systems (DGGS) powered by DGGRID v8. |
| 53 | [duck_geoarrow](https://duckdb.org/community_extensions/extensions/duck_geoarrow.html) | [duck_geoarrow](https://github.com/am2222/duck_geoarrow) | 🟢 Ongoing | 3 - 🟡 Stable | 57 days ago (2026-04-15 13:13:55 UTC) | 6 | C++ | This extension, Duck_Geoarrow, provides functions to convert between WKB (Wel... |
| 54 | [duck_hunt](https://duckdb.org/community_extensions/extensions/duck_hunt.html) | [duck_hunt](https://github.com/teaguesterling/duck_hunt) | 🟢 Ongoing | 2 - ✅ Active | 11 days ago (2026-05-31 20:09:43 UTC) | 3 | C++ | Tools for working with unit test suite results |
| 55 | [duck_lineage](https://duckdb.org/community_extensions/extensions/duck_lineage.html) | [duck_lineage](https://github.com/ilum-cloud/duck_lineage) | 🟢 Ongoing | 2 - ✅ Active | 16 days ago (2026-05-26 23:21:55 UTC) | 76 | Python | A extension for DuckDB, which captures lineage events for executed queries |
| 56 | [duck_lk](https://duckdb.org/community_extensions/extensions/duck_lk.html) | [duck-lk](https://github.com/nrminor/duck-lk) | 🟢 Ongoing | 3 - 🟡 Stable | 55 days ago (2026-04-18 03:05:52 UTC) | 0 | Rust | Interact with tables from your LabKey LIMS natively in DuckDB |
| 57 | [duck_tails](https://duckdb.org/community_extensions/extensions/duck_tails.html) | [duck_tails](https://github.com/teaguesterling/duck_tails) | 🟢 Ongoing | 1 - 🔥 Very Active | 2 days ago (2026-06-09 16:53:48 UTC) | 16 | C++ | A DuckDB extension for exploring and reading git history. |
| 58 | [duckdb_delta_sharing](https://duckdb.org/community_extensions/extensions/duckdb_delta_sharing.html) | [duckdb-delta-sharing](https://github.com/prequel-co/duckdb-delta-sharing) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-06-11 19:52:08 UTC) | 3 | C++ | An extension for using DuckDB as a delta sharing client |
| 59 | [duckdb_geoip_rs](https://duckdb.org/community_extensions/extensions/duckdb_geoip_rs.html) | [duckdb-geoip-rs](https://github.com/william-billaud/duckdb-geoip-rs) | 🟢 Ongoing | 2 - ✅ Active | 21 days ago (2026-05-21 21:23:32 UTC) | 6 | Rust | Database connectivity extension by william-billaud |
| 60 | [duckdb_mcp](https://duckdb.org/community_extensions/extensions/duckdb_mcp.html) | [duckdb_mcp](https://github.com/teaguesterling/duckdb_mcp) | 🟢 Ongoing | 1 - 🔥 Very Active | 4 days ago (2026-06-07 20:12:55 UTC) | 54 | C++ | A simple MCP server extension for DuckDB |
| 61 | [duckdb_midi](https://github.com/nkwork9999/duckdb-midi) | [duckdb-midi](https://github.com/nkwork9999/duckdb-midi) | ❓ Unknown | 1 - 🔥 Very Active | 4 days ago (2026-06-07 15:55:12 UTC) | 0 | C++ | Database connectivity extension by nkwork9999 |
| 62 | [duckdb_zarr](https://duckdb.org/community_extensions/extensions/duckdb_zarr.html) | [duckdb_zarr](https://github.com/WayScience/duckdb_zarr) | 🟢 Ongoing | 3 - 🟡 Stable | 74 days ago (2026-03-29 23:42:57 UTC) | 6 | C++ | A DuckDB extension for querying Zarr arrays with SQL through relational proje... |
| 63 | [duckdbi](https://duckdb.org/community_extensions/extensions/duckdbi.html) | [DuckDBI](https://github.com/nkwork9999/DuckDBI) | 🟢 Ongoing | 3 - 🟡 Stable | 89 days ago (2026-03-14 11:04:19 UTC) | 3 | C++ | Database connectivity extension by nkwork9999 |
| 64 | [duckgl](https://duckdb.org/community_extensions/extensions/duckgl.html) | [duckgl](https://github.com/nkwork9999/duckgl) | 🟢 Ongoing | 4 - 🟠 Stale | 99 days ago (2026-03-04 16:41:20 UTC) | 7 | C++ | DuckDB extension: duckgl by nkwork9999 |
| 65 | [duckherder](https://duckdb.org/community_extensions/extensions/duckherder.html) | [duckdb-distributed-execution](https://github.com/dentiny/duckdb-distributed-execution) | ❓ Unknown | 4 - 🟠 Stale | 93 days ago (2026-03-10 09:36:00 UTC) | 59 | C++ | Distributed execution for duckdb queries. |
| 66 | [duckhog](https://duckdb.org/community_extensions/extensions/duckhog.html) | [duckhog](https://github.com/PostHog/duckhog) | ❓ Unknown | 2 - ✅ Active | 16 days ago (2026-05-26 17:05:33 UTC) | 7 | C++ | duckdb extension to connect to posthog managed data warehouse  |
| 67 | [duckhts](https://duckdb.org/community_extensions/extensions/duckhts.html) | [duckhts](https://github.com/RGenomicsETL/duckhts) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-06-11 05:01:29 UTC) | 15 | C | 'htslib' based 'Duckdb' Extenstion for High Throughput Sequencing File Formats |
| 68 | [ducklake_cdc](https://duckdb.org/community_extensions/extensions/ducklake_cdc.html) | [ducklake-cdc-extension](https://github.com/ekkuleivonen/ducklake-cdc-extension) | ❓ Unknown | 3 - 🟡 Stable | 36 days ago (2026-05-06 19:37:35 UTC) | 15 | C++ | The missing operational layer for DuckLake’s change feed. |
| 69 | [ducknng](https://github.com/sounkou-bioinfo/ducknng) | [ducknng](https://github.com/sounkou-bioinfo/ducknng) | ❓ Unknown | 1 - 🔥 Very Active | 4 days ago (2026-06-07 13:14:13 UTC) | 2 | C | ducknng: a 'DuckDB' Binding To The 'NNG' Scalability Protocols Library And an... |
| 70 | [duckorch](https://duckdb.org/community_extensions/extensions/duckorch.html) | [duck-orch](https://github.com/nkwork9999/duck-orch) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-06-11 17:28:09 UTC) | 2 | Rust | DuckDB extension: duckorch by nkwork9999 |
| 71 | [duckpgq](https://duckdb.org/community_extensions/extensions/duckpgq.html) | [duckpgq-extension](https://github.com/cwida/duckpgq-extension) | ❓ Unknown | 3 - 🟡 Stable | 63 days ago (2026-04-09 13:13:43 UTC) | 416 | C++ | DuckDB extension that adds support for SQL/PGQ and graph algorithms |
| 72 | [ducksmiles](https://duckdb.org/community_extensions/extensions/ducksmiles.html) | [duckSMILES](https://github.com/nkwork9999/duckSMILES) | 🟢 Ongoing | 1 - 🔥 Very Active | 4 days ago (2026-06-07 12:33:47 UTC) | 1 | Rust | DuckDB extension: ducksmiles by nkwork9999 |
| 73 | [ducksync](https://duckdb.org/community_extensions/extensions/ducksync.html) | [ducksync](https://github.com/danjsiegel/ducksync) | 🟢 Ongoing | 2 - ✅ Active | 8 days ago (2026-06-03 17:22:43 UTC) | 7 | C++ | DuckDB extension: ducksync by danjsiegel |
| 74 | [ducktinycc](https://duckdb.org/community_extensions/extensions/ducktinycc.html) | [DuckTinyCC](https://github.com/sounkou-bioinfo/DuckTinyCC) | 🟢 Ongoing | 2 - ✅ Active | 30 days ago (2026-05-13 06:09:08 UTC) | 3 | C | 'C' Scripting in 'Duckdb' using 'TinyCC' |
| 75 | [eeagrid](https://duckdb.org/community_extensions/extensions/eeagrid.html) | [duckdb-eeagrid](https://github.com/ahuarte47/duckdb-eeagrid) | 🟢 Ongoing | 2 - ✅ Active | 22 days ago (2026-05-20 16:03:05 UTC) | 0 | C++ | Functions for transforming XY coordinates to and from the EEA Reference Grid... |
| 76 | [eenddb](https://duckdb.org/community_extensions/extensions/eenddb.html) | [eenddb](https://github.com/Dtenwolde/eenddb) | 🟢 Ongoing | 3 - 🟡 Stable | 72 days ago (2026-03-31 09:31:58 UTC) | 5 | C++ | Database connectivity extension by Dtenwolde |
| 77 | [elasticsearch](https://duckdb.org/community_extensions/extensions/elasticsearch.html) | [duckdb-elasticsearch](https://github.com/tlinhart/duckdb-elasticsearch) | ❓ Unknown | 3 - 🟡 Stable | 43 days ago (2026-04-29 13:01:51 UTC) | 19 | C++ | Query Elasticsearch data directly from DuckDB |
| 78 | [erpl_web](https://duckdb.org/community_extensions/extensions/erpl_web.html) | [erpl-web](https://github.com/DataZooDE/erpl-web) | 🟢 Ongoing | 2 - ✅ Active | 8 days ago (2026-06-03 12:22:03 UTC) | 27 | C++ | ERPL is a DuckDB extension to connect to API based ecosystems via standard in... |
| 79 | [eurostat](https://duckdb.org/community_extensions/extensions/eurostat.html) | [duckdb-eurostat](https://github.com/ahuarte47/duckdb-eurostat) | 🟢 Ongoing | 2 - ✅ Active | 22 days ago (2026-05-20 21:28:22 UTC) | 31 | C++ | DuckDB extension for reading data from EUROSTAT database using SQL  |
| 80 | [evalexpr_rhai](https://duckdb.org/community_extensions/extensions/evalexpr_rhai.html) | [evalexpr_rhai](https://github.com/Query-farm/evalexpr_rhai) | 🟢 Ongoing | 3 - 🟡 Stable | 50 days ago (2026-04-23 01:40:35 UTC) | 25 | C++ | A DuckDB extension to evaluate the Rhai scripting language as part of SQL. |
| 81 | [events](https://duckdb.org/community_extensions/extensions/events.html) | [events](https://github.com/Query-farm/events) | 🟢 Ongoing | 3 - 🟡 Stable | 57 days ago (2026-04-15 12:59:21 UTC) | 2 | C++ | Capture database events and deliver JSON notifications to external programs v... |
| 82 | [faiss](https://duckdb.org/community_extensions/extensions/faiss.html) | [duckdb-faiss-ext](https://github.com/duckdb-faiss-ext/duckdb-faiss-ext) | 🟢 Ongoing | 4 - 🟠 Stale | 94 days ago (2026-03-09 11:54:02 UTC) | 31 | Go | DuckDB wrapper for FAISS - Experimental |
| 83 | [fakeit](https://duckdb.org/community_extensions/extensions/fakeit.html) | [duckdb-fakeit](https://github.com/tobilg/duckdb-fakeit) | 🟢 Ongoing | 1 - 🔥 Very Active | 6 days ago (2026-06-05 16:44:37 UTC) | 13 | Rust | DuckDB extension: fakeit by tobilg |
| 84 | [file_dialog](https://duckdb.org/community_extensions/extensions/file_dialog.html) | [duckdb-ext-file-dialog](https://github.com/yutannihilation/duckdb-ext-file-dialog) | 🟢 Ongoing | 2 - ✅ Active | 16 days ago (2026-05-27 00:05:12 UTC) | 15 | Rust | A DuckDB extension to choose file interactively using native file open dialogs |
| 85 | [finetype](https://duckdb.org/community_extensions/extensions/finetype.html) | [finetype](https://github.com/meridian-online/finetype) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-06-12 07:41:06 UTC) | 0 | Rust | Precision format detection for text data. Semantic type inference with transf... |
| 86 | [fire_duck_ext](https://duckdb.org/community_extensions/extensions/fire_duck_ext.html) | [fire_duck_ext](https://github.com/BorisBesky/fire_duck_ext) | 🟢 Ongoing | 3 - 🟡 Stable | 47 days ago (2026-04-25 17:50:34 UTC) | 3 | C++ | duckdb extension for firestore |
| 87 | [firebird](https://duckdb.org/community_extensions/extensions/firebird.html) | [duckdb-firebird](https://github.com/flozer/duckdb-firebird) | 🟢 Ongoing | 2 - ✅ Active | 8 days ago (2026-06-03 16:54:24 UTC) | 4 | C++ | DuckDB extension: firebird by flozer |
| 88 | [fit](https://duckdb.org/community_extensions/extensions/fit.html) | [duckdb-fit-extension](https://github.com/antoriche/duckdb-fit-extension) | 🟢 Ongoing | 4 - 🟠 Stale | 178 days ago (2025-12-15 19:16:40 UTC) | 1 | C++ | DuckDB extension: fit by antoriche |
| 89 | [fivetran](https://duckdb.org/community_extensions/extensions/fivetran.html) | [duckdb_sparse_variant](https://github.com/fivetran/duckdb_sparse_variant) | 🟢 Ongoing | 2 - ✅ Active | 23 days ago (2026-05-19 07:42:06 UTC) | 0 | C++ | A DuckDB extension providing sparse VARIANT encoding for STRUCTs and an optim... |
| 90 | [flock](https://duckdb.org/community_extensions/extensions/flock.html) | [flock](https://github.com/dais-polymtl/flock) | 🟢 Ongoing | 1 - 🔥 Very Active | 7 days ago (2026-06-04 19:36:13 UTC) | 342 | C++ | Beyond Quacking: Deep Integration of Language Models and RAG into DuckDB (VLD... |
| 91 | [fsquery](https://duckdb.org/community_extensions/extensions/fsquery.html) | [fsquery](https://github.com/halgari/fsquery) | 🟢 Ongoing | 3 - 🟡 Stable | 87 days ago (2026-03-16 16:09:24 UTC) | 1 | C++ | An extension that allows DuckDB to enumerate and stat files on the disk |
| 92 | [func_apply](https://duckdb.org/community_extensions/extensions/func_apply.html) | [duckdb_func_apply](https://github.com/teaguesterling/duckdb_func_apply) | 🟢 Ongoing | 2 - ✅ Active | 11 days ago (2026-05-31 20:11:00 UTC) | 3 | C++ | An exension to allow dynamic function application |
| 93 | [fuzzycomplete](https://duckdb.org/community_extensions/extensions/fuzzycomplete.html) | [fuzzycomplete](https://github.com/Query-farm/fuzzycomplete) | 🟢 Ongoing | 3 - 🟡 Stable | 74 days ago (2026-03-29 21:04:37 UTC) | 28 | C++ | DuckDB Extension for fuzzy string matching based autocompletion |
| 94 | [gaggle](https://duckdb.org/community_extensions/extensions/gaggle.html) | [gaggle](https://github.com/CogitatorTech/gaggle) | 🟢 Ongoing | 2 - ✅ Active | 18 days ago (2026-05-24 17:09:37 UTC) | 17 | Rust | A DuckDB extension for working with Kaggle datasets |
| 95 | [gcs](https://duckdb.org/community_extensions/extensions/gcs.html) | [duckdb-gcs](https://github.com/northpolesec/duckdb-gcs) | 🟢 Ongoing | 2 - ✅ Active | 21 days ago (2026-05-21 11:15:37 UTC) | 22 | C++ | A GCS-native extension for DuckDB |
| 96 | [gdx](https://duckdb.org/community_extensions/extensions/gdx.html) | [duckdb-gdx](https://github.com/chrispahm/duckdb-gdx) | ❓ Unknown | 2 - ✅ Active | 20 days ago (2026-05-22 08:05:29 UTC) | 1 | C++ | DuckDB extension: gdx by chrispahm |
| 97 | [geography](https://duckdb.org/community_extensions/extensions/geography.html) | [duckdb-geography](https://github.com/paleolimbot/duckdb-geography) | ❓ Unknown | 4 - 🟠 Stale | 91 days ago (2026-03-12 16:05:00 UTC) | 45 | C++ | Geospatial data extension by paleolimbot |
| 98 | [geosilo](https://duckdb.org/community_extensions/extensions/geosilo.html) | [geosilo](https://github.com/Query-farm/geosilo) | 🟢 Ongoing | 3 - 🟡 Stable | 45 days ago (2026-04-27 16:21:07 UTC) | 25 | C++ | DuckDB extension for compact geometry encoding using delta-encoded coordinate... |
| 99 | [geotiff](https://duckdb.org/community_extensions/extensions/geotiff.html) | [duckdb-geotiff](https://github.com/babaknaimi/duckdb-geotiff) | ❓ Unknown | 4 - 🟠 Stale | 296 days ago (2025-08-20 05:12:15 UTC) | 2 | C++ | Duckdb extension to read GeoTiffs directly with duckdb database |
| 100 | [ggsql](https://duckdb.org/community_extensions/extensions/ggsql.html) | [ggsql-duckdb](https://github.com/posit-dev/ggsql-duckdb) | 🟢 Ongoing | 2 - ✅ Active | 24 days ago (2026-05-19 06:12:36 UTC) | 17 | Rust | A DuckDB extension adding support for ggsql  |
| 101 | [gh](https://duckdb.org/community_extensions/extensions/gh.html) | [duckdb-gh](https://github.com/carlopi/duckdb-gh) | 🟢 Ongoing | 3 - 🟡 Stable | 43 days ago (2026-04-29 14:21:02 UTC) | 4 | C++ | DuckDB extension: gh by carlopi |
| 102 | [gsheets](https://duckdb.org/community_extensions/extensions/gsheets.html) | [duckdb_gsheets](https://github.com/evidence-dev/duckdb_gsheets) | 🟢 Ongoing | 4 - 🟠 Stale | 111 days ago (2026-02-21 04:11:04 UTC) | 345 | C++ | DuckDB extension to read and write Google Sheets using SQL |
| 103 | [h3](https://duckdb.org/community_extensions/extensions/h3.html) | [h3-duckdb](https://github.com/isaacbrodsky/h3-duckdb) | 🟢 Ongoing | 2 - ✅ Active | 18 days ago (2026-05-24 15:42:28 UTC) | 248 | C++ | Bindings for H3 to DuckDB |
| 104 | [h5db](https://duckdb.org/community_extensions/extensions/h5db.html) | [h5db](https://github.com/jokasimr/h5db) | 🟢 Ongoing | 1 - 🔥 Very Active | 4 days ago (2026-06-07 10:55:50 UTC) | 1 | C++ | Duckdb extension for reading HDF5 files. |
| 105 | [harbor](https://duckdb.org/community_extensions/extensions/harbor.html) | [duckdb-harbor](https://github.com/shreeve/duckdb-harbor) | 🟢 Ongoing | 1 - 🔥 Very Active | 2 days ago (2026-06-10 04:49:21 UTC) | 0 | C++ | HTTP server for DuckDB UI, JSON /sql, and CLI |
| 106 | [hashfuncs](https://duckdb.org/community_extensions/extensions/hashfuncs.html) | [hashfuncs](https://github.com/Query-farm/hashfuncs) | 🟢 Ongoing | 3 - 🟡 Stable | 74 days ago (2026-03-29 21:04:38 UTC) | 12 | C++ | A DuckDB extension that supplies non-cryptographic hash functions. |
| 107 | [hdf5](https://duckdb.org/community_extensions/extensions/hdf5.html) | [duckdb-hdf5](https://github.com/Berrysoft/duckdb-hdf5) | ❓ Unknown | 3 - 🟡 Stable | 50 days ago (2026-04-23 01:30:36 UTC) | 12 | Rust | HDF5 plugin for duckdb |
| 108 | [hedged_request_fs](https://duckdb.org/community_extensions/extensions/hedged_request_fs.html) | [duckdb-hedged-request](https://github.com/dentiny/duckdb-hedged-request) | 🟢 Ongoing | 2 - ✅ Active | 18 days ago (2026-05-24 09:35:49 UTC) | 1 | C++ | DuckDB extension: hedged_request_fs by dentiny |
| 109 | [highs](https://duckdb.org/community_extensions/extensions/highs.html) | [HiGHS-duckdb](https://github.com/fhk/HiGHS-duckdb) | ❓ Unknown | 4 - 🟠 Stale | 107 days ago (2026-02-25 02:07:48 UTC) | 1 | C++ | Run the solver in the database! |
| 110 | [hive_metastore](https://duckdb.org/community_extensions/extensions/hive_metastore.html) | [duckdb-hive-metastore](https://github.com/ilum-cloud/duckdb-hive-metastore) | 🟢 Ongoing | 2 - ✅ Active | 20 days ago (2026-05-22 17:49:59 UTC) | 4 | C++ | DuckDB extension allowing to connect to Apache Hive Metastore and query the d... |
| 111 | [hnsw_acorn](https://duckdb.org/community_extensions/extensions/hnsw_acorn.html) | [duckdb-hnsw-acorn](https://github.com/cigrainger/duckdb-hnsw-acorn) | 🟢 Ongoing | 3 - 🟡 Stable | 75 days ago (2026-03-28 07:49:47 UTC) | 63 | C++ | ACORN-1 pre-filtered HNSW search for DuckDB |
| 112 | [holtfs](https://duckdb.org/community_extensions/extensions/holtfs.html) | [duckdb-holtfs](https://github.com/feichai0017/duckdb-holtfs) | 🟢 Ongoing | 2 - ✅ Active | 16 days ago (2026-05-27 06:55:19 UTC) | 0 | C++ | DuckDB extension for planning scans through Holt-backed metadata indexes |
| 113 | [hostfs](https://duckdb.org/community_extensions/extensions/hostfs.html) | [hostFS](https://github.com/gropaul/hostFS) | ❓ Unknown | 4 - 🟠 Stale | 253 days ago (2025-10-01 21:02:13 UTC) | 31 | C++ | DuckDB extension: hostfs by gropaul |
| 114 | [html_query](https://duckdb.org/community_extensions/extensions/html_query.html) | [duckdb_html_query](https://github.com/midwork-finds-jobs/duckdb_html_query) | ❓ Unknown | 4 - 🟠 Stale | 126 days ago (2026-02-05 15:33:13 UTC) | 2 | Rust | Filter HTML inside duckdb |
| 115 | [html_readability](https://duckdb.org/community_extensions/extensions/html_readability.html) | [duckdb-html-readability](https://github.com/midwork-finds-jobs/duckdb-html-readability) | ❓ Unknown | 4 - 🟠 Stale | 126 days ago (2026-02-05 15:33:16 UTC) | 0 | Rust | DuckDB extension to parse html to readable text |
| 116 | [http_client](https://duckdb.org/community_extensions/extensions/http_client.html) | [httpclient](https://github.com/Query-farm/httpclient) | 🟢 Ongoing | 3 - 🟡 Stable | 57 days ago (2026-04-15 14:08:54 UTC) | 79 | C++ | DuckDB HTTP GET/POST Client in a Community Extension |
| 117 | [http_request](https://duckdb.org/community_extensions/extensions/http_request.html) | [duckdb_http_request](https://github.com/midwork-finds-jobs/duckdb_http_request) | ❓ Unknown | 4 - 🟠 Stale | 114 days ago (2026-02-17 13:03:03 UTC) | 3 | C++ | Uses the native duckdb httputil to make extra requests in SELECT |
| 118 | [http_stats](https://duckdb.org/community_extensions/extensions/http_stats.html) | [duckdb-http-stats](https://github.com/tlinhart/duckdb-http-stats) | 🟢 Ongoing | 3 - 🟡 Stable | 76 days ago (2026-03-27 13:58:03 UTC) | 1 | C++ | Better HTTP statistics for DuckDB |
| 119 | [httpd_log](https://duckdb.org/community_extensions/extensions/httpd_log.html) | [duckdb-httpd-log](https://github.com/saygox/duckdb-httpd-log) | ❓ Unknown | 4 - 🟠 Stale | 151 days ago (2026-01-12 06:14:58 UTC) | 0 | C++ | duckdb extension |
| 120 | [httpfs_timeout_retry](https://duckdb.org/community_extensions/extensions/httpfs_timeout_retry.html) | [duckdb-httpfs-timeout-retry](https://github.com/dentiny/duckdb-httpfs-timeout-retry) | 🟢 Ongoing | 2 - ✅ Active | 18 days ago (2026-05-24 10:38:20 UTC) | 0 | C++ | Web/HTTP functionality extension by dentiny |
| 121 | [httpserver](https://duckdb.org/community_extensions/extensions/httpserver.html) | [httpserver](https://github.com/Query-farm/httpserver) | ❓ Unknown | 3 - 🟡 Stable | 59 days ago (2026-04-13 23:57:25 UTC) | 279 | C++ | DuckDB HTTP API Server and Query Interface in a  Community Extension |
| 122 | [infera](https://duckdb.org/community_extensions/extensions/infera.html) | [infera](https://github.com/CogitatorTech/infera) | 🟢 Ongoing | 2 - ✅ Active | 18 days ago (2026-05-24 17:20:54 UTC) | 132 | Rust | A DuckDB extension for in-database inference |
| 123 | [inflector](https://duckdb.org/community_extensions/extensions/inflector.html) | [inflector](https://github.com/Query-farm/inflector) | 🟢 Ongoing | 2 - ✅ Active | 21 days ago (2026-05-21 12:33:21 UTC) | 8 | C++ | Powerful string case transformation and inflection capabilities directly to y... |
| 124 | [ion](https://duckdb.org/community_extensions/extensions/ion.html) | [duckdb-ion](https://github.com/kestra-io/duckdb-ion) | 🟢 Ongoing | 4 - 🟠 Stale | 93 days ago (2026-03-10 15:49:39 UTC) | 4 | C++ | AWS Ion extension for DuckDB |
| 125 | [json_schema](https://duckdb.org/community_extensions/extensions/json_schema.html) | [json_schema](https://github.com/Query-farm/json_schema) | 🟢 Ongoing | 3 - 🟡 Stable | 74 days ago (2026-03-29 21:04:43 UTC) | 3 | C++ | A DuckDB extension that bring support for validating JSON data using JSON sch... |
| 126 | [jsonata](https://duckdb.org/community_extensions/extensions/jsonata.html) | [jsonata](https://github.com/Query-farm/jsonata) | 🟢 Ongoing | 3 - 🟡 Stable | 37 days ago (2026-05-05 11:01:27 UTC) | 6 | C++ | The JSONata extension for DuckDB enables expressive, JSON-focused querying an... |
| 127 | [jwt](https://duckdb.org/community_extensions/extensions/jwt.html) | [duckdb_jwt](https://github.com/GalvinGao/duckdb_jwt) | ❓ Unknown | 4 - 🟠 Stale | 338 days ago (2025-07-09 00:13:56 UTC) | 0 | C++ | DuckDB extension: jwt by GalvinGao |
| 128 | [keboola](https://duckdb.org/community_extensions/extensions/keboola.html) | [duckdb-extension](https://github.com/keboola/duckdb-extension) | 🟢 Ongoing | 2 - ✅ Active | 23 days ago (2026-05-19 23:33:34 UTC) | 0 | C++ | DuckDB extension for Keboola Storage — query and write Keboola tables using s... |
| 129 | [lastra](https://duckdb.org/community_extensions/extensions/lastra.html) | [duckdb-lastra](https://github.com/QTSurfer/duckdb-lastra) | 🟢 Ongoing | 3 - 🟡 Stable | 31 days ago (2026-05-11 12:15:36 UTC) | 0 | C++ | DuckDB extension for reading Lastra columnar time series files natively |
| 130 | [latency_injection_fs](https://duckdb.org/community_extensions/extensions/latency_injection_fs.html) | [duckdb-filesystem-latency-injection](https://github.com/dentiny/duckdb-filesystem-latency-injection) | 🟢 Ongoing | 2 - ✅ Active | 18 days ago (2026-05-24 10:15:19 UTC) | 0 | C++ | DuckDB extension: latency_injection_fs by dentiny |
| 131 | [level_pivot](https://duckdb.org/community_extensions/extensions/level_pivot.html) | [duckdb-level-pivot](https://github.com/halgari/duckdb-level-pivot) | 🟢 Ongoing | 3 - 🟡 Stable | 49 days ago (2026-04-23 16:05:04 UTC) | 0 | C++ | DuckDB extension: level_pivot by halgari |
| 132 | [lindel](https://duckdb.org/community_extensions/extensions/lindel.html) | [lindel](https://github.com/Query-farm/lindel) | 🟢 Ongoing | 3 - 🟡 Stable | 44 days ago (2026-04-28 20:32:34 UTC) | 66 | C++ | DuckDB Extension Linearization/Delinearization, Z-Order, Hilbert and Morton C... |
| 133 | [llm](https://duckdb.org/community_extensions/extensions/llm.html) | [duckdb-llm](https://github.com/midwork-finds-jobs/duckdb-llm) | 🟢 Ongoing | 4 - 🟠 Stale | 114 days ago (2026-02-17 14:09:08 UTC) | 3 | C++ | DuckDB extension: llm by midwork-finds-jobs |
| 134 | [lpts](https://duckdb.org/community_extensions/extensions/lpts.html) | [lpts](https://github.com/cwida/lpts) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-06-11 07:24:38 UTC) | 3 | C++ | Logical Plan To SQL DuckDB Extension |
| 135 | [lsh](https://duckdb.org/community_extensions/extensions/lsh.html) | [lsh](https://github.com/princeton-ddss/lsh) | ❓ Unknown | 3 - 🟡 Stable | 56 days ago (2026-04-16 17:00:45 UTC) | 13 | Rust | DuckDB community extension for locality-sensitive hashing (LSH) |
| 136 | [lua](https://duckdb.org/community_extensions/extensions/lua.html) | [duckdb-lua](https://github.com/isaacbrodsky/duckdb-lua) | 🟢 Ongoing | 2 - ✅ Active | 18 days ago (2026-05-24 15:43:06 UTC) | 12 | C++ | DuckDB extension to evaluate Lua expressions. |
| 137 | [magic](https://duckdb.org/community_extensions/extensions/magic.html) | [duckdb-magic](https://github.com/carlopi/duckdb-magic) | ❓ Unknown | 3 - 🟡 Stable | 59 days ago (2026-04-13 19:33:31 UTC) | 8 | C++ | Auto-detect file types via `libmagic` (`file` utility) |
| 138 | [marisa](https://duckdb.org/community_extensions/extensions/marisa.html) | [marisa](https://github.com/Query-farm/marisa) | 🟢 Ongoing | 3 - 🟡 Stable | 74 days ago (2026-03-29 21:04:45 UTC) | 13 | C++ | The Marisa extension by Query.Farm integrates the fast, space-efficient MARIS... |
| 139 | [markdown](https://duckdb.org/community_extensions/extensions/markdown.html) | [duckdb_markdown](https://github.com/teaguesterling/duckdb_markdown) | 🟢 Ongoing | 2 - ✅ Active | 11 days ago (2026-05-31 20:10:26 UTC) | 23 | C++ | Heirarchical markdown parsing for DuckDB |
| 140 | [maxmind](https://duckdb.org/community_extensions/extensions/maxmind.html) | [duckdb-maxmind](https://github.com/marselester/duckdb-maxmind) | 🟢 Ongoing | 3 - 🟡 Stable | 56 days ago (2026-04-17 02:52:43 UTC) | 7 | Zig | DuckDB MaxMind extension written in Zig. |
| 141 | [miint](https://duckdb.org/community_extensions/extensions/miint.html) | [duckdb-miint](https://github.com/the-miint/duckdb-miint) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-06-11 22:37:56 UTC) | 5 | C | DuckDB extension: miint by the-miint |
| 142 | [minijinja](https://duckdb.org/community_extensions/extensions/minijinja.html) | [minijinja](https://github.com/Query-farm/minijinja) | 🟢 Ongoing | 3 - 🟡 Stable | 74 days ago (2026-03-29 21:04:46 UTC) | 5 | C++ | DuckDB extension: minijinja |
| 143 | [miniplot](https://duckdb.org/community_extensions/extensions/miniplot.html) | [miniplot](https://github.com/nkwork9999/miniplot) | 🟢 Ongoing | 4 - 🟠 Stale | 209 days ago (2025-11-15 02:42:43 UTC) | 22 | C++ | DuckDB extension: miniplot by nkwork9999 |
| 144 | [mlpack](https://duckdb.org/community_extensions/extensions/mlpack.html) | [duckdb-mlpack](https://github.com/eddelbuettel/duckdb-mlpack) | 🟢 Ongoing | 4 - 🟠 Stale | 135 days ago (2026-01-27 14:18:00 UTC) | 19 | C++ | Bringing mlpack to duckdb |
| 145 | [monetary](https://duckdb.org/community_extensions/extensions/monetary.html) | [monetary](https://github.com/fyffee/monetary) | ❓ Unknown | 4 - 🟠 Stale | 133 days ago (2026-01-29 11:29:01 UTC) | 0 | C++ | DuckDB extension: monetary by fyffee |
| 146 | [mongo](https://duckdb.org/community_extensions/extensions/mongo.html) | [duckdb-mongo](https://github.com/stephaniewang526/duckdb-mongo) | 🟢 Ongoing | 1 - 🔥 Very Active | 7 days ago (2026-06-05 02:29:05 UTC) | 52 | C++ | Integrates DuckDB with MongoDB, enabling direct SQL queries over MongoDB coll... |
| 147 | [mooncake](https://duckdb.org/community_extensions/extensions/mooncake.html) | [duckdb_mooncake](https://github.com/Mooncake-Labs/duckdb_mooncake) | ❓ Unknown | 4 - 🟠 Stale | 229 days ago (2025-10-26 07:13:05 UTC) | 10 | C++ | Read Iceberg tables written by moonlink in real time |
| 148 | [mpduck](https://duckdb.org/community_extensions/extensions/mpduck.html) | [mpduck](https://github.com/MatthewMooreZA/mpduck) | 🟢 Ongoing | 3 - 🟡 Stable | 59 days ago (2026-04-13 17:59:29 UTC) | 1 | C++ | DuckDB extension to read and write Prophet model point files. |
| 149 | [msolap](https://duckdb.org/community_extensions/extensions/msolap.html) | [duckdb-msolap-extension](https://github.com/Hugoberry/duckdb-msolap-extension) | ❓ Unknown | 4 - 🟠 Stale | 260 days ago (2025-09-24 16:33:46 UTC) | 14 | C++ | DuckDB extension: msolap by Hugoberry |
| 150 | [mssql](https://duckdb.org/community_extensions/extensions/mssql.html) | [mssql-extension](https://github.com/hugr-lab/mssql-extension) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-06-10 09:34:03 UTC) | 112 | C++ | DuckDB extension for Microsoft SQL Server (TDS + TLS), with catalog integrati... |
| 151 | [nanoarrow](https://duckdb.org/community_extensions/extensions/nanoarrow.html) | [duckdb-nanoarrow](https://github.com/paleolimbot/duckdb-nanoarrow) | ❓ Unknown | 4 - 🟠 Stale | 91 days ago (2026-03-12 13:57:38 UTC) | 75 | C++ | DuckDB extension: nanoarrow by paleolimbot |
| 152 | [nanodbc](https://duckdb.org/community_extensions/extensions/nanodbc.html) | [duckdb-nanodbc-extension](https://github.com/Hugoberry/duckdb-nanodbc-extension) | ❓ Unknown | 3 - 🟡 Stable | 41 days ago (2026-05-01 13:18:55 UTC) | 52 | C++ | Database connectivity extension by Hugoberry |
| 153 | [nats_js](https://duckdb.org/community_extensions/extensions/nats_js.html) | [duckdb-nats-jetstream](https://github.com/brannn/duckdb-nats-jetstream) | ❓ Unknown | 3 - 🟡 Stable | 74 days ago (2026-03-30 05:12:16 UTC) | 21 | C++ | DuckDB extension for querying NATS JetStream message streams with SQL |
| 154 | [netquack](https://duckdb.org/community_extensions/extensions/netquack.html) | [duckdb-netquack](https://github.com/hatamiarash7/duckdb-netquack) | ❓ Unknown | 2 - ✅ Active | 20 days ago (2026-05-22 16:42:00 UTC) | 39 | C++ | DuckDB extension for parsing, extracting, and analyzing domains, URIs, and pa... |
| 155 | [nsv](https://duckdb.org/community_extensions/extensions/nsv.html) | [nsv-duckdb](https://github.com/nsv-format/nsv-duckdb) | 🟢 Ongoing | 1 - 🔥 Very Active | 4 days ago (2026-06-07 19:12:56 UTC) | 0 | Rust | A DuckDB extension for NSV processing |
| 156 | [oast](https://duckdb.org/community_extensions/extensions/oast.html) | [duckdb-oast](https://github.com/hrbrmstr/duckdb-oast) | 🟢 Ongoing | 4 - 🟠 Stale | 121 days ago (2026-02-10 12:00:32 UTC) | 4 | C | A DuckDB extension for validating, decoding, and extracting OAST (Out-of-Band... |
| 157 | [observefs](https://duckdb.org/community_extensions/extensions/observefs.html) | [duckdb-filesystem-observability](https://github.com/dentiny/duckdb-filesystem-observability) | 🟢 Ongoing | 2 - ✅ Active | 18 days ago (2026-05-24 09:58:34 UTC) | 16 | C++ | Provides observability for duckdb filesystem. |
| 158 | [ofquack](https://duckdb.org/community_extensions/extensions/ofquack.html) | [ofquack](https://github.com/krokozyab/ofquack) | ❓ Unknown | 4 - 🟠 Stale | over a year ago (2025-04-22 12:24:17 UTC) | 6 | C++ | Oracle Fusion DuckDB extension  |
| 159 | [onager](https://duckdb.org/community_extensions/extensions/onager.html) | [onager](https://github.com/CogitatorTech/onager) | 🟢 Ongoing | 2 - ✅ Active | 18 days ago (2026-05-24 16:55:16 UTC) | 133 | Rust | A DuckDB extension for graph data analytics |
| 160 | [onelake](https://duckdb.org/community_extensions/extensions/onelake.html) | [duckdb_onelake](https://github.com/datumnova/duckdb_onelake) | ❓ Unknown | 4 - 🟠 Stale | 192 days ago (2025-12-01 10:28:22 UTC) | 19 | C++ | DuckDB extension: onelake by datumnova |
| 161 | [open_prompt](https://duckdb.org/community_extensions/extensions/open_prompt.html) | [openprompt](https://github.com/Query-farm/openprompt) | 🟢 Ongoing | 3 - 🟡 Stable | 79 days ago (2026-03-24 20:13:01 UTC) | 60 | C++ | DuckDB Community Extension to prompt LLMs from SQL |
| 162 | [osmium](https://duckdb.org/community_extensions/extensions/osmium.html) | [duckdb-osmium](https://github.com/jake-low/duckdb-osmium) | 🟢 Ongoing | 1 - 🔥 Very Active | 6 days ago (2026-06-06 07:21:22 UTC) | 18 | C++ | DuckDB extension for reading OpenStreetMap PBF files using libosmium |
| 163 | [otlp](https://duckdb.org/community_extensions/extensions/otlp.html) | [duckdb-otlp](https://github.com/smithclay/duckdb-otlp) | 🟢 Ongoing | 1 - 🔥 Very Active | 4 days ago (2026-06-07 10:45:46 UTC) | 64 | Python | stream, store, and query OpenTelemetry metrics, logs, and traces (OTLP) in du... |
| 164 | [overture](https://duckdb.org/community_extensions/extensions/overture.html) | [duckdb-overture](https://github.com/cubilica/duckdb-overture) | 🟢 Ongoing | 3 - 🟡 Stable | 58 days ago (2026-04-14 16:46:56 UTC) | 4 | C++ | DuckDB extension: overture by cubilica |
| 165 | [pac](https://duckdb.org/community_extensions/extensions/pac.html) | [privacy](https://github.com/cwida/privacy) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-06-11 10:59:12 UTC) | 17 | C++ | Automatic query privatization in DuckDB |
| 166 | [paimon](https://duckdb.org/community_extensions/extensions/paimon.html) | [duckdb-paimon](https://github.com/polardb/duckdb-paimon) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-06-11 02:09:20 UTC) | 32 | C++ | DuckDB extension for accessing Apache Paimon. 🦆 |
| 167 | [parser_tools](https://duckdb.org/community_extensions/extensions/parser_tools.html) | [duckdb_extension_parser_tools](https://github.com/hotdata-dev/duckdb_extension_parser_tools) | 🟢 Ongoing | 4 - 🟠 Stale | 132 days ago (2026-01-30 16:44:26 UTC) | 25 | C++ | Parse sql - with sql! |
| 168 | [pbi_scanner](https://duckdb.org/community_extensions/extensions/pbi_scanner.html) | [pbi_scanner](https://github.com/crazy-treyn/pbi_scanner) | 🟢 Ongoing | 1 - 🔥 Very Active | 3 days ago (2026-06-08 13:21:14 UTC) | 15 | C++ | DuckDB extension that enables querying Power BI Semantic Models with DAX. |
| 169 | [pbix](https://duckdb.org/community_extensions/extensions/pbix.html) | [duckdb-pbix-extension](https://github.com/Hugoberry/duckdb-pbix-extension) | 🟢 Ongoing | 4 - 🟠 Stale | 230 days ago (2025-10-24 13:47:34 UTC) | 37 | C++ | Duckdb extension for parsing the metadata and contents of the embedded data m... |
| 170 | [pcap_duckdb](https://duckdb.org/community_extensions/extensions/pcap_duckdb.html) | [pcap_duckdb](https://github.com/siara-in/pcap_duckdb) | 🟢 Ongoing | 2 - ✅ Active | 8 days ago (2026-06-04 05:10:33 UTC) | 1 | C++ | Database connectivity extension by siara-in |
| 171 | [pcap_reader](https://duckdb.org/community_extensions/extensions/pcap_reader.html) | [pcap](https://github.com/Query-farm/pcap) | ❓ Unknown | 2 - ✅ Active | 24 days ago (2026-05-18 22:26:34 UTC) | 13 | Rust | DuckDB PCAP Reader Extension made in Rust |
| 172 | [pdal](https://duckdb.org/community_extensions/extensions/pdal.html) | [duckdb-pdal](https://github.com/ahuarte47/duckdb-pdal) | 🟢 Ongoing | 2 - ✅ Active | 22 days ago (2026-05-20 17:17:09 UTC) | 26 | C++ | DuckDB extension for manipulating point cloud data using SQL |
| 173 | [pfc](https://duckdb.org/community_extensions/extensions/pfc.html) | [pfc-duckdb](https://github.com/ImpossibleForge/pfc-duckdb) | 🟢 Ongoing | 2 - ✅ Active | 23 days ago (2026-05-19 17:32:55 UTC) | 1 | C++ | DuckDB extension to read PFC-JSONL compressed log files with block-level time... |
| 174 | [pic2vec](https://duckdb.org/community_extensions/extensions/pic2vec.html) | [pic2vec](https://github.com/nkwork9999/pic2vec) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-06-10 11:29:26 UTC) | 0 | C++ | DuckDB extension: pic2vec by nkwork9999 |
| 175 | [pivot_table](https://duckdb.org/community_extensions/extensions/pivot_table.html) | [pivot_table](https://github.com/Alex-Monahan/pivot_table) | ❓ Unknown | 3 - 🟡 Stable | 55 days ago (2026-04-17 15:20:58 UTC) | 20 | C++ | Full spreadsheet-style pivot table through SQL macros. Just specify values, r... |
| 176 | [plinking_duck](https://duckdb.org/community_extensions/extensions/plinking_duck.html) | [plinking_duck](https://github.com/teaguesterling/plinking_duck) | 🟢 Ongoing | 2 - ✅ Active | 11 days ago (2026-05-31 20:10:06 UTC) | 3 | C++ | DuckDB tools for Plink2  |
| 177 | [poached](https://duckdb.org/community_extensions/extensions/poached.html) | [poached](https://github.com/sidequery/poached) | 🟢 Ongoing | 4 - 🟠 Stale | 167 days ago (2025-12-26 21:13:19 UTC) | 11 | C++ | A DuckDB extension that exposes SQL parsing functionality for building IDEs,... |
| 178 | [polyglot](https://duckdb.org/community_extensions/extensions/polyglot.html) | [duckdb-polyglot](https://github.com/tobilg/duckdb-polyglot) | ❓ Unknown | 1 - 🔥 Very Active | 6 days ago (2026-06-05 21:14:53 UTC) | 22 | Rust | Use other SQL dialects in DuckDB  |
| 179 | [protoduck](https://duckdb.org/community_extensions/extensions/protoduck.html) | [protoduck](https://github.com/fcsnk/protoduck) | ❓ Unknown | 3 - 🟡 Stable | 44 days ago (2026-04-28 19:03:35 UTC) | 1 | Rust | DuckDB extension: protoduck by fcsnk |
| 180 | [prql](https://duckdb.org/community_extensions/extensions/prql.html) | [duckdb-prql](https://github.com/ywelsch/duckdb-prql) | 🟢 Ongoing | 2 - ✅ Active | 14 days ago (2026-05-28 11:18:16 UTC) | 326 | C++ | PRQL as a DuckDB extension |
| 181 | [psql](https://duckdb.org/community_extensions/extensions/psql.html) | [duckdb-psql](https://github.com/ywelsch/duckdb-psql) | 🟢 Ongoing | 3 - 🟡 Stable | 58 days ago (2026-04-14 18:55:40 UTC) | 104 | C++ | A piped SQL for DuckDB |
| 182 | [pst](https://duckdb.org/community_extensions/extensions/pst.html) | [duckdb-pst](https://github.com/intellekthq/duckdb-pst) | ❓ Unknown | 2 - ✅ Active | 21 days ago (2026-05-21 12:14:09 UTC) | 10 | C++ | In-place querying of Microsoft PST files, directly from storage, with SQL. |
| 183 | [psyduck](https://duckdb.org/community_extensions/extensions/psyduck.html) | [psyduck](https://github.com/Ian-Fogelman/psyduck) | 🟢 Ongoing | 4 - 🟠 Stale | 179 days ago (2025-12-14 15:10:39 UTC) | 7 | C++ | Pysduck a DuckDB community extension about Pokémon. |
| 184 | [pyroscope](https://duckdb.org/community_extensions/extensions/pyroscope.html) | [pyroscope](https://github.com/Query-farm/pyroscope) | ❓ Unknown | 4 - 🟠 Stale | 113 days ago (2026-02-18 19:49:53 UTC) | 21 | Rust | DuckDB Pyroscope Extension for Continuous Profiling |
| 185 | [quack_oauth](https://duckdb.org/community_extensions/extensions/quack_oauth.html) | [quack-oauth](https://github.com/DataZooDE/quack-oauth) | 🟢 Ongoing | 2 - ✅ Active | 15 days ago (2026-05-28 04:29:19 UTC) | 9 | C++ | Extensions providing OAuth and OpenID primitives for authentication and autho... |
| 186 | [quackfix](https://duckdb.org/community_extensions/extensions/quackfix.html) | [QuackFIX](https://github.com/hyehudai/QuackFIX) | ❓ Unknown | 4 - 🟠 Stale | 168 days ago (2025-12-25 10:36:24 UTC) | 16 | C++ | Fix log extension for duckdb |
| 187 | [quackformers](https://duckdb.org/community_extensions/extensions/quackformers.html) | [quackformers](https://github.com/martin-conur/quackformers) | ❓ Unknown | 2 - ✅ Active | 24 days ago (2026-05-18 14:26:14 UTC) | 12 | Rust | DuckDB NLP extension. |
| 188 | [quackscale](https://duckdb.org/community_extensions/extensions/quackscale.html) | [quackscale](https://github.com/Query-farm/quackscale) | 🟢 Ongoing | 2 - ✅ Active | 9 days ago (2026-06-02 17:02:27 UTC) | 17 | Shell | DuckDB WireGuard Extension with Quack & Ducklake over Tailscale, Headscale & Co |
| 189 | [quackstats](https://duckdb.org/community_extensions/extensions/quackstats.html) | [quackstats](https://github.com/jasadams/quackstats) | ❓ Unknown | 4 - 🟠 Stale | 130 days ago (2026-02-01 12:01:35 UTC) | 2 | Rust | DuckDB extension for time series forecasting and seasonality detection |
| 190 | [quackstore](https://duckdb.org/community_extensions/extensions/quackstore.html) | [QuackStore](https://github.com/coginiti-dev/QuackStore) | 🟢 Ongoing | 3 - 🟡 Stable | 37 days ago (2026-05-05 13:29:19 UTC) | 116 | C++ | DuckDB extension: quackstore by coginiti-dev |
| 191 | [query_condition_cache](https://duckdb.org/community_extensions/extensions/query_condition_cache.html) | [duckdb-query-condition-cache](https://github.com/dentiny/duckdb-query-condition-cache) | 🟢 Ongoing | 2 - ✅ Active | 18 days ago (2026-05-24 12:15:09 UTC) | 8 | C++ | DuckDB extension: query_condition_cache by dentiny |
| 192 | [quickjs](https://duckdb.org/community_extensions/extensions/quickjs.html) | [quickjs](https://github.com/Query-farm/quickjs) | 🟢 Ongoing | 3 - 🟡 Stable | 74 days ago (2026-03-29 21:04:47 UTC) | 14 | C++ | DuckDB extension: quickjs by quackscience |
| 193 | [radio](https://duckdb.org/community_extensions/extensions/radio.html) | [radio](https://github.com/Query-farm/radio) | 🟢 Ongoing | 3 - 🟡 Stable | 74 days ago (2026-03-29 21:04:47 UTC) | 40 | C++ | Radio is a DuckDB extension by Query.Farm that brings real-time event streams... |
| 194 | [rapidfuzz](https://duckdb.org/community_extensions/extensions/rapidfuzz.html) | [rapidfuzz](https://github.com/Query-farm/rapidfuzz) | 🟢 Ongoing | 3 - 🟡 Stable | 74 days ago (2026-03-29 21:04:48 UTC) | 17 | C++ | DuckDB Community Extension adding RapidFuzz algorithms for search, deduplicat... |
| 195 | [raquet](https://duckdb.org/community_extensions/extensions/raquet.html) | [duckdb-raquet](https://github.com/jatorre/duckdb-raquet) | 🟢 Ongoing | 1 - 🔥 Very Active | 3 days ago (2026-06-08 22:14:07 UTC) | 13 | C++ | DuckDB extension for reading Raquet format (raster data in Parquet with QUADB... |
| 196 | [raster](https://duckdb.org/community_extensions/extensions/raster.html) | [duckdb-raster](https://github.com/ahuarte47/duckdb-raster) | 🟢 Ongoing | 2 - ✅ Active | 22 days ago (2026-05-20 18:39:27 UTC) | 47 | C++ | DuckDB Extension for reading and writing raster files using SQL. |
| 197 | [rate_limit_fs](https://duckdb.org/community_extensions/extensions/rate_limit_fs.html) | [duckdb-rate-limit-filesystem](https://github.com/dentiny/duckdb-rate-limit-filesystem) | 🟢 Ongoing | 2 - ✅ Active | 18 days ago (2026-05-24 11:05:36 UTC) | 1 | C++ | DuckDB extension: rate_limit_fs by dentiny |
| 198 | [rdf](https://duckdb.org/community_extensions/extensions/rdf.html) | [duck_rdf](https://github.com/nonodename/duck_rdf) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-06-11 12:33:25 UTC) | 19 | C++ | RDF file extension for DuckDB. Reads and writes supported |
| 199 | [read_dbf](https://duckdb.org/community_extensions/extensions/read_dbf.html) | [duckdb-dbf](https://github.com/tocharan/duckdb-dbf) | 🟢 Ongoing | 4 - 🟠 Stale | 106 days ago (2026-02-25 17:13:20 UTC) | 3 | C++ | Database connectivity extension by tocharan |
| 200 | [read_lines](https://duckdb.org/community_extensions/extensions/read_lines.html) | [duckdb_read_lines](https://github.com/teaguesterling/duckdb_read_lines) | 🟢 Ongoing | 2 - ✅ Active | 11 days ago (2026-05-31 20:11:15 UTC) | 3 | C++ | Simple parsers for fast extraction from line-based files  |
| 201 | [read_stat](https://duckdb.org/community_extensions/extensions/read_stat.html) | [duckdb-read-stat](https://github.com/dylanmeysmans/duckdb-read-stat) | 🟢 Ongoing | 4 - 🟠 Stale | 196 days ago (2025-11-27 13:46:07 UTC) | 33 | C | Read data sets from SAS, Stata, and SPSS from DuckDB with ReadStat |
| 202 | [redis](https://duckdb.org/community_extensions/extensions/redis.html) | [redis](https://github.com/Query-farm/redis) | 🟢 Ongoing | 3 - 🟡 Stable | 74 days ago (2026-03-29 21:04:49 UTC) | 13 | C++ | DuckDB Redis Client community extension |
| 203 | [robust](https://duckdb.org/community_extensions/extensions/robust.html) | [robust](https://github.com/robust-sql/robust) | 🟢 Ongoing | 1 - 🔥 Very Active | 7 days ago (2026-06-05 06:14:25 UTC) | 2 | C++ | A DuckDB extension implementing Predicate Transfer to reduce cardinality expl... |
| 204 | [rusty_quack](https://duckdb.org/community_extensions/extensions/rusty_quack.html) | [extension-template-rs](https://github.com/duckdb/extension-template-rs) | ❓ Unknown | 1 - 🔥 Very Active | 2 days ago (2026-06-09 09:23:13 UTC) | 109 | Rust | (Experimental) Template for Rust-based DuckDB extensions |
| 205 | [rusty_sheet](https://duckdb.org/community_extensions/extensions/rusty_sheet.html) | [rusty-sheet](https://github.com/redraiment/rusty-sheet) | 🟢 Ongoing | 4 - 🟠 Stale | 119 days ago (2026-02-13 02:27:56 UTC) | 72 | Rust | An Excel/WPS/OpenDocument Spreadsheets file reader for DuckDB |
| 206 | [salesforce](https://duckdb.org/community_extensions/extensions/salesforce.html) | [duckdb-salesforce](https://github.com/flozer/duckdb-salesforce) | 🟢 Ongoing | 1 - 🔥 Very Active | 2 days ago (2026-06-09 11:40:53 UTC) | 0 | C++ | DuckDB extension: salesforce by flozer |
| 207 | [sazgar](https://duckdb.org/community_extensions/extensions/sazgar.html) | [Sazgar](https://github.com/Angelerator/Sazgar) | 🟢 Ongoing | 2 - ✅ Active | 21 days ago (2026-05-22 04:56:10 UTC) | 13 | HTML | DuckDB extension for system monitoring & intelligent SQL routing. 25+ functio... |
| 208 | [scalarfs](https://duckdb.org/community_extensions/extensions/scalarfs.html) | [duckdb_scalarfs](https://github.com/teaguesterling/duckdb_scalarfs) | 🟢 Ongoing | 2 - ✅ Active | 11 days ago (2026-05-31 20:10:42 UTC) | 8 | C++ | A collection of simple virtual filesystems for treating scalar values as files. |
| 209 | [scrooge](https://duckdb.org/community_extensions/extensions/scrooge.html) | [Scrooge-McDuck](https://github.com/pdet/Scrooge-McDuck) | ❓ Unknown | 3 - 🟡 Stable | 38 days ago (2026-05-04 14:27:57 UTC) | 162 | C++ | DuckDB extension: scrooge by pdet |
| 210 | [se3](https://duckdb.org/community_extensions/extensions/se3.html) | [se3](https://github.com/jokasimr/se3) | 🟢 Ongoing | 4 - 🟠 Stale | 95 days ago (2026-03-08 13:32:27 UTC) | 0 | C++ | Duckdb extension for efficient rotation / translation operations on points in... |
| 211 | [semantic_views](https://duckdb.org/community_extensions/extensions/semantic_views.html) | [duckdb-semantic-views](https://github.com/anentropic/duckdb-semantic-views) | 🟢 Ongoing | 1 - 🔥 Very Active | 7 days ago (2026-06-04 15:08:18 UTC) | 6 | Rust | Semantic Views for DuckDB. |
| 212 | [sheetreader](https://duckdb.org/community_extensions/extensions/sheetreader.html) | [sheetreader-duckdb](https://github.com/polydbms/sheetreader-duckdb) | 🟢 Ongoing | 3 - 🟡 Stable | 88 days ago (2026-03-15 11:03:07 UTC) | 56 | C++ | DuckDB extension: sheetreader by polydbms |
| 213 | [shellfs](https://duckdb.org/community_extensions/extensions/shellfs.html) | [shellfs](https://github.com/Query-farm/shellfs) | 🟢 Ongoing | 3 - 🟡 Stable | 74 days ago (2026-03-29 21:04:50 UTC) | 96 | C++ | DuckDB extension allowing shell commands to be used for input and output. |
| 214 | [sistat](https://duckdb.org/community_extensions/extensions/sistat.html) | [duckdb-sistat](https://github.com/fklezin/duckdb-sistat) | 🟢 Ongoing | 4 - 🟠 Stale | 94 days ago (2026-03-09 09:09:46 UTC) | 3 | C++ | DuckDB extension to query Slovenia's SiStat open data directly using SQL. No... |
| 215 | [sitemap](https://duckdb.org/community_extensions/extensions/sitemap.html) | [duckdb-sitemap](https://github.com/midwork-finds-jobs/duckdb-sitemap) | 🟢 Ongoing | 4 - 🟠 Stale | 114 days ago (2026-02-17 14:13:12 UTC) | 1 | C++ | DuckDB extension for parsing XML sitemaps from websites |
| 216 | [sitting_duck](https://duckdb.org/community_extensions/extensions/sitting_duck.html) | [sitting_duck](https://github.com/teaguesterling/sitting_duck) | 🟢 Ongoing | 1 - 🔥 Very Active | 7 days ago (2026-06-04 15:00:57 UTC) | 17 | C | Sitting Duck is a DuckDB extension that makes Abstract Syntax Trees (ASTs) fr... |
| 217 | [slack](https://github.com/dentiny/duckdb-slack) | [duckdb-slack](https://github.com/dentiny/duckdb-slack) | ❓ Unknown | 4 - 🟠 Stale | 112 days ago (2026-02-19 18:08:54 UTC) | 0 | C++ | DuckDB extension: slack by dentiny |
| 218 | [snowflake](https://duckdb.org/community_extensions/extensions/snowflake.html) | [duckdb-snowflake](https://github.com/iqea-ai/duckdb-snowflake) | 🟢 Ongoing | 1 - 🔥 Very Active | 5 days ago (2026-06-07 00:47:25 UTC) | 54 | C++ | A powerful DuckDB extension that enables seamless querying of Snowflake datab... |
| 219 | [splink_udfs](https://duckdb.org/community_extensions/extensions/splink_udfs.html) | N/A | ❓ Unknown | 1 - 🔥 Very Active | today | 0 | N/A | DuckDB extension: splink_udfs |
| 220 | [spxlsx](https://duckdb.org/community_extensions/extensions/spxlsx.html) | [spxlsx](https://github.com/paulmupeters/spxlsx) | 🟢 Ongoing | 2 - ✅ Active | 18 days ago (2026-05-24 21:36:41 UTC) | 1 | C++ | Duckdb extension to read sharepoint lists and excel |
| 221 | [sshfs](https://duckdb.org/community_extensions/extensions/sshfs.html) | [duckdb-sshfs](https://github.com/midwork-finds-jobs/duckdb-sshfs) | 🟢 Ongoing | 1 - 🔥 Very Active | 5 days ago (2026-06-06 19:02:46 UTC) | 11 | C++ | DuckDB sshfs extension - Read and write files through ssh inside DuckDB |
| 222 | [st_read_multi](https://duckdb.org/community_extensions/extensions/st_read_multi.html) | [duckdb-ext-st-read-multi](https://github.com/yutannihilation/duckdb-ext-st-read-multi) | 🟢 Ongoing | 2 - ✅ Active | 9 days ago (2026-06-02 17:40:14 UTC) | 10 | Rust | A DuckDB extension to import multiple geospatial files with `ST_Read_Multi()` |
| 223 | [stochastic](https://duckdb.org/community_extensions/extensions/stochastic.html) | [stochastic](https://github.com/Query-farm/stochastic) | 🟢 Ongoing | 3 - 🟡 Stable | 74 days ago (2026-03-29 21:05:21 UTC) | 23 | C++ | A DuckDB extension that add comprehensive statistical distribution functions... |
| 224 | [substrait](https://duckdb.org/community_extensions/extensions/substrait.html) | [duckdb-substrait-extension](https://github.com/substrait-io/duckdb-substrait-extension) | ❓ Unknown | 1 - 🔥 Very Active | 6 days ago (2026-06-05 10:05:46 UTC) | 63 | C++ | DuckDB extension: substrait by substrait-io |
| 225 | [sudan](https://duckdb.org/community_extensions/extensions/sudan.html) | [duckdb-sudan-](https://github.com/Osman-Geomatics93/duckdb-sudan-) | ❓ Unknown | 4 - 🟠 Stale | 112 days ago (2026-02-19 11:49:28 UTC) | 0 | Jupyter Notebook | DuckDB extension: sudan by Osman-Geomatics93 |
| 226 | [system_stats](https://duckdb.org/community_extensions/extensions/system_stats.html) | [system_stats](https://github.com/dentiny/system_stats) | 🟢 Ongoing | 2 - ✅ Active | 18 days ago (2026-05-24 10:51:12 UTC) | 3 | C++ | DuckDB extension: system_stats by dentiny |
| 227 | [table_guard](https://duckdb.org/community_extensions/extensions/table_guard.html) | [duckdb-table-guard](https://github.com/yoogoc/duckdb-table-guard) | 🟢 Ongoing | 2 - ✅ Active | 28 days ago (2026-05-14 09:52:13 UTC) | 0 | C++ | A DuckDB extension for table-level access control |
| 228 | [table_inspector](https://duckdb.org/community_extensions/extensions/table_inspector.html) | [duckdb-table-inspector](https://github.com/dentiny/duckdb-table-inspector) | 🟢 Ongoing | 2 - ✅ Active | 18 days ago (2026-05-24 09:12:19 UTC) | 2 | C++ | DuckDB extension: table_inspector by dentiny |
| 229 | [talib](https://duckdb.org/community_extensions/extensions/talib.html) | [atm_talib](https://github.com/neuesql/atm_talib) | 🟢 Ongoing | 3 - 🟡 Stable | 52 days ago (2026-04-21 06:06:51 UTC) | 5 | C++ | A duckdb TA-Lib to add technical analysis in Financial Markets with SQL easily |
| 230 | [tarfs](https://duckdb.org/community_extensions/extensions/tarfs.html) | [duckdb_tarfs](https://github.com/Maxxen/duckdb_tarfs) | ❓ Unknown | 4 - 🟠 Stale | over a year ago (2024-08-26 11:01:47 UTC) | 12 | C++ | DuckDB extension: tarfs by Maxxen |
| 231 | [tera](https://duckdb.org/community_extensions/extensions/tera.html) | [tera](https://github.com/Query-farm/tera) | 🟢 Ongoing | 3 - 🟡 Stable | 74 days ago (2026-03-29 21:04:51 UTC) | 9 | C++ | DuckDB extension: tera |
| 232 | [textplot](https://duckdb.org/community_extensions/extensions/textplot.html) | [textplot](https://github.com/Query-farm/textplot) | 🟢 Ongoing | 3 - 🟡 Stable | 45 days ago (2026-04-27 17:31:59 UTC) | 24 | C++ | A DuckDB community extension that enables text-based data visualization direc... |
| 233 | [title_mapper](https://duckdb.org/community_extensions/extensions/title_mapper.html) | [duckdb-title-mapper](https://github.com/martin-conur/duckdb-title-mapper) | 🟢 Ongoing | 2 - ✅ Active | 17 days ago (2026-05-25 21:56:26 UTC) | 3 | Rust | DuckDB extension: title_mapper by martin-conur |
| 234 | [tpch_rust](https://duckdb.org/community_extensions/extensions/tpch_rust.html) | [duckdb-tpch-rust](https://github.com/guillesd/duckdb-tpch-rust) | 🟢 Ongoing | 1 - 🔥 Very Active | 3 days ago (2026-06-08 15:40:17 UTC) | 0 | Rust | DuckDB extension to generate tpch tables using tpch-rs |
| 235 | [tributary](https://duckdb.org/community_extensions/extensions/tributary.html) | [tributary](https://github.com/Query-farm/tributary) | ❓ Unknown | 3 - 🟡 Stable | 74 days ago (2026-03-29 21:04:53 UTC) | 55 | C++ | A DuckDB Extension for Kafka |
| 236 | [tsid](https://duckdb.org/community_extensions/extensions/tsid.html) | [tsid](https://github.com/Query-farm/tsid) | 🟢 Ongoing | 3 - 🟡 Stable | 74 days ago (2026-03-29 21:04:54 UTC) | 6 | C++ | TSID Extension for DuckDB  |
| 237 | [ulid](https://duckdb.org/community_extensions/extensions/ulid.html) | [duckdb_ulid](https://github.com/Maxxen/duckdb_ulid) | ❓ Unknown | 4 - 🟠 Stale | over a year ago (2024-07-09 09:35:50 UTC) | 25 | C++ | DuckDB extension: ulid by Maxxen |
| 238 | [urlpattern](https://duckdb.org/community_extensions/extensions/urlpattern.html) | [duckdb_urlpattern](https://github.com/teaguesterling/duckdb_urlpattern) | ❓ Unknown | 2 - ✅ Active | 11 days ago (2026-05-31 20:31:25 UTC) | 4 | C++ | An implementation of URLPattern for DuckDB |
| 239 | [us_address_standardizer](https://duckdb.org/community_extensions/extensions/us_address_standardizer.html) | [duckdb-address-standardizer](https://github.com/ericmanning/duckdb-address-standardizer) | 🟢 Ongoing | 2 - ✅ Active | 22 days ago (2026-05-20 14:50:54 UTC) | 3 | C | DuckDB extension for parsing and standardizing (USA) postal addresses using P... |
| 240 | [valhalla_routing](https://duckdb.org/community_extensions/extensions/valhalla_routing.html) | [duckdb-valhalla-routing](https://github.com/midwork-finds-jobs/duckdb-valhalla-routing) | 🟢 Ongoing | 4 - 🟠 Stale | 114 days ago (2026-02-17 11:36:12 UTC) | 6 | Makefile | WIP: Attempt to package valhalla routing engine to duckdb |
| 241 | [vindex](https://duckdb.org/community_extensions/extensions/vindex.html) | [duckdb-vector-index](https://github.com/Icemap/duckdb-vector-index) | 🟢 Ongoing | 3 - 🟡 Stable | 43 days ago (2026-04-29 20:05:03 UTC) | 7 | C++ | A DuckDB extension providing HNSW, IVF, DiskANN, and SPANN vector indexes wit... |
| 242 | [waddle](https://duckdb.org/community_extensions/extensions/waddle.html) | [extension-template](https://github.com/duckdb/extension-template) | 🟢 Ongoing | 2 - ✅ Active | 9 days ago (2026-06-02 10:44:13 UTC) | 278 | Python | Template for DuckDB extensions to help you develop, test and deploy a custom... |
| 243 | [warc](https://duckdb.org/community_extensions/extensions/warc.html) | [duckdb_warc](https://github.com/midwork-finds-jobs/duckdb_warc) | ❓ Unknown | 4 - 🟠 Stale | 126 days ago (2026-02-05 15:33:27 UTC) | 4 | Rust | DuckDB extension for parsing WARC files |
| 244 | [web_archive](https://duckdb.org/community_extensions/extensions/web_archive.html) | [duckdb-web-archive](https://github.com/midwork-finds-jobs/duckdb-web-archive) | 🟢 Ongoing | 4 - 🟠 Stale | 128 days ago (2026-02-03 08:28:03 UTC) | 21 | C++ | DuckDB extension to fetch pages from Wayback Machine & Common Crawl |
| 245 | [web_search](https://duckdb.org/community_extensions/extensions/web_search.html) | [duckdb-web-search](https://github.com/midwork-finds-jobs/duckdb-web-search) | 🟢 Ongoing | 3 - 🟡 Stable | 52 days ago (2026-04-20 21:51:13 UTC) | 0 | C++ | Web/HTTP functionality extension by midwork-finds-jobs |
| 246 | [webbed](https://duckdb.org/community_extensions/extensions/webbed.html) | [duckdb_webbed](https://github.com/teaguesterling/duckdb_webbed) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-06-12 00:25:42 UTC) | 59 | C++ | A comprehensive XML and HTML processing extension for DuckDB that enables SQL... |
| 247 | [webdavfs](https://duckdb.org/community_extensions/extensions/webdavfs.html) | [duckdb-webdavfs](https://github.com/midwork-finds-jobs/duckdb-webdavfs) | ❓ Unknown | 3 - 🟡 Stable | 48 days ago (2026-04-25 03:42:47 UTC) | 1 | C++ | DuckDB WebDAVfs Extension - WebDAV filesystem support for DuckDB |
| 248 | [webmacro](https://duckdb.org/community_extensions/extensions/webmacro.html) | [webmacro](https://github.com/Query-farm/webmacro) | 🟢 Ongoing | 3 - 🟡 Stable | 79 days ago (2026-03-24 20:13:18 UTC) | 15 | C++ | DuckDB WebMacro: Share and Load your SQL Macros via gists |
| 249 | [whisper](https://duckdb.org/community_extensions/extensions/whisper.html) | [duckdb-whisper](https://github.com/tobilg/duckdb-whisper) | 🟢 Ongoing | 1 - 🔥 Very Active | 6 days ago (2026-06-05 20:34:22 UTC) | 10 | C++ | Use whisper.cpp within DuckDB to translate / transpile speech to text |
| 250 | [wireduck](https://duckdb.org/community_extensions/extensions/wireduck.html) | [wireduck](https://github.com/hyehudai/wireduck) | 🟢 Ongoing | 4 - 🟠 Stale | 261 days ago (2025-09-23 21:22:03 UTC) | 48 | C++ | Duckdb extension to read pcap files |
| 251 | [yaml](https://duckdb.org/community_extensions/extensions/yaml.html) | [duckdb_yaml](https://github.com/teaguesterling/duckdb_yaml) | 🟢 Ongoing | 2 - ✅ Active | 11 days ago (2026-05-31 20:11:37 UTC) | 18 | C++ |  A DuckDB to read and work with YAML files in a similar way to JSON files (al... |
| 252 | [yardstick](https://duckdb.org/community_extensions/extensions/yardstick.html) | [yardstick](https://github.com/sidequery/yardstick) | 🟢 Ongoing | 2 - ✅ Active | 10 days ago (2026-06-01 13:34:28 UTC) | 56 | Rust | An implementation of Measures in SQL as a DuckDB extension |
| 253 | [zeek](https://duckdb.org/community_extensions/extensions/zeek.html) | [zeek-duckdb](https://github.com/ynadji/zeek-duckdb) | 🟢 Ongoing | 3 - 🟡 Stable | 58 days ago (2026-04-14 22:02:22 UTC) | 3 | C++ | read_zeek table function to read Zeek TSV logs into DuckDB |
| 254 | [zim](https://duckdb.org/community_extensions/extensions/zim.html) | [duckdb_zim](https://github.com/teaguesterling/duckdb_zim) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-06-12 00:43:09 UTC) | 0 | C++ | DuckDB extension for working with zim files |
| 255 | [zipfs](https://duckdb.org/community_extensions/extensions/zipfs.html) | [duckdb-zipfs](https://github.com/isaacbrodsky/duckdb-zipfs) | 🟢 Ongoing | 2 - ✅ Active | 18 days ago (2026-05-24 15:42:52 UTC) | 64 | C++ | DuckDB extension to read files within zip archives. |

</details>
## Appendix: DuckDB Release Information

### Current Release Context

DuckDB follows **semantic versioning** with regular releases. For complete and up-to-date release information, see the official [**DuckDB Release Calendar**](https://duckdb.org/release_calendar.html).

### Upcoming Releases

|| Version | Planned Date | LTS |
||---------|-------------|-----|
|| v1.5.4 📅 | 2026-06-15 |  |
|| v1.4.5 📅 | 2026-06-15 | ✓ |

### Recent Releases

|| Version | Release Date | Codename | Named After | LTS | Status |
||---------|--------------|----------|-------------|-----|--------|
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
|| **v1.2.1** | 2025-03-05 | – | – |  | Active |
|| **v1.2.0** | 2025-02-05 | Histrionicus | *Harlequin duck* |  | EOL |

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

<p class="fine-print">Last updated: 2026-06-12</p>
