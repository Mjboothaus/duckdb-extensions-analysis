# DuckDB Extensions Status Report

Generated on: **2025-09-19 14:32:33 UTC**

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
| **mooncake** | [Mooncake-Labs/duckdb_mooncake](https://github.com/Mooncake-Labs/duckdb_mooncake) | ✅ Ongoing | 0 days ago | 0 | C++ | Read Iceberg tables written by moonlink in real ti... |
| **nanodbc** | [Hugoberry/duckdb-nanodbc-extension](https://github.com/Hugoberry/duckdb-nanodbc-extension) | ✅ Ongoing | 0 days ago | 34 | C++ | Database connectivity extension by Hugoberry |
| **observefs** | [dentiny/duckdb-filesystem-observability](https://github.com/dentiny/duckdb-filesystem-observability) | ✅ Ongoing | 0 days ago | 0 | C++ | Provides observability for duckdb filesystem. |
| **snowflake** | [iqea-ai/duckdb-snowflake](https://github.com/iqea-ai/duckdb-snowflake) | ✅ Ongoing | 0 days ago | 8 | C++ | A powerful DuckDB extension that enables seamless ... |
| **zipfs** | [isaacbrodsky/duckdb-zipfs](https://github.com/isaacbrodsky/duckdb-zipfs) | ✅ Ongoing | 0 days ago | 41 | C++ | DuckDB extension to read files within zip archives... |
| **airport** | [Query-farm/airport](https://github.com/Query-farm/airport) | ✅ Ongoing | 1 days ago | 297 | C++ | The Airport extension for DuckDB, enables the use ... |
| **bigquery** | [hafenkran/duckdb-bigquery](https://github.com/hafenkran/duckdb-bigquery) | ✅ Ongoing | 1 days ago | 130 | C++ | Integrates DuckDB with Google BigQuery, allowing d... |
| **file_dialog** | [yutannihilation/duckdb-ext-file-dialog](https://github.com/yutannihilation/duckdb-ext-file-dialog) | ✅ Ongoing | 1 days ago | 14 | Rust | A DuckDB extension to choose file interactively us... |
| **flockmtl** | [dais-polymtl/flock](https://github.com/dais-polymtl/flock) | ✅ Ongoing | 1 days ago | 268 | C++ | FlockMTL: DuckDB extension for multimodal querying... |
| **magic** | [carlopi/duckdb_magic](https://github.com/carlopi/duckdb_magic) | ✅ Ongoing | 1 days ago | 7 | C++ | Auto-detect file types via `libmagic` (`file` util... |
| **nanoarrow** | [paleolimbot/duckdb-nanoarrow](https://github.com/paleolimbot/duckdb-nanoarrow) | ✅ Ongoing | 1 days ago | 44 | C++ | DuckDB extension: nanoarrow by paleolimbot |
| **rapidfuzz** | [Query-farm/rapidfuzz](https://github.com/Query-farm/rapidfuzz) | ✅ Ongoing | 1 days ago | 3 | C++ | DuckDB extension: rapidfuzz |
| **rusty_quack** | [duckdb/extension-template-rs](https://github.com/duckdb/extension-template-rs) | ✅ Ongoing | 1 days ago | 79 | Rust | (Experimental) Template for Rust-based DuckDB exte... |
| **st_read_multi** | [yutannihilation/duckdb-ext-st-read-multi](https://github.com/yutannihilation/duckdb-ext-st-read-multi) | ✅ Ongoing | 1 days ago | 3 | Rust | A DuckDB extension to import multiple geospatial f... |
| **h3** | [isaacbrodsky/h3-duckdb](https://github.com/isaacbrodsky/h3-duckdb) | ✅ Ongoing | 2 days ago | 220 | C++ | Bindings for H3 to DuckDB |
| **lua** | [isaacbrodsky/duckdb-lua](https://github.com/isaacbrodsky/duckdb-lua) | ✅ Ongoing | 2 days ago | 3 | C++ | DuckDB extension to evaluate Lua expressions. |
| **quack** | [duckdb/extension-template](https://github.com/duckdb/extension-template) | ✅ Ongoing | 2 days ago | 221 | Python | Template for DuckDB extensions to help you develop... |
| **vortex** | [vortex-data/duckdb-vortex](https://github.com/vortex-data/duckdb-vortex) | ✅ Ongoing | 2 days ago | 24 | Shell | DuckDB extension allowing reading/writing of vorte... |
| **bitfilters** | [Query-farm/bitfilters](https://github.com/Query-farm/bitfilters) | ✅ Ongoing | 3 days ago | 2 | C++ | A high-performance DuckDB extension providing prob... |
| **cache_httpfs** | [dentiny/duck-read-cache-fs](https://github.com/dentiny/duck-read-cache-fs) | ✅ Ongoing | 3 days ago | 96 | C++ | This repository is made as read-only filesystem fo... |
| **splink_udfs** | [moj-analytical-services/splink_udfs](https://github.com/moj-analytical-services/splink_udfs) | ✅ Ongoing | 3 days ago | 8 | C++ | DuckDB extension: splink_udfs by moj-analytical-se... |
| **stochastic** | [Query-farm/stochastic](https://github.com/Query-farm/stochastic) | ✅ Ongoing | 3 days ago | 11 | C++ | A DuckDB extension that add comprehensive statisti... |
| **textplot** | [Query-farm/textplot](https://github.com/Query-farm/textplot) | ✅ Ongoing | 3 days ago | 9 | C++ | A DuckDB community extension that enables text-bas... |
| **shellfs** | [Query-farm/shellfs](https://github.com/Query-farm/shellfs) | ✅ Ongoing | 4 days ago | 79 | C++ | DuckDB extension allowing shell commands to be use... |
| **yaml** | [teaguesterling/duckdb_yaml](https://github.com/teaguesterling/duckdb_yaml) | ✅ Ongoing | 7 days ago | 9 | C++ |  A DuckDB to read and work with YAML files in a si... |
| **eeagrid** | [ahuarte47/duckdb-eeagrid](https://github.com/ahuarte47/duckdb-eeagrid) | ✅ Ongoing | 8 days ago | 0 | C++ | Functions for transforming XY coordinates to and f... |
| **gsheets** | [evidence-dev/duckdb_gsheets](https://github.com/evidence-dev/duckdb_gsheets) | ✅ Ongoing | 9 days ago | 297 | C++ | DuckDB extension to read and write Google Sheets u... |
| **cronjob** | [Query-farm/duckdb-extension-cronjob](https://github.com/Query-farm/duckdb-extension-cronjob) | ✅ Ongoing | 10 days ago | 41 | C++ | DuckDB CronJob Extension |
| **faiss** | [duckdb-faiss-ext/duckdb-faiss-ext](https://github.com/duckdb-faiss-ext/duckdb-faiss-ext) | ✅ Ongoing | 11 days ago | 25 | Go | DuckDB wrapper for FAISS - Experimental |
| **chsql** | [Query-farm/duckdb-extension-clickhouse-sql](https://github.com/Query-farm/duckdb-extension-clickhouse-sql) | ✅ Ongoing | 27 days ago | 70 | C++ | DuckDB Community Extension implementing ClickHouse... |
| **geotiff** | [babaknaimi/duckdb-geotiff](https://github.com/babaknaimi/duckdb-geotiff) | ✅ Ongoing | 30 days ago | 2 | C++ | Duckdb extension to read GeoTiffs directly with du... |
| **geography** | [paleolimbot/duckdb-geography](https://github.com/paleolimbot/duckdb-geography) | ✅ Ongoing | 31 days ago | 32 | C++ | Geospatial data extension by paleolimbot |
| **highs** | [fhk/HiGHS-duckdb](https://github.com/fhk/HiGHS-duckdb) | ✅ Ongoing | 34 days ago | 0 | C++ | Run the solver in the database! |
| **rusty_sheet** | [redraiment/rusty-sheet](https://github.com/redraiment/rusty-sheet) | ✅ Ongoing | 36 days ago | 16 | Rust | An Excel/OpenDocument Spreadsheets file reader for... |
| **httpserver** | [Query-farm/duckdb-extension-httpserver](https://github.com/Query-farm/duckdb-extension-httpserver) | ✅ Ongoing | 37 days ago | 229 | HTML | DuckDB HTTP API Server and Query Interface in a  C... |
| **webbed** | [teaguesterling/duckdb_webbed](https://github.com/teaguesterling/duckdb_webbed) | ✅ Ongoing | 37 days ago | 12 | C++ | Web/HTTP functionality extension by teaguesterling |
| **read_stat** | [mettekou/duckdb-read-stat](https://github.com/mettekou/duckdb-read-stat) | ✅ Ongoing | 39 days ago | 22 | C | Read data sets from SAS, Stata, and SPSS from Duck... |
| **hashfuncs** | [Query-farm/hashfuncs](https://github.com/Query-farm/hashfuncs) | ✅ Ongoing | 43 days ago | 2 | C++ | A DuckDB extension that supplies non-cryptographic... |
| **hdf5** | [Berrysoft/duckdb-hdf5](https://github.com/Berrysoft/duckdb-hdf5) | ✅ Ongoing | 43 days ago | 9 | Rust | HDF5 plugin for duckdb |
| **marisa** | [Query-farm/marisa](https://github.com/Query-farm/marisa) | ✅ Ongoing | 43 days ago | 2 | C++ | The Marisa extension by Query.Farm integrates the ... |
| **http_client** | [Query-farm/duckdb-extension-httpclient](https://github.com/Query-farm/duckdb-extension-httpclient) | ✅ Ongoing | 52 days ago | 70 | C++ | DuckDB HTTP GET/POST Client in a Community Extensi... |
| **duckdb_mcp** | [teaguesterling/duckdb_mcp](https://github.com/teaguesterling/duckdb_mcp) | ✅ Ongoing | 54 days ago | 6 | C++ | A simple MCP server extension for DuckDB |
| **chsql_native** | [Query-farm/duckdb-extension-clickhouse-native](https://github.com/Query-farm/duckdb-extension-clickhouse-native) | ✅ Ongoing | 58 days ago | 16 | Rust | Experimental ClickHouse Native Client and Native f... |
| **duckpgq** | [cwida/duckpgq-extension](https://github.com/cwida/duckpgq-extension) | ✅ Ongoing | 59 days ago | 260 | C++ | DuckDB extension that adds support for SQL/PGQ and... |
| **duck_tails** | [teaguesterling/duck_tails](https://github.com/teaguesterling/duck_tails) | ✅ Ongoing | 61 days ago | 2 | C++ | A DuckDB extension for exploring and reading git h... |
| **datasketches** | [Query-farm/datasketches](https://github.com/Query-farm/datasketches) | ✅ Ongoing | 62 days ago | 25 | C++ | Integrates DuckDB with the high-performance Apache... |
| **lindel** | [Query-farm/lindel](https://github.com/Query-farm/lindel) | ✅ Ongoing | 62 days ago | 50 | C++ | DuckDB Extension Linearization/Delinearization, Z-... |
| **capi_quack** | [duckdb/extension-template-c](https://github.com/duckdb/extension-template-c) | ✅ Ongoing | 63 days ago | 17 | C | (Experimental) C/C++ template for DuckDB extension... |
| **markdown** | [teaguesterling/duckdb_markdown](https://github.com/teaguesterling/duckdb_markdown) | ✅ Ongoing | 70 days ago | 5 | C++ | Heirarchical markdown parsing for DuckDB |
| **jwt** | [GalvinGao/duckdb_jwt](https://github.com/GalvinGao/duckdb_jwt) | ✅ Ongoing | 72 days ago | 0 | C++ | DuckDB extension: jwt by GalvinGao |
| **parser_tools** | [zfarrell/duckdb_extension_parser_tools](https://github.com/zfarrell/duckdb_extension_parser_tools) | ✅ Ongoing | 72 days ago | 15 | C++ | Parse sql - with sql! |
| **substrait** | [substrait-io/duckdb-substrait-extension](https://github.com/substrait-io/duckdb-substrait-extension) | ✅ Ongoing | 82 days ago | 48 | C++ | DuckDB extension: substrait by substrait-io |
| **quickjs** | [Query-farm/duckdb-quickjs](https://github.com/Query-farm/duckdb-quickjs) | ✅ Ongoing | 83 days ago | 8 | C++ | DuckDB extension: quickjs by quackscience |
| **pbix** | [Hugoberry/duckdb-pbix-extension](https://github.com/Hugoberry/duckdb-pbix-extension) | ✅ Ongoing | 90 days ago | 27 | C++ | Duckdb extension for parsing the metadata and cont... |
| **radio** | [Query-farm/radio](https://github.com/Query-farm/radio) | ✅ Ongoing | 98 days ago | 30 | C++ | Radio is a DuckDB extension by Query.Farm that bri... |
| **redis** | [Query-farm/duckdb-extension-redis](https://github.com/Query-farm/duckdb-extension-redis) | ✅ Ongoing | 98 days ago | 7 | C++ | DuckDB Redis Client community extension |
| **tributary** | [Query-farm/tributary](https://github.com/Query-farm/tributary) | ✅ Ongoing | 98 days ago | 29 | C++ | A DuckDB Extension for Kafka |
| **crypto** | [Query-farm/crypto](https://github.com/Query-farm/crypto) | ✅ Ongoing | 101 days ago | 22 | Rust | DuckDB Extension for cryptographic hash functions ... |
| **evalexpr_rhai** | [Query-farm/evalexpr_rhai](https://github.com/Query-farm/evalexpr_rhai) | ✅ Ongoing | 101 days ago | 21 | C++ | A DuckDB extension to evaluate the Rhai scripting ... |
| **fuzzycomplete** | [Query-farm/fuzzycomplete](https://github.com/Query-farm/fuzzycomplete) | ✅ Ongoing | 101 days ago | 21 | C++ | DuckDB Extension for fuzzy string matching based a... |
| **pcap_reader** | [Query-farm/duckdb-extension-pcap](https://github.com/Query-farm/duckdb-extension-pcap) | ✅ Ongoing | 101 days ago | 10 | Rust | DuckDB PCAP Reader Extension made in Rust |
| **pyroscope** | [Query-farm/duckdb-extension-pyroscope](https://github.com/Query-farm/duckdb-extension-pyroscope) | ✅ Ongoing | 101 days ago | 19 | Rust | DuckDB Pyroscope Extension for Continuous Profilin... |
| **netquack** | [hatamiarash7/duckdb-netquack](https://github.com/hatamiarash7/duckdb-netquack) | ✅ Ongoing | 105 days ago | 17 | C++ | DuckDB extension for parsing, extracting, and anal... |
| **quackformers** | [martin-conur/quackformers](https://github.com/martin-conur/quackformers) | ✅ Ongoing | 110 days ago | 6 | Rust | DuckDB NLP extension. |
| **arrow** | [duckdb/duckdb-extension-alias](https://github.com/duckdb/duckdb-extension-alias) | ✅ Ongoing | 133 days ago | 4 | C | DuckDB extension: arrow |
| **msolap** | [Hugoberry/duckdb-msolap-extension](https://github.com/Hugoberry/duckdb-msolap-extension) | ✅ Ongoing | 134 days ago | 8 | C++ | DuckDB extension: msolap by Hugoberry |
| **ofquack** | [krokozyab/ofquack](https://github.com/krokozyab/ofquack) | ✅ Ongoing | 150 days ago | 5 | C++ | Oracle Fusion DuckDB extension  |
| **scrooge** | [pdet/Scrooge-McDuck](https://github.com/pdet/Scrooge-McDuck) | ✅ Ongoing | 158 days ago | 149 | C++ | DuckDB extension: scrooge by pdet |
| **wireduck** | [hyehudai/wireduck](https://github.com/hyehudai/wireduck) | ✅ Ongoing | 160 days ago | 45 | C++ | Duckdb extension to read pcap files |
| **psql** | [ywelsch/duckdb-psql](https://github.com/ywelsch/duckdb-psql) | ✅ Ongoing | 165 days ago | 92 | C++ | A piped SQL for DuckDB |
| **blockduck** | [luohaha/BlockDuck](https://github.com/luohaha/BlockDuck) | ✅ Ongoing | 176 days ago | 8 | C++ | Live SQL Queries on Blockchain |
| **prql** | [ywelsch/duckdb-prql](https://github.com/ywelsch/duckdb-prql) | ✅ Ongoing | 186 days ago | 297 | C++ | PRQL as a DuckDB extension |
| **hostfs** | [gropaul/hostFS](https://github.com/gropaul/hostFS) | ✅ Ongoing | 192 days ago | 23 | C++ | DuckDB extension: hostfs by gropaul |
| **open_prompt** | [Query-farm/duckdb-extension-openprompt](https://github.com/Query-farm/duckdb-extension-openprompt) | ✅ Ongoing | 253 days ago | 50 | C++ | DuckDB Community Extension to prompt LLMs from SQL |
| **webmacro** | [Query-farm/duckdb-extension-webmacro](https://github.com/Query-farm/duckdb-extension-webmacro) | ✅ Ongoing | 278 days ago | 13 | C++ | DuckDB WebMacro: Share and Load your SQL Macros vi... |
| **tsid** | [Query-farm/duckdb-extension-tsid](https://github.com/Query-farm/duckdb-extension-tsid) | ✅ Ongoing | 283 days ago | 5 | C++ | TSID Extension for DuckDB  |
| **sheetreader** | [polydbms/sheetreader-duckdb](https://github.com/polydbms/sheetreader-duckdb) | ✅ Ongoing | 338 days ago | 55 | Jupyter Notebook | DuckDB extension: sheetreader by polydbms |
| **pivot_table** | [Alex-Monahan/pivot_table](https://github.com/Alex-Monahan/pivot_table) | ✅ Ongoing | 361 days ago | 15 | C++ | Full spreadsheet-style pivot table through SQL mac... |
| **tarfs** | [Maxxen/duckdb_tarfs](https://github.com/Maxxen/duckdb_tarfs) | ✅ Ongoing | 389 days ago | 10 | C++ | DuckDB extension: tarfs by Maxxen |
| **ulid** | [Maxxen/duckdb_ulid](https://github.com/Maxxen/duckdb_ulid) | ✅ Ongoing | 437 days ago | 24 | C++ | DuckDB extension: ulid by Maxxen |

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