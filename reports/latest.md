# DuckDB Extensions Analysis

🦆 **Automated monitoring and analysis of DuckDB's extension ecosystem**


[Jump to Summary](#summary) | [Core Extensions](#core-extensions) | [Community Extensions](#community-extensions)

---

This report provides a comprehensive analysis of DuckDB extensions, including both core extensions (built into DuckDB) and community-contributed extensions.

## Data Sources

This analysis is based on the following authoritative sources:

**Core Extensions**

- **Overview**: [DuckDB Extensions](https://duckdb.org/docs/stable/extensions/overview.html)
- **Core Extensions**: [Core Extensions Documentation](https://duckdb.org/docs/stable/core_extensions/overview.html)
- **Versioning**: [Extension Versioning](https://duckdb.org/docs/stable/extensions/versioning_of_extensions.html)
- **Repository**: [duckdb/duckdb](https://github.com/Mjboothaus/duckdb-extensions-analysis)
- **Releases**: [GitHub Releases](https://github.com/Mjboothaus/duckdb-extensions-analysis/releases)

**Community Extensions**

- **Registry**: [Community Extensions Repository](https://github.com/duckdb/community-extensions)
- **Directory**: [Extensions Folder](https://github.com/duckdb/community-extensions/tree/main/extensions)
- **Featured**: [Community Extensions Page](https://community-extensions.duckdb.org/)
- **Individual Repositories**: GitHub repositories linked in the extensions directory

---
## Summary

### 📊 Current Status

| **Metric** | **Count** |
|------------|-----------|
| **Core Extensions** | 27 |
| **Community Extensions** | 172 |
| **Total Extensions** | 199 |
| **Recently Active** (≤ 30 days) | 120 (60.3%) |
| **Very Active** (≤ 7 days) | 48 (24.1%) |

*Historical trend tracking is planned for future releases to show extension ecosystem growth over time*


---
## Core Extensions

Core extensions maintained by the DuckDB team and distributed via the official extension repository

**Total:** 27 extensions

<details open markdown="1">
<summary>Click to expand/collapse core extensions table</summary>

| # | Extension | Repository | Status | Last Activity | Stars | Language | Description |
|---|-----------|------------|--------|---------------|-------|----------|-------------|
| 1 | [autocomplete](https://duckdb.org/docs/stable/core_extensions/autocomplete.html) | [duckdb/duckdb](https://github.com/duckdb/duckdb/tree/main/extension/autocomplete) | 🟢 Ongoing | 3 days ago (2026-02-10 08:21:42 UTC) | N/A (part of core DuckDB repo) | C++ | Core DuckDB extension: autocomplete |
| 2 | [avro](https://duckdb.org/docs/stable/core_extensions/avro.html) | [duckdb-avro](https://github.com/duckdb/duckdb-avro) | 🟢 Ongoing | 6 days ago (2026-02-07 16:08:01 UTC) | 32 | C++ | Apache Avro format support |
| 3 | [aws](https://duckdb.org/docs/stable/core_extensions/aws.html) | [duckdb-aws](https://github.com/duckdb/duckdb-aws) | 🟢 Ongoing | 3 days ago (2026-02-10 09:26:41 UTC) | 58 | C++ | AWS S3 integration |
| 4 | [azure](https://duckdb.org/docs/stable/core_extensions/azure.html) | [duckdb-azure](https://github.com/duckdb/duckdb-azure) | 🟢 Ongoing | 4 days ago (2026-02-09 08:47:05 UTC) | 72 | C++ | Azure extension for DuckDB |
| 5 | [delta](https://duckdb.org/docs/stable/core_extensions/delta.html) | [duckdb-delta](https://github.com/duckdb/duckdb-delta) | 🟢 Ongoing | 8 days ago (2026-02-05 14:30:11 UTC) | 212 | C++ | DuckDB extension for Delta Lake |
| 6 | [ducklake](https://duckdb.org/docs/stable/core_extensions/ducklake.html) | [duckdb/ducklake](https://github.com/duckdb/ducklake) | 🟢 Ongoing | 18 days ago | N/A (part of core DuckDB repo) | C++ | Delta Lake support via DuckLake (different from delta extension) |
| 7 | [encodings](https://duckdb.org/docs/stable/core_extensions/encodings.html) | [duckdb-encodings](https://github.com/duckdb/duckdb-encodings) | 🟢 Ongoing | 149 days ago (2025-09-17 12:57:45 UTC) | 15 | C++ | Character encoding support |
| 8 | [excel](https://duckdb.org/docs/stable/core_extensions/excel.html) | [duckdb-excel](https://github.com/duckdb/duckdb-excel) | 🟢 Ongoing | 35 days ago (2026-01-09 23:09:10 UTC) | 53 | C++ | Excel extension for DuckDB |
| 9 | [fts](https://duckdb.org/docs/stable/core_extensions/full_text_search.html) | [duckdb-fts](https://github.com/duckdb/duckdb-fts) | 🟢 Ongoing | 150 days ago (2025-09-16 14:12:43 UTC) | 30 | C++ | Full-text search functionality |
| 10 | [httpfs](https://duckdb.org/docs/stable/core_extensions/httpfs/overview.html) | [duckdb-httpfs](https://github.com/duckdb/duckdb-httpfs) | 🟢 Ongoing | today (2026-02-13 14:35:42 UTC) | 45 | C++ | HTTP/S3 filesystem support |
| 11 | [iceberg](https://duckdb.org/docs/stable/core_extensions/iceberg/overview.html) | [duckdb-iceberg](https://github.com/duckdb/duckdb-iceberg) | 🟢 Ongoing | today (2026-02-13 14:18:17 UTC) | 376 | C++ | Apache Iceberg format support |
| 12 | [icu](https://duckdb.org/docs/stable/core_extensions/icu.html) | [duckdb/duckdb](https://github.com/duckdb/duckdb/tree/main/extension/icu) | 🟢 Ongoing | 4 days ago (2026-02-09 19:29:59 UTC) | N/A (part of core DuckDB repo) | C++ | Core DuckDB extension: icu |
| 13 | [inet](https://duckdb.org/docs/stable/core_extensions/inet.html) | [duckdb-inet](https://github.com/duckdb/duckdb-inet) | 🟢 Ongoing | 85 days ago (2025-11-20 22:54:12 UTC) | 14 | C++ | Internet address data types |
| 14 | [jemalloc](https://duckdb.org/docs/stable/core_extensions/jemalloc.html) | [duckdb/duckdb](https://github.com/duckdb/duckdb/tree/main/extension/jemalloc) | 🟢 Ongoing | 251 days ago (2025-06-07 09:38:02 UTC) | N/A (part of core DuckDB repo) | C++ | Core DuckDB extension: jemalloc |
| 15 | [json](https://duckdb.org/docs/stable/data/json/overview.html) | [duckdb/duckdb](https://github.com/duckdb/duckdb/tree/main/extension/json) | 🟢 Ongoing | 3 days ago (2026-02-10 08:21:42 UTC) | N/A (part of core DuckDB repo) | C++ | Core DuckDB extension: json |
| 16 | [motherduck](https://duckdb.org/docs/stable/core_extensions/motherduck.html) | [duckdb/duckdb](https://github.com/duckdb/duckdb) *(Third Party - Closed source - maintained by MotherDuck Inc.)* | 🟢 Ongoing | 18 days ago | N/A (part of core DuckDB repo) | C++ | Core DuckDB extension: motherduck |
| 17 | [mysql](https://duckdb.org/docs/stable/core_extensions/mysql.html) | [duckdb-mysql](https://github.com/duckdb/duckdb-mysql) | 🟢 Ongoing | today (2026-02-13 11:08:46 UTC) | 91 | C++ | MySQL database connectivity |
| 18 | [parquet](https://duckdb.org/docs/stable/data/parquet/overview.html) | [duckdb/duckdb](https://github.com/duckdb/duckdb/tree/main/extension/parquet) | 🟢 Ongoing | today (2026-02-13 08:12:10 UTC) | N/A (part of core DuckDB repo) | C++ | Core DuckDB extension: parquet |
| 19 | [postgres](https://duckdb.org/docs/stable/core_extensions/postgres.html) | [duckdb-postgres](https://github.com/duckdb/duckdb-postgres) | 🟢 Ongoing | 7 days ago (2026-02-06 07:24:25 UTC) | 340 | C++ | PostgreSQL database connectivity |
| 20 | [spatial](https://duckdb.org/docs/stable/core_extensions/spatial/overview.html) | [duckdb-spatial](https://github.com/duckdb/duckdb-spatial) | 🟢 Ongoing | 25 days ago (2026-01-19 21:32:45 UTC) | 663 | C++ | Geospatial data types and functions |
| 21 | [sqlite](https://duckdb.org/docs/stable/core_extensions/sqlite.html) | [duckdb-sqlite](https://github.com/duckdb/duckdb-sqlite) | 🟢 Ongoing | 22 days ago (2026-01-22 09:02:01 UTC) | 265 | C++ | DuckDB extension to read and write to SQLite databases |
| 22 | [tpcds](https://duckdb.org/docs/stable/core_extensions/tpcds.html) | [duckdb/duckdb](https://github.com/duckdb/duckdb/tree/main/extension/tpcds) | 🟢 Ongoing | 17 days ago (2026-01-27 10:14:30 UTC) | N/A (part of core DuckDB repo) | C++ | Core DuckDB extension: tpcds |
| 23 | [tpch](https://duckdb.org/docs/stable/core_extensions/tpch.html) | [duckdb/duckdb](https://github.com/duckdb/duckdb/tree/main/extension/tpch) | 🟢 Ongoing | 25 days ago (2026-01-19 08:50:02 UTC) | N/A (part of core DuckDB repo) | C++ | Core DuckDB extension: tpch |
| 24 | [ui](https://duckdb.org/docs/stable/core_extensions/ui.html) | [duckdb-ui](https://github.com/duckdb/duckdb-ui) | 🟢 Ongoing | 2 days ago (2026-02-11 23:21:13 UTC) | 417 | C++ | Browser-based user interface for DuckDB |
| 25 | [unity_catalog](https://duckdb.org/docs/stable/core_extensions/unity_catalog.html) | [unity_catalog](https://github.com/duckdb/unity_catalog) | 🟢 Ongoing | 15 days ago (2026-01-29 13:40:31 UTC) | 98 | C++ | Proof-of-concept extension combining the delta extension with Unity Catalog |
| 26 | [vortex](https://duckdb.org/docs/stable/core_extensions/vortex.html) | [duckdb/duckdb](https://github.com/duckdb/duckdb) *(Third Party - Closed source - third-party extension)* | 🟢 Ongoing | 18 days ago | N/A (part of core DuckDB repo) | C++ | Core DuckDB extension: vortex |
| 27 | [vss](https://duckdb.org/docs/stable/core_extensions/vss.html) | [duckdb-vss](https://github.com/duckdb/duckdb-vss) | 🟢 Ongoing | 21 days ago (2026-01-23 10:10:02 UTC) | 236 | C++ | Vector similarity search |

</details>

---
---
## Community Extensions

Third-party extensions maintained by the community


**Total:** 172 extensions | 🔥 Very Active (≤7d): 48 | ✅ Active (≤30d): 72 | 🟡 Stable (≤90d): 24 | 🟠 Stale (>90d): 28

<details open markdown="1">
<summary>Click to expand/collapse community extensions table</summary>

| # | Extension | Repository | Status | Activity | Last Activity | Stars | Language | Description |
|---|-----------|------------|--------|----------|---------------|-------|----------|-------------|
| 1 | [a5](https://duckdb.org/community_extensions/extensions/a5.html) | [a5](https://github.com/Query-farm/a5) | 🟢 Ongoing | 2 - ✅ Active | 12 days ago (2026-02-01 08:02:04 UTC) | 11 | C++ | A5 Geospatial Extension for DuckDB |
| 2 | [acp](https://duckdb.org/community_extensions/extensions/acp.html) | [duckdb-acp](https://github.com/sidequery/duckdb-acp) | ❓ Unknown | 3 - 🟡 Stable | 65 days ago (2025-12-11 03:36:46 UTC) | 42 | Rust | Use Claude Code & other AI agents from inside DuckDB via extension |
| 3 | [adbc_scanner](https://duckdb.org/community_extensions/extensions/adbc_scanner.html) | [adbc_scanner](https://github.com/Query-farm/adbc_scanner) | 🟢 Ongoing | 1 - 🔥 Very Active | 4 days ago (2026-02-09 15:41:42 UTC) | 10 | C++ | A DuckDB ADBC Scanner Extension - adds support for using ADBC drivers with Du... |
| 4 | [airport](https://duckdb.org/community_extensions/extensions/airport.html) | [airport](https://github.com/Query-farm/airport) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-02-13 04:21:39 UTC) | 323 | C++ | The Airport extension for DuckDB, enables the use of Arrow Flight with DuckDB |
| 5 | [aixchess](https://duckdb.org/community_extensions/extensions/aixchess.html) | [aix](https://github.com/thomas-daniels/aix) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-02-13 21:46:20 UTC) | 10 | Rust | Aix: Efficiently storing and querying chess game collections |
| 6 | [anndata](https://duckdb.org/community_extensions/extensions/anndata.html) | [anndata-duckdb-extension](https://github.com/honicky/anndata-duckdb-extension) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-02-12 06:35:43 UTC) | 2 | C++ | Attach and AnnData file in duckdb and query it with SQL.  Perform SQL over gr... |
| 7 | [anofox_forecast](https://duckdb.org/community_extensions/extensions/anofox_forecast.html) | [anofox-forecast](https://github.com/DataZooDE/anofox-forecast) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-02-12 21:47:03 UTC) | 26 | C++ | Statistical timeseries forecasting in DuckDB |
| 8 | [anofox_statistics](https://duckdb.org/community_extensions/extensions/anofox_statistics.html) | [anofox-statistics](https://github.com/DataZooDE/anofox-statistics) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-02-13 08:54:57 UTC) | 7 | Rust | A DuckDB extension for statistical regression analysis, providing OLS, Ridge,... |
| 9 | [anofox_tabular](https://duckdb.org/community_extensions/extensions/anofox_tabular.html) | [anofox-tabular](https://github.com/DataZooDE/anofox-tabular) | ❓ Unknown | 1 - 🔥 Very Active | today (2026-02-13 07:54:21 UTC) | 12 | C++ | A duckdb extension which combines data quality and data preparation tools for... |
| 10 | [arrow](https://duckdb.org/community_extensions/extensions/arrow.html) | [duckdb-extension-alias](https://github.com/duckdb/duckdb-extension-alias) | ❓ Unknown | 4 - 🟠 Stale | 130 days ago (2025-10-06 09:07:38 UTC) | 4 | C | DuckDB extension: arrow |
| 11 | [bigquery](https://duckdb.org/community_extensions/extensions/bigquery.html) | [duckdb-bigquery](https://github.com/hafenkran/duckdb-bigquery) | 🟢 Ongoing | 1 - 🔥 Very Active | 3 days ago (2026-02-10 23:04:25 UTC) | 152 | C++ | Integrates DuckDB with Google BigQuery, allowing direct querying and manageme... |
| 12 | [bitfilters](https://duckdb.org/community_extensions/extensions/bitfilters.html) | [bitfilters](https://github.com/Query-farm/bitfilters) | 🟢 Ongoing | 2 - ✅ Active | 12 days ago (2026-02-01 08:02:15 UTC) | 5 | C++ | A high-performance DuckDB extension providing probabilistic data structures f... |
| 13 | [blockduck](https://duckdb.org/community_extensions/extensions/blockduck.html) | [BlockDuck](https://github.com/luohaha/BlockDuck) | 🟢 Ongoing | 4 - 🟠 Stale | 128 days ago (2025-10-08 16:19:04 UTC) | 10 | C++ | Live SQL Queries on Blockchain |
| 14 | [boilstream](https://duckdb.org/community_extensions/extensions/boilstream.html) | [boilstream-extension](https://github.com/dforsber/boilstream-extension) | 🟢 Ongoing | 1 - 🔥 Very Active | 6 days ago (2026-02-07 11:51:26 UTC) | 6 | C++ | Secure Remote Secrets Storage for DuckDB |
| 15 | [brew](https://duckdb.org/community_extensions/extensions/brew.html) | [duckdb-brew](https://github.com/adriens/duckdb-brew) | 🟢 Ongoing | 2 - ✅ Active | 9 days ago (2026-02-04 07:25:56 UTC) | 0 | C++ | duckdb extension to report installed brew packages/casks/formulas with SQL |
| 16 | [bvh2sql](https://duckdb.org/community_extensions/extensions/bvh2sql.html) | [bvh2sql](https://github.com/nkwork9999/bvh2sql) | 🟢 Ongoing | 4 - 🟠 Stale | 103 days ago (2025-11-02 18:17:05 UTC) | 0 | Makefile | SQL-related extension by nkwork9999 |
| 17 | [cache_httpfs](https://duckdb.org/community_extensions/extensions/cache_httpfs.html) | [duck-read-cache-fs](https://github.com/dentiny/duck-read-cache-fs) | 🟢 Ongoing | 1 - 🔥 Very Active | 4 days ago (2026-02-09 18:33:38 UTC) | 131 | C++ | This repository is made as read-only filesystem for remote access. |
| 18 | [cache_prewarm](https://duckdb.org/community_extensions/extensions/cache_prewarm.html) | [duckdb-cache-prewarm](https://github.com/dentiny/duckdb-cache-prewarm) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-02-12 22:19:59 UTC) | 1 | C++ | DuckDB extension: cache_prewarm by dentiny |
| 19 | [capi_quack](https://duckdb.org/community_extensions/extensions/capi_quack.html) | [extension-template-c](https://github.com/duckdb/extension-template-c) | ❓ Unknown | 2 - ✅ Active | 8 days ago (2026-02-05 11:39:05 UTC) | 28 | C | (Experimental) C/C++ template for DuckDB extensions based on the C API |
| 20 | [cassandra](https://duckdb.org/community_extensions/extensions/cassandra.html) | [duckdb-cassandra](https://github.com/dioptre/duckdb-cassandra) | 🟢 Ongoing | 4 - 🟠 Stale | 116 days ago (2025-10-20 19:15:10 UTC) | 0 | C++ | DuckDB Connector for Cassandra |
| 21 | [chaos](https://duckdb.org/community_extensions/extensions/chaos.html) | [duckdb-chaos](https://github.com/taniabogatsch/duckdb-chaos) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-02-12 14:50:01 UTC) | 0 | C++ | DuckDB extension: chaos by taniabogatsch |
| 22 | [chess](https://duckdb.org/community_extensions/extensions/chess.html) | [duckdb-chess](https://github.com/dotneB/duckdb-chess) | 🟢 Ongoing | 1 - 🔥 Very Active | 5 days ago (2026-02-08 23:07:17 UTC) | 1 | Rust | A DuckDB extension for parsing and analyzing chess games in PGN format. |
| 23 | [chsql](https://duckdb.org/community_extensions/extensions/chsql.html) | [clickhouse-sql](https://github.com/Query-farm/clickhouse-sql) | ❓ Unknown | 4 - 🟠 Stale | 143 days ago (2025-09-23 19:24:33 UTC) | 89 | C++ | DuckDB Community Extension implementing ClickHouse SQL Dialect macros and Cus... |
| 24 | [chsql_native](https://duckdb.org/community_extensions/extensions/chsql_native.html) | [clickhouse-native](https://github.com/Query-farm/clickhouse-native) | ❓ Unknown | 4 - 🟠 Stale | 143 days ago (2025-09-23 19:24:31 UTC) | 17 | Rust | Experimental ClickHouse Native Client and Native file reader Extension for Du... |
| 25 | [clamp](https://duckdb.org/community_extensions/extensions/clamp.html) | [duckdb_clamp](https://github.com/oglego/duckdb_clamp) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-02-14 01:58:57 UTC) | 2 | C++ | The Clamp extension introduces range-clamping scalar functions to DuckDB. Ini... |
| 26 | [cloudfront](https://duckdb.org/community_extensions/extensions/cloudfront.html) | [duckdb-cloudfront](https://github.com/midwork-finds-jobs/duckdb-cloudfront) | 🟢 Ongoing | 2 - ✅ Active | 8 days ago (2026-02-05 15:32:51 UTC) | 1 | C++ | DuckDB module which provides custom authentication methods on top of httpfs m... |
| 27 | [crawler](https://duckdb.org/community_extensions/extensions/crawler.html) | [duckdb-crawler](https://github.com/midwork-finds-jobs/duckdb-crawler) | 🟢 Ongoing | 1 - 🔥 Very Active | 5 days ago (2026-02-08 06:32:31 UTC) | 4 | C++ | DuckDB extension: crawler by midwork-finds-jobs |
| 28 | [cronjob](https://duckdb.org/community_extensions/extensions/cronjob.html) | [cronjob](https://github.com/Query-farm/cronjob) | 🟢 Ongoing | 2 - ✅ Active | 12 days ago (2026-02-01 08:02:30 UTC) | 46 | C++ | DuckDB CronJob Extension |
| 29 | [crypto](https://duckdb.org/community_extensions/extensions/crypto.html) | [crypto](https://github.com/Query-farm/crypto) | 🟢 Ongoing | 2 - ✅ Active | 12 days ago (2026-02-01 08:02:34 UTC) | 27 | C++ | DuckDB Extension for cryptographic hash functions and HMAC |
| 30 | [curl_httpfs](https://duckdb.org/community_extensions/extensions/curl_httpfs.html) | [duckdb-curl-filesystem](https://github.com/dentiny/duckdb-curl-filesystem) | 🟢 Ongoing | 2 - ✅ Active | 18 days ago (2026-01-27 05:00:04 UTC) | 8 | C++ | Filesystem built upon libcurl. |
| 31 | [cwiqduck](https://duckdb.org/community_extensions/extensions/cwiqduck.html) | [cwiqduck](https://github.com/cwiq-os/cwiqduck) | 🟢 Ongoing | 3 - 🟡 Stable | 67 days ago (2025-12-09 02:09:40 UTC) | 3 | C++ | DuckDB extensions for CWIQ |
| 32 | [dash](https://duckdb.org/community_extensions/extensions/dash.html) | [dash](https://github.com/gropaul/dash) | ❓ Unknown | 3 - 🟡 Stable | 66 days ago (2025-12-09 22:02:22 UTC) | 36 | C++ | DuckDB Extension featuring a Query Builder GUI and Dashboarding features |
| 33 | [datasketches](https://duckdb.org/community_extensions/extensions/datasketches.html) | [datasketches](https://github.com/Query-farm/datasketches) | 🟢 Ongoing | 2 - ✅ Active | 12 days ago (2026-02-01 08:02:42 UTC) | 40 | C++ | Integrates DuckDB with the high-performance Apache DataSketches library. This... |
| 34 | [dazzleduck](https://github.com/dazzleduck-web/dazzleduck-sql-duckdb) | [dazzleduck-sql-duckdb](https://github.com/dazzleduck-web/dazzleduck-sql-duckdb) | ❓ Unknown | 2 - ✅ Active | 15 days ago (2026-01-29 08:11:53 UTC) | 0 | C++ | DuckDB extension: dazzleduck by dazzleduck-web |
| 35 | [dns](https://duckdb.org/community_extensions/extensions/dns.html) | [duckdb-dns](https://github.com/tobilg/duckdb-dns) | 🟢 Ongoing | 2 - ✅ Active | 17 days ago (2026-01-27 11:51:21 UTC) | 15 | Rust | DNS (Reverse) Lookup Extension for DuckDB |
| 36 | [dplyr](https://duckdb.org/community_extensions/extensions/dplyr.html) | [libdplyr](https://github.com/mrchypark/libdplyr) | ❓ Unknown | 1 - 🔥 Very Active | today (2026-02-13 20:10:59 UTC) | 13 | Rust | DuckDB extension: dplyr by mrchypark |
| 37 | [dqtest](https://duckdb.org/community_extensions/extensions/dqtest.html) | [duckdb-dataquality-extension](https://github.com/vhe74/duckdb-dataquality-extension) | 🟢 Ongoing | 2 - ✅ Active | 10 days ago (2026-02-03 18:35:04 UTC) | 3 | C++ | Duckdb extension to run data quality tests |
| 38 | [duck_block_utils](https://duckdb.org/community_extensions/extensions/duck_block_utils.html) | [duckdb_duck_block_utils](https://github.com/teaguesterling/duckdb_duck_block_utils) | 🟢 Ongoing | 1 - 🔥 Very Active | 6 days ago (2026-02-07 22:38:25 UTC) | 1 | C++ | A collection of utility functions to work with doc block-style structures and... |
| 39 | [duck_delta_share](https://duckdb.org/community_extensions/extensions/duck_delta_share.html) | [duck_delta_share](https://github.com/cwiq-os/duck_delta_share) | 🟢 Ongoing | 2 - ✅ Active | 25 days ago (2026-01-20 02:52:58 UTC) | 2 | C++ | DuckDB extension for enabling Delta Sharing client capabilities.  |
| 40 | [duck_hunt](https://duckdb.org/community_extensions/extensions/duck_hunt.html) | [duck_hunt](https://github.com/teaguesterling/duck_hunt) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-02-13 23:21:36 UTC) | 3 | C++ | Tools for working with unit test suite results |
| 41 | [duck_tails](https://duckdb.org/community_extensions/extensions/duck_tails.html) | [duck_tails](https://github.com/teaguesterling/duck_tails) | 🟢 Ongoing | 1 - 🔥 Very Active | 6 days ago (2026-02-07 22:25:33 UTC) | 12 | C++ | A DuckDB extension for exploring and reading git history. |
| 42 | [duckdb_mcp](https://duckdb.org/community_extensions/extensions/duckdb_mcp.html) | [duckdb_mcp](https://github.com/teaguesterling/duckdb_mcp) | 🟢 Ongoing | 1 - 🔥 Very Active | 6 days ago (2026-02-07 22:30:26 UTC) | 32 | C++ | A simple MCP server extension for DuckDB |
| 43 | [duckgl](https://duckdb.org/community_extensions/extensions/duckgl.html) | [duckgl](https://github.com/nkwork9999/duckgl) | ❓ Unknown | 3 - 🟡 Stable | 49 days ago (2025-12-27 04:09:47 UTC) | 3 | C++ | DuckDB extension: duckgl by nkwork9999 |
| 44 | [duckherder](https://duckdb.org/community_extensions/extensions/duckherder.html) | [duckdb-distributed-execution](https://github.com/dentiny/duckdb-distributed-execution) | 🟢 Ongoing | 1 - 🔥 Very Active | 4 days ago (2026-02-09 18:55:02 UTC) | 47 | C++ | Distributed execution for duckdb queries. |
| 45 | [duckpgq](https://duckdb.org/community_extensions/extensions/duckpgq.html) | [duckpgq-extension](https://github.com/cwida/duckpgq-extension) | ❓ Unknown | 1 - 🔥 Very Active | 3 days ago (2026-02-10 14:50:29 UTC) | 358 | C++ | DuckDB extension that adds support for SQL/PGQ and graph algorithms |
| 46 | [ducksync](https://duckdb.org/community_extensions/extensions/ducksync.html) | [ducksync](https://github.com/danjsiegel/ducksync) | 🟢 Ongoing | 2 - ✅ Active | 12 days ago (2026-02-02 04:25:58 UTC) | 5 | C++ | DuckDB extension: ducksync by danjsiegel |
| 47 | [eeagrid](https://duckdb.org/community_extensions/extensions/eeagrid.html) | [duckdb-eeagrid](https://github.com/ahuarte47/duckdb-eeagrid) | 🟢 Ongoing | 2 - ✅ Active | 17 days ago (2026-01-27 07:01:15 UTC) | 0 | C++ | Functions for transforming XY coordinates to and from the EEA Reference Grid... |
| 48 | [elasticsearch](https://duckdb.org/community_extensions/extensions/elasticsearch.html) | [duckdb-elasticsearch](https://github.com/tlinhart/duckdb-elasticsearch) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-02-13 11:47:16 UTC) | 12 | C++ | Query Elasticsearch data directly from DuckDB |
| 49 | [encoding](https://duckdb.org/community_extensions/extensions/encoding.html) | [duckdb-encoding](https://github.com/onnimonni/duckdb-encoding) | 🟡 Archived | 2 - ✅ Active | 10 days ago (2026-02-03 07:11:42 UTC) | 3 | Rust | DuckDB extension: encoding by onnimonni |
| 50 | [erpl_web](https://duckdb.org/community_extensions/extensions/erpl_web.html) | [erpl-web](https://github.com/DataZooDE/erpl-web) | 🟢 Ongoing | 2 - ✅ Active | 17 days ago (2026-01-27 21:02:04 UTC) | 24 | C++ | ERPL is a DuckDB extension to connect to API based ecosystems via standard in... |
| 51 | [eurostat](https://duckdb.org/community_extensions/extensions/eurostat.html) | [duckdb-eurostat](https://github.com/ahuarte47/duckdb-eurostat) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-02-13 07:46:01 UTC) | 27 | C++ | DuckDB extension for reading data from EUROSTAT database using SQL  |
| 52 | [evalexpr_rhai](https://duckdb.org/community_extensions/extensions/evalexpr_rhai.html) | [evalexpr_rhai](https://github.com/Query-farm/evalexpr_rhai) | 🟢 Ongoing | 2 - ✅ Active | 12 days ago (2026-02-01 08:02:55 UTC) | 24 | C++ | A DuckDB extension to evaluate the Rhai scripting language as part of SQL. |
| 53 | [faiss](https://duckdb.org/community_extensions/extensions/faiss.html) | [duckdb-faiss-ext](https://github.com/duckdb-faiss-ext/duckdb-faiss-ext) | 🟢 Ongoing | 3 - 🟡 Stable | 67 days ago (2025-12-09 01:30:08 UTC) | 29 | Go | DuckDB wrapper for FAISS - Experimental |
| 54 | [fakeit](https://duckdb.org/community_extensions/extensions/fakeit.html) | [duckdb-fakeit](https://github.com/tobilg/duckdb-fakeit) | 🟢 Ongoing | 2 - ✅ Active | 17 days ago (2026-01-27 11:41:16 UTC) | 9 | Rust | DuckDB extension: fakeit by tobilg |
| 55 | [file_dialog](https://duckdb.org/community_extensions/extensions/file_dialog.html) | [duckdb-ext-file-dialog](https://github.com/yutannihilation/duckdb-ext-file-dialog) | 🟢 Ongoing | 2 - ✅ Active | 15 days ago (2026-01-29 11:36:23 UTC) | 15 | Rust | A DuckDB extension to choose file interactively using native file open dialogs |
| 56 | [fire_duck_ext](https://duckdb.org/community_extensions/extensions/fire_duck_ext.html) | [fire_duck_ext](https://github.com/BorisBesky/fire_duck_ext) | 🟢 Ongoing | 1 - 🔥 Very Active | 4 days ago (2026-02-09 07:17:21 UTC) | 1 | C++ | duckdb extension for firestore |
| 57 | [fit](https://duckdb.org/community_extensions/extensions/fit.html) | [duckdb-fit-extension](https://github.com/antoriche/duckdb-fit-extension) | ❓ Unknown | 3 - 🟡 Stable | 60 days ago (2025-12-15 19:16:40 UTC) | 1 | C++ | DuckDB extension: fit by antoriche |
| 58 | [fivetran](https://duckdb.org/community_extensions/extensions/fivetran.html) | [fivetran](https://github.com/lnkuiper/fivetran) | 🟢 Ongoing | 2 - ✅ Active | 17 days ago (2026-01-27 11:13:43 UTC) | 0 | C++ | DuckDB extension: fivetran by lnkuiper |
| 59 | [flock](https://duckdb.org/community_extensions/extensions/flock.html) | [flock](https://github.com/dais-polymtl/flock) | 🟢 Ongoing | 2 - ✅ Active | 21 days ago (2026-01-24 00:14:39 UTC) | 293 | C++ | Flock: multimodal querying for DuckDB |
| 60 | [func_apply](https://duckdb.org/community_extensions/extensions/func_apply.html) | [duckdb_func_apply](https://github.com/teaguesterling/duckdb_func_apply) | ❓ Unknown | 3 - 🟡 Stable | 33 days ago (2026-01-11 19:20:07 UTC) | 3 | C++ | An exension to allow dynamic function application |
| 61 | [fuzzycomplete](https://duckdb.org/community_extensions/extensions/fuzzycomplete.html) | [fuzzycomplete](https://github.com/Query-farm/fuzzycomplete) | 🟢 Ongoing | 2 - ✅ Active | 12 days ago (2026-02-01 08:02:59 UTC) | 25 | C++ | DuckDB Extension for fuzzy string matching based autocompletion |
| 62 | [gaggle](https://duckdb.org/community_extensions/extensions/gaggle.html) | [gaggle](https://github.com/CogitatorTech/gaggle) | 🟢 Ongoing | 2 - ✅ Active | 16 days ago (2026-01-28 17:22:38 UTC) | 15 | Rust | A DuckDB extension for working with Kaggle datasets |
| 63 | [gcs](https://duckdb.org/community_extensions/extensions/gcs.html) | [duckdb-gcs](https://github.com/northpolesec/duckdb-gcs) | 🟢 Ongoing | 3 - 🟡 Stable | 73 days ago (2025-12-02 12:17:16 UTC) | 11 | C++ | A GCS-native extension for DuckDB |
| 64 | [geography](https://duckdb.org/community_extensions/extensions/geography.html) | [duckdb-geography](https://github.com/paleolimbot/duckdb-geography) | 🟢 Ongoing | 4 - 🟠 Stale | 134 days ago (2025-10-02 11:09:38 UTC) | 38 | C++ | Geospatial data extension by paleolimbot |
| 65 | [geotiff](https://duckdb.org/community_extensions/extensions/geotiff.html) | [duckdb-geotiff](https://github.com/babaknaimi/duckdb-geotiff) | ❓ Unknown | 4 - 🟠 Stale | 178 days ago (2025-08-20 05:12:15 UTC) | 2 | C++ | Duckdb extension to read GeoTiffs directly with duckdb database |
| 66 | [gsheets](https://duckdb.org/community_extensions/extensions/gsheets.html) | [duckdb_gsheets](https://github.com/evidence-dev/duckdb_gsheets) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-02-13 17:44:05 UTC) | 332 | C++ | DuckDB extension to read and write Google Sheets using SQL |
| 67 | [h3](https://duckdb.org/community_extensions/extensions/h3.html) | [h3-duckdb](https://github.com/isaacbrodsky/h3-duckdb) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-02-12 20:26:29 UTC) | 242 | C++ | Bindings for H3 to DuckDB |
| 68 | [h5db](https://duckdb.org/community_extensions/extensions/h5db.html) | [h5db](https://github.com/jokasimr/h5db) | 🟢 Ongoing | 2 - ✅ Active | 16 days ago (2026-01-28 06:35:21 UTC) | 1 | C++ | Duckdb extension for reading HDF5 files. |
| 69 | [hashfuncs](https://duckdb.org/community_extensions/extensions/hashfuncs.html) | [hashfuncs](https://github.com/Query-farm/hashfuncs) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-02-13 14:52:47 UTC) | 12 | C++ | A DuckDB extension that supplies non-cryptographic hash functions. |
| 70 | [hdf5](https://duckdb.org/community_extensions/extensions/hdf5.html) | [duckdb-hdf5](https://github.com/Berrysoft/duckdb-hdf5) | ❓ Unknown | 2 - ✅ Active | 10 days ago (2026-02-03 19:24:06 UTC) | 12 | Rust | HDF5 plugin for duckdb |
| 71 | [highs](https://duckdb.org/community_extensions/extensions/highs.html) | [HiGHS-duckdb](https://github.com/fhk/HiGHS-duckdb) | ❓ Unknown | 4 - 🟠 Stale | 181 days ago (2025-08-16 06:41:18 UTC) | 1 | C++ | Run the solver in the database! |
| 72 | [hostfs](https://duckdb.org/community_extensions/extensions/hostfs.html) | [hostFS](https://github.com/gropaul/hostFS) | ❓ Unknown | 4 - 🟠 Stale | 135 days ago (2025-10-01 21:02:13 UTC) | 29 | C++ | DuckDB extension: hostfs by gropaul |
| 73 | [html_query](https://duckdb.org/community_extensions/extensions/html_query.html) | [duckdb_html_query](https://github.com/midwork-finds-jobs/duckdb_html_query) | ❓ Unknown | 2 - ✅ Active | 8 days ago (2026-02-05 15:33:13 UTC) | 1 | Rust | Filter HTML inside duckdb |
| 74 | [html_readability](https://duckdb.org/community_extensions/extensions/html_readability.html) | [duckdb-html-readability](https://github.com/midwork-finds-jobs/duckdb-html-readability) | ❓ Unknown | 2 - ✅ Active | 8 days ago (2026-02-05 15:33:16 UTC) | 0 | Rust | DuckDB extension to parse html to readable text |
| 75 | [http_client](https://duckdb.org/community_extensions/extensions/http_client.html) | [httpclient](https://github.com/Query-farm/httpclient) | 🟢 Ongoing | 2 - ✅ Active | 12 days ago (2026-02-01 08:03:06 UTC) | 77 | C++ | DuckDB HTTP GET/POST Client in a Community Extension |
| 76 | [http_request](https://duckdb.org/community_extensions/extensions/http_request.html) | [duckdb_http_request](https://github.com/midwork-finds-jobs/duckdb_http_request) | 🟢 Ongoing | 2 - ✅ Active | 8 days ago (2026-02-05 15:32:56 UTC) | 0 | C++ | Uses the native duckdb httputil to make extra requests in SELECT |
| 77 | [httpd_log](https://duckdb.org/community_extensions/extensions/httpd_log.html) | [duckdb-httpd-log](https://github.com/saygox/duckdb-httpd-log) | ❓ Unknown | 3 - 🟡 Stable | 33 days ago (2026-01-12 06:14:58 UTC) | 0 | C++ | duckdb extension |
| 78 | [httpserver](https://duckdb.org/community_extensions/extensions/httpserver.html) | [httpserver](https://github.com/Query-farm/httpserver) | 🟢 Ongoing | 2 - ✅ Active | 12 days ago (2026-02-01 08:03:10 UTC) | 269 | C++ | DuckDB HTTP API Server and Query Interface in a  Community Extension |
| 79 | [infera](https://duckdb.org/community_extensions/extensions/infera.html) | [infera](https://github.com/CogitatorTech/infera) | 🟢 Ongoing | 2 - ✅ Active | 16 days ago (2026-01-28 17:21:13 UTC) | 126 | Rust | A DuckDB extension for in-database inference |
| 80 | [inflector](https://duckdb.org/community_extensions/extensions/inflector.html) | [inflector](https://github.com/Query-farm/inflector) | ❓ Unknown | 2 - ✅ Active | 12 days ago (2026-02-01 08:03:18 UTC) | 6 | C++ | Powerful string case transformation and inflection capabilities directly to y... |
| 81 | [ion](https://duckdb.org/community_extensions/extensions/ion.html) | [duckdb-ion](https://github.com/kestra-io/duckdb-ion) | ❓ Unknown | 1 - 🔥 Very Active | 7 days ago (2026-02-06 18:38:54 UTC) | 1 | C++ | AWS Ion extension for DuckDB |
| 82 | [json_schema](https://duckdb.org/community_extensions/extensions/json_schema.html) | [json_schema](https://github.com/Query-farm/json_schema) | 🟢 Ongoing | 2 - ✅ Active | 12 days ago (2026-02-01 08:03:29 UTC) | 2 | C++ | A DuckDB extension that bring support for validating JSON data using JSON sch... |
| 83 | [jsonata](https://duckdb.org/community_extensions/extensions/jsonata.html) | [jsonata](https://github.com/Query-farm/jsonata) | 🟢 Ongoing | 2 - ✅ Active | 12 days ago (2026-02-01 08:03:33 UTC) | 2 | C++ | The JSONata extension for DuckDB enables expressive, JSON-focused querying an... |
| 84 | [jwt](https://duckdb.org/community_extensions/extensions/jwt.html) | [duckdb_jwt](https://github.com/GalvinGao/duckdb_jwt) | ❓ Unknown | 4 - 🟠 Stale | 220 days ago (2025-07-09 00:13:56 UTC) | 0 | C++ | DuckDB extension: jwt by GalvinGao |
| 85 | [lance](https://duckdb.org/community_extensions/extensions/lance.html) | [lance-duckdb](https://github.com/lance-format/lance-duckdb) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-02-13 18:51:51 UTC) | 73 | C++ | The lance extensions for DuckDB enable reading and writing of lance tables. |
| 86 | [level_pivot](https://github.com/halgari/duckdb-level-pivot) | [duckdb-level-pivot](https://github.com/halgari/duckdb-level-pivot) | ❓ Unknown | 1 - 🔥 Very Active | today (2026-02-12 22:14:53 UTC) | 0 | C++ | DuckDB extension: level_pivot by halgari |
| 87 | [lindel](https://duckdb.org/community_extensions/extensions/lindel.html) | [lindel](https://github.com/Query-farm/lindel) | 🟢 Ongoing | 2 - ✅ Active | 12 days ago (2026-02-01 07:54:50 UTC) | 58 | C++ | DuckDB Extension Linearization/Delinearization, Z-Order, Hilbert and Morton C... |
| 88 | [llm](https://duckdb.org/community_extensions/extensions/llm.html) | [duckdb-llm](https://github.com/midwork-finds-jobs/duckdb-llm) | 🟢 Ongoing | 2 - ✅ Active | 8 days ago (2026-02-05 15:33:05 UTC) | 1 | C++ | DuckDB extension: llm by midwork-finds-jobs |
| 89 | [lsh](https://duckdb.org/community_extensions/extensions/lsh.html) | [lsh](https://github.com/princeton-ddss/lsh) | 🟢 Ongoing | 2 - ✅ Active | 17 days ago (2026-01-27 16:03:44 UTC) | 11 | Rust | DuckDB community extension for locality-sensitive hashing (LSH) |
| 90 | [lua](https://duckdb.org/community_extensions/extensions/lua.html) | [duckdb-lua](https://github.com/isaacbrodsky/duckdb-lua) | 🟢 Ongoing | 2 - ✅ Active | 14 days ago (2026-01-30 23:30:44 UTC) | 9 | C++ | DuckDB extension to evaluate Lua expressions. |
| 91 | [magic](https://duckdb.org/community_extensions/extensions/magic.html) | [duckdb_magic](https://github.com/carlopi/duckdb_magic) | 🟢 Ongoing | 4 - 🟠 Stale | 139 days ago (2025-09-27 18:50:32 UTC) | 7 | C++ | Auto-detect file types via `libmagic` (`file` utility) |
| 92 | [marisa](https://duckdb.org/community_extensions/extensions/marisa.html) | [marisa](https://github.com/Query-farm/marisa) | 🟢 Ongoing | 2 - ✅ Active | 12 days ago (2026-02-01 08:05:41 UTC) | 10 | C++ | The Marisa extension by Query.Farm integrates the fast, space-efficient MARIS... |
| 93 | [markdown](https://duckdb.org/community_extensions/extensions/markdown.html) | [duckdb_markdown](https://github.com/teaguesterling/duckdb_markdown) | 🟢 Ongoing | 2 - ✅ Active | 16 days ago (2026-01-28 22:52:54 UTC) | 14 | C++ | Heirarchical markdown parsing for DuckDB |
| 94 | [miint](https://duckdb.org/community_extensions/extensions/miint.html) | [duckdb-miint](https://github.com/the-miint/duckdb-miint) | 🟢 Ongoing | 1 - 🔥 Very Active | 2 days ago (2026-02-11 23:17:54 UTC) | 1 | C | DuckDB extension: miint by the-miint |
| 95 | [minijinja](https://duckdb.org/community_extensions/extensions/minijinja.html) | [minijinja](https://github.com/Query-farm/minijinja) | 🟢 Ongoing | 2 - ✅ Active | 12 days ago (2026-02-01 08:05:44 UTC) | 5 | C++ | DuckDB extension: minijinja |
| 96 | [miniplot](https://duckdb.org/community_extensions/extensions/miniplot.html) | [miniplot](https://github.com/nkwork9999/miniplot) | 🟢 Ongoing | 4 - 🟠 Stale | 91 days ago (2025-11-15 02:42:43 UTC) | 17 | C++ | DuckDB extension: miniplot by nkwork9999 |
| 97 | [mlpack](https://duckdb.org/community_extensions/extensions/mlpack.html) | [duckdb-mlpack](https://github.com/eddelbuettel/duckdb-mlpack) | 🟢 Ongoing | 2 - ✅ Active | 17 days ago (2026-01-27 14:18:00 UTC) | 18 | C++ | Bringing mlpack to duckdb |
| 98 | [monetary](https://duckdb.org/community_extensions/extensions/monetary.html) | [monetary](https://github.com/fyffee/monetary) | 🟢 Ongoing | 2 - ✅ Active | 15 days ago (2026-01-29 11:29:01 UTC) | 0 | C++ | DuckDB extension: monetary by fyffee |
| 99 | [mongo](https://duckdb.org/community_extensions/extensions/mongo.html) | [duckdb-mongo](https://github.com/stephaniewang526/duckdb-mongo) | 🟢 Ongoing | 1 - 🔥 Very Active | 7 days ago (2026-02-06 21:25:53 UTC) | 38 | C++ | Integrates DuckDB with MongoDB, enabling direct SQL queries over MongoDB coll... |
| 100 | [mooncake](https://duckdb.org/community_extensions/extensions/mooncake.html) | [duckdb_mooncake](https://github.com/Mooncake-Labs/duckdb_mooncake) | 🟢 Ongoing | 4 - 🟠 Stale | 110 days ago (2025-10-26 07:13:05 UTC) | 7 | C++ | Read Iceberg tables written by moonlink in real time |
| 101 | [msolap](https://duckdb.org/community_extensions/extensions/msolap.html) | [duckdb-msolap-extension](https://github.com/Hugoberry/duckdb-msolap-extension) | 🟢 Ongoing | 4 - 🟠 Stale | 142 days ago (2025-09-24 16:33:46 UTC) | 12 | C++ | DuckDB extension: msolap by Hugoberry |
| 102 | [mssql](https://duckdb.org/community_extensions/extensions/mssql.html) | [mssql-extension](https://github.com/hugr-lab/mssql-extension) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-02-13 21:06:19 UTC) | 61 | C++ | DuckDB extension for Microsoft SQL Server (TDS + TLS), with catalog integrati... |
| 103 | [nanoarrow](https://duckdb.org/community_extensions/extensions/nanoarrow.html) | [duckdb-nanoarrow](https://github.com/paleolimbot/duckdb-nanoarrow) | ❓ Unknown | 3 - 🟡 Stable | 39 days ago (2026-01-05 20:26:36 UTC) | 66 | C++ | DuckDB extension: nanoarrow by paleolimbot |
| 104 | [nanodbc](https://duckdb.org/community_extensions/extensions/nanodbc.html) | [duckdb-nanodbc-extension](https://github.com/Hugoberry/duckdb-nanodbc-extension) | 🟢 Ongoing | 3 - 🟡 Stable | 73 days ago (2025-12-02 16:24:39 UTC) | 53 | C++ | Database connectivity extension by Hugoberry |
| 105 | [nats_js](https://duckdb.org/community_extensions/extensions/nats_js.html) | [duckdb-nats-jetstream](https://github.com/brannn/duckdb-nats-jetstream) | 🟢 Ongoing | 4 - 🟠 Stale | 91 days ago (2025-11-14 07:24:21 UTC) | 16 | C++ | DuckDB extension for querying NATS JetStream message streams with SQL |
| 106 | [netquack](https://duckdb.org/community_extensions/extensions/netquack.html) | [duckdb-netquack](https://github.com/hatamiarash7/duckdb-netquack) | ❓ Unknown | 3 - 🟡 Stable | 36 days ago (2026-01-08 08:14:54 UTC) | 31 | C++ | DuckDB extension for parsing, extracting, and analyzing domains, URIs, and pa... |
| 107 | [oast](https://duckdb.org/community_extensions/extensions/oast.html) | [duckdb-oast](https://github.com/hrbrmstr/duckdb-oast) | 🟢 Ongoing | 1 - 🔥 Very Active | 3 days ago (2026-02-10 12:00:32 UTC) | 3 | C | A DuckDB extension for validating, decoding, and extracting OAST (Out-of-Band... |
| 108 | [observefs](https://duckdb.org/community_extensions/extensions/observefs.html) | [duckdb-filesystem-observability](https://github.com/dentiny/duckdb-filesystem-observability) | 🟢 Ongoing | 1 - 🔥 Very Active | 5 days ago (2026-02-08 21:42:30 UTC) | 10 | C++ | Provides observability for duckdb filesystem. |
| 109 | [ofquack](https://duckdb.org/community_extensions/extensions/ofquack.html) | [ofquack](https://github.com/krokozyab/ofquack) | ❓ Unknown | 4 - 🟠 Stale | 297 days ago (2025-04-22 12:24:17 UTC) | 6 | C++ | Oracle Fusion DuckDB extension  |
| 110 | [onager](https://duckdb.org/community_extensions/extensions/onager.html) | [onager](https://github.com/CogitatorTech/onager) | 🟢 Ongoing | 2 - ✅ Active | 13 days ago (2026-01-31 19:06:07 UTC) | 120 | Rust | A DuckDB extension for graph data analytics |
| 111 | [onelake](https://duckdb.org/community_extensions/extensions/onelake.html) | [duckdb_onelake](https://github.com/datumnova/duckdb_onelake) | ❓ Unknown | 3 - 🟡 Stable | 74 days ago (2025-12-01 10:28:22 UTC) | 19 | C++ | DuckDB extension: onelake by datumnova |
| 112 | [open_prompt](https://duckdb.org/community_extensions/extensions/open_prompt.html) | [openprompt](https://github.com/Query-farm/openprompt) | 🟢 Ongoing | 2 - ✅ Active | 12 days ago (2026-02-01 08:05:48 UTC) | 55 | C++ | DuckDB Community Extension to prompt LLMs from SQL |
| 113 | [otlp](https://duckdb.org/community_extensions/extensions/otlp.html) | [duckdb-otlp](https://github.com/smithclay/duckdb-otlp) | 🟢 Ongoing | 3 - 🟡 Stable | 31 days ago (2026-01-14 04:35:46 UTC) | 36 | C++ | query OpenTelemetry metrics, logs, and traces (OTLP) in duckdb |
| 114 | [parser_tools](https://duckdb.org/community_extensions/extensions/parser_tools.html) | [duckdb_extension_parser_tools](https://github.com/hotdata-dev/duckdb_extension_parser_tools) | 🟢 Ongoing | 2 - ✅ Active | 14 days ago (2026-01-30 16:44:26 UTC) | 23 | C++ | Parse sql - with sql! |
| 115 | [pbix](https://duckdb.org/community_extensions/extensions/pbix.html) | [duckdb-pbix-extension](https://github.com/Hugoberry/duckdb-pbix-extension) | ❓ Unknown | 4 - 🟠 Stale | 112 days ago (2025-10-24 13:47:34 UTC) | 34 | C++ | Duckdb extension for parsing the metadata and contents of the embedded data m... |
| 116 | [pcap_reader](https://duckdb.org/community_extensions/extensions/pcap_reader.html) | [pcap](https://github.com/Query-farm/pcap) | ❓ Unknown | 4 - 🟠 Stale | 143 days ago (2025-09-23 19:24:42 UTC) | 12 | Rust | DuckDB PCAP Reader Extension made in Rust |
| 117 | [pdal](https://duckdb.org/community_extensions/extensions/pdal.html) | [duckdb-pdal](https://github.com/ahuarte47/duckdb-pdal) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-02-12 07:53:43 UTC) | 25 | C++ | DuckDB extension for manipulating point cloud data using SQL |
| 118 | [pivot_table](https://duckdb.org/community_extensions/extensions/pivot_table.html) | [pivot_table](https://github.com/Alex-Monahan/pivot_table) | ❓ Unknown | 4 - 🟠 Stale | over a year ago (2024-09-22 21:18:45 UTC) | 18 | C++ | Full spreadsheet-style pivot table through SQL macros. Just specify values, r... |
| 119 | [poached](https://duckdb.org/community_extensions/extensions/poached.html) | [poached](https://github.com/sidequery/poached) | ❓ Unknown | 3 - 🟡 Stable | 49 days ago (2025-12-26 21:13:19 UTC) | 8 | C++ | A DuckDB extension that exposes SQL parsing functionality for building IDEs,... |
| 120 | [prql](https://duckdb.org/community_extensions/extensions/prql.html) | [duckdb-prql](https://github.com/ywelsch/duckdb-prql) | 🟢 Ongoing | 4 - 🟠 Stale | 144 days ago (2025-09-22 18:45:53 UTC) | 317 | C++ | PRQL as a DuckDB extension |
| 121 | [psql](https://duckdb.org/community_extensions/extensions/psql.html) | [duckdb-psql](https://github.com/ywelsch/duckdb-psql) | 🟢 Ongoing | 4 - 🟠 Stale | 144 days ago (2025-09-22 18:45:44 UTC) | 103 | C++ | A piped SQL for DuckDB |
| 122 | [pst](https://duckdb.org/community_extensions/extensions/pst.html) | [duckdb-pst](https://github.com/intellekthq/duckdb-pst) | 🟢 Ongoing | 2 - ✅ Active | 11 days ago (2026-02-03 02:04:03 UTC) | 10 | C++ | In-place querying of Microsoft PST files, directly from storage, with SQL. |
| 123 | [psyduck](https://duckdb.org/community_extensions/extensions/psyduck.html) | [psyduck](https://github.com/Ian-Fogelman/psyduck) | 🟢 Ongoing | 3 - 🟡 Stable | 61 days ago (2025-12-14 15:10:39 UTC) | 6 | C++ | Pysduck a DuckDB community extension about Pokémon. |
| 124 | [pyroscope](https://duckdb.org/community_extensions/extensions/pyroscope.html) | [pyroscope](https://github.com/Query-farm/pyroscope) | ❓ Unknown | 4 - 🟠 Stale | 143 days ago (2025-09-23 19:24:44 UTC) | 20 | Rust | DuckDB Pyroscope Extension for Continuous Profiling |
| 125 | [quack](https://duckdb.org/community_extensions/extensions/quack.html) | [extension-template](https://github.com/duckdb/extension-template) | ❓ Unknown | 2 - ✅ Active | 8 days ago (2026-02-05 11:38:51 UTC) | 262 | Python | Template for DuckDB extensions to help you develop, test and deploy a custom... |
| 126 | [quackfix](https://duckdb.org/community_extensions/extensions/quackfix.html) | [QuackFIX](https://github.com/hyehudai/QuackFIX) | ❓ Unknown | 3 - 🟡 Stable | 50 days ago (2025-12-25 10:36:24 UTC) | 17 | C++ | Fix log extension for duckdb |
| 127 | [quackformers](https://duckdb.org/community_extensions/extensions/quackformers.html) | [quackformers](https://github.com/martin-conur/quackformers) | ❓ Unknown | 3 - 🟡 Stable | 54 days ago (2025-12-21 18:43:16 UTC) | 10 | Rust | DuckDB NLP extension. |
| 128 | [quackstats](https://duckdb.org/community_extensions/extensions/quackstats.html) | [quackstats](https://github.com/jasadams/quackstats) | 🟢 Ongoing | 2 - ✅ Active | 12 days ago (2026-02-01 12:01:35 UTC) | 1 | Rust | DuckDB extension for time series forecasting and seasonality detection |
| 129 | [quackstore](https://duckdb.org/community_extensions/extensions/quackstore.html) | [QuackStore](https://github.com/coginiti-dev/QuackStore) | 🟢 Ongoing | 2 - ✅ Active | 17 days ago (2026-01-27 15:27:17 UTC) | 110 | C++ | DuckDB extension: quackstore by coginiti-dev |
| 130 | [quickjs](https://duckdb.org/community_extensions/extensions/quickjs.html) | [quickjs](https://github.com/Query-farm/quickjs) | 🟢 Ongoing | 2 - ✅ Active | 12 days ago (2026-02-01 08:05:52 UTC) | 11 | C++ | DuckDB extension: quickjs by quackscience |
| 131 | [radio](https://duckdb.org/community_extensions/extensions/radio.html) | [radio](https://github.com/Query-farm/radio) | 🟢 Ongoing | 2 - ✅ Active | 12 days ago (2026-02-01 08:05:55 UTC) | 35 | C++ | Radio is a DuckDB extension by Query.Farm that brings real-time event streams... |
| 132 | [rapidfuzz](https://duckdb.org/community_extensions/extensions/rapidfuzz.html) | [rapidfuzz](https://github.com/Query-farm/rapidfuzz) | 🟢 Ongoing | 2 - ✅ Active | 12 days ago (2026-02-01 08:05:58 UTC) | 12 | C++ | DuckDB Community Extension adding RapidFuzz algorithms for search, deduplicat... |
| 133 | [rate_limit_fs](https://duckdb.org/community_extensions/extensions/rate_limit_fs.html) | [duckdb-rate-limit-filesystem](https://github.com/dentiny/duckdb-rate-limit-filesystem) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-02-13 04:10:18 UTC) | 1 | C++ | DuckDB extension: rate_limit_fs by dentiny |
| 134 | [read_lines](https://duckdb.org/community_extensions/extensions/read_lines.html) | [duckdb_read_lines](https://github.com/teaguesterling/duckdb_read_lines) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-02-14 00:34:57 UTC) | 0 | C++ | Simple parsers for fast extraction from line-based files  |
| 135 | [read_stat](https://duckdb.org/community_extensions/extensions/read_stat.html) | [duckdb-read-stat](https://github.com/mettekou/duckdb-read-stat) | 🟢 Ongoing | 3 - 🟡 Stable | 78 days ago (2025-11-27 13:46:07 UTC) | 27 | C | Read data sets from SAS, Stata, and SPSS from DuckDB with ReadStat |
| 136 | [redis](https://duckdb.org/community_extensions/extensions/redis.html) | [redis](https://github.com/Query-farm/redis) | 🟢 Ongoing | 2 - ✅ Active | 12 days ago (2026-02-01 08:06:05 UTC) | 9 | C++ | DuckDB Redis Client community extension |
| 137 | [rusty_quack](https://duckdb.org/community_extensions/extensions/rusty_quack.html) | [extension-template-rs](https://github.com/duckdb/extension-template-rs) | ❓ Unknown | 2 - ✅ Active | 10 days ago (2026-02-03 15:32:23 UTC) | 94 | Rust | (Experimental) Template for Rust-based DuckDB extensions |
| 138 | [rusty_sheet](https://duckdb.org/community_extensions/extensions/rusty_sheet.html) | [rusty-sheet](https://github.com/redraiment/rusty-sheet) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-02-13 02:27:56 UTC) | 63 | Rust | An Excel/WPS/OpenDocument Spreadsheets file reader for DuckDB |
| 139 | [sazgar](https://duckdb.org/community_extensions/extensions/sazgar.html) | [Sazgar](https://github.com/Angelerator/Sazgar) | ❓ Unknown | 3 - 🟡 Stable | 36 days ago (2026-01-08 11:30:16 UTC) | 14 | HTML | DuckDB extension for system monitoring & intelligent SQL routing. 25+ functio... |
| 140 | [scalarfs](https://duckdb.org/community_extensions/extensions/scalarfs.html) | [duckdb_scalarfs](https://github.com/teaguesterling/duckdb_scalarfs) | 🟢 Ongoing | 1 - 🔥 Very Active | 6 days ago (2026-02-08 00:13:05 UTC) | 6 | C++ | A collection of simple virtual filesystems for treating scalar values as files. |
| 141 | [scrooge](https://duckdb.org/community_extensions/extensions/scrooge.html) | [Scrooge-McDuck](https://github.com/pdet/Scrooge-McDuck) | ❓ Unknown | 4 - 🟠 Stale | 305 days ago (2025-04-14 11:16:07 UTC) | 152 | C++ | DuckDB extension: scrooge by pdet |
| 142 | [sheetreader](https://duckdb.org/community_extensions/extensions/sheetreader.html) | [sheetreader-duckdb](https://github.com/polydbms/sheetreader-duckdb) | ❓ Unknown | 3 - 🟡 Stable | 65 days ago (2025-12-10 21:40:53 UTC) | 56 | Jupyter Notebook | DuckDB extension: sheetreader by polydbms |
| 143 | [shellfs](https://duckdb.org/community_extensions/extensions/shellfs.html) | [shellfs](https://github.com/Query-farm/shellfs) | 🟢 Ongoing | 2 - ✅ Active | 12 days ago (2026-02-01 08:06:09 UTC) | 93 | C++ | DuckDB extension allowing shell commands to be used for input and output. |
| 144 | [sitemap](https://duckdb.org/community_extensions/extensions/sitemap.html) | [duckdb-sitemap](https://github.com/midwork-finds-jobs/duckdb-sitemap) | 🟢 Ongoing | 2 - ✅ Active | 8 days ago (2026-02-05 15:33:47 UTC) | 1 | C++ | DuckDB extension for parsing XML sitemaps from websites |
| 145 | [sitting_duck](https://duckdb.org/community_extensions/extensions/sitting_duck.html) | [sitting_duck](https://github.com/teaguesterling/sitting_duck) | 🟢 Ongoing | 1 - 🔥 Very Active | 6 days ago (2026-02-07 22:29:26 UTC) | 8 | C | DuckDB extension: sitting_duck by teaguesterling |
| 146 | [snowflake](https://duckdb.org/community_extensions/extensions/snowflake.html) | [duckdb-snowflake](https://github.com/iqea-ai/duckdb-snowflake) | 🟢 Ongoing | 3 - 🟡 Stable | 65 days ago (2025-12-10 21:41:05 UTC) | 40 | C++ | A powerful DuckDB extension that enables seamless querying of Snowflake datab... |
| 147 | [splink_udfs](https://duckdb.org/community_extensions/extensions/splink_udfs.html) | [splink_udfs](https://github.com/moj-analytical-services/splink_udfs) | ❓ Unknown | 1 - 🔥 Very Active | 7 days ago (2026-02-06 11:01:11 UTC) | 17 | C++ | DuckDB extension: splink_udfs by moj-analytical-services |
| 148 | [sshfs](https://duckdb.org/community_extensions/extensions/sshfs.html) | [duckdb-sshfs](https://github.com/midwork-finds-jobs/duckdb-sshfs) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-02-13 18:13:02 UTC) | 5 | C++ | DuckDB sshfs extension - Read and write files through ssh inside DuckDB |
| 149 | [st_read_multi](https://duckdb.org/community_extensions/extensions/st_read_multi.html) | [duckdb-ext-st-read-multi](https://github.com/yutannihilation/duckdb-ext-st-read-multi) | 🟢 Ongoing | 1 - 🔥 Very Active | 4 days ago (2026-02-10 05:49:45 UTC) | 7 | Rust | A DuckDB extension to import multiple geospatial files with `ST_Read_Multi()` |
| 150 | [stochastic](https://duckdb.org/community_extensions/extensions/stochastic.html) | [stochastic](https://github.com/Query-farm/stochastic) | 🟢 Ongoing | 2 - ✅ Active | 12 days ago (2026-02-01 08:06:13 UTC) | 15 | C++ | A DuckDB extension that add comprehensive statistical distribution functions... |
| 151 | [substrait](https://duckdb.org/community_extensions/extensions/substrait.html) | [duckdb-substrait-extension](https://github.com/substrait-io/duckdb-substrait-extension) | ❓ Unknown | 1 - 🔥 Very Active | today (2026-02-12 15:49:24 UTC) | 56 | C++ | DuckDB extension: substrait by substrait-io |
| 152 | [system_stats](https://duckdb.org/community_extensions/extensions/system_stats.html) | [system_stats](https://github.com/dentiny/system_stats) | 🟢 Ongoing | 1 - 🔥 Very Active | 5 days ago (2026-02-08 23:55:14 UTC) | 1 | C++ | DuckDB extension: system_stats by dentiny |
| 153 | [tarfs](https://duckdb.org/community_extensions/extensions/tarfs.html) | [duckdb_tarfs](https://github.com/Maxxen/duckdb_tarfs) | ❓ Unknown | 4 - 🟠 Stale | over a year ago (2024-08-26 11:01:47 UTC) | 11 | C++ | DuckDB extension: tarfs by Maxxen |
| 154 | [tera](https://duckdb.org/community_extensions/extensions/tera.html) | [tera](https://github.com/Query-farm/tera) | 🟢 Ongoing | 2 - ✅ Active | 12 days ago (2026-02-01 08:06:16 UTC) | 8 | C++ | DuckDB extension: tera |
| 155 | [textplot](https://duckdb.org/community_extensions/extensions/textplot.html) | [textplot](https://github.com/Query-farm/textplot) | 🟢 Ongoing | 2 - ✅ Active | 12 days ago (2026-02-01 08:06:20 UTC) | 17 | C++ | A DuckDB community extension that enables text-based data visualization direc... |
| 156 | [title_mapper](https://duckdb.org/community_extensions/extensions/title_mapper.html) | [duckdb-title-mapper](https://github.com/martin-conur/duckdb-title-mapper) | ❓ Unknown | 4 - 🟠 Stale | 124 days ago (2025-10-12 22:54:26 UTC) | 2 | Rust | DuckDB extension: title_mapper by martin-conur |
| 157 | [tributary](https://duckdb.org/community_extensions/extensions/tributary.html) | [tributary](https://github.com/Query-farm/tributary) | 🟢 Ongoing | 2 - ✅ Active | 12 days ago (2026-02-01 08:06:24 UTC) | 53 | C++ | A DuckDB Extension for Kafka |
| 158 | [tsid](https://duckdb.org/community_extensions/extensions/tsid.html) | [tsid](https://github.com/Query-farm/tsid) | 🟢 Ongoing | 2 - ✅ Active | 12 days ago (2026-02-01 08:06:28 UTC) | 5 | C++ | TSID Extension for DuckDB  |
| 159 | [ulid](https://duckdb.org/community_extensions/extensions/ulid.html) | [duckdb_ulid](https://github.com/Maxxen/duckdb_ulid) | ❓ Unknown | 4 - 🟠 Stale | over a year ago (2024-07-09 09:35:50 UTC) | 24 | C++ | DuckDB extension: ulid by Maxxen |
| 160 | [urlpattern](https://duckdb.org/community_extensions/extensions/urlpattern.html) | [duckdb_urlpattern](https://github.com/teaguesterling/duckdb_urlpattern) | ❓ Unknown | 3 - 🟡 Stable | 33 days ago (2026-01-11 21:26:52 UTC) | 2 | C++ | An implementation of URLPattern for DuckDB |
| 161 | [valhalla_routing](https://duckdb.org/community_extensions/extensions/valhalla_routing.html) | [duckdb-valhalla-routing](https://github.com/midwork-finds-jobs/duckdb-valhalla-routing) | 🟢 Ongoing | 2 - ✅ Active | 8 days ago (2026-02-05 15:33:09 UTC) | 2 | Makefile | WIP: Attempt to package valhalla routing engine to duckdb |
| 162 | [warc](https://duckdb.org/community_extensions/extensions/warc.html) | [duckdb_warc](https://github.com/midwork-finds-jobs/duckdb_warc) | ❓ Unknown | 2 - ✅ Active | 8 days ago (2026-02-05 15:33:27 UTC) | 2 | Rust | DuckDB extension for parsing WARC files |
| 163 | [web_archive](https://duckdb.org/community_extensions/extensions/web_archive.html) | [duckdb-web-archive](https://github.com/midwork-finds-jobs/duckdb-web-archive) | 🟢 Ongoing | 2 - ✅ Active | 10 days ago (2026-02-03 08:28:03 UTC) | 14 | C++ | DuckDB extension to fetch pages from Wayback Machine & Common Crawl |
| 164 | [web_search](https://duckdb.org/community_extensions/extensions/web_search.html) | [duckdb-web-search](https://github.com/midwork-finds-jobs/duckdb-web-search) | 🟢 Ongoing | 2 - ✅ Active | 8 days ago (2026-02-05 15:33:01 UTC) | 0 | C++ | Web/HTTP functionality extension by midwork-finds-jobs |
| 165 | [webbed](https://duckdb.org/community_extensions/extensions/webbed.html) | [duckdb_webbed](https://github.com/teaguesterling/duckdb_webbed) | 🟢 Ongoing | 3 - 🟡 Stable | 39 days ago (2026-01-06 04:34:56 UTC) | 41 | C++ | Web/HTTP functionality extension by teaguesterling |
| 166 | [webdavfs](https://duckdb.org/community_extensions/extensions/webdavfs.html) | [duckdb-webdavfs](https://github.com/midwork-finds-jobs/duckdb-webdavfs) | 🟢 Ongoing | 2 - ✅ Active | 8 days ago (2026-02-05 16:02:46 UTC) | 1 | C++ | DuckDB WebDAVfs Extension - WebDAV filesystem support for DuckDB |
| 167 | [webmacro](https://duckdb.org/community_extensions/extensions/webmacro.html) | [webmacro](https://github.com/Query-farm/webmacro) | 🟢 Ongoing | 2 - ✅ Active | 12 days ago (2026-02-01 08:06:31 UTC) | 15 | C++ | DuckDB WebMacro: Share and Load your SQL Macros via gists |
| 168 | [whisper](https://duckdb.org/community_extensions/extensions/whisper.html) | [duckdb-whisper](https://github.com/tobilg/duckdb-whisper) | 🟢 Ongoing | 2 - ✅ Active | 8 days ago (2026-02-05 06:57:05 UTC) | 1 | C++ | Use whisper.cpp within DuckDB to translate / transpile speech to text |
| 169 | [wireduck](https://duckdb.org/community_extensions/extensions/wireduck.html) | [wireduck](https://github.com/hyehudai/wireduck) | ❓ Unknown | 4 - 🟠 Stale | 143 days ago (2025-09-23 21:22:03 UTC) | 47 | C++ | Duckdb extension to read pcap files |
| 170 | [yaml](https://duckdb.org/community_extensions/extensions/yaml.html) | [duckdb_yaml](https://github.com/teaguesterling/duckdb_yaml) | 🟢 Ongoing | 1 - 🔥 Very Active | 6 days ago (2026-02-07 22:12:52 UTC) | 13 | C++ |  A DuckDB to read and work with YAML files in a similar way to JSON files (al... |
| 171 | [yardstick](https://duckdb.org/community_extensions/extensions/yardstick.html) | [yardstick](https://github.com/sidequery/yardstick) | ❓ Unknown | 2 - ✅ Active | 15 days ago (2026-01-29 16:56:26 UTC) | 41 | Rust | An implementation of Measures in SQL as a DuckDB extension |
| 172 | [zipfs](https://duckdb.org/community_extensions/extensions/zipfs.html) | [duckdb-zipfs](https://github.com/isaacbrodsky/duckdb-zipfs) | 🟢 Ongoing | 2 - ✅ Active | 12 days ago (2026-02-01 16:04:36 UTC) | 55 | C++ | DuckDB extension to read files within zip archives. |

</details>
## Appendix: DuckDB Release Information

### Current Release Context

DuckDB follows **semantic versioning** with regular releases. For complete and up-to-date release information, see the official [**DuckDB Release Calendar**](https://duckdb.org/release_calendar.html).

### Release History

| Version | Release Date | Codename | Named After | LTS | Status |
|---------|--------------|----------|-------------|-----|--------|
| **v1.5.0** 📅 | 2026-02-23 | – | – |  | Planned |
| **v1.4.4** | 2026-01-27 | – | – | ✓ | Active |
| **v1.4.3** | 2025-12-09 | – | – | ✓ | Active |
| **v1.4.2** | 2025-11-12 | – | – | ✓ | Active |
| **v1.4.1** | 2025-10-07 | – | – | ✓ | Active |
| **v1.4.0** | 2025-09-16 | Andium | *Andean teal* | ✓ | Active |
| **v1.3.2** | 2025-07-08 | – | – |  | Active |
| **v1.3.1** | 2025-06-16 | – | – |  | Active |
| **v1.3.0** | 2025-05-21 | Ossivalis | *Goldeneye duck* |  | EOL |
| **v1.2.2** | 2025-04-08 | – | – |  | Active |
| **v1.2.1** | 2025-03-05 | – | – |  | Active |
| **v1.2.0** | 2025-02-05 | Histrionicus | *Harlequin duck* |  | EOL |
| **v1.1.3** | 2024-11-04 | – | – |  | Active |
| **v1.1.2** | 2024-10-14 | – | – |  | Active |
| **v1.1.1** | 2024-09-24 | – | – |  | Active |

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
- **📦 GitHub Releases**: [https://github.com/Mjboothaus/duckdb-extensions-analysis/releases](https://github.com/Mjboothaus/duckdb-extensions-analysis/releases)
- **📰 Release Notes**: [duckdb.org/news/](https://duckdb.org/news/)
- **🛠️ Development Roadmap**: [duckdb.org/roadmap.html](https://duckdb.org/roadmap.html)

<p class="fine-print">Data sourced from the official <a href="https://duckdb.org/data/duckdb-releases.csv">DuckDB releases CSV</a>. For the most current information, see the <a href="https://duckdb.org/release_calendar.html">release calendar</a>.</p>
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

<p class="fine-print">Last updated: 2026-02-14</p>
