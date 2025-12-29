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
| **Community Extensions** | 137 |
| **Total Extensions** | 162 |
| **Recently Active** (≤ 30 days) | 97 |
| **Very Active** (≤ 7 days) | 23 |


---
## Core Extensions

Core extensions maintained by the DuckDB team and distributed via the official extension repository

| # | Extension | Repository | Status | Last Activity | Stars | Language | Description |
|---|-----------|------------|--------|---------------|-------|----------|-------------|
| 1 | [autocomplete](https://duckdb.org/docs/stable/core_extensions/autocomplete.html) | [duckdb/duckdb](https://github.com/duckdb/duckdb/tree/main/extension/autocomplete) | 🟢 Ongoing | 8 days ago (2025-12-20 21:38:19 UTC) | N/A (part of core DuckDB repo) | C++ | Core DuckDB extension: autocomplete |
| 2 | [avro](https://duckdb.org/docs/stable/core_extensions/avro.html) | [duckdb-avro](https://github.com/duckdb/duckdb-avro) | 🟢 Ongoing | 27 days ago (2025-12-01 09:17:47 UTC) | 31 | C++ | Apache Avro format support |
| 3 | [aws](https://duckdb.org/docs/stable/core_extensions/aws.html) | [duckdb-aws](https://github.com/duckdb/duckdb-aws) | 🟢 Ongoing | 87 days ago (2025-10-02 10:50:00 UTC) | 58 | C++ | AWS S3 integration |
| 4 | [azure](https://duckdb.org/docs/stable/core_extensions/azure.html) | [duckdb-azure](https://github.com/duckdb/duckdb-azure) | 🟢 Ongoing | 5 days ago (2025-12-23 11:02:09 UTC) | 69 | C++ | Azure extension for DuckDB |
| 5 | [delta](https://duckdb.org/docs/stable/core_extensions/delta.html) | [duckdb-delta](https://github.com/duckdb/duckdb-delta) | 🟢 Ongoing | 13 days ago (2025-12-15 15:21:29 UTC) | 204 | C++ | DuckDB extension for Delta Lake |
| 6 | [ducklake](https://duckdb.org/docs/stable/core_extensions/ducklake.html) | [duckdb/ducklake](https://github.com/duckdb/ducklake) | 🟢 Ongoing | 19 days ago | N/A (part of core DuckDB repo) | C++ | Delta Lake support via DuckLake (different from delta extension) |
| 7 | [encodings](https://duckdb.org/docs/stable/core_extensions/encodings.html) | [duckdb-encodings](https://github.com/duckdb/duckdb-encodings) | 🟢 Ongoing | 102 days ago (2025-09-17 12:57:45 UTC) | 16 | C++ | Character encoding support |
| 8 | [excel](https://duckdb.org/docs/stable/core_extensions/excel.html) | [duckdb-excel](https://github.com/duckdb/duckdb-excel) | 🟢 Ongoing | 116 days ago (2025-09-03 21:31:45 UTC) | 49 | C++ | Excel extension for DuckDB |
| 9 | [fts](https://duckdb.org/docs/stable/core_extensions/full_text_search.html) | [duckdb-fts](https://github.com/duckdb/duckdb-fts) | 🟢 Ongoing | 103 days ago (2025-09-16 14:12:43 UTC) | 31 | C++ | Full-text search functionality |
| 10 | [httpfs](https://duckdb.org/docs/stable/core_extensions/httpfs/overview.html) | [duckdb-httpfs](https://github.com/duckdb/duckdb-httpfs) | 🟢 Ongoing | 5 days ago (2025-12-23 12:52:43 UTC) | 43 | C++ | HTTP/S3 filesystem support |
| 11 | [iceberg](https://duckdb.org/docs/stable/core_extensions/iceberg/overview.html) | [duckdb-iceberg](https://github.com/duckdb/duckdb-iceberg) | 🟢 Ongoing | 17 days ago (2025-12-11 13:59:33 UTC) | 355 | C++ | Apache Iceberg format support |
| 12 | [icu](https://duckdb.org/docs/stable/core_extensions/icu.html) | [duckdb/duckdb](https://github.com/duckdb/duckdb/tree/main/extension/icu) | 🟢 Ongoing | 18 days ago (2025-12-10 23:52:08 UTC) | N/A (part of core DuckDB repo) | C++ | Core DuckDB extension: icu |
| 13 | [inet](https://duckdb.org/docs/stable/core_extensions/inet.html) | [duckdb-inet](https://github.com/duckdb/duckdb-inet) | 🟢 Ongoing | 38 days ago (2025-11-20 22:54:12 UTC) | 15 | C++ | Internet address data types |
| 14 | [jemalloc](https://duckdb.org/docs/stable/core_extensions/jemalloc.html) | [duckdb/duckdb](https://github.com/duckdb/duckdb/tree/main/extension/jemalloc) | 🟢 Ongoing | 204 days ago (2025-06-07 09:38:02 UTC) | N/A (part of core DuckDB repo) | C++ | Core DuckDB extension: jemalloc |
| 15 | [json](https://duckdb.org/docs/stable/data/json/overview.html) | [duckdb/duckdb](https://github.com/duckdb/duckdb/tree/main/extension/json) | 🟢 Ongoing | 14 days ago (2025-12-15 00:28:51 UTC) | N/A (part of core DuckDB repo) | C++ | Core DuckDB extension: json |
| 16 | [mysql](https://duckdb.org/docs/stable/core_extensions/mysql.html) | [duckdb-mysql](https://github.com/duckdb/duckdb-mysql) | 🟢 Ongoing | 12 days ago (2025-12-16 07:32:58 UTC) | 85 | C++ | MySQL database connectivity |
| 17 | [parquet](https://duckdb.org/docs/stable/data/parquet/overview.html) | [duckdb/duckdb](https://github.com/duckdb/duckdb/tree/main/extension/parquet) | 🟢 Ongoing | 4 days ago (2025-12-24 13:32:55 UTC) | N/A (part of core DuckDB repo) | C++ | Core DuckDB extension: parquet |
| 18 | [postgres](https://duckdb.org/docs/stable/core_extensions/postgres.html) | [duckdb-postgres](https://github.com/duckdb/duckdb-postgres) | 🟢 Ongoing | 31 days ago (2025-11-27 14:55:29 UTC) | 330 | C++ | PostgreSQL database connectivity |
| 19 | [spatial](https://duckdb.org/docs/stable/core_extensions/spatial/overview.html) | [duckdb-spatial](https://github.com/duckdb/duckdb-spatial) | 🟢 Ongoing | 26 days ago (2025-12-02 12:34:41 UTC) | 647 | C++ | Geospatial data types and functions |
| 20 | [sqlite](https://duckdb.org/docs/stable/core_extensions/sqlite.html) | [duckdb-sqlite](https://github.com/duckdb/duckdb-sqlite) | 🟢 Ongoing | 91 days ago (2025-09-28 07:21:39 UTC) | 260 | C++ | DuckDB extension to read and write to SQLite databases |
| 21 | [tpcds](https://duckdb.org/docs/stable/core_extensions/tpcds.html) | [duckdb/duckdb](https://github.com/duckdb/duckdb/tree/main/extension/tpcds) | 🟢 Ongoing | 6 days ago (2025-12-22 16:58:23 UTC) | N/A (part of core DuckDB repo) | C++ | Core DuckDB extension: tpcds |
| 22 | [tpch](https://duckdb.org/docs/stable/core_extensions/tpch.html) | [duckdb/duckdb](https://github.com/duckdb/duckdb/tree/main/extension/tpch) | 🟢 Ongoing | 6 days ago (2025-12-22 16:58:23 UTC) | N/A (part of core DuckDB repo) | C++ | Core DuckDB extension: tpch |
| 23 | [ui](https://duckdb.org/docs/stable/core_extensions/ui.html) | [duckdb-ui](https://github.com/duckdb/duckdb-ui) | 🟢 Ongoing | 18 days ago (2025-12-10 17:04:50 UTC) | 399 | C++ | Browser-based user interface for DuckDB |
| 24 | [vortex](https://duckdb.org/docs/stable/core_extensions/vortex.html) | ~~[vortex](https://github.com/duckdb/duckdb/extensions/vortex)~~ **NOT FOUND:** https://github.com/duckdb/duckdb/extensions/vortex (HTTP 404) | 🟢 Ongoing | 19 days ago | N/A (part of core DuckDB repo) | C++ | Core DuckDB extension: vortex |
| 25 | [vss](https://duckdb.org/docs/stable/core_extensions/vss.html) | [duckdb-vss](https://github.com/duckdb/duckdb-vss) | 🟢 Ongoing | 114 days ago (2025-09-05 07:04:02 UTC) | 229 | C++ | Vector similarity search |

**Total:** 25 extensions

---
---
## Community Extensions

Third-party extensions maintained by the community

| # | Extension | Repository | Status | Last Activity | Stars | Language | Description |
|---|-----------|------------|--------|---------------|-------|----------|-------------|
| 1 | [anofox_tabular](https://duckdb.org/community_extensions/extensions/anofox_tabular.html) | [anofox-tabular](https://github.com/DataZooDE/anofox-tabular) | ❓ Unknown | today (2025-12-29 05:05:06 UTC) | 7 | C++ | A duckdb extension which combines data quality and data preparation tools for... |
| 2 | [boilstream](https://duckdb.org/community_extensions/extensions/boilstream.html) | [boilstream-extension](https://github.com/dforsber/boilstream-extension) | 🟢 Ongoing | today (2025-12-28 15:24:39 UTC) | 2 | C++ | Secure Remote Secrets Storage for DuckDB |
| 3 | [lance](https://duckdb.org/community_extensions/extensions/lance.html) | [lance-duckdb](https://github.com/lance-format/lance-duckdb) | 🟢 Ongoing | today (2025-12-29 05:31:14 UTC) | 34 | C++ | The lance extensions for DuckDB enable reading and writing of lance tables. |
| 4 | [markdown](https://duckdb.org/community_extensions/extensions/markdown.html) | [duckdb_markdown](https://github.com/teaguesterling/duckdb_markdown) | 🟢 Ongoing | today (2025-12-29 01:58:26 UTC) | 9 | C++ | Heirarchical markdown parsing for DuckDB |
| 5 | [pdal](https://duckdb.org/community_extensions/extensions/pdal.html) | [duckdb-pdal](https://github.com/ahuarte47/duckdb-pdal) | 🟢 Ongoing | today (2025-12-28 20:29:22 UTC) | 22 | C++ | DuckDB extension for manipulating point cloud data using SQL |
| 6 | [sitting_duck](https://duckdb.org/community_extensions/extensions/sitting_duck.html) | [sitting_duck](https://github.com/teaguesterling/sitting_duck) | 🟢 Ongoing | today (2025-12-29 01:55:05 UTC) | 4 | C | DuckDB extension: sitting_duck by teaguesterling |
| 7 | [yardstick](https://duckdb.org/community_extensions/extensions/yardstick.html) | [yardstick](https://github.com/sidequery/yardstick) | 🟢 Ongoing | today (2025-12-29 05:29:40 UTC) | 30 | Rust | An implementation of Measures in SQL as a DuckDB extension |
| 8 | [anofox_forecast](https://duckdb.org/community_extensions/extensions/anofox_forecast.html) | [anofox-forecast](https://github.com/DataZooDE/anofox-forecast) | 🟢 Ongoing | today (2025-12-27 11:18:42 UTC) | 21 | C++ | Statistical timeseries forecasting in DuckDB |
| 9 | [anofox_statistics](https://duckdb.org/community_extensions/extensions/anofox_statistics.html) | [anofox-statistics](https://github.com/DataZooDE/anofox-statistics) | 🟢 Ongoing | today (2025-12-27 15:32:10 UTC) | 5 | Rust | A DuckDB extension for statistical regression analysis, providing OLS, Ridge,... |
| 10 | [onager](https://duckdb.org/community_extensions/extensions/onager.html) | [onager](https://github.com/CogitatorTech/onager) | 🟢 Ongoing | today (2025-12-27 11:17:15 UTC) | 31 | Rust | A DuckDB extension for graph data analytics |
| 11 | [cache_httpfs](https://duckdb.org/community_extensions/extensions/cache_httpfs.html) | [duck-read-cache-fs](https://github.com/dentiny/duck-read-cache-fs) | 🟢 Ongoing | 2 days ago (2025-12-26 11:50:29 UTC) | 123 | C++ | This repository is made as read-only filesystem for remote access. |
| 12 | [duck_hunt](https://duckdb.org/community_extensions/extensions/duck_hunt.html) | [duck_hunt](https://github.com/teaguesterling/duck_hunt) | 🟢 Ongoing | 2 days ago (2025-12-26 21:19:05 UTC) | 1 | C++ | Tools for working with unit test suite results |
| 13 | [duckgl](https://duckdb.org/community_extensions/extensions/duckgl.html) | [duckgl](https://github.com/nkwork9999/duckgl) | 🟢 Ongoing | 2 days ago (2025-12-27 04:09:47 UTC) | 0 | C++ | DuckDB extension: duckgl by nkwork9999 |
| 14 | [observefs](https://duckdb.org/community_extensions/extensions/observefs.html) | [duckdb-filesystem-observability](https://github.com/dentiny/duckdb-filesystem-observability) | 🟢 Ongoing | 2 days ago (2025-12-26 13:18:25 UTC) | 8 | C++ | Provides observability for duckdb filesystem. |
| 15 | [poached](https://duckdb.org/community_extensions/extensions/poached.html) | [poached](https://github.com/sidequery/poached) | 🟢 Ongoing | 2 days ago (2025-12-26 21:13:19 UTC) | 7 | C++ | A DuckDB extension that exposes SQL parsing functionality for building IDEs,... |
| 16 | [erpl_web](https://duckdb.org/community_extensions/extensions/erpl_web.html) | [erpl-web](https://github.com/DataZooDE/erpl-web) | 🟢 Ongoing | 3 days ago (2025-12-25 13:47:47 UTC) | 22 | C++ | ERPL is a DuckDB extension to connect to API based ecosystems via standard in... |
| 17 | [quackfix](https://duckdb.org/community_extensions/extensions/quackfix.html) | [QuackFIX](https://github.com/hyehudai/QuackFIX) | 🟢 Ongoing | 3 days ago (2025-12-25 10:36:24 UTC) | 6 | C++ | Fix log extension for duckdb |
| 18 | [llm](https://duckdb.org/community_extensions/extensions/llm.html) | [duckdb-llm](https://github.com/midwork-finds-jobs/duckdb-llm) | 🟢 Ongoing | 4 days ago (2025-12-25 05:35:42 UTC) | 0 | C++ | DuckDB extension: llm by midwork-finds-jobs |
| 19 | [http_request](https://duckdb.org/community_extensions/extensions/http_request.html) | [duckdb_http_request](https://github.com/midwork-finds-jobs/duckdb_http_request) | 🟢 Ongoing | 5 days ago (2025-12-23 18:13:58 UTC) | 0 | C++ | Uses the native duckdb httputil to make extra requests in SELECT |
| 20 | [zipfs](https://duckdb.org/community_extensions/extensions/zipfs.html) | [duckdb-zipfs](https://github.com/isaacbrodsky/duckdb-zipfs) | 🟢 Ongoing | 5 days ago (2025-12-23 21:32:46 UTC) | 53 | C++ | DuckDB extension to read files within zip archives. |
| 21 | [minijinja](https://duckdb.org/community_extensions/extensions/minijinja.html) | [minijinja](https://github.com/Query-farm/minijinja) | 🟢 Ongoing | 6 days ago (2025-12-22 14:59:08 UTC) | 5 | C++ | DuckDB extension: minijinja |
| 22 | [st_read_multi](https://duckdb.org/community_extensions/extensions/st_read_multi.html) | [duckdb-ext-st-read-multi](https://github.com/yutannihilation/duckdb-ext-st-read-multi) | 🟢 Ongoing | 6 days ago (2025-12-22 13:17:03 UTC) | 5 | Rust | A DuckDB extension to import multiple geospatial files with `ST_Read_Multi()` |
| 23 | [quackformers](https://duckdb.org/community_extensions/extensions/quackformers.html) | [quackformers](https://github.com/martin-conur/quackformers) | ❓ Unknown | 7 days ago (2025-12-21 18:43:16 UTC) | 8 | Rust | DuckDB NLP extension. |
| 24 | [h3](https://duckdb.org/community_extensions/extensions/h3.html) | [h3-duckdb](https://github.com/isaacbrodsky/h3-duckdb) | 🟢 Ongoing | 9 days ago (2025-12-19 21:58:47 UTC) | 234 | C++ | Bindings for H3 to DuckDB |
| 25 | [anndata](https://duckdb.org/community_extensions/extensions/anndata.html) | [anndata-duckdb-extension](https://github.com/honicky/anndata-duckdb-extension) | 🟢 Ongoing | 10 days ago (2025-12-18 18:16:10 UTC) | 0 | C++ | Attach and AnnData file in duckdb and query it with SQL.  Perform SQL over gr... |
| 26 | [duckherder](https://duckdb.org/community_extensions/extensions/duckherder.html) | [duckdb-distributed-execution](https://github.com/dentiny/duckdb-distributed-execution) | 🟢 Ongoing | 10 days ago (2025-12-18 11:12:23 UTC) | 39 | C++ | Distributed execution for duckdb queries. |
| 27 | [quack](https://duckdb.org/community_extensions/extensions/quack.html) | [extension-template](https://github.com/duckdb/extension-template) | ❓ Unknown | 10 days ago (2025-12-18 13:53:03 UTC) | 250 | Python | Template for DuckDB extensions to help you develop, test and deploy a custom... |
| 28 | [rusty_sheet](https://duckdb.org/community_extensions/extensions/rusty_sheet.html) | [rusty-sheet](https://github.com/redraiment/rusty-sheet) | 🟢 Ongoing | 10 days ago (2025-12-19 03:04:01 UTC) | 56 | Rust | An Excel/WPS/OpenDocument Spreadsheets file reader for DuckDB |
| 29 | [capi_quack](https://duckdb.org/community_extensions/extensions/capi_quack.html) | [extension-template-c](https://github.com/duckdb/extension-template-c) | ❓ Unknown | 12 days ago (2025-12-16 13:25:38 UTC) | 27 | C | (Experimental) C/C++ template for DuckDB extensions based on the C API |
| 30 | [duckpgq](https://duckdb.org/community_extensions/extensions/duckpgq.html) | [duckpgq-extension](https://github.com/cwida/duckpgq-extension) | 🟢 Ongoing | 12 days ago (2025-12-16 09:31:39 UTC) | 330 | C++ | DuckDB extension that adds support for SQL/PGQ and graph algorithms |
| 31 | [rusty_quack](https://duckdb.org/community_extensions/extensions/rusty_quack.html) | [extension-template-rs](https://github.com/duckdb/extension-template-rs) | ❓ Unknown | 12 days ago (2025-12-16 13:27:35 UTC) | 87 | Rust | (Experimental) Template for Rust-based DuckDB extensions |
| 32 | [sazgar](https://duckdb.org/community_extensions/extensions/sazgar.html) | [Sazgar](https://github.com/Angelerator/Sazgar) | 🟢 Ongoing | 12 days ago (2025-12-16 16:15:14 UTC) | 11 | Rust | Comprehensive system monitoring - CPU, memory, disk, network, processes |
| 33 | [substrait](https://duckdb.org/community_extensions/extensions/substrait.html) | [duckdb-substrait-extension](https://github.com/substrait-io/duckdb-substrait-extension) | ❓ Unknown | 12 days ago (2025-12-16 13:47:32 UTC) | 53 | C++ | DuckDB extension: substrait by substrait-io |
| 34 | [file_dialog](https://duckdb.org/community_extensions/extensions/file_dialog.html) | [duckdb-ext-file-dialog](https://github.com/yutannihilation/duckdb-ext-file-dialog) | 🟢 Ongoing | 13 days ago (2025-12-16 00:04:06 UTC) | 15 | Rust | A DuckDB extension to choose file interactively using native file open dialogs |
| 35 | [fit](https://duckdb.org/community_extensions/extensions/fit.html) | [duckdb-fit-extension](https://github.com/antoriche/duckdb-fit-extension) | 🟢 Ongoing | 13 days ago (2025-12-15 19:16:40 UTC) | 1 | C++ | DuckDB extension: fit by antoriche |
| 36 | [gsheets](https://duckdb.org/community_extensions/extensions/gsheets.html) | [duckdb_gsheets](https://github.com/evidence-dev/duckdb_gsheets) | 🟢 Ongoing | 13 days ago (2025-12-15 16:42:02 UTC) | 318 | C++ | DuckDB extension to read and write Google Sheets using SQL |
| 37 | [lsh](https://duckdb.org/community_extensions/extensions/lsh.html) | [lsh](https://github.com/princeton-ddss/lsh) | 🟢 Ongoing | 13 days ago (2025-12-15 18:21:36 UTC) | 9 | Rust | DuckDB community extension for locality-sensitive hashing (LSH) |
| 38 | [html_query](https://duckdb.org/community_extensions/extensions/html_query.html) | [duckdb_html_query](https://github.com/midwork-finds-jobs/duckdb_html_query) | 🟢 Ongoing | 14 days ago (2025-12-15 04:21:34 UTC) | 1 | Rust | Filter HTML inside duckdb |
| 39 | [psyduck](https://duckdb.org/community_extensions/extensions/psyduck.html) | [psyduck](https://github.com/Ian-Fogelman/psyduck) | 🟢 Ongoing | 14 days ago (2025-12-14 15:10:39 UTC) | 6 | C++ | Pysduck a DuckDB community extension about Pokémon. |
| 40 | [tera](https://duckdb.org/community_extensions/extensions/tera.html) | [tera](https://github.com/Query-farm/tera) | 🟢 Ongoing | 14 days ago (2025-12-14 14:20:55 UTC) | 6 | C++ | DuckDB extension: tera |
| 41 | [web_archive](https://duckdb.org/community_extensions/extensions/web_archive.html) | [duckdb-web-archive](https://github.com/midwork-finds-jobs/duckdb-web-archive) | 🟢 Ongoing | 14 days ago (2025-12-15 05:15:58 UTC) | 9 | C++ | DuckDB extension to fetch pages from common crawl |
| 42 | [webbed](https://duckdb.org/community_extensions/extensions/webbed.html) | [duckdb_webbed](https://github.com/teaguesterling/duckdb_webbed) | 🟢 Ongoing | 14 days ago (2025-12-14 20:53:17 UTC) | 38 | C++ | Web/HTTP functionality extension by teaguesterling |
| 43 | [adbc_scanner](https://duckdb.org/community_extensions/extensions/adbc_scanner.html) | [adbc_scanner](https://github.com/Query-farm/adbc_scanner) | 🟢 Ongoing | 15 days ago (2025-12-14 02:45:27 UTC) | 6 | C++ | A DuckDB ADBC Scanner Extension - adds support for using ADBC drivers with Du... |
| 44 | [datasketches](https://duckdb.org/community_extensions/extensions/datasketches.html) | [datasketches](https://github.com/Query-farm/datasketches) | 🟢 Ongoing | 16 days ago (2025-12-12 16:13:17 UTC) | 37 | C++ | Integrates DuckDB with the high-performance Apache DataSketches library. This... |
| 45 | [jsonata](https://duckdb.org/community_extensions/extensions/jsonata.html) | [jsonata](https://github.com/Query-farm/jsonata) | 🟢 Ongoing | 16 days ago (2025-12-12 13:21:15 UTC) | 2 | C++ | The JSONata extension for DuckDB enables expressive, JSON-focused querying an... |
| 46 | [gaggle](https://duckdb.org/community_extensions/extensions/gaggle.html) | [gaggle](https://github.com/CogitatorTech/gaggle) | 🟢 Ongoing | 17 days ago (2025-12-11 17:03:13 UTC) | 13 | Rust | A DuckDB extension for working with Kaggle datasets |
| 47 | [infera](https://duckdb.org/community_extensions/extensions/infera.html) | [infera](https://github.com/CogitatorTech/infera) | 🟢 Ongoing | 17 days ago (2025-12-11 07:11:16 UTC) | 116 | Rust | A DuckDB extension for in-database inference |
| 48 | [acp](https://duckdb.org/community_extensions/extensions/acp.html) | [duckdb-acp](https://github.com/sidequery/duckdb-acp) | 🟢 Ongoing | 18 days ago (2025-12-11 03:36:46 UTC) | 18 | Rust | Use Claude Code & other AI agents from inside DuckDB via extension |
| 49 | [bigquery](https://duckdb.org/community_extensions/extensions/bigquery.html) | [duckdb-bigquery](https://github.com/hafenkran/duckdb-bigquery) | 🟢 Ongoing | 18 days ago (2025-12-10 14:08:21 UTC) | 148 | C++ | Integrates DuckDB with Google BigQuery, allowing direct querying and manageme... |
| 50 | [dns](https://duckdb.org/community_extensions/extensions/dns.html) | [duckdb-dns](https://github.com/tobilg/duckdb-dns) | 🟢 Ongoing | 18 days ago (2025-12-10 17:12:12 UTC) | 14 | Rust | DNS (Reverse) Lookup Extension for DuckDB |
| 51 | [eeagrid](https://duckdb.org/community_extensions/extensions/eeagrid.html) | [duckdb-eeagrid](https://github.com/ahuarte47/duckdb-eeagrid) | 🟢 Ongoing | 18 days ago (2025-12-10 17:17:32 UTC) | 0 | C++ | Functions for transforming XY coordinates to and from the EEA Reference Grid... |
| 52 | [fakeit](https://duckdb.org/community_extensions/extensions/fakeit.html) | [duckdb-fakeit](https://github.com/tobilg/duckdb-fakeit) | 🟢 Ongoing | 18 days ago (2025-12-10 17:31:48 UTC) | 4 | Rust | DuckDB extension: fakeit by tobilg |
| 53 | [fivetran](https://duckdb.org/community_extensions/extensions/fivetran.html) | [fivetran](https://github.com/lnkuiper/fivetran) | 🟢 Ongoing | 18 days ago (2025-12-10 12:26:53 UTC) | 0 | C++ | DuckDB extension: fivetran by lnkuiper |
| 54 | [inflector](https://duckdb.org/community_extensions/extensions/inflector.html) | [inflector](https://github.com/Query-farm/inflector) | 🟢 Ongoing | 18 days ago (2025-12-10 16:06:48 UTC) | 2 | C++ | Powerful string case transformation and inflection capabilities directly to y... |
| 55 | [sheetreader](https://duckdb.org/community_extensions/extensions/sheetreader.html) | [sheetreader-duckdb](https://github.com/polydbms/sheetreader-duckdb) | ❓ Unknown | 18 days ago (2025-12-10 21:40:53 UTC) | 56 | Jupyter Notebook | DuckDB extension: sheetreader by polydbms |
| 56 | [snowflake](https://duckdb.org/community_extensions/extensions/snowflake.html) | [duckdb-snowflake](https://github.com/iqea-ai/duckdb-snowflake) | 🟢 Ongoing | 18 days ago (2025-12-10 21:41:05 UTC) | 24 | C++ | A powerful DuckDB extension that enables seamless querying of Snowflake datab... |
| 57 | [curl_httpfs](https://duckdb.org/community_extensions/extensions/curl_httpfs.html) | [duckdb-curl-filesystem](https://github.com/dentiny/duckdb-curl-filesystem) | 🟢 Ongoing | 19 days ago (2025-12-09 19:31:30 UTC) | 7 | C++ | Filesystem built upon libcurl. |
| 58 | [dash](https://duckdb.org/community_extensions/extensions/dash.html) | [dash](https://github.com/gropaul/dash) | 🟢 Ongoing | 19 days ago (2025-12-09 22:02:22 UTC) | 31 | C++ | DuckDB Extension featuring a Query Builder GUI and Dashboarding features |
| 59 | [duckdb_mcp](https://duckdb.org/community_extensions/extensions/duckdb_mcp.html) | [duckdb_mcp](https://github.com/teaguesterling/duckdb_mcp) | 🟢 Ongoing | 19 days ago (2025-12-09 16:36:19 UTC) | 21 | C++ | A simple MCP server extension for DuckDB |
| 60 | [lua](https://duckdb.org/community_extensions/extensions/lua.html) | [duckdb-lua](https://github.com/isaacbrodsky/duckdb-lua) | 🟢 Ongoing | 19 days ago (2025-12-09 19:09:42 UTC) | 8 | C++ | DuckDB extension to evaluate Lua expressions. |
| 61 | [mlpack](https://duckdb.org/community_extensions/extensions/mlpack.html) | [duckdb-mlpack](https://github.com/eddelbuettel/duckdb-mlpack) | 🟢 Ongoing | 19 days ago (2025-12-09 14:37:46 UTC) | 15 | C++ | Bringing mlpack to duckdb |
| 62 | [system_stats](https://duckdb.org/community_extensions/extensions/system_stats.html) | [system_stats](https://github.com/dentiny/system_stats) | 🟢 Ongoing | 19 days ago (2025-12-09 21:55:14 UTC) | 1 | C++ | DuckDB extension: system_stats by dentiny |
| 63 | [cwiqduck](https://duckdb.org/community_extensions/extensions/cwiqduck.html) | [cwiqduck](https://github.com/cwiq-os/cwiqduck) | 🟢 Ongoing | 20 days ago (2025-12-09 02:09:40 UTC) | 2 | C++ | DuckDB extensions for CWIQ |
| 64 | [faiss](https://duckdb.org/community_extensions/extensions/faiss.html) | [duckdb-faiss-ext](https://github.com/duckdb-faiss-ext/duckdb-faiss-ext) | 🟢 Ongoing | 20 days ago (2025-12-09 01:30:08 UTC) | 29 | Go | DuckDB wrapper for FAISS - Experimental |
| 65 | [duck_tails](https://duckdb.org/community_extensions/extensions/duck_tails.html) | [duck_tails](https://github.com/teaguesterling/duck_tails) | 🟢 Ongoing | 21 days ago (2025-12-07 20:49:06 UTC) | 9 | C++ | A DuckDB extension for exploring and reading git history. |
| 66 | [flock](https://duckdb.org/community_extensions/extensions/flock.html) | [flock](https://github.com/dais-polymtl/flock) | 🟢 Ongoing | 22 days ago (2025-12-06 23:04:48 UTC) | 286 | C++ | Flock: multimodal querying for DuckDB |
| 67 | [netquack](https://duckdb.org/community_extensions/extensions/netquack.html) | [duckdb-netquack](https://github.com/hatamiarash7/duckdb-netquack) | ❓ Unknown | 22 days ago (2025-12-06 07:03:51 UTC) | 29 | C++ | DuckDB extension for parsing, extracting, and analyzing domains, URIs, and pa... |
| 68 | [a5](https://duckdb.org/community_extensions/extensions/a5.html) | [a5](https://github.com/Query-farm/a5) | 🟢 Ongoing | 24 days ago (2025-12-04 16:09:50 UTC) | 9 | C++ | A5 Geospatial Extension for DuckDB |
| 69 | [airport](https://duckdb.org/community_extensions/extensions/airport.html) | [airport](https://github.com/Query-farm/airport) | 🟢 Ongoing | 24 days ago (2025-12-04 20:21:07 UTC) | 318 | C++ | The Airport extension for DuckDB, enables the use of Arrow Flight with DuckDB |
| 70 | [bitfilters](https://duckdb.org/community_extensions/extensions/bitfilters.html) | [bitfilters](https://github.com/Query-farm/bitfilters) | 🟢 Ongoing | 24 days ago (2025-12-04 16:09:52 UTC) | 5 | C++ | A high-performance DuckDB extension providing probabilistic data structures f... |
| 71 | [cloudfront](https://duckdb.org/community_extensions/extensions/cloudfront.html) | [duckdb-cloudfront](https://github.com/midwork-finds-jobs/duckdb-cloudfront) | 🟢 Ongoing | 24 days ago (2025-12-04 16:09:56 UTC) | 0 | C++ | DuckDB module which provides custom authentication methods on top of httpfs m... |
| 72 | [cronjob](https://duckdb.org/community_extensions/extensions/cronjob.html) | [cronjob](https://github.com/Query-farm/cronjob) | 🟢 Ongoing | 24 days ago (2025-12-04 23:24:46 UTC) | 45 | C++ | DuckDB CronJob Extension |
| 73 | [crypto](https://duckdb.org/community_extensions/extensions/crypto.html) | [crypto](https://github.com/Query-farm/crypto) | 🟢 Ongoing | 24 days ago (2025-12-04 16:09:56 UTC) | 25 | C++ | DuckDB Extension for cryptographic hash functions and HMAC |
| 74 | [evalexpr_rhai](https://duckdb.org/community_extensions/extensions/evalexpr_rhai.html) | [evalexpr_rhai](https://github.com/Query-farm/evalexpr_rhai) | 🟢 Ongoing | 24 days ago (2025-12-04 18:56:32 UTC) | 22 | C++ | A DuckDB extension to evaluate the Rhai scripting language as part of SQL. |
| 75 | [fuzzycomplete](https://duckdb.org/community_extensions/extensions/fuzzycomplete.html) | [fuzzycomplete](https://github.com/Query-farm/fuzzycomplete) | 🟢 Ongoing | 24 days ago (2025-12-04 16:10:01 UTC) | 24 | C++ | DuckDB Extension for fuzzy string matching based autocompletion |
| 76 | [hashfuncs](https://duckdb.org/community_extensions/extensions/hashfuncs.html) | [hashfuncs](https://github.com/Query-farm/hashfuncs) | 🟢 Ongoing | 24 days ago (2025-12-04 16:10:01 UTC) | 9 | C++ | A DuckDB extension that supplies non-cryptographic hash functions. |
| 77 | [http_client](https://duckdb.org/community_extensions/extensions/http_client.html) | [httpclient](https://github.com/Query-farm/httpclient) | 🟢 Ongoing | 24 days ago (2025-12-04 16:10:02 UTC) | 76 | C++ | DuckDB HTTP GET/POST Client in a Community Extension |
| 78 | [httpserver](https://duckdb.org/community_extensions/extensions/httpserver.html) | [httpserver](https://github.com/Query-farm/httpserver) | 🟢 Ongoing | 24 days ago (2025-12-04 18:26:31 UTC) | 262 | C++ | DuckDB HTTP API Server and Query Interface in a  Community Extension |
| 79 | [json_schema](https://duckdb.org/community_extensions/extensions/json_schema.html) | [json_schema](https://github.com/Query-farm/json_schema) | 🟢 Ongoing | 24 days ago (2025-12-04 19:14:15 UTC) | 1 | Python | A DuckDB extension that bring support for validating JSON data using JSON sch... |
| 80 | [lindel](https://duckdb.org/community_extensions/extensions/lindel.html) | [lindel](https://github.com/Query-farm/lindel) | 🟢 Ongoing | 24 days ago (2025-12-04 16:10:08 UTC) | 56 | C++ | DuckDB Extension Linearization/Delinearization, Z-Order, Hilbert and Morton C... |
| 81 | [marisa](https://duckdb.org/community_extensions/extensions/marisa.html) | [marisa](https://github.com/Query-farm/marisa) | 🟢 Ongoing | 24 days ago (2025-12-04 20:29:42 UTC) | 5 | C++ | The Marisa extension by Query.Farm integrates the fast, space-efficient MARIS... |
| 82 | [open_prompt](https://duckdb.org/community_extensions/extensions/open_prompt.html) | [openprompt](https://github.com/Query-farm/openprompt) | ❓ Unknown | 24 days ago (2025-12-04 23:27:33 UTC) | 53 | C++ | DuckDB Community Extension to prompt LLMs from SQL |
| 83 | [quickjs](https://duckdb.org/community_extensions/extensions/quickjs.html) | [quickjs](https://github.com/Query-farm/quickjs) | 🟢 Ongoing | 24 days ago (2025-12-04 23:29:10 UTC) | 9 | C++ | DuckDB extension: quickjs by quackscience |
| 84 | [radio](https://duckdb.org/community_extensions/extensions/radio.html) | [radio](https://github.com/Query-farm/radio) | 🟢 Ongoing | 24 days ago (2025-12-04 16:10:12 UTC) | 35 | C++ | Radio is a DuckDB extension by Query.Farm that brings real-time event streams... |
| 85 | [rapidfuzz](https://duckdb.org/community_extensions/extensions/rapidfuzz.html) | [rapidfuzz](https://github.com/Query-farm/rapidfuzz) | 🟢 Ongoing | 24 days ago (2025-12-04 16:10:12 UTC) | 9 | C++ | DuckDB Community Extension adding RapidFuzz algorithms for search, deduplicat... |
| 86 | [redis](https://duckdb.org/community_extensions/extensions/redis.html) | [redis](https://github.com/Query-farm/redis) | 🟢 Ongoing | 24 days ago (2025-12-04 23:42:10 UTC) | 8 | C++ | DuckDB Redis Client community extension |
| 87 | [shellfs](https://duckdb.org/community_extensions/extensions/shellfs.html) | [shellfs](https://github.com/Query-farm/shellfs) | 🟢 Ongoing | 24 days ago (2025-12-04 18:51:18 UTC) | 88 | C++ | DuckDB extension allowing shell commands to be used for input and output. |
| 88 | [stochastic](https://duckdb.org/community_extensions/extensions/stochastic.html) | [stochastic](https://github.com/Query-farm/stochastic) | 🟢 Ongoing | 24 days ago (2025-12-04 16:10:15 UTC) | 13 | C++ | A DuckDB extension that add comprehensive statistical distribution functions... |
| 89 | [textplot](https://duckdb.org/community_extensions/extensions/textplot.html) | [textplot](https://github.com/Query-farm/textplot) | 🟢 Ongoing | 24 days ago (2025-12-04 16:10:17 UTC) | 13 | C++ | A DuckDB community extension that enables text-based data visualization direc... |
| 90 | [tributary](https://duckdb.org/community_extensions/extensions/tributary.html) | [tributary](https://github.com/Query-farm/tributary) | 🟢 Ongoing | 24 days ago (2025-12-04 16:10:18 UTC) | 51 | C++ | A DuckDB Extension for Kafka |
| 91 | [tsid](https://duckdb.org/community_extensions/extensions/tsid.html) | [tsid](https://github.com/Query-farm/tsid) | 🟢 Ongoing | 24 days ago (2025-12-04 23:54:00 UTC) | 5 | C++ | TSID Extension for DuckDB  |
| 92 | [webmacro](https://duckdb.org/community_extensions/extensions/webmacro.html) | [webmacro](https://github.com/Query-farm/webmacro) | 🟢 Ongoing | 24 days ago (2025-12-05 00:15:35 UTC) | 14 | C++ | DuckDB WebMacro: Share and Load your SQL Macros via gists |
| 93 | [gcs](https://duckdb.org/community_extensions/extensions/gcs.html) | [duckdb-gcs](https://github.com/northpolesec/duckdb-gcs) | 🟢 Ongoing | 26 days ago (2025-12-02 12:17:16 UTC) | 8 | C++ | A GCS-native extension for DuckDB |
| 94 | [nanodbc](https://duckdb.org/community_extensions/extensions/nanodbc.html) | [duckdb-nanodbc-extension](https://github.com/Hugoberry/duckdb-nanodbc-extension) | 🟢 Ongoing | 26 days ago (2025-12-02 16:24:39 UTC) | 48 | C++ | Database connectivity extension by Hugoberry |
| 95 | [onelake](https://duckdb.org/community_extensions/extensions/onelake.html) | [duckdb_onelake](https://github.com/datumnova/duckdb_onelake) | ❓ Unknown | 27 days ago (2025-12-01 10:28:22 UTC) | 18 | C++ | DuckDB extension: onelake by datumnova |
| 96 | [warc](https://duckdb.org/community_extensions/extensions/warc.html) | [duckdb_warc](https://github.com/midwork-finds-jobs/duckdb_warc) | ❓ Unknown | 28 days ago (2025-11-30 19:41:21 UTC) | 1 | Rust | DuckDB extension for parsing WARC files |
| 97 | [yaml](https://duckdb.org/community_extensions/extensions/yaml.html) | [duckdb_yaml](https://github.com/teaguesterling/duckdb_yaml) | 🟢 Ongoing | 28 days ago (2025-11-30 23:52:59 UTC) | 10 | C++ |  A DuckDB to read and work with YAML files in a similar way to JSON files (al... |
| 98 | [quackstore](https://duckdb.org/community_extensions/extensions/quackstore.html) | [QuackStore](https://github.com/coginiti-dev/QuackStore) | ❓ Unknown | 31 days ago (2025-11-27 16:15:12 UTC) | 109 | C++ | DuckDB extension: quackstore by coginiti-dev |
| 99 | [read_stat](https://duckdb.org/community_extensions/extensions/read_stat.html) | [duckdb-read-stat](https://github.com/mettekou/duckdb-read-stat) | 🟢 Ongoing | 31 days ago (2025-11-27 13:46:07 UTC) | 26 | C | Read data sets from SAS, Stata, and SPSS from DuckDB with ReadStat |
| 100 | [duck_delta_share](https://duckdb.org/community_extensions/extensions/duck_delta_share.html) | [duck_delta_share](https://github.com/cwiq-os/duck_delta_share) | 🟢 Ongoing | 35 days ago (2025-11-24 00:43:03 UTC) | 1 | C++ | DuckDB extension for enabling Delta Sharing client capabilities.  |
| 101 | [sshfs](https://duckdb.org/community_extensions/extensions/sshfs.html) | [duckdb-sshfs](https://github.com/midwork-finds-jobs/duckdb-sshfs) | ❓ Unknown | 41 days ago (2025-11-17 11:24:29 UTC) | 1 | C++ | DuckDB sshfs extension - Read and write files through ssh inside DuckDB |
| 102 | [webdavfs](https://duckdb.org/community_extensions/extensions/webdavfs.html) | [duckdb-webdavfs](https://github.com/midwork-finds-jobs/duckdb-webdavfs) | ❓ Unknown | 42 days ago (2025-11-16 18:45:25 UTC) | 1 | C++ | DuckDB WebDAVfs Extension - WebDAV filesystem support for DuckDB |
| 103 | [otlp](https://duckdb.org/community_extensions/extensions/otlp.html) | [duckdb-otlp](https://github.com/smithclay/duckdb-otlp) | 🟢 Ongoing | 43 days ago (2025-11-15 19:34:51 UTC) | 31 | C++ | query OpenTelemetry metrics, logs, and traces (OTLP) in duckdb |
| 104 | [miniplot](https://duckdb.org/community_extensions/extensions/miniplot.html) | [miniplot](https://github.com/nkwork9999/miniplot) | 🟢 Ongoing | 44 days ago (2025-11-15 02:42:43 UTC) | 15 | C++ | DuckDB extension: miniplot by nkwork9999 |
| 105 | [nats_js](https://duckdb.org/community_extensions/extensions/nats_js.html) | [duckdb-nats-jetstream](https://github.com/brannn/duckdb-nats-jetstream) | 🟢 Ongoing | 44 days ago (2025-11-14 07:24:21 UTC) | 7 | C++ | DuckDB extension for querying NATS JetStream message streams with SQL |
| 106 | [splink_udfs](https://duckdb.org/community_extensions/extensions/splink_udfs.html) | [splink_udfs](https://github.com/moj-analytical-services/splink_udfs) | ❓ Unknown | 44 days ago (2025-11-14 14:37:49 UTC) | 15 | C++ | DuckDB extension: splink_udfs by moj-analytical-services |
| 107 | [bvh2sql](https://duckdb.org/community_extensions/extensions/bvh2sql.html) | [bvh2sql](https://github.com/nkwork9999/bvh2sql) | 🟢 Ongoing | 56 days ago (2025-11-02 18:17:05 UTC) | 0 | Makefile | SQL-related extension by nkwork9999 |
| 108 | [mooncake](https://duckdb.org/community_extensions/extensions/mooncake.html) | [duckdb_mooncake](https://github.com/Mooncake-Labs/duckdb_mooncake) | 🟢 Ongoing | 63 days ago (2025-10-26 07:13:05 UTC) | 4 | C++ | Read Iceberg tables written by moonlink in real time |
| 109 | [pbix](https://duckdb.org/community_extensions/extensions/pbix.html) | [duckdb-pbix-extension](https://github.com/Hugoberry/duckdb-pbix-extension) | 🟢 Ongoing | 65 days ago (2025-10-24 13:47:34 UTC) | 31 | C++ | Duckdb extension for parsing the metadata and contents of the embedded data m... |
| 110 | [cassandra](https://duckdb.org/community_extensions/extensions/cassandra.html) | [duckdb-cassandra](https://github.com/dioptre/duckdb-cassandra) | 🟢 Ongoing | 69 days ago (2025-10-20 19:15:10 UTC) | 0 | C++ | DuckDB Connector for Cassandra |
| 111 | [encoding](https://duckdb.org/community_extensions/extensions/encoding.html) | [duckdb-encoding](https://github.com/onnimonni/duckdb-encoding) | ❓ Unknown | 72 days ago (2025-10-17 06:53:16 UTC) | 2 | Rust | DuckDB extension: encoding by onnimonni |
| 112 | [hdf5](https://duckdb.org/community_extensions/extensions/hdf5.html) | [duckdb-hdf5](https://github.com/Berrysoft/duckdb-hdf5) | ❓ Unknown | 74 days ago (2025-10-15 17:27:39 UTC) | 12 | Rust | HDF5 plugin for duckdb |
| 113 | [title_mapper](https://duckdb.org/community_extensions/extensions/title_mapper.html) | [duckdb-title-mapper](https://github.com/martin-conur/duckdb-title-mapper) | ❓ Unknown | 77 days ago (2025-10-12 22:54:26 UTC) | 2 | Rust | DuckDB extension: title_mapper by martin-conur |
| 114 | [blockduck](https://duckdb.org/community_extensions/extensions/blockduck.html) | [BlockDuck](https://github.com/luohaha/BlockDuck) | 🟢 Ongoing | 81 days ago (2025-10-08 16:19:04 UTC) | 10 | C++ | Live SQL Queries on Blockchain |
| 115 | [arrow](https://duckdb.org/community_extensions/extensions/arrow.html) | [duckdb-extension-alias](https://github.com/duckdb/duckdb-extension-alias) | ❓ Unknown | 83 days ago (2025-10-06 09:07:38 UTC) | 5 | C | DuckDB extension: arrow |
| 116 | [geography](https://duckdb.org/community_extensions/extensions/geography.html) | [duckdb-geography](https://github.com/paleolimbot/duckdb-geography) | 🟢 Ongoing | 87 days ago (2025-10-02 11:09:38 UTC) | 35 | C++ | Geospatial data extension by paleolimbot |
| 117 | [hostfs](https://duckdb.org/community_extensions/extensions/hostfs.html) | [hostFS](https://github.com/gropaul/hostFS) | ❓ Unknown | 88 days ago (2025-10-01 21:02:13 UTC) | 28 | C++ | DuckDB extension: hostfs by gropaul |
| 118 | [magic](https://duckdb.org/community_extensions/extensions/magic.html) | [duckdb_magic](https://github.com/carlopi/duckdb_magic) | 🟢 Ongoing | 92 days ago (2025-09-27 18:50:32 UTC) | 7 | C++ | Auto-detect file types via `libmagic` (`file` utility) |
| 119 | [msolap](https://duckdb.org/community_extensions/extensions/msolap.html) | [duckdb-msolap-extension](https://github.com/Hugoberry/duckdb-msolap-extension) | 🟢 Ongoing | 95 days ago (2025-09-24 16:33:46 UTC) | 12 | C++ | DuckDB extension: msolap by Hugoberry |
| 120 | [parser_tools](https://duckdb.org/community_extensions/extensions/parser_tools.html) | [duckdb_extension_parser_tools](https://github.com/hotdata-dev/duckdb_extension_parser_tools) | 🟢 Ongoing | 95 days ago (2025-09-24 17:46:33 UTC) | 22 | C++ | Parse sql - with sql! |
| 121 | [chsql](https://duckdb.org/community_extensions/extensions/chsql.html) | [clickhouse-sql](https://github.com/Query-farm/clickhouse-sql) | ❓ Unknown | 96 days ago (2025-09-23 19:24:33 UTC) | 85 | C++ | DuckDB Community Extension implementing ClickHouse SQL Dialect macros and Cus... |
| 122 | [chsql_native](https://duckdb.org/community_extensions/extensions/chsql_native.html) | [clickhouse-native](https://github.com/Query-farm/clickhouse-native) | ❓ Unknown | 96 days ago (2025-09-23 19:24:31 UTC) | 17 | Rust | Experimental ClickHouse Native Client and Native file reader Extension for Du... |
| 123 | [pcap_reader](https://duckdb.org/community_extensions/extensions/pcap_reader.html) | [pcap](https://github.com/Query-farm/pcap) | ❓ Unknown | 96 days ago (2025-09-23 19:24:42 UTC) | 11 | Rust | DuckDB PCAP Reader Extension made in Rust |
| 124 | [pyroscope](https://duckdb.org/community_extensions/extensions/pyroscope.html) | [pyroscope](https://github.com/Query-farm/pyroscope) | ❓ Unknown | 96 days ago (2025-09-23 19:24:44 UTC) | 20 | Rust | DuckDB Pyroscope Extension for Continuous Profiling |
| 125 | [wireduck](https://duckdb.org/community_extensions/extensions/wireduck.html) | [wireduck](https://github.com/hyehudai/wireduck) | 🟢 Ongoing | 96 days ago (2025-09-23 21:22:03 UTC) | 47 | C++ | Duckdb extension to read pcap files |
| 126 | [prql](https://duckdb.org/community_extensions/extensions/prql.html) | [duckdb-prql](https://github.com/ywelsch/duckdb-prql) | 🟢 Ongoing | 97 days ago (2025-09-22 18:45:53 UTC) | 313 | C++ | PRQL as a DuckDB extension |
| 127 | [psql](https://duckdb.org/community_extensions/extensions/psql.html) | [duckdb-psql](https://github.com/ywelsch/duckdb-psql) | 🟢 Ongoing | 97 days ago (2025-09-22 18:45:44 UTC) | 100 | C++ | A piped SQL for DuckDB |
| 128 | [chaos](https://duckdb.org/community_extensions/extensions/chaos.html) | [duckdb-chaos](https://github.com/taniabogatsch/duckdb-chaos) | 🟢 Ongoing | 100 days ago (2025-09-19 11:42:23 UTC) | 0 | C++ | DuckDB extension: chaos by taniabogatsch |
| 129 | [nanoarrow](https://duckdb.org/community_extensions/extensions/nanoarrow.html) | [duckdb-nanoarrow](https://github.com/paleolimbot/duckdb-nanoarrow) | ❓ Unknown | 102 days ago (2025-09-17 18:31:44 UTC) | 60 | C++ | DuckDB extension: nanoarrow by paleolimbot |
| 130 | [geotiff](https://duckdb.org/community_extensions/extensions/geotiff.html) | [duckdb-geotiff](https://github.com/babaknaimi/duckdb-geotiff) | ❓ Unknown | 131 days ago (2025-08-20 05:12:15 UTC) | 2 | C++ | Duckdb extension to read GeoTiffs directly with duckdb database |
| 131 | [highs](https://duckdb.org/community_extensions/extensions/highs.html) | [HiGHS-duckdb](https://github.com/fhk/HiGHS-duckdb) | ❓ Unknown | 134 days ago (2025-08-16 06:41:18 UTC) | 1 | C++ | Run the solver in the database! |
| 132 | [jwt](https://duckdb.org/community_extensions/extensions/jwt.html) | [duckdb_jwt](https://github.com/GalvinGao/duckdb_jwt) | ❓ Unknown | 173 days ago (2025-07-09 00:13:56 UTC) | 0 | C++ | DuckDB extension: jwt by GalvinGao |
| 133 | [ofquack](https://duckdb.org/community_extensions/extensions/ofquack.html) | [ofquack](https://github.com/krokozyab/ofquack) | ❓ Unknown | 250 days ago (2025-04-22 12:24:17 UTC) | 5 | C++ | Oracle Fusion DuckDB extension  |
| 134 | [scrooge](https://duckdb.org/community_extensions/extensions/scrooge.html) | [Scrooge-McDuck](https://github.com/pdet/Scrooge-McDuck) | ❓ Unknown | 258 days ago (2025-04-14 11:16:07 UTC) | 151 | C++ | DuckDB extension: scrooge by pdet |
| 135 | [pivot_table](https://duckdb.org/community_extensions/extensions/pivot_table.html) | [pivot_table](https://github.com/Alex-Monahan/pivot_table) | ❓ Unknown | over a year ago (2024-09-22 21:18:45 UTC) | 17 | C++ | Full spreadsheet-style pivot table through SQL macros. Just specify values, r... |
| 136 | [tarfs](https://duckdb.org/community_extensions/extensions/tarfs.html) | [duckdb_tarfs](https://github.com/Maxxen/duckdb_tarfs) | ❓ Unknown | over a year ago (2024-08-26 11:01:47 UTC) | 11 | C++ | DuckDB extension: tarfs by Maxxen |
| 137 | [ulid](https://duckdb.org/community_extensions/extensions/ulid.html) | [duckdb_ulid](https://github.com/Maxxen/duckdb_ulid) | ❓ Unknown | over a year ago (2024-07-09 09:35:50 UTC) | 24 | C++ | DuckDB extension: ulid by Maxxen |

**Total:** 137 extensions
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
