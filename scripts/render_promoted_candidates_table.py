import argparse
import csv
from datetime import datetime, timezone
from pathlib import Path


def parse_dt(s: str | None) -> datetime | None:
    if not s:
        return None
    try:
        return datetime.fromisoformat(s.replace("Z", "+00:00"))
    except Exception:
        return None


def main() -> int:
    parser = argparse.ArgumentParser(description="Render promoted candidates CSV as a readable table")
    parser.add_argument("input", help="CSV file produced by scripts/promote_extension_candidates.py")
    parser.add_argument(
        "--as-of",
        default=None,
        help="ISO date/time to compute recency (defaults to now, UTC). Example: 2026-03-01T00:00:00Z",
    )
    parser.add_argument(
        "--max-reason",
        type=int,
        default=60,
        help="Max characters for the reason column",
    )
    args = parser.parse_args()

    as_of = datetime.now(timezone.utc)
    if args.as_of:
        as_of = datetime.fromisoformat(args.as_of.replace("Z", "+00:00"))

    rows = list(csv.DictReader(Path(args.input).open()))

    # Augment with URL + days_ago
    for r in rows:
        repo = r.get("repo") or ""
        r["url"] = f"https://github.com/{repo}" if repo else ""
        pushed = r.get("pushed") or ""
        dt = parse_dt(pushed)
        r["days_ago"] = str((as_of - dt).days) if dt else ""

    # Sort: score desc, then recency asc (smaller days), then stars desc
    def key(r: dict):
        score = int(r.get("score") or 0)
        stars = int(r.get("stars") or 0)
        days = int(r.get("days_ago") or 10**9) if str(r.get("days_ago") or "").isdigit() else 10**9
        return (score, -days, stars)

    rows.sort(key=key, reverse=True)

    cols = [
        "repo",
        "url",
        "pushed",
        "days_ago",
        "score",
        "stars",
        "is_template_clone",
        "release_asset_count",
        "reason",
    ]

    width = {c: len(c) for c in cols}
    for r in rows:
        for c in cols:
            v = str(r.get(c, "") or "")
            if c == "reason" and len(v) > args.max_reason:
                v = v[: max(0, args.max_reason - 3)] + "..."
            width[c] = min(100, max(width[c], len(v)))

    def fmt_row(r: dict) -> str:
        parts = []
        for c in cols:
            v = str(r.get(c, "") or "")
            if c == "reason" and len(v) > args.max_reason:
                v = v[: max(0, args.max_reason - 3)] + "..."
            if c in {"score", "stars", "release_asset_count", "days_ago"}:
                parts.append(v.rjust(width[c]))
            else:
                parts.append(v.ljust(width[c]))
        return " | ".join(parts)

    header = " | ".join([c.ljust(width[c]) for c in cols])
    sep = "-+-".join(["-" * width[c] for c in cols])
    print(header)
    print(sep)
    for r in rows:
        print(fmt_row(r))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
