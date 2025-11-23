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
- **Repository**: [duckdb/duckdb](https://github.com/duckdb/duckdb)
- **Releases**: [GitHub Releases](https://github.com/duckdb/duckdb/releases)

**Community Extensions**

- **Registry**: [Community Extensions Repository](https://github.com/duckdb/community-extensions)
- **Directory**: [Extensions Folder](https://github.com/duckdb/community-extensions/tree/main/extensions)
- **Featured**: [Community Extensions Page](https://community-extensions.duckdb.org/)
- **Individual Repositories**: GitHub repositories linked in the extensions directory

---
## Summary

| **Metric** | **Count** |
|------------|-----------|
| **Core Extensions** | 25 |
| **Community Extensions** | 116 |
| **Total Extensions** | 141 |
| **Recently Active** (≤ 30 days) | 52 |
| **Very Active** (≤ 7 days) | 26 |


---
## Core Extensions

Core extensions maintained by the DuckDB team and distributed via the official extension repository

| # | Extension | Repository | Status | Last Activity | Stars | Language | Description |
|---|-----------|------------|--------|---------------|-------|----------|-------------|
| 1 | [autocomplete](https://duckdb.org/docs/stable/core_extensions/autocomplete.html) | [duckdb/duckdb](https://github.com/duckdb/duckdb/tree/main/extension/autocomplete) | 🟢 Ongoing | 3 days ago (2025-11-19 07:18:05 UTC) | N/A (part of core DuckDB repo) | C++ | Core DuckDB extension: autocomplete |
| 2 | [avro](https://duckdb.org/docs/stable/core_extensions/avro.html) | [duckdb-avro](https://github.com/duckdb/duckdb-avro) | 🟢 Ongoing | 47 days ago (2025-10-06 15:40:15 UTC) | 29 | C++ | Apache Avro format support |
| 3 | [aws](https://duckdb.org/docs/stable/core_extensions/aws.html) | [duckdb-aws](https://github.com/duckdb/duckdb-aws) | 🟢 Ongoing | 51 days ago (2025-10-02 10:50:00 UTC) | 56 | C++ | AWS S3 integration |
| 4 | [azure](https://duckdb.org/docs/stable/core_extensions/azure.html) | [duckdb-azure](https://github.com/duckdb/duckdb-azure) | 🟢 Ongoing | 5 days ago (2025-11-17 15:14:52 UTC) | 67 | C++ | Azure extension for DuckDB |
| 5 | [delta](https://duckdb.org/docs/stable/core_extensions/delta.html) | [duckdb-delta](https://github.com/duckdb/duckdb-delta) | 🟢 Ongoing | 30 days ago (2025-10-23 16:36:38 UTC) | 203 | C++ | DuckDB extension for Delta Lake |
| 6 | [ducklake](https://duckdb.org/docs/stable/core_extensions/ducklake.html) | [duckdb/ducklake](https://github.com/duckdb/ducklake) | 🟢 Ongoing | 10 days ago | N/A (part of core DuckDB repo) | C++ | Delta Lake support via DuckLake (different from delta extension) |
| 7 | [encodings](https://duckdb.org/docs/stable/core_extensions/encodings.html) | [duckdb-encodings](https://github.com/duckdb/duckdb-encodings) | 🟢 Ongoing | 66 days ago (2025-09-17 12:57:45 UTC) | 16 | C++ | Character encoding support |
| 8 | [excel](https://duckdb.org/docs/stable/core_extensions/excel.html) | [duckdb-excel](https://github.com/duckdb/duckdb-excel) | 🟢 Ongoing | 80 days ago (2025-09-03 21:31:45 UTC) | 45 | C++ | Excel extension for DuckDB |
| 9 | [fts](https://duckdb.org/docs/stable/core_extensions/full_text_search.html) | [duckdb-fts](https://github.com/duckdb/duckdb-fts) | 🟢 Ongoing | 67 days ago (2025-09-16 14:12:43 UTC) | 28 | C++ | Full-text search functionality |
| 10 | [httpfs](https://duckdb.org/docs/stable/core_extensions/httpfs/overview.html) | [duckdb-httpfs](https://github.com/duckdb/duckdb-httpfs) | 🟢 Ongoing | 9 days ago (2025-11-13 15:11:45 UTC) | 36 | C++ | HTTP/S3 filesystem support |
| 11 | [iceberg](https://duckdb.org/docs/stable/core_extensions/iceberg/overview.html) | [duckdb-iceberg](https://github.com/duckdb/duckdb-iceberg) | 🟢 Ongoing | 2 days ago (2025-11-20 14:04:30 UTC) | 340 | C++ | Apache Iceberg format support |
| 12 | [icu](https://duckdb.org/docs/stable/core_extensions/icu.html) | [duckdb/duckdb](https://github.com/duckdb/duckdb/tree/main/extension/icu) | 🟢 Ongoing | 15 days ago (2025-11-07 07:45:29 UTC) | N/A (part of core DuckDB repo) | C++ | Core DuckDB extension: icu |
| 13 | [inet](https://duckdb.org/docs/stable/core_extensions/inet.html) | [duckdb-inet](https://github.com/duckdb/duckdb-inet) | 🟢 Ongoing | 2 days ago (2025-11-20 22:54:12 UTC) | 14 | C++ | Internet address data types |
| 14 | [jemalloc](https://duckdb.org/docs/stable/core_extensions/jemalloc.html) | [duckdb/duckdb](https://github.com/duckdb/duckdb/tree/main/extension/jemalloc) | 🟢 Ongoing | 168 days ago (2025-06-07 09:38:02 UTC) | N/A (part of core DuckDB repo) | C++ | Core DuckDB extension: jemalloc |
| 15 | [json](https://duckdb.org/docs/stable/data/json/overview.html) | [duckdb/duckdb](https://github.com/duckdb/duckdb/tree/main/extension/json) | 🟢 Ongoing | 19 days ago (2025-11-03 21:43:54 UTC) | N/A (part of core DuckDB repo) | C++ | Core DuckDB extension: json |
| 16 | [mysql](https://duckdb.org/docs/stable/core_extensions/mysql.html) | [duckdb-mysql](https://github.com/duckdb/duckdb-mysql) | 🟢 Ongoing | 3 days ago (2025-11-19 10:25:23 UTC) | 83 | C++ | MySQL database connectivity |
| 17 | [parquet](https://duckdb.org/docs/stable/data/parquet/overview.html) | [duckdb/duckdb](https://github.com/duckdb/duckdb/tree/main/extension/parquet) | 🟢 Ongoing | 4 days ago (2025-11-18 19:40:38 UTC) | N/A (part of core DuckDB repo) | C++ | Core DuckDB extension: parquet |
| 18 | [postgres](https://duckdb.org/docs/stable/core_extensions/postgres.html) | [duckdb-postgres](https://github.com/duckdb/duckdb-postgres) | 🟢 Ongoing | 12 days ago (2025-11-10 20:30:45 UTC) | 321 | C++ | PostgreSQL database connectivity |
| 19 | [spatial](https://duckdb.org/docs/stable/core_extensions/spatial/overview.html) | [duckdb-spatial](https://github.com/duckdb/duckdb-spatial) | 🟢 Ongoing | 21 days ago (2025-11-01 18:27:03 UTC) | 641 | C++ | Geospatial data types and functions |
| 20 | [sqlite](https://duckdb.org/docs/stable/core_extensions/sqlite.html) | [duckdb-sqlite](https://github.com/duckdb/duckdb-sqlite) | 🟢 Ongoing | 55 days ago (2025-09-28 07:21:39 UTC) | 258 | C++ | DuckDB extension to read and write to SQLite databases |
| 21 | [tpcds](https://duckdb.org/docs/stable/core_extensions/tpcds.html) | [duckdb/duckdb](https://github.com/duckdb/duckdb/tree/main/extension/tpcds) | 🟢 Ongoing | 109 days ago (2025-08-05 13:26:52 UTC) | N/A (part of core DuckDB repo) | C++ | Core DuckDB extension: tpcds |
| 22 | [tpch](https://duckdb.org/docs/stable/core_extensions/tpch.html) | [duckdb/duckdb](https://github.com/duckdb/duckdb/tree/main/extension/tpch) | 🟢 Ongoing | 109 days ago (2025-08-05 13:26:52 UTC) | N/A (part of core DuckDB repo) | C++ | Core DuckDB extension: tpch |
| 23 | [ui](https://duckdb.org/docs/stable/core_extensions/ui.html) | [duckdb-ui](https://github.com/duckdb/duckdb-ui) | 🟢 Ongoing | 10 days ago (2025-11-12 17:24:09 UTC) | 381 | C++ | Browser-based user interface for DuckDB |
| 24 | [vortex](https://duckdb.org/docs/stable/core_extensions/vortex.html) | ~~[vortex](https://github.com/duckdb/duckdb/extensions/vortex)~~ **NOT FOUND:** https://github.com/duckdb/duckdb/extensions/vortex (HTTP 404) | 🟢 Ongoing | 10 days ago | N/A (part of core DuckDB repo) | C++ | Core DuckDB extension: vortex |
| 25 | [vss](https://duckdb.org/docs/stable/core_extensions/vss.html) | [duckdb-vss](https://github.com/duckdb/duckdb-vss) | 🟢 Ongoing | 78 days ago (2025-09-05 07:04:02 UTC) | 225 | C++ | Vector similarity search |

**Total:** 25 extensions

---
---
## Community Extensions

Third-party extensions maintained by the community

| # | Extension | Repository | Status | Last Activity | Stars | Language | Description |
|---|-----------|------------|--------|---------------|-------|----------|-------------|
| 1 | [anofox_statistics](https://duckdb.org/community_extensions/extensions/anofox_statistics.html) | [anofox-statistics](https://github.com/DataZooDE/anofox-statistics) | 🟢 Ongoing | today (2025-11-22 23:19:14 UTC) | 4 | C++ | A DuckDB extension for statistical regression analysis, providing OLS, Ridge,... |
| 2 | [infera](https://duckdb.org/community_extensions/extensions/infera.html) | [infera](https://github.com/CogitatorTech/infera) | ❓ Unknown | today (2025-11-22 19:34:31 UTC) | 101 | Rust | A DuckDB extension for in-database inference |
| 3 | [quack](https://duckdb.org/community_extensions/extensions/quack.html) | [extension-template](https://github.com/duckdb/extension-template) | ❓ Unknown | today (2025-11-22 08:39:56 UTC) | 241 | Python | Template for DuckDB extensions to help you develop, test and deploy a custom... |
| 4 | [anofox_forecast](https://duckdb.org/community_extensions/extensions/anofox_forecast.html) | [anofox-forecast](https://github.com/DataZooDE/anofox-forecast) | 🟢 Ongoing | today (2025-11-21 06:43:25 UTC) | 13 | C++ | Statistical timeseries forecasting in DuckDB |
| 5 | [anofox_tabular](https://github.com/DataZooDE/anofox-tabular) | [anofox-tabular](https://github.com/DataZooDE/anofox-tabular) | ❓ Unknown | today (2025-11-21 10:27:44 UTC) | 2 | C++ | A duckdb extension which combines data quality and data preparation tools for... |
| 6 | [boilstream](https://duckdb.org/community_extensions/extensions/boilstream.html) | [boilstream-extension](https://github.com/dforsber/boilstream-extension) | 🟢 Ongoing | today (2025-11-21 12:37:02 UTC) | 1 | JavaScript | Secure Remote Secrets Storage for DuckDB |
| 7 | [capi_quack](https://duckdb.org/community_extensions/extensions/capi_quack.html) | [extension-template-c](https://github.com/duckdb/extension-template-c) | ❓ Unknown | today (2025-11-21 13:20:44 UTC) | 22 | C | (Experimental) C/C++ template for DuckDB extensions based on the C API |
| 8 | [duckherder](https://duckdb.org/community_extensions/extensions/duckherder.html) | [duckdb-distributed-execution](https://github.com/dentiny/duckdb-distributed-execution) | 🟢 Ongoing | today (2025-11-21 10:23:16 UTC) | 25 | C++ | Distributed execution for duckdb queries. |
| 9 | [gcs](https://duckdb.org/community_extensions/extensions/gcs.html) | [duckdb-gcs](https://github.com/northpolesec/duckdb-gcs) | 🟢 Ongoing | today (2025-11-21 22:12:26 UTC) | 4 | C++ | A GCS-native extension for DuckDB |
| 10 | [mlpack](https://duckdb.org/community_extensions/extensions/mlpack.html) | [duckdb-mlpack](https://github.com/eddelbuettel/duckdb-mlpack) | 🟢 Ongoing | today (2025-11-21 13:38:04 UTC) | 6 | CMake | Bringing mlpack to duckdb |
| 11 | [nanodbc](https://duckdb.org/community_extensions/extensions/nanodbc.html) | [duckdb-nanodbc-extension](https://github.com/Hugoberry/duckdb-nanodbc-extension) | 🟡 Archived | today (2025-11-21 17:39:58 UTC) | 46 | C++ | Database connectivity extension by Hugoberry |
| 12 | [onelake](https://duckdb.org/community_extensions/extensions/onelake.html) | [duckdb_onelake](https://github.com/datumnova/duckdb_onelake) | 🟢 Ongoing | today (2025-11-21 15:27:21 UTC) | 18 | C++ | DuckDB extension: onelake by datumnova |
| 13 | [sheetreader](https://duckdb.org/community_extensions/extensions/sheetreader.html) | [sheetreader-duckdb](https://github.com/polydbms/sheetreader-duckdb) | ❓ Unknown | today (2025-11-21 16:20:04 UTC) | 55 | Jupyter Notebook | DuckDB extension: sheetreader by polydbms |
| 14 | [psyduck](https://duckdb.org/community_extensions/extensions/psyduck.html) | [psyduck](https://github.com/Ian-Fogelman/psyduck) | 🟢 Ongoing | 2 days ago (2025-11-21 04:57:02 UTC) | 4 | C++ | Pysduck a DuckDB community extension about Pokémon. |
| 15 | [rusty_sheet](https://duckdb.org/community_extensions/extensions/rusty_sheet.html) | [rusty-sheet](https://github.com/redraiment/rusty-sheet) | 🟢 Ongoing | 2 days ago (2025-11-21 02:23:01 UTC) | 49 | Rust | An Excel/WPS/OpenDocument Spreadsheets file reader for DuckDB |
| 16 | [erpl_web](https://duckdb.org/community_extensions/extensions/erpl_web.html) | [erpl-web](https://github.com/DataZooDE/erpl-web) | 🟢 Ongoing | 3 days ago (2025-11-19 07:25:34 UTC) | 21 | C++ | ERPL is a DuckDB extension to connect to API based ecosystems via standard in... |
| 17 | [lsh](https://duckdb.org/community_extensions/extensions/lsh.html) | [lsh](https://github.com/princeton-ddss/lsh) | 🟢 Ongoing | 3 days ago (2025-11-19 21:21:33 UTC) | 5 | Rust | DuckDB community extension for locality-sensitive hashing (LSH) |
| 18 | [snowflake](https://duckdb.org/community_extensions/extensions/snowflake.html) | [duckdb-snowflake](https://github.com/iqea-ai/duckdb-snowflake) | 🟢 Ongoing | 3 days ago (2025-11-19 18:25:08 UTC) | 19 | C++ | A powerful DuckDB extension that enables seamless querying of Snowflake datab... |
| 19 | [airport](https://duckdb.org/community_extensions/extensions/airport.html) | [airport](https://github.com/Query-farm/airport) | 🟢 Ongoing | 5 days ago (2025-11-17 13:12:27 UTC) | 312 | C++ | The Airport extension for DuckDB, enables the use of Arrow Flight with DuckDB |
| 20 | [cache_httpfs](https://duckdb.org/community_extensions/extensions/cache_httpfs.html) | [duck-read-cache-fs](https://github.com/dentiny/duck-read-cache-fs) | 🟢 Ongoing | 5 days ago (2025-11-18 03:58:18 UTC) | 110 | C++ | This repository is made as read-only filesystem for remote access. |
| 21 | [sshfs](https://duckdb.org/community_extensions/extensions/sshfs.html) | [duckdb-sshfs](https://github.com/midwork-finds-jobs/duckdb-sshfs) | 🟢 Ongoing | 5 days ago (2025-11-17 11:24:29 UTC) | 1 | C++ | DuckDB sshfs extension - Read and write files through ssh inside DuckDB |
| 22 | [bigquery](https://duckdb.org/community_extensions/extensions/bigquery.html) | [duckdb-bigquery](https://github.com/hafenkran/duckdb-bigquery) | 🟢 Ongoing | 6 days ago (2025-11-16 17:25:38 UTC) | 143 | C++ | Integrates DuckDB with Google BigQuery, allowing direct querying and manageme... |
| 23 | [gaggle](https://duckdb.org/community_extensions/extensions/gaggle.html) | [gaggle](https://github.com/CogitatorTech/gaggle) | 🟢 Ongoing | 6 days ago (2025-11-16 13:39:10 UTC) | 8 | Rust | A DuckDB extension for working with Kaggle datasets |
| 24 | [observefs](https://duckdb.org/community_extensions/extensions/observefs.html) | [duckdb-filesystem-observability](https://github.com/dentiny/duckdb-filesystem-observability) | 🟢 Ongoing | 6 days ago (2025-11-16 08:26:38 UTC) | 5 | C++ | Provides observability for duckdb filesystem. |
| 25 | [webdavfs](https://duckdb.org/community_extensions/extensions/webdavfs.html) | [duckdb-webdavfs](https://github.com/midwork-finds-jobs/duckdb-webdavfs) | 🟢 Ongoing | 6 days ago (2025-11-16 18:45:25 UTC) | 0 | C++ | DuckDB WebDAVfs Extension - WebDAV filesystem support for DuckDB |
| 26 | [otlp](https://duckdb.org/community_extensions/extensions/otlp.html) | [duckdb-otlp](https://github.com/smithclay/duckdb-otlp) | 🟢 Ongoing | 7 days ago (2025-11-15 19:34:51 UTC) | 24 | C++ | query OpenTelemetry metrics, logs, and traces (OTLP) in duckdb |
| 27 | [dns](https://duckdb.org/community_extensions/extensions/dns.html) | [duckdb-dns](https://github.com/tobilg/duckdb-dns) | 🟢 Ongoing | 8 days ago (2025-11-14 11:23:24 UTC) | 14 | Rust | DNS (Reverse) Lookup Extension for DuckDB |
| 28 | [fakeit](https://duckdb.org/community_extensions/extensions/fakeit.html) | [duckdb-fakeit](https://github.com/tobilg/duckdb-fakeit) | 🟢 Ongoing | 8 days ago (2025-11-14 10:59:30 UTC) | 0 | Rust | DuckDB extension: fakeit by tobilg |
| 29 | [h3](https://duckdb.org/community_extensions/extensions/h3.html) | [h3-duckdb](https://github.com/isaacbrodsky/h3-duckdb) | 🟢 Ongoing | 8 days ago (2025-11-15 01:21:11 UTC) | 228 | C++ | Bindings for H3 to DuckDB |
| 30 | [miniplot](https://duckdb.org/community_extensions/extensions/miniplot.html) | [miniplot](https://github.com/nkwork9999/miniplot) | 🟢 Ongoing | 8 days ago (2025-11-15 02:42:43 UTC) | 12 | C++ | DuckDB extension: miniplot by nkwork9999 |
| 31 | [nats_js](https://duckdb.org/community_extensions/extensions/nats_js.html) | [duckdb-nats-jetstream](https://github.com/brannn/duckdb-nats-jetstream) | 🟢 Ongoing | 8 days ago (2025-11-14 07:24:21 UTC) | 4 | C++ | DuckDB extension for querying NATS JetStream message streams with SQL |
| 32 | [splink_udfs](https://duckdb.org/community_extensions/extensions/splink_udfs.html) | [splink_udfs](https://github.com/moj-analytical-services/splink_udfs) | ❓ Unknown | 8 days ago (2025-11-14 14:37:49 UTC) | 13 | C++ | DuckDB extension: splink_udfs by moj-analytical-services |
| 33 | [curl_httpfs](https://duckdb.org/community_extensions/extensions/curl_httpfs.html) | [duckdb-curl-filesystem](https://github.com/dentiny/duckdb-curl-filesystem) | 🟢 Ongoing | 9 days ago (2025-11-13 11:22:58 UTC) | 4 | C++ | Filesystem built upon libcurl. |
| 34 | [eeagrid](https://duckdb.org/community_extensions/extensions/eeagrid.html) | [duckdb-eeagrid](https://github.com/ahuarte47/duckdb-eeagrid) | 🟢 Ongoing | 10 days ago (2025-11-12 17:24:51 UTC) | 0 | C++ | Functions for transforming XY coordinates to and from the EEA Reference Grid... |
| 35 | [fivetran](https://duckdb.org/community_extensions/extensions/fivetran.html) | [fivetran](https://github.com/lnkuiper/fivetran) | 🟢 Ongoing | 10 days ago (2025-11-12 13:19:10 UTC) | 0 | C++ | DuckDB extension: fivetran by lnkuiper |
| 36 | [inflector](https://duckdb.org/community_extensions/extensions/inflector.html) | [inflector](https://github.com/Query-farm/inflector) | 🟢 Ongoing | 10 days ago (2025-11-12 20:48:44 UTC) | 2 | C++ | Powerful string case transformation and inflection capabilities directly to y... |
| 37 | [lua](https://duckdb.org/community_extensions/extensions/lua.html) | [duckdb-lua](https://github.com/isaacbrodsky/duckdb-lua) | 🟢 Ongoing | 10 days ago (2025-11-12 23:18:27 UTC) | 7 | C++ | DuckDB extension to evaluate Lua expressions. |
| 38 | [zipfs](https://duckdb.org/community_extensions/extensions/zipfs.html) | [duckdb-zipfs](https://github.com/isaacbrodsky/duckdb-zipfs) | 🟢 Ongoing | 10 days ago (2025-11-12 23:18:45 UTC) | 49 | C++ | DuckDB extension to read files within zip archives. |
| 39 | [a5](https://duckdb.org/community_extensions/extensions/a5.html) | [a5](https://github.com/Query-farm/a5) | 🟢 Ongoing | 12 days ago (2025-11-10 19:49:51 UTC) | 9 | C++ | A5 Geospatial Extension for DuckDB |
| 40 | [jsonata](https://duckdb.org/community_extensions/extensions/jsonata.html) | [jsonata](https://github.com/Query-farm/jsonata) | 🟢 Ongoing | 13 days ago (2025-11-09 18:06:25 UTC) | 2 | C++ | The JSONata extension for DuckDB enables expressive, JSON-focused querying an... |
| 41 | [quackformers](https://duckdb.org/community_extensions/extensions/quackformers.html) | [quackformers](https://github.com/martin-conur/quackformers) | ❓ Unknown | 18 days ago (2025-11-04 17:21:33 UTC) | 8 | Rust | DuckDB NLP extension. |
| 42 | [duck_delta_share](https://duckdb.org/community_extensions/extensions/duck_delta_share.html) | [duck_delta_share](https://github.com/cwiq-os/duck_delta_share) | 🟢 Ongoing | 19 days ago (2025-11-04 05:28:26 UTC) | 1 | C++ | DuckDB extension for enabling Delta Sharing client capabilities.  |
| 43 | [http_client](https://duckdb.org/community_extensions/extensions/http_client.html) | [httpclient](https://github.com/Query-farm/httpclient) | 🟢 Ongoing | 19 days ago (2025-11-03 10:41:51 UTC) | 74 | C++ | DuckDB HTTP GET/POST Client in a Community Extension |
| 44 | [bvh2sql](https://duckdb.org/community_extensions/extensions/bvh2sql.html) | [bvh2sql](https://github.com/nkwork9999/bvh2sql) | 🟢 Ongoing | 20 days ago (2025-11-02 18:17:05 UTC) | 0 | Makefile | SQL-related extension by nkwork9999 |
| 45 | [duckpgq](https://duckdb.org/community_extensions/extensions/duckpgq.html) | [duckpgq-extension](https://github.com/cwida/duckpgq-extension) | ❓ Unknown | 25 days ago (2025-10-28 14:08:33 UTC) | 312 | C++ | DuckDB extension that adds support for SQL/PGQ and graph algorithms |
| 46 | [minijinja](https://duckdb.org/community_extensions/extensions/minijinja.html) | [minijinja](https://github.com/Query-farm/minijinja) | 🟢 Ongoing | 26 days ago (2025-10-28 01:02:17 UTC) | 3 | C++ | DuckDB extension: minijinja |
| 47 | [st_read_multi](https://duckdb.org/community_extensions/extensions/st_read_multi.html) | [duckdb-ext-st-read-multi](https://github.com/yutannihilation/duckdb-ext-st-read-multi) | ❓ Unknown | 26 days ago (2025-10-27 13:47:48 UTC) | 5 | Rust | A DuckDB extension to import multiple geospatial files with `ST_Read_Multi()` |
| 48 | [tera](https://duckdb.org/community_extensions/extensions/tera.html) | [tera](https://github.com/Query-farm/tera) | 🟢 Ongoing | 26 days ago (2025-10-28 01:02:36 UTC) | 4 | C++ | DuckDB extension: tera |
| 49 | [mooncake](https://duckdb.org/community_extensions/extensions/mooncake.html) | [duckdb_mooncake](https://github.com/Mooncake-Labs/duckdb_mooncake) | 🟢 Ongoing | 27 days ago (2025-10-26 07:13:05 UTC) | 3 | C++ | Read Iceberg tables written by moonlink in real time |
| 50 | [tributary](https://duckdb.org/community_extensions/extensions/tributary.html) | [tributary](https://github.com/Query-farm/tributary) | 🟢 Ongoing | 28 days ago (2025-10-25 17:01:58 UTC) | 38 | C++ | A DuckDB Extension for Kafka |
| 51 | [json_schema](https://duckdb.org/community_extensions/extensions/json_schema.html) | [json_schema](https://github.com/Query-farm/json_schema) | 🟢 Ongoing | 29 days ago (2025-10-25 01:37:54 UTC) | 1 | Python | A DuckDB extension that bring support for validating JSON data using JSON sch... |
| 52 | [pbix](https://duckdb.org/community_extensions/extensions/pbix.html) | [duckdb-pbix-extension](https://github.com/Hugoberry/duckdb-pbix-extension) | 🟢 Ongoing | 29 days ago (2025-10-24 13:47:34 UTC) | 31 | C++ | Duckdb extension for parsing the metadata and contents of the embedded data m... |
| 53 | [cassandra](https://duckdb.org/community_extensions/extensions/cassandra.html) | [duckdb-cassandra](https://github.com/dioptre/duckdb-cassandra) | 🟢 Ongoing | 33 days ago (2025-10-20 19:15:10 UTC) | 0 | C++ | DuckDB Connector for Cassandra |
| 54 | [shellfs](https://duckdb.org/community_extensions/extensions/shellfs.html) | [shellfs](https://github.com/Query-farm/shellfs) | 🟢 Ongoing | 34 days ago (2025-10-19 19:25:56 UTC) | 83 | C++ | DuckDB extension allowing shell commands to be used for input and output. |
| 55 | [encoding](https://duckdb.org/community_extensions/extensions/encoding.html) | [duckdb-encoding](https://github.com/onnimonni/duckdb-encoding) | ❓ Unknown | 36 days ago (2025-10-17 06:53:16 UTC) | 2 | Rust | DuckDB extension: encoding by onnimonni |
| 56 | [dash](https://duckdb.org/community_extensions/extensions/dash.html) | [dash](https://github.com/gropaul/dash) | 🟢 Ongoing | 37 days ago (2025-10-16 07:33:44 UTC) | 17 | C++ | DuckDB Extension featuring a Query Builder GUI and Dashboarding features |
| 57 | [hdf5](https://duckdb.org/community_extensions/extensions/hdf5.html) | [duckdb-hdf5](https://github.com/Berrysoft/duckdb-hdf5) | ❓ Unknown | 38 days ago (2025-10-15 17:27:39 UTC) | 12 | Rust | HDF5 plugin for duckdb |
| 58 | [evalexpr_rhai](https://duckdb.org/community_extensions/extensions/evalexpr_rhai.html) | [evalexpr_rhai](https://github.com/Query-farm/evalexpr_rhai) | 🟢 Ongoing | 39 days ago (2025-10-15 03:12:44 UTC) | 21 | C++ | A DuckDB extension to evaluate the Rhai scripting language as part of SQL. |
| 59 | [file_dialog](https://duckdb.org/community_extensions/extensions/file_dialog.html) | [duckdb-ext-file-dialog](https://github.com/yutannihilation/duckdb-ext-file-dialog) | ❓ Unknown | 39 days ago (2025-10-14 15:53:28 UTC) | 14 | Rust | A DuckDB extension to choose file interactively using native file open dialogs |
| 60 | [lindel](https://duckdb.org/community_extensions/extensions/lindel.html) | [lindel](https://github.com/Query-farm/lindel) | 🟢 Ongoing | 39 days ago (2025-10-14 11:47:39 UTC) | 54 | C++ | DuckDB Extension Linearization/Delinearization, Z-Order, Hilbert and Morton C... |
| 61 | [bitfilters](https://duckdb.org/community_extensions/extensions/bitfilters.html) | [bitfilters](https://github.com/Query-farm/bitfilters) | 🟢 Ongoing | 40 days ago (2025-10-13 11:43:37 UTC) | 5 | C++ | A high-performance DuckDB extension providing probabilistic data structures f... |
| 62 | [crypto](https://duckdb.org/community_extensions/extensions/crypto.html) | [crypto](https://github.com/Query-farm/crypto) | 🟢 Ongoing | 40 days ago (2025-10-13 11:43:38 UTC) | 23 | C++ | DuckDB Extension for cryptographic hash functions and HMAC |
| 63 | [datasketches](https://duckdb.org/community_extensions/extensions/datasketches.html) | [datasketches](https://github.com/Query-farm/datasketches) | 🟢 Ongoing | 40 days ago (2025-10-13 11:43:38 UTC) | 36 | C++ | Integrates DuckDB with the high-performance Apache DataSketches library. This... |
| 64 | [duck_tails](https://duckdb.org/community_extensions/extensions/duck_tails.html) | [duck_tails](https://github.com/teaguesterling/duck_tails) | ❓ Unknown | 40 days ago (2025-10-14 03:29:06 UTC) | 4 | C++ | A DuckDB extension for exploring and reading git history. |
| 65 | [fuzzycomplete](https://duckdb.org/community_extensions/extensions/fuzzycomplete.html) | [fuzzycomplete](https://github.com/Query-farm/fuzzycomplete) | 🟢 Ongoing | 40 days ago (2025-10-13 11:43:40 UTC) | 23 | C++ | DuckDB Extension for fuzzy string matching based autocompletion |
| 66 | [hashfuncs](https://duckdb.org/community_extensions/extensions/hashfuncs.html) | [hashfuncs](https://github.com/Query-farm/hashfuncs) | 🟢 Ongoing | 40 days ago (2025-10-13 11:43:41 UTC) | 8 | C++ | A DuckDB extension that supplies non-cryptographic hash functions. |
| 67 | [marisa](https://duckdb.org/community_extensions/extensions/marisa.html) | [marisa](https://github.com/Query-farm/marisa) | 🟢 Ongoing | 40 days ago (2025-10-13 11:43:42 UTC) | 4 | C++ | The Marisa extension by Query.Farm integrates the fast, space-efficient MARIS... |
| 68 | [radio](https://duckdb.org/community_extensions/extensions/radio.html) | [radio](https://github.com/Query-farm/radio) | 🟢 Ongoing | 40 days ago (2025-10-13 11:43:42 UTC) | 32 | C++ | Radio is a DuckDB extension by Query.Farm that brings real-time event streams... |
| 69 | [rapidfuzz](https://duckdb.org/community_extensions/extensions/rapidfuzz.html) | [rapidfuzz](https://github.com/Query-farm/rapidfuzz) | 🟢 Ongoing | 40 days ago (2025-10-13 11:43:43 UTC) | 9 | C++ | DuckDB Community Extension adding RapidFuzz algorithms for search, deduplicat... |
| 70 | [stochastic](https://duckdb.org/community_extensions/extensions/stochastic.html) | [stochastic](https://github.com/Query-farm/stochastic) | 🟢 Ongoing | 40 days ago (2025-10-13 11:43:45 UTC) | 12 | C++ | A DuckDB extension that add comprehensive statistical distribution functions... |
| 71 | [textplot](https://duckdb.org/community_extensions/extensions/textplot.html) | [textplot](https://github.com/Query-farm/textplot) | 🟢 Ongoing | 40 days ago (2025-10-13 11:43:46 UTC) | 11 | C++ | A DuckDB community extension that enables text-based data visualization direc... |
| 72 | [duckdb_mcp](https://duckdb.org/community_extensions/extensions/duckdb_mcp.html) | [duckdb_mcp](https://github.com/teaguesterling/duckdb_mcp) | 🟢 Ongoing | 41 days ago (2025-10-12 19:52:30 UTC) | 14 | C++ | A simple MCP server extension for DuckDB |
| 73 | [markdown](https://duckdb.org/community_extensions/extensions/markdown.html) | [duckdb_markdown](https://github.com/teaguesterling/duckdb_markdown) | 🟢 Ongoing | 41 days ago (2025-10-12 19:38:52 UTC) | 8 | C++ | Heirarchical markdown parsing for DuckDB |
| 74 | [title_mapper](https://duckdb.org/community_extensions/extensions/title_mapper.html) | [duckdb-title-mapper](https://github.com/martin-conur/duckdb-title-mapper) | ❓ Unknown | 41 days ago (2025-10-12 22:54:26 UTC) | 2 | Rust | DuckDB extension: title_mapper by martin-conur |
| 75 | [webbed](https://duckdb.org/community_extensions/extensions/webbed.html) | [duckdb_webbed](https://github.com/teaguesterling/duckdb_webbed) | 🟢 Ongoing | 41 days ago (2025-10-12 21:30:22 UTC) | 29 | C++ | Web/HTTP functionality extension by teaguesterling |
| 76 | [httpserver](https://duckdb.org/community_extensions/extensions/httpserver.html) | [httpserver](https://github.com/Query-farm/httpserver) | 🟢 Ongoing | 42 days ago (2025-10-11 20:55:47 UTC) | 250 | HTML | DuckDB HTTP API Server and Query Interface in a  Community Extension |
| 77 | [rusty_quack](https://duckdb.org/community_extensions/extensions/rusty_quack.html) | [extension-template-rs](https://github.com/duckdb/extension-template-rs) | ❓ Unknown | 43 days ago (2025-10-10 08:12:32 UTC) | 86 | Rust | (Experimental) Template for Rust-based DuckDB extensions |
| 78 | [blockduck](https://duckdb.org/community_extensions/extensions/blockduck.html) | [BlockDuck](https://github.com/luohaha/BlockDuck) | 🟢 Ongoing | 45 days ago (2025-10-08 16:19:04 UTC) | 9 | C++ | Live SQL Queries on Blockchain |
| 79 | [quackstore](https://duckdb.org/community_extensions/extensions/quackstore.html) | [QuackStore](https://github.com/coginiti-dev/QuackStore) | 🟢 Ongoing | 45 days ago (2025-10-08 09:52:19 UTC) | 92 | C++ | DuckDB extension: quackstore by coginiti-dev |
| 80 | [arrow](https://duckdb.org/community_extensions/extensions/arrow.html) | [duckdb-extension-alias](https://github.com/duckdb/duckdb-extension-alias) | ❓ Unknown | 47 days ago (2025-10-06 09:07:38 UTC) | 5 | C | DuckDB extension: arrow |
| 81 | [netquack](https://duckdb.org/community_extensions/extensions/netquack.html) | [duckdb-netquack](https://github.com/hatamiarash7/duckdb-netquack) | ❓ Unknown | 48 days ago (2025-10-05 06:25:03 UTC) | 24 | C++ | DuckDB extension for parsing, extracting, and analyzing domains, URIs, and pa... |
| 82 | [yaml](https://duckdb.org/community_extensions/extensions/yaml.html) | [duckdb_yaml](https://github.com/teaguesterling/duckdb_yaml) | 🟢 Ongoing | 49 days ago (2025-10-05 00:31:42 UTC) | 9 | C++ |  A DuckDB to read and work with YAML files in a similar way to JSON files (al... |
| 83 | [geography](https://duckdb.org/community_extensions/extensions/geography.html) | [duckdb-geography](https://github.com/paleolimbot/duckdb-geography) | 🟢 Ongoing | 51 days ago (2025-10-02 11:09:38 UTC) | 34 | C++ | Geospatial data extension by paleolimbot |
| 84 | [hostfs](https://duckdb.org/community_extensions/extensions/hostfs.html) | [hostFS](https://github.com/gropaul/hostFS) | ❓ Unknown | 52 days ago (2025-10-01 21:02:13 UTC) | 28 | C++ | DuckDB extension: hostfs by gropaul |
| 85 | [faiss](https://duckdb.org/community_extensions/extensions/faiss.html) | [duckdb-faiss-ext](https://github.com/duckdb-faiss-ext/duckdb-faiss-ext) | ❓ Unknown | 54 days ago (2025-09-29 12:01:42 UTC) | 27 | Go | DuckDB wrapper for FAISS - Experimental |
| 86 | [magic](https://duckdb.org/community_extensions/extensions/magic.html) | [duckdb_magic](https://github.com/carlopi/duckdb_magic) | 🟢 Ongoing | 56 days ago (2025-09-27 18:50:32 UTC) | 7 | C++ | Auto-detect file types via `libmagic` (`file` utility) |
| 87 | [msolap](https://duckdb.org/community_extensions/extensions/msolap.html) | [duckdb-msolap-extension](https://github.com/Hugoberry/duckdb-msolap-extension) | 🟢 Ongoing | 59 days ago (2025-09-24 16:33:46 UTC) | 12 | C++ | DuckDB extension: msolap by Hugoberry |
| 88 | [parser_tools](https://duckdb.org/community_extensions/extensions/parser_tools.html) | [duckdb_extension_parser_tools](https://github.com/hotdata-dev/duckdb_extension_parser_tools) | 🟢 Ongoing | 59 days ago (2025-09-24 17:46:33 UTC) | 18 | C++ | Parse sql - with sql! |
| 89 | [chsql](https://duckdb.org/community_extensions/extensions/chsql.html) | [clickhouse-sql](https://github.com/Query-farm/clickhouse-sql) | ❓ Unknown | 60 days ago (2025-09-23 19:24:33 UTC) | 82 | C++ | DuckDB Community Extension implementing ClickHouse SQL Dialect macros and Cus... |
| 90 | [chsql_native](https://duckdb.org/community_extensions/extensions/chsql_native.html) | [clickhouse-native](https://github.com/Query-farm/clickhouse-native) | ❓ Unknown | 60 days ago (2025-09-23 19:24:31 UTC) | 17 | Rust | Experimental ClickHouse Native Client and Native file reader Extension for Du... |
| 91 | [cronjob](https://duckdb.org/community_extensions/extensions/cronjob.html) | [cronjob](https://github.com/Query-farm/cronjob) | ❓ Unknown | 60 days ago (2025-09-23 19:24:35 UTC) | 44 | C++ | DuckDB CronJob Extension |
| 92 | [open_prompt](https://duckdb.org/community_extensions/extensions/open_prompt.html) | [openprompt](https://github.com/Query-farm/openprompt) | ❓ Unknown | 60 days ago (2025-09-23 19:24:40 UTC) | 51 | C++ | DuckDB Community Extension to prompt LLMs from SQL |
| 93 | [pcap_reader](https://duckdb.org/community_extensions/extensions/pcap_reader.html) | [pcap](https://github.com/Query-farm/pcap) | ❓ Unknown | 60 days ago (2025-09-23 19:24:42 UTC) | 11 | Rust | DuckDB PCAP Reader Extension made in Rust |
| 94 | [pyroscope](https://duckdb.org/community_extensions/extensions/pyroscope.html) | [pyroscope](https://github.com/Query-farm/pyroscope) | ❓ Unknown | 60 days ago (2025-09-23 19:24:44 UTC) | 19 | Rust | DuckDB Pyroscope Extension for Continuous Profiling |
| 95 | [quickjs](https://duckdb.org/community_extensions/extensions/quickjs.html) | [quickjs](https://github.com/Query-farm/quickjs) | 🟢 Ongoing | 60 days ago (2025-09-23 19:24:51 UTC) | 8 | C++ | DuckDB extension: quickjs by quackscience |
| 96 | [redis](https://duckdb.org/community_extensions/extensions/redis.html) | [redis](https://github.com/Query-farm/redis) | ❓ Unknown | 60 days ago (2025-09-23 19:24:45 UTC) | 8 | C++ | DuckDB Redis Client community extension |
| 97 | [tsid](https://duckdb.org/community_extensions/extensions/tsid.html) | [tsid](https://github.com/Query-farm/tsid) | ❓ Unknown | 60 days ago (2025-09-23 19:24:47 UTC) | 5 | C++ | TSID Extension for DuckDB  |
| 98 | [webmacro](https://duckdb.org/community_extensions/extensions/webmacro.html) | [webmacro](https://github.com/Query-farm/webmacro) | ❓ Unknown | 60 days ago (2025-09-23 19:24:49 UTC) | 13 | C++ | DuckDB WebMacro: Share and Load your SQL Macros via gists |
| 99 | [wireduck](https://duckdb.org/community_extensions/extensions/wireduck.html) | [wireduck](https://github.com/hyehudai/wireduck) | 🟢 Ongoing | 60 days ago (2025-09-23 21:22:03 UTC) | 47 | C++ | Duckdb extension to read pcap files |
| 100 | [prql](https://duckdb.org/community_extensions/extensions/prql.html) | [duckdb-prql](https://github.com/ywelsch/duckdb-prql) | 🟢 Ongoing | 61 days ago (2025-09-22 18:45:53 UTC) | 307 | C++ | PRQL as a DuckDB extension |
| 101 | [psql](https://duckdb.org/community_extensions/extensions/psql.html) | [duckdb-psql](https://github.com/ywelsch/duckdb-psql) | 🟢 Ongoing | 61 days ago (2025-09-22 18:45:44 UTC) | 96 | C++ | A piped SQL for DuckDB |
| 102 | [cwiqduck](https://duckdb.org/community_extensions/extensions/cwiqduck.html) | [cwiqduck](https://github.com/cwiq-os/cwiqduck) | 🟢 Ongoing | 62 days ago (2025-09-22 02:39:48 UTC) | 2 | C++ | DuckDB extensions for CWIQ |
| 103 | [chaos](https://duckdb.org/community_extensions/extensions/chaos.html) | [duckdb-chaos](https://github.com/taniabogatsch/duckdb-chaos) | 🟢 Ongoing | 64 days ago (2025-09-19 11:42:23 UTC) | 0 | C++ | DuckDB extension: chaos by taniabogatsch |
| 104 | [flock](https://duckdb.org/community_extensions/extensions/flock.html) | [flock](https://github.com/dais-polymtl/flock) | 🟢 Ongoing | 64 days ago (2025-09-19 15:11:32 UTC) | 280 | C++ | Flock: multimodal querying for DuckDB |
| 105 | [nanoarrow](https://duckdb.org/community_extensions/extensions/nanoarrow.html) | [duckdb-nanoarrow](https://github.com/paleolimbot/duckdb-nanoarrow) | ❓ Unknown | 66 days ago (2025-09-17 18:31:44 UTC) | 52 | C++ | DuckDB extension: nanoarrow by paleolimbot |
| 106 | [gsheets](https://duckdb.org/community_extensions/extensions/gsheets.html) | [duckdb_gsheets](https://github.com/evidence-dev/duckdb_gsheets) | 🟢 Ongoing | 74 days ago (2025-09-09 21:14:54 UTC) | 309 | C++ | DuckDB extension to read and write Google Sheets using SQL |
| 107 | [geotiff](https://duckdb.org/community_extensions/extensions/geotiff.html) | [duckdb-geotiff](https://github.com/babaknaimi/duckdb-geotiff) | ❓ Unknown | 95 days ago (2025-08-20 05:12:15 UTC) | 2 | C++ | Duckdb extension to read GeoTiffs directly with duckdb database |
| 108 | [highs](https://duckdb.org/community_extensions/extensions/highs.html) | [HiGHS-duckdb](https://github.com/fhk/HiGHS-duckdb) | ❓ Unknown | 98 days ago (2025-08-16 06:41:18 UTC) | 1 | C++ | Run the solver in the database! |
| 109 | [read_stat](https://duckdb.org/community_extensions/extensions/read_stat.html) | [duckdb-read-stat](https://github.com/mettekou/duckdb-read-stat) | 🟢 Ongoing | 103 days ago (2025-08-11 08:46:10 UTC) | 23 | C | Read data sets from SAS, Stata, and SPSS from DuckDB with ReadStat |
| 110 | [jwt](https://duckdb.org/community_extensions/extensions/jwt.html) | [duckdb_jwt](https://github.com/GalvinGao/duckdb_jwt) | ❓ Unknown | 137 days ago (2025-07-09 00:13:56 UTC) | 0 | C++ | DuckDB extension: jwt by GalvinGao |
| 111 | [substrait](https://duckdb.org/community_extensions/extensions/substrait.html) | [duckdb-substrait-extension](https://github.com/substrait-io/duckdb-substrait-extension) | ❓ Unknown | 147 days ago (2025-06-29 02:00:00 UTC) | 53 | C++ | DuckDB extension: substrait by substrait-io |
| 112 | [ofquack](https://duckdb.org/community_extensions/extensions/ofquack.html) | [ofquack](https://github.com/krokozyab/ofquack) | ❓ Unknown | 214 days ago (2025-04-22 12:24:17 UTC) | 5 | C++ | Oracle Fusion DuckDB extension  |
| 113 | [scrooge](https://duckdb.org/community_extensions/extensions/scrooge.html) | [Scrooge-McDuck](https://github.com/pdet/Scrooge-McDuck) | ❓ Unknown | 222 days ago (2025-04-14 11:16:07 UTC) | 150 | C++ | DuckDB extension: scrooge by pdet |
| 114 | [pivot_table](https://duckdb.org/community_extensions/extensions/pivot_table.html) | [pivot_table](https://github.com/Alex-Monahan/pivot_table) | ❓ Unknown | over a year ago (2024-09-22 21:18:45 UTC) | 16 | C++ | Full spreadsheet-style pivot table through SQL macros. Just specify values, r... |
| 115 | [tarfs](https://duckdb.org/community_extensions/extensions/tarfs.html) | [duckdb_tarfs](https://github.com/Maxxen/duckdb_tarfs) | ❓ Unknown | over a year ago (2024-08-26 11:01:47 UTC) | 11 | C++ | DuckDB extension: tarfs by Maxxen |
| 116 | [ulid](https://duckdb.org/community_extensions/extensions/ulid.html) | [duckdb_ulid](https://github.com/Maxxen/duckdb_ulid) | ❓ Unknown | over a year ago (2024-07-09 09:35:50 UTC) | 24 | C++ | DuckDB extension: ulid by Maxxen |

**Total:** 116 extensions
---

## Appendix: DuckDB Release Information

### Current Release Context

DuckDB follows **semantic versioning** with regular releases. For complete and up-to-date release information, see the official [**DuckDB Release Calendar**](https://duckdb.org/release_calendar.html).

### Release History

| Version | Release Date | Codename | Named After | LTS | Blog Post |
|---------|--------------|----------|-------------|-----|-----------|
| **v1.5.0** 📅 | 2026-02-04 | *Planned* | – | ✓ | *Upcoming release* |
| **v1.4.1** 🎆 | 2025-10-07 | – | – | – | [Announcing DuckDB 1.4.1](https://duckdb.org/2025/10/07/announcing-duckdb-141) |
| **v1.4.0** | 2025-09-16 | Andium | *Anas andium* (Andean teal) | ✓ | [Announcing DuckDB 1.4.0](https://duckdb.org/2025/09/16/announcing-duckdb-140) |
| v1.3.2 | 2025-07-08 | – | – | – | – |
| v1.3.1 | 2025-06-16 | – | – | – | – |
| **v1.3.0** | 2025-05-21 | Ossivalis | *Bucephala ossivalis* (Goldeneye duck) | – | [Announcing DuckDB 1.3.0](https://duckdb.org/2025/05/21/announcing-duckdb-130) |
| v1.2.2 | 2025-04-08 | – | – | – | – |
| v1.2.1 | 2025-03-05 | – | – | – | – |
| **v1.2.0** | 2025-02-05 | Histrionicus | *Histrionicus histrionicus* (Harlequin duck) | – | [Announcing DuckDB 1.2.0](https://duckdb.org/2025/02/05/announcing-duckdb-120) |
| v1.1.3 | 2024-11-04 | – | – | – | – |
| v1.1.2 | 2024-10-14 | – | – | – | – |
| v1.1.1 | 2024-09-24 | – | – | – | – |
| **v1.1.0** | 2024-09-09 | Eatoni | *Anas eatoni* (Eaton's pintail) | – | [Announcing DuckDB 1.1.0](https://duckdb.org/2024/09/09/announcing-duckdb-110) |
| **v1.0.0** | 2024-06-03 | Nivis | *Anas nivis* (Snow duck) | – | [Announcing DuckDB 1.0.0](https://duckdb.org/2024/06/03/announcing-duckdb-100) |

### Historical Releases (Pre-1.0)

| Version | Release Date | Codename | Named After | Blog Post |
|---------|--------------|----------|-------------|-----------|
| v0.10.3 | 2024-05-22 | – | – | – |
| v0.10.2 | 2024-04-17 | – | – | – |
| v0.10.1 | 2024-03-18 | – | – | – |
| **v0.10.0** | 2024-02-13 | Fusca | *Melanitta fusca* (Velvet scoter) | [Announcing DuckDB 0.10.0](https://duckdb.org/2024/02/13/announcing-duckdb-0100) |
| v0.9.2 | 2023-11-14 | – | – | – |
| v0.9.1 | 2023-10-11 | – | – | – |
| **v0.9.0** | 2023-09-26 | Undulata | *Anas undulata* (Yellow-billed duck) | [Announcing DuckDB 0.9.0](https://duckdb.org/2023/09/26/announcing-duckdb-090) |
| v0.8.1 | 2023-06-13 | – | – | – |
| **v0.8.0** | 2023-05-17 | Fulvigula | *Anas fulvigula* (Mottled duck) | [Announcing DuckDB 0.8.0](https://duckdb.org/2023/05/17/announcing-duckdb-080) |
| v0.7.1 | 2023-02-27 | – | – | – |
| **v0.7.0** | 2023-02-13 | Labradorius | *Camptorhynchus labradorius* (Labrador duck) | [Announcing DuckDB 0.7.0](https://duckdb.org/2023/02/13/announcing-duckdb-070) |
| v0.6.1 | 2022-12-06 | – | – | – |
| **v0.6.0** | 2022-11-14 | Oxyura | *Oxyura leucocephala* (White-headed duck) | [Announcing DuckDB 0.6.0](https://duckdb.org/2022/11/14/announcing-duckdb-060) |
| v0.5.1 | 2022-09-19 | – | – | – |
| **v0.5.0** | 2022-09-05 | Pulchellus | *Nettapus pulchellus* (Green pygmy goose) | – |

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

*Data sourced from the official [DuckDB releases CSV](https://duckdb.org/data/duckdb-releases.csv). For the most current information, always check the [release calendar](https://duckdb.org/release_calendar.html).*
