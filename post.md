+++ 
title = "When DuckDB Extensions Don't Keep Up: A Practical Guide to Version Management" 
date = "2025-10-18" 

[taxonomies] 
tags=["DuckDB", "Extensions", "Version Management", "Data Engineering"]

[extra]
comment = true
+++

*Ever upgraded a database only to find your favourite features missing? Here's what I learned about managing DuckDB extension compatibility—and how to avoid getting stuck.*

---

Last month, I eagerly upgraded to [DuckDB](https://duckdb.org) v1.4.0 for its new database encryption feature. Everything seemed perfect until I tried loading the `ui` extension—DuckDB's excellent web-based interface. 

**Error**: Extension not available.

Worse yet, downgrading via Homebrew proved more complex than expected. This experience taught me an important lesson about managing extensible software: **not all extensions are ready on day one of a new release**.

If you work with DuckDB extensions—whether for geospatial analysis, cloud connectivity, or data visualisation—this post will help you avoid similar surprises and manage version compatibility effectively.

## The Extension Compatibility Challenge

DuckDB's power lies partly in its extensions—add-ons that enable everything from JSON querying to geospatial analysis. There are two types:

- **Core extensions**: Maintained by the DuckDB team (usually available immediately)
- **Community extensions**: Third-party contributions (may take days or weeks to update)

Like any extensible system (think Python packages or browser add-ons), extensions need time to catch up with new releases. The problem? It's easy to assume everything will "just work" after upgrading.

*For the technical details on extension versioning, see the [DuckDB versioning documentation](https://duckdb.org/docs/stable/extensions/versioning_of_extensions.html).*

## What I Discovered: The Extension Lag Reality

**Core Extensions** (maintained by DuckDB team) usually have zero-day availability. These include essentials like `json`, `parquet`, and `httpfs`. However, my `ui` extension experience proved that even core extensions can have delays—particularly on specific platforms like macOS.

**Community Extensions** (80+ third-party extensions) typically lag 0-15 days behind new releases, depending on maintainer response time. The good news? I found all community extensions are actively maintained with recent activity in 2024-2025.

## Practical Solutions: Three Essential Strategies

After this experience, I developed a simple workflow to avoid extension-related upgrade surprises:

### 1. Check Before You Upgrade
Before upgrading DuckDB, verify that critical extensions are available:
```sql
INSTALL extension_name;  -- Test if it works
```

### 2. Test in Isolation
Use Python virtual environments to test new DuckDB versions without affecting your main setup (see Appendix D for detailed steps).

### 3. Have a Rollback Plan
Know how to downgrade if needed. While Homebrew doesn't have a simple `downgrade` command, you can use `brew extract` or download binaries directly (detailed in Appendix C).

## The Bigger Picture: Extension Ecosystem Health

To better understand DuckDB's extension landscape, I built a tool that monitors both core and community extensions (available on [GitHub](https://github.com/databooth/duckdb-extensions-analysis)). Key findings:

- **24 core extensions** with generally excellent availability
- **80+ community extensions** with active maintenance 
- **Zero discontinued extensions** (all repositories remain active)
- **Typical lag**: 0-15 days for community extensions, usually 0 days for core

This analysis reinforced that DuckDB's extension ecosystem is healthy and well-maintained—my `ui` experience was an exception, not the rule.

## Key Takeaways

DuckDB's rapid development is impressive, but extension compatibility requires some planning:

1. **Test critical extensions** before upgrading production systems
2. **Use virtual environments** to safely test new versions
3. **Have a rollback strategy** ready (especially important with Homebrew)
4. **Monitor extension status** for delayed availability

The extension ecosystem is robust and well-maintained—delays like my `ui` experience are uncommon but worth preparing for.

**Resources:**
- Extension monitoring tool: [github.com/databooth/duckdb-extensions-analysis](https://github.com/databooth/duckdb-extensions-analysis)
- Check your local setup: Use the SQL queries in Appendix B
- Safe testing: Virtual environment setup in Appendix D

Have you encountered similar extension compatibility issues? I'd love to hear about your experiences in the comments.

---

## Appendix A: Python Script for Community Extension Statuses

This Python script checks the status of community extensions by querying the GitHub API. It fetches the extension list, reads `metadata.toml` files for source repositories, and checks if each is archived (discontinued) or when it was last updated. Install dependencies: `pip install httpx loguru tenacity toml`. Save as `check_duckdb_extensions.py` and run with `python check_duckdb_extensions.py`. If you hit GitHub’s rate limit (60 requests/hour unauthenticated), generate a personal access token at https://github.com/settings/tokens and add it to `HEADERS` as `{"Authorization": "token YOUR_TOKEN"}`.

**[View the full script on GitHub →](https://github.com/databooth/duckdb-extensions-analysis/blob/main/scripts/analyze_extensions.py)**

**Inserting Results**: Run the script and copy the `INFO` lines (e.g., “h3 (Repo: isaacbrodsky/h3-duckdb): Ongoing | Last push: 2025-09-16T00:00:00 (2 days ago)”) into the post under “Community Extensions.” For example:

> Running the script on 18 September 2025 showed:
> ```
> 2025-09-18 17:03:00 | INFO | Found 14 community extensions: nanoarrow, bigquery, capi_quack, eeagrid, ...
> 2025-09-18 17:03:01 | INFO | Processing h3
> 2025-09-18 17:03:02 | INFO | h3 (Repo: isaacbrodsky/h3-duckdb): Ongoing | Last push: 2025-09-16T00:00:00 (2 days ago)
> 2025-09-18 17:03:02 | INFO | Processing prql
> 2025-09-18 17:03:03 | INFO | prql (Repo: ywelsch/duckdb-prql): Ongoing | Last push: 2025-08-10T00:00:00 (39 days ago)
> ...
> ```

Alternatively, summarise: “The script confirmed all 14 community extensions are ongoing, with `h3` updated 2 days ago and `prql` 39 days ago.”

## Appendix B: Investigating Installed Extensions in Your Local DuckDB Instance
To check which extensions are installed in your local DuckDB instance and their versions, use the following SQL queries in the DuckDB CLI or a connected client. These help you assess compatibility before upgrading to a new version like v1.4.0.

1. **List Installed Extensions**:
   ```sql
   SELECT * FROM duckdb_extensions();
   ```
   This returns a table with columns like `extension_name`, `loaded`, `installed`, and `version`. The `installed` column indicates if the extension is installed, and `version` shows the installed version (or NULL if not installed).

2. **Check Specific Extension (e.g., ui)**:
   ```sql
   SELECT * FROM duckdb_extensions() WHERE extension_name = 'ui';
   ```
   If the `ui` extension is installed, you’ll see its version and load status. If `installed` is FALSE or the row is missing, it’s not installed.

3. **Attempt Installation**:
   To test if an extension is available for your platform and DuckDB version:
   ```sql
   INSTALL ui;
   LOAD ui;
   ```
   If installation fails (e.g., “HTTP Error: 404” for `ui` on v1.4.0 macOS), the extension isn’t available yet. Check periodically to detect when it becomes available.

4. **Example Output**:
   Running `SELECT * FROM duckdb_extensions();` on a local instance might yield:
   ```
   extension_name | loaded | installed | version
   ---------------|--------|-----------|--------
   json           | true   | true      | v1.4.0
   parquet        | false  | true      | v1.4.0
   ui             | false  | false     | NULL
   ...
   ```
   This shows `json` and `parquet` are installed, but `ui` is not, confirming the v1.4.0 macOS issue.

**Steps**:
- Launch the DuckDB CLI (`duckdb`) or connect via a client (e.g., Python with `duckdb` package).
- Run the queries above.
- Review the output to identify installed extensions and their versions.
- If planning an upgrade, compare installed versions with those required for the new DuckDB version (check https://duckdb.org/docs/stable/extensions/index for compatibility).

## Appendix C: Downgrading DuckDB Versions on macOS
Downgrading DuckDB via Homebrew isn’t direct (no built-in `brew downgrade` command), but you can use `brew extract` to install a previous formula or download binaries from DuckDB’s GitHub releases. Below are steps for both, assuming you’re downgrading from v1.4.0 to v1.3.0 (adjust versions as needed).

### Method 1: Using Homebrew Extract (Recommended for Homebrew Users)
1. Uninstall the current version:
   ```
   brew uninstall duckdb
   ```

2. Create a local tap and extract the formula for v1.3.0:
   ```
   brew tap-new $USER/local-duckdb
   brew extract --version=1.3.0 duckdb $USER/local-duckdb
   ```

3. Install the extracted version:
   ```
   brew install $USER/local-duckdb/duckdb@1.3.0
   ```

4. Verify:
   ```
   duckdb --version
   ```
   This should output "v1.3.0". If needed, clean up the tap later with `brew untap $USER/local-duckdb`.

### Method 2: Download Binary from GitHub Releases (Simpler Alternative)
1. Visit https://github.com/duckdb/duckdb/releases and find v1.3.0 (released 21 May 2025).

2. Download the macOS universal binary: `duckdb_cli-osx-universal.zip`.

3. Extract the zip file to get the `duckdb` executable.

4. Move it to a directory in your PATH (e.g., `/usr/local/bin`):
   ```
   unzip duckdb_cli-osx-universal.zip
   mv duckdb /usr/local/bin/
   ```

5. Verify:
   ```
   duckdb --version
   ```
   This runs the downgraded version without affecting Homebrew. You can keep multiple versions by renaming the binary (e.g., `duckdb-1.3.0`).

**Notes**:
- For Python bindings, use `pip install duckdb==1.3.0` in a virtual environment.
- Always back up databases before version changes, as DuckDB supports backward compatibility but not always forward.
- If building from source, clone the repo and checkout the tag: `git checkout v1.3.0` then build.

These methods provide flexible pathways to revert if extensions like `ui` aren’t ready in a new release.

## Appendix D: Steps to Set Up and Test a New Version of DuckDB in a Venv
You can set up a Python virtual environment (venv) to install and test a specific or new version of the DuckDB Python package (`duckdb`) without impacting your Homebrew-installed DuckDB CLI or system-wide setup. This leverages venv's isolation, which ensures the pip-installed DuckDB (including its embedded engine) stays contained within the venv and doesn't conflict with or override the Homebrew binary (e.g., at `/usr/local/bin/duckdb`). The Python package is primarily for scripting and data analysis in Python, while Homebrew handles the standalone CLI—testing in venv allows you to evaluate the DuckDB engine's behavior via Python without affecting the CLI.

### Steps to Set Up and Test a New Version of DuckDB in a Venv
1. **Create a Virtual Environment**:
   - Navigate to a project directory (or create one, e.g., `mkdir duckdb-test && cd duckdb-test`).
   - Create the venv: `python3 -m venv myenv` (replace `myenv` with your preferred name; use `python` if that's your default Python 3 executable).

2. **Activate the Venv**:
   - On macOS/Linux: `source myenv/bin/activate`
   - On Windows: `myenv\Scripts\activate`

3. **Install a Specific DuckDB Version**:
   - Use pip to install the desired version (e.g., for testing v1.4.0): `pip install duckdb==1.4.0`
   - For a newer/pre-release version: `pip install duckdb --upgrade --pre`
   - This installs the DuckDB Python bindings and engine within the venv only.

4. **Test the Version**:
   - Run Python: `python`
   - Import and check: 
     ```python
     import duckdb
     print(duckdb.__version__)  # Should output the installed version, e.g., '1.4.0'
     ```
   - Test functionality (e.g., query with extensions):
     ```python
     con = duckdb.connect()
     con.install_extension('ui')  # Or any extension; this tests availability in the new version
     con.load_extension('ui')
     con.sql('SELECT 42')  # Basic query to confirm the engine works
     ```
   - If testing the `ui` extension (as in your experience), note it may still have availability delays, but this isolates the test.

5. **Deactivate When Done**:
   - Run `deactivate` to exit the venv. Your Homebrew DuckDB remains unchanged—verify with `duckdb --version` outside the venv.

### Key Notes
- **Isolation Confirmation**: The venv ensures no interference with Homebrew's DuckDB CLI or libraries. Pip-installed `duckdb` embeds its own engine, so scripts in the venv use that version, while the CLI uses Homebrew's.
- **If You Need the CLI for Testing**: Venv is Python-focused. For CLI testing without affecting Homebrew, download the binary from https://github.com/duckdb/duckdb/releases (e.g., `duckdb_cli-osx-universal.zip` for v1.4.0), extract, and run it directly (e.g., `./duckdb`) or alias it temporarily.
- **Potential Limitations**: If your workflow mixes CLI and Python, ensure consistency (e.g., via `duckdb.connect()` in scripts). Always back up data before version tests, as DuckDB supports backward but not always forward compatibility.
- **Troubleshooting**: If pip fails (e.g., build issues), ensure you have build tools like `cmake` (install via Homebrew if needed: `brew install cmake`). For older versions, check availability on PyPI.

## Appendix E: Python Script for Checking Currency of Core and Community Extensions
This script assesses the "currency" (status and recency) of core and community extensions. Core extensions are pulled from DuckDB docs (status like "stable" and recency tied to the latest DuckDB release). Community extensions are checked via GitHub API. Install dependencies: `pip install httpx loguru tenacity toml beautifulsoup4 requests`. Save as `check_duckdb_extensions_full.py` and run with `python check_duckdb_extensions_full.py`. If you hit GitHub’s rate limit, add a token to `HEADERS`.


**[View the complete analysis tool on GitHub →](https://github.com/databooth/duckdb-extensions-analysis)**

**Inserting Results**: Run the script and copy the `INFO` lines into the post. For example, under “Core Extensions” or “Community Extensions,” add the relevant output or a summary. The script first logs core extensions (e.g., "json (Core, Stage: stable): Ongoing | Last updated: 2025-09-16 00:00:00 (2 days ago in v1.4.0)"), then community ones. Update `DUCKDB_VERSION` and `DUCKDB_RELEASE_DATE` for new releases.