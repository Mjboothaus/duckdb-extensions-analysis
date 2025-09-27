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
| **Core Extensions** | 24 |
| **Community Extensions** | 83 |
| **Featured Extensions** | 42 |
| **Total Extensions** | 107 |
| **Recently Active** (≤ 30 days) | 59 |
| **Very Active** (≤ 7 days) | 48 |


---
## Core Extensions

Core extensions maintained by the DuckDB team and distributed via the official extension repository

| # | Extension | Repository | Status | Last Activity | Stars | Language | Description |
|---|-----------|------------|--------|---------------|-------|----------|-------------|
| 1 | [autocomplete](https://duckdb.org/docs/stable/core_extensions/autocomplete.html) | [duckdb/duckdb](https://github.com/duckdb/duckdb/tree/main/extension/autocomplete) | 🟢 Ongoing | 9 days ago | 0 | C++ | Core DuckDB extension: autocomplete |
| 2 | [avro](https://duckdb.org/docs/stable/core_extensions/avro.html) | [duckdb-avro](https://github.com/duckdb/duckdb-avro) | 🟢 Ongoing | 38 days ago | 0 | C++ | Apache Avro format support |
| 3 | [aws](https://duckdb.org/docs/stable/core_extensions/aws.html) | [duckdb-aws](https://github.com/duckdb/duckdb-aws) | 🟢 Ongoing | 18 days ago | 0 | C++ | AWS S3 integration |
| 4 | [azure](https://duckdb.org/docs/stable/core_extensions/azure.html) | [duckdb-azure](https://github.com/duckdb/duckdb-azure) | 🟢 Ongoing | today | 0 | C++ | Azure Blob Storage integration |
| 5 | [delta](https://duckdb.org/docs/stable/core_extensions/delta.html) | [duckdb-delta](https://github.com/duckdb/duckdb-delta) | 🟢 Ongoing | today | 0 | C++ | Delta Lake format support |
| 6 | [ducklake](https://duckdb.org/docs/stable/core_extensions/ducklake.html) | [duckdb/ducklake](https://github.com/duckdb/ducklake) | 🟢 Ongoing | 11 days ago | 0 | C++ | Delta Lake support via DuckLake (different from delta extension) |
| 7 | [encodings](https://duckdb.org/docs/stable/core_extensions/encodings.html) | [duckdb-encodings](https://github.com/duckdb/duckdb-encodings) | 🟢 Ongoing | 9 days ago | 0 | C++ | Character encoding support |
| 8 | [excel](https://duckdb.org/docs/stable/core_extensions/excel.html) | [duckdb-excel](https://github.com/duckdb/duckdb-excel) | 🟢 Ongoing | 23 days ago | 0 | C++ | Excel file format support |
| 9 | [fts](https://duckdb.org/docs/stable/core_extensions/full_text_search.html) | [duckdb-fts](https://github.com/duckdb/duckdb-fts) | 🟢 Ongoing | 10 days ago | 0 | C++ | Full-text search functionality |
| 10 | [httpfs](https://duckdb.org/docs/stable/core_extensions/httpfs/overview.html) | [duckdb-httpfs](https://github.com/duckdb/duckdb-httpfs) | 🟢 Ongoing | today | 0 | C++ | HTTP/S3 filesystem support |
| 11 | [iceberg](https://duckdb.org/docs/stable/core_extensions/iceberg/overview.html) | [duckdb-iceberg](https://github.com/duckdb/duckdb-iceberg) | 🟢 Ongoing | 2 days ago | 0 | C++ | Apache Iceberg format support |
| 12 | [icu](https://duckdb.org/docs/stable/core_extensions/icu.html) | [duckdb/duckdb](https://github.com/duckdb/duckdb/tree/main/extension/icu) | 🟢 Ongoing | 10 days ago | 0 | C++ | Core DuckDB extension: icu |
| 13 | [inet](https://duckdb.org/docs/stable/core_extensions/inet.html) | [duckdb-inet](https://github.com/duckdb/duckdb-inet) | 🟢 Ongoing | 7 days ago | 0 | C++ | Internet address data types |
| 14 | [jemalloc](https://duckdb.org/docs/stable/core_extensions/jemalloc.html) | [duckdb/duckdb](https://github.com/duckdb/duckdb/tree/main/extension/jemalloc) | 🟢 Ongoing | 111 days ago | 0 | C++ | Core DuckDB extension: jemalloc |
| 15 | [json](https://duckdb.org/docs/stable/data/json/overview.html) | [duckdb/duckdb](https://github.com/duckdb/duckdb/tree/main/extension/json) | 🟢 Ongoing | 17 days ago | 0 | C++ | Core DuckDB extension: json |
| 16 | [mysql](https://duckdb.org/docs/stable/core_extensions/mysql.html) | [duckdb-mysql](https://github.com/duckdb/duckdb-mysql) | 🟢 Ongoing | today | 0 | C++ | MySQL database connectivity |
| 17 | [parquet](https://duckdb.org/docs/stable/data/parquet/overview.html) | [duckdb/duckdb](https://github.com/duckdb/duckdb/tree/main/extension/parquet) | 🟢 Ongoing | 3 days ago | 0 | C++ | Core DuckDB extension: parquet |
| 18 | [postgres](https://duckdb.org/docs/stable/core_extensions/postgres.html) | [duckdb-postgres](https://github.com/duckdb/duckdb-postgres) | 🟢 Ongoing | 10 days ago | 0 | C++ | PostgreSQL database connectivity |
| 19 | [spatial](https://duckdb.org/docs/stable/core_extensions/spatial/overview.html) | [duckdb-spatial](https://github.com/duckdb/duckdb-spatial) | 🟢 Ongoing | 2 days ago | 0 | C++ | Geospatial data types and functions |
| 20 | [sqlite](https://duckdb.org/docs/stable/core_extensions/sqlite.html) | [duckdb-sqlite](https://github.com/duckdb/duckdb-sqlite) | 🟢 Ongoing | 10 days ago | 0 | C++ | SQLite database connectivity |
| 21 | [tpcds](https://duckdb.org/docs/stable/core_extensions/tpcds.html) | [duckdb/duckdb](https://github.com/duckdb/duckdb/tree/main/extension/tpcds) | 🟢 Ongoing | 52 days ago | 0 | C++ | Core DuckDB extension: tpcds |
| 22 | [tpch](https://duckdb.org/docs/stable/core_extensions/tpch.html) | [duckdb/duckdb](https://github.com/duckdb/duckdb/tree/main/extension/tpch) | 🟢 Ongoing | 52 days ago | 0 | C++ | Core DuckDB extension: tpch |
| 23 | [ui](https://duckdb.org/docs/stable/core_extensions/ui.html) | [duckdb-ui](https://github.com/duckdb/duckdb-ui) | 🟢 Ongoing | 9 days ago | 0 | C++ | Browser-based user interface for DuckDB |
| 24 | [vss](https://duckdb.org/docs/stable/core_extensions/vss.html) | [duckdb-vss](https://github.com/duckdb/duckdb-vss) | 🟢 Ongoing | 21 days ago | 0 | C++ | Vector similarity search |

**Total:** 24 extensions

---
---
## Community Extensions

Third-party extensions maintained by the community

| # | Extension | Repository | Status | Last Activity | Stars | Language | Description | Featured |
|---|-----------|------------|--------|---------------|-------|----------|-------------|----------|
| 1 | [airport](https://duckdb.org/community_extensions/extensions/airport.html) | [airport](https://github.com/Query-farm/airport) | 🟢 Ongoing | today | 299 | C++ | The Airport extension for DuckDB, enables the use of Arrow Flight with DuckDB | ⭐ |
| 2 | [bitfilters](https://duckdb.org/community_extensions/extensions/bitfilters.html) | [bitfilters](https://github.com/Query-farm/bitfilters) | 🟢 Ongoing | today | 2 | C++ | A high-performance DuckDB extension providing probabilistic data structures f... | ⭐ |
| 3 | [crypto](https://duckdb.org/community_extensions/extensions/crypto.html) | [crypto](https://github.com/Query-farm/crypto) | 🟢 Ongoing | today | 22 | C++ | DuckDB Extension for cryptographic hash functions and HMAC | ⭐ |
| 4 | [datasketches](https://duckdb.org/community_extensions/extensions/datasketches.html) | [datasketches](https://github.com/Query-farm/datasketches) | 🟢 Ongoing | today | 30 | C++ | Integrates DuckDB with the high-performance Apache DataSketches library. This... | ⭐ |
| 5 | [evalexpr_rhai](https://duckdb.org/community_extensions/extensions/evalexpr_rhai.html) | [evalexpr_rhai](https://github.com/Query-farm/evalexpr_rhai) | 🟢 Ongoing | today | 21 | C++ | A DuckDB extension to evaluate the Rhai scripting language as part of SQL. | ⭐ |
| 6 | [fuzzycomplete](https://duckdb.org/community_extensions/extensions/fuzzycomplete.html) | [fuzzycomplete](https://github.com/Query-farm/fuzzycomplete) | 🟢 Ongoing | today | 21 | C++ | DuckDB Extension for fuzzy string matching based autocompletion | ⭐ |
| 7 | [h3](https://duckdb.org/community_extensions/extensions/h3.html) | [h3-duckdb](https://github.com/isaacbrodsky/h3-duckdb) | 🟢 Ongoing | today | 221 | C++ | Bindings for H3 to DuckDB |  |
| 8 | [hashfuncs](https://duckdb.org/community_extensions/extensions/hashfuncs.html) | [hashfuncs](https://github.com/Query-farm/hashfuncs) | 🟢 Ongoing | today | 4 | C++ | A DuckDB extension that supplies non-cryptographic hash functions. | ⭐ |
| 9 | [lindel](https://duckdb.org/community_extensions/extensions/lindel.html) | [lindel](https://github.com/Query-farm/lindel) | 🟢 Ongoing | today | 50 | C++ | DuckDB Extension Linearization/Delinearization, Z-Order, Hilbert and Morton C... | ⭐ |
| 10 | [marisa](https://duckdb.org/community_extensions/extensions/marisa.html) | [marisa](https://github.com/Query-farm/marisa) | 🟢 Ongoing | today | 2 | C++ | The Marisa extension by Query.Farm integrates the fast, space-efficient MARIS... | ⭐ |
| 11 | [pbix](https://duckdb.org/community_extensions/extensions/pbix.html) | [duckdb-pbix-extension](https://github.com/Hugoberry/duckdb-pbix-extension) | 🟢 Ongoing | today | 27 | C++ | Duckdb extension for parsing the metadata and contents of the embedded data m... | ⭐ |
| 12 | [radio](https://duckdb.org/community_extensions/extensions/radio.html) | [radio](https://github.com/Query-farm/radio) | 🟢 Ongoing | today | 30 | C++ | Radio is a DuckDB extension by Query.Farm that brings real-time event streams... | ⭐ |
| 13 | [rapidfuzz](https://duckdb.org/community_extensions/extensions/rapidfuzz.html) | [rapidfuzz](https://github.com/Query-farm/rapidfuzz) | 🟢 Ongoing | today | 3 | C++ | DuckDB Community Extension adding RapidFuzz algorithms for search, deduplicat... | ⭐ |
| 14 | [shellfs](https://duckdb.org/community_extensions/extensions/shellfs.html) | [shellfs](https://github.com/Query-farm/shellfs) | 🟢 Ongoing | today | 81 | C++ | DuckDB extension allowing shell commands to be used for input and output. | ⭐ |
| 15 | [snowflake](https://duckdb.org/community_extensions/extensions/snowflake.html) | [duckdb-snowflake](https://github.com/iqea-ai/duckdb-snowflake) | 🟢 Ongoing | today | 12 | C++ | A powerful DuckDB extension that enables seamless querying of Snowflake datab... | ⭐ |
| 16 | [stochastic](https://duckdb.org/community_extensions/extensions/stochastic.html) | [stochastic](https://github.com/Query-farm/stochastic) | 🟢 Ongoing | today | 11 | C++ | A DuckDB extension that add comprehensive statistical distribution functions... | ⭐ |
| 17 | [textplot](https://duckdb.org/community_extensions/extensions/textplot.html) | [textplot](https://github.com/Query-farm/textplot) | 🟢 Ongoing | today | 10 | C++ | A DuckDB community extension that enables text-based data visualization direc... | ⭐ |
| 18 | [tributary](https://duckdb.org/community_extensions/extensions/tributary.html) | [tributary](https://github.com/Query-farm/tributary) | 🟢 Ongoing | today | 30 | C++ | A DuckDB Extension for Kafka | ⭐ |
| 19 | [vortex](https://duckdb.org/community_extensions/extensions/vortex.html) | [duckdb-vortex](https://github.com/vortex-data/duckdb-vortex) | 🟢 Ongoing | today | 24 | Shell | DuckDB extension allowing reading/writing of vortex files | ⭐ |
| 20 | [quack](https://duckdb.org/community_extensions/extensions/quack.html) | [extension-template](https://github.com/duckdb/extension-template) | 🟢 Ongoing | today | 222 | Python | Template for DuckDB extensions to help you develop, test and deploy a custom... | ⭐ |
| 21 | [httpserver](https://duckdb.org/community_extensions/extensions/httpserver.html) | [httpserver](https://github.com/Query-farm/httpserver) | 🟢 Ongoing | 2 days ago | 231 | HTML | DuckDB HTTP API Server and Query Interface in a  Community Extension |  |
| 22 | [msolap](https://duckdb.org/community_extensions/extensions/msolap.html) | [duckdb-msolap-extension](https://github.com/Hugoberry/duckdb-msolap-extension) | 🟢 Ongoing | 2 days ago | 8 | C++ | DuckDB extension: msolap by Hugoberry |  |
| 23 | [nanodbc](https://duckdb.org/community_extensions/extensions/nanodbc.html) | [duckdb-nanodbc-extension](https://github.com/Hugoberry/duckdb-nanodbc-extension) | 🟢 Ongoing | 2 days ago | 37 | C++ | Database connectivity extension by Hugoberry | ⭐ |
| 24 | [parser_tools](https://duckdb.org/community_extensions/extensions/parser_tools.html) | [duckdb_extension_parser_tools](https://github.com/zfarrell/duckdb_extension_parser_tools) | 🟢 Ongoing | 2 days ago | 15 | C++ | Parse sql - with sql! | ⭐ |
| 25 | [chsql](https://duckdb.org/community_extensions/extensions/chsql.html) | [clickhouse-sql](https://github.com/Query-farm/clickhouse-sql) | 🟢 Ongoing | 3 days ago | 73 | C++ | DuckDB Community Extension implementing ClickHouse SQL Dialect macros and Cus... |  |
| 26 | [chsql_native](https://duckdb.org/community_extensions/extensions/chsql_native.html) | [clickhouse-native](https://github.com/Query-farm/clickhouse-native) | 🟢 Ongoing | 3 days ago | 16 | Rust | Experimental ClickHouse Native Client and Native file reader Extension for Du... |  |
| 27 | [cronjob](https://duckdb.org/community_extensions/extensions/cronjob.html) | [cronjob](https://github.com/Query-farm/cronjob) | 🟢 Ongoing | 3 days ago | 41 | C++ | DuckDB CronJob Extension |  |
| 28 | [http_client](https://duckdb.org/community_extensions/extensions/http_client.html) | [httpclient](https://github.com/Query-farm/httpclient) | 🟢 Ongoing | 3 days ago | 71 | C++ | DuckDB HTTP GET/POST Client in a Community Extension |  |
| 29 | [netquack](https://duckdb.org/community_extensions/extensions/netquack.html) | [duckdb-netquack](https://github.com/hatamiarash7/duckdb-netquack) | 🟢 Ongoing | 3 days ago | 17 | C++ | DuckDB extension for parsing, extracting, and analyzing domains, URIs, and pa... |  |
| 30 | [open_prompt](https://duckdb.org/community_extensions/extensions/open_prompt.html) | [openprompt](https://github.com/Query-farm/openprompt) | 🟢 Ongoing | 3 days ago | 50 | C++ | DuckDB Community Extension to prompt LLMs from SQL |  |
| 31 | [pcap_reader](https://duckdb.org/community_extensions/extensions/pcap_reader.html) | [pcap](https://github.com/Query-farm/pcap) | 🟢 Ongoing | 3 days ago | 11 | Rust | DuckDB PCAP Reader Extension made in Rust |  |
| 32 | [pyroscope](https://duckdb.org/community_extensions/extensions/pyroscope.html) | [pyroscope](https://github.com/Query-farm/pyroscope) | 🟢 Ongoing | 3 days ago | 19 | Rust | DuckDB Pyroscope Extension for Continuous Profiling |  |
| 33 | [quickjs](https://duckdb.org/community_extensions/extensions/quickjs.html) | [quickjs](https://github.com/Query-farm/quickjs) | 🟢 Ongoing | 3 days ago | 8 | C++ | DuckDB extension: quickjs by quackscience | ⭐ |
| 34 | [redis](https://duckdb.org/community_extensions/extensions/redis.html) | [redis](https://github.com/Query-farm/redis) | 🟢 Ongoing | 3 days ago | 7 | C++ | DuckDB Redis Client community extension |  |
| 35 | [splink_udfs](https://duckdb.org/community_extensions/extensions/splink_udfs.html) | [splink_udfs](https://github.com/moj-analytical-services/splink_udfs) | 🟢 Ongoing | 3 days ago | 9 | C++ | DuckDB extension: splink_udfs by moj-analytical-services | ⭐ |
| 36 | [tsid](https://duckdb.org/community_extensions/extensions/tsid.html) | [tsid](https://github.com/Query-farm/tsid) | 🟢 Ongoing | 3 days ago | 5 | C++ | TSID Extension for DuckDB  |  |
| 37 | [webmacro](https://duckdb.org/community_extensions/extensions/webmacro.html) | [webmacro](https://github.com/Query-farm/webmacro) | 🟢 Ongoing | 3 days ago | 13 | C++ | DuckDB WebMacro: Share and Load your SQL Macros via gists |  |
| 38 | [wireduck](https://duckdb.org/community_extensions/extensions/wireduck.html) | [wireduck](https://github.com/hyehudai/wireduck) | 🟢 Ongoing | 3 days ago | 46 | C++ | Duckdb extension to read pcap files | ⭐ |
| 39 | [cache_httpfs](https://duckdb.org/community_extensions/extensions/cache_httpfs.html) | [duck-read-cache-fs](https://github.com/dentiny/duck-read-cache-fs) | 🟢 Ongoing | 4 days ago | 98 | C++ | This repository is made as read-only filesystem for remote access. | ⭐ |
| 40 | [observefs](https://duckdb.org/community_extensions/extensions/observefs.html) | [duckdb-filesystem-observability](https://github.com/dentiny/duckdb-filesystem-observability) | 🟢 Ongoing | 4 days ago | 1 | C++ | Provides observability for duckdb filesystem. | ⭐ |
| 41 | [prql](https://duckdb.org/community_extensions/extensions/prql.html) | [duckdb-prql](https://github.com/ywelsch/duckdb-prql) | 🟢 Ongoing | 4 days ago | 297 | C++ | PRQL as a DuckDB extension | ⭐ |
| 42 | [psql](https://duckdb.org/community_extensions/extensions/psql.html) | [duckdb-psql](https://github.com/ywelsch/duckdb-psql) | 🟢 Ongoing | 4 days ago | 92 | C++ | A piped SQL for DuckDB | ⭐ |
| 43 | [bigquery](https://duckdb.org/community_extensions/extensions/bigquery.html) | [duckdb-bigquery](https://github.com/hafenkran/duckdb-bigquery) | 🟢 Ongoing | 5 days ago | 132 | C++ | Integrates DuckDB with Google BigQuery, allowing direct querying and manageme... | ⭐ |
| 44 | [cwiqduck](https://duckdb.org/community_extensions/extensions/cwiqduck.html) | [cwiqduck](https://github.com/cwiq-os/cwiqduck) | 🟢 Ongoing | 5 days ago | 1 | C++ | DuckDB extensions for CWIQ | ⭐ |
| 45 | [magic](https://duckdb.org/community_extensions/extensions/magic.html) | [duckdb_magic](https://github.com/carlopi/duckdb_magic) | 🟢 Ongoing | 5 days ago | 7 | C++ | Auto-detect file types via `libmagic` (`file` utility) | ⭐ |
| 46 | [zipfs](https://duckdb.org/community_extensions/extensions/zipfs.html) | [duckdb-zipfs](https://github.com/isaacbrodsky/duckdb-zipfs) | 🟢 Ongoing | 5 days ago | 41 | C++ | DuckDB extension to read files within zip archives. | ⭐ |
| 47 | [chaos](https://duckdb.org/community_extensions/extensions/chaos.html) | [duckdb-chaos](https://github.com/taniabogatsch/duckdb-chaos) | 🟢 Ongoing | 7 days ago | 0 | C++ | DuckDB extension: chaos by taniabogatsch | ⭐ |
| 48 | [flock](https://duckdb.org/community_extensions/extensions/flock.html) | [flock](https://github.com/dais-polymtl/flock) | 🟢 Ongoing | 7 days ago | 269 | C++ | Flock: multimodal querying for DuckDB | ⭐ |
| 49 | ~~[gcs](https://duckdb.org/community_extensions/extensions/gcs.html)~~ **NOT FOUND:** https://duckdb.org/community_extensions/extensions/gcs.html (HTTP 404) | [duckdb-gcs](https://github.com/northpolesec/duckdb-gcs) | 🟢 Ongoing | 8 days ago | 0 | C++ | A GCS-native extension for DuckDB |  |
| 50 | [mooncake](https://duckdb.org/community_extensions/extensions/mooncake.html) | [duckdb_mooncake](https://github.com/Mooncake-Labs/duckdb_mooncake) | 🟢 Ongoing | 8 days ago | 0 | C++ | Read Iceberg tables written by moonlink in real time | ⭐ |
| 51 | [file_dialog](https://duckdb.org/community_extensions/extensions/file_dialog.html) | [duckdb-ext-file-dialog](https://github.com/yutannihilation/duckdb-ext-file-dialog) | 🟢 Ongoing | 9 days ago | 14 | Rust | A DuckDB extension to choose file interactively using native file open dialogs | ⭐ |
| 52 | [nanoarrow](https://duckdb.org/community_extensions/extensions/nanoarrow.html) | [duckdb-nanoarrow](https://github.com/paleolimbot/duckdb-nanoarrow) | 🟢 Ongoing | 9 days ago | 46 | C++ | DuckDB extension: nanoarrow by paleolimbot | ⭐ |
| 53 | [rusty_quack](https://duckdb.org/community_extensions/extensions/rusty_quack.html) | [extension-template-rs](https://github.com/duckdb/extension-template-rs) | 🟢 Ongoing | 9 days ago | 80 | Rust | (Experimental) Template for Rust-based DuckDB extensions |  |
| 54 | [st_read_multi](https://duckdb.org/community_extensions/extensions/st_read_multi.html) | [duckdb-ext-st-read-multi](https://github.com/yutannihilation/duckdb-ext-st-read-multi) | 🟢 Ongoing | 9 days ago | 3 | Rust | A DuckDB extension to import multiple geospatial files with `ST_Read_Multi()` | ⭐ |
| 55 | [lua](https://duckdb.org/community_extensions/extensions/lua.html) | [duckdb-lua](https://github.com/isaacbrodsky/duckdb-lua) | 🟢 Ongoing | 10 days ago | 5 | C++ | DuckDB extension to evaluate Lua expressions. | ⭐ |
| 56 | [yaml](https://duckdb.org/community_extensions/extensions/yaml.html) | [duckdb_yaml](https://github.com/teaguesterling/duckdb_yaml) | 🟢 Ongoing | 15 days ago | 9 | C++ |  A DuckDB to read and work with YAML files in a similar way to JSON files (al... |  |
| 57 | [eeagrid](https://duckdb.org/community_extensions/extensions/eeagrid.html) | [duckdb-eeagrid](https://github.com/ahuarte47/duckdb-eeagrid) | 🟢 Ongoing | 16 days ago | 0 | C++ | Functions for transforming XY coordinates to and from the EEA Reference Grid... | ⭐ |
| 58 | [gsheets](https://duckdb.org/community_extensions/extensions/gsheets.html) | [duckdb_gsheets](https://github.com/evidence-dev/duckdb_gsheets) | 🟢 Ongoing | 17 days ago | 298 | C++ | DuckDB extension to read and write Google Sheets using SQL | ⭐ |
| 59 | [faiss](https://duckdb.org/community_extensions/extensions/faiss.html) | [duckdb-faiss-ext](https://github.com/duckdb-faiss-ext/duckdb-faiss-ext) | 🟢 Ongoing | 18 days ago | 25 | Go | DuckDB wrapper for FAISS - Experimental |  |
| 60 | [geography](https://duckdb.org/community_extensions/extensions/geography.html) | [duckdb-geography](https://github.com/paleolimbot/duckdb-geography) | 🟢 Ongoing | 38 days ago | 32 | C++ | Geospatial data extension by paleolimbot |  |
| 61 | [geotiff](https://duckdb.org/community_extensions/extensions/geotiff.html) | [duckdb-geotiff](https://github.com/babaknaimi/duckdb-geotiff) | 🟢 Ongoing | 38 days ago | 2 | C++ | Duckdb extension to read GeoTiffs directly with duckdb database |  |
| 62 | [highs](https://duckdb.org/community_extensions/extensions/highs.html) | [HiGHS-duckdb](https://github.com/fhk/HiGHS-duckdb) | 🟢 Ongoing | 42 days ago | 0 | C++ | Run the solver in the database! |  |
| 63 | [rusty_sheet](https://duckdb.org/community_extensions/extensions/rusty_sheet.html) | [rusty-sheet](https://github.com/redraiment/rusty-sheet) | 🟢 Ongoing | 43 days ago | 17 | Rust | An Excel/OpenDocument Spreadsheets file reader for DuckDB |  |
| 64 | [webbed](https://duckdb.org/community_extensions/extensions/webbed.html) | [duckdb_webbed](https://github.com/teaguesterling/duckdb_webbed) | 🟢 Ongoing | 45 days ago | 15 | C++ | Web/HTTP functionality extension by teaguesterling |  |
| 65 | [read_stat](https://duckdb.org/community_extensions/extensions/read_stat.html) | [duckdb-read-stat](https://github.com/mettekou/duckdb-read-stat) | 🟢 Ongoing | 47 days ago | 22 | C | Read data sets from SAS, Stata, and SPSS from DuckDB with ReadStat |  |
| 66 | [hdf5](https://duckdb.org/community_extensions/extensions/hdf5.html) | [duckdb-hdf5](https://github.com/Berrysoft/duckdb-hdf5) | 🟢 Ongoing | 51 days ago | 9 | Rust | HDF5 plugin for duckdb |  |
| 67 | [duckdb_mcp](https://duckdb.org/community_extensions/extensions/duckdb_mcp.html) | [duckdb_mcp](https://github.com/teaguesterling/duckdb_mcp) | 🟢 Ongoing | 62 days ago | 6 | C++ | A simple MCP server extension for DuckDB |  |
| 68 | [duckpgq](https://duckdb.org/community_extensions/extensions/duckpgq.html) | [duckpgq-extension](https://github.com/cwida/duckpgq-extension) | 🟢 Ongoing | 67 days ago | 264 | C++ | DuckDB extension that adds support for SQL/PGQ and graph algorithms |  |
| 69 | [duck_tails](https://duckdb.org/community_extensions/extensions/duck_tails.html) | [duck_tails](https://github.com/teaguesterling/duck_tails) | 🟢 Ongoing | 69 days ago | 2 | C++ | A DuckDB extension for exploring and reading git history. |  |
| 70 | [capi_quack](https://duckdb.org/community_extensions/extensions/capi_quack.html) | [extension-template-c](https://github.com/duckdb/extension-template-c) | 🟢 Ongoing | 71 days ago | 17 | C | (Experimental) C/C++ template for DuckDB extensions based on the C API | ⭐ |
| 71 | [markdown](https://duckdb.org/community_extensions/extensions/markdown.html) | [duckdb_markdown](https://github.com/teaguesterling/duckdb_markdown) | 🟢 Ongoing | 78 days ago | 5 | C++ | Heirarchical markdown parsing for DuckDB |  |
| 72 | [jwt](https://duckdb.org/community_extensions/extensions/jwt.html) | [duckdb_jwt](https://github.com/GalvinGao/duckdb_jwt) | 🟢 Ongoing | 80 days ago | 0 | C++ | DuckDB extension: jwt by GalvinGao |  |
| 73 | [substrait](https://duckdb.org/community_extensions/extensions/substrait.html) | [duckdb-substrait-extension](https://github.com/substrait-io/duckdb-substrait-extension) | 🟢 Ongoing | 90 days ago | 48 | C++ | DuckDB extension: substrait by substrait-io |  |
| 74 | [quackformers](https://duckdb.org/community_extensions/extensions/quackformers.html) | [quackformers](https://github.com/martin-conur/quackformers) | 🟢 Ongoing | 118 days ago | 6 | Rust | DuckDB NLP extension. |  |
| 75 | [arrow](https://duckdb.org/community_extensions/extensions/arrow.html) | [duckdb-extension-alias](https://github.com/duckdb/duckdb-extension-alias) | 🟢 Ongoing | 141 days ago | 4 | C | DuckDB extension: arrow |  |
| 76 | [ofquack](https://duckdb.org/community_extensions/extensions/ofquack.html) | [ofquack](https://github.com/krokozyab/ofquack) | 🟢 Ongoing | 157 days ago | 5 | C++ | Oracle Fusion DuckDB extension  |  |
| 77 | [scrooge](https://duckdb.org/community_extensions/extensions/scrooge.html) | [Scrooge-McDuck](https://github.com/pdet/Scrooge-McDuck) | 🟢 Ongoing | 165 days ago | 148 | C++ | DuckDB extension: scrooge by pdet |  |
| 78 | [blockduck](https://duckdb.org/community_extensions/extensions/blockduck.html) | [BlockDuck](https://github.com/luohaha/BlockDuck) | 🟢 Ongoing | 184 days ago | 8 | C++ | Live SQL Queries on Blockchain |  |
| 79 | [hostfs](https://duckdb.org/community_extensions/extensions/hostfs.html) | [hostFS](https://github.com/gropaul/hostFS) | 🟢 Ongoing | 200 days ago | 23 | C++ | DuckDB extension: hostfs by gropaul |  |
| 80 | [sheetreader](https://duckdb.org/community_extensions/extensions/sheetreader.html) | [sheetreader-duckdb](https://github.com/polydbms/sheetreader-duckdb) | 🟢 Ongoing | 346 days ago | 55 | Jupyter Notebook | DuckDB extension: sheetreader by polydbms |  |
| 81 | [pivot_table](https://duckdb.org/community_extensions/extensions/pivot_table.html) | [pivot_table](https://github.com/Alex-Monahan/pivot_table) | 🟢 Ongoing | over a year ago | 15 | C++ | Full spreadsheet-style pivot table through SQL macros. Just specify values, r... |  |
| 82 | [tarfs](https://duckdb.org/community_extensions/extensions/tarfs.html) | [duckdb_tarfs](https://github.com/Maxxen/duckdb_tarfs) | 🟢 Ongoing | over a year ago | 10 | C++ | DuckDB extension: tarfs by Maxxen |  |
| 83 | [ulid](https://duckdb.org/community_extensions/extensions/ulid.html) | [duckdb_ulid](https://github.com/Maxxen/duckdb_ulid) | 🟢 Ongoing | over a year ago | 24 | C++ | DuckDB extension: ulid by Maxxen |  |

**Total:** 83 extensions  
**Featured:** 42 extensions (marked with ⭐)
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
