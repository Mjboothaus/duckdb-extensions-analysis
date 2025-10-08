#!/usr/bin/env python3
"""
Export Detailed Analysis for Manual Review

This script exports comprehensive analysis details including:
- Extension status reasoning
- Activity metrics and thresholds
- Repository analysis data
- URL validation results
- Deprecation detection reasoning
"""

import sys
import json
import csv
from pathlib import Path
from datetime import datetime, timedelta
import asyncio

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from conf.config import Config
from src.analyzers import AnalysisOrchestrator


async def export_detailed_analysis():
    """Export detailed analysis data for manual review."""
    
    try:
        config = Config()
        orchestrator = AnalysisOrchestrator(config, cache_hours=24)  # Use cache for speed
        
        print("🔍 Exporting detailed analysis data for manual review...")
        print("=" * 60)
        
        # Run analysis
        analysis_result = await orchestrator.run_analysis_mode('full')
        
        # Prepare detailed data
        detailed_data = []
        
        # Process core extensions
        for ext in analysis_result.core_extensions:
        detailed_data.append({
            'extension': ext.name,
            'type': 'Core',
            'status': ext.status,
            'status_reasoning': _get_status_reasoning(ext, 'core'),
            'repository': ext.repository,
            'last_push_date': ext.last_push.isoformat() if ext.last_push else 'Unknown',
            'days_since_push': ext.last_activity,
            'stars': ext.stars,
            'language': ext.language,
            'description': ext.description,
            'docs_url': ext.docs_url,
            'activity_level': _classify_activity(ext.last_activity, 'core'),
            'repository_accessible': 'Yes' if ext.repository else 'No',
            'documentation_accessible': 'Yes' if ext.docs_url else 'No',
        })
    
    # Process community extensions
    for ext in analysis_result.community_extensions:
        detailed_data.append({
            'extension': ext.name,
            'type': 'Community',
            'status': ext.status,
            'status_reasoning': _get_status_reasoning(ext, 'community'),
            'repository': ext.repository,
            'last_push_date': ext.last_push.isoformat() if ext.last_push else 'Unknown',
            'days_since_push': ext.last_activity,
            'stars': ext.stars,
            'language': ext.language,
            'description': ext.description,
            'docs_url': ext.docs_url,
            'activity_level': _classify_activity(ext.last_activity, 'community'),
            'repository_accessible': 'Yes' if hasattr(ext, 'repository_error') and not ext.repository_error else 'Unknown',
            'documentation_accessible': 'Yes' if ext.docs_url else 'No',
            'deprecation_score': getattr(ext, 'deprecation_score', 'N/A'),
            'deprecation_reasons': getattr(ext, 'deprecation_reasons', []),
        })
    
    # Export to CSV
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    
    # Ensure reports directory exists
    reports_dir = Path('reports')
    reports_dir.mkdir(exist_ok=True)
    
    csv_filename = reports_dir / f'detailed_analysis_review_{timestamp}.csv'
    
    fieldnames = [
        'extension', 'type', 'status', 'status_reasoning', 'activity_level',
        'repository', 'repository_accessible', 'last_push_date', 'days_since_push',
        'docs_url', 'documentation_accessible', 'stars', 'language', 'description',
        'deprecation_score', 'deprecation_reasons'
    ]
    
    with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        
        for row in detailed_data:
            # Handle list fields
            if isinstance(row.get('deprecation_reasons'), list):
                row['deprecation_reasons'] = '; '.join(row['deprecation_reasons'])
            writer.writerow(row)
    
    print(f"✅ Detailed analysis exported to: {csv_filename}")
    print(f"📊 Total extensions analyzed: {len(detailed_data)}")
    
    # Show summary by status
    status_counts = {}
    for ext_data in detailed_data:
        status = ext_data['status']
        status_counts[status] = status_counts.get(status, 0) + 1
    
    print("\n📈 Status Distribution:")
    for status, count in sorted(status_counts.items()):
        print(f"  {status}: {count} extensions")
    
        print(f"\n🔍 Open the CSV file for detailed manual review:")
        print(f"  open {csv_filename}")
        
        return str(csv_filename)
    
    except Exception as e:
        print(f"❌ Error during analysis export: {e}")
        import traceback
        traceback.print_exc()
        return None


def _get_status_reasoning(ext, ext_type):
    """Generate human-readable reasoning for status classification."""
    reasons = []
    
    # Activity-based reasoning
    if ext.last_activity is not None:
        if ext_type == 'core':
            if ext.last_activity <= 7:
                reasons.append(f"Recent activity: {ext.last_activity} days ago (≤7 day threshold for core)")
            elif ext.last_activity <= 30:
                reasons.append(f"Moderate activity: {ext.last_activity} days ago (within 30 days)")
            else:
                reasons.append(f"Low activity: {ext.last_activity} days ago (>30 days)")
        else:  # community
            if ext.last_activity <= 30:
                reasons.append(f"Recent activity: {ext.last_activity} days ago (≤30 day threshold)")
            elif ext.last_activity <= 90:
                reasons.append(f"Moderate activity: {ext.last_activity} days ago (within 90 days)")
            elif ext.last_activity <= 365:
                reasons.append(f"Low activity: {ext.last_activity} days ago (within 1 year)")
            else:
                reasons.append(f"Very low activity: {ext.last_activity} days ago (>1 year)")
    else:
        reasons.append("Activity unknown: No commit data available")
    
    # Repository accessibility
    if not ext.repository:
        reasons.append("Repository URL missing or inaccessible")
    elif hasattr(ext, 'repository_error') and ext.repository_error:
        reasons.append(f"Repository access error: {ext.repository_error}")
    
    # Documentation accessibility
    if not ext.docs_url:
        reasons.append("Documentation URL missing")
    
    # Deprecation indicators (for community extensions)
    if hasattr(ext, 'deprecation_score') and ext.deprecation_score is not None:
        if ext.deprecation_score > 0.7:
            reasons.append(f"High deprecation score: {ext.deprecation_score:.2f}")
        elif ext.deprecation_score > 0.5:
            reasons.append(f"Moderate deprecation score: {ext.deprecation_score:.2f}")
    
    if hasattr(ext, 'deprecation_reasons') and ext.deprecation_reasons:
        reasons.append(f"Deprecation indicators: {', '.join(ext.deprecation_reasons[:3])}")
    
    # Default reasoning if no specific reasons found
    if not reasons:
        reasons.append("Status determined by default classification logic")
    
    return ' | '.join(reasons)


def _classify_activity(days_ago, ext_type):
    """Classify activity level based on days since last push."""
    if days_ago is None:
        return "Unknown"
    
    if ext_type == 'core':
        if days_ago <= 7:
            return "Very Active"
        elif days_ago <= 30:
            return "Active"
        elif days_ago <= 90:
            return "Moderate"
        else:
            return "Low"
    else:  # community
        if days_ago <= 7:
            return "Very Active"
        elif days_ago <= 30:
            return "Active"
        elif days_ago <= 90:
            return "Moderate"
        elif days_ago <= 365:
            return "Low"
        else:
            return "Inactive"


if __name__ == "__main__":
    asyncio.run(export_detailed_analysis())