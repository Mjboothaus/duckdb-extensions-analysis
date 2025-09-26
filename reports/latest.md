# DuckDB Extensions Analysis

🦆 **Automated monitoring and analysis of DuckDB's extension ecosystem**


[Jump to Summary](#summary) | [Core Extensions](#core-extensions) | [Community Extensions](#community-extensions) | [URL Validation](#url-validation-results)

---

This report provides a comprehensive analysis of DuckDB extensions, including both core extensions (built into DuckDB) and community-contributed extensions.

## Data Sources

This analysis is based on the following authoritative sources:

### Core Extensions
- **Overview**: [DuckDB Extensions](https://duckdb.org/docs/stable/extensions/overview.html)
- **Core Extensions**: [Core Extensions Documentation](https://duckdb.org/docs/stable/core_extensions/overview.html)
- **Versioning**: [Extension Versioning](https://duckdb.org/docs/stable/extensions/versioning_of_extensions.html)
- **Repository**: [duckdb/duckdb](https://github.com/duckdb/duckdb)
- **Releases**: [GitHub Releases](https://github.com/duckdb/duckdb/releases)

### Community Extensions
- **Registry**: [Community Extensions Repository](https://github.com/duckdb/community-extensions)
- **Directory**: [Extensions Folder](https://github.com/duckdb/community-extensions/tree/main/extensions)
- **Featured**: [Community Extensions Page](https://community-extensions.duckdb.org/)
- **Individual Repositories**: GitHub repositories linked in the extensions directory

---
## Summary

| **Metric** | **Count** |
|------------|-----------|
| **Core Extensions** | 24 |
| **Community Extensions** | 83 |
| **Featured Extensions** | 41 |
| **Total Extensions** | 107 |
| **Recently Active** (≤ 30 days) | 59 |
| **Very Active** (≤ 7 days) | 52 |


---
## Core Extensions

Core extensions maintained by the DuckDB team and distributed via the official extension repository

| # | Extension | Repository | Status | Last Activity | Stars | Language | Description |
|---|-----------|------------|--------|---------------|-------|----------|-------------|
| 1 | [autocomplete](https://duckdb.org/docs/stable/core_extensions/autocomplete.html) | [duckdb/duckdb](https://github.com/duckdb/duckdb/tree/main/extension/autocomplete) | 🟢 Ongoing | 8 days ago | 0 | C++ | Core DuckDB extension: autocomplete |
| 2 | [avro](https://duckdb.org/docs/stable/core_extensions/avro.html) | [duckdb-avro](https://github.com/duckdb/duckdb-avro) | 🟢 Ongoing | 37 days ago | 0 | C++ | Apache Avro format support |
| 3 | [aws](https://duckdb.org/docs/stable/core_extensions/aws.html) | [duckdb-aws](https://github.com/duckdb/duckdb-aws) | 🟢 Ongoing | 17 days ago | 0 | C++ | AWS S3 integration |
| 4 | [azure](https://duckdb.org/docs/stable/core_extensions/azure.html) | [duckdb-azure](https://github.com/duckdb/duckdb-azure) | 🟢 Ongoing | 7 days ago | 0 | C++ | Azure Blob Storage integration |
| 5 | [delta](https://duckdb.org/docs/stable/core_extensions/delta.html) | [duckdb-delta](https://github.com/duckdb/duckdb-delta) | 🟢 Ongoing | today | 0 | C++ | Delta Lake format support |
| 6 | [ducklake](https://duckdb.org/docs/stable/core_extensions/ducklake.html) | [duckdb/ducklake](https://github.com/duckdb/ducklake) | 🟢 Ongoing | 9 days ago | 0 | C++ | Delta Lake support via DuckLake (different from delta extension) |
| 7 | [encodings](https://duckdb.org/docs/stable/core_extensions/encodings.html) | [duckdb-encodings](https://github.com/duckdb/duckdb-encodings) | 🟢 Ongoing | 8 days ago | 0 | C++ | Character encoding support |
| 8 | [excel](https://duckdb.org/docs/stable/core_extensions/excel.html) | [duckdb-excel](https://github.com/duckdb/duckdb-excel) | 🟢 Ongoing | 22 days ago | 0 | C++ | Excel file format support |
| 9 | [fts](https://duckdb.org/docs/stable/core_extensions/full_text_search.html) | [duckdb-fts](https://github.com/duckdb/duckdb-fts) | 🟢 Ongoing | 9 days ago | 0 | C++ | Full-text search functionality |
| 10 | [httpfs](https://duckdb.org/docs/stable/core_extensions/httpfs/overview.html) | [duckdb-httpfs](https://github.com/duckdb/duckdb-httpfs) | 🟢 Ongoing | today | 0 | C++ | HTTP/S3 filesystem support |
| 11 | [iceberg](https://duckdb.org/docs/stable/core_extensions/iceberg/overview.html) | [duckdb-iceberg](https://github.com/duckdb/duckdb-iceberg) | 🟢 Ongoing | today | 0 | C++ | Apache Iceberg format support |
| 12 | [icu](https://duckdb.org/docs/stable/core_extensions/icu.html) | [duckdb/duckdb](https://github.com/duckdb/duckdb/tree/main/extension/icu) | 🟢 Ongoing | 9 days ago | 0 | C++ | Core DuckDB extension: icu |
| 13 | [inet](https://duckdb.org/docs/stable/core_extensions/inet.html) | [duckdb-inet](https://github.com/duckdb/duckdb-inet) | 🟢 Ongoing | 6 days ago | 0 | C++ | Internet address data types |
| 14 | [jemalloc](https://duckdb.org/docs/stable/core_extensions/jemalloc.html) | [duckdb/duckdb](https://github.com/duckdb/duckdb/tree/main/extension/jemalloc) | 🟢 Ongoing | 110 days ago | 0 | C++ | Core DuckDB extension: jemalloc |
| 15 | [json](https://duckdb.org/docs/stable/data/json/overview.html) | [duckdb/duckdb](https://github.com/duckdb/duckdb/tree/main/extension/json) | 🟢 Ongoing | 16 days ago | 0 | C++ | Core DuckDB extension: json |
| 16 | [mysql](https://duckdb.org/docs/stable/core_extensions/mysql.html) | [duckdb-mysql](https://github.com/duckdb/duckdb-mysql) | 🟢 Ongoing | 18 days ago | 0 | C++ | MySQL database connectivity |
| 17 | [parquet](https://duckdb.org/docs/stable/data/parquet/overview.html) | [duckdb/duckdb](https://github.com/duckdb/duckdb/tree/main/extension/parquet) | 🟢 Ongoing | 2 days ago | 0 | C++ | Core DuckDB extension: parquet |
| 18 | [postgres](https://duckdb.org/docs/stable/core_extensions/postgres.html) | [duckdb-postgres](https://github.com/duckdb/duckdb-postgres) | 🟢 Ongoing | 9 days ago | 0 | C++ | PostgreSQL database connectivity |
| 19 | [spatial](https://duckdb.org/docs/stable/core_extensions/spatial/overview.html) | [duckdb-spatial](https://github.com/duckdb/duckdb-spatial) | 🟢 Ongoing | today | 0 | C++ | Geospatial data types and functions |
| 20 | [sqlite](https://duckdb.org/docs/stable/core_extensions/sqlite.html) | [duckdb-sqlite](https://github.com/duckdb/duckdb-sqlite) | 🟢 Ongoing | 9 days ago | 0 | C++ | SQLite database connectivity |
| 21 | [tpcds](https://duckdb.org/docs/stable/core_extensions/tpcds.html) | [duckdb/duckdb](https://github.com/duckdb/duckdb/tree/main/extension/tpcds) | 🟢 Ongoing | 51 days ago | 0 | C++ | Core DuckDB extension: tpcds |
| 22 | [tpch](https://duckdb.org/docs/stable/core_extensions/tpch.html) | [duckdb/duckdb](https://github.com/duckdb/duckdb/tree/main/extension/tpch) | 🟢 Ongoing | 51 days ago | 0 | C++ | Core DuckDB extension: tpch |
| 23 | [ui](https://duckdb.org/docs/stable/core_extensions/ui.html) | [duckdb-ui](https://github.com/duckdb/duckdb-ui) | 🟢 Ongoing | 9 days ago | 0 | C++ | Browser-based user interface for DuckDB |
| 24 | [vss](https://duckdb.org/docs/stable/core_extensions/vss.html) | [duckdb-vss](https://github.com/duckdb/duckdb-vss) | 🟢 Ongoing | 20 days ago | 0 | C++ | Vector similarity search |

**Total:** 24 extensions

---
---
## Community Extensions

Third-party extensions maintained by the community

| # | Extension | Repository | Status | Last Activity | Stars | Language | Description | Featured |
|---|-----------|------------|--------|---------------|-------|----------|-------------|----------|
| 1 | [datasketches](https://duckdb.org/docs/extensions/community_extensions.html#datasketches) | [datasketches](https://github.com/Query-farm/datasketches) | 🟢 Ongoing | today | 27 | C++ | Integrates DuckDB with the high-performance Apache DataSketches library. This... | ⭐ |
| 2 | [fuzzycomplete](https://duckdb.org/docs/extensions/community_extensions.html#fuzzycomplete) | [fuzzycomplete](https://github.com/Query-farm/fuzzycomplete) | 🟢 Ongoing | today | 21 | C++ | DuckDB Extension for fuzzy string matching based autocompletion | ⭐ |
| 3 | [h3](https://duckdb.org/docs/extensions/community_extensions.html#h3) | [h3-duckdb](https://github.com/isaacbrodsky/h3-duckdb) | 🟢 Ongoing | today | 221 | C++ | Bindings for H3 to DuckDB |  |
| 4 | [hashfuncs](https://duckdb.org/docs/extensions/community_extensions.html#hashfuncs) | [hashfuncs](https://github.com/Query-farm/hashfuncs) | 🟢 Ongoing | today | 4 | C++ | A DuckDB extension that supplies non-cryptographic hash functions. | ⭐ |
| 5 | [lindel](https://duckdb.org/docs/extensions/community_extensions.html#lindel) | [lindel](https://github.com/Query-farm/lindel) | 🟢 Ongoing | today | 50 | C++ | DuckDB Extension Linearization/Delinearization, Z-Order, Hilbert and Morton C... | ⭐ |
| 6 | [marisa](https://duckdb.org/docs/extensions/community_extensions.html#marisa) | [marisa](https://github.com/Query-farm/marisa) | 🟢 Ongoing | today | 2 | C++ | The Marisa extension by Query.Farm integrates the fast, space-efficient MARIS... | ⭐ |
| 7 | [pbix](https://duckdb.org/docs/extensions/community_extensions.html#pbix) | [duckdb-pbix-extension](https://github.com/Hugoberry/duckdb-pbix-extension) | 🟢 Ongoing | today | 27 | C++ | Duckdb extension for parsing the metadata and contents of the embedded data m... | ⭐ |
| 8 | [stochastic](https://duckdb.org/docs/extensions/community_extensions.html#stochastic) | [stochastic](https://github.com/Query-farm/stochastic) | 🟢 Ongoing | today | 11 | C++ | A DuckDB extension that add comprehensive statistical distribution functions... | ⭐ |
| 9 | [textplot](https://duckdb.org/docs/extensions/community_extensions.html#textplot) | [textplot](https://github.com/Query-farm/textplot) | 🟢 Ongoing | today | 10 | C++ | A DuckDB community extension that enables text-based data visualization direc... | ⭐ |
| 10 | [tributary](https://duckdb.org/docs/extensions/community_extensions.html#tributary) | [tributary](https://github.com/Query-farm/tributary) | 🟢 Ongoing | today | 30 | C++ | A DuckDB Extension for Kafka | ⭐ |
| 11 | [vortex](https://duckdb.org/docs/extensions/community_extensions.html#vortex) | [duckdb-vortex](https://github.com/vortex-data/duckdb-vortex) | 🟢 Ongoing | today | 24 | Shell | DuckDB extension allowing reading/writing of vortex files |  |
| 12 | [httpserver](https://duckdb.org/docs/extensions/community_extensions.html#httpserver) | [httpserver](https://github.com/Query-farm/httpserver) | 🟢 Ongoing | today | 231 | HTML | DuckDB HTTP API Server and Query Interface in a  Community Extension |  |
| 13 | [msolap](https://duckdb.org/docs/extensions/community_extensions.html#msolap) | [duckdb-msolap-extension](https://github.com/Hugoberry/duckdb-msolap-extension) | 🟢 Ongoing | today | 8 | C++ | DuckDB extension: msolap by Hugoberry |  |
| 14 | [nanodbc](https://duckdb.org/docs/extensions/community_extensions.html#nanodbc) | [duckdb-nanodbc-extension](https://github.com/Hugoberry/duckdb-nanodbc-extension) | 🟢 Ongoing | today | 37 | C++ | Database connectivity extension by Hugoberry | ⭐ |
| 15 | [netquack](https://duckdb.org/docs/extensions/community_extensions.html#netquack) | [duckdb-netquack](https://github.com/hatamiarash7/duckdb-netquack) | 🟢 Ongoing | today | 17 | C++ | DuckDB extension for parsing, extracting, and analyzing domains, URIs, and pa... |  |
| 16 | [parser_tools](https://duckdb.org/docs/extensions/community_extensions.html#parser_tools) | [duckdb_extension_parser_tools](https://github.com/zfarrell/duckdb_extension_parser_tools) | 🟢 Ongoing | today | 15 | C++ | Parse sql - with sql! | ⭐ |
| 17 | [radio](https://duckdb.org/docs/extensions/community_extensions.html#radio) | [radio](https://github.com/Query-farm/radio) | 🟢 Ongoing | today | 30 | C++ | Radio is a DuckDB extension by Query.Farm that brings real-time event streams... | ⭐ |
| 18 | [splink_udfs](https://duckdb.org/docs/extensions/community_extensions.html#splink_udfs) | [splink_udfs](https://github.com/moj-analytical-services/splink_udfs) | 🟢 Ongoing | today | 9 | C++ | DuckDB extension: splink_udfs by moj-analytical-services | ⭐ |
| 19 | [airport](https://duckdb.org/docs/extensions/community_extensions.html#airport) | [airport](https://github.com/Query-farm/airport) | 🟢 Ongoing | 2 days ago | 299 | C++ | The Airport extension for DuckDB, enables the use of Arrow Flight with DuckDB | ⭐ |
| 20 | [bitfilters](https://duckdb.org/docs/extensions/community_extensions.html#bitfilters) | [bitfilters](https://github.com/Query-farm/bitfilters) | 🟢 Ongoing | 2 days ago | 2 | C++ | A high-performance DuckDB extension providing probabilistic data structures f... | ⭐ |
| 21 | [cache_httpfs](https://duckdb.org/docs/extensions/community_extensions.html#cache_httpfs) | [duck-read-cache-fs](https://github.com/dentiny/duck-read-cache-fs) | 🟢 Ongoing | 2 days ago | 97 | C++ | This repository is made as read-only filesystem for remote access. | ⭐ |
| 22 | [chsql](https://duckdb.org/docs/extensions/community_extensions.html#chsql) | [clickhouse-sql](https://github.com/Query-farm/clickhouse-sql) | 🟢 Ongoing | 2 days ago | 72 | C++ | DuckDB Community Extension implementing ClickHouse SQL Dialect macros and Cus... |  |
| 23 | [chsql_native](https://duckdb.org/docs/extensions/community_extensions.html#chsql_native) | [clickhouse-native](https://github.com/Query-farm/clickhouse-native) | 🟢 Ongoing | 2 days ago | 16 | Rust | Experimental ClickHouse Native Client and Native file reader Extension for Du... |  |
| 24 | [cronjob](https://duckdb.org/docs/extensions/community_extensions.html#cronjob) | [cronjob](https://github.com/Query-farm/cronjob) | 🟢 Ongoing | 2 days ago | 41 | C++ | DuckDB CronJob Extension |  |
| 25 | [crypto](https://duckdb.org/docs/extensions/community_extensions.html#crypto) | [crypto](https://github.com/Query-farm/crypto) | 🟢 Ongoing | 2 days ago | 22 | C++ | DuckDB Extension for cryptographic hash functions and HMAC | ⭐ |
| 26 | [evalexpr_rhai](https://duckdb.org/docs/extensions/community_extensions.html#evalexpr_rhai) | [evalexpr_rhai](https://github.com/Query-farm/evalexpr_rhai) | 🟢 Ongoing | 2 days ago | 21 | C++ | A DuckDB extension to evaluate the Rhai scripting language as part of SQL. | ⭐ |
| 27 | [http_client](https://duckdb.org/docs/extensions/community_extensions.html#http_client) | [httpclient](https://github.com/Query-farm/httpclient) | 🟢 Ongoing | 2 days ago | 71 | C++ | DuckDB HTTP GET/POST Client in a Community Extension |  |
| 28 | [observefs](https://duckdb.org/docs/extensions/community_extensions.html#observefs) | [duckdb-filesystem-observability](https://github.com/dentiny/duckdb-filesystem-observability) | 🟢 Ongoing | 2 days ago | 1 | C++ | Provides observability for duckdb filesystem. | ⭐ |
| 29 | [open_prompt](https://duckdb.org/docs/extensions/community_extensions.html#open_prompt) | [openprompt](https://github.com/Query-farm/openprompt) | 🟢 Ongoing | 2 days ago | 50 | C++ | DuckDB Community Extension to prompt LLMs from SQL |  |
| 30 | [pcap_reader](https://duckdb.org/docs/extensions/community_extensions.html#pcap_reader) | [pcap](https://github.com/Query-farm/pcap) | 🟢 Ongoing | 2 days ago | 11 | Rust | DuckDB PCAP Reader Extension made in Rust |  |
| 31 | [pyroscope](https://duckdb.org/docs/extensions/community_extensions.html#pyroscope) | [pyroscope](https://github.com/Query-farm/pyroscope) | 🟢 Ongoing | 2 days ago | 19 | Rust | DuckDB Pyroscope Extension for Continuous Profiling |  |
| 32 | [quickjs](https://duckdb.org/docs/extensions/community_extensions.html#quickjs) | [quickjs](https://github.com/Query-farm/quickjs) | 🟢 Ongoing | 2 days ago | 8 | C++ | DuckDB extension: quickjs by quackscience | ⭐ |
| 33 | [rapidfuzz](https://duckdb.org/docs/extensions/community_extensions.html#rapidfuzz) | [rapidfuzz](https://github.com/Query-farm/rapidfuzz) | 🟢 Ongoing | 2 days ago | 3 | C++ | DuckDB Community Extension adding RapidFuzz algorithms for search, deduplicat... | ⭐ |
| 34 | [redis](https://duckdb.org/docs/extensions/community_extensions.html#redis) | [redis](https://github.com/Query-farm/redis) | 🟢 Ongoing | 2 days ago | 7 | C++ | DuckDB Redis Client community extension |  |
| 35 | [shellfs](https://duckdb.org/docs/extensions/community_extensions.html#shellfs) | [shellfs](https://github.com/Query-farm/shellfs) | 🟢 Ongoing | 2 days ago | 81 | C++ | DuckDB extension allowing shell commands to be used for input and output. | ⭐ |
| 36 | [snowflake](https://duckdb.org/docs/extensions/community_extensions.html#snowflake) | [duckdb-snowflake](https://github.com/iqea-ai/duckdb-snowflake) | 🟢 Ongoing | 2 days ago | 12 | C++ | A powerful DuckDB extension that enables seamless querying of Snowflake datab... | ⭐ |
| 37 | [tsid](https://duckdb.org/docs/extensions/community_extensions.html#tsid) | [tsid](https://github.com/Query-farm/tsid) | 🟢 Ongoing | 2 days ago | 5 | C++ | TSID Extension for DuckDB  |  |
| 38 | [webmacro](https://duckdb.org/docs/extensions/community_extensions.html#webmacro) | [webmacro](https://github.com/Query-farm/webmacro) | 🟢 Ongoing | 2 days ago | 13 | C++ | DuckDB WebMacro: Share and Load your SQL Macros via gists |  |
| 39 | [wireduck](https://duckdb.org/docs/extensions/community_extensions.html#wireduck) | [wireduck](https://github.com/hyehudai/wireduck) | 🟢 Ongoing | 2 days ago | 46 | C++ | Duckdb extension to read pcap files | ⭐ |
| 40 | [magic](https://duckdb.org/docs/extensions/community_extensions.html#magic) | [duckdb_magic](https://github.com/carlopi/duckdb_magic) | 🟢 Ongoing | 3 days ago | 7 | C++ | Auto-detect file types via `libmagic` (`file` utility) | ⭐ |
| 41 | [prql](https://duckdb.org/docs/extensions/community_extensions.html#prql) | [duckdb-prql](https://github.com/ywelsch/duckdb-prql) | 🟢 Ongoing | 3 days ago | 297 | C++ | PRQL as a DuckDB extension | ⭐ |
| 42 | [psql](https://duckdb.org/docs/extensions/community_extensions.html#psql) | [duckdb-psql](https://github.com/ywelsch/duckdb-psql) | 🟢 Ongoing | 3 days ago | 92 | C++ | A piped SQL for DuckDB | ⭐ |
| 43 | [bigquery](https://duckdb.org/docs/extensions/community_extensions.html#bigquery) | [duckdb-bigquery](https://github.com/hafenkran/duckdb-bigquery) | 🟢 Ongoing | 4 days ago | 131 | C++ | Integrates DuckDB with Google BigQuery, allowing direct querying and manageme... | ⭐ |
| 44 | [cwiqduck](https://duckdb.org/docs/extensions/community_extensions.html#cwiqduck) | [cwiqduck](https://github.com/cwiq-os/cwiqduck) | 🟢 Ongoing | 4 days ago | 1 | C++ | DuckDB extensions for CWIQ | ⭐ |
| 45 | [zipfs](https://duckdb.org/docs/extensions/community_extensions.html#zipfs) | [duckdb-zipfs](https://github.com/isaacbrodsky/duckdb-zipfs) | 🟢 Ongoing | 4 days ago | 41 | C++ | DuckDB extension to read files within zip archives. | ⭐ |
| 46 | [chaos](https://duckdb.org/docs/extensions/community_extensions.html#chaos) | [duckdb-chaos](https://github.com/taniabogatsch/duckdb-chaos) | 🟢 Ongoing | 6 days ago | 0 | C++ | DuckDB extension: chaos by taniabogatsch | ⭐ |
| 47 | [flock](https://duckdb.org/docs/extensions/community_extensions.html#flock) | [flock](https://github.com/dais-polymtl/flock) | 🟢 Ongoing | 6 days ago | 269 | C++ | FlockMTL: DuckDB extension for multimodal querying using language models (LMs... | ⭐ |
| 48 | [file_dialog](https://duckdb.org/docs/extensions/community_extensions.html#file_dialog) | [duckdb-ext-file-dialog](https://github.com/yutannihilation/duckdb-ext-file-dialog) | 🟢 Ongoing | 7 days ago | 14 | Rust | A DuckDB extension to choose file interactively using native file open dialogs | ⭐ |
| 49 | [gcs](https://duckdb.org/docs/extensions/community_extensions.html#gcs) | [duckdb-gcs](https://github.com/northpolesec/duckdb-gcs) | 🟢 Ongoing | 7 days ago | 0 | C++ | A GCS-native extension for DuckDB |  |
| 50 | [mooncake](https://duckdb.org/docs/extensions/community_extensions.html#mooncake) | [duckdb_mooncake](https://github.com/Mooncake-Labs/duckdb_mooncake) | 🟢 Ongoing | 7 days ago | 0 | C++ | Read Iceberg tables written by moonlink in real time | ⭐ |
| 51 | [rusty_quack](https://duckdb.org/docs/extensions/community_extensions.html#rusty_quack) | [extension-template-rs](https://github.com/duckdb/extension-template-rs) | 🟢 Ongoing | 7 days ago | 80 | Rust | (Experimental) Template for Rust-based DuckDB extensions |  |
| 52 | [st_read_multi](https://duckdb.org/docs/extensions/community_extensions.html#st_read_multi) | [duckdb-ext-st-read-multi](https://github.com/yutannihilation/duckdb-ext-st-read-multi) | 🟢 Ongoing | 7 days ago | 3 | Rust | A DuckDB extension to import multiple geospatial files with `ST_Read_Multi()` | ⭐ |
| 53 | [nanoarrow](https://duckdb.org/docs/extensions/community_extensions.html#nanoarrow) | [duckdb-nanoarrow](https://github.com/paleolimbot/duckdb-nanoarrow) | 🟢 Ongoing | 8 days ago | 46 | C++ | DuckDB extension: nanoarrow by paleolimbot | ⭐ |
| 54 | [lua](https://duckdb.org/docs/extensions/community_extensions.html#lua) | [duckdb-lua](https://github.com/isaacbrodsky/duckdb-lua) | 🟢 Ongoing | 9 days ago | 5 | C++ | DuckDB extension to evaluate Lua expressions. | ⭐ |
| 55 | [quack](https://duckdb.org/docs/extensions/community_extensions.html#quack) | [extension-template](https://github.com/duckdb/extension-template) | 🟢 Ongoing | 9 days ago | 222 | Python | Template for DuckDB extensions to help you develop, test and deploy a custom... | ⭐ |
| 56 | [yaml](https://duckdb.org/docs/extensions/community_extensions.html#yaml) | [duckdb_yaml](https://github.com/teaguesterling/duckdb_yaml) | 🟢 Ongoing | 14 days ago | 9 | C++ |  A DuckDB to read and work with YAML files in a similar way to JSON files (al... |  |
| 57 | [eeagrid](https://duckdb.org/docs/extensions/community_extensions.html#eeagrid) | [duckdb-eeagrid](https://github.com/ahuarte47/duckdb-eeagrid) | 🟢 Ongoing | 15 days ago | 0 | C++ | Functions for transforming XY coordinates to and from the EEA Reference Grid... | ⭐ |
| 58 | [gsheets](https://duckdb.org/docs/extensions/community_extensions.html#gsheets) | [duckdb_gsheets](https://github.com/evidence-dev/duckdb_gsheets) | 🟢 Ongoing | 16 days ago | 298 | C++ | DuckDB extension to read and write Google Sheets using SQL | ⭐ |
| 59 | [faiss](https://duckdb.org/docs/extensions/community_extensions.html#faiss) | [duckdb-faiss-ext](https://github.com/duckdb-faiss-ext/duckdb-faiss-ext) | 🟢 Ongoing | 17 days ago | 25 | Go | DuckDB wrapper for FAISS - Experimental |  |
| 60 | [geography](https://duckdb.org/docs/extensions/community_extensions.html#geography) | [duckdb-geography](https://github.com/paleolimbot/duckdb-geography) | 🟢 Ongoing | 37 days ago | 32 | C++ | Geospatial data extension by paleolimbot |  |
| 61 | [geotiff](https://duckdb.org/docs/extensions/community_extensions.html#geotiff) | [duckdb-geotiff](https://github.com/babaknaimi/duckdb-geotiff) | 🟢 Ongoing | 37 days ago | 2 | C++ | Duckdb extension to read GeoTiffs directly with duckdb database |  |
| 62 | [highs](https://duckdb.org/docs/extensions/community_extensions.html#highs) | [HiGHS-duckdb](https://github.com/fhk/HiGHS-duckdb) | 🟢 Ongoing | 40 days ago | 0 | C++ | Run the solver in the database! |  |
| 63 | [rusty_sheet](https://duckdb.org/docs/extensions/community_extensions.html#rusty_sheet) | [rusty-sheet](https://github.com/redraiment/rusty-sheet) | 🟢 Ongoing | 42 days ago | 17 | Rust | An Excel/OpenDocument Spreadsheets file reader for DuckDB |  |
| 64 | [webbed](https://duckdb.org/docs/extensions/community_extensions.html#webbed) | [duckdb_webbed](https://github.com/teaguesterling/duckdb_webbed) | 🟢 Ongoing | 44 days ago | 14 | C++ | Web/HTTP functionality extension by teaguesterling |  |
| 65 | [read_stat](https://duckdb.org/docs/extensions/community_extensions.html#read_stat) | [duckdb-read-stat](https://github.com/mettekou/duckdb-read-stat) | 🟢 Ongoing | 45 days ago | 22 | C | Read data sets from SAS, Stata, and SPSS from DuckDB with ReadStat |  |
| 66 | [hdf5](https://duckdb.org/docs/extensions/community_extensions.html#hdf5) | [duckdb-hdf5](https://github.com/Berrysoft/duckdb-hdf5) | 🟢 Ongoing | 49 days ago | 9 | Rust | HDF5 plugin for duckdb |  |
| 67 | [duckdb_mcp](https://duckdb.org/docs/extensions/community_extensions.html#duckdb_mcp) | [duckdb_mcp](https://github.com/teaguesterling/duckdb_mcp) | 🟢 Ongoing | 61 days ago | 6 | C++ | A simple MCP server extension for DuckDB |  |
| 68 | [duckpgq](https://duckdb.org/docs/extensions/community_extensions.html#duckpgq) | [duckpgq-extension](https://github.com/cwida/duckpgq-extension) | 🟢 Ongoing | 65 days ago | 264 | C++ | DuckDB extension that adds support for SQL/PGQ and graph algorithms |  |
| 69 | [duck_tails](https://duckdb.org/docs/extensions/community_extensions.html#duck_tails) | [duck_tails](https://github.com/teaguesterling/duck_tails) | 🟢 Ongoing | 68 days ago | 2 | C++ | A DuckDB extension for exploring and reading git history. |  |
| 70 | [capi_quack](https://duckdb.org/docs/extensions/community_extensions.html#capi_quack) | [extension-template-c](https://github.com/duckdb/extension-template-c) | 🟢 Ongoing | 70 days ago | 17 | C | (Experimental) C/C++ template for DuckDB extensions based on the C API | ⭐ |
| 71 | [markdown](https://duckdb.org/docs/extensions/community_extensions.html#markdown) | [duckdb_markdown](https://github.com/teaguesterling/duckdb_markdown) | 🟢 Ongoing | 77 days ago | 5 | C++ | Heirarchical markdown parsing for DuckDB |  |
| 72 | [jwt](https://duckdb.org/docs/extensions/community_extensions.html#jwt) | [duckdb_jwt](https://github.com/GalvinGao/duckdb_jwt) | 🟢 Ongoing | 79 days ago | 0 | C++ | DuckDB extension: jwt by GalvinGao |  |
| 73 | [substrait](https://duckdb.org/docs/extensions/community_extensions.html#substrait) | [duckdb-substrait-extension](https://github.com/substrait-io/duckdb-substrait-extension) | 🟢 Ongoing | 89 days ago | 48 | C++ | DuckDB extension: substrait by substrait-io |  |
| 74 | [quackformers](https://duckdb.org/docs/extensions/community_extensions.html#quackformers) | [quackformers](https://github.com/martin-conur/quackformers) | 🟢 Ongoing | 117 days ago | 6 | Rust | DuckDB NLP extension. |  |
| 75 | [arrow](https://duckdb.org/docs/extensions/community_extensions.html#arrow) | [duckdb-extension-alias](https://github.com/duckdb/duckdb-extension-alias) | 🟢 Ongoing | 139 days ago | 4 | C | DuckDB extension: arrow |  |
| 76 | [ofquack](https://duckdb.org/docs/extensions/community_extensions.html#ofquack) | [ofquack](https://github.com/krokozyab/ofquack) | 🟢 Ongoing | 156 days ago | 5 | C++ | Oracle Fusion DuckDB extension  |  |
| 77 | [scrooge](https://duckdb.org/docs/extensions/community_extensions.html#scrooge) | [Scrooge-McDuck](https://github.com/pdet/Scrooge-McDuck) | 🟢 Ongoing | 164 days ago | 148 | C++ | DuckDB extension: scrooge by pdet |  |
| 78 | [blockduck](https://duckdb.org/docs/extensions/community_extensions.html#blockduck) | [BlockDuck](https://github.com/luohaha/BlockDuck) | 🟢 Ongoing | 183 days ago | 8 | C++ | Live SQL Queries on Blockchain |  |
| 79 | [hostfs](https://duckdb.org/docs/extensions/community_extensions.html#hostfs) | [hostFS](https://github.com/gropaul/hostFS) | 🟢 Ongoing | 199 days ago | 23 | C++ | DuckDB extension: hostfs by gropaul |  |
| 80 | [sheetreader](https://duckdb.org/docs/extensions/community_extensions.html#sheetreader) | [sheetreader-duckdb](https://github.com/polydbms/sheetreader-duckdb) | 🟢 Ongoing | 345 days ago | 55 | Jupyter Notebook | DuckDB extension: sheetreader by polydbms |  |
| 81 | [pivot_table](https://duckdb.org/docs/extensions/community_extensions.html#pivot_table) | [pivot_table](https://github.com/Alex-Monahan/pivot_table) | 🟢 Ongoing | over a year ago | 15 | C++ | Full spreadsheet-style pivot table through SQL macros. Just specify values, r... |  |
| 82 | [tarfs](https://duckdb.org/docs/extensions/community_extensions.html#tarfs) | [duckdb_tarfs](https://github.com/Maxxen/duckdb_tarfs) | 🟢 Ongoing | over a year ago | 10 | C++ | DuckDB extension: tarfs by Maxxen |  |
| 83 | [ulid](https://duckdb.org/docs/extensions/community_extensions.html#ulid) | [duckdb_ulid](https://github.com/Maxxen/duckdb_ulid) | 🟢 Ongoing | over a year ago | 24 | C++ | DuckDB extension: ulid by Maxxen |  |

**Total:** 83 extensions  
**Featured:** 41 extensions (marked with ⭐)
---

## Appendix: DuckDB Release Information

### Current Release Context

DuckDB follows **semantic versioning** with regular releases. For complete and up-to-date release information, see the official [**DuckDB Release Calendar**](https://duckdb.org/release_calendar.html).

### Release History

| Version | Release Date | Codename | Named After | LTS | Blog Post |
|---------|--------------|----------|-------------|-----|-----------|
| **v1.5.0** 📅 | 2026-02-04 | *Planned* | – | ✅ | *Upcoming release* |
| **v1.4.1** 📅 | 2025-10-06 | – | – | – | *Upcoming release* |
| **v1.4.0** | 2025-09-16 | Andium | *Anas andium* (Andean teal) | ✅ | [Announcing DuckDB 1.4.0](https://duckdb.org/2025/09/16/announcing-duckdb-140) |
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
## URL Validation Results

This section shows the results of validating URLs associated with extensions, including both simple HTTP status checks and enhanced content validation for documentation URLs.

### Validation Summary


| **Status** | **Count** | **Description** |
|------------|-----------|-----------------|
| ✅ **OK** | 0 | URLs are accessible and content is valid |
| ⚠️ **Likely Wrong** | 0 | URLs are accessible but content may not match extension |
| ❌ **Broken** | 0 | URLs are not accessible or return errors |
| **Total Validated** | 230 | Total URLs checked |


### Validation Details

**autocomplete_repository**
- URL: `https://github.com/duckdb/duckdb/tree/main/extension/autocomplete`
- Status: ❌ Broken- HTTP Status: 200
**avro_repository**
- URL: `https://github.com/duckdb/duckdb-avro`
- Status: ❌ Broken- HTTP Status: 200
**avro_external_repo**
- URL: `https://github.com/duckdb/duckdb-avro`
- Status: ❌ Broken- HTTP Status: 200
**aws_repository**
- URL: `https://github.com/duckdb/duckdb-aws`
- Status: ❌ Broken- HTTP Status: 200
**aws_external_repo**
- URL: `https://github.com/duckdb/duckdb-aws`
- Status: ❌ Broken- HTTP Status: 200
**azure_repository**
- URL: `https://github.com/duckdb/duckdb-azure`
- Status: ❌ Broken- HTTP Status: 200
**azure_external_repo**
- URL: `https://github.com/duckdb/duckdb-azure`
- Status: ❌ Broken- HTTP Status: 200
**delta_repository**
- URL: `https://github.com/duckdb/duckdb-delta`
- Status: ❌ Broken- HTTP Status: 200
**delta_external_repo**
- URL: `https://github.com/duckdb/duckdb-delta`
- Status: ❌ Broken- HTTP Status: 200
**ducklake_repository**
- URL: `https://github.com/duckdb/ducklake`
- Status: ❌ Broken- HTTP Status: 200
**encodings_repository**
- URL: `https://github.com/duckdb/duckdb-encodings`
- Status: ❌ Broken- HTTP Status: 200
**encodings_external_repo**
- URL: `https://github.com/duckdb/duckdb-encodings`
- Status: ❌ Broken- HTTP Status: 200
**excel_repository**
- URL: `https://github.com/duckdb/duckdb-excel`
- Status: ❌ Broken- HTTP Status: 200
**excel_external_repo**
- URL: `https://github.com/duckdb/duckdb-excel`
- Status: ❌ Broken- HTTP Status: 200
**fts_repository**
- URL: `https://github.com/duckdb/duckdb-fts`
- Status: ❌ Broken- HTTP Status: 200
**fts_external_repo**
- URL: `https://github.com/duckdb/duckdb-fts`
- Status: ❌ Broken- HTTP Status: 200
**httpfs_repository**
- URL: `https://github.com/duckdb/duckdb-httpfs`
- Status: ❌ Broken- HTTP Status: 200
**httpfs_external_repo**
- URL: `https://github.com/duckdb/duckdb-httpfs`
- Status: ❌ Broken- HTTP Status: 200
**iceberg_repository**
- URL: `https://github.com/duckdb/duckdb-iceberg`
- Status: ❌ Broken- HTTP Status: 200
**iceberg_external_repo**
- URL: `https://github.com/duckdb/duckdb-iceberg`
- Status: ❌ Broken- HTTP Status: 200
**icu_repository**
- URL: `https://github.com/duckdb/duckdb/tree/main/extension/icu`
- Status: ❌ Broken- HTTP Status: 200
**inet_repository**
- URL: `https://github.com/duckdb/duckdb-inet`
- Status: ❌ Broken- HTTP Status: 200
**inet_external_repo**
- URL: `https://github.com/duckdb/duckdb-inet`
- Status: ❌ Broken- HTTP Status: 200
**jemalloc_repository**
- URL: `https://github.com/duckdb/duckdb/tree/main/extension/jemalloc`
- Status: ❌ Broken- HTTP Status: 200
**json_repository**
- URL: `https://github.com/duckdb/duckdb/tree/main/extension/json`
- Status: ❌ Broken- HTTP Status: 200
**mysql_repository**
- URL: `https://github.com/duckdb/duckdb-mysql`
- Status: ❌ Broken- HTTP Status: 200
**mysql_external_repo**
- URL: `https://github.com/duckdb/duckdb-mysql`
- Status: ❌ Broken- HTTP Status: 200
**parquet_repository**
- URL: `https://github.com/duckdb/duckdb/tree/main/extension/parquet`
- Status: ❌ Broken- HTTP Status: 200
**postgres_repository**
- URL: `https://github.com/duckdb/duckdb-postgres`
- Status: ❌ Broken- HTTP Status: 200
**postgres_external_repo**
- URL: `https://github.com/duckdb/duckdb-postgres`
- Status: ❌ Broken- HTTP Status: 200
**spatial_repository**
- URL: `https://github.com/duckdb/duckdb-spatial`
- Status: ❌ Broken- HTTP Status: 200
**spatial_external_repo**
- URL: `https://github.com/duckdb/duckdb-spatial`
- Status: ❌ Broken- HTTP Status: 200
**sqlite_repository**
- URL: `https://github.com/duckdb/duckdb-sqlite`
- Status: ❌ Broken- HTTP Status: 200
**sqlite_external_repo**
- URL: `https://github.com/duckdb/duckdb-sqlite`
- Status: ❌ Broken- HTTP Status: 200
**tpcds_repository**
- URL: `https://github.com/duckdb/duckdb/tree/main/extension/tpcds`
- Status: ❌ Broken- HTTP Status: 200
**tpch_repository**
- URL: `https://github.com/duckdb/duckdb/tree/main/extension/tpch`
- Status: ❌ Broken- HTTP Status: 200
**ui_repository**
- URL: `https://github.com/duckdb/duckdb-ui`
- Status: ❌ Broken- HTTP Status: 200
**ui_external_repo**
- URL: `https://github.com/duckdb/duckdb-ui`
- Status: ❌ Broken- HTTP Status: 200
**vss_repository**
- URL: `https://github.com/duckdb/duckdb-vss`
- Status: ❌ Broken- HTTP Status: 200
**vss_external_repo**
- URL: `https://github.com/duckdb/duckdb-vss`
- Status: ❌ Broken- HTTP Status: 200
**datasketches_repository**
- URL: `https://github.com/Query-farm/datasketches`
- Status: ❌ Broken- HTTP Status: 200
**fuzzycomplete_repository**
- URL: `https://github.com/Query-farm/fuzzycomplete`
- Status: ❌ Broken- HTTP Status: 200
**h3_repository**
- URL: `https://github.com/isaacbrodsky/h3-duckdb`
- Status: ❌ Broken- HTTP Status: 200
**hashfuncs_repository**
- URL: `https://github.com/Query-farm/hashfuncs`
- Status: ❌ Broken- HTTP Status: 200
**lindel_repository**
- URL: `https://github.com/Query-farm/lindel`
- Status: ❌ Broken- HTTP Status: 200
**marisa_repository**
- URL: `https://github.com/Query-farm/marisa`
- Status: ❌ Broken- HTTP Status: 200
**pbix_repository**
- URL: `https://github.com/Hugoberry/duckdb-pbix-extension`
- Status: ❌ Broken- HTTP Status: 200
**stochastic_repository**
- URL: `https://github.com/Query-farm/stochastic`
- Status: ❌ Broken- HTTP Status: 200
**textplot_repository**
- URL: `https://github.com/Query-farm/textplot`
- Status: ❌ Broken- HTTP Status: 200
**tributary_repository**
- URL: `https://github.com/Query-farm/tributary`
- Status: ❌ Broken- HTTP Status: 200
**vortex_repository**
- URL: `https://github.com/vortex-data/duckdb-vortex`
- Status: ❌ Broken- HTTP Status: 200
**httpserver_repository**
- URL: `https://github.com/Query-farm/httpserver`
- Status: ❌ Broken- HTTP Status: 200
**msolap_repository**
- URL: `https://github.com/Hugoberry/duckdb-msolap-extension`
- Status: ❌ Broken- HTTP Status: 200
**nanodbc_repository**
- URL: `https://github.com/Hugoberry/duckdb-nanodbc-extension`
- Status: ❌ Broken- HTTP Status: 200
**netquack_repository**
- URL: `https://github.com/hatamiarash7/duckdb-netquack`
- Status: ❌ Broken- HTTP Status: 200
**parser_tools_repository**
- URL: `https://github.com/zfarrell/duckdb_extension_parser_tools`
- Status: ❌ Broken- HTTP Status: 200
**radio_repository**
- URL: `https://github.com/Query-farm/radio`
- Status: ❌ Broken- HTTP Status: 200
**splink_udfs_repository**
- URL: `https://github.com/moj-analytical-services/splink_udfs`
- Status: ❌ Broken- HTTP Status: 200
**airport_repository**
- URL: `https://github.com/Query-farm/airport`
- Status: ❌ Broken- HTTP Status: 200
**bitfilters_repository**
- URL: `https://github.com/Query-farm/bitfilters`
- Status: ❌ Broken- HTTP Status: 200
**cache_httpfs_repository**
- URL: `https://github.com/dentiny/duck-read-cache-fs`
- Status: ❌ Broken- HTTP Status: 200
**chsql_repository**
- URL: `https://github.com/Query-farm/clickhouse-sql`
- Status: ❌ Broken- HTTP Status: 200
**chsql_native_repository**
- URL: `https://github.com/Query-farm/clickhouse-native`
- Status: ❌ Broken- HTTP Status: 200
**cronjob_repository**
- URL: `https://github.com/Query-farm/cronjob`
- Status: ❌ Broken- HTTP Status: 200
**crypto_repository**
- URL: `https://github.com/Query-farm/crypto`
- Status: ❌ Broken- HTTP Status: 200
**evalexpr_rhai_repository**
- URL: `https://github.com/Query-farm/evalexpr_rhai`
- Status: ❌ Broken- HTTP Status: 200
**http_client_repository**
- URL: `https://github.com/Query-farm/httpclient`
- Status: ❌ Broken- HTTP Status: 200
**observefs_repository**
- URL: `https://github.com/dentiny/duckdb-filesystem-observability`
- Status: ❌ Broken- HTTP Status: 200
**open_prompt_repository**
- URL: `https://github.com/Query-farm/openprompt`
- Status: ❌ Broken- HTTP Status: 200
**pcap_reader_repository**
- URL: `https://github.com/Query-farm/pcap`
- Status: ❌ Broken- HTTP Status: 200
**pyroscope_repository**
- URL: `https://github.com/Query-farm/pyroscope`
- Status: ❌ Broken- HTTP Status: 200
**quickjs_repository**
- URL: `https://github.com/Query-farm/quickjs`
- Status: ❌ Broken- HTTP Status: 200
**rapidfuzz_repository**
- URL: `https://github.com/Query-farm/rapidfuzz`
- Status: ❌ Broken- HTTP Status: 200
**redis_repository**
- URL: `https://github.com/Query-farm/redis`
- Status: ❌ Broken- HTTP Status: 200
**shellfs_repository**
- URL: `https://github.com/Query-farm/shellfs`
- Status: ❌ Broken- HTTP Status: 200
**snowflake_repository**
- URL: `https://github.com/iqea-ai/duckdb-snowflake`
- Status: ❌ Broken- HTTP Status: 200
**tsid_repository**
- URL: `https://github.com/Query-farm/tsid`
- Status: ❌ Broken- HTTP Status: 200
**webmacro_repository**
- URL: `https://github.com/Query-farm/webmacro`
- Status: ❌ Broken- HTTP Status: 200
**wireduck_repository**
- URL: `https://github.com/hyehudai/wireduck`
- Status: ❌ Broken- HTTP Status: 200
**magic_repository**
- URL: `https://github.com/carlopi/duckdb_magic`
- Status: ❌ Broken- HTTP Status: 200
**prql_repository**
- URL: `https://github.com/ywelsch/duckdb-prql`
- Status: ❌ Broken- HTTP Status: 200
**psql_repository**
- URL: `https://github.com/ywelsch/duckdb-psql`
- Status: ❌ Broken- HTTP Status: 200
**bigquery_repository**
- URL: `https://github.com/hafenkran/duckdb-bigquery`
- Status: ❌ Broken- HTTP Status: 200
**cwiqduck_repository**
- URL: `https://github.com/cwiq-os/cwiqduck`
- Status: ❌ Broken- HTTP Status: 200
**zipfs_repository**
- URL: `https://github.com/isaacbrodsky/duckdb-zipfs`
- Status: ❌ Broken- HTTP Status: 200
**chaos_repository**
- URL: `https://github.com/taniabogatsch/duckdb-chaos`
- Status: ❌ Broken- HTTP Status: 200
**flock_repository**
- URL: `https://github.com/dais-polymtl/flock`
- Status: ❌ Broken- HTTP Status: 200
**file_dialog_repository**
- URL: `https://github.com/yutannihilation/duckdb-ext-file-dialog`
- Status: ❌ Broken- HTTP Status: 200
**gcs_repository**
- URL: `https://github.com/northpolesec/duckdb-gcs`
- Status: ❌ Broken- HTTP Status: 200
**mooncake_repository**
- URL: `https://github.com/Mooncake-Labs/duckdb_mooncake`
- Status: ❌ Broken- HTTP Status: 200
**rusty_quack_repository**
- URL: `https://github.com/duckdb/extension-template-rs`
- Status: ❌ Broken- HTTP Status: 200
**st_read_multi_repository**
- URL: `https://github.com/yutannihilation/duckdb-ext-st-read-multi`
- Status: ❌ Broken- HTTP Status: 200
**nanoarrow_repository**
- URL: `https://github.com/paleolimbot/duckdb-nanoarrow`
- Status: ❌ Broken- HTTP Status: 200
**lua_repository**
- URL: `https://github.com/isaacbrodsky/duckdb-lua`
- Status: ❌ Broken- HTTP Status: 200
**quack_repository**
- URL: `https://github.com/duckdb/extension-template`
- Status: ❌ Broken- HTTP Status: 200
**yaml_repository**
- URL: `https://github.com/teaguesterling/duckdb_yaml`
- Status: ❌ Broken- HTTP Status: 200
**eeagrid_repository**
- URL: `https://github.com/ahuarte47/duckdb-eeagrid`
- Status: ❌ Broken- HTTP Status: 200
**gsheets_repository**
- URL: `https://github.com/evidence-dev/duckdb_gsheets`
- Status: ❌ Broken- HTTP Status: 200
**faiss_repository**
- URL: `https://github.com/duckdb-faiss-ext/duckdb-faiss-ext`
- Status: ❌ Broken- HTTP Status: 200
**geography_repository**
- URL: `https://github.com/paleolimbot/duckdb-geography`
- Status: ❌ Broken- HTTP Status: 200
**geotiff_repository**
- URL: `https://github.com/babaknaimi/duckdb-geotiff`
- Status: ❌ Broken- HTTP Status: 200
**highs_repository**
- URL: `https://github.com/fhk/HiGHS-duckdb`
- Status: ❌ Broken- HTTP Status: 200
**rusty_sheet_repository**
- URL: `https://github.com/redraiment/rusty-sheet`
- Status: ❌ Broken- HTTP Status: 200
**webbed_repository**
- URL: `https://github.com/teaguesterling/duckdb_webbed`
- Status: ❌ Broken- HTTP Status: 200
**read_stat_repository**
- URL: `https://github.com/mettekou/duckdb-read-stat`
- Status: ❌ Broken- HTTP Status: 200
**hdf5_repository**
- URL: `https://github.com/Berrysoft/duckdb-hdf5`
- Status: ❌ Broken- HTTP Status: 200
**duckdb_mcp_repository**
- URL: `https://github.com/teaguesterling/duckdb_mcp`
- Status: ❌ Broken- HTTP Status: 200
**duckpgq_repository**
- URL: `https://github.com/cwida/duckpgq-extension`
- Status: ❌ Broken- HTTP Status: 200
**duck_tails_repository**
- URL: `https://github.com/teaguesterling/duck_tails`
- Status: ❌ Broken- HTTP Status: 200
**capi_quack_repository**
- URL: `https://github.com/duckdb/extension-template-c`
- Status: ❌ Broken- HTTP Status: 200
**markdown_repository**
- URL: `https://github.com/teaguesterling/duckdb_markdown`
- Status: ❌ Broken- HTTP Status: 200
**jwt_repository**
- URL: `https://github.com/GalvinGao/duckdb_jwt`
- Status: ❌ Broken- HTTP Status: 200
**substrait_repository**
- URL: `https://github.com/substrait-io/duckdb-substrait-extension`
- Status: ❌ Broken- HTTP Status: 200
**quackformers_repository**
- URL: `https://github.com/martin-conur/quackformers`
- Status: ❌ Broken- HTTP Status: 200
**arrow_repository**
- URL: `https://github.com/duckdb/duckdb-extension-alias`
- Status: ❌ Broken- HTTP Status: 200
**ofquack_repository**
- URL: `https://github.com/krokozyab/ofquack`
- Status: ❌ Broken- HTTP Status: 200
**scrooge_repository**
- URL: `https://github.com/pdet/Scrooge-McDuck`
- Status: ❌ Broken- HTTP Status: 200
**blockduck_repository**
- URL: `https://github.com/luohaha/BlockDuck`
- Status: ❌ Broken- HTTP Status: 200
**hostfs_repository**
- URL: `https://github.com/gropaul/hostFS`
- Status: ❌ Broken- HTTP Status: 200
**sheetreader_repository**
- URL: `https://github.com/polydbms/sheetreader-duckdb`
- Status: ❌ Broken- HTTP Status: 200
**pivot_table_repository**
- URL: `https://github.com/Alex-Monahan/pivot_table`
- Status: ❌ Broken- HTTP Status: 200
**tarfs_repository**
- URL: `https://github.com/Maxxen/duckdb_tarfs`
- Status: ❌ Broken- HTTP Status: 200
**ulid_repository**
- URL: `https://github.com/Maxxen/duckdb_ulid`
- Status: ❌ Broken- HTTP Status: 200
**autocomplete_documentation**
- URL: `https://duckdb.org/docs/stable/core_extensions/autocomplete.html`
- Status: ❌ Broken- HTTP Status: 200- Extension name found on page
**avro_documentation**
- URL: `https://duckdb.org/docs/stable/core_extensions/avro.html`
- Status: ❌ Broken- HTTP Status: 200- Extension name found on page
**aws_documentation**
- URL: `https://duckdb.org/docs/stable/core_extensions/aws.html`
- Status: ❌ Broken- HTTP Status: 200- Extension name found on page
**azure_documentation**
- URL: `https://duckdb.org/docs/stable/core_extensions/azure.html`
- Status: ❌ Broken- HTTP Status: 200- Extension name found on page
**delta_documentation**
- URL: `https://duckdb.org/docs/stable/core_extensions/delta.html`
- Status: ❌ Broken- HTTP Status: 200- Extension name found on page
**ducklake_documentation**
- URL: `https://duckdb.org/docs/stable/core_extensions/ducklake.html`
- Status: ❌ Broken- HTTP Status: 200- Extension name found on page
**encodings_documentation**
- URL: `https://duckdb.org/docs/stable/core_extensions/encodings.html`
- Status: ❌ Broken- HTTP Status: 200- Extension name found on page
**excel_documentation**
- URL: `https://duckdb.org/docs/stable/core_extensions/excel.html`
- Status: ❌ Broken- HTTP Status: 200- Extension name found on page
**fts_documentation**
- URL: `https://duckdb.org/docs/stable/core_extensions/full_text_search.html`
- Status: ❌ Broken- HTTP Status: 200- Extension name found on page
**httpfs_documentation**
- URL: `https://duckdb.org/docs/stable/core_extensions/httpfs/overview.html`
- Status: ❌ Broken- HTTP Status: 200- Extension name found on page
**iceberg_documentation**
- URL: `https://duckdb.org/docs/stable/core_extensions/iceberg/overview.html`
- Status: ❌ Broken- HTTP Status: 200- Extension name found on page
**icu_documentation**
- URL: `https://duckdb.org/docs/stable/core_extensions/icu.html`
- Status: ❌ Broken- HTTP Status: 200- Extension name found on page
**inet_documentation**
- URL: `https://duckdb.org/docs/stable/core_extensions/inet.html`
- Status: ❌ Broken- HTTP Status: 200- Extension name found on page
**jemalloc_documentation**
- URL: `https://duckdb.org/docs/stable/core_extensions/jemalloc.html`
- Status: ❌ Broken- HTTP Status: 200- Extension name found on page
**json_documentation**
- URL: `https://duckdb.org/docs/stable/data/json/overview.html`
- Status: ❌ Broken- HTTP Status: 200- Extension name found on page
**mysql_documentation**
- URL: `https://duckdb.org/docs/stable/core_extensions/mysql.html`
- Status: ❌ Broken- HTTP Status: 200- Extension name found on page
**parquet_documentation**
- URL: `https://duckdb.org/docs/stable/data/parquet/overview.html`
- Status: ❌ Broken- HTTP Status: 200- Extension name found on page
**postgres_documentation**
- URL: `https://duckdb.org/docs/stable/core_extensions/postgres.html`
- Status: ❌ Broken- HTTP Status: 200- Extension name found on page
**spatial_documentation**
- URL: `https://duckdb.org/docs/stable/core_extensions/spatial/overview.html`
- Status: ❌ Broken- HTTP Status: 200- Extension name found on page
**sqlite_documentation**
- URL: `https://duckdb.org/docs/stable/core_extensions/sqlite.html`
- Status: ❌ Broken- HTTP Status: 200- Extension name found on page
**tpcds_documentation**
- URL: `https://duckdb.org/docs/stable/core_extensions/tpcds.html`
- Status: ❌ Broken- HTTP Status: 200- Extension name found on page
**tpch_documentation**
- URL: `https://duckdb.org/docs/stable/core_extensions/tpch.html`
- Status: ❌ Broken- HTTP Status: 200- Extension name found on page
**ui_documentation**
- URL: `https://duckdb.org/docs/stable/core_extensions/ui.html`
- Status: ❌ Broken- HTTP Status: 200- Extension name found on page
**vss_documentation**
- URL: `https://duckdb.org/docs/stable/core_extensions/vss.html`
- Status: ❌ Broken- HTTP Status: 200- Extension name found on page
**datasketches_documentation**
- URL: `https://duckdb.org/docs/extensions/community_extensions.html#datasketches`
- Status: ❌ Broken- HTTP Status: 200- Extension name NOT found on page
**fuzzycomplete_documentation**
- URL: `https://duckdb.org/docs/extensions/community_extensions.html#fuzzycomplete`
- Status: ❌ Broken- HTTP Status: 200- Extension name NOT found on page
**h3_documentation**
- URL: `https://duckdb.org/docs/extensions/community_extensions.html#h3`
- Status: ❌ Broken- HTTP Status: 200- Extension name NOT found on page
**hashfuncs_documentation**
- URL: `https://duckdb.org/docs/extensions/community_extensions.html#hashfuncs`
- Status: ❌ Broken- HTTP Status: 200- Extension name NOT found on page
**lindel_documentation**
- URL: `https://duckdb.org/docs/extensions/community_extensions.html#lindel`
- Status: ❌ Broken- HTTP Status: 200- Extension name NOT found on page
**marisa_documentation**
- URL: `https://duckdb.org/docs/extensions/community_extensions.html#marisa`
- Status: ❌ Broken- HTTP Status: 200- Extension name NOT found on page
**pbix_documentation**
- URL: `https://duckdb.org/docs/extensions/community_extensions.html#pbix`
- Status: ❌ Broken- HTTP Status: 200- Extension name NOT found on page
**stochastic_documentation**
- URL: `https://duckdb.org/docs/extensions/community_extensions.html#stochastic`
- Status: ❌ Broken- HTTP Status: 200- Extension name NOT found on page
**textplot_documentation**
- URL: `https://duckdb.org/docs/extensions/community_extensions.html#textplot`
- Status: ❌ Broken- HTTP Status: 200- Extension name NOT found on page
**tributary_documentation**
- URL: `https://duckdb.org/docs/extensions/community_extensions.html#tributary`
- Status: ❌ Broken- HTTP Status: 200- Extension name NOT found on page
**vortex_documentation**
- URL: `https://duckdb.org/docs/extensions/community_extensions.html#vortex`
- Status: ❌ Broken- HTTP Status: 200- Extension name NOT found on page
**httpserver_documentation**
- URL: `https://duckdb.org/docs/extensions/community_extensions.html#httpserver`
- Status: ❌ Broken- HTTP Status: 200- Extension name NOT found on page
**msolap_documentation**
- URL: `https://duckdb.org/docs/extensions/community_extensions.html#msolap`
- Status: ❌ Broken- HTTP Status: 200- Extension name NOT found on page
**nanodbc_documentation**
- URL: `https://duckdb.org/docs/extensions/community_extensions.html#nanodbc`
- Status: ❌ Broken- HTTP Status: 200- Extension name NOT found on page
**netquack_documentation**
- URL: `https://duckdb.org/docs/extensions/community_extensions.html#netquack`
- Status: ❌ Broken- HTTP Status: 200- Extension name NOT found on page
**parser_tools_documentation**
- URL: `https://duckdb.org/docs/extensions/community_extensions.html#parser_tools`
- Status: ❌ Broken- HTTP Status: 200- Extension name NOT found on page
**radio_documentation**
- URL: `https://duckdb.org/docs/extensions/community_extensions.html#radio`
- Status: ❌ Broken- HTTP Status: 200- Extension name NOT found on page
**splink_udfs_documentation**
- URL: `https://duckdb.org/docs/extensions/community_extensions.html#splink_udfs`
- Status: ❌ Broken- HTTP Status: 200- Extension name NOT found on page
**airport_documentation**
- URL: `https://duckdb.org/docs/extensions/community_extensions.html#airport`
- Status: ❌ Broken- HTTP Status: 200- Extension name NOT found on page
**bitfilters_documentation**
- URL: `https://duckdb.org/docs/extensions/community_extensions.html#bitfilters`
- Status: ❌ Broken- HTTP Status: 200- Extension name NOT found on page
**cache_httpfs_documentation**
- URL: `https://duckdb.org/docs/extensions/community_extensions.html#cache_httpfs`
- Status: ❌ Broken- HTTP Status: 200- Extension name NOT found on page
**chsql_documentation**
- URL: `https://duckdb.org/docs/extensions/community_extensions.html#chsql`
- Status: ❌ Broken- HTTP Status: 200- Extension name NOT found on page
**chsql_native_documentation**
- URL: `https://duckdb.org/docs/extensions/community_extensions.html#chsql_native`
- Status: ❌ Broken- HTTP Status: 200- Extension name NOT found on page
**cronjob_documentation**
- URL: `https://duckdb.org/docs/extensions/community_extensions.html#cronjob`
- Status: ❌ Broken- HTTP Status: 200- Extension name NOT found on page
**crypto_documentation**
- URL: `https://duckdb.org/docs/extensions/community_extensions.html#crypto`
- Status: ❌ Broken- HTTP Status: 200- Extension name NOT found on page
**evalexpr_rhai_documentation**
- URL: `https://duckdb.org/docs/extensions/community_extensions.html#evalexpr_rhai`
- Status: ❌ Broken- HTTP Status: 200- Extension name NOT found on page
**http_client_documentation**
- URL: `https://duckdb.org/docs/extensions/community_extensions.html#http_client`
- Status: ❌ Broken- HTTP Status: 200- Extension name NOT found on page
**observefs_documentation**
- URL: `https://duckdb.org/docs/extensions/community_extensions.html#observefs`
- Status: ❌ Broken- HTTP Status: 200- Extension name NOT found on page
**open_prompt_documentation**
- URL: `https://duckdb.org/docs/extensions/community_extensions.html#open_prompt`
- Status: ❌ Broken- HTTP Status: 200- Extension name NOT found on page
**pcap_reader_documentation**
- URL: `https://duckdb.org/docs/extensions/community_extensions.html#pcap_reader`
- Status: ❌ Broken- HTTP Status: 200- Extension name NOT found on page
**pyroscope_documentation**
- URL: `https://duckdb.org/docs/extensions/community_extensions.html#pyroscope`
- Status: ❌ Broken- HTTP Status: 200- Extension name NOT found on page
**quickjs_documentation**
- URL: `https://duckdb.org/docs/extensions/community_extensions.html#quickjs`
- Status: ❌ Broken- HTTP Status: 200- Extension name NOT found on page
**rapidfuzz_documentation**
- URL: `https://duckdb.org/docs/extensions/community_extensions.html#rapidfuzz`
- Status: ❌ Broken- HTTP Status: 200- Extension name NOT found on page
**redis_documentation**
- URL: `https://duckdb.org/docs/extensions/community_extensions.html#redis`
- Status: ❌ Broken- HTTP Status: 200- Extension name NOT found on page
**shellfs_documentation**
- URL: `https://duckdb.org/docs/extensions/community_extensions.html#shellfs`
- Status: ❌ Broken- HTTP Status: 200- Extension name NOT found on page
**snowflake_documentation**
- URL: `https://duckdb.org/docs/extensions/community_extensions.html#snowflake`
- Status: ❌ Broken- HTTP Status: 200- Extension name NOT found on page
**tsid_documentation**
- URL: `https://duckdb.org/docs/extensions/community_extensions.html#tsid`
- Status: ❌ Broken- HTTP Status: 200- Extension name NOT found on page
**webmacro_documentation**
- URL: `https://duckdb.org/docs/extensions/community_extensions.html#webmacro`
- Status: ❌ Broken- HTTP Status: 200- Extension name NOT found on page
**wireduck_documentation**
- URL: `https://duckdb.org/docs/extensions/community_extensions.html#wireduck`
- Status: ❌ Broken- HTTP Status: 200- Extension name NOT found on page
**magic_documentation**
- URL: `https://duckdb.org/docs/extensions/community_extensions.html#magic`
- Status: ❌ Broken- HTTP Status: 200- Extension name NOT found on page
**prql_documentation**
- URL: `https://duckdb.org/docs/extensions/community_extensions.html#prql`
- Status: ❌ Broken- HTTP Status: 200- Extension name NOT found on page
**psql_documentation**
- URL: `https://duckdb.org/docs/extensions/community_extensions.html#psql`
- Status: ❌ Broken- HTTP Status: 200- Extension name NOT found on page
**bigquery_documentation**
- URL: `https://duckdb.org/docs/extensions/community_extensions.html#bigquery`
- Status: ❌ Broken- HTTP Status: 200- Extension name NOT found on page
**cwiqduck_documentation**
- URL: `https://duckdb.org/docs/extensions/community_extensions.html#cwiqduck`
- Status: ❌ Broken- HTTP Status: 200- Extension name NOT found on page
**zipfs_documentation**
- URL: `https://duckdb.org/docs/extensions/community_extensions.html#zipfs`
- Status: ❌ Broken- HTTP Status: 200- Extension name NOT found on page
**chaos_documentation**
- URL: `https://duckdb.org/docs/extensions/community_extensions.html#chaos`
- Status: ❌ Broken- HTTP Status: 200- Extension name NOT found on page
**flock_documentation**
- URL: `https://duckdb.org/docs/extensions/community_extensions.html#flock`
- Status: ❌ Broken- HTTP Status: 200- Extension name NOT found on page
**file_dialog_documentation**
- URL: `https://duckdb.org/docs/extensions/community_extensions.html#file_dialog`
- Status: ❌ Broken- HTTP Status: 200- Extension name NOT found on page
**gcs_documentation**
- URL: `https://duckdb.org/docs/extensions/community_extensions.html#gcs`
- Status: ❌ Broken- HTTP Status: 200- Extension name NOT found on page
**mooncake_documentation**
- URL: `https://duckdb.org/docs/extensions/community_extensions.html#mooncake`
- Status: ❌ Broken- HTTP Status: 200- Extension name NOT found on page
**rusty_quack_documentation**
- URL: `https://duckdb.org/docs/extensions/community_extensions.html#rusty_quack`
- Status: ❌ Broken- HTTP Status: 200- Extension name NOT found on page
**st_read_multi_documentation**
- URL: `https://duckdb.org/docs/extensions/community_extensions.html#st_read_multi`
- Status: ❌ Broken- HTTP Status: 200- Extension name NOT found on page
**nanoarrow_documentation**
- URL: `https://duckdb.org/docs/extensions/community_extensions.html#nanoarrow`
- Status: ❌ Broken- HTTP Status: 200- Extension name NOT found on page
**lua_documentation**
- URL: `https://duckdb.org/docs/extensions/community_extensions.html#lua`
- Status: ❌ Broken- HTTP Status: 200- Extension name NOT found on page
**quack_documentation**
- URL: `https://duckdb.org/docs/extensions/community_extensions.html#quack`
- Status: ❌ Broken- HTTP Status: 200- Extension name NOT found on page
**yaml_documentation**
- URL: `https://duckdb.org/docs/extensions/community_extensions.html#yaml`
- Status: ❌ Broken- HTTP Status: 200- Extension name NOT found on page
**eeagrid_documentation**
- URL: `https://duckdb.org/docs/extensions/community_extensions.html#eeagrid`
- Status: ❌ Broken- HTTP Status: 200- Extension name NOT found on page
**gsheets_documentation**
- URL: `https://duckdb.org/docs/extensions/community_extensions.html#gsheets`
- Status: ❌ Broken- HTTP Status: 200- Extension name NOT found on page
**faiss_documentation**
- URL: `https://duckdb.org/docs/extensions/community_extensions.html#faiss`
- Status: ❌ Broken- HTTP Status: 200- Extension name NOT found on page
**geography_documentation**
- URL: `https://duckdb.org/docs/extensions/community_extensions.html#geography`
- Status: ❌ Broken- HTTP Status: 200- Extension name NOT found on page
**geotiff_documentation**
- URL: `https://duckdb.org/docs/extensions/community_extensions.html#geotiff`
- Status: ❌ Broken- HTTP Status: 200- Extension name NOT found on page
**highs_documentation**
- URL: `https://duckdb.org/docs/extensions/community_extensions.html#highs`
- Status: ❌ Broken- HTTP Status: 200- Extension name NOT found on page
**rusty_sheet_documentation**
- URL: `https://duckdb.org/docs/extensions/community_extensions.html#rusty_sheet`
- Status: ❌ Broken- HTTP Status: 200- Extension name NOT found on page
**webbed_documentation**
- URL: `https://duckdb.org/docs/extensions/community_extensions.html#webbed`
- Status: ❌ Broken- HTTP Status: 200- Extension name NOT found on page
**read_stat_documentation**
- URL: `https://duckdb.org/docs/extensions/community_extensions.html#read_stat`
- Status: ❌ Broken- HTTP Status: 200- Extension name NOT found on page
**hdf5_documentation**
- URL: `https://duckdb.org/docs/extensions/community_extensions.html#hdf5`
- Status: ❌ Broken- HTTP Status: 200- Extension name NOT found on page
**duckdb_mcp_documentation**
- URL: `https://duckdb.org/docs/extensions/community_extensions.html#duckdb_mcp`
- Status: ❌ Broken- HTTP Status: 200- Extension name NOT found on page
**duckpgq_documentation**
- URL: `https://duckdb.org/docs/extensions/community_extensions.html#duckpgq`
- Status: ❌ Broken- HTTP Status: 200- Extension name NOT found on page
**duck_tails_documentation**
- URL: `https://duckdb.org/docs/extensions/community_extensions.html#duck_tails`
- Status: ❌ Broken- HTTP Status: 200- Extension name NOT found on page
**capi_quack_documentation**
- URL: `https://duckdb.org/docs/extensions/community_extensions.html#capi_quack`
- Status: ❌ Broken- HTTP Status: 200- Extension name NOT found on page
**markdown_documentation**
- URL: `https://duckdb.org/docs/extensions/community_extensions.html#markdown`
- Status: ❌ Broken- HTTP Status: 200- Extension name NOT found on page
**jwt_documentation**
- URL: `https://duckdb.org/docs/extensions/community_extensions.html#jwt`
- Status: ❌ Broken- HTTP Status: 200- Extension name NOT found on page
**substrait_documentation**
- URL: `https://duckdb.org/docs/extensions/community_extensions.html#substrait`
- Status: ❌ Broken- HTTP Status: 200- Extension name NOT found on page
**quackformers_documentation**
- URL: `https://duckdb.org/docs/extensions/community_extensions.html#quackformers`
- Status: ❌ Broken- HTTP Status: 200- Extension name NOT found on page
**arrow_documentation**
- URL: `https://duckdb.org/docs/extensions/community_extensions.html#arrow`
- Status: ❌ Broken- HTTP Status: 200- Extension name NOT found on page
**ofquack_documentation**
- URL: `https://duckdb.org/docs/extensions/community_extensions.html#ofquack`
- Status: ❌ Broken- HTTP Status: 200- Extension name NOT found on page
**scrooge_documentation**
- URL: `https://duckdb.org/docs/extensions/community_extensions.html#scrooge`
- Status: ❌ Broken- HTTP Status: 200- Extension name NOT found on page
**blockduck_documentation**
- URL: `https://duckdb.org/docs/extensions/community_extensions.html#blockduck`
- Status: ❌ Broken- HTTP Status: 200- Extension name NOT found on page
**hostfs_documentation**
- URL: `https://duckdb.org/docs/extensions/community_extensions.html#hostfs`
- Status: ❌ Broken- HTTP Status: 200- Extension name NOT found on page
**sheetreader_documentation**
- URL: `https://duckdb.org/docs/extensions/community_extensions.html#sheetreader`
- Status: ❌ Broken- HTTP Status: 200- Extension name NOT found on page
**pivot_table_documentation**
- URL: `https://duckdb.org/docs/extensions/community_extensions.html#pivot_table`
- Status: ❌ Broken- HTTP Status: 200- Extension name NOT found on page
**tarfs_documentation**
- URL: `https://duckdb.org/docs/extensions/community_extensions.html#tarfs`
- Status: ❌ Broken- HTTP Status: 200- Extension name NOT found on page
**ulid_documentation**
- URL: `https://duckdb.org/docs/extensions/community_extensions.html#ulid`
- Status: ❌ Broken- HTTP Status: 200- Extension name NOT found on page


