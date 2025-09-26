+++ 
title = "Navigating DuckDB Extension Updates: A Lesson from Upgrading" 
date = "2025-09-26" 

[taxonomies] 
tags=["DuckDB", "Extensions", "Upgrading"]

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

## Appendix A: DuckDB Extension Analysis Tool

Add cross-reference to the other post and linking text.


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
