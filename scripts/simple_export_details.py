#!/usr/bin/env python3
"""Simple script to export detailed analysis data for manual review."""

import sys
import csv
from pathlib import Path
from datetime import datetime
import asyncio

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from conf.config import Config
from src.analyzers import AnalysisOrchestrator


async def main():
    try:
        print("🔍 Starting detailed export...")
        config = Config()
        orchestrator = AnalysisOrchestrator(config, cache_hours=24)
        
        # Run analysis
        result = await orchestrator.run_analysis_mode('full')
        
        # Prepare data
        data = []
        
        # Core extensions
        for ext in result.core_extensions:
            data.append({
                'extension': ext.name,
                'type': 'Core',
                'status': ext.status,
                'repository': ext.repository,
                'last_push': ext.last_push.isoformat() if ext.last_push else 'Unknown',
                'days_since_push': ext.last_activity,
                'stars': ext.stars,
                'language': ext.language,
                'description': ext.description,
                'docs_url': ext.docs_url,
                'activity_class': 'Active' if ext.last_activity and ext.last_activity <= 30 else 'Low' if ext.last_activity else 'Unknown'
            })
        
        # Community extensions
        for ext in result.community_extensions:
            data.append({
                'extension': ext.name,
                'type': 'Community',
                'status': ext.status,
                'repository': ext.repository,
                'last_push': ext.last_push.isoformat() if ext.last_push else 'Unknown',
                'days_since_push': ext.last_activity,
                'stars': ext.stars,
                'language': ext.language,
                'description': ext.description,
                'docs_url': ext.docs_url,
                'activity_class': 'Active' if ext.last_activity and ext.last_activity <= 90 else 'Low' if ext.last_activity and ext.last_activity <= 365 else 'Inactive' if ext.last_activity else 'Unknown'
            })
        
        # Export CSV
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f'reports/detailed_manual_review_{timestamp}.csv'
        
        # Create reports dir if needed
        Path('reports').mkdir(exist_ok=True)
        
        with open(filename, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=[
                'extension', 'type', 'status', 'repository', 'last_push', 'days_since_push', 
                'stars', 'language', 'description', 'docs_url', 'activity_class'
            ])
            writer.writeheader()
            writer.writerows(data)
        
        print(f"✅ Exported {len(data)} extensions to: {filename}")
        return filename
        
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    asyncio.run(main())