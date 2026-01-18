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
| **Community Extensions** | 150 |
| **Total Extensions** | 177 |
| **Recently Active** (≤ 30 days) | 57 (32.2%) |
| **Very Active** (≤ 7 days) | 30 (16.9%) |

*Historical trend tracking is planned for future releases to show extension ecosystem growth over time*


---
## Core Extensions

Core extensions maintained by the DuckDB team and distributed via the official extension repository

**Total:** 27 extensions

<details open markdown="1">
<summary>Click to expand/collapse core extensions table</summary>

| # | Extension | Repository | Status | Last Activity | Stars | Language | Description |
|---|-----------|------------|--------|---------------|-------|----------|-------------|
| 1 | [autocomplete](https://duckdb.org/docs/stable/core_extensions/autocomplete.html) | [duckdb/duckdb](https://github.com/duckdb/duckdb/tree/main/extension/autocomplete) | 🟢 Ongoing | 28 days ago (2025-12-20 21:38:19 UTC) | N/A (part of core DuckDB repo) | C++ | Core DuckDB extension: autocomplete |
| 2 | [avro](https://duckdb.org/docs/stable/core_extensions/avro.html) | [duckdb-avro](https://github.com/duckdb/duckdb-avro) | 🟢 Ongoing | 47 days ago (2025-12-01 09:17:47 UTC) | 32 | C++ | Apache Avro format support |
| 3 | [aws](https://duckdb.org/docs/stable/core_extensions/aws.html) | [duckdb-aws](https://github.com/duckdb/duckdb-aws) | 🟢 Ongoing | 107 days ago (2025-10-02 10:50:00 UTC) | 58 | C++ | AWS S3 integration |
| 4 | [azure](https://duckdb.org/docs/stable/core_extensions/azure.html) | [duckdb-azure](https://github.com/duckdb/duckdb-azure) | 🟢 Ongoing | 25 days ago (2025-12-23 11:02:09 UTC) | 70 | C++ | Azure extension for DuckDB |
| 5 | [delta](https://duckdb.org/docs/stable/core_extensions/delta.html) | [duckdb-delta](https://github.com/duckdb/duckdb-delta) | 🟢 Ongoing | 33 days ago (2025-12-15 15:21:29 UTC) | 207 | C++ | DuckDB extension for Delta Lake |
| 6 | [ducklake](https://duckdb.org/docs/stable/core_extensions/ducklake.html) | [duckdb/ducklake](https://github.com/duckdb/ducklake) | 🟢 Ongoing | 39 days ago | N/A (part of core DuckDB repo) | C++ | Delta Lake support via DuckLake (different from delta extension) |
| 7 | [encodings](https://duckdb.org/docs/stable/core_extensions/encodings.html) | [duckdb-encodings](https://github.com/duckdb/duckdb-encodings) | 🟢 Ongoing | 122 days ago (2025-09-17 12:57:45 UTC) | 15 | C++ | Character encoding support |
| 8 | [excel](https://duckdb.org/docs/stable/core_extensions/excel.html) | [duckdb-excel](https://github.com/duckdb/duckdb-excel) | 🟢 Ongoing | 8 days ago (2026-01-09 23:09:10 UTC) | 51 | C++ | Excel extension for DuckDB |
| 9 | [fts](https://duckdb.org/docs/stable/core_extensions/full_text_search.html) | [duckdb-fts](https://github.com/duckdb/duckdb-fts) | 🟢 Ongoing | 123 days ago (2025-09-16 14:12:43 UTC) | 30 | C++ | Full-text search functionality |
| 10 | [httpfs](https://duckdb.org/docs/stable/core_extensions/httpfs/overview.html) | [duckdb-httpfs](https://github.com/duckdb/duckdb-httpfs) | 🟢 Ongoing | 2 days ago (2026-01-15 15:15:20 UTC) | 43 | C++ | HTTP/S3 filesystem support |
| 11 | [iceberg](https://duckdb.org/docs/stable/core_extensions/iceberg/overview.html) | [duckdb-iceberg](https://github.com/duckdb/duckdb-iceberg) | 🟢 Ongoing | 2 days ago (2026-01-15 07:52:40 UTC) | 369 | C++ | Apache Iceberg format support |
| 12 | [icu](https://duckdb.org/docs/stable/core_extensions/icu.html) | [duckdb/duckdb](https://github.com/duckdb/duckdb/tree/main/extension/icu) | 🟢 Ongoing | 10 days ago (2026-01-07 10:49:13 UTC) | N/A (part of core DuckDB repo) | C++ | Core DuckDB extension: icu |
| 13 | [inet](https://duckdb.org/docs/stable/core_extensions/inet.html) | [duckdb-inet](https://github.com/duckdb/duckdb-inet) | 🟢 Ongoing | 58 days ago (2025-11-20 22:54:12 UTC) | 15 | C++ | Internet address data types |
| 14 | [jemalloc](https://duckdb.org/docs/stable/core_extensions/jemalloc.html) | [duckdb/duckdb](https://github.com/duckdb/duckdb/tree/main/extension/jemalloc) | 🟢 Ongoing | 224 days ago (2025-06-07 09:38:02 UTC) | N/A (part of core DuckDB repo) | C++ | Core DuckDB extension: jemalloc |
| 15 | [json](https://duckdb.org/docs/stable/data/json/overview.html) | [duckdb/duckdb](https://github.com/duckdb/duckdb/tree/main/extension/json) | 🟢 Ongoing | 10 days ago (2026-01-07 20:57:11 UTC) | N/A (part of core DuckDB repo) | C++ | Core DuckDB extension: json |
| 16 | [motherduck](https://duckdb.org/docs/stable/core_extensions/motherduck.html) | [duckdb/duckdb](https://github.com/duckdb/duckdb) *(Third Party - Closed source - maintained by MotherDuck Inc.)* | 🟢 Ongoing | 39 days ago | N/A (part of core DuckDB repo) | C++ | Core DuckDB extension: motherduck |
| 17 | [mysql](https://duckdb.org/docs/stable/core_extensions/mysql.html) | [duckdb-mysql](https://github.com/duckdb/duckdb-mysql) | 🟢 Ongoing | today (2026-01-18 00:34:22 UTC) | 86 | C++ | MySQL database connectivity |
| 18 | [parquet](https://duckdb.org/docs/stable/data/parquet/overview.html) | [duckdb/duckdb](https://github.com/duckdb/duckdb/tree/main/extension/parquet) | 🟢 Ongoing | 10 days ago (2026-01-07 10:48:16 UTC) | N/A (part of core DuckDB repo) | C++ | Core DuckDB extension: parquet |
| 19 | [postgres](https://duckdb.org/docs/stable/core_extensions/postgres.html) | [duckdb-postgres](https://github.com/duckdb/duckdb-postgres) | 🟢 Ongoing | 51 days ago (2025-11-27 14:55:29 UTC) | 337 | C++ | PostgreSQL database connectivity |
| 20 | [spatial](https://duckdb.org/docs/stable/core_extensions/spatial/overview.html) | [duckdb-spatial](https://github.com/duckdb/duckdb-spatial) | 🟢 Ongoing | today (2026-01-17 14:44:29 UTC) | 654 | C++ | Geospatial data types and functions |
| 21 | [sqlite](https://duckdb.org/docs/stable/core_extensions/sqlite.html) | [duckdb-sqlite](https://github.com/duckdb/duckdb-sqlite) | 🟢 Ongoing | 111 days ago (2025-09-28 07:21:39 UTC) | 260 | C++ | DuckDB extension to read and write to SQLite databases |
| 22 | [tpcds](https://duckdb.org/docs/stable/core_extensions/tpcds.html) | [duckdb/duckdb](https://github.com/duckdb/duckdb/tree/main/extension/tpcds) | 🟢 Ongoing | 10 days ago (2026-01-07 10:48:16 UTC) | N/A (part of core DuckDB repo) | C++ | Core DuckDB extension: tpcds |
| 23 | [tpch](https://duckdb.org/docs/stable/core_extensions/tpch.html) | [duckdb/duckdb](https://github.com/duckdb/duckdb/tree/main/extension/tpch) | 🟢 Ongoing | 17 days ago (2025-12-31 13:09:15 UTC) | N/A (part of core DuckDB repo) | C++ | Core DuckDB extension: tpch |
| 24 | [ui](https://duckdb.org/docs/stable/core_extensions/ui.html) | [duckdb-ui](https://github.com/duckdb/duckdb-ui) | 🟢 Ongoing | 3 days ago (2026-01-14 10:58:06 UTC) | 402 | C++ | Browser-based user interface for DuckDB |
| 25 | [unity_catalog](https://duckdb.org/docs/stable/core_extensions/unity_catalog.html) | [unity_catalog](https://github.com/duckdb/unity_catalog) | 🟢 Ongoing | 2 days ago (2026-01-15 10:27:04 UTC) | 95 | C++ | Proof-of-concept extension combining the delta extension with Unity Catalog |
| 26 | [vortex](https://duckdb.org/docs/stable/core_extensions/vortex.html) | [duckdb/duckdb](https://github.com/duckdb/duckdb) *(Third Party - Closed source - third-party extension)* | 🟢 Ongoing | 39 days ago | N/A (part of core DuckDB repo) | C++ | Core DuckDB extension: vortex |
| 27 | [vss](https://duckdb.org/docs/stable/core_extensions/vss.html) | [duckdb-vss](https://github.com/duckdb/duckdb-vss) | 🟢 Ongoing | 3 days ago (2026-01-14 19:27:25 UTC) | 230 | C++ | Vector similarity search |

</details>

---
---
## Community Extensions

Third-party extensions maintained by the community


**Total:** 150 extensions | 🔥 Very Active (≤7d): 30 | ✅ Active (≤30d): 27 | 🟡 Stable (≤90d): 67 | 🟠 Stale (>90d): 26

<details open markdown="1">
<summary>Click to expand/collapse community extensions table</summary>

| # | Extension | Repository | Status | Activity | Last Activity | Stars | Language | Description |
|---|-----------|------------|--------|----------|---------------|-------|----------|-------------|
| 1 | [a5](https://duckdb.org/community_extensions/extensions/a5.html) | [a5](https://github.com/Query-farm/a5) | 🟢 Ongoing | 🟡 Stable | 44 days ago (2025-12-04 16:09:50 UTC) | 10 | C++ | A5 Geospatial Extension for DuckDB |
| 2 | [acp](https://duckdb.org/community_extensions/extensions/acp.html) | [duckdb-acp](https://github.com/sidequery/duckdb-acp) | 🟢 Ongoing | 🟡 Stable | 38 days ago (2025-12-11 03:36:46 UTC) | 32 | Rust | Use Claude Code & other AI agents from inside DuckDB via extension |
| 3 | [adbc_scanner](https://duckdb.org/community_extensions/extensions/adbc_scanner.html) | [adbc_scanner](https://github.com/Query-farm/adbc_scanner) | 🟢 Ongoing | 🟡 Stable | 35 days ago (2025-12-14 02:45:27 UTC) | 7 | C++ | A DuckDB ADBC Scanner Extension - adds support for using ADBC drivers with Du... |
| 4 | [airport](https://duckdb.org/community_extensions/extensions/airport.html) | [airport](https://github.com/Query-farm/airport) | 🟢 Ongoing | 🟡 Stable | 44 days ago (2025-12-04 20:21:07 UTC) | 318 | C++ | The Airport extension for DuckDB, enables the use of Arrow Flight with DuckDB |
| 5 | [anndata](https://duckdb.org/community_extensions/extensions/anndata.html) | [anndata-duckdb-extension](https://github.com/honicky/anndata-duckdb-extension) | 🟢 Ongoing | ✅ Active | 18 days ago (2025-12-31 00:53:17 UTC) | 0 | C++ | Attach and AnnData file in duckdb and query it with SQL.  Perform SQL over gr... |
| 6 | [anofox_forecast](https://duckdb.org/community_extensions/extensions/anofox_forecast.html) | [anofox-forecast](https://github.com/DataZooDE/anofox-forecast) | 🟢 Ongoing | 🔥 Very Active | today (2026-01-17 23:40:12 UTC) | 23 | Rust | Statistical timeseries forecasting in DuckDB |
| 7 | [anofox_statistics](https://duckdb.org/community_extensions/extensions/anofox_statistics.html) | [anofox-statistics](https://github.com/DataZooDE/anofox-statistics) | 🟢 Ongoing | 🔥 Very Active | today (2026-01-16 20:57:46 UTC) | 6 | Rust | A DuckDB extension for statistical regression analysis, providing OLS, Ridge,... |
| 8 | [anofox_tabular](https://duckdb.org/community_extensions/extensions/anofox_tabular.html) | [anofox-tabular](https://github.com/DataZooDE/anofox-tabular) | ❓ Unknown | 🔥 Very Active | today (2026-01-16 11:47:54 UTC) | 8 | C++ | A duckdb extension which combines data quality and data preparation tools for... |
| 9 | [arrow](https://duckdb.org/community_extensions/extensions/arrow.html) | [duckdb-extension-alias](https://github.com/duckdb/duckdb-extension-alias) | ❓ Unknown | 🟠 Stale | 103 days ago (2025-10-06 09:07:38 UTC) | 4 | C | DuckDB extension: arrow |
| 10 | [bigquery](https://duckdb.org/community_extensions/extensions/bigquery.html) | [duckdb-bigquery](https://github.com/hafenkran/duckdb-bigquery) | 🟢 Ongoing | 🔥 Very Active | 6 days ago (2026-01-11 18:36:32 UTC) | 149 | C++ | Integrates DuckDB with Google BigQuery, allowing direct querying and manageme... |
| 11 | [bitfilters](https://duckdb.org/community_extensions/extensions/bitfilters.html) | [bitfilters](https://github.com/Query-farm/bitfilters) | 🟢 Ongoing | 🟡 Stable | 44 days ago (2025-12-04 16:09:52 UTC) | 5 | C++ | A high-performance DuckDB extension providing probabilistic data structures f... |
| 12 | [blockduck](https://duckdb.org/community_extensions/extensions/blockduck.html) | [BlockDuck](https://github.com/luohaha/BlockDuck) | 🟢 Ongoing | 🟠 Stale | 101 days ago (2025-10-08 16:19:04 UTC) | 10 | C++ | Live SQL Queries on Blockchain |
| 13 | [boilstream](https://duckdb.org/community_extensions/extensions/boilstream.html) | [boilstream-extension](https://github.com/dforsber/boilstream-extension) | 🟢 Ongoing | ✅ Active | 11 days ago (2026-01-06 18:06:51 UTC) | 5 | C++ | Secure Remote Secrets Storage for DuckDB |
| 14 | [bvh2sql](https://duckdb.org/community_extensions/extensions/bvh2sql.html) | [bvh2sql](https://github.com/nkwork9999/bvh2sql) | 🟢 Ongoing | 🟡 Stable | 76 days ago (2025-11-02 18:17:05 UTC) | 0 | Makefile | SQL-related extension by nkwork9999 |
| 15 | [cache_httpfs](https://duckdb.org/community_extensions/extensions/cache_httpfs.html) | [duck-read-cache-fs](https://github.com/dentiny/duck-read-cache-fs) | 🟢 Ongoing | 🔥 Very Active | 3 days ago (2026-01-14 12:59:08 UTC) | 125 | C++ | This repository is made as read-only filesystem for remote access. |
| 16 | [capi_quack](https://duckdb.org/community_extensions/extensions/capi_quack.html) | [extension-template-c](https://github.com/duckdb/extension-template-c) | ❓ Unknown | 🟡 Stable | 32 days ago (2025-12-16 13:25:38 UTC) | 27 | C | (Experimental) C/C++ template for DuckDB extensions based on the C API |
| 17 | [cassandra](https://duckdb.org/community_extensions/extensions/cassandra.html) | [duckdb-cassandra](https://github.com/dioptre/duckdb-cassandra) | 🟢 Ongoing | 🟡 Stable | 89 days ago (2025-10-20 19:15:10 UTC) | 0 | C++ | DuckDB Connector for Cassandra |
| 18 | [chaos](https://duckdb.org/community_extensions/extensions/chaos.html) | [duckdb-chaos](https://github.com/taniabogatsch/duckdb-chaos) | 🟢 Ongoing | 🟠 Stale | 120 days ago (2025-09-19 11:42:23 UTC) | 0 | C++ | DuckDB extension: chaos by taniabogatsch |
| 19 | [chsql](https://duckdb.org/community_extensions/extensions/chsql.html) | [clickhouse-sql](https://github.com/Query-farm/clickhouse-sql) | ❓ Unknown | 🟠 Stale | 116 days ago (2025-09-23 19:24:33 UTC) | 87 | C++ | DuckDB Community Extension implementing ClickHouse SQL Dialect macros and Cus... |
| 20 | [chsql_native](https://duckdb.org/community_extensions/extensions/chsql_native.html) | [clickhouse-native](https://github.com/Query-farm/clickhouse-native) | ❓ Unknown | 🟠 Stale | 116 days ago (2025-09-23 19:24:31 UTC) | 17 | Rust | Experimental ClickHouse Native Client and Native file reader Extension for Du... |
| 21 | [cloudfront](https://duckdb.org/community_extensions/extensions/cloudfront.html) | [duckdb-cloudfront](https://github.com/midwork-finds-jobs/duckdb-cloudfront) | 🟢 Ongoing | 🟡 Stable | 44 days ago (2025-12-04 16:09:56 UTC) | 0 | C++ | DuckDB module which provides custom authentication methods on top of httpfs m... |
| 22 | [cronjob](https://duckdb.org/community_extensions/extensions/cronjob.html) | [cronjob](https://github.com/Query-farm/cronjob) | 🟢 Ongoing | 🟡 Stable | 44 days ago (2025-12-04 23:24:46 UTC) | 45 | C++ | DuckDB CronJob Extension |
| 23 | [crypto](https://duckdb.org/community_extensions/extensions/crypto.html) | [crypto](https://github.com/Query-farm/crypto) | 🟢 Ongoing | 🟡 Stable | 44 days ago (2025-12-04 16:09:56 UTC) | 26 | C++ | DuckDB Extension for cryptographic hash functions and HMAC |
| 24 | [curl_httpfs](https://duckdb.org/community_extensions/extensions/curl_httpfs.html) | [duckdb-curl-filesystem](https://github.com/dentiny/duckdb-curl-filesystem) | 🟢 Ongoing | 🟡 Stable | 39 days ago (2025-12-09 19:31:30 UTC) | 8 | C++ | Filesystem built upon libcurl. |
| 25 | [cwiqduck](https://duckdb.org/community_extensions/extensions/cwiqduck.html) | [cwiqduck](https://github.com/cwiq-os/cwiqduck) | 🟢 Ongoing | 🟡 Stable | 40 days ago (2025-12-09 02:09:40 UTC) | 2 | C++ | DuckDB extensions for CWIQ |
| 26 | [dash](https://duckdb.org/community_extensions/extensions/dash.html) | [dash](https://github.com/gropaul/dash) | 🟢 Ongoing | 🟡 Stable | 39 days ago (2025-12-09 22:02:22 UTC) | 32 | C++ | DuckDB Extension featuring a Query Builder GUI and Dashboarding features |
| 27 | [datasketches](https://duckdb.org/community_extensions/extensions/datasketches.html) | [datasketches](https://github.com/Query-farm/datasketches) | 🟢 Ongoing | 🟡 Stable | 36 days ago (2025-12-12 16:13:17 UTC) | 39 | C++ | Integrates DuckDB with the high-performance Apache DataSketches library. This... |
| 28 | [dns](https://duckdb.org/community_extensions/extensions/dns.html) | [duckdb-dns](https://github.com/tobilg/duckdb-dns) | 🟢 Ongoing | 🟡 Stable | 38 days ago (2025-12-10 17:12:12 UTC) | 14 | Rust | DNS (Reverse) Lookup Extension for DuckDB |
| 29 | [dplyr](https://duckdb.org/community_extensions/extensions/dplyr.html) | [libdplyr](https://github.com/mrchypark/libdplyr) | 🟢 Ongoing | ✅ Active | 9 days ago (2026-01-08 14:38:26 UTC) | 5 | Rust | DuckDB extension: dplyr by mrchypark |
| 30 | [duck_block_utils](https://duckdb.org/community_extensions/extensions/duck_block_utils.html) | [duckdb_duck_block_utils](https://github.com/teaguesterling/duckdb_duck_block_utils) | 🟢 Ongoing | 🔥 Very Active | 6 days ago (2026-01-11 19:30:48 UTC) | 0 | C++ | A collection of utility functions to work with doc block-style structures and... |
| 31 | [duck_delta_share](https://duckdb.org/community_extensions/extensions/duck_delta_share.html) | [duck_delta_share](https://github.com/cwiq-os/duck_delta_share) | 🟢 Ongoing | 🔥 Very Active | 2 days ago (2026-01-16 05:03:15 UTC) | 1 | C++ | DuckDB extension for enabling Delta Sharing client capabilities.  |
| 32 | [duck_hunt](https://duckdb.org/community_extensions/extensions/duck_hunt.html) | [duck_hunt](https://github.com/teaguesterling/duck_hunt) | 🟢 Ongoing | 🔥 Very Active | 2 days ago (2026-01-15 15:16:22 UTC) | 3 | C++ | Tools for working with unit test suite results |
| 33 | [duck_tails](https://duckdb.org/community_extensions/extensions/duck_tails.html) | [duck_tails](https://github.com/teaguesterling/duck_tails) | 🟢 Ongoing | 🔥 Very Active | 6 days ago (2026-01-11 19:27:46 UTC) | 12 | C++ | A DuckDB extension for exploring and reading git history. |
| 34 | [duckdb_mcp](https://duckdb.org/community_extensions/extensions/duckdb_mcp.html) | [duckdb_mcp](https://github.com/teaguesterling/duckdb_mcp) | 🟢 Ongoing | 🔥 Very Active | today (2026-01-17 00:07:28 UTC) | 23 | C++ | A simple MCP server extension for DuckDB |
| 35 | [duckgl](https://duckdb.org/community_extensions/extensions/duckgl.html) | [duckgl](https://github.com/nkwork9999/duckgl) | 🟢 Ongoing | ✅ Active | 22 days ago (2025-12-27 04:09:47 UTC) | 1 | C++ | DuckDB extension: duckgl by nkwork9999 |
| 36 | [duckherder](https://duckdb.org/community_extensions/extensions/duckherder.html) | [duckdb-distributed-execution](https://github.com/dentiny/duckdb-distributed-execution) | 🟢 Ongoing | ✅ Active | 30 days ago (2025-12-18 11:12:23 UTC) | 42 | C++ | Distributed execution for duckdb queries. |
| 37 | [duckpgq](https://duckdb.org/community_extensions/extensions/duckpgq.html) | [duckpgq-extension](https://github.com/cwida/duckpgq-extension) | 🟢 Ongoing | 🟡 Stable | 32 days ago (2025-12-16 09:31:39 UTC) | 346 | C++ | DuckDB extension that adds support for SQL/PGQ and graph algorithms |
| 38 | [eeagrid](https://duckdb.org/community_extensions/extensions/eeagrid.html) | [duckdb-eeagrid](https://github.com/ahuarte47/duckdb-eeagrid) | 🟢 Ongoing | 🟡 Stable | 38 days ago (2025-12-10 17:17:32 UTC) | 0 | C++ | Functions for transforming XY coordinates to and from the EEA Reference Grid... |
| 39 | [encoding](https://duckdb.org/community_extensions/extensions/encoding.html) | [duckdb-encoding](https://github.com/onnimonni/duckdb-encoding) | ❓ Unknown | 🟠 Stale | 92 days ago (2025-10-17 06:53:16 UTC) | 2 | Rust | DuckDB extension: encoding by onnimonni |
| 40 | [erpl_web](https://duckdb.org/community_extensions/extensions/erpl_web.html) | [erpl-web](https://github.com/DataZooDE/erpl-web) | 🟢 Ongoing | ✅ Active | 23 days ago (2025-12-25 13:47:47 UTC) | 23 | C++ | ERPL is a DuckDB extension to connect to API based ecosystems via standard in... |
| 41 | [evalexpr_rhai](https://duckdb.org/community_extensions/extensions/evalexpr_rhai.html) | [evalexpr_rhai](https://github.com/Query-farm/evalexpr_rhai) | 🟢 Ongoing | 🟡 Stable | 44 days ago (2025-12-04 18:56:32 UTC) | 22 | C++ | A DuckDB extension to evaluate the Rhai scripting language as part of SQL. |
| 42 | [faiss](https://duckdb.org/community_extensions/extensions/faiss.html) | [duckdb-faiss-ext](https://github.com/duckdb-faiss-ext/duckdb-faiss-ext) | 🟢 Ongoing | 🟡 Stable | 40 days ago (2025-12-09 01:30:08 UTC) | 29 | Go | DuckDB wrapper for FAISS - Experimental |
| 43 | [fakeit](https://duckdb.org/community_extensions/extensions/fakeit.html) | [duckdb-fakeit](https://github.com/tobilg/duckdb-fakeit) | 🟢 Ongoing | 🟡 Stable | 38 days ago (2025-12-10 17:31:48 UTC) | 5 | Rust | DuckDB extension: fakeit by tobilg |
| 44 | [file_dialog](https://duckdb.org/community_extensions/extensions/file_dialog.html) | [duckdb-ext-file-dialog](https://github.com/yutannihilation/duckdb-ext-file-dialog) | 🟢 Ongoing | 🔥 Very Active | 5 days ago (2026-01-12 14:33:29 UTC) | 15 | Rust | A DuckDB extension to choose file interactively using native file open dialogs |
| 45 | [fit](https://duckdb.org/community_extensions/extensions/fit.html) | [duckdb-fit-extension](https://github.com/antoriche/duckdb-fit-extension) | 🟢 Ongoing | 🟡 Stable | 33 days ago (2025-12-15 19:16:40 UTC) | 1 | C++ | DuckDB extension: fit by antoriche |
| 46 | [fivetran](https://duckdb.org/community_extensions/extensions/fivetran.html) | [fivetran](https://github.com/lnkuiper/fivetran) | 🟢 Ongoing | ✅ Active | 9 days ago (2026-01-08 14:26:11 UTC) | 0 | C++ | DuckDB extension: fivetran by lnkuiper |
| 47 | [flock](https://duckdb.org/community_extensions/extensions/flock.html) | [flock](https://github.com/dais-polymtl/flock) | 🟢 Ongoing | 🟡 Stable | 42 days ago (2025-12-06 23:04:48 UTC) | 288 | C++ | Flock: multimodal querying for DuckDB |
| 48 | [func_apply](https://duckdb.org/community_extensions/extensions/func_apply.html) | [duckdb_func_apply](https://github.com/teaguesterling/duckdb_func_apply) | 🟢 Ongoing | 🔥 Very Active | 6 days ago (2026-01-11 19:20:07 UTC) | 3 | C++ | An exension to allow dynamic function application |
| 49 | [fuzzycomplete](https://duckdb.org/community_extensions/extensions/fuzzycomplete.html) | [fuzzycomplete](https://github.com/Query-farm/fuzzycomplete) | 🟢 Ongoing | 🟡 Stable | 44 days ago (2025-12-04 16:10:01 UTC) | 24 | C++ | DuckDB Extension for fuzzy string matching based autocompletion |
| 50 | [gaggle](https://duckdb.org/community_extensions/extensions/gaggle.html) | [gaggle](https://github.com/CogitatorTech/gaggle) | 🟢 Ongoing | 🟡 Stable | 37 days ago (2025-12-11 17:03:13 UTC) | 14 | Rust | A DuckDB extension for working with Kaggle datasets |
| 51 | [gcs](https://duckdb.org/community_extensions/extensions/gcs.html) | [duckdb-gcs](https://github.com/northpolesec/duckdb-gcs) | 🟢 Ongoing | 🟡 Stable | 46 days ago (2025-12-02 12:17:16 UTC) | 9 | C++ | A GCS-native extension for DuckDB |
| 52 | [geography](https://duckdb.org/community_extensions/extensions/geography.html) | [duckdb-geography](https://github.com/paleolimbot/duckdb-geography) | 🟢 Ongoing | 🟠 Stale | 107 days ago (2025-10-02 11:09:38 UTC) | 35 | C++ | Geospatial data extension by paleolimbot |
| 53 | [geotiff](https://duckdb.org/community_extensions/extensions/geotiff.html) | [duckdb-geotiff](https://github.com/babaknaimi/duckdb-geotiff) | ❓ Unknown | 🟠 Stale | 151 days ago (2025-08-20 05:12:15 UTC) | 2 | C++ | Duckdb extension to read GeoTiffs directly with duckdb database |
| 54 | [gsheets](https://duckdb.org/community_extensions/extensions/gsheets.html) | [duckdb_gsheets](https://github.com/evidence-dev/duckdb_gsheets) | 🟢 Ongoing | ✅ Active | 8 days ago (2026-01-09 17:58:19 UTC) | 329 | C++ | DuckDB extension to read and write Google Sheets using SQL |
| 55 | [h3](https://duckdb.org/community_extensions/extensions/h3.html) | [h3-duckdb](https://github.com/isaacbrodsky/h3-duckdb) | 🟢 Ongoing | ✅ Active | 29 days ago (2025-12-19 21:58:47 UTC) | 240 | C++ | Bindings for H3 to DuckDB |
| 56 | [hashfuncs](https://duckdb.org/community_extensions/extensions/hashfuncs.html) | [hashfuncs](https://github.com/Query-farm/hashfuncs) | 🟢 Ongoing | 🟡 Stable | 44 days ago (2025-12-04 16:10:01 UTC) | 10 | C++ | A DuckDB extension that supplies non-cryptographic hash functions. |
| 57 | [hdf5](https://duckdb.org/community_extensions/extensions/hdf5.html) | [duckdb-hdf5](https://github.com/Berrysoft/duckdb-hdf5) | ❓ Unknown | 🟠 Stale | 94 days ago (2025-10-15 17:27:39 UTC) | 12 | Rust | HDF5 plugin for duckdb |
| 58 | [highs](https://duckdb.org/community_extensions/extensions/highs.html) | [HiGHS-duckdb](https://github.com/fhk/HiGHS-duckdb) | ❓ Unknown | 🟠 Stale | 154 days ago (2025-08-16 06:41:18 UTC) | 1 | C++ | Run the solver in the database! |
| 59 | [hostfs](https://duckdb.org/community_extensions/extensions/hostfs.html) | [hostFS](https://github.com/gropaul/hostFS) | ❓ Unknown | 🟠 Stale | 108 days ago (2025-10-01 21:02:13 UTC) | 29 | C++ | DuckDB extension: hostfs by gropaul |
| 60 | [html_query](https://duckdb.org/community_extensions/extensions/html_query.html) | [duckdb_html_query](https://github.com/midwork-finds-jobs/duckdb_html_query) | 🟢 Ongoing | ✅ Active | 9 days ago (2026-01-08 19:22:14 UTC) | 1 | Rust | Filter HTML inside duckdb |
| 61 | [html_readability](https://duckdb.org/community_extensions/extensions/html_readability.html) | [duckdb-html-readability](https://github.com/midwork-finds-jobs/duckdb-html-readability) | 🟢 Ongoing | 🔥 Very Active | 2 days ago (2026-01-16 04:48:03 UTC) | 0 | Rust | DuckDB extension to parse html to readable text |
| 62 | [http_client](https://duckdb.org/community_extensions/extensions/http_client.html) | [httpclient](https://github.com/Query-farm/httpclient) | 🟢 Ongoing | 🟡 Stable | 44 days ago (2025-12-04 16:10:02 UTC) | 77 | C++ | DuckDB HTTP GET/POST Client in a Community Extension |
| 63 | [http_request](https://duckdb.org/community_extensions/extensions/http_request.html) | [duckdb_http_request](https://github.com/midwork-finds-jobs/duckdb_http_request) | 🟢 Ongoing | 🔥 Very Active | 3 days ago (2026-01-15 05:09:39 UTC) | 0 | C++ | Uses the native duckdb httputil to make extra requests in SELECT |
| 64 | [httpd_log](https://duckdb.org/community_extensions/extensions/httpd_log.html) | [duckdb-httpd-log](https://github.com/saygox/duckdb-httpd-log) | 🟢 Ongoing | 🔥 Very Active | 5 days ago (2026-01-12 06:14:58 UTC) | 0 | C++ | duckdb extension |
| 65 | [httpserver](https://duckdb.org/community_extensions/extensions/httpserver.html) | [httpserver](https://github.com/Query-farm/httpserver) | 🟢 Ongoing | 🟡 Stable | 44 days ago (2025-12-04 18:26:31 UTC) | 263 | C++ | DuckDB HTTP API Server and Query Interface in a  Community Extension |
| 66 | [infera](https://duckdb.org/community_extensions/extensions/infera.html) | [infera](https://github.com/CogitatorTech/infera) | 🟢 Ongoing | 🟡 Stable | 37 days ago (2025-12-11 07:11:16 UTC) | 119 | Rust | A DuckDB extension for in-database inference |
| 67 | [inflector](https://duckdb.org/community_extensions/extensions/inflector.html) | [inflector](https://github.com/Query-farm/inflector) | 🟢 Ongoing | 🟡 Stable | 38 days ago (2025-12-10 16:06:48 UTC) | 5 | C++ | Powerful string case transformation and inflection capabilities directly to y... |
| 68 | [ion](https://duckdb.org/community_extensions/extensions/ion.html) | [duckdb-ion](https://github.com/kestra-io/duckdb-ion) | 🟢 Ongoing | 🔥 Very Active | 5 days ago (2026-01-12 18:20:02 UTC) | 0 | C++ | AWS Ion extension for DuckDB |
| 69 | [json_schema](https://duckdb.org/community_extensions/extensions/json_schema.html) | [json_schema](https://github.com/Query-farm/json_schema) | 🟢 Ongoing | 🟡 Stable | 44 days ago (2025-12-04 19:14:15 UTC) | 2 | Python | A DuckDB extension that bring support for validating JSON data using JSON sch... |
| 70 | [jsonata](https://duckdb.org/community_extensions/extensions/jsonata.html) | [jsonata](https://github.com/Query-farm/jsonata) | 🟢 Ongoing | 🟡 Stable | 36 days ago (2025-12-12 13:21:15 UTC) | 2 | C++ | The JSONata extension for DuckDB enables expressive, JSON-focused querying an... |
| 71 | [jwt](https://duckdb.org/community_extensions/extensions/jwt.html) | [duckdb_jwt](https://github.com/GalvinGao/duckdb_jwt) | ❓ Unknown | 🟠 Stale | 193 days ago (2025-07-09 00:13:56 UTC) | 0 | C++ | DuckDB extension: jwt by GalvinGao |
| 72 | [lance](https://duckdb.org/community_extensions/extensions/lance.html) | [lance-duckdb](https://github.com/lance-format/lance-duckdb) | 🟢 Ongoing | ✅ Active | 10 days ago (2026-01-07 15:19:52 UTC) | 52 | C++ | The lance extensions for DuckDB enable reading and writing of lance tables. |
| 73 | [lindel](https://duckdb.org/community_extensions/extensions/lindel.html) | [lindel](https://github.com/Query-farm/lindel) | 🟢 Ongoing | 🟡 Stable | 44 days ago (2025-12-04 16:10:08 UTC) | 58 | C++ | DuckDB Extension Linearization/Delinearization, Z-Order, Hilbert and Morton C... |
| 74 | [llm](https://duckdb.org/community_extensions/extensions/llm.html) | [duckdb-llm](https://github.com/midwork-finds-jobs/duckdb-llm) | 🟢 Ongoing | ✅ Active | 23 days ago (2025-12-25 05:35:42 UTC) | 1 | C++ | DuckDB extension: llm by midwork-finds-jobs |
| 75 | [lsh](https://duckdb.org/community_extensions/extensions/lsh.html) | [lsh](https://github.com/princeton-ddss/lsh) | 🟢 Ongoing | 🟡 Stable | 33 days ago (2025-12-15 18:21:36 UTC) | 10 | Rust | DuckDB community extension for locality-sensitive hashing (LSH) |
| 76 | [lua](https://duckdb.org/community_extensions/extensions/lua.html) | [duckdb-lua](https://github.com/isaacbrodsky/duckdb-lua) | 🟢 Ongoing | 🟡 Stable | 39 days ago (2025-12-09 19:09:42 UTC) | 9 | C++ | DuckDB extension to evaluate Lua expressions. |
| 77 | [magic](https://duckdb.org/community_extensions/extensions/magic.html) | [duckdb_magic](https://github.com/carlopi/duckdb_magic) | 🟢 Ongoing | 🟠 Stale | 112 days ago (2025-09-27 18:50:32 UTC) | 7 | C++ | Auto-detect file types via `libmagic` (`file` utility) |
| 78 | [marisa](https://duckdb.org/community_extensions/extensions/marisa.html) | [marisa](https://github.com/Query-farm/marisa) | 🟢 Ongoing | 🟡 Stable | 44 days ago (2025-12-04 20:29:42 UTC) | 6 | C++ | The Marisa extension by Query.Farm integrates the fast, space-efficient MARIS... |
| 79 | [markdown](https://duckdb.org/community_extensions/extensions/markdown.html) | [duckdb_markdown](https://github.com/teaguesterling/duckdb_markdown) | 🟢 Ongoing | 🔥 Very Active | 3 days ago (2026-01-15 00:50:07 UTC) | 13 | C++ | Heirarchical markdown parsing for DuckDB |
| 80 | [minijinja](https://duckdb.org/community_extensions/extensions/minijinja.html) | [minijinja](https://github.com/Query-farm/minijinja) | 🟢 Ongoing | ✅ Active | 26 days ago (2025-12-22 14:59:08 UTC) | 5 | C++ | DuckDB extension: minijinja |
| 81 | [miniplot](https://duckdb.org/community_extensions/extensions/miniplot.html) | [miniplot](https://github.com/nkwork9999/miniplot) | 🟢 Ongoing | 🟡 Stable | 64 days ago (2025-11-15 02:42:43 UTC) | 15 | C++ | DuckDB extension: miniplot by nkwork9999 |
| 82 | [mlpack](https://duckdb.org/community_extensions/extensions/mlpack.html) | [duckdb-mlpack](https://github.com/eddelbuettel/duckdb-mlpack) | 🟢 Ongoing | ✅ Active | 8 days ago (2026-01-09 21:49:18 UTC) | 17 | C++ | Bringing mlpack to duckdb |
| 83 | [mongo](https://duckdb.org/community_extensions/extensions/mongo.html) | [duckdb-mongo](https://github.com/stephaniewang526/duckdb-mongo) | 🟢 Ongoing | 🔥 Very Active | today (2026-01-16 21:43:10 UTC) | 31 | C++ | Integrates DuckDB with MongoDB, enabling direct SQL queries over MongoDB coll... |
| 84 | [mooncake](https://duckdb.org/community_extensions/extensions/mooncake.html) | [duckdb_mooncake](https://github.com/Mooncake-Labs/duckdb_mooncake) | 🟢 Ongoing | 🟡 Stable | 83 days ago (2025-10-26 07:13:05 UTC) | 7 | C++ | Read Iceberg tables written by moonlink in real time |
| 85 | [msolap](https://duckdb.org/community_extensions/extensions/msolap.html) | [duckdb-msolap-extension](https://github.com/Hugoberry/duckdb-msolap-extension) | 🟢 Ongoing | 🟠 Stale | 115 days ago (2025-09-24 16:33:46 UTC) | 12 | C++ | DuckDB extension: msolap by Hugoberry |
| 86 | [nanoarrow](https://duckdb.org/community_extensions/extensions/nanoarrow.html) | [duckdb-nanoarrow](https://github.com/paleolimbot/duckdb-nanoarrow) | ❓ Unknown | ✅ Active | 12 days ago (2026-01-05 20:26:36 UTC) | 65 | C++ | DuckDB extension: nanoarrow by paleolimbot |
| 87 | [nanodbc](https://duckdb.org/community_extensions/extensions/nanodbc.html) | [duckdb-nanodbc-extension](https://github.com/Hugoberry/duckdb-nanodbc-extension) | 🟢 Ongoing | 🟡 Stable | 46 days ago (2025-12-02 16:24:39 UTC) | 50 | C++ | Database connectivity extension by Hugoberry |
| 88 | [nats_js](https://duckdb.org/community_extensions/extensions/nats_js.html) | [duckdb-nats-jetstream](https://github.com/brannn/duckdb-nats-jetstream) | 🟢 Ongoing | 🟡 Stable | 64 days ago (2025-11-14 07:24:21 UTC) | 15 | C++ | DuckDB extension for querying NATS JetStream message streams with SQL |
| 89 | [netquack](https://duckdb.org/community_extensions/extensions/netquack.html) | [duckdb-netquack](https://github.com/hatamiarash7/duckdb-netquack) | ❓ Unknown | ✅ Active | 9 days ago (2026-01-08 08:14:54 UTC) | 31 | C++ | DuckDB extension for parsing, extracting, and analyzing domains, URIs, and pa... |
| 90 | [observefs](https://duckdb.org/community_extensions/extensions/observefs.html) | [duckdb-filesystem-observability](https://github.com/dentiny/duckdb-filesystem-observability) | 🟢 Ongoing | 🔥 Very Active | 5 days ago (2026-01-12 11:21:05 UTC) | 9 | C++ | Provides observability for duckdb filesystem. |
| 91 | [ofquack](https://duckdb.org/community_extensions/extensions/ofquack.html) | [ofquack](https://github.com/krokozyab/ofquack) | ❓ Unknown | 🟠 Stale | 270 days ago (2025-04-22 12:24:17 UTC) | 5 | C++ | Oracle Fusion DuckDB extension  |
| 92 | [onager](https://duckdb.org/community_extensions/extensions/onager.html) | [onager](https://github.com/CogitatorTech/onager) | 🟢 Ongoing | 🔥 Very Active | today (2026-01-17 18:33:49 UTC) | 108 | Rust | A DuckDB extension for graph data analytics |
| 93 | [onelake](https://duckdb.org/community_extensions/extensions/onelake.html) | [duckdb_onelake](https://github.com/datumnova/duckdb_onelake) | ❓ Unknown | 🟡 Stable | 47 days ago (2025-12-01 10:28:22 UTC) | 18 | C++ | DuckDB extension: onelake by datumnova |
| 94 | [open_prompt](https://duckdb.org/community_extensions/extensions/open_prompt.html) | [openprompt](https://github.com/Query-farm/openprompt) | ❓ Unknown | 🟡 Stable | 44 days ago (2025-12-04 23:27:33 UTC) | 53 | C++ | DuckDB Community Extension to prompt LLMs from SQL |
| 95 | [otlp](https://duckdb.org/community_extensions/extensions/otlp.html) | [duckdb-otlp](https://github.com/smithclay/duckdb-otlp) | 🟢 Ongoing | 🔥 Very Active | 4 days ago (2026-01-14 04:35:46 UTC) | 33 | C++ | query OpenTelemetry metrics, logs, and traces (OTLP) in duckdb |
| 96 | [parser_tools](https://duckdb.org/community_extensions/extensions/parser_tools.html) | [duckdb_extension_parser_tools](https://github.com/hotdata-dev/duckdb_extension_parser_tools) | 🟢 Ongoing | 🟠 Stale | 115 days ago (2025-09-24 17:46:33 UTC) | 23 | C++ | Parse sql - with sql! |
| 97 | [pbix](https://duckdb.org/community_extensions/extensions/pbix.html) | [duckdb-pbix-extension](https://github.com/Hugoberry/duckdb-pbix-extension) | 🟢 Ongoing | 🟡 Stable | 85 days ago (2025-10-24 13:47:34 UTC) | 33 | C++ | Duckdb extension for parsing the metadata and contents of the embedded data m... |
| 98 | [pcap_reader](https://duckdb.org/community_extensions/extensions/pcap_reader.html) | [pcap](https://github.com/Query-farm/pcap) | ❓ Unknown | 🟠 Stale | 116 days ago (2025-09-23 19:24:42 UTC) | 11 | Rust | DuckDB PCAP Reader Extension made in Rust |
| 99 | [pdal](https://duckdb.org/community_extensions/extensions/pdal.html) | [duckdb-pdal](https://github.com/ahuarte47/duckdb-pdal) | 🟢 Ongoing | 🔥 Very Active | 2 days ago (2026-01-15 22:51:11 UTC) | 24 | C++ | DuckDB extension for manipulating point cloud data using SQL |
| 100 | [pivot_table](https://duckdb.org/community_extensions/extensions/pivot_table.html) | [pivot_table](https://github.com/Alex-Monahan/pivot_table) | ❓ Unknown | 🟠 Stale | over a year ago (2024-09-22 21:18:45 UTC) | 17 | C++ | Full spreadsheet-style pivot table through SQL macros. Just specify values, r... |
| 101 | [poached](https://duckdb.org/community_extensions/extensions/poached.html) | [poached](https://github.com/sidequery/poached) | 🟢 Ongoing | ✅ Active | 22 days ago (2025-12-26 21:13:19 UTC) | 7 | C++ | A DuckDB extension that exposes SQL parsing functionality for building IDEs,... |
| 102 | [prql](https://duckdb.org/community_extensions/extensions/prql.html) | [duckdb-prql](https://github.com/ywelsch/duckdb-prql) | 🟢 Ongoing | 🟠 Stale | 117 days ago (2025-09-22 18:45:53 UTC) | 315 | C++ | PRQL as a DuckDB extension |
| 103 | [psql](https://duckdb.org/community_extensions/extensions/psql.html) | [duckdb-psql](https://github.com/ywelsch/duckdb-psql) | 🟢 Ongoing | 🟠 Stale | 117 days ago (2025-09-22 18:45:44 UTC) | 101 | C++ | A piped SQL for DuckDB |
| 104 | [pst](https://duckdb.org/community_extensions/extensions/pst.html) | [duckdb-pst](https://github.com/intellekthq/duckdb-pst) | 🟢 Ongoing | 🔥 Very Active | today (2026-01-17 19:55:20 UTC) | 8 | C++ | In-place querying of Microsoft PST files, directly from storage, with SQL. |
| 105 | [psyduck](https://duckdb.org/community_extensions/extensions/psyduck.html) | [psyduck](https://github.com/Ian-Fogelman/psyduck) | 🟢 Ongoing | 🟡 Stable | 34 days ago (2025-12-14 15:10:39 UTC) | 6 | C++ | Pysduck a DuckDB community extension about Pokémon. |
| 106 | [pyroscope](https://duckdb.org/community_extensions/extensions/pyroscope.html) | [pyroscope](https://github.com/Query-farm/pyroscope) | ❓ Unknown | 🟠 Stale | 116 days ago (2025-09-23 19:24:44 UTC) | 20 | Rust | DuckDB Pyroscope Extension for Continuous Profiling |
| 107 | [quack](https://duckdb.org/community_extensions/extensions/quack.html) | [extension-template](https://github.com/duckdb/extension-template) | ❓ Unknown | ✅ Active | 30 days ago (2025-12-18 13:53:03 UTC) | 256 | Python | Template for DuckDB extensions to help you develop, test and deploy a custom... |
| 108 | [quackfix](https://duckdb.org/community_extensions/extensions/quackfix.html) | [QuackFIX](https://github.com/hyehudai/QuackFIX) | 🟢 Ongoing | ✅ Active | 23 days ago (2025-12-25 10:36:24 UTC) | 16 | C++ | Fix log extension for duckdb |
| 109 | [quackformers](https://duckdb.org/community_extensions/extensions/quackformers.html) | [quackformers](https://github.com/martin-conur/quackformers) | ❓ Unknown | ✅ Active | 27 days ago (2025-12-21 18:43:16 UTC) | 10 | Rust | DuckDB NLP extension. |
| 110 | [quackstore](https://duckdb.org/community_extensions/extensions/quackstore.html) | [QuackStore](https://github.com/coginiti-dev/QuackStore) | ❓ Unknown | 🟡 Stable | 51 days ago (2025-11-27 16:15:12 UTC) | 109 | C++ | DuckDB extension: quackstore by coginiti-dev |
| 111 | [quickjs](https://duckdb.org/community_extensions/extensions/quickjs.html) | [quickjs](https://github.com/Query-farm/quickjs) | 🟢 Ongoing | 🟡 Stable | 44 days ago (2025-12-04 23:29:10 UTC) | 10 | C++ | DuckDB extension: quickjs by quackscience |
| 112 | [radio](https://duckdb.org/community_extensions/extensions/radio.html) | [radio](https://github.com/Query-farm/radio) | 🟢 Ongoing | 🟡 Stable | 44 days ago (2025-12-04 16:10:12 UTC) | 35 | C++ | Radio is a DuckDB extension by Query.Farm that brings real-time event streams... |
| 113 | [rapidfuzz](https://duckdb.org/community_extensions/extensions/rapidfuzz.html) | [rapidfuzz](https://github.com/Query-farm/rapidfuzz) | 🟢 Ongoing | 🟡 Stable | 44 days ago (2025-12-04 16:10:12 UTC) | 10 | C++ | DuckDB Community Extension adding RapidFuzz algorithms for search, deduplicat... |
| 114 | [read_stat](https://duckdb.org/community_extensions/extensions/read_stat.html) | [duckdb-read-stat](https://github.com/mettekou/duckdb-read-stat) | 🟢 Ongoing | 🟡 Stable | 51 days ago (2025-11-27 13:46:07 UTC) | 27 | C | Read data sets from SAS, Stata, and SPSS from DuckDB with ReadStat |
| 115 | [redis](https://duckdb.org/community_extensions/extensions/redis.html) | [redis](https://github.com/Query-farm/redis) | 🟢 Ongoing | 🟡 Stable | 44 days ago (2025-12-04 23:42:10 UTC) | 8 | C++ | DuckDB Redis Client community extension |
| 116 | [rusty_quack](https://duckdb.org/community_extensions/extensions/rusty_quack.html) | [extension-template-rs](https://github.com/duckdb/extension-template-rs) | ❓ Unknown | 🟡 Stable | 32 days ago (2025-12-16 13:27:35 UTC) | 92 | Rust | (Experimental) Template for Rust-based DuckDB extensions |
| 117 | [rusty_sheet](https://duckdb.org/community_extensions/extensions/rusty_sheet.html) | [rusty-sheet](https://github.com/redraiment/rusty-sheet) | 🟢 Ongoing | ✅ Active | 30 days ago (2025-12-19 03:04:01 UTC) | 60 | Rust | An Excel/WPS/OpenDocument Spreadsheets file reader for DuckDB |
| 118 | [sazgar](https://duckdb.org/community_extensions/extensions/sazgar.html) | [Sazgar](https://github.com/Angelerator/Sazgar) | 🟢 Ongoing | ✅ Active | 9 days ago (2026-01-08 11:30:16 UTC) | 14 | HTML | DuckDB extension for system monitoring & intelligent SQL routing. 25+ functio... |
| 119 | [scalarfs](https://duckdb.org/community_extensions/extensions/scalarfs.html) | [duckdb_scalarfs](https://github.com/teaguesterling/duckdb_scalarfs) | 🟢 Ongoing | 🔥 Very Active | 2 days ago (2026-01-15 15:20:47 UTC) | 6 | C++ | A collection of simple virtual filesystems for treating scalar values as files. |
| 120 | [scrooge](https://duckdb.org/community_extensions/extensions/scrooge.html) | [Scrooge-McDuck](https://github.com/pdet/Scrooge-McDuck) | ❓ Unknown | 🟠 Stale | 278 days ago (2025-04-14 11:16:07 UTC) | 152 | C++ | DuckDB extension: scrooge by pdet |
| 121 | [sheetreader](https://duckdb.org/community_extensions/extensions/sheetreader.html) | [sheetreader-duckdb](https://github.com/polydbms/sheetreader-duckdb) | ❓ Unknown | 🟡 Stable | 38 days ago (2025-12-10 21:40:53 UTC) | 56 | Jupyter Notebook | DuckDB extension: sheetreader by polydbms |
| 122 | [shellfs](https://duckdb.org/community_extensions/extensions/shellfs.html) | [shellfs](https://github.com/Query-farm/shellfs) | 🟢 Ongoing | 🟡 Stable | 44 days ago (2025-12-04 18:51:18 UTC) | 91 | C++ | DuckDB extension allowing shell commands to be used for input and output. |
| 123 | [sitemap](https://duckdb.org/community_extensions/extensions/sitemap.html) | [duckdb-sitemap](https://github.com/midwork-finds-jobs/duckdb-sitemap) | 🟢 Ongoing | ✅ Active | 9 days ago (2026-01-08 16:57:50 UTC) | 1 | C++ | DuckDB extension for parsing XML sitemaps from websites |
| 124 | [sitting_duck](https://duckdb.org/community_extensions/extensions/sitting_duck.html) | [sitting_duck](https://github.com/teaguesterling/sitting_duck) | 🟢 Ongoing | 🔥 Very Active | 6 days ago (2026-01-11 19:26:45 UTC) | 6 | C | DuckDB extension: sitting_duck by teaguesterling |
| 125 | [snowflake](https://duckdb.org/community_extensions/extensions/snowflake.html) | [duckdb-snowflake](https://github.com/iqea-ai/duckdb-snowflake) | 🟢 Ongoing | 🟡 Stable | 38 days ago (2025-12-10 21:41:05 UTC) | 26 | C++ | A powerful DuckDB extension that enables seamless querying of Snowflake datab... |
| 126 | [splink_udfs](https://duckdb.org/community_extensions/extensions/splink_udfs.html) | [splink_udfs](https://github.com/moj-analytical-services/splink_udfs) | ❓ Unknown | 🟡 Stable | 64 days ago (2025-11-14 14:37:49 UTC) | 14 | C++ | DuckDB extension: splink_udfs by moj-analytical-services |
| 127 | [sshfs](https://duckdb.org/community_extensions/extensions/sshfs.html) | [duckdb-sshfs](https://github.com/midwork-finds-jobs/duckdb-sshfs) | ❓ Unknown | 🟡 Stable | 61 days ago (2025-11-17 11:24:29 UTC) | 1 | C++ | DuckDB sshfs extension - Read and write files through ssh inside DuckDB |
| 128 | [st_read_multi](https://duckdb.org/community_extensions/extensions/st_read_multi.html) | [duckdb-ext-st-read-multi](https://github.com/yutannihilation/duckdb-ext-st-read-multi) | 🟢 Ongoing | 🔥 Very Active | 4 days ago (2026-01-13 22:41:46 UTC) | 5 | Rust | A DuckDB extension to import multiple geospatial files with `ST_Read_Multi()` |
| 129 | [stochastic](https://duckdb.org/community_extensions/extensions/stochastic.html) | [stochastic](https://github.com/Query-farm/stochastic) | 🟢 Ongoing | 🟡 Stable | 44 days ago (2025-12-04 16:10:15 UTC) | 14 | C++ | A DuckDB extension that add comprehensive statistical distribution functions... |
| 130 | [substrait](https://duckdb.org/community_extensions/extensions/substrait.html) | [duckdb-substrait-extension](https://github.com/substrait-io/duckdb-substrait-extension) | ❓ Unknown | 🟡 Stable | 32 days ago (2025-12-16 13:47:32 UTC) | 53 | C++ | DuckDB extension: substrait by substrait-io |
| 131 | [system_stats](https://duckdb.org/community_extensions/extensions/system_stats.html) | [system_stats](https://github.com/dentiny/system_stats) | 🟢 Ongoing | 🟡 Stable | 39 days ago (2025-12-09 21:55:14 UTC) | 1 | C++ | DuckDB extension: system_stats by dentiny |
| 132 | [tarfs](https://duckdb.org/community_extensions/extensions/tarfs.html) | [duckdb_tarfs](https://github.com/Maxxen/duckdb_tarfs) | ❓ Unknown | 🟠 Stale | over a year ago (2024-08-26 11:01:47 UTC) | 11 | C++ | DuckDB extension: tarfs by Maxxen |
| 133 | [tera](https://duckdb.org/community_extensions/extensions/tera.html) | [tera](https://github.com/Query-farm/tera) | 🟢 Ongoing | 🟡 Stable | 34 days ago (2025-12-14 14:20:55 UTC) | 7 | C++ | DuckDB extension: tera |
| 134 | [textplot](https://duckdb.org/community_extensions/extensions/textplot.html) | [textplot](https://github.com/Query-farm/textplot) | 🟢 Ongoing | 🟡 Stable | 44 days ago (2025-12-04 16:10:17 UTC) | 15 | C++ | A DuckDB community extension that enables text-based data visualization direc... |
| 135 | [title_mapper](https://duckdb.org/community_extensions/extensions/title_mapper.html) | [duckdb-title-mapper](https://github.com/martin-conur/duckdb-title-mapper) | ❓ Unknown | 🟠 Stale | 97 days ago (2025-10-12 22:54:26 UTC) | 2 | Rust | DuckDB extension: title_mapper by martin-conur |
| 136 | [tributary](https://duckdb.org/community_extensions/extensions/tributary.html) | [tributary](https://github.com/Query-farm/tributary) | 🟢 Ongoing | 🟡 Stable | 44 days ago (2025-12-04 16:10:18 UTC) | 52 | C++ | A DuckDB Extension for Kafka |
| 137 | [tsid](https://duckdb.org/community_extensions/extensions/tsid.html) | [tsid](https://github.com/Query-farm/tsid) | 🟢 Ongoing | 🟡 Stable | 44 days ago (2025-12-04 23:54:00 UTC) | 5 | C++ | TSID Extension for DuckDB  |
| 138 | [ulid](https://duckdb.org/community_extensions/extensions/ulid.html) | [duckdb_ulid](https://github.com/Maxxen/duckdb_ulid) | ❓ Unknown | 🟠 Stale | over a year ago (2024-07-09 09:35:50 UTC) | 24 | C++ | DuckDB extension: ulid by Maxxen |
| 139 | [urlpattern](https://duckdb.org/community_extensions/extensions/urlpattern.html) | [duckdb_urlpattern](https://github.com/teaguesterling/duckdb_urlpattern) | 🟢 Ongoing | 🔥 Very Active | 6 days ago (2026-01-11 21:26:52 UTC) | 1 | C++ | An implementation of URLPattern for DuckDB |
| 140 | [valhalla_routing](https://duckdb.org/community_extensions/extensions/valhalla_routing.html) | [duckdb-valhalla-routing](https://github.com/midwork-finds-jobs/duckdb-valhalla-routing) | 🟢 Ongoing | ✅ Active | 11 days ago (2026-01-07 04:28:53 UTC) | 0 | Makefile | WIP: Attempt to package valhalla routing engine to duckdb |
| 141 | [warc](https://duckdb.org/community_extensions/extensions/warc.html) | [duckdb_warc](https://github.com/midwork-finds-jobs/duckdb_warc) | ❓ Unknown | 🟡 Stable | 48 days ago (2025-11-30 19:41:21 UTC) | 2 | Rust | DuckDB extension for parsing WARC files |
| 142 | [web_archive](https://duckdb.org/community_extensions/extensions/web_archive.html) | [duckdb-web-archive](https://github.com/midwork-finds-jobs/duckdb-web-archive) | 🟢 Ongoing | 🔥 Very Active | today (2026-01-16 17:44:08 UTC) | 12 | C++ | DuckDB extension to fetch pages from Wayback Machine & Common Crawl |
| 143 | [web_search](https://duckdb.org/community_extensions/extensions/web_search.html) | [duckdb-web-search](https://github.com/midwork-finds-jobs/duckdb-web-search) | 🟢 Ongoing | 🔥 Very Active | 5 days ago (2026-01-12 06:46:15 UTC) | 0 | C++ | Web/HTTP functionality extension by midwork-finds-jobs |
| 144 | [webbed](https://duckdb.org/community_extensions/extensions/webbed.html) | [duckdb_webbed](https://github.com/teaguesterling/duckdb_webbed) | 🟢 Ongoing | ✅ Active | 12 days ago (2026-01-06 04:34:56 UTC) | 39 | C++ | Web/HTTP functionality extension by teaguesterling |
| 145 | [webdavfs](https://duckdb.org/community_extensions/extensions/webdavfs.html) | [duckdb-webdavfs](https://github.com/midwork-finds-jobs/duckdb-webdavfs) | ❓ Unknown | 🟡 Stable | 62 days ago (2025-11-16 18:45:25 UTC) | 1 | C++ | DuckDB WebDAVfs Extension - WebDAV filesystem support for DuckDB |
| 146 | [webmacro](https://duckdb.org/community_extensions/extensions/webmacro.html) | [webmacro](https://github.com/Query-farm/webmacro) | 🟢 Ongoing | 🟡 Stable | 44 days ago (2025-12-05 00:15:35 UTC) | 15 | C++ | DuckDB WebMacro: Share and Load your SQL Macros via gists |
| 147 | [wireduck](https://duckdb.org/community_extensions/extensions/wireduck.html) | [wireduck](https://github.com/hyehudai/wireduck) | 🟢 Ongoing | 🟠 Stale | 116 days ago (2025-09-23 21:22:03 UTC) | 47 | C++ | Duckdb extension to read pcap files |
| 148 | [yaml](https://duckdb.org/community_extensions/extensions/yaml.html) | [duckdb_yaml](https://github.com/teaguesterling/duckdb_yaml) | 🟢 Ongoing | 🔥 Very Active | 6 days ago (2026-01-11 19:39:03 UTC) | 10 | C++ |  A DuckDB to read and work with YAML files in a similar way to JSON files (al... |
| 149 | [yardstick](https://duckdb.org/community_extensions/extensions/yardstick.html) | [yardstick](https://github.com/sidequery/yardstick) | 🟢 Ongoing | ✅ Active | 8 days ago (2026-01-09 15:38:18 UTC) | 35 | Rust | An implementation of Measures in SQL as a DuckDB extension |
| 150 | [zipfs](https://duckdb.org/community_extensions/extensions/zipfs.html) | [duckdb-zipfs](https://github.com/isaacbrodsky/duckdb-zipfs) | 🟢 Ongoing | ✅ Active | 19 days ago (2025-12-29 18:19:46 UTC) | 53 | C++ | DuckDB extension to read files within zip archives. |

</details>
## Appendix: DuckDB Release Information

### Current Release Context

DuckDB follows **semantic versioning** with regular releases. For complete and up-to-date release information, see the official [**DuckDB Release Calendar**](https://duckdb.org/release_calendar.html).

### Release History

| Version | Release Date | Codename | Named After | LTS | Status |
|---------|--------------|----------|-------------|-----|--------|
| **v1.5.0** 📅 | 2026-02-16 | – | – |  | Planned |
| **v1.4.4** 📅 | 2026-01-26 | – | – | ✓ | Planned |
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

<p class="fine-print">Last updated: 2026-01-18</p>
