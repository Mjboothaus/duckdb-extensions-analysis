# DuckDB Extensions Status Report

Generated on: **2025-09-21 21:23:28 UTC**

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
- **Featured**: [Community Extensions Page](https://duckdb.org/community_extensions/)
- **Individual Repositories**: GitHub repositories linked in the extensions directory

---

## Core Extensions

DuckDB core extensions from version **v1.4.0** (released 5 days ago).

| # | Extension | Repository | Status | Last Activity | Stars | Language | Description |
|---|-----------|------------|--------|---------------|-------|----------|-------------|
| 1 | **[autocomplete](https://duckdb.org/docs/stable/core_extensions/autocomplete.html)** | [duckdb/duckdb](https://github.com/duckdb/duckdb) | ✅ Active | 3 days ago | — | C++ | Auto-completion support for DuckDB CLI |
| 2 | **[avro](https://duckdb.org/docs/stable/core_extensions/avro.html)** | [duckdb/duckdb-avro](https://github.com/duckdb/duckdb-avro) | ✅ Active | 32 days ago | — | C++ | Apache Avro format support for reading and writing |
| 3 | **[aws](https://duckdb.org/docs/stable/core_extensions/aws.html)** | [duckdb/duckdb-aws](https://github.com/duckdb/duckdb-aws) | ✅ Active | 13 days ago | — | C++ | AWS S3 integration and cloud services support |
| 4 | **[azure](https://duckdb.org/docs/stable/core_extensions/azure.html)** | [duckdb/duckdb-azure](https://github.com/duckdb/duckdb-azure) | ✅ Active | 3 days ago | — | C++ | Azure Blob Storage integration and cloud services |
| 5 | **[delta](https://duckdb.org/docs/stable/core_extensions/delta.html)** | [duckdb/duckdb-delta](https://github.com/duckdb/duckdb-delta) | ✅ Active | 2 days ago | — | C++ | Delta Lake format support for ACID transactions |
| 6 | **[ducklake](https://duckdb.org/docs/stable/core_extensions/ducklake.html)** | [duckdb/duckdb](https://github.com/duckdb/duckdb) | ✅ Active | ~5 days ago | — | C++ | Delta Lake support via DuckLake implementation |
| 7 | **[encodings](https://duckdb.org/docs/stable/core_extensions/encodings.html)** | [duckdb/duckdb-encodings](https://github.com/duckdb/duckdb-encodings) | ✅ Active | 3 days ago | — | C++ | Character encoding support for text processing |
| 8 | **[excel](https://duckdb.org/docs/stable/core_extensions/excel.html)** | [duckdb/duckdb-excel](https://github.com/duckdb/duckdb-excel) | ✅ Active | 17 days ago | — | C++ | Microsoft Excel file format support |
| 9 | **[fts](https://duckdb.org/docs/stable/core_extensions/full_text_search.html)** | [duckdb/duckdb-fts](https://github.com/duckdb/duckdb-fts) | ✅ Active | 4 days ago | — | C++ | Full-text search functionality and indexing |
| 10 | **[httpfs](https://duckdb.org/docs/stable/core_extensions/httpfs/overview.html)** | [duckdb/duckdb-httpfs](https://github.com/duckdb/duckdb-httpfs) | ✅ Active | 9 days ago | — | C++ | HTTP/S3 filesystem support for remote data |
| 11 | **[iceberg](https://duckdb.org/docs/stable/core_extensions/iceberg/overview.html)** | [duckdb/duckdb-iceberg](https://github.com/duckdb/duckdb-iceberg) | ✅ Active | 2 days ago | — | C++ | Apache Iceberg format support for data lakes |
| 12 | **[icu](https://duckdb.org/docs/stable/core_extensions/icu.html)** | [duckdb/duckdb](https://github.com/duckdb/duckdb) | ✅ Active | 4 days ago | — | C++ | International Components for Unicode support |
| 13 | **[inet](https://duckdb.org/docs/stable/core_extensions/inet.html)** | [duckdb/duckdb-inet](https://github.com/duckdb/duckdb-inet) | ✅ Active | 1 days ago | — | C++ | Internet address data types and functions |
| 14 | **[jemalloc](https://duckdb.org/docs/stable/core_extensions/jemalloc.html)** | [duckdb/duckdb](https://github.com/duckdb/duckdb) | ✅ Active | 106 days ago | — | C++ | Memory allocator for improved performance |
| 15 | **[json](https://duckdb.org/docs/stable/data/json/overview.html)** | [duckdb/duckdb](https://github.com/duckdb/duckdb) | ✅ Active | 12 days ago | — | C++ | JSON data format support and functions |
| 16 | **[mysql](https://duckdb.org/docs/stable/core_extensions/mysql.html)** | [duckdb/duckdb-mysql](https://github.com/duckdb/duckdb-mysql) | ✅ Active | 14 days ago | — | C++ | MySQL database connectivity and integration |
| 17 | **[parquet](https://duckdb.org/docs/stable/data/parquet/overview.html)** | [duckdb/duckdb](https://github.com/duckdb/duckdb) | ✅ Active | 3 days ago | — | C++ | Apache Parquet columnar format support |
| 18 | **[postgres](https://duckdb.org/docs/stable/core_extensions/postgres.html)** | [duckdb/duckdb-postgres](https://github.com/duckdb/duckdb-postgres) | ✅ Active | 4 days ago | — | C++ | PostgreSQL database connectivity and integration |
| 19 | **[spatial](https://duckdb.org/docs/stable/core_extensions/spatial/overview.html)** | [duckdb/duckdb-spatial](https://github.com/duckdb/duckdb-spatial) | ✅ Active | 10 days ago | — | C++ | Geospatial data types and spatial functions |
| 20 | **[sqlite](https://duckdb.org/docs/stable/core_extensions/sqlite.html)** | [duckdb/duckdb-sqlite](https://github.com/duckdb/duckdb-sqlite) | ✅ Active | 4 days ago | — | C++ | SQLite database connectivity and integration |
| 21 | **[tpcds](https://duckdb.org/docs/stable/core_extensions/tpcds.html)** | [duckdb/duckdb](https://github.com/duckdb/duckdb) | ✅ Active | 46 days ago | — | C++ | TPC-DS benchmark data generation |
| 22 | **[tpch](https://duckdb.org/docs/stable/core_extensions/tpch.html)** | [duckdb/duckdb](https://github.com/duckdb/duckdb) | ✅ Active | 46 days ago | — | C++ | TPC-H benchmark data generation |
| 23 | **[ui](https://duckdb.org/docs/stable/core_extensions/ui.html)** | [duckdb/duckdb-ui](https://github.com/duckdb/duckdb-ui) | ✅ Active | 4 days ago | — | C++ | Browser-based user interface for DuckDB |
| 24 | **[vss](https://duckdb.org/docs/stable/core_extensions/vss.html)** | [duckdb/duckdb-vss](https://github.com/duckdb/duckdb-vss) | ✅ Active | 16 days ago | — | C++ | Vector similarity search capabilities |

**Total Core Extensions**: 24


## Community Extensions

| # | Extension | Repository | Status | Last Activity | Stars | Language | Description |
|---|-----------|------------|--------|---------------|-------|----------|-------------|
| 1 | **airport** | [Query-farm/airport](https://github.com/Query-farm/airport) | ✅ Active | 3 days ago | 297 | C++ | The Airport extension for DuckDB, enables the use ... |
| 2 | **arrow** | [duckdb/duckdb-extension-alias](https://github.com/duckdb/duckdb-extension-alias) | ✅ Active | 135 days ago | 4 | C | DuckDB extension: arrow |
| 3 | **bigquery** | [hafenkran/duckdb-bigquery](https://github.com/hafenkran/duckdb-bigquery) | ✅ Active | 4 days ago | 130 | C++ | Integrates DuckDB with Google BigQuery, allowing d... |
| 4 | **bitfilters** | [Query-farm/bitfilters](https://github.com/Query-farm/bitfilters) | ✅ Active | 6 days ago | 2 | C++ | A high-performance DuckDB extension providing prob... |
| 5 | **blockduck** | [luohaha/BlockDuck](https://github.com/luohaha/BlockDuck) | ✅ Active | 179 days ago | 8 | C++ | Live SQL Queries on Blockchain |
| 6 | **cache_httpfs** | [dentiny/duck-read-cache-fs](https://github.com/dentiny/duck-read-cache-fs) | ✅ Active | 0 days ago | 96 | C++ | This repository is made as read-only filesystem fo... |
| 7 | **capi_quack** | [duckdb/extension-template-c](https://github.com/duckdb/extension-template-c) | ✅ Active | 66 days ago | 17 | C | (Experimental) C/C++ template for DuckDB extension... |
| 8 | **chaos** | [taniabogatsch/duckdb-chaos](https://github.com/taniabogatsch/duckdb-chaos) | ✅ Active | 2 days ago | 0 | C++ | DuckDB extension: chaos by taniabogatsch |
| 9 | **chsql** | [Query-farm/duckdb-extension-clickhouse-sql](https://github.com/Query-farm/duckdb-extension-clickhouse-sql) | ✅ Active | 30 days ago | 70 | C++ | DuckDB Community Extension implementing ClickHouse... |
| 10 | **chsql_native** | [Query-farm/duckdb-extension-clickhouse-native](https://github.com/Query-farm/duckdb-extension-clickhouse-native) | ✅ Active | 60 days ago | 16 | Rust | Experimental ClickHouse Native Client and Native f... |
| 11 | **cronjob** | [Query-farm/duckdb-extension-cronjob](https://github.com/Query-farm/duckdb-extension-cronjob) | ✅ Active | 12 days ago | 41 | C++ | DuckDB CronJob Extension |
| 12 | **crypto** | [Query-farm/crypto](https://github.com/Query-farm/crypto) | ✅ Active | 104 days ago | 22 | Rust | DuckDB Extension for cryptographic hash functions ... |
| 13 | **cwiqduck** | [cwiq-os/cwiqduck](https://github.com/cwiq-os/cwiqduck) | ✅ Active | 2 days ago | 1 | C++ | DuckDB extensions for CWIQ |
| 14 | **datasketches** | [Query-farm/datasketches](https://github.com/Query-farm/datasketches) | ✅ Active | 64 days ago | 25 | C++ | Integrates DuckDB with the high-performance Apache... |
| 15 | **duck_tails** | [teaguesterling/duck_tails](https://github.com/teaguesterling/duck_tails) | ✅ Active | 64 days ago | 2 | C++ | A DuckDB extension for exploring and reading git h... |
| 16 | **duckdb_mcp** | [teaguesterling/duckdb_mcp](https://github.com/teaguesterling/duckdb_mcp) | ✅ Active | 57 days ago | 6 | C++ | A simple MCP server extension for DuckDB |
| 17 | **duckpgq** | [cwida/duckpgq-extension](https://github.com/cwida/duckpgq-extension) | ✅ Active | 61 days ago | 261 | C++ | DuckDB extension that adds support for SQL/PGQ and... |
| 18 | **eeagrid** | [ahuarte47/duckdb-eeagrid](https://github.com/ahuarte47/duckdb-eeagrid) | ✅ Active | 11 days ago | 0 | C++ | Functions for transforming XY coordinates to and f... |
| 19 | **evalexpr_rhai** | [Query-farm/evalexpr_rhai](https://github.com/Query-farm/evalexpr_rhai) | ✅ Active | 103 days ago | 21 | C++ | A DuckDB extension to evaluate the Rhai scripting ... |
| 20 | **faiss** | [duckdb-faiss-ext/duckdb-faiss-ext](https://github.com/duckdb-faiss-ext/duckdb-faiss-ext) | ✅ Active | 13 days ago | 25 | Go | DuckDB wrapper for FAISS - Experimental |
| 21 | **file_dialog** | [yutannihilation/duckdb-ext-file-dialog](https://github.com/yutannihilation/duckdb-ext-file-dialog) | ✅ Active | 3 days ago | 14 | Rust | A DuckDB extension to choose file interactively us... |
| 22 | **flock** | [dais-polymtl/flock](https://github.com/dais-polymtl/flock) | ✅ Active | 2 days ago | 269 | C++ | FlockMTL: DuckDB extension for multimodal querying... |
| 23 | **fuzzycomplete** | [Query-farm/fuzzycomplete](https://github.com/Query-farm/fuzzycomplete) | ✅ Active | 103 days ago | 21 | C++ | DuckDB Extension for fuzzy string matching based a... |
| 24 | **geography** | [paleolimbot/duckdb-geography](https://github.com/paleolimbot/duckdb-geography) | ✅ Active | 33 days ago | 32 | C++ | Geospatial data extension by paleolimbot |
| 25 | **geotiff** | [babaknaimi/duckdb-geotiff](https://github.com/babaknaimi/duckdb-geotiff) | ✅ Active | 32 days ago | 2 | C++ | Duckdb extension to read GeoTiffs directly with du... |
| 26 | **gsheets** | [evidence-dev/duckdb_gsheets](https://github.com/evidence-dev/duckdb_gsheets) | ✅ Active | 12 days ago | 298 | C++ | DuckDB extension to read and write Google Sheets u... |
| 27 | **h3** | [isaacbrodsky/h3-duckdb](https://github.com/isaacbrodsky/h3-duckdb) | ✅ Active | 5 days ago | 220 | C++ | Bindings for H3 to DuckDB |
| 28 | **hashfuncs** | [Query-farm/hashfuncs](https://github.com/Query-farm/hashfuncs) | ✅ Active | 45 days ago | 4 | C++ | A DuckDB extension that supplies non-cryptographic... |
| 29 | **hdf5** | [Berrysoft/duckdb-hdf5](https://github.com/Berrysoft/duckdb-hdf5) | ✅ Active | 45 days ago | 9 | Rust | HDF5 plugin for duckdb |
| 30 | **highs** | [fhk/HiGHS-duckdb](https://github.com/fhk/HiGHS-duckdb) | ✅ Active | 36 days ago | 0 | C++ | Run the solver in the database! |
| 31 | **hostfs** | [gropaul/hostFS](https://github.com/gropaul/hostFS) | ✅ Active | 194 days ago | 23 | C++ | DuckDB extension: hostfs by gropaul |
| 32 | **http_client** | [Query-farm/duckdb-extension-httpclient](https://github.com/Query-farm/duckdb-extension-httpclient) | ✅ Active | 55 days ago | 70 | C++ | DuckDB HTTP GET/POST Client in a Community Extensi... |
| 33 | **httpserver** | [Query-farm/duckdb-extension-httpserver](https://github.com/Query-farm/duckdb-extension-httpserver) | ✅ Active | 40 days ago | 230 | HTML | DuckDB HTTP API Server and Query Interface in a  C... |
| 34 | **jwt** | [GalvinGao/duckdb_jwt](https://github.com/GalvinGao/duckdb_jwt) | ✅ Active | 74 days ago | 0 | C++ | DuckDB extension: jwt by GalvinGao |
| 35 | **lindel** | [Query-farm/lindel](https://github.com/Query-farm/lindel) | ✅ Active | 65 days ago | 50 | C++ | DuckDB Extension Linearization/Delinearization, Z-... |
| 36 | **lua** | [isaacbrodsky/duckdb-lua](https://github.com/isaacbrodsky/duckdb-lua) | ✅ Active | 4 days ago | 4 | C++ | DuckDB extension to evaluate Lua expressions. |
| 37 | **magic** | [carlopi/duckdb_magic](https://github.com/carlopi/duckdb_magic) | ✅ Active | 4 days ago | 7 | C++ | Auto-detect file types via `libmagic` (`file` util... |
| 38 | **marisa** | [Query-farm/marisa](https://github.com/Query-farm/marisa) | ✅ Active | 45 days ago | 2 | C++ | The Marisa extension by Query.Farm integrates the ... |
| 39 | **markdown** | [teaguesterling/duckdb_markdown](https://github.com/teaguesterling/duckdb_markdown) | ✅ Active | 72 days ago | 5 | C++ | Heirarchical markdown parsing for DuckDB |
| 40 | **mooncake** | [Mooncake-Labs/duckdb_mooncake](https://github.com/Mooncake-Labs/duckdb_mooncake) | ✅ Active | 2 days ago | 0 | C++ | Read Iceberg tables written by moonlink in real ti... |
| 41 | **msolap** | [Hugoberry/duckdb-msolap-extension](https://github.com/Hugoberry/duckdb-msolap-extension) | ✅ Active | 2 days ago | 8 | C++ | DuckDB extension: msolap by Hugoberry |
| 42 | **nanoarrow** | [paleolimbot/duckdb-nanoarrow](https://github.com/paleolimbot/duckdb-nanoarrow) | ✅ Active | 4 days ago | 45 | C++ | DuckDB extension: nanoarrow by paleolimbot |
| 43 | **nanodbc** | [Hugoberry/duckdb-nanodbc-extension](https://github.com/Hugoberry/duckdb-nanodbc-extension) | ✅ Active | 2 days ago | 34 | C++ | Database connectivity extension by Hugoberry |
| 44 | **netquack** | [hatamiarash7/duckdb-netquack](https://github.com/hatamiarash7/duckdb-netquack) | ✅ Active | 107 days ago | 17 | C++ | DuckDB extension for parsing, extracting, and anal... |
| 45 | **observefs** | [dentiny/duckdb-filesystem-observability](https://github.com/dentiny/duckdb-filesystem-observability) | ✅ Active | 0 days ago | 0 | C++ | Provides observability for duckdb filesystem. |
| 46 | **ofquack** | [krokozyab/ofquack](https://github.com/krokozyab/ofquack) | ✅ Active | 152 days ago | 5 | C++ | Oracle Fusion DuckDB extension  |
| 47 | **open_prompt** | [Query-farm/duckdb-extension-openprompt](https://github.com/Query-farm/duckdb-extension-openprompt) | ✅ Active | 256 days ago | 50 | C++ | DuckDB Community Extension to prompt LLMs from SQL |
| 48 | **parser_tools** | [zfarrell/duckdb_extension_parser_tools](https://github.com/zfarrell/duckdb_extension_parser_tools) | ✅ Active | 2 days ago | 15 | C++ | Parse sql - with sql! |
| 49 | **pbix** | [Hugoberry/duckdb-pbix-extension](https://github.com/Hugoberry/duckdb-pbix-extension) | ✅ Active | 2 days ago | 27 | C++ | Duckdb extension for parsing the metadata and cont... |
| 50 | **pcap_reader** | [Query-farm/duckdb-extension-pcap](https://github.com/Query-farm/duckdb-extension-pcap) | ✅ Active | 104 days ago | 10 | Rust | DuckDB PCAP Reader Extension made in Rust |
| 51 | **pivot_table** | [Alex-Monahan/pivot_table](https://github.com/Alex-Monahan/pivot_table) | ✅ Active | 364 days ago | 15 | C++ | Full spreadsheet-style pivot table through SQL mac... |
| 52 | **prql** | [ywelsch/duckdb-prql](https://github.com/ywelsch/duckdb-prql) | ✅ Active | 188 days ago | 297 | C++ | PRQL as a DuckDB extension |
| 53 | **psql** | [ywelsch/duckdb-psql](https://github.com/ywelsch/duckdb-psql) | ✅ Active | 167 days ago | 92 | C++ | A piped SQL for DuckDB |
| 54 | **pyroscope** | [Query-farm/duckdb-extension-pyroscope](https://github.com/Query-farm/duckdb-extension-pyroscope) | ✅ Active | 104 days ago | 19 | Rust | DuckDB Pyroscope Extension for Continuous Profilin... |
| 55 | **quack** | [duckdb/extension-template](https://github.com/duckdb/extension-template) | ✅ Active | 5 days ago | 221 | Python | Template for DuckDB extensions to help you develop... |
| 56 | **quackformers** | [martin-conur/quackformers](https://github.com/martin-conur/quackformers) | ✅ Active | 113 days ago | 6 | Rust | DuckDB NLP extension. |
| 57 | **quickjs** | [Query-farm/duckdb-quickjs](https://github.com/Query-farm/duckdb-quickjs) | ✅ Active | 85 days ago | 8 | C++ | DuckDB extension: quickjs by quackscience |
| 58 | **radio** | [Query-farm/radio](https://github.com/Query-farm/radio) | ✅ Active | 100 days ago | 30 | C++ | Radio is a DuckDB extension by Query.Farm that bri... |
| 59 | **rapidfuzz** | [Query-farm/rapidfuzz](https://github.com/Query-farm/rapidfuzz) | ✅ Active | 3 days ago | 3 | C++ | DuckDB extension: rapidfuzz |
| 60 | **read_stat** | [mettekou/duckdb-read-stat](https://github.com/mettekou/duckdb-read-stat) | ✅ Active | 41 days ago | 22 | C | Read data sets from SAS, Stata, and SPSS from Duck... |
| 61 | **redis** | [Query-farm/duckdb-extension-redis](https://github.com/Query-farm/duckdb-extension-redis) | ✅ Active | 100 days ago | 7 | C++ | DuckDB Redis Client community extension |
| 62 | **rusty_quack** | [duckdb/extension-template-rs](https://github.com/duckdb/extension-template-rs) | ✅ Active | 3 days ago | 80 | Rust | (Experimental) Template for Rust-based DuckDB exte... |
| 63 | **rusty_sheet** | [redraiment/rusty-sheet](https://github.com/redraiment/rusty-sheet) | ✅ Active | 38 days ago | 17 | Rust | An Excel/OpenDocument Spreadsheets file reader for... |
| 64 | **scrooge** | [pdet/Scrooge-McDuck](https://github.com/pdet/Scrooge-McDuck) | ✅ Active | 160 days ago | 149 | C++ | DuckDB extension: scrooge by pdet |
| 65 | **sheetreader** | [polydbms/sheetreader-duckdb](https://github.com/polydbms/sheetreader-duckdb) | ✅ Active | 341 days ago | 55 | Jupyter Notebook | DuckDB extension: sheetreader by polydbms |
| 66 | **shellfs** | [Query-farm/shellfs](https://github.com/Query-farm/shellfs) | ✅ Active | 6 days ago | 80 | C++ | DuckDB extension allowing shell commands to be use... |
| 67 | **snowflake** | [iqea-ai/duckdb-snowflake](https://github.com/iqea-ai/duckdb-snowflake) | ✅ Active | 2 days ago | 9 | C++ | A powerful DuckDB extension that enables seamless ... |
| 68 | **splink_udfs** | [moj-analytical-services/splink_udfs](https://github.com/moj-analytical-services/splink_udfs) | ✅ Active | 5 days ago | 8 | C++ | DuckDB extension: splink_udfs by moj-analytical-se... |
| 69 | **st_read_multi** | [yutannihilation/duckdb-ext-st-read-multi](https://github.com/yutannihilation/duckdb-ext-st-read-multi) | ✅ Active | 3 days ago | 3 | Rust | A DuckDB extension to import multiple geospatial f... |
| 70 | **stochastic** | [Query-farm/stochastic](https://github.com/Query-farm/stochastic) | ✅ Active | 6 days ago | 11 | C++ | A DuckDB extension that add comprehensive statisti... |
| 71 | **substrait** | [substrait-io/duckdb-substrait-extension](https://github.com/substrait-io/duckdb-substrait-extension) | ✅ Active | 84 days ago | 48 | C++ | DuckDB extension: substrait by substrait-io |
| 72 | **tarfs** | [Maxxen/duckdb_tarfs](https://github.com/Maxxen/duckdb_tarfs) | ✅ Active | 391 days ago | 10 | C++ | DuckDB extension: tarfs by Maxxen |
| 73 | **textplot** | [Query-farm/textplot](https://github.com/Query-farm/textplot) | ✅ Active | 6 days ago | 9 | C++ | A DuckDB community extension that enables text-bas... |
| 74 | **tributary** | [Query-farm/tributary](https://github.com/Query-farm/tributary) | ✅ Active | 100 days ago | 29 | C++ | A DuckDB Extension for Kafka |
| 75 | **tsid** | [Query-farm/duckdb-extension-tsid](https://github.com/Query-farm/duckdb-extension-tsid) | ✅ Active | 286 days ago | 5 | C++ | TSID Extension for DuckDB  |
| 76 | **ulid** | [Maxxen/duckdb_ulid](https://github.com/Maxxen/duckdb_ulid) | ✅ Active | 439 days ago | 24 | C++ | DuckDB extension: ulid by Maxxen |
| 77 | **vortex** | [vortex-data/duckdb-vortex](https://github.com/vortex-data/duckdb-vortex) | ✅ Active | 4 days ago | 24 | Shell | DuckDB extension allowing reading/writing of vorte... |
| 78 | **webbed** | [teaguesterling/duckdb_webbed](https://github.com/teaguesterling/duckdb_webbed) | ✅ Active | 39 days ago | 13 | C++ | Web/HTTP functionality extension by teaguesterling |
| 79 | **webmacro** | [Query-farm/duckdb-extension-webmacro](https://github.com/Query-farm/duckdb-extension-webmacro) | ✅ Active | 280 days ago | 13 | C++ | DuckDB WebMacro: Share and Load your SQL Macros vi... |
| 80 | **wireduck** | [hyehudai/wireduck](https://github.com/hyehudai/wireduck) | ✅ Active | 162 days ago | 45 | C++ | Duckdb extension to read pcap files |
| 81 | **yaml** | [teaguesterling/duckdb_yaml](https://github.com/teaguesterling/duckdb_yaml) | ✅ Active | 10 days ago | 9 | C++ |  A DuckDB to read and work with YAML files in a si... |
| 82 | **zipfs** | [isaacbrodsky/duckdb-zipfs](https://github.com/isaacbrodsky/duckdb-zipfs) | ✅ Active | 2 days ago | 41 | C++ | DuckDB extension to read files within zip archives... |

### Community Extensions Summary
- **Total Extensions**: 82
- **Active Extensions**: 82 (100.0%)
- **Archived Extensions**: 0 (0.0%)
- **Extensions with Issues**: 0 (0.0%)


---

## Appendix: DuckDB Release Information

### Current Release Context

DuckDB follows **semantic versioning** with regular releases. For complete and up-to-date release information, see the official [**DuckDB Release Calendar**](https://duckdb.org/release_calendar.html).

### Release History

| Version | Release Date | Codename | Named After | LTS | Blog Post |
|---------|--------------|----------|-------------|-----|-----------|
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
- **📦 GitHub Releases**: [github.com/duckdb/duckdb/releases](https://github.com/duckdb/duckdb/releases)
- **📰 Release Notes**: [duckdb.org/news/](https://duckdb.org/news/)
- **🛠️ Development Roadmap**: [github.com/duckdb/duckdb/discussions/6499](https://github.com/duckdb/duckdb/discussions/6499)

*Data sourced from the official [DuckDB releases CSV](https://duckdb.org/data/duckdb-releases.csv). For the most current information, always check the [release calendar](https://duckdb.org/release_calendar.html).*

## Data Sources & Methodology

This analysis is based on the following authoritative sources and their structural conventions:

### Core Extensions Data Sources
- **Primary**: [Core Extensions Documentation](https://duckdb.org/docs/stable/core_extensions/overview.html)
- **Secondary**: [Extensions Overview](https://duckdb.org/docs/stable/extensions/overview.html)  
- **GitHub Repository**: [duckdb/duckdb](https://github.com/duckdb/duckdb) for commit history and development stages

**Important Notes on Documentation Structure Exceptions:**
- Some core extensions like `json` and `parquet` have documentation under `/docs/stable/data/` rather than `/docs/stable/core_extensions/`
- URL patterns vary: some use `/extension_name.html` while others use `/extension_name/overview.html`
- The documentation structure may evolve over time, requiring periodic updates to URL discovery logic

### Community Extensions Data Sources  
- **Registry**: [Community Extensions Repository](https://github.com/duckdb/community-extensions)
- **Directory**: [Extensions Folder](https://github.com/duckdb/community-extensions/tree/main/extensions)
- **Featured Page**: [Community Extensions](https://duckdb.org/community_extensions/)
- **Individual Repositories**: GitHub repositories linked in the extensions directory

### Status Determination Methodology
- ✅ **Ongoing**: Repository is active and not archived
- 🔴 **Discontinued**: Repository is archived or marked as discontinued  
- ❌ **No Repo/Error**: Repository information unavailable or inaccessible

### Activity & Update Metrics
- **Core Extensions**: Based on last commit date to DuckDB repository for extension-specific code
- **Community Extensions**: Based on last push/commit date to individual extension repositories
- **Caching**: API responses are cached (24 hours for URLs, configurable for other data) to improve performance and reduce rate limiting

### Data Quality & Reliability Notes
- URL discovery relies on parsing HTML documentation pages, which may change structure
- GitHub API rate limits may occasionally affect data freshness
- Extension metadata quality varies between community extensions
- Some extensions may have multiple repositories or documentation locations

Report generated using the [duckdb-extensions-analysis](https://github.com/Mjboothaus/duckdb-extensions-analysis) tool.