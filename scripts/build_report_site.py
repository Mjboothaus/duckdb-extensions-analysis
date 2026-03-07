#!/usr/bin/env python3

import argparse
import re
import subprocess
from datetime import datetime
from pathlib import Path

import markdown


def _extract_report_timestamp(md_content: str, *, git_path: Path) -> str:
    """Extract a report timestamp.

    Preference order:
    1) A timestamp embedded in the Markdown content.
    2) Latest git commit time for the Markdown file.
    3) Current time (UTC).
    """

    report_timestamp = "Loading..."

    # Try to find the timestamp in the Markdown first.
    timestamp_patterns = [
        r"\*\*Report Generated:\*\* ([\d-]+ [\d:]+ UTC)",
        r"Report Generated: ([\d-]+ [\d:]+ UTC)",
        r"Last Updated: ([\d-]+ [\d:]+ UTC)",
    ]

    for pattern in timestamp_patterns:
        timestamp_match = re.search(pattern, md_content)
        if timestamp_match:
            report_timestamp = timestamp_match.group(1)
            break

    # If not found in Markdown, try git (latest commit time for the input file).
    if report_timestamp == "Loading...":
        try:
            git_timestamp = subprocess.check_output(
                [
                    "git",
                    "log",
                    "-1",
                    "--format=%cd",
                    "--date=format:%Y-%m-%d %H:%M:%S UTC",
                    "--",
                    str(git_path),
                ],
                cwd=Path.cwd(),
                universal_newlines=True,
            ).strip()
            if git_timestamp:
                report_timestamp = git_timestamp
        except Exception:
            # Git may not be available (or file not tracked). Fall back to current time.
            pass

    if report_timestamp == "Loading...":
        report_timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")

    return report_timestamp


def _nav_links_for_md(md_content: str) -> str:
    """Return the header nav links HTML snippet based on the report content."""

    # Detect third-party report by its stable section heading.
    if "## Verified third-party extensions" in md_content:
        return (
            '<a href="#verified-third-party-extensions">Jump to Extensions</a>'
            ' | <a href="#appendix-discovery-and-verification-methodology">Methodology</a>'
            ' | <a href="https://mjboothaus.github.io/duckdb-extensions-analysis/">Main report</a>'
        )

    return (
        '<a href="#summary">Jump to Summary</a>'
        ' | <a href="#core-extensions">Core Extensions</a>'
        ' | <a href="#community-extensions">Community Extensions</a>'
        ' | <a href="https://mjboothaus.github.io/duckdb-extensions-analysis/third-party/">Verified third-party extensions</a>'
    )


def build_site(*, input_md: Path, out_dir: Path, out_file: str) -> None:
    md_content = input_md.read_text(encoding="utf-8")

    report_timestamp = _extract_report_timestamp(md_content, git_path=input_md)

    nav_links = _nav_links_for_md(md_content)

    # Convert Markdown to HTML with proper handling of HTML blocks.
    # The 'md_in_html' extension enables Markdown parsing inside <details> and other HTML tags.
    md = markdown.Markdown(
        extensions=[
            "tables",
            "fenced_code",
            "toc",
            "md_in_html",  # Critical: enables markdown parsing inside <details>
        ]
    )
    html_content = md.convert(md_content)

    template_dir = Path("scripts/templates")
    html_template = (template_dir / "index.html").read_text(encoding="utf-8")
    css_content = (template_dir / "styles.css").read_text(encoding="utf-8")
    js_content = (template_dir / "main.js").read_text(encoding="utf-8")

    full_html = html_template.replace("{{STYLES}}", css_content)
    full_html = full_html.replace("{{CONTENT}}", html_content)
    full_html = full_html.replace("{{REPORT_TIMESTAMP}}", report_timestamp)
    full_html = full_html.replace("{{NAV_LINKS}}", nav_links)
    full_html = full_html.replace("{{JAVASCRIPT}}", js_content)

    out_dir.mkdir(parents=True, exist_ok=True)

    (out_dir / out_file).write_text(full_html, encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Generate a static HTML site from a Markdown report.",
    )
    parser.add_argument(
        "--input",
        default="reports/latest.md",
        help="Path to the input Markdown report.",
    )
    parser.add_argument(
        "--out-dir",
        default="_site",
        help="Output directory for generated site files.",
    )
    parser.add_argument(
        "--out-file",
        default="index.html",
        help="Output HTML filename.",
    )
    args = parser.parse_args()

    input_md = Path(args.input)
    out_dir = Path(args.out_dir)

    build_site(input_md=input_md, out_dir=out_dir, out_file=args.out_file)

    print("✅ HTML site generated successfully")


if __name__ == "__main__":
    main()
