# DuckDB Extensions Status Report

Generated on: **2025-09-19 11:17:15 UTC**

This report provides a comprehensive analysis of DuckDB extensions, including both core extensions (built into DuckDB) and community-contributed extensions.

## Core Extensions

DuckDB core extensions from version **v1.4.0** (released 3 days ago).

| Extension | Development Stage | Status | Last Updated |
|-----------|-------------------|--------|--------------|
| **autocomplete** | Stable | ✅ Ongoing | 3 days ago (in v1.4.0) |
| **avro** | GitHub | ✅ Ongoing | 3 days ago (in v1.4.0) |
| **aws** | GitHub | ✅ Ongoing | 3 days ago (in v1.4.0) |
| **azure** | GitHub | ✅ Ongoing | 3 days ago (in v1.4.0) |
| **delta** | GitHub | ✅ Ongoing | 3 days ago (in v1.4.0) |
| **ducklake** | GitHub | ✅ Ongoing | 3 days ago (in v1.4.0) |
| **encodings** | GitHub | ✅ Ongoing | 3 days ago (in v1.4.0) |
| **excel** | GitHub | ✅ Ongoing | 3 days ago (in v1.4.0) |
| **fts** | GitHub | ✅ Ongoing | 3 days ago (in v1.4.0) |
| **httpfs** | GitHub | ✅ Ongoing | 3 days ago (in v1.4.0) |
| **iceberg** | GitHub | ✅ Ongoing | 3 days ago (in v1.4.0) |
| **icu** | Stable | ✅ Ongoing | 3 days ago (in v1.4.0) |
| **inet** | GitHub | ✅ Ongoing | 3 days ago (in v1.4.0) |
| **jemalloc** | Stable | ✅ Ongoing | 3 days ago (in v1.4.0) |
| **json** | Stable | ✅ Ongoing | 3 days ago (in v1.4.0) |
| **mysql** | GitHub | ✅ Ongoing | 3 days ago (in v1.4.0) |
| **parquet** | Stable | ✅ Ongoing | 3 days ago (in v1.4.0) |
| **postgres** | GitHub | ✅ Ongoing | 3 days ago (in v1.4.0) |
| **spatial** | GitHub | ✅ Ongoing | 3 days ago (in v1.4.0) |
| **sqlite** | GitHub | ✅ Ongoing | 3 days ago (in v1.4.0) |
| **tpcds** | Stable | ✅ Ongoing | 3 days ago (in v1.4.0) |
| **tpch** | Stable | ✅ Ongoing | 3 days ago (in v1.4.0) |
| **ui** | GitHub | ✅ Ongoing | 3 days ago (in v1.4.0) |
| **vss** | GitHub | ✅ Ongoing | 3 days ago (in v1.4.0) |

**Total Core Extensions**: 24


## Community Extensions

