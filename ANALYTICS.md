# Analytics

## Overview

This project uses **Umami Cloud** for privacy-focused, lightweight web analytics on the GitHub Pages site.

## Implementation

- **Platform**: [Umami Cloud](https://umami.is)
- **Dashboard**: https://analytics.umami.is
- **Site URL**: https://mjboothaus.github.io/duckdb-extensions-analysis/
- **Integration**: Script tag in `scripts/templates/index.html`

## What's Tracked

Umami respects user privacy and collects minimal data:

- Page views and unique visitors
- Referrer sources
- Device types (desktop/mobile/tablet)
- Browser and OS information
- Geographic location (country level only)

**Not tracked:**
- Personal identifying information
- Cookies (cookieless tracking)
- Cross-site user behaviour
- IP addresses (anonymised)

## Why Umami?

- **Privacy-first**: GDPR and CCPA compliant by default
- **Lightweight**: ~2KB script, no performance impact
- **Open source**: Transparent, auditable code
- **Simple**: No cookie banners needed

## Access

Analytics dashboard access is restricted to repository maintainers. Public aggregate stats may be shared in future releases.

## Removal

To disable tracking, remove the Umami script tag from `scripts/templates/index.html` (lines 13-14).
