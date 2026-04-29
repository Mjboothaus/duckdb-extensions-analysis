# DuckDB Extensions Analysis

🦆 **Automated monitoring and analysis of DuckDB's extension ecosystem**


[Jump to Summary](#summary) | [Core Extensions](#core-extensions) | [Community Extensions](#community-extensions)

---

**Running on DuckDB:** v1.5.2 (2026-04-13)
This report provides a comprehensive analysis of DuckDB extensions, including both core extensions (built into DuckDB) and community-contributed extensions.

For third-party extensions discovered outside the official registries, see: [Third-party extensions](https://mjboothaus.github.io/duckdb-extensions-analysis/third-party/).

*Note:* third-party labelling is an ongoing work in progress, so the verified list is partial.

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

### 📊 Quick Stats (with trends)

| **Metric** | **Current** | **Change** |
|------------|-------------|------------|
| **Total Extensions** | 230 | +2 🔼 |
| **Core Extensions** | 0 | Changed |
| **Community Extensions** | 230 | +1 🔼 |
| **Recently Active** (≤ 30 days) | 136 (59.1%) | -5 🔽 |
| **Very Active** (≤ 7 days) | 49 (21.3%) | — |

*Changes since previous analysis*


### 🆕 Recent Additions

gh, sistat



### 🗑️ Removed

encoding



---
## Core Extensions

Core extensions maintained by the DuckDB team and distributed via the official extension repository

**Total:** 0 extensions

<details open markdown="1">
<summary>Click to expand/collapse core extensions table</summary>

| # | Extension | Repository | Status | Last Activity | Stars | Language | Description |
|---|-----------|------------|--------|---------------|-------|----------|-------------|

</details>

---
---
## Community Extensions

Third-party extensions maintained by the community


**Total:** 230 extensions | 🔥 Very Active (≤7d): 49 | ✅ Active (≤30d): 87 | 🟡 Stable (≤90d): 62 | 🟠 Stale (>90d): 32

<details open markdown="1">
<summary>Click to expand/collapse community extensions table</summary>

| # | Extension | Repository | Status | Activity | Last Activity | Stars | Language | Description |
|---|-----------|------------|--------|----------|---------------|-------|----------|-------------|
| 1 | [a5](https://duckdb.org/community_extensions/extensions/a5.html) | [a5](https://github.com/Query-farm/a5) | 🟢 Ongoing | 2 - ✅ Active | 30 days ago (2026-03-29 21:04:28 UTC) | 12 | C++ | A5 Geospatial Extension for DuckDB |
| 2 | [acp](https://duckdb.org/community_extensions/extensions/acp.html) | [duckdb-acp](https://github.com/sidequery/duckdb-acp) | 🟡 Archived | 4 - 🟠 Stale | 139 days ago (2025-12-11 03:36:46 UTC) | 55 | Rust | Use Claude Code & other AI agents from inside DuckDB via extension |
| 3 | [adbc_scanner](https://duckdb.org/community_extensions/extensions/adbc_scanner.html) | [adbc_scanner](https://github.com/Query-farm/adbc_scanner) | 🟢 Ongoing | 1 - 🔥 Very Active | 6 days ago (2026-04-22 14:37:02 UTC) | 13 | C++ | A DuckDB ADBC Scanner Extension - adds support for using ADBC drivers with Du... |
| 4 | [agent_data](https://duckdb.org/community_extensions/extensions/agent_data.html) | [agent_data_duckdb](https://github.com/axsaucedo/agent_data_duckdb) | ❓ Unknown | 3 - 🟡 Stable | 65 days ago (2026-02-22 16:22:05 UTC) | 13 | Rust | DuckDB extension: agent_data by axsaucedo |
| 5 | [airport](https://duckdb.org/community_extensions/extensions/airport.html) | [airport](https://github.com/Query-farm/airport) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-04-27 17:09:49 UTC) | 331 | C++ | The Airport extension for DuckDB, enables the use of Arrow Flight with DuckDB |
| 6 | [aixchess](https://duckdb.org/community_extensions/extensions/aixchess.html) | [aix](https://github.com/thomas-daniels/aix) | 🟢 Ongoing | 2 - ✅ Active | 30 days ago (2026-03-29 12:16:27 UTC) | 24 | Rust | Aix: Efficiently storing and querying chess game collections |
| 7 | [anndata](https://duckdb.org/community_extensions/extensions/anndata.html) | [anndata-duckdb-extension](https://github.com/honicky/anndata-duckdb-extension) | 🟢 Ongoing | 3 - 🟡 Stable | 43 days ago (2026-03-17 04:18:16 UTC) | 8 | C++ | Attach and AnnData file in duckdb and query it with SQL.  Perform SQL over gr... |
| 8 | [anofox_forecast](https://duckdb.org/community_extensions/extensions/anofox_forecast.html) | [anofox-forecast](https://github.com/DataZooDE/anofox-forecast) | ❓ Unknown | 2 - ✅ Active | 13 days ago (2026-04-15 14:27:57 UTC) | 31 | C++ | Statistical timeseries forecasting in DuckDB |
| 9 | [anofox_statistics](https://duckdb.org/community_extensions/extensions/anofox_statistics.html) | [anofox-statistics](https://github.com/DataZooDE/anofox-statistics) | ❓ Unknown | 2 - ✅ Active | 11 days ago (2026-04-17 12:50:57 UTC) | 8 | Rust | A DuckDB extension for statistical regression analysis, providing OLS, Ridge,... |
| 10 | [anofox_tabular](https://duckdb.org/community_extensions/extensions/anofox_tabular.html) | [anofox-tabular](https://github.com/DataZooDE/anofox-tabular) | ❓ Unknown | 1 - 🔥 Very Active | 7 days ago (2026-04-21 18:53:20 UTC) | 14 | C++ | A duckdb extension which combines data quality and data preparation tools for... |
| 11 | [arrow](https://duckdb.org/community_extensions/extensions/arrow.html) | [duckdb-extension-alias](https://github.com/duckdb/duckdb-extension-alias) | ❓ Unknown | 4 - 🟠 Stale | 204 days ago (2025-10-06 09:07:38 UTC) | 4 | C | DuckDB extension: arrow |
| 12 | [astro](https://duckdb.org/community_extensions/extensions/astro.html) | [astro-duck](https://github.com/synapticore-io/astro-duck) | 🟢 Ongoing | 1 - 🔥 Very Active | 7 days ago (2026-04-21 09:12:41 UTC) | 0 | C++ | 60+ astronomical SQL functions for DuckDB: coordinate transforms, CCM89 dust... |
| 13 | [behavioral](https://duckdb.org/community_extensions/extensions/behavioral.html) | [duckdb-behavioral](https://github.com/tomtom215/duckdb-behavioral) | ❓ Unknown | 1 - 🔥 Very Active | 6 days ago (2026-04-22 21:31:53 UTC) | 9 | Rust | A DuckDB Community Extension to enable Behavioral Analytics, inspired by Clic... |
| 14 | [bigquery](https://duckdb.org/community_extensions/extensions/bigquery.html) | [duckdb-bigquery](https://github.com/hafenkran/duckdb-bigquery) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-04-27 20:13:51 UTC) | 160 | C++ | Integrates DuckDB with Google BigQuery, allowing direct querying and manageme... |
| 15 | [bitfilters](https://duckdb.org/community_extensions/extensions/bitfilters.html) | [bitfilters](https://github.com/Query-farm/bitfilters) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-04-27 17:21:05 UTC) | 6 | C++ | A high-performance DuckDB extension providing probabilistic data structures f... |
| 16 | [blockduck](https://duckdb.org/community_extensions/extensions/blockduck.html) | [BlockDuck](https://github.com/luohaha/BlockDuck) | 🟢 Ongoing | 4 - 🟠 Stale | 202 days ago (2025-10-08 16:19:04 UTC) | 10 | C++ | Live SQL Queries on Blockchain |
| 17 | [boilstream](https://duckdb.org/community_extensions/extensions/boilstream.html) | [boilstream-extension](https://github.com/dforsber/boilstream-extension) | 🟢 Ongoing | 1 - 🔥 Very Active | 6 days ago (2026-04-23 02:17:43 UTC) | 10 | C++ | Secure Remote Secrets Storage for DuckDB |
| 18 | [brew](https://duckdb.org/community_extensions/extensions/brew.html) | [duckdb-brew](https://github.com/adriens/duckdb-brew) | 🟢 Ongoing | 3 - 🟡 Stable | 34 days ago (2026-03-25 21:43:39 UTC) | 1 | C++ | duckdb extension to report installed brew packages/casks/formulas with SQL |
| 19 | [bvh2sql](https://duckdb.org/community_extensions/extensions/bvh2sql.html) | [bvh2sql](https://github.com/nkwork9999/bvh2sql) | 🟢 Ongoing | 4 - 🟠 Stale | 177 days ago (2025-11-02 18:17:05 UTC) | 0 | Makefile | SQL-related extension by nkwork9999 |
| 20 | [cache_httpfs](https://duckdb.org/community_extensions/extensions/cache_httpfs.html) | [duck-read-cache-fs](https://github.com/dentiny/duck-read-cache-fs) | 🟢 Ongoing | 2 - ✅ Active | 11 days ago (2026-04-17 07:33:55 UTC) | 137 | C++ | This repository is made as read-only filesystem for remote access. |
| 21 | [cache_prewarm](https://duckdb.org/community_extensions/extensions/cache_prewarm.html) | [duckdb-cache-prewarm](https://github.com/dentiny/duckdb-cache-prewarm) | 🟢 Ongoing | 2 - ✅ Active | 8 days ago (2026-04-20 19:04:46 UTC) | 8 | C++ | DuckDB extension: cache_prewarm by dentiny |
| 22 | [capi_quack](https://duckdb.org/community_extensions/extensions/capi_quack.html) | [extension-template-c](https://github.com/duckdb/extension-template-c) | ❓ Unknown | 3 - 🟡 Stable | 33 days ago (2026-03-26 12:21:42 UTC) | 30 | C | (Experimental) C/C++ template for DuckDB extensions based on the C API |
| 23 | [cassandra](https://duckdb.org/community_extensions/extensions/cassandra.html) | [duckdb-cassandra](https://github.com/dioptre/duckdb-cassandra) | ❓ Unknown | 4 - 🟠 Stale | 190 days ago (2025-10-20 19:15:10 UTC) | 2 | C++ | DuckDB Connector for Cassandra |
| 24 | [celestial](https://duckdb.org/community_extensions/extensions/celestial.html) | [duckdb-celestial](https://github.com/lisa-sgs/duckdb-celestial) | 🟢 Ongoing | 3 - 🟡 Stable | 46 days ago (2026-03-13 14:47:49 UTC) | 2 | C++ | DuckDB extension providing astronomical coordinates utilities |
| 25 | [chaos](https://duckdb.org/community_extensions/extensions/chaos.html) | [duckdb-chaos](https://github.com/taniabogatsch/duckdb-chaos) | 🟢 Ongoing | 3 - 🟡 Stable | 75 days ago (2026-02-12 14:50:01 UTC) | 1 | C++ | DuckDB extension: chaos by taniabogatsch |
| 26 | [chess](https://duckdb.org/community_extensions/extensions/chess.html) | [duckdb-chess](https://github.com/dotneB/duckdb-chess) | 🟢 Ongoing | 2 - ✅ Active | 13 days ago (2026-04-16 04:32:18 UTC) | 2 | Rust | A DuckDB extension for parsing and analyzing chess games in PGN format. |
| 27 | [chsql](https://duckdb.org/community_extensions/extensions/chsql.html) | [clickhouse-sql](https://github.com/Query-farm/clickhouse-sql) | ❓ Unknown | 3 - 🟡 Stable | 69 days ago (2026-02-18 19:49:47 UTC) | 90 | C++ | DuckDB Community Extension implementing ClickHouse SQL Dialect macros and Cus... |
| 28 | [chsql_native](https://duckdb.org/community_extensions/extensions/chsql_native.html) | [clickhouse-native](https://github.com/Query-farm/clickhouse-native) | ❓ Unknown | 3 - 🟡 Stable | 69 days ago (2026-02-18 19:49:46 UTC) | 19 | Rust | Experimental ClickHouse Native Client and Native file reader Extension for Du... |
| 29 | [cityjson](https://duckdb.org/community_extensions/extensions/cityjson.html) | [duckdb-cityjson](https://github.com/cityjson/duckdb-cityjson) | ❓ Unknown | 2 - ✅ Active | 14 days ago (2026-04-14 07:30:03 UTC) | 8 | C++ | Data format handling extension by cityjson |
| 30 | [clamp](https://duckdb.org/community_extensions/extensions/clamp.html) | [duckdb_clamp](https://github.com/oglego/duckdb_clamp) | 🟢 Ongoing | 1 - 🔥 Very Active | 3 days ago (2026-04-26 01:35:35 UTC) | 2 | C++ | The Clamp extension introduces range-clamping scalar functions to DuckDB. Ini... |
| 31 | [cloudfront](https://duckdb.org/community_extensions/extensions/cloudfront.html) | [duckdb-cloudfront](https://github.com/midwork-finds-jobs/duckdb-cloudfront) | 🟢 Ongoing | 3 - 🟡 Stable | 82 days ago (2026-02-05 15:32:51 UTC) | 1 | C++ | DuckDB module which provides custom authentication methods on top of httpfs m... |
| 32 | [crawler](https://duckdb.org/community_extensions/extensions/crawler.html) | [duckdb-crawler](https://github.com/midwork-finds-jobs/duckdb-crawler) | 🟢 Ongoing | 2 - ✅ Active | 26 days ago (2026-04-03 04:32:07 UTC) | 10 | C++ | DuckDB extension: crawler by midwork-finds-jobs |
| 33 | [cronjob](https://duckdb.org/community_extensions/extensions/cronjob.html) | [cronjob](https://github.com/Query-farm/cronjob) | 🟢 Ongoing | 2 - ✅ Active | 30 days ago (2026-03-29 21:04:33 UTC) | 48 | C++ | DuckDB CronJob Extension |
| 34 | [crypto](https://duckdb.org/community_extensions/extensions/crypto.html) | [crypto](https://github.com/Query-farm/crypto) | 🟢 Ongoing | 1 - 🔥 Very Active | 6 days ago (2026-04-22 13:25:10 UTC) | 27 | C++ | DuckDB Extension for cryptographic hash functions and HMAC |
| 35 | [curl_httpfs](https://duckdb.org/community_extensions/extensions/curl_httpfs.html) | [duckdb-curl-filesystem](https://github.com/dentiny/duckdb-curl-filesystem) | 🟢 Ongoing | 2 - ✅ Active | 10 days ago (2026-04-19 00:08:47 UTC) | 7 | C++ | Filesystem built upon libcurl. |
| 36 | [cwiqduck](https://duckdb.org/community_extensions/extensions/cwiqduck.html) | [cwiqduck](https://github.com/cwiq-os/cwiqduck) | 🟢 Ongoing | 4 - 🟠 Stale | 141 days ago (2025-12-09 02:09:40 UTC) | 3 | C++ | DuckDB extensions for CWIQ |
| 37 | [dash](https://duckdb.org/community_extensions/extensions/dash.html) | [dash](https://github.com/gropaul/dash) | 🟢 Ongoing | 1 - 🔥 Very Active | 6 days ago (2026-04-22 22:15:03 UTC) | 51 | C++ | Local GUI and Data Canvas as a DuckDB extension |
| 38 | [datasketches](https://duckdb.org/community_extensions/extensions/datasketches.html) | [datasketches](https://github.com/Query-farm/datasketches) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-04-27 17:17:18 UTC) | 44 | C++ | Integrates DuckDB with the high-performance Apache DataSketches library. This... |
| 39 | [dazzleduck](https://duckdb.org/community_extensions/extensions/dazzleduck.html) | [dazzleduck-sql-duckdb](https://github.com/dazzleduck-web/dazzleduck-sql-duckdb) | ❓ Unknown | 3 - 🟡 Stable | 47 days ago (2026-03-12 22:24:42 UTC) | 1 | C++ | DuckDB extension: dazzleduck by dazzleduck-web |
| 40 | [decimal_arithmetic](https://duckdb.org/community_extensions/extensions/decimal_arithmetic.html) | [duckdb-decimal-arithmetic](https://github.com/duckdb/duckdb-decimal-arithmetic) | 🟢 Ongoing | 2 - ✅ Active | 13 days ago (2026-04-15 14:14:23 UTC) | 0 | C++ | DuckDB extension: decimal_arithmetic |
| 41 | [delta_classic](https://duckdb.org/community_extensions/extensions/delta_classic.html) | [delta_classic](https://github.com/djouallah/delta_classic) | 🟢 Ongoing | 3 - 🟡 Stable | 47 days ago (2026-03-13 00:57:38 UTC) | 5 | C++ | DuckDB extension to attach a directory of Delta tables as a database |
| 42 | [delta_export](https://duckdb.org/community_extensions/extensions/delta_export.html) | [delta_export](https://github.com/djouallah/delta_export) | 🟢 Ongoing | 3 - 🟡 Stable | 46 days ago (2026-03-13 07:02:40 UTC) | 5 | C++ | DuckDB extension to export Delta Lake metadata from DuckLake |
| 43 | [dns](https://duckdb.org/community_extensions/extensions/dns.html) | [duckdb-dns](https://github.com/tobilg/duckdb-dns) | 🟢 Ongoing | 1 - 🔥 Very Active | 5 days ago (2026-04-23 16:42:42 UTC) | 16 | Rust | DNS (Reverse) Lookup Extension for DuckDB |
| 44 | [dplyr](https://duckdb.org/community_extensions/extensions/dplyr.html) | [libdplyr](https://github.com/mrchypark/libdplyr) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-04-29 04:44:46 UTC) | 13 | Rust | DuckDB extension: dplyr by mrchypark |
| 45 | [dqtest](https://duckdb.org/community_extensions/extensions/dqtest.html) | [duckdb-dataquality-extension](https://github.com/vhe74/duckdb-dataquality-extension) | 🟢 Ongoing | 3 - 🟡 Stable | 84 days ago (2026-02-03 18:35:04 UTC) | 4 | C++ | Duckdb extension to run data quality tests |
| 46 | [duck_block_utils](https://duckdb.org/community_extensions/extensions/duck_block_utils.html) | [duckdb_duck_block_utils](https://github.com/teaguesterling/duckdb_duck_block_utils) | 🟢 Ongoing | 3 - 🟡 Stable | 64 days ago (2026-02-23 23:41:31 UTC) | 1 | C++ | A collection of utility functions to work with doc block-style structures and... |
| 47 | [duck_delta_share](https://duckdb.org/community_extensions/extensions/duck_delta_share.html) | [duck_delta_share](https://github.com/cwiq-os/duck_delta_share) | 🟢 Ongoing | 4 - 🟠 Stale | 99 days ago (2026-01-20 02:52:58 UTC) | 3 | C++ | DuckDB extension for enabling Delta Sharing client capabilities.  |
| 48 | [duck_dggs](https://duckdb.org/community_extensions/extensions/duck_dggs.html) | [duckdb-dggs](https://github.com/am2222/duckdb-dggs) | 🟢 Ongoing | 1 - 🔥 Very Active | 4 days ago (2026-04-25 03:22:27 UTC) | 0 | C++ | A DuckDB extension for discrete global grid systems (DGGS) powered by DGGRID v8. |
| 49 | [duck_geoarrow](https://duckdb.org/community_extensions/extensions/duck_geoarrow.html) | [duck_geoarrow](https://github.com/am2222/duck_geoarrow) | 🟢 Ongoing | 2 - ✅ Active | 13 days ago (2026-04-15 13:13:55 UTC) | 2 | C++ | This extension, Duck_Geoarrow, provides functions to convert between WKB (Wel... |
| 50 | [duck_hunt](https://duckdb.org/community_extensions/extensions/duck_hunt.html) | [duck_hunt](https://github.com/teaguesterling/duck_hunt) | 🟢 Ongoing | 3 - 🟡 Stable | 37 days ago (2026-03-22 20:00:38 UTC) | 3 | C++ | Tools for working with unit test suite results |
| 51 | [duck_lineage](https://duckdb.org/community_extensions/extensions/duck_lineage.html) | [duck_lineage](https://github.com/ilum-cloud/duck_lineage) | 🟢 Ongoing | 2 - ✅ Active | 13 days ago (2026-04-15 18:25:53 UTC) | 55 | Python | A extension for DuckDB, which captures lineage events for executed queries |
| 52 | [duck_lk](https://duckdb.org/community_extensions/extensions/duck_lk.html) | [duck-lk](https://github.com/nrminor/duck-lk) | 🟢 Ongoing | 2 - ✅ Active | 11 days ago (2026-04-18 03:05:52 UTC) | 0 | Rust | Interact with tables from your LabKey LIMS natively in DuckDB |
| 53 | [duck_tails](https://duckdb.org/community_extensions/extensions/duck_tails.html) | [duck_tails](https://github.com/teaguesterling/duck_tails) | 🟢 Ongoing | 2 - ✅ Active | 16 days ago (2026-04-12 17:48:36 UTC) | 15 | C++ | A DuckDB extension for exploring and reading git history. |
| 54 | [duckdb_geoip_rs](https://duckdb.org/community_extensions/extensions/duckdb_geoip_rs.html) | [duckdb-geoip-rs](https://github.com/william-billaud/duckdb-geoip-rs) | 🟢 Ongoing | 2 - ✅ Active | 14 days ago (2026-04-14 14:44:09 UTC) | 5 | Rust | Database connectivity extension by william-billaud |
| 55 | [duckdb_mcp](https://duckdb.org/community_extensions/extensions/duckdb_mcp.html) | [duckdb_mcp](https://github.com/teaguesterling/duckdb_mcp) | 🟢 Ongoing | 2 - ✅ Active | 17 days ago (2026-04-11 18:16:01 UTC) | 48 | C++ | A simple MCP server extension for DuckDB |
| 56 | [duckdb_midi](https://github.com/nkwork9999/duckdb-midi) | [duckdb-midi](https://github.com/nkwork9999/duckdb-midi) | ❓ Unknown | 3 - 🟡 Stable | 45 days ago (2026-03-14 10:57:41 UTC) | 0 | C++ | Database connectivity extension by nkwork9999 |
| 57 | [duckdb_zarr](https://duckdb.org/community_extensions/extensions/duckdb_zarr.html) | [duckdb_zarr](https://github.com/WayScience/duckdb_zarr) | 🟢 Ongoing | 2 - ✅ Active | 30 days ago (2026-03-29 23:42:57 UTC) | 2 | C++ | A DuckDB extension for querying Zarr arrays with SQL through relational proje... |
| 58 | [duckdbi](https://duckdb.org/community_extensions/extensions/duckdbi.html) | [DuckDBI](https://github.com/nkwork9999/DuckDBI) | 🟢 Ongoing | 3 - 🟡 Stable | 45 days ago (2026-03-14 11:04:19 UTC) | 1 | C++ | Database connectivity extension by nkwork9999 |
| 59 | [duckgl](https://duckdb.org/community_extensions/extensions/duckgl.html) | [duckgl](https://github.com/nkwork9999/duckgl) | 🟢 Ongoing | 3 - 🟡 Stable | 55 days ago (2026-03-04 16:41:20 UTC) | 5 | C++ | DuckDB extension: duckgl by nkwork9999 |
| 60 | [duckherder](https://duckdb.org/community_extensions/extensions/duckherder.html) | [duckdb-distributed-execution](https://github.com/dentiny/duckdb-distributed-execution) | ❓ Unknown | 3 - 🟡 Stable | 49 days ago (2026-03-10 09:36:00 UTC) | 53 | C++ | Distributed execution for duckdb queries. |
| 61 | [duckhog](https://duckdb.org/community_extensions/extensions/duckhog.html) | [duckhog](https://github.com/PostHog/duckhog) | ❓ Unknown | 1 - 🔥 Very Active | 2 days ago (2026-04-27 02:31:11 UTC) | 6 | C++ | duckdb extension to connect to posthog managed data warehouse  |
| 62 | [duckhts](https://duckdb.org/community_extensions/extensions/duckhts.html) | [duckhts](https://github.com/RGenomicsETL/duckhts) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-04-28 17:01:39 UTC) | 12 | C | 'htslib' based 'Duckdb' Extenstion for High Throughput Sequencing File Formats |
| 63 | [duckpgq](https://duckdb.org/community_extensions/extensions/duckpgq.html) | [duckpgq-extension](https://github.com/cwida/duckpgq-extension) | ❓ Unknown | 2 - ✅ Active | 19 days ago (2026-04-09 13:13:43 UTC) | 398 | C++ | DuckDB extension that adds support for SQL/PGQ and graph algorithms |
| 64 | [ducksmiles](https://duckdb.org/community_extensions/extensions/ducksmiles.html) | [duckSMILES](https://github.com/nkwork9999/duckSMILES) | 🟢 Ongoing | 2 - ✅ Active | 21 days ago (2026-04-07 14:15:33 UTC) | 0 | Rust | DuckDB extension: ducksmiles by nkwork9999 |
| 65 | [ducksync](https://duckdb.org/community_extensions/extensions/ducksync.html) | [ducksync](https://github.com/danjsiegel/ducksync) | 🟢 Ongoing | 2 - ✅ Active | 8 days ago (2026-04-21 00:33:14 UTC) | 6 | C++ | DuckDB extension: ducksync by danjsiegel |
| 66 | [ducktinycc](https://duckdb.org/community_extensions/extensions/ducktinycc.html) | [DuckTinyCC](https://github.com/sounkou-bioinfo/DuckTinyCC) | 🟢 Ongoing | 2 - ✅ Active | 22 days ago (2026-04-06 19:11:24 UTC) | 3 | C | 'C' Scripting in 'Duckdb' using 'TinyCC' |
| 67 | [eeagrid](https://duckdb.org/community_extensions/extensions/eeagrid.html) | [duckdb-eeagrid](https://github.com/ahuarte47/duckdb-eeagrid) | 🟢 Ongoing | 2 - ✅ Active | 8 days ago (2026-04-20 18:06:44 UTC) | 0 | C++ | Functions for transforming XY coordinates to and from the EEA Reference Grid... |
| 68 | [eenddb](https://duckdb.org/community_extensions/extensions/eenddb.html) | [eenddb](https://github.com/Dtenwolde/eenddb) | 🟢 Ongoing | 2 - ✅ Active | 28 days ago (2026-03-31 09:31:58 UTC) | 4 | C++ | Database connectivity extension by Dtenwolde |
| 69 | [elasticsearch](https://duckdb.org/community_extensions/extensions/elasticsearch.html) | [duckdb-elasticsearch](https://github.com/tlinhart/duckdb-elasticsearch) | ❓ Unknown | 1 - 🔥 Very Active | today (2026-04-28 16:58:17 UTC) | 17 | C++ | Query Elasticsearch data directly from DuckDB |
| 70 | [erpl_web](https://duckdb.org/community_extensions/extensions/erpl_web.html) | [erpl-web](https://github.com/DataZooDE/erpl-web) | 🟢 Ongoing | 1 - 🔥 Very Active | 7 days ago (2026-04-21 18:48:21 UTC) | 27 | C++ | ERPL is a DuckDB extension to connect to API based ecosystems via standard in... |
| 71 | [eurostat](https://duckdb.org/community_extensions/extensions/eurostat.html) | [duckdb-eurostat](https://github.com/ahuarte47/duckdb-eurostat) | 🟢 Ongoing | 2 - ✅ Active | 8 days ago (2026-04-20 18:08:48 UTC) | 30 | C++ | DuckDB extension for reading data from EUROSTAT database using SQL  |
| 72 | [evalexpr_rhai](https://duckdb.org/community_extensions/extensions/evalexpr_rhai.html) | [evalexpr_rhai](https://github.com/Query-farm/evalexpr_rhai) | 🟢 Ongoing | 1 - 🔥 Very Active | 6 days ago (2026-04-23 01:40:35 UTC) | 25 | C++ | A DuckDB extension to evaluate the Rhai scripting language as part of SQL. |
| 73 | [events](https://duckdb.org/community_extensions/extensions/events.html) | [events](https://github.com/Query-farm/events) | 🟢 Ongoing | 2 - ✅ Active | 13 days ago (2026-04-15 12:59:21 UTC) | 0 | C++ | Capture database events and deliver JSON notifications to external programs v... |
| 74 | [faiss](https://duckdb.org/community_extensions/extensions/faiss.html) | [duckdb-faiss-ext](https://github.com/duckdb-faiss-ext/duckdb-faiss-ext) | 🟢 Ongoing | 3 - 🟡 Stable | 50 days ago (2026-03-09 11:54:02 UTC) | 31 | Go | DuckDB wrapper for FAISS - Experimental |
| 75 | [fakeit](https://duckdb.org/community_extensions/extensions/fakeit.html) | [duckdb-fakeit](https://github.com/tobilg/duckdb-fakeit) | 🟢 Ongoing | 1 - 🔥 Very Active | 5 days ago (2026-04-23 17:00:03 UTC) | 11 | Rust | DuckDB extension: fakeit by tobilg |
| 76 | [file_dialog](https://duckdb.org/community_extensions/extensions/file_dialog.html) | [duckdb-ext-file-dialog](https://github.com/yutannihilation/duckdb-ext-file-dialog) | ❓ Unknown | 2 - ✅ Active | 10 days ago (2026-04-18 12:47:08 UTC) | 15 | Rust | A DuckDB extension to choose file interactively using native file open dialogs |
| 77 | [finetype](https://duckdb.org/community_extensions/extensions/finetype.html) | [duckdb-finetype](https://github.com/meridian-online/duckdb-finetype) | ❓ Unknown | 3 - 🟡 Stable | 42 days ago (2026-03-17 22:10:13 UTC) | 0 | Rust | DuckDB extension for semantic type classification powered by FineType |
| 78 | [fire_duck_ext](https://duckdb.org/community_extensions/extensions/fire_duck_ext.html) | [fire_duck_ext](https://github.com/BorisBesky/fire_duck_ext) | 🟢 Ongoing | 1 - 🔥 Very Active | 3 days ago (2026-04-25 17:50:34 UTC) | 3 | C++ | duckdb extension for firestore |
| 79 | [fit](https://duckdb.org/community_extensions/extensions/fit.html) | [duckdb-fit-extension](https://github.com/antoriche/duckdb-fit-extension) | ❓ Unknown | 4 - 🟠 Stale | 134 days ago (2025-12-15 19:16:40 UTC) | 1 | C++ | DuckDB extension: fit by antoriche |
| 80 | [fivetran](https://duckdb.org/community_extensions/extensions/fivetran.html) | [fivetran](https://github.com/lnkuiper/fivetran) | ❓ Unknown | 4 - 🟠 Stale | 91 days ago (2026-01-27 11:13:43 UTC) | 0 | C++ | DuckDB extension: fivetran by lnkuiper |
| 81 | [flock](https://duckdb.org/community_extensions/extensions/flock.html) | [flock](https://github.com/dais-polymtl/flock) | 🟢 Ongoing | 2 - ✅ Active | 18 days ago (2026-04-10 16:03:31 UTC) | 335 | C++ | Beyond Quacking: Deep Integration of Language Models and RAG into DuckDB (VLD... |
| 82 | [fsquery](https://duckdb.org/community_extensions/extensions/fsquery.html) | [fsquery](https://github.com/halgari/fsquery) | 🟢 Ongoing | 3 - 🟡 Stable | 43 days ago (2026-03-16 16:09:24 UTC) | 1 | C++ | An extension that allows DuckDB to enumerate and stat files on the disk |
| 83 | [func_apply](https://duckdb.org/community_extensions/extensions/func_apply.html) | [duckdb_func_apply](https://github.com/teaguesterling/duckdb_func_apply) | 🟢 Ongoing | 3 - 🟡 Stable | 64 days ago (2026-02-23 23:42:41 UTC) | 3 | C++ | An exension to allow dynamic function application |
| 84 | [fuzzycomplete](https://duckdb.org/community_extensions/extensions/fuzzycomplete.html) | [fuzzycomplete](https://github.com/Query-farm/fuzzycomplete) | 🟢 Ongoing | 2 - ✅ Active | 30 days ago (2026-03-29 21:04:37 UTC) | 27 | C++ | DuckDB Extension for fuzzy string matching based autocompletion |
| 85 | [gaggle](https://duckdb.org/community_extensions/extensions/gaggle.html) | [gaggle](https://github.com/CogitatorTech/gaggle) | 🟢 Ongoing | 2 - ✅ Active | 10 days ago (2026-04-18 20:27:34 UTC) | 15 | Rust | A DuckDB extension for working with Kaggle datasets |
| 86 | [gcs](https://duckdb.org/community_extensions/extensions/gcs.html) | [duckdb-gcs](https://github.com/northpolesec/duckdb-gcs) | ❓ Unknown | 3 - 🟡 Stable | 46 days ago (2026-03-13 20:21:40 UTC) | 19 | C++ | A GCS-native extension for DuckDB |
| 87 | [gdx](https://duckdb.org/community_extensions/extensions/gdx.html) | [duckdb-gdx](https://github.com/chrispahm/duckdb-gdx) | 🟢 Ongoing | 1 - 🔥 Very Active | 7 days ago (2026-04-21 15:20:11 UTC) | 1 | C++ | DuckDB extension: gdx by chrispahm |
| 88 | [geography](https://duckdb.org/community_extensions/extensions/geography.html) | [duckdb-geography](https://github.com/paleolimbot/duckdb-geography) | ❓ Unknown | 3 - 🟡 Stable | 47 days ago (2026-03-12 16:05:00 UTC) | 44 | C++ | Geospatial data extension by paleolimbot |
| 89 | [geosilo](https://duckdb.org/community_extensions/extensions/geosilo.html) | [geosilo](https://github.com/Query-farm/geosilo) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-04-27 16:21:07 UTC) | 22 | C++ | DuckDB extension for compact geometry encoding using delta-encoded coordinate... |
| 90 | [geotiff](https://duckdb.org/community_extensions/extensions/geotiff.html) | [duckdb-geotiff](https://github.com/babaknaimi/duckdb-geotiff) | ❓ Unknown | 4 - 🟠 Stale | 252 days ago (2025-08-20 05:12:15 UTC) | 2 | C++ | Duckdb extension to read GeoTiffs directly with duckdb database |
| 91 | [gh](https://duckdb.org/community_extensions/extensions/gh.html) | [duckdb-gh](https://github.com/carlopi/duckdb-gh) | 🟢 Ongoing | 2 - ✅ Active | 15 days ago (2026-04-13 19:17:02 UTC) | 3 | C++ | DuckDB extension: gh by carlopi |
| 92 | [gsheets](https://duckdb.org/community_extensions/extensions/gsheets.html) | [duckdb_gsheets](https://github.com/evidence-dev/duckdb_gsheets) | 🟢 Ongoing | 3 - 🟡 Stable | 67 days ago (2026-02-21 04:11:04 UTC) | 341 | C++ | DuckDB extension to read and write Google Sheets using SQL |
| 93 | [h3](https://duckdb.org/community_extensions/extensions/h3.html) | [h3-duckdb](https://github.com/isaacbrodsky/h3-duckdb) | 🟢 Ongoing | 1 - 🔥 Very Active | 2 days ago (2026-04-26 20:48:50 UTC) | 246 | C++ | Bindings for H3 to DuckDB |
| 94 | [h5db](https://duckdb.org/community_extensions/extensions/h5db.html) | [h5db](https://github.com/jokasimr/h5db) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-04-28 19:42:34 UTC) | 1 | C++ | Duckdb extension for reading HDF5 files. |
| 95 | [hashfuncs](https://duckdb.org/community_extensions/extensions/hashfuncs.html) | [hashfuncs](https://github.com/Query-farm/hashfuncs) | 🟢 Ongoing | 2 - ✅ Active | 30 days ago (2026-03-29 21:04:38 UTC) | 12 | C++ | A DuckDB extension that supplies non-cryptographic hash functions. |
| 96 | [hdf5](https://duckdb.org/community_extensions/extensions/hdf5.html) | [duckdb-hdf5](https://github.com/Berrysoft/duckdb-hdf5) | ❓ Unknown | 1 - 🔥 Very Active | 6 days ago (2026-04-23 01:30:36 UTC) | 12 | Rust | HDF5 plugin for duckdb |
| 97 | [hedged_request_fs](https://duckdb.org/community_extensions/extensions/hedged_request_fs.html) | [duckdb-hedged-request](https://github.com/dentiny/duckdb-hedged-request) | 🟢 Ongoing | 2 - ✅ Active | 11 days ago (2026-04-17 07:41:57 UTC) | 1 | C++ | DuckDB extension: hedged_request_fs by dentiny |
| 98 | [highs](https://duckdb.org/community_extensions/extensions/highs.html) | [HiGHS-duckdb](https://github.com/fhk/HiGHS-duckdb) | ❓ Unknown | 3 - 🟡 Stable | 63 days ago (2026-02-25 02:07:48 UTC) | 1 | C++ | Run the solver in the database! |
| 99 | [hive_metastore](https://duckdb.org/community_extensions/extensions/hive_metastore.html) | [duckdb-hive-metastore](https://github.com/ilum-cloud/duckdb-hive-metastore) | 🟢 Ongoing | 2 - ✅ Active | 19 days ago (2026-04-09 14:32:30 UTC) | 1 | C++ | DuckDB extension allowing to connect to Apache Hive Metastore and query the d... |
| 100 | [hnsw_acorn](https://duckdb.org/community_extensions/extensions/hnsw_acorn.html) | [duckdb-hnsw-acorn](https://github.com/cigrainger/duckdb-hnsw-acorn) | 🟢 Ongoing | 3 - 🟡 Stable | 31 days ago (2026-03-28 07:49:47 UTC) | 60 | C++ | ACORN-1 pre-filtered HNSW search for DuckDB |
| 101 | [hostfs](https://duckdb.org/community_extensions/extensions/hostfs.html) | [hostFS](https://github.com/gropaul/hostFS) | ❓ Unknown | 4 - 🟠 Stale | 209 days ago (2025-10-01 21:02:13 UTC) | 31 | C++ | DuckDB extension: hostfs by gropaul |
| 102 | [html_query](https://duckdb.org/community_extensions/extensions/html_query.html) | [duckdb_html_query](https://github.com/midwork-finds-jobs/duckdb_html_query) | ❓ Unknown | 3 - 🟡 Stable | 82 days ago (2026-02-05 15:33:13 UTC) | 1 | Rust | Filter HTML inside duckdb |
| 103 | [html_readability](https://duckdb.org/community_extensions/extensions/html_readability.html) | [duckdb-html-readability](https://github.com/midwork-finds-jobs/duckdb-html-readability) | ❓ Unknown | 3 - 🟡 Stable | 82 days ago (2026-02-05 15:33:16 UTC) | 0 | Rust | DuckDB extension to parse html to readable text |
| 104 | [http_client](https://duckdb.org/community_extensions/extensions/http_client.html) | [httpclient](https://github.com/Query-farm/httpclient) | 🟢 Ongoing | 2 - ✅ Active | 13 days ago (2026-04-15 14:08:54 UTC) | 78 | C++ | DuckDB HTTP GET/POST Client in a Community Extension |
| 105 | [http_request](https://duckdb.org/community_extensions/extensions/http_request.html) | [duckdb_http_request](https://github.com/midwork-finds-jobs/duckdb_http_request) | ❓ Unknown | 3 - 🟡 Stable | 70 days ago (2026-02-17 13:03:03 UTC) | 2 | C++ | Uses the native duckdb httputil to make extra requests in SELECT |
| 106 | [http_stats](https://duckdb.org/community_extensions/extensions/http_stats.html) | [duckdb-http-stats](https://github.com/tlinhart/duckdb-http-stats) | 🟢 Ongoing | 3 - 🟡 Stable | 32 days ago (2026-03-27 13:58:03 UTC) | 0 | C++ | Better HTTP statistics for DuckDB |
| 107 | [httpd_log](https://duckdb.org/community_extensions/extensions/httpd_log.html) | [duckdb-httpd-log](https://github.com/saygox/duckdb-httpd-log) | ❓ Unknown | 4 - 🟠 Stale | 107 days ago (2026-01-12 06:14:58 UTC) | 0 | C++ | duckdb extension |
| 108 | [httpfs_timeout_retry](https://duckdb.org/community_extensions/extensions/httpfs_timeout_retry.html) | [duckdb-httpfs-timeout-retry](https://github.com/dentiny/duckdb-httpfs-timeout-retry) | 🟢 Ongoing | 2 - ✅ Active | 10 days ago (2026-04-19 00:43:09 UTC) | 0 | C++ | Web/HTTP functionality extension by dentiny |
| 109 | [httpserver](https://duckdb.org/community_extensions/extensions/httpserver.html) | [httpserver](https://github.com/Query-farm/httpserver) | ❓ Unknown | 2 - ✅ Active | 15 days ago (2026-04-13 23:57:25 UTC) | 277 | C++ | DuckDB HTTP API Server and Query Interface in a  Community Extension |
| 110 | [infera](https://duckdb.org/community_extensions/extensions/infera.html) | [infera](https://github.com/CogitatorTech/infera) | 🟢 Ongoing | 2 - ✅ Active | 10 days ago (2026-04-18 20:29:02 UTC) | 132 | Rust | A DuckDB extension for in-database inference |
| 111 | [inflector](https://duckdb.org/community_extensions/extensions/inflector.html) | [inflector](https://github.com/Query-farm/inflector) | 🟢 Ongoing | 2 - ✅ Active | 18 days ago (2026-04-10 22:37:09 UTC) | 8 | C++ | Powerful string case transformation and inflection capabilities directly to y... |
| 112 | [ion](https://duckdb.org/community_extensions/extensions/ion.html) | [duckdb-ion](https://github.com/kestra-io/duckdb-ion) | 🟢 Ongoing | 3 - 🟡 Stable | 49 days ago (2026-03-10 15:49:39 UTC) | 4 | C++ | AWS Ion extension for DuckDB |
| 113 | [json_schema](https://duckdb.org/community_extensions/extensions/json_schema.html) | [json_schema](https://github.com/Query-farm/json_schema) | 🟢 Ongoing | 2 - ✅ Active | 30 days ago (2026-03-29 21:04:43 UTC) | 2 | C++ | A DuckDB extension that bring support for validating JSON data using JSON sch... |
| 114 | [jsonata](https://duckdb.org/community_extensions/extensions/jsonata.html) | [jsonata](https://github.com/Query-farm/jsonata) | 🟢 Ongoing | 1 - 🔥 Very Active | 6 days ago (2026-04-22 14:36:35 UTC) | 6 | C++ | The JSONata extension for DuckDB enables expressive, JSON-focused querying an... |
| 115 | [jwt](https://duckdb.org/community_extensions/extensions/jwt.html) | [duckdb_jwt](https://github.com/GalvinGao/duckdb_jwt) | ❓ Unknown | 4 - 🟠 Stale | 294 days ago (2025-07-09 00:13:56 UTC) | 0 | C++ | DuckDB extension: jwt by GalvinGao |
| 116 | [keboola](https://duckdb.org/community_extensions/extensions/keboola.html) | [duckdb-extension](https://github.com/keboola/duckdb-extension) | 🟢 Ongoing | 2 - ✅ Active | 15 days ago (2026-04-14 02:58:46 UTC) | 0 | C++ | DuckDB extension for Keboola Storage — query and write Keboola tables using s... |
| 117 | [lastra](https://duckdb.org/community_extensions/extensions/lastra.html) | [duckdb-lastra](https://github.com/QTSurfer/duckdb-lastra) | 🟢 Ongoing | 2 - ✅ Active | 16 days ago (2026-04-12 10:13:13 UTC) | 0 | C++ | DuckDB extension for reading Lastra columnar time series files natively |
| 118 | [latency_injection_fs](https://duckdb.org/community_extensions/extensions/latency_injection_fs.html) | [duckdb-filesystem-latency-injection](https://github.com/dentiny/duckdb-filesystem-latency-injection) | 🟢 Ongoing | 2 - ✅ Active | 10 days ago (2026-04-19 00:53:46 UTC) | 0 | C++ | DuckDB extension: latency_injection_fs by dentiny |
| 119 | [level_pivot](https://duckdb.org/community_extensions/extensions/level_pivot.html) | [duckdb-level-pivot](https://github.com/halgari/duckdb-level-pivot) | 🟢 Ongoing | 1 - 🔥 Very Active | 5 days ago (2026-04-23 16:05:04 UTC) | 0 | C++ | DuckDB extension: level_pivot by halgari |
| 120 | [lindel](https://duckdb.org/community_extensions/extensions/lindel.html) | [lindel](https://github.com/Query-farm/lindel) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-04-28 20:32:34 UTC) | 61 | C++ | DuckDB Extension Linearization/Delinearization, Z-Order, Hilbert and Morton C... |
| 121 | [llm](https://duckdb.org/community_extensions/extensions/llm.html) | [duckdb-llm](https://github.com/midwork-finds-jobs/duckdb-llm) | 🟢 Ongoing | 3 - 🟡 Stable | 70 days ago (2026-02-17 14:09:08 UTC) | 1 | C++ | DuckDB extension: llm by midwork-finds-jobs |
| 122 | [lsh](https://duckdb.org/community_extensions/extensions/lsh.html) | [lsh](https://github.com/princeton-ddss/lsh) | 🟢 Ongoing | 2 - ✅ Active | 12 days ago (2026-04-16 17:00:45 UTC) | 12 | Rust | DuckDB community extension for locality-sensitive hashing (LSH) |
| 123 | [lua](https://duckdb.org/community_extensions/extensions/lua.html) | [duckdb-lua](https://github.com/isaacbrodsky/duckdb-lua) | 🟢 Ongoing | 1 - 🔥 Very Active | 2 days ago (2026-04-26 20:43:12 UTC) | 10 | C++ | DuckDB extension to evaluate Lua expressions. |
| 124 | [magic](https://duckdb.org/community_extensions/extensions/magic.html) | [duckdb-magic](https://github.com/carlopi/duckdb-magic) | 🟢 Ongoing | 2 - ✅ Active | 15 days ago (2026-04-13 19:33:31 UTC) | 7 | C++ | Auto-detect file types via `libmagic` (`file` utility) |
| 125 | [marisa](https://duckdb.org/community_extensions/extensions/marisa.html) | [marisa](https://github.com/Query-farm/marisa) | 🟢 Ongoing | 2 - ✅ Active | 30 days ago (2026-03-29 21:04:45 UTC) | 11 | C++ | The Marisa extension by Query.Farm integrates the fast, space-efficient MARIS... |
| 126 | [markdown](https://duckdb.org/community_extensions/extensions/markdown.html) | [duckdb_markdown](https://github.com/teaguesterling/duckdb_markdown) | 🟢 Ongoing | 3 - 🟡 Stable | 31 days ago (2026-03-28 16:02:23 UTC) | 16 | C++ | Heirarchical markdown parsing for DuckDB |
| 127 | [maxmind](https://duckdb.org/community_extensions/extensions/maxmind.html) | [duckdb-maxmind](https://github.com/marselester/duckdb-maxmind) | 🟢 Ongoing | 2 - ✅ Active | 12 days ago (2026-04-17 02:52:43 UTC) | 5 | Zig | DuckDB MaxMind extension written in Zig. |
| 128 | [miint](https://duckdb.org/community_extensions/extensions/miint.html) | [duckdb-miint](https://github.com/the-miint/duckdb-miint) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-04-27 22:10:38 UTC) | 4 | C | DuckDB extension: miint by the-miint |
| 129 | [minijinja](https://duckdb.org/community_extensions/extensions/minijinja.html) | [minijinja](https://github.com/Query-farm/minijinja) | 🟢 Ongoing | 2 - ✅ Active | 30 days ago (2026-03-29 21:04:46 UTC) | 5 | C++ | DuckDB extension: minijinja |
| 130 | [miniplot](https://duckdb.org/community_extensions/extensions/miniplot.html) | [miniplot](https://github.com/nkwork9999/miniplot) | 🟢 Ongoing | 4 - 🟠 Stale | 165 days ago (2025-11-15 02:42:43 UTC) | 19 | C++ | DuckDB extension: miniplot by nkwork9999 |
| 131 | [mlpack](https://duckdb.org/community_extensions/extensions/mlpack.html) | [duckdb-mlpack](https://github.com/eddelbuettel/duckdb-mlpack) | 🟢 Ongoing | 4 - 🟠 Stale | 91 days ago (2026-01-27 14:18:00 UTC) | 18 | C++ | Bringing mlpack to duckdb |
| 132 | [monetary](https://duckdb.org/community_extensions/extensions/monetary.html) | [monetary](https://github.com/fyffee/monetary) | ❓ Unknown | 3 - 🟡 Stable | 89 days ago (2026-01-29 11:29:01 UTC) | 0 | C++ | DuckDB extension: monetary by fyffee |
| 133 | [mongo](https://duckdb.org/community_extensions/extensions/mongo.html) | [duckdb-mongo](https://github.com/stephaniewang526/duckdb-mongo) | 🟢 Ongoing | 1 - 🔥 Very Active | 3 days ago (2026-04-25 20:48:52 UTC) | 46 | C++ | Integrates DuckDB with MongoDB, enabling direct SQL queries over MongoDB coll... |
| 134 | [mooncake](https://duckdb.org/community_extensions/extensions/mooncake.html) | [duckdb_mooncake](https://github.com/Mooncake-Labs/duckdb_mooncake) | ❓ Unknown | 4 - 🟠 Stale | 184 days ago (2025-10-26 07:13:05 UTC) | 9 | C++ | Read Iceberg tables written by moonlink in real time |
| 135 | [mpduck](https://duckdb.org/community_extensions/extensions/mpduck.html) | [mpduck](https://github.com/MatthewMooreZA/mpduck) | 🟢 Ongoing | 2 - ✅ Active | 15 days ago (2026-04-13 17:59:29 UTC) | 0 | C++ | DuckDB extension to read and write Prophet model point files. |
| 136 | [msolap](https://duckdb.org/community_extensions/extensions/msolap.html) | [duckdb-msolap-extension](https://github.com/Hugoberry/duckdb-msolap-extension) | ❓ Unknown | 4 - 🟠 Stale | 216 days ago (2025-09-24 16:33:46 UTC) | 14 | C++ | DuckDB extension: msolap by Hugoberry |
| 137 | [mssql](https://duckdb.org/community_extensions/extensions/mssql.html) | [mssql-extension](https://github.com/hugr-lab/mssql-extension) | 🟢 Ongoing | 2 - ✅ Active | 22 days ago (2026-04-06 14:55:32 UTC) | 97 | C++ | DuckDB extension for Microsoft SQL Server (TDS + TLS), with catalog integrati... |
| 138 | [nanoarrow](https://duckdb.org/community_extensions/extensions/nanoarrow.html) | [duckdb-nanoarrow](https://github.com/paleolimbot/duckdb-nanoarrow) | ❓ Unknown | 3 - 🟡 Stable | 47 days ago (2026-03-12 13:57:38 UTC) | 72 | C++ | DuckDB extension: nanoarrow by paleolimbot |
| 139 | [nanodbc](https://duckdb.org/community_extensions/extensions/nanodbc.html) | [duckdb-nanodbc-extension](https://github.com/Hugoberry/duckdb-nanodbc-extension) | ❓ Unknown | 4 - 🟠 Stale | 147 days ago (2025-12-02 16:24:39 UTC) | 53 | C++ | Database connectivity extension by Hugoberry |
| 140 | [nats_js](https://duckdb.org/community_extensions/extensions/nats_js.html) | [duckdb-nats-jetstream](https://github.com/brannn/duckdb-nats-jetstream) | ❓ Unknown | 2 - ✅ Active | 30 days ago (2026-03-30 05:12:16 UTC) | 20 | C++ | DuckDB extension for querying NATS JetStream message streams with SQL |
| 141 | [netquack](https://duckdb.org/community_extensions/extensions/netquack.html) | [duckdb-netquack](https://github.com/hatamiarash7/duckdb-netquack) | ❓ Unknown | 2 - ✅ Active | 14 days ago (2026-04-14 08:22:12 UTC) | 37 | C++ | DuckDB extension for parsing, extracting, and analyzing domains, URIs, and pa... |
| 142 | [nsv](https://duckdb.org/community_extensions/extensions/nsv.html) | [nsv-duckdb](https://github.com/nsv-format/nsv-duckdb) | 🟢 Ongoing | 2 - ✅ Active | 26 days ago (2026-04-02 23:44:28 UTC) | 0 | C++ | A DuckDB extension for NSV processing |
| 143 | [oast](https://duckdb.org/community_extensions/extensions/oast.html) | [duckdb-oast](https://github.com/hrbrmstr/duckdb-oast) | 🟢 Ongoing | 3 - 🟡 Stable | 77 days ago (2026-02-10 12:00:32 UTC) | 4 | C | A DuckDB extension for validating, decoding, and extracting OAST (Out-of-Band... |
| 144 | [observefs](https://duckdb.org/community_extensions/extensions/observefs.html) | [duckdb-filesystem-observability](https://github.com/dentiny/duckdb-filesystem-observability) | 🟢 Ongoing | 2 - ✅ Active | 10 days ago (2026-04-19 00:32:49 UTC) | 13 | C++ | Provides observability for duckdb filesystem. |
| 145 | [ofquack](https://duckdb.org/community_extensions/extensions/ofquack.html) | [ofquack](https://github.com/krokozyab/ofquack) | ❓ Unknown | 4 - 🟠 Stale | over a year ago (2025-04-22 12:24:17 UTC) | 6 | C++ | Oracle Fusion DuckDB extension  |
| 146 | [onager](https://duckdb.org/community_extensions/extensions/onager.html) | [onager](https://github.com/CogitatorTech/onager) | 🟢 Ongoing | 2 - ✅ Active | 10 days ago (2026-04-19 06:46:24 UTC) | 128 | Rust | A DuckDB extension for graph data analytics |
| 147 | [onelake](https://duckdb.org/community_extensions/extensions/onelake.html) | [duckdb_onelake](https://github.com/datumnova/duckdb_onelake) | ❓ Unknown | 4 - 🟠 Stale | 148 days ago (2025-12-01 10:28:22 UTC) | 19 | C++ | DuckDB extension: onelake by datumnova |
| 148 | [open_prompt](https://duckdb.org/community_extensions/extensions/open_prompt.html) | [openprompt](https://github.com/Query-farm/openprompt) | 🟢 Ongoing | 3 - 🟡 Stable | 35 days ago (2026-03-24 20:13:01 UTC) | 58 | C++ | DuckDB Community Extension to prompt LLMs from SQL |
| 149 | [osmium](https://duckdb.org/community_extensions/extensions/osmium.html) | [duckdb-osmium](https://github.com/jake-low/duckdb-osmium) | 🟢 Ongoing | 2 - ✅ Active | 8 days ago (2026-04-20 15:58:54 UTC) | 14 | C++ | DuckDB extension for reading OpenStreetMap PBF files using libosmium |
| 150 | [otlp](https://duckdb.org/community_extensions/extensions/otlp.html) | [duckdb-otlp](https://github.com/smithclay/duckdb-otlp) | 🟢 Ongoing | 3 - 🟡 Stable | 50 days ago (2026-03-10 03:17:08 UTC) | 42 | C++ | query OpenTelemetry metrics, logs, and traces (OTLP) in duckdb |
| 151 | [overture](https://duckdb.org/community_extensions/extensions/overture.html) | [duckdb-overture](https://github.com/cubilica/duckdb-overture) | 🟢 Ongoing | 2 - ✅ Active | 14 days ago (2026-04-14 16:46:56 UTC) | 3 | C++ | DuckDB extension: overture by cubilica |
| 152 | [pac](https://duckdb.org/community_extensions/extensions/pac.html) | [pac](https://github.com/cwida/pac) | 🟢 Ongoing | 1 - 🔥 Very Active | 6 days ago (2026-04-22 09:09:41 UTC) | 15 | C++ | Automatic query privatization in DuckDB |
| 153 | [paimon](https://duckdb.org/community_extensions/extensions/paimon.html) | [duckdb-paimon](https://github.com/polardb/duckdb-paimon) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-04-29 05:50:27 UTC) | 25 | C++ | DuckDB extension for accessing Apache Paimon. 🦆 |
| 154 | [parser_tools](https://duckdb.org/community_extensions/extensions/parser_tools.html) | [duckdb_extension_parser_tools](https://github.com/hotdata-dev/duckdb_extension_parser_tools) | 🟢 Ongoing | 3 - 🟡 Stable | 88 days ago (2026-01-30 16:44:26 UTC) | 25 | C++ | Parse sql - with sql! |
| 155 | [pbix](https://duckdb.org/community_extensions/extensions/pbix.html) | [duckdb-pbix-extension](https://github.com/Hugoberry/duckdb-pbix-extension) | 🟢 Ongoing | 4 - 🟠 Stale | 186 days ago (2025-10-24 13:47:34 UTC) | 35 | C++ | Duckdb extension for parsing the metadata and contents of the embedded data m... |
| 156 | [pcap_reader](https://duckdb.org/community_extensions/extensions/pcap_reader.html) | [pcap](https://github.com/Query-farm/pcap) | ❓ Unknown | 3 - 🟡 Stable | 69 days ago (2026-02-18 19:49:52 UTC) | 12 | Rust | DuckDB PCAP Reader Extension made in Rust |
| 157 | [pdal](https://duckdb.org/community_extensions/extensions/pdal.html) | [duckdb-pdal](https://github.com/ahuarte47/duckdb-pdal) | 🟢 Ongoing | 2 - ✅ Active | 8 days ago (2026-04-20 22:53:12 UTC) | 25 | C++ | DuckDB extension for manipulating point cloud data using SQL |
| 158 | [pfc](https://duckdb.org/community_extensions/extensions/pfc.html) | [pfc-duckdb](https://github.com/ImpossibleForge/pfc-duckdb) | 🟢 Ongoing | 1 - 🔥 Very Active | 2 days ago (2026-04-26 10:09:19 UTC) | 1 | C++ | DuckDB extension to read PFC-JSONL compressed log files with block-level time... |
| 159 | [pivot_table](https://duckdb.org/community_extensions/extensions/pivot_table.html) | [pivot_table](https://github.com/Alex-Monahan/pivot_table) | ❓ Unknown | 2 - ✅ Active | 11 days ago (2026-04-17 15:20:58 UTC) | 18 | C++ | Full spreadsheet-style pivot table through SQL macros. Just specify values, r... |
| 160 | [plinking_duck](https://duckdb.org/community_extensions/extensions/plinking_duck.html) | [plinking_duck](https://github.com/teaguesterling/plinking_duck) | 🟢 Ongoing | 1 - 🔥 Very Active | 2 days ago (2026-04-26 16:02:34 UTC) | 2 | C++ | DuckDB tools for Plink2  |
| 161 | [poached](https://duckdb.org/community_extensions/extensions/poached.html) | [poached](https://github.com/sidequery/poached) | 🟢 Ongoing | 4 - 🟠 Stale | 123 days ago (2025-12-26 21:13:19 UTC) | 9 | C++ | A DuckDB extension that exposes SQL parsing functionality for building IDEs,... |
| 162 | [polyglot](https://duckdb.org/community_extensions/extensions/polyglot.html) | [duckdb-polyglot](https://github.com/tobilg/duckdb-polyglot) | 🟢 Ongoing | 1 - 🔥 Very Active | 5 days ago (2026-04-23 17:14:46 UTC) | 21 | Rust | Use other SQL dialects in DuckDB  |
| 163 | [prql](https://duckdb.org/community_extensions/extensions/prql.html) | [duckdb-prql](https://github.com/ywelsch/duckdb-prql) | ❓ Unknown | 4 - 🟠 Stale | 218 days ago (2025-09-22 18:45:53 UTC) | 319 | C++ | PRQL as a DuckDB extension |
| 164 | [psql](https://duckdb.org/community_extensions/extensions/psql.html) | [duckdb-psql](https://github.com/ywelsch/duckdb-psql) | 🟢 Ongoing | 2 - ✅ Active | 14 days ago (2026-04-14 18:55:40 UTC) | 104 | C++ | A piped SQL for DuckDB |
| 165 | [pst](https://duckdb.org/community_extensions/extensions/pst.html) | [duckdb-pst](https://github.com/intellekthq/duckdb-pst) | 🟢 Ongoing | 2 - ✅ Active | 14 days ago (2026-04-14 16:18:53 UTC) | 10 | C++ | In-place querying of Microsoft PST files, directly from storage, with SQL. |
| 166 | [psyduck](https://duckdb.org/community_extensions/extensions/psyduck.html) | [psyduck](https://github.com/Ian-Fogelman/psyduck) | 🟢 Ongoing | 4 - 🟠 Stale | 135 days ago (2025-12-14 15:10:39 UTC) | 7 | C++ | Pysduck a DuckDB community extension about Pokémon. |
| 167 | [pyroscope](https://duckdb.org/community_extensions/extensions/pyroscope.html) | [pyroscope](https://github.com/Query-farm/pyroscope) | ❓ Unknown | 3 - 🟡 Stable | 69 days ago (2026-02-18 19:49:53 UTC) | 21 | Rust | DuckDB Pyroscope Extension for Continuous Profiling |
| 168 | [quack](https://duckdb.org/community_extensions/extensions/quack.html) | [extension-template](https://github.com/duckdb/extension-template) | ❓ Unknown | 1 - 🔥 Very Active | 4 days ago (2026-04-24 13:49:56 UTC) | 272 | Python | Template for DuckDB extensions to help you develop, test and deploy a custom... |
| 169 | [quackfix](https://duckdb.org/community_extensions/extensions/quackfix.html) | [QuackFIX](https://github.com/hyehudai/QuackFIX) | ❓ Unknown | 4 - 🟠 Stale | 124 days ago (2025-12-25 10:36:24 UTC) | 16 | C++ | Fix log extension for duckdb |
| 170 | [quackformers](https://duckdb.org/community_extensions/extensions/quackformers.html) | [quackformers](https://github.com/martin-conur/quackformers) | ❓ Unknown | 4 - 🟠 Stale | 128 days ago (2025-12-21 18:43:16 UTC) | 12 | Rust | DuckDB NLP extension. |
| 171 | [quackstats](https://duckdb.org/community_extensions/extensions/quackstats.html) | [quackstats](https://github.com/jasadams/quackstats) | ❓ Unknown | 3 - 🟡 Stable | 86 days ago (2026-02-01 12:01:35 UTC) | 2 | Rust | DuckDB extension for time series forecasting and seasonality detection |
| 172 | [quackstore](https://duckdb.org/community_extensions/extensions/quackstore.html) | [QuackStore](https://github.com/coginiti-dev/QuackStore) | ❓ Unknown | 4 - 🟠 Stale | 91 days ago (2026-01-27 15:27:17 UTC) | 111 | C++ | DuckDB extension: quackstore by coginiti-dev |
| 173 | [query_condition_cache](https://duckdb.org/community_extensions/extensions/query_condition_cache.html) | [duckdb-query-condition-cache](https://github.com/dentiny/duckdb-query-condition-cache) | 🟢 Ongoing | 1 - 🔥 Very Active | 6 days ago (2026-04-22 17:01:27 UTC) | 6 | C++ | DuckDB extension: query_condition_cache by dentiny |
| 174 | [quickjs](https://duckdb.org/community_extensions/extensions/quickjs.html) | [quickjs](https://github.com/Query-farm/quickjs) | 🟢 Ongoing | 2 - ✅ Active | 30 days ago (2026-03-29 21:04:47 UTC) | 11 | C++ | DuckDB extension: quickjs by quackscience |
| 175 | [radio](https://duckdb.org/community_extensions/extensions/radio.html) | [radio](https://github.com/Query-farm/radio) | 🟢 Ongoing | 2 - ✅ Active | 30 days ago (2026-03-29 21:04:47 UTC) | 37 | C++ | Radio is a DuckDB extension by Query.Farm that brings real-time event streams... |
| 176 | [rapidfuzz](https://duckdb.org/community_extensions/extensions/rapidfuzz.html) | [rapidfuzz](https://github.com/Query-farm/rapidfuzz) | 🟢 Ongoing | 2 - ✅ Active | 30 days ago (2026-03-29 21:04:48 UTC) | 15 | C++ | DuckDB Community Extension adding RapidFuzz algorithms for search, deduplicat... |
| 177 | [raquet](https://duckdb.org/community_extensions/extensions/raquet.html) | [duckdb-raquet](https://github.com/jatorre/duckdb-raquet) | 🟢 Ongoing | 2 - ✅ Active | 12 days ago (2026-04-16 12:13:31 UTC) | 10 | C++ | DuckDB extension for reading Raquet format (raster data in Parquet with QUADB... |
| 178 | [raster](https://duckdb.org/community_extensions/extensions/raster.html) | [duckdb-raster](https://github.com/ahuarte47/duckdb-raster) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-04-29 00:35:01 UTC) | 34 | C++ | DuckDB Extension for reading and writing raster files using SQL. |
| 179 | [rate_limit_fs](https://duckdb.org/community_extensions/extensions/rate_limit_fs.html) | [duckdb-rate-limit-filesystem](https://github.com/dentiny/duckdb-rate-limit-filesystem) | 🟢 Ongoing | 2 - ✅ Active | 11 days ago (2026-04-17 09:06:38 UTC) | 1 | C++ | DuckDB extension: rate_limit_fs by dentiny |
| 180 | [rdf](https://duckdb.org/community_extensions/extensions/rdf.html) | [duck_rdf](https://github.com/nonodename/duck_rdf) | 🟢 Ongoing | 2 - ✅ Active | 19 days ago (2026-04-09 15:52:28 UTC) | 18 | C++ | RDF file extension for DuckDB. Reads and writes supported |
| 181 | [read_dbf](https://duckdb.org/community_extensions/extensions/read_dbf.html) | [duckdb-dbf](https://github.com/tocharan/duckdb-dbf) | 🟢 Ongoing | 3 - 🟡 Stable | 62 days ago (2026-02-25 17:13:20 UTC) | 2 | C++ | Database connectivity extension by tocharan |
| 182 | [read_lines](https://duckdb.org/community_extensions/extensions/read_lines.html) | [duckdb_read_lines](https://github.com/teaguesterling/duckdb_read_lines) | 🟢 Ongoing | 3 - 🟡 Stable | 38 days ago (2026-03-21 19:27:06 UTC) | 3 | C++ | Simple parsers for fast extraction from line-based files  |
| 183 | [read_stat](https://duckdb.org/community_extensions/extensions/read_stat.html) | [duckdb-read-stat](https://github.com/dylanmeysmans/duckdb-read-stat) | 🟢 Ongoing | 4 - 🟠 Stale | 152 days ago (2025-11-27 13:46:07 UTC) | 30 | C | Read data sets from SAS, Stata, and SPSS from DuckDB with ReadStat |
| 184 | [redis](https://duckdb.org/community_extensions/extensions/redis.html) | [redis](https://github.com/Query-farm/redis) | 🟢 Ongoing | 2 - ✅ Active | 30 days ago (2026-03-29 21:04:49 UTC) | 12 | C++ | DuckDB Redis Client community extension |
| 185 | [rusty_quack](https://duckdb.org/community_extensions/extensions/rusty_quack.html) | [extension-template-rs](https://github.com/duckdb/extension-template-rs) | ❓ Unknown | 2 - ✅ Active | 14 days ago (2026-04-14 09:37:53 UTC) | 102 | Rust | (Experimental) Template for Rust-based DuckDB extensions |
| 186 | [rusty_sheet](https://duckdb.org/community_extensions/extensions/rusty_sheet.html) | [rusty-sheet](https://github.com/redraiment/rusty-sheet) | 🟢 Ongoing | 3 - 🟡 Stable | 75 days ago (2026-02-13 02:27:56 UTC) | 69 | Rust | An Excel/WPS/OpenDocument Spreadsheets file reader for DuckDB |
| 187 | [sazgar](https://duckdb.org/community_extensions/extensions/sazgar.html) | [Sazgar](https://github.com/Angelerator/Sazgar) | ❓ Unknown | 3 - 🟡 Stable | 38 days ago (2026-03-22 04:21:55 UTC) | 13 | HTML | DuckDB extension for system monitoring & intelligent SQL routing. 25+ functio... |
| 188 | [scalarfs](https://duckdb.org/community_extensions/extensions/scalarfs.html) | [duckdb_scalarfs](https://github.com/teaguesterling/duckdb_scalarfs) | 🟢 Ongoing | 2 - ✅ Active | 17 days ago (2026-04-11 16:49:55 UTC) | 7 | C++ | A collection of simple virtual filesystems for treating scalar values as files. |
| 189 | [scrooge](https://duckdb.org/community_extensions/extensions/scrooge.html) | [Scrooge-McDuck](https://github.com/pdet/Scrooge-McDuck) | 🟢 Ongoing | 2 - ✅ Active | 30 days ago (2026-03-29 11:06:41 UTC) | 159 | C++ | DuckDB extension: scrooge by pdet |
| 190 | [se3](https://duckdb.org/community_extensions/extensions/se3.html) | [se3](https://github.com/jokasimr/se3) | 🟢 Ongoing | 3 - 🟡 Stable | 51 days ago (2026-03-08 13:32:27 UTC) | 0 | C++ | Duckdb extension for efficient rotation / translation operations on points in... |
| 191 | [semantic_views](https://duckdb.org/community_extensions/extensions/semantic_views.html) | [duckdb-semantic-views](https://github.com/anentropic/duckdb-semantic-views) | 🟢 Ongoing | 1 - 🔥 Very Active | 2 days ago (2026-04-26 20:40:21 UTC) | 4 | Rust | Semantic Views for DuckDB. |
| 192 | [sheetreader](https://duckdb.org/community_extensions/extensions/sheetreader.html) | [sheetreader-duckdb](https://github.com/polydbms/sheetreader-duckdb) | 🟢 Ongoing | 3 - 🟡 Stable | 44 days ago (2026-03-15 11:03:07 UTC) | 56 | C++ | DuckDB extension: sheetreader by polydbms |
| 193 | [shellfs](https://duckdb.org/community_extensions/extensions/shellfs.html) | [shellfs](https://github.com/Query-farm/shellfs) | 🟢 Ongoing | 2 - ✅ Active | 30 days ago (2026-03-29 21:04:50 UTC) | 92 | C++ | DuckDB extension allowing shell commands to be used for input and output. |
| 194 | [sistat](https://duckdb.org/community_extensions/extensions/sistat.html) | [duckdb-sistat](https://github.com/fklezin/duckdb-sistat) | 🟢 Ongoing | 3 - 🟡 Stable | 50 days ago (2026-03-09 09:09:46 UTC) | 2 | C++ | DuckDB extension to query Slovenia's SiStat open data directly using SQL. No... |
| 195 | [sitemap](https://duckdb.org/community_extensions/extensions/sitemap.html) | [duckdb-sitemap](https://github.com/midwork-finds-jobs/duckdb-sitemap) | 🟢 Ongoing | 3 - 🟡 Stable | 70 days ago (2026-02-17 14:13:12 UTC) | 1 | C++ | DuckDB extension for parsing XML sitemaps from websites |
| 196 | [sitting_duck](https://duckdb.org/community_extensions/extensions/sitting_duck.html) | [sitting_duck](https://github.com/teaguesterling/sitting_duck) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-04-27 13:00:14 UTC) | 13 | C | DuckDB extension: sitting_duck by teaguesterling |
| 197 | [slack](https://github.com/dentiny/duckdb-slack) | [duckdb-slack](https://github.com/dentiny/duckdb-slack) | ❓ Unknown | 3 - 🟡 Stable | 68 days ago (2026-02-19 18:08:54 UTC) | 0 | C++ | DuckDB extension: slack by dentiny |
| 198 | [snowflake](https://duckdb.org/community_extensions/extensions/snowflake.html) | [duckdb-snowflake](https://github.com/iqea-ai/duckdb-snowflake) | 🟢 Ongoing | 2 - ✅ Active | 8 days ago (2026-04-20 22:54:50 UTC) | 50 | C++ | A powerful DuckDB extension that enables seamless querying of Snowflake datab... |
| 199 | [splink_udfs](https://duckdb.org/community_extensions/extensions/splink_udfs.html) | [splink_udfs](https://github.com/moj-analytical-services/splink_udfs) | ❓ Unknown | 3 - 🟡 Stable | 81 days ago (2026-02-06 11:01:11 UTC) | 17 | C++ | DuckDB extension: splink_udfs by moj-analytical-services |
| 200 | [spxlsx](https://duckdb.org/community_extensions/extensions/spxlsx.html) | [spxlsx](https://github.com/paulmupeters/spxlsx) | 🟢 Ongoing | 2 - ✅ Active | 13 days ago (2026-04-15 12:15:43 UTC) | 0 | C++ | Duckdb extension to read sharepoint lists and excel |
| 201 | [sshfs](https://duckdb.org/community_extensions/extensions/sshfs.html) | [duckdb-sshfs](https://github.com/midwork-finds-jobs/duckdb-sshfs) | 🟢 Ongoing | 1 - 🔥 Very Active | 3 days ago (2026-04-25 19:02:39 UTC) | 10 | C++ | DuckDB sshfs extension - Read and write files through ssh inside DuckDB |
| 202 | [st_read_multi](https://duckdb.org/community_extensions/extensions/st_read_multi.html) | [duckdb-ext-st-read-multi](https://github.com/yutannihilation/duckdb-ext-st-read-multi) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-04-29 00:31:35 UTC) | 9 | Rust | A DuckDB extension to import multiple geospatial files with `ST_Read_Multi()` |
| 203 | [stochastic](https://duckdb.org/community_extensions/extensions/stochastic.html) | [stochastic](https://github.com/Query-farm/stochastic) | 🟢 Ongoing | 2 - ✅ Active | 30 days ago (2026-03-29 21:05:21 UTC) | 19 | C++ | A DuckDB extension that add comprehensive statistical distribution functions... |
| 204 | [substrait](https://duckdb.org/community_extensions/extensions/substrait.html) | [duckdb-substrait-extension](https://github.com/substrait-io/duckdb-substrait-extension) | ❓ Unknown | 3 - 🟡 Stable | 75 days ago (2026-02-12 15:49:24 UTC) | 60 | C++ | DuckDB extension: substrait by substrait-io |
| 205 | [sudan](https://duckdb.org/community_extensions/extensions/sudan.html) | [duckdb-sudan-](https://github.com/Osman-Geomatics93/duckdb-sudan-) | 🟢 Ongoing | 3 - 🟡 Stable | 68 days ago (2026-02-19 11:49:28 UTC) | 0 | Jupyter Notebook | DuckDB extension: sudan by Osman-Geomatics93 |
| 206 | [system_stats](https://duckdb.org/community_extensions/extensions/system_stats.html) | [system_stats](https://github.com/dentiny/system_stats) | 🟢 Ongoing | 2 - ✅ Active | 10 days ago (2026-04-18 23:05:24 UTC) | 2 | C++ | DuckDB extension: system_stats by dentiny |
| 207 | [table_inspector](https://duckdb.org/community_extensions/extensions/table_inspector.html) | [duckdb-table-inspector](https://github.com/dentiny/duckdb-table-inspector) | 🟢 Ongoing | 2 - ✅ Active | 10 days ago (2026-04-19 01:47:23 UTC) | 0 | C++ | DuckDB extension: table_inspector by dentiny |
| 208 | [talib](https://duckdb.org/community_extensions/extensions/talib.html) | [atm_talib](https://github.com/neuesql/atm_talib) | 🟢 Ongoing | 2 - ✅ Active | 8 days ago (2026-04-21 06:06:51 UTC) | 2 | C++ | A duckdb TA-Lib to add technical analysis with SQL easily |
| 209 | [tarfs](https://duckdb.org/community_extensions/extensions/tarfs.html) | [duckdb_tarfs](https://github.com/Maxxen/duckdb_tarfs) | ❓ Unknown | 4 - 🟠 Stale | over a year ago (2024-08-26 11:01:47 UTC) | 12 | C++ | DuckDB extension: tarfs by Maxxen |
| 210 | [tera](https://duckdb.org/community_extensions/extensions/tera.html) | [tera](https://github.com/Query-farm/tera) | 🟢 Ongoing | 2 - ✅ Active | 30 days ago (2026-03-29 21:04:51 UTC) | 8 | C++ | DuckDB extension: tera |
| 211 | [textplot](https://duckdb.org/community_extensions/extensions/textplot.html) | [textplot](https://github.com/Query-farm/textplot) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-04-27 17:31:59 UTC) | 23 | C++ | A DuckDB community extension that enables text-based data visualization direc... |
| 212 | [title_mapper](https://duckdb.org/community_extensions/extensions/title_mapper.html) | [duckdb-title-mapper](https://github.com/martin-conur/duckdb-title-mapper) | ❓ Unknown | 4 - 🟠 Stale | 198 days ago (2025-10-12 22:54:26 UTC) | 2 | Rust | DuckDB extension: title_mapper by martin-conur |
| 213 | [tributary](https://duckdb.org/community_extensions/extensions/tributary.html) | [tributary](https://github.com/Query-farm/tributary) | ❓ Unknown | 2 - ✅ Active | 30 days ago (2026-03-29 21:04:53 UTC) | 55 | C++ | A DuckDB Extension for Kafka |
| 214 | [tsid](https://duckdb.org/community_extensions/extensions/tsid.html) | [tsid](https://github.com/Query-farm/tsid) | 🟢 Ongoing | 2 - ✅ Active | 30 days ago (2026-03-29 21:04:54 UTC) | 6 | C++ | TSID Extension for DuckDB  |
| 215 | [ulid](https://duckdb.org/community_extensions/extensions/ulid.html) | ~~[duckdb_ulid](https://github.com/Maxxen/duckdb_ulid)~~ **NOT FOUND:** https://github.com/Maxxen/duckdb_ulid (Request timeout) | ❓ Unknown | 4 - 🟠 Stale | over a year ago (2024-07-09 09:35:50 UTC) | 25 | C++ | DuckDB extension: ulid by Maxxen |
| 216 | [urlpattern](https://duckdb.org/community_extensions/extensions/urlpattern.html) | [duckdb_urlpattern](https://github.com/teaguesterling/duckdb_urlpattern) | ❓ Unknown | 3 - 🟡 Stable | 64 days ago (2026-02-24 00:52:19 UTC) | 2 | C++ | An implementation of URLPattern for DuckDB |
| 217 | [us_address_standardizer](https://duckdb.org/community_extensions/extensions/us_address_standardizer.html) | [duckdb-address-standardizer](https://github.com/ericmanning/duckdb-address-standardizer) | 🟢 Ongoing | 2 - ✅ Active | 8 days ago (2026-04-20 14:07:41 UTC) | 2 | C | DuckDB extension for parsing and standardizing (USA) postal addresses using P... |
| 218 | [valhalla_routing](https://duckdb.org/community_extensions/extensions/valhalla_routing.html) | [duckdb-valhalla-routing](https://github.com/midwork-finds-jobs/duckdb-valhalla-routing) | 🟢 Ongoing | 3 - 🟡 Stable | 70 days ago (2026-02-17 11:36:12 UTC) | 5 | Makefile | WIP: Attempt to package valhalla routing engine to duckdb |
| 219 | [warc](https://duckdb.org/community_extensions/extensions/warc.html) | [duckdb_warc](https://github.com/midwork-finds-jobs/duckdb_warc) | ❓ Unknown | 3 - 🟡 Stable | 82 days ago (2026-02-05 15:33:27 UTC) | 4 | Rust | DuckDB extension for parsing WARC files |
| 220 | [web_archive](https://duckdb.org/community_extensions/extensions/web_archive.html) | [duckdb-web-archive](https://github.com/midwork-finds-jobs/duckdb-web-archive) | 🟢 Ongoing | 3 - 🟡 Stable | 84 days ago (2026-02-03 08:28:03 UTC) | 19 | C++ | DuckDB extension to fetch pages from Wayback Machine & Common Crawl |
| 221 | [web_search](https://duckdb.org/community_extensions/extensions/web_search.html) | [duckdb-web-search](https://github.com/midwork-finds-jobs/duckdb-web-search) | 🟢 Ongoing | 2 - ✅ Active | 8 days ago (2026-04-20 21:51:13 UTC) | 0 | C++ | Web/HTTP functionality extension by midwork-finds-jobs |
| 222 | [webbed](https://duckdb.org/community_extensions/extensions/webbed.html) | [duckdb_webbed](https://github.com/teaguesterling/duckdb_webbed) | 🟢 Ongoing | 2 - ✅ Active | 30 days ago (2026-03-29 23:35:19 UTC) | 49 | C++ | Web/HTTP functionality extension by teaguesterling |
| 223 | [webdavfs](https://duckdb.org/community_extensions/extensions/webdavfs.html) | [duckdb-webdavfs](https://github.com/midwork-finds-jobs/duckdb-webdavfs) | ❓ Unknown | 1 - 🔥 Very Active | 4 days ago (2026-04-25 03:42:47 UTC) | 1 | C++ | DuckDB WebDAVfs Extension - WebDAV filesystem support for DuckDB |
| 224 | [webmacro](https://duckdb.org/community_extensions/extensions/webmacro.html) | [webmacro](https://github.com/Query-farm/webmacro) | ❓ Unknown | 3 - 🟡 Stable | 35 days ago (2026-03-24 20:13:18 UTC) | 15 | C++ | DuckDB WebMacro: Share and Load your SQL Macros via gists |
| 225 | [whisper](https://duckdb.org/community_extensions/extensions/whisper.html) | [duckdb-whisper](https://github.com/tobilg/duckdb-whisper) | 🟢 Ongoing | 1 - 🔥 Very Active | 5 days ago (2026-04-24 06:11:20 UTC) | 10 | C++ | Use whisper.cpp within DuckDB to translate / transpile speech to text |
| 226 | [wireduck](https://duckdb.org/community_extensions/extensions/wireduck.html) | [wireduck](https://github.com/hyehudai/wireduck) | 🟢 Ongoing | 4 - 🟠 Stale | 217 days ago (2025-09-23 21:22:03 UTC) | 48 | C++ | Duckdb extension to read pcap files |
| 227 | [yaml](https://duckdb.org/community_extensions/extensions/yaml.html) | [duckdb_yaml](https://github.com/teaguesterling/duckdb_yaml) | 🟢 Ongoing | 3 - 🟡 Stable | 62 days ago (2026-02-26 00:17:07 UTC) | 15 | C++ |  A DuckDB to read and work with YAML files in a similar way to JSON files (al... |
| 228 | [yardstick](https://duckdb.org/community_extensions/extensions/yardstick.html) | [yardstick](https://github.com/sidequery/yardstick) | 🟢 Ongoing | 2 - ✅ Active | 13 days ago (2026-04-15 13:05:59 UTC) | 49 | Rust | An implementation of Measures in SQL as a DuckDB extension |
| 229 | [zeek](https://duckdb.org/community_extensions/extensions/zeek.html) | [zeek-duckdb](https://github.com/ynadji/zeek-duckdb) | 🟢 Ongoing | 2 - ✅ Active | 14 days ago (2026-04-14 22:02:22 UTC) | 2 | C++ | read_zeek table function to read Zeek TSV logs into DuckDB |
| 230 | [zipfs](https://duckdb.org/community_extensions/extensions/zipfs.html) | [duckdb-zipfs](https://github.com/isaacbrodsky/duckdb-zipfs) | 🟢 Ongoing | 1 - 🔥 Very Active | 2 days ago (2026-04-26 20:42:31 UTC) | 61 | C++ | DuckDB extension to read files within zip archives. |

</details>
## Appendix: DuckDB Release Information

### Current Release Context

DuckDB follows **semantic versioning** with regular releases. For complete and up-to-date release information, see the official [**DuckDB Release Calendar**](https://duckdb.org/release_calendar.html).

### Release History

| Version | Release Date | Codename | Named After | LTS | Status |
|---------|--------------|----------|-------------|-----|--------|
| **v1.5.3** 📅 | 2026-05-18 | – | – |  | Planned |
| **v1.5.2** | 2026-04-13 | – | – |  | Active |
| **v1.5.1** | 2026-03-23 | – | – |  | Active |
| **v1.5.0** | 2026-03-09 | Variegata | *Paradise shelduck* |  | Active |
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

<p class="fine-print">Last updated: 2026-04-29</p>