| Extension | Repository | Status | Last Push | Stars | Language | Description |
|-----------|------------|--------|-----------|-------|----------|-------------|
| **airport** | [query-farm/airport](https://github.com/query-farm/airport) | ✅ Ongoing | 0 days ago | 297 | C++ | The Airport extension for DuckDB, enables the use ... |
| **nanodbc** | [Hugoberry/duckdb-nanodbc-extension](https://github.com/Hugoberry/duckdb-nanodbc-extension) | ✅ Ongoing | 0 days ago | 34 | C++ | No description |
| **zipfs** | [isaacbrodsky/duckdb-zipfs](https://github.com/isaacbrodsky/duckdb-zipfs) | ✅ Ongoing | 0 days ago | 41 | C++ | DuckDB extension to read files within zip archives... |
| **bigquery** | [hafenkran/duckdb-bigquery](https://github.com/hafenkran/duckdb-bigquery) | ✅ Ongoing | 1 days ago | 130 | C++ | Integrates DuckDB with Google BigQuery, allowing d... |
| **file_dialog** | [yutannihilation/duckdb-ext-file-dialog](https://github.com/yutannihilation/duckdb-ext-file-dialog) | ✅ Ongoing | 1 days ago | 14 | Rust | A DuckDB extension to choose file interactively us... |
| **flockmtl** | [dais-polymtl/flockmtl](https://github.com/dais-polymtl/flockmtl) | ✅ Ongoing | 1 days ago | 268 | C++ | FlockMTL: DuckDB extension for multimodal querying... |
| **magic** | [carlopi/duckdb_magic](https://github.com/carlopi/duckdb_magic) | ✅ Ongoing | 1 days ago | 7 | C++ | Auto-detect file types via `libmagic` (`file` util... |
| **nanoarrow** | [paleolimbot/duckdb-nanoarrow](https://github.com/paleolimbot/duckdb-nanoarrow) | ✅ Ongoing | 1 days ago | 44 | C++ | No description |
| **observefs** | [dentiny/duckdb-filesystem-observability](https://github.com/dentiny/duckdb-filesystem-observability) | ✅ Ongoing | 1 days ago | 0 | C++ | Provides observability for duckdb filesystem. |
| **rapidfuzz** | [query-farm/rapidfuzz](https://github.com/query-farm/rapidfuzz) | ✅ Ongoing | 1 days ago | 3 | C++ | No description |
| **rusty_quack** | [duckdb/extension-template-rs](https://github.com/duckdb/extension-template-rs) | ✅ Ongoing | 1 days ago | 79 | Rust | (Experimental) Template for Rust-based DuckDB exte... |
| **snowflake** | [iqea-ai/duckdb-snowflake](https://github.com/iqea-ai/duckdb-snowflake) | ✅ Ongoing | 1 days ago | 8 | C++ | A powerful DuckDB extension that enables seamless ... |
| **st_read_multi** | [yutannihilation/duckdb-ext-st-read-multi](https://github.com/yutannihilation/duckdb-ext-st-read-multi) | ✅ Ongoing | 1 days ago | 3 | Rust | A DuckDB extension to import multiple geospatial f... |
| **h3** | [isaacbrodsky/h3-duckdb](https://github.com/isaacbrodsky/h3-duckdb) | ✅ Ongoing | 2 days ago | 220 | C++ | Bindings for H3 to DuckDB |
| **lua** | [isaacbrodsky/duckdb-lua](https://github.com/isaacbrodsky/duckdb-lua) | ✅ Ongoing | 2 days ago | 3 | C++ | DuckDB extension to evaluate Lua expressions. |
| **mooncake** | [Mooncake-Labs/duckdb_mooncake](https://github.com/Mooncake-Labs/duckdb_mooncake) | ✅ Ongoing | 2 days ago | 0 | C++ | Read Iceberg tables written by moonlink in real ti... |
| **quack** | [duckdb/extension-template](https://github.com/duckdb/extension-template) | ✅ Ongoing | 2 days ago | 221 | Python | Template for DuckDB extensions to help you develop... |
| **splink_udfs** | [moj-analytical-services/splink_udfs](https://github.com/moj-analytical-services/splink_udfs) | ✅ Ongoing | 2 days ago | 8 | C++ | No description |
| **vortex** | [vortex-data/duckdb-vortex](https://github.com/vortex-data/duckdb-vortex) | ✅ Ongoing | 2 days ago | 24 | Shell | DuckDB extension allowing reading/writing of vorte... |
| **bitfilters** | [query-farm/bitfilters](https://github.com/query-farm/bitfilters) | ✅ Ongoing | 3 days ago | 2 | C++ | A high-performance DuckDB extension providing prob... |
| **cache_httpfs** | [dentiny/duck-read-cache-fs](https://github.com/dentiny/duck-read-cache-fs) | ✅ Ongoing | 3 days ago | 96 | C++ | This repository is made as read-only filesystem fo... |
| **shellfs** | [query-farm/shellfs](https://github.com/query-farm/shellfs) | ✅ Ongoing | 3 days ago | 79 | C++ | DuckDB extension allowing shell commands to be use... |
| **stochastic** | [query-farm/stochastic](https://github.com/query-farm/stochastic) | ✅ Ongoing | 3 days ago | 11 | C++ | A DuckDB extension that add comprehensive statisti... |
| **textplot** | [query-farm/textplot](https://github.com/query-farm/textplot) | ✅ Ongoing | 3 days ago | 9 | C++ | A DuckDB community extension that enables text-bas... |
| **yaml** | [teaguesterling/duckdb_yaml](https://github.com/teaguesterling/duckdb_yaml) | ✅ Ongoing | 7 days ago | 9 | C++ |  A DuckDB to read and work with YAML files in a si... |
| **eeagrid** | [ahuarte47/duckdb-eeagrid](https://github.com/ahuarte47/duckdb-eeagrid) | ✅ Ongoing | 8 days ago | 0 | C++ | Functions for transforming XY coordinates to and f... |
| **cronjob** | [quackscience/duckdb-extension-cronjob](https://github.com/quackscience/duckdb-extension-cronjob) | ✅ Ongoing | 9 days ago | 41 | C++ | DuckDB CronJob Extension |
| **gsheets** | [evidence-dev/duckdb_gsheets](https://github.com/evidence-dev/duckdb_gsheets) | ✅ Ongoing | 9 days ago | 297 | C++ | DuckDB extension to read and write Google Sheets u... |
| **faiss** | [duckdb-faiss-ext/duckdb-faiss-ext](https://github.com/duckdb-faiss-ext/duckdb-faiss-ext) | ✅ Ongoing | 10 days ago | 25 | Go | DuckDB wrapper for FAISS - Experimental |
| **chsql** | [quackscience/duckdb-extension-clickhouse-sql](https://github.com/quackscience/duckdb-extension-clickhouse-sql) | ✅ Ongoing | 27 days ago | 70 | C++ | DuckDB Community Extension implementing ClickHouse... |
| **geography** | [paleolimbot/duckdb-geography](https://github.com/paleolimbot/duckdb-geography) | ✅ Ongoing | 30 days ago | 32 | C++ | No description |
| **geotiff** | [babaknaimi/duckdb-geotiff](https://github.com/babaknaimi/duckdb-geotiff) | ✅ Ongoing | 30 days ago | 2 | C++ | Duckdb extension to read GeoTiffs directly with du... |
| **highs** | [fhk/highs-duckdb](https://github.com/fhk/highs-duckdb) | ✅ Ongoing | 34 days ago | 0 | C++ | Run the solver in the database! |
| **rusty_sheet** | [redraiment/rusty-sheet](https://github.com/redraiment/rusty-sheet) | ✅ Ongoing | 36 days ago | 16 | Rust | An Excel/OpenDocument Spreadsheets file reader for... |
| **httpserver** | [Query-farm/duckdb-extension-httpserver](https://github.com/Query-farm/duckdb-extension-httpserver) | ✅ Ongoing | 37 days ago | 228 | HTML | DuckDB HTTP API Server and Query Interface in a  C... |
| **webbed** | [teaguesterling/duckdb_webbed](https://github.com/teaguesterling/duckdb_webbed) | ✅ Ongoing | 37 days ago | 12 | C++ | No description |
| **read_stat** | [mettekou/duckdb-read-stat](https://github.com/mettekou/duckdb-read-stat) | ✅ Ongoing | 39 days ago | 22 | C | Read data sets from SAS, Stata, and SPSS from Duck... |
| **hashfuncs** | [query-farm/hashfuncs](https://github.com/query-farm/hashfuncs) | ✅ Ongoing | 43 days ago | 2 | C++ | A DuckDB extension that supplies non-cryptographic... |
| **hdf5** | [Berrysoft/duckdb-hdf5](https://github.com/Berrysoft/duckdb-hdf5) | ✅ Ongoing | 43 days ago | 9 | Rust | HDF5 plugin for duckdb |
| **marisa** | [query-farm/marisa](https://github.com/query-farm/marisa) | ✅ Ongoing | 43 days ago | 2 | C++ | The Marisa extension by Query.Farm integrates the ... |
| **http_client** | [quackscience/duckdb-extension-httpclient](https://github.com/quackscience/duckdb-extension-httpclient) | ✅ Ongoing | 52 days ago | 70 | C++ | DuckDB HTTP GET/POST Client in a Community Extensi... |
| **duckdb_mcp** | [teaguesterling/duckdb_mcp](https://github.com/teaguesterling/duckdb_mcp) | ✅ Ongoing | 54 days ago | 6 | C++ | A simple MCP server extension for DuckDB |
| **chsql_native** | [quackscience/duckdb-extension-clickhouse-native](https://github.com/quackscience/duckdb-extension-clickhouse-native) | ✅ Ongoing | 57 days ago | 16 | Rust | Experimental ClickHouse Native Client and Native f... |
| **duckpgq** | [cwida/duckpgq-extension](https://github.com/cwida/duckpgq-extension) | ✅ Ongoing | 59 days ago | 259 | C++ | DuckDB extension that adds support for SQL/PGQ and... |
| **datasketches** | [query-farm/datasketches](https://github.com/query-farm/datasketches) | ✅ Ongoing | 61 days ago | 25 | C++ | Integrates DuckDB with the high-performance Apache... |
| **duck_tails** | [teaguesterling/duck_tails](https://github.com/teaguesterling/duck_tails) | ✅ Ongoing | 61 days ago | 2 | C++ | A DuckDB extension for exploring and reading git h... |
| **lindel** | [query-farm/lindel](https://github.com/query-farm/lindel) | ✅ Ongoing | 62 days ago | 50 | C++ | DuckDB Extension Linearization/Delinearization, Z-... |
| **capi_quack** | [duckdb/extension-template-c](https://github.com/duckdb/extension-template-c) | ✅ Ongoing | 63 days ago | 17 | C | (Experimental) C/C++ template for DuckDB extension... |
| **markdown** | [teaguesterling/duckdb_markdown](https://github.com/teaguesterling/duckdb_markdown) | ✅ Ongoing | 70 days ago | 5 | C++ | Heirarchical markdown parsing for DuckDB |
| **jwt** | [GalvinGao/duckdb_jwt](https://github.com/GalvinGao/duckdb_jwt) | ✅ Ongoing | 72 days ago | 0 | C++ | No description |
| **parser_tools** | [zfarrell/duckdb_extension_parser_tools](https://github.com/zfarrell/duckdb_extension_parser_tools) | ✅ Ongoing | 72 days ago | 15 | C++ | Parse sql - with sql! |
| **quickjs** | [quackscience/duckdb-quickjs](https://github.com/quackscience/duckdb-quickjs) | ✅ Ongoing | 82 days ago | 8 | C++ | No description |
| **substrait** | [substrait-io/duckdb-substrait-extension](https://github.com/substrait-io/duckdb-substrait-extension) | ✅ Ongoing | 82 days ago | 48 | C++ | No description |
| **pbix** | [Hugoberry/duckdb-pbix-extension](https://github.com/Hugoberry/duckdb-pbix-extension) | ✅ Ongoing | 90 days ago | 27 | C++ | Duckdb extension for parsing the metadata and cont... |
| **redis** | [quackscience/duckdb-extension-redis](https://github.com/quackscience/duckdb-extension-redis) | ✅ Ongoing | 97 days ago | 7 | C++ | DuckDB Redis Client community extension |
| **radio** | [query-farm/radio](https://github.com/query-farm/radio) | ✅ Ongoing | 98 days ago | 30 | C++ | Radio is a DuckDB extension by Query.Farm that bri... |
| **tributary** | [query-farm/tributary](https://github.com/query-farm/tributary) | ✅ Ongoing | 98 days ago | 29 | C++ | A DuckDB Extension for Kafka |
| **crypto** | [query-farm/crypto](https://github.com/query-farm/crypto) | ✅ Ongoing | 101 days ago | 22 | Rust | DuckDB Extension for cryptographic hash functions ... |
| **evalexpr_rhai** | [query-farm/evalexpr_rhai](https://github.com/query-farm/evalexpr_rhai) | ✅ Ongoing | 101 days ago | 21 | C++ | A DuckDB extension to evaluate the Rhai scripting ... |
| **fuzzycomplete** | [query-farm/fuzzycomplete](https://github.com/query-farm/fuzzycomplete) | ✅ Ongoing | 101 days ago | 21 | C++ | DuckDB Extension for fuzzy string matching based a... |
| **pcap_reader** | [quackscience/duckdb-extension-pcap](https://github.com/quackscience/duckdb-extension-pcap) | ✅ Ongoing | 101 days ago | 10 | Rust | DuckDB PCAP Reader Extension made in Rust |
| **pyroscope** | [quackscience/duckdb-extension-pyroscope](https://github.com/quackscience/duckdb-extension-pyroscope) | ✅ Ongoing | 101 days ago | 19 | Rust | DuckDB Pyroscope Extension for Continuous Profilin... |
| **netquack** | [hatamiarash7/duckdb-netquack](https://github.com/hatamiarash7/duckdb-netquack) | ✅ Ongoing | 104 days ago | 17 | C++ | DuckDB extension for parsing, extracting, and anal... |
| **quackformers** | [martin-conur/quackformers](https://github.com/martin-conur/quackformers) | ✅ Ongoing | 110 days ago | 6 | Rust | DuckDB NLP extension. |
| **arrow** | [duckdb/duckdb-extension-alias](https://github.com/duckdb/duckdb-extension-alias) | ✅ Ongoing | 133 days ago | 4 | C | No description |
| **msolap** | [Hugoberry/duckdb-msolap-extension](https://github.com/Hugoberry/duckdb-msolap-extension) | ✅ Ongoing | 134 days ago | 8 | C++ | No description |
| **ofquack** | [krokozyab/ofquack](https://github.com/krokozyab/ofquack) | ✅ Ongoing | 149 days ago | 5 | C++ | Oracle Fusion DuckDB extension  |
| **scrooge** | [pdet/Scrooge-McDuck](https://github.com/pdet/Scrooge-McDuck) | ✅ Ongoing | 158 days ago | 149 | C++ | No description |
| **wireduck** | [hyehudai/wireduck](https://github.com/hyehudai/wireduck) | ✅ Ongoing | 159 days ago | 45 | C++ | Duckdb extension to read pcap files |
| **psql** | [ywelsch/duckdb-psql](https://github.com/ywelsch/duckdb-psql) | ✅ Ongoing | 165 days ago | 92 | C++ | A piped SQL for DuckDB |
| **blockduck** | [luohaha/BlockDuck](https://github.com/luohaha/BlockDuck) | ✅ Ongoing | 176 days ago | 8 | C++ | Live SQL Queries on Blockchain |
| **prql** | [ywelsch/duckdb-prql](https://github.com/ywelsch/duckdb-prql) | ✅ Ongoing | 185 days ago | 297 | C++ | PRQL as a DuckDB extension |
| **hostfs** | [gropaul/hostFS](https://github.com/gropaul/hostFS) | ✅ Ongoing | 192 days ago | 23 | C++ | No description |
| **open_prompt** | [quackscience/duckdb-extension-openprompt](https://github.com/quackscience/duckdb-extension-openprompt) | ✅ Ongoing | 253 days ago | 50 | C++ | DuckDB Community Extension to prompt LLMs from SQL |
| **webmacro** | [quackscience/duckdb-extension-webmacro](https://github.com/quackscience/duckdb-extension-webmacro) | ✅ Ongoing | 277 days ago | 13 | C++ | DuckDB WebMacro: Share and Load your SQL Macros vi... |
| **tsid** | [quackscience/duckdb-extension-tsid](https://github.com/quackscience/duckdb-extension-tsid) | ✅ Ongoing | 283 days ago | 5 | C++ | TSID Extension for DuckDB  |
| **sheetreader** | [polydbms/sheetreader-duckdb](https://github.com/polydbms/sheetreader-duckdb) | ✅ Ongoing | 338 days ago | 55 | Jupyter Notebook | No description |
| **pivot_table** | [Alex-Monahan/pivot_table](https://github.com/Alex-Monahan/pivot_table) | ✅ Ongoing | 361 days ago | 15 | C++ | Full spreadsheet-style pivot table through SQL mac... |
| **tarfs** | [Maxxen/duckdb_tarfs](https://github.com/Maxxen/duckdb_tarfs) | ✅ Ongoing | 389 days ago | 10 | C++ | No description |
| **ulid** | [Maxxen/duckdb_ulid](https://github.com/Maxxen/duckdb_ulid) | ✅ Ongoing | 437 days ago | 24 | C++ | No description |

### Community Extensions Summary
- **Total Extensions**: 80
- **Active Extensions**: 80 (100.0%)
- **Discontinued Extensions**: 0 (0.0%)
- **Extensions with Issues**: 0 (0.0%)

## Methodology

- **Core Extensions**: Information gathered from the official DuckDB documentation
- **Community Extensions**: Information gathered from the `duckdb/community-extensions` repository and individual extension repositories
- **Status Determination**:
  - ✅ **Ongoing**: Repository is active and not archived
  - 🔴 **Discontinued**: Repository is archived or marked as discontinued
  - ❌ **No Repo/Error**: Repository information unavailable or inaccessible
- **Activity Metrics**: Based on the last push/commit date to the repository
- **Caching**: API responses are cached to improve performance and reduce rate limiting

Report generated using the [duckdb-extensions-analysis](https://github.com/Mjboothaus/duckdb-extensions-analysis) tool.