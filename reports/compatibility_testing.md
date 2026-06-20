# DuckDB extension compatibility testing (experimental)
This report summarises *on-demand* compatibility checks that attempt to `INSTALL` and `LOAD` extensions across a small set of DuckDB versions.

Back to the main extensions report: [DuckDB Extensions Analysis](https://mjboothaus.github.io/duckdb-extensions-analysis/) ([Markdown](https://github.com/Mjboothaus/duckdb-extensions-analysis/blob/main/reports/latest.md)).

*Note:* This is an early implementation. Results are best-effort and may be incomplete if the run hit a time limit.

---
## Test scope
- **DuckDB versions tested:** 1.3.2, 1.4.5, 1.5.4
- **Extensions attempted:** 39
- **Pairs attempted (extension × version):** 117
- **Pairs completed:** 117
- **Results recorded:** 117
- **Per-test timeout:** 120 seconds
- **Max runtime:** 600 seconds
- **Actual runtime:** 250 seconds

## Results (summary)

||| Status | Count |
|||--------|------:|
||| ✅ Compatible (install+load) | 79 |
||| ❌ Failed | 38 |
||| ⏱️ Timed out | 0 |
||| ⏱️ Skipped (time limit) | 0 |

## Results (details)

||| Extension | DuckDB version | Status | Seconds | Notes |
|||----------|----------------|--------|--------:|-------|
|||| autocomplete | 1.3.2 | ✅ | 2.4 |  |
|||| avro | 1.3.2 | ✅ | 1.9 |  |
|||| aws | 1.3.2 | ✅ | 1.8 |  |
|||| azure | 1.3.2 | ✅ | 1.9 |  |
|||| delta | 1.3.2 | ✅ | 2.2 |  |
|||| ducklake | 1.3.2 | ✅ | 2.1 |  |
|||| encodings | 1.3.2 | ✅ | 3.9 |  |
|||| excel | 1.3.2 | ✅ | 1.9 |  |
|||| fts | 1.3.2 | ✅ | 1.8 |  |
|||| httpfs | 1.3.2 | ✅ | 2.0 |  |
|||| iceberg | 1.3.2 | ✅ | 2.0 |  |
|||| icu | 1.3.2 | ✅ | 2.1 |  |
|||| inet | 1.3.2 | ✅ | 2.0 |  |
|||| json | 1.3.2 | ✅ | 2.0 |  |
|||| lance | 1.3.2 | ❌ | 1.8 | HTTP Error: Failed to download extension "lance" at URL "http://extensions.duckdb.org/v1.3.2/linux_amd64/lance.duckdb_extension.gz" (HTTP 404)

Candidate extensions: "autocomplete", "excel", "azure", "sqlite", "sqlite3"
For more info, visit https://duckdb.org/docs/stable/extensions/troubleshooting/?version=v1.3.2&platform=linux_amd64&extension=lance |
|||| motherduck | 1.3.2 | ✅ | 2.5 |  |
|||| mysql | 1.3.2 | ✅ | 2.0 |  |
|||| odbc | 1.3.2 | ❌ | 1.8 | HTTP Error: Failed to download extension "odbc" at URL "http://extensions.duckdb.org/v1.3.2/linux_amd64/odbc.duckdb_extension.gz" (HTTP 404)

Candidate extensions: "md", "ducklake", "encodings", "autocomplete", "postgres_scanner"
For more info, visit https://duckdb.org/docs/stable/extensions/troubleshooting/?version=v1.3.2&platform=linux_amd64&extension=odbc |
|||| parquet | 1.3.2 | ✅ | 1.9 |  |
|||| postgres | 1.3.2 | ✅ | 2.0 |  |
|||| quack | 1.3.2 | ❌ | 1.8 | HTTP Error: Failed to download extension "quack" at URL "http://extensions.duckdb.org/v1.3.2/linux_amd64/quack.duckdb_extension.gz" (HTTP 404)

Candidate extensions: "ducklake", "ui", "mysql_scanner", "sqlite_scanner", "icu"
For more info, visit https://duckdb.org/docs/stable/extensions/troubleshooting/?version=v1.3.2&platform=linux_amd64&extension=quack |
|||| spatial | 1.3.2 | ✅ | 2.3 |  |
|||| sqlite | 1.3.2 | ✅ | 2.1 |  |
|||| tpcds | 1.3.2 | ✅ | 2.0 |  |
|||| tpch | 1.3.2 | ✅ | 2.1 |  |
|||| unity_catalog | 1.3.2 | ❌ | 1.8 | HTTP Error: Failed to download extension "unity_catalog" at URL "http://extensions.duckdb.org/v1.3.2/linux_amd64/unity_catalog.duckdb_extension.gz" (HTTP 404)

Candidate extensions: "ui", "spatial", "icu", "sqlite_scanner", "tpch"
For more info, visit https://duckdb.org/docs/stable/extensions/troubleshooting/?version=v1.3.2&platform=linux_amd64&extension=unity_catalog |
|||| ui | 1.3.2 | ✅ | 2.1 |  |
|||| vortex | 1.3.2 | ❌ | 1.8 | HTTP Error: Failed to download extension "vortex" at URL "http://extensions.duckdb.org/v1.3.2/linux_amd64/vortex.duckdb_extension.gz" (HTTP 404)

Candidate extensions: "postgres", "motherduck", "azure", "core_functions", "sqlite"
For more info, visit https://duckdb.org/docs/stable/extensions/troubleshooting/?version=v1.3.2&platform=linux_amd64&extension=vortex |
|||| vss | 1.3.2 | ✅ | 2.1 |  |
|||| bigquery | 1.3.2 | ❌ | 2.2 | HTTP Error: Failed to download extension "bigquery" at URL "http://extensions.duckdb.org/v1.3.2/linux_amd64/bigquery.duckdb_extension.gz" (HTTP 404)

Candidate extensions: "icu", "iceberg", "parquet", "inet", "azure"
For more info, visit https://duckdb.org/docs/stable/extensions/troubleshooting/?version=v1.3.2&platform=linux_amd64&extension=bigquery |
|||| cityjson | 1.3.2 | ❌ | 1.8 | HTTP Error: Failed to download extension "cityjson" at URL "http://extensions.duckdb.org/v1.3.2/linux_amd64/cityjson.duckdb_extension.gz" (HTTP 404)

Candidate extensions: "fts", "inet", "encodings", "mysql", "https"
For more info, visit https://duckdb.org/docs/stable/extensions/troubleshooting/?version=v1.3.2&platform=linux_amd64&extension=cityjson |
|||| delta_classic | 1.3.2 | ❌ | 1.8 | HTTP Error: Failed to download extension "delta_classic" at URL "http://extensions.duckdb.org/v1.3.2/linux_amd64/delta_classic.duckdb_extension.gz" (HTTP 404)

Candidate extensions: "delta", "tpcds", "core_functions", "tpch", "inet"
For more info, visit https://duckdb.org/docs/stable/extensions/troubleshooting/?version=v1.3.2&platform=linux_amd64&extension=delta_classic |
|||| duck_hunt | 1.3.2 | ❌ | 1.8 | HTTP Error: Failed to download extension "duck_hunt" at URL "http://extensions.duckdb.org/v1.3.2/linux_amd64/duck_hunt.duckdb_extension.gz" (HTTP 404)

Candidate extensions: "ducklake", "tpch", "core_functions", "ui", "md"
For more info, visit https://duckdb.org/docs/stable/extensions/troubleshooting/?version=v1.3.2&platform=linux_amd64&extension=duck_hunt |
|||| duckdb_delta_sharing | 1.3.2 | ❌ | 1.8 | HTTP Error: Failed to download extension "duckdb_delta_sharing" at URL "http://extensions.duckdb.org/v1.3.2/linux_amd64/duckdb_delta_sharing.duckdb_extension.gz" (HTTP 404)

Candidate extensions: "delta", "ducklake", "sqlite_scanner", "mysql_scanner", "inet"
For more info, visit https://duckdb.org/docs/stable/extensions/troubleshooting/?version=v1.3.2&platform=linux_amd64&extension=duckdb_delta_sharing |
|||| duckton | 1.3.2 | ❌ | 1.8 | HTTP Error: Failed to download extension "duckton" at URL "http://extensions.duckdb.org/v1.3.2/linux_amd64/duckton.duckdb_extension.gz" (HTTP 404)

Candidate extensions: "ducklake", "encodings", "delta", "core_functions", "autocomplete"
For more info, visit https://duckdb.org/docs/stable/extensions/troubleshooting/?version=v1.3.2&platform=linux_amd64&extension=duckton |
|||| finetype | 1.3.2 | ❌ | 1.8 | HTTP Error: Failed to download extension "finetype" at URL "http://extensions.duckdb.org/v1.3.2/linux_amd64/finetype.duckdb_extension.gz" (HTTP 404)

Candidate extensions: "inet", "fts", "iceberg", "http", "https"
For more info, visit https://duckdb.org/docs/stable/extensions/troubleshooting/?version=v1.3.2&platform=linux_amd64&extension=finetype |
|||| gcs | 1.3.2 | ❌ | 1.8 | HTTP Error: Failed to download extension "gcs" at URL "http://extensions.duckdb.org/v1.3.2/linux_amd64/gcs.duckdb_extension.gz" (HTTP 404)

Candidate extensions: "icu", "fts", "vss", "aws", "tpch"
For more info, visit https://duckdb.org/docs/stable/extensions/troubleshooting/?version=v1.3.2&platform=linux_amd64&extension=gcs |
|||| gdx | 1.3.2 | ❌ | 1.8 | HTTP Error: Failed to download extension "gdx" at URL "http://extensions.duckdb.org/v1.3.2/linux_amd64/gdx.duckdb_extension.gz" (HTTP 404)

Candidate extensions: "md", "excel", "delta"
For more info, visit https://duckdb.org/docs/stable/extensions/troubleshooting/?version=v1.3.2&platform=linux_amd64&extension=gdx |
|||| laterite_ags4 | 1.3.2 | ❌ | 1.8 | HTTP Error: Failed to download extension "laterite_ags4" at URL "http://extensions.duckdb.org/v1.3.2/linux_amd64/laterite_ags4.duckdb_extension.gz" (HTTP 404)

Candidate extensions: "spatial", "postgres_scanner", "delta", "sqlite_scanner", "encodings"
For more info, visit https://duckdb.org/docs/stable/extensions/troubleshooting/?version=v1.3.2&platform=linux_amd64&extension=laterite_ags4 |
|||| autocomplete | 1.4.5 | ✅ | 2.2 |  |
|||| avro | 1.4.5 | ✅ | 2.0 |  |
|||| aws | 1.4.5 | ✅ | 2.1 |  |
|||| azure | 1.4.5 | ✅ | 2.1 |  |
|||| delta | 1.4.5 | ✅ | 2.6 |  |
|||| ducklake | 1.4.5 | ✅ | 2.2 |  |
|||| encodings | 1.4.5 | ✅ | 4.5 |  |
|||| excel | 1.4.5 | ✅ | 2.1 |  |
|||| fts | 1.4.5 | ✅ | 2.1 |  |
|||| httpfs | 1.4.5 | ✅ | 2.0 |  |
|||| iceberg | 1.4.5 | ✅ | 2.3 |  |
|||| icu | 1.4.5 | ✅ | 2.1 |  |
|||| inet | 1.4.5 | ✅ | 2.1 |  |
|||| json | 1.4.5 | ✅ | 2.2 |  |
|||| lance | 1.4.5 | ✅ | 6.0 |  |
|||| motherduck | 1.4.5 | ❌ | 2.0 | Invalid Input Error: Initialization function "motherduck_duckdb_cpp_init" from file "/home/runner/.duckdb/extensions/v1.4.5/linux_amd64/motherduck.duckdb_extension" threw an exception: "
Your DuckDB version (v1.4.5) is not supported by MotherDuck. Please upgrade your DuckDB to v1.5.3.

See https://motherduck.com/docs/getting-started/connect-query-from-duckdb-cli for more information." |
|||| mysql | 1.4.5 | ✅ | 2.4 |  |
|||| odbc | 1.4.5 | ❌ | 1.9 | HTTP Error: Failed to download extension "odbc" at URL "http://extensions.duckdb.org/v1.4.5/linux_amd64/odbc.duckdb_extension.gz" (HTTP 404)

Candidate extensions: "md", "ducklake", "encodings", "autocomplete", "postgres_scanner"
For more info, visit https://duckdb.org/docs/stable/extensions/troubleshooting?version=v1.4.5&platform=linux_amd64&extension=odbc |
|||| parquet | 1.4.5 | ✅ | 2.0 |  |
|||| postgres | 1.4.5 | ✅ | 2.3 |  |
|||| quack | 1.4.5 | ✅ | 2.5 |  |
|||| spatial | 1.4.5 | ✅ | 2.7 |  |
|||| sqlite | 1.4.5 | ✅ | 2.4 |  |
|||| tpcds | 1.4.5 | ✅ | 2.1 |  |
|||| tpch | 1.4.5 | ✅ | 2.1 |  |
|||| unity_catalog | 1.4.5 | ✅ | 2.2 |  |
|||| ui | 1.4.5 | ✅ | 2.4 |  |
|||| vortex | 1.4.5 | ✅ | 3.2 |  |
|||| vss | 1.4.5 | ✅ | 2.3 |  |
|||| bigquery | 1.4.5 | ❌ | 1.9 | HTTP Error: Failed to download extension "bigquery" at URL "http://extensions.duckdb.org/v1.4.5/linux_amd64/bigquery.duckdb_extension.gz" (HTTP 404)

Candidate extensions: "icu", "iceberg", "parquet", "inet", "azure"
For more info, visit https://duckdb.org/docs/stable/extensions/troubleshooting?version=v1.4.5&platform=linux_amd64&extension=bigquery |
|||| cityjson | 1.4.5 | ❌ | 1.8 | HTTP Error: Failed to download extension "cityjson" at URL "http://extensions.duckdb.org/v1.4.5/linux_amd64/cityjson.duckdb_extension.gz" (HTTP 404)

Candidate extensions: "fts", "inet", "encodings", "uc_catalog", "https"
For more info, visit https://duckdb.org/docs/stable/extensions/troubleshooting?version=v1.4.5&platform=linux_amd64&extension=cityjson |
|||| delta_classic | 1.4.5 | ❌ | 1.9 | HTTP Error: Failed to download extension "delta_classic" at URL "http://extensions.duckdb.org/v1.4.5/linux_amd64/delta_classic.duckdb_extension.gz" (HTTP 404)

Candidate extensions: "delta", "tpcds", "core_functions", "uc_catalog", "tpch"
For more info, visit https://duckdb.org/docs/stable/extensions/troubleshooting?version=v1.4.5&platform=linux_amd64&extension=delta_classic |
|||| duck_hunt | 1.4.5 | ❌ | 1.9 | HTTP Error: Failed to download extension "duck_hunt" at URL "http://extensions.duckdb.org/v1.4.5/linux_amd64/duck_hunt.duckdb_extension.gz" (HTTP 404)

Candidate extensions: "ducklake", "uc_catalog", "tpch", "core_functions", "md"
For more info, visit https://duckdb.org/docs/stable/extensions/troubleshooting?version=v1.4.5&platform=linux_amd64&extension=duck_hunt |
|||| duckdb_delta_sharing | 1.4.5 | ❌ | 1.9 | HTTP Error: Failed to download extension "duckdb_delta_sharing" at URL "http://extensions.duckdb.org/v1.4.5/linux_amd64/duckdb_delta_sharing.duckdb_extension.gz" (HTTP 404)

Candidate extensions: "delta", "ducklake", "uc_catalog", "sqlite_scanner", "mysql_scanner"
For more info, visit https://duckdb.org/docs/stable/extensions/troubleshooting?version=v1.4.5&platform=linux_amd64&extension=duckdb_delta_sharing |
|||| duckton | 1.4.5 | ❌ | 1.9 | HTTP Error: Failed to download extension "duckton" at URL "http://extensions.duckdb.org/v1.4.5/linux_amd64/duckton.duckdb_extension.gz" (HTTP 404)

Candidate extensions: "ducklake", "uc_catalog", "encodings", "delta", "core_functions"
For more info, visit https://duckdb.org/docs/stable/extensions/troubleshooting?version=v1.4.5&platform=linux_amd64&extension=duckton |
|||| finetype | 1.4.5 | ❌ | 1.9 | HTTP Error: Failed to download extension "finetype" at URL "http://extensions.duckdb.org/v1.4.5/linux_amd64/finetype.duckdb_extension.gz" (HTTP 404)

Candidate extensions: "inet", "fts", "iceberg", "http", "delta"
For more info, visit https://duckdb.org/docs/stable/extensions/troubleshooting?version=v1.4.5&platform=linux_amd64&extension=finetype |
|||| gcs | 1.4.5 | ❌ | 1.9 | HTTP Error: Failed to download extension "gcs" at URL "http://extensions.duckdb.org/v1.4.5/linux_amd64/gcs.duckdb_extension.gz" (HTTP 404)

Candidate extensions: "icu", "aws", "vss", "fts", "tpch"
For more info, visit https://duckdb.org/docs/stable/extensions/troubleshooting?version=v1.4.5&platform=linux_amd64&extension=gcs |
|||| gdx | 1.4.5 | ❌ | 1.9 | HTTP Error: Failed to download extension "gdx" at URL "http://extensions.duckdb.org/v1.4.5/linux_amd64/gdx.duckdb_extension.gz" (HTTP 404)

Candidate extensions: "md", "excel", "delta"
For more info, visit https://duckdb.org/docs/stable/extensions/troubleshooting?version=v1.4.5&platform=linux_amd64&extension=gdx |
|||| laterite_ags4 | 1.4.5 | ❌ | 1.9 | HTTP Error: Failed to download extension "laterite_ags4" at URL "http://extensions.duckdb.org/v1.4.5/linux_amd64/laterite_ags4.duckdb_extension.gz" (HTTP 404)

Candidate extensions: "spatial", "postgres_scanner", "delta", "sqlite_scanner", "encodings"
For more info, visit https://duckdb.org/docs/stable/extensions/troubleshooting?version=v1.4.5&platform=linux_amd64&extension=laterite_ags4 |
|||| autocomplete | 1.5.4 | ✅ | 1.9 |  |
|||| avro | 1.5.4 | ✅ | 1.8 |  |
|||| aws | 1.5.4 | ✅ | 2.0 |  |
|||| azure | 1.5.4 | ✅ | 2.0 |  |
|||| delta | 1.5.4 | ✅ | 2.4 |  |
|||| ducklake | 1.5.4 | ✅ | 2.1 |  |
|||| encodings | 1.5.4 | ✅ | 4.2 |  |
|||| excel | 1.5.4 | ✅ | 1.8 |  |
|||| fts | 1.5.4 | ✅ | 1.9 |  |
|||| httpfs | 1.5.4 | ✅ | 1.9 |  |
|||| iceberg | 1.5.4 | ✅ | 2.2 |  |
|||| icu | 1.5.4 | ✅ | 1.9 |  |
|||| inet | 1.5.4 | ✅ | 1.8 |  |
|||| json | 1.5.4 | ✅ | 2.0 |  |
|||| lance | 1.5.4 | ✅ | 3.9 |  |
|||| motherduck | 1.5.4 | ❌ | 2.1 | Invalid Input Error: Initialization function "motherduck_duckdb_cpp_init" from file "/home/runner/.duckdb/extensions/v1.5.4/linux_amd64/motherduck.duckdb_extension" threw an exception: "
Your DuckDB version (v1.5.4) is not yet supported by MotherDuck. The latest supported version is v1.5.3. Please downgrade to use MotherDuck.

See https://motherduck.com/docs/getting-started/connect-query-from-duckdb-cli for more information." |
|||| mysql | 1.5.4 | ✅ | 2.1 |  |
|||| odbc | 1.5.4 | ✅ | 1.9 |  |
|||| parquet | 1.5.4 | ✅ | 1.8 |  |
|||| postgres | 1.5.4 | ✅ | 2.1 |  |
|||| quack | 1.5.4 | ✅ | 2.2 |  |
|||| spatial | 1.5.4 | ✅ | 2.6 |  |
|||| sqlite | 1.5.4 | ✅ | 2.1 |  |
|||| tpcds | 1.5.4 | ✅ | 1.9 |  |
|||| tpch | 1.5.4 | ✅ | 1.9 |  |
|||| unity_catalog | 1.5.4 | ✅ | 2.3 |  |
|||| ui | 1.5.4 | ✅ | 2.3 |  |
|||| vortex | 1.5.4 | ✅ | 2.4 |  |
|||| vss | 1.5.4 | ✅ | 2.3 |  |
|||| bigquery | 1.5.4 | ❌ | 1.9 | HTTP Error: Failed to download extension "bigquery" at URL "http://extensions.duckdb.org/v1.5.4/linux_amd64/bigquery.duckdb_extension.gz" (HTTP 404)

Candidate extensions: "icu", "iceberg", "parquet", "inet", "quack"
For more info, visit https://duckdb.org/docs/stable/extensions/troubleshooting?version=v1.5.4&platform=linux_amd64&extension=bigquery |
|||| cityjson | 1.5.4 | ❌ | 1.9 | HTTP Error: Failed to download extension "cityjson" at URL "http://extensions.duckdb.org/v1.5.4/linux_amd64/cityjson.duckdb_extension.gz" (HTTP 404)

Candidate extensions: "fts", "unity_catalog", "inet", "encodings", "uc_catalog"
For more info, visit https://duckdb.org/docs/stable/extensions/troubleshooting?version=v1.5.4&platform=linux_amd64&extension=cityjson |
|||| delta_classic | 1.5.4 | ❌ | 1.9 | HTTP Error: Failed to download extension "delta_classic" at URL "http://extensions.duckdb.org/v1.5.4/linux_amd64/delta_classic.duckdb_extension.gz" (HTTP 404)

Candidate extensions: "delta", "tpcds", "core_functions", "uc_catalog", "inet"
For more info, visit https://duckdb.org/docs/stable/extensions/troubleshooting?version=v1.5.4&platform=linux_amd64&extension=delta_classic |
|||| duck_hunt | 1.5.4 | ❌ | 1.8 | HTTP Error: Failed to download extension "duck_hunt" at URL "http://extensions.duckdb.org/v1.5.4/linux_amd64/duck_hunt.duckdb_extension.gz" (HTTP 404)

Candidate extensions: "ducklake", "quack", "uc_catalog", "odbc_scanner", "odbc"
For more info, visit https://duckdb.org/docs/stable/extensions/troubleshooting?version=v1.5.4&platform=linux_amd64&extension=duck_hunt |
|||| duckdb_delta_sharing | 1.5.4 | ❌ | 1.8 | HTTP Error: Failed to download extension "duckdb_delta_sharing" at URL "http://extensions.duckdb.org/v1.5.4/linux_amd64/duckdb_delta_sharing.duckdb_extension.gz" (HTTP 404)

Candidate extensions: "delta", "ducklake", "uc_catalog", "odbc_scanner", "unity_catalog"
For more info, visit https://duckdb.org/docs/stable/extensions/troubleshooting?version=v1.5.4&platform=linux_amd64&extension=duckdb_delta_sharing |
|||| duckton | 1.5.4 | ❌ | 1.8 | HTTP Error: Failed to download extension "duckton" at URL "http://extensions.duckdb.org/v1.5.4/linux_amd64/duckton.duckdb_extension.gz" (HTTP 404)

Candidate extensions: "ducklake", "quack", "uc_catalog", "odbc", "encodings"
For more info, visit https://duckdb.org/docs/stable/extensions/troubleshooting?version=v1.5.4&platform=linux_amd64&extension=duckton |
|||| finetype | 1.5.4 | ❌ | 1.9 | HTTP Error: Failed to download extension "finetype" at URL "http://extensions.duckdb.org/v1.5.4/linux_amd64/finetype.duckdb_extension.gz" (HTTP 404)

Candidate extensions: "inet", "fts", "iceberg", "http", "delta"
For more info, visit https://duckdb.org/docs/stable/extensions/troubleshooting?version=v1.5.4&platform=linux_amd64&extension=finetype |
|||| gcs | 1.5.4 | ❌ | 1.9 | HTTP Error: Failed to download extension "gcs" at URL "http://extensions.duckdb.org/v1.5.4/linux_amd64/gcs.duckdb_extension.gz" (HTTP 404)

Candidate extensions: "odbc_scanner", "aws", "fts", "icu", "vss"
For more info, visit https://duckdb.org/docs/stable/extensions/troubleshooting?version=v1.5.4&platform=linux_amd64&extension=gcs |
|||| gdx | 1.5.4 | ❌ | 1.9 | HTTP Error: Failed to download extension "gdx" at URL "http://extensions.duckdb.org/v1.5.4/linux_amd64/gdx.duckdb_extension.gz" (HTTP 404)

Candidate extensions: "md", "odbc", "delta", "excel"
For more info, visit https://duckdb.org/docs/stable/extensions/troubleshooting?version=v1.5.4&platform=linux_amd64&extension=gdx |
|||| laterite_ags4 | 1.5.4 | ❌ | 1.9 | HTTP Error: Failed to download extension "laterite_ags4" at URL "http://extensions.duckdb.org/v1.5.4/linux_amd64/laterite_ags4.duckdb_extension.gz" (HTTP 404)

Candidate extensions: "spatial", "postgres_scanner", "delta", "lance", "sqlite_scanner"
For more info, visit https://duckdb.org/docs/stable/extensions/troubleshooting?version=v1.5.4&platform=linux_amd64&extension=laterite_ags4 |

