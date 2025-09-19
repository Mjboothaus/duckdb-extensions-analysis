+++ 
title = "Navigating DuckDB Extension Updates: A Lesson from Upgrading" 
date = "2025-10-18" 

[taxonomies] 
tags=["DuckBD", "Extensions", "Upgrading"]

[extra]
comment = true
+++

## Executive Summary

Upgrading to a new [DuckDB](https://duckdb.org) version unlocks powerful data processing capabilities (and indeed an awesome new database encryption feature and the prime motivation for upgrading), but unexpected delays in extension availability, like the excellent web-based usee interface being unavailable, can disrupt critical analytics workflows. 

My experience upgrading and facing this issue reminded me of a key lesson: extensions, whether core (developed by the DuckDB team) or community (third-party add-ons), may not be ready immediately, a common challenge in extensible software ecosystems. 

This matters for organisations because incompatible extensions can delay projects, increase costs, or require rollbacks, impacting data-driven decision-making. This post provides straightforward tools to check installed extensions, verify their online status, safely test new versions, and revert to stable ones if needed.

---

DuckDB’s rapid evolution is a boon for data engineers, with `v1.4.0`, released on 16 September 2025, delivering exciting new features. However, a recent experience taught me a valuable lesson: extensions don’t always update instantly with new releases. After upgrading to `v1.4.0`, I assumed the web-based `ui` extension would be available, only to find it missing on macOS. When I tried to downgrade back to my previous version using Homebrew, it wasn’t straightforward, though alternatives exist. 

This prompted me to investigate the status of DuckDB’s core and community extensions for versions `v1.0.0` and later. In this post, I’ll share insights on extension availability, highlight why you need to be judicious when choosing a DuckDB version, and provide tools to check your local setup and downgrade if needed. My aim is to help you plan your projects effectively, not to unnecessarily critique this fantastic tool.

## Why Extensions Require Careful Planning

DuckDB extensions enhance its functionality, from querying JSON with the [`json`](https://duckdb.org/docs/stable/data/json/overview.html) extension to visualising data via the `ui` or performing geospatial analysis with [`h3`](https://duckdb.org/community_extensions/extensions/h3.html). Core extensions are maintained by the DuckDB team, while community extensions are third-party contributions hosted at https://github.com/duckdb/community-extensions. 

Like Python’s packages or R’s libraries, extensions in such ecosystems may lag behind core releases as maintainers ensure compatibility. My assumption that the `ui` extension would be ready for `v1.4.0` was a reminder to verify availability before upgrading, especially for critical components. If issues arise post-upgrade, downgrading can be tricky with [Homebrew](https://brew.sh), but there are workarounds (see Appendix C).

## Core Extensions: Usually Ready, with Exceptions

Core extensions, distributed via https://extensions.duckdb.org, are compiled alongside DuckDB releases. The official documentation (https://duckdb.org/docs/stable/core_extensions/overview.html) lists them as **stable**, except for the `arrow` extension, deprecated in v1.3.0 and replaced by the community-maintained `nanoarrow`. From `v1.0.0` (June 2024) to `v1.4.0` (September 2025), core extensions typically have a **zero-day lag**, available on release day.

However, my upgrade to `v1.4.0` hit a snag: the `ui` extension, first introduced in `v1.2.1` (12 March 2025), isn’t available on macOS (`osx_arm64` and `osx_amd64`) as of 18 September 2025. Running `INSTALL ui;` in DuckDB `v1.4.0` fails, indicating a delay of **at least two days**, likely due to a build issue (although this extension is heavily sponsored by the excellent team at [MotherDuck](https://motherduck.com)). This was unexpected, as the `ui` was available immediately for `v1.2.1` and `v1.3.0`, and other core extensions like `json` and `parquet` are consistently ready. Other platforms (e.g., Linux, Windows) may also be affected, but you can check using tools in the appendices. This highlights the wisdom of confirming extension availability before upgrading, a common consideration in add-on ecosystems.

## Community Extensions: Active with Minimal Delays

Community extensions, distributed via https://community-extensions.duckdb.org, are built through continuous integration (CI). If no code changes are needed, they’re available within hours (0-day lag). If updates are required, lags may reach 7–15 days, depending on maintainers. An extension is discontinued if its GitHub repository is archived or removed from https://duckdb.org/community_extensions/list_of_extensions.html.

The current 14 community extensions include `nanoarrow`, `bigquery`, `h3`, `prql`, and others. Using a Python script (Appendix A), I checked their statuses:
- **h3** (geospatial indexing): Aligns with DuckDB releases, with `v1.4.0` available on 16 September 2025 (0-day lag). Bugfix releases (e.g., `v1.3.1`, 26 days after `v1.3.0`) address issues, not compatibility.
- **prql** (query language): No tagged releases, but CI rebuilds for `v1.0.0+` ensure availability within zero to a few days, with potential delays for compatibility fixes.

The script (below) confirmed all 14 extensions are **ongoing**, with no archived repositories and recent activity (commits in 2025), indicating active maintenance.

## Investigating Your Local DuckDB Setup

Before upgrading, it’s wise to check which extensions are installed in your local DuckDB instance and their versions. Appendix B provides SQL queries to list installed extensions and their versions, helping you assess compatibility with a new DuckDB version. This is especially useful if you rely on specific extensions like `ui` or `h3`.

## Downgrading If Needed

If an upgrade reveals extension issues (like my `ui` experience), you may want to revert to a previous version. Homebrew may support direct downgrades (depending on the package), but you can use `brew extract` to install older formulas. Appendix C details steps for downgrading via Homebrew and alternatives, such as downloading binaries from DuckDB’s GitHub releases. These pathways ensure you can roll back without much hassle.

## Choosing the Right Version

DuckDB’s extension ecosystem is robust, but like any tool with add-ons, version selection requires care. Core extensions are usually available immediately, though the `ui` delay in `v1.4.0` on macOS shows exceptions can occur. Community extensions typically keep pace well, with lags of 0–15 days, and none are discontinued to date. To make informed choices:
- Verify core extension statuses at https://duckdb.org/docs/stable/core_extensions/overview.html. There are a number of examples of "Experimental" extensions on this page.
- Test extension availability with `INSTALL <extension>;` or the script in Appendix A.
- Check installed extensions in your local instance using Appendix B.
- If needed, downgrade using Appendix C.
- Monitor updates for delayed extensions (e.g., `ui`) by retrying installation or checking availability.

## Conclusion

My experience upgrading to `v1.4.0` and finding the `ui` extension unavailable, followed by the non-trivial Homebrew downgrade, was a reminder to approach version upgrades thoughtfully. DuckDB’s extensions are a strength, but their availability isn’t guaranteed on release day, a common trait in add-on ecosystems. By checking statuses, local setups, and having downgrade options, you can avoid surprises. Use the tools in the appendices to explore extension statuses and your DuckDB instance. 

Have you faced similar issues with extensions or downgrades?

---

## Appendix A: Python Script for Community Extension Statuses

This Python script checks the status of community extensions by querying the GitHub API. It fetches the extension list, reads `metadata.toml` files for source repositories, and checks if each is archived (discontinued) or when it was last updated. Install dependencies: `pip install httpx loguru tenacity toml`. Save as `check_duckdb_extensions.py` and run with `python check_duckdb_extensions.py`. If you hit GitHub’s rate limit (60 requests/hour unauthenticated), generate a personal access token at https://github.com/settings/tokens and add it to `HEADERS` as `{"Authorization": "token YOUR_TOKEN"}`.

TODO: Add link to code in GitHub repo

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


TODO: Add link to code in GitHub repo

**Inserting Results**: Run the script and copy the `INFO` lines into the post. For example, under “Core Extensions” or “Community Extensions,” add the relevant output or a summary. The script first logs core extensions (e.g., "json (Core, Stage: stable): Ongoing | Last updated: 2025-09-16 00:00:00 (2 days ago in v1.4.0)"), then community ones. Update `DUCKDB_VERSION` and `DUCKDB_RELEASE_DATE` for new releases.