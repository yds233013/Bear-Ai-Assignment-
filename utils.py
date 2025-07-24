"""
Utility functions for Bear AI Assignment
Helper functions used across the project.
"""

import re
from datetime import datetime

def count_brand_mentions(text, brands):
    """Count how many times each brand is mentioned in the text"""
    counts = {brand: 0 for brand in brands}
    
    # Case-insensitive search for brand mentions
    for brand in brands:
        # Use regex to find whole word matches
        pattern = r'\b' + re.escape(brand) + r'\b'
        matches = re.findall(pattern, text, re.IGNORECASE)
        counts[brand] = len(matches)
    
    return counts

def create_result_entry(prompt_id, prompt, response, brand_counts):
    """Create a standardized result entry"""
    return {
        'prompt_id': prompt_id,
        'prompt': prompt,
        'response_length': len(response),
        'brand_mentions': brand_counts,
        'timestamp': datetime.now().isoformat()
    }

def print_summary(results, brands):
    """Print a summary of the scraping results"""
    print(f"\n🎯 Summary:")
    print(f"Total prompts processed: {len(results)}")
    
    total_mentions = {brand: 0 for brand in brands}
    for result in results:
        for brand, count in result['brand_mentions'].items():
            total_mentions[brand] += count
    
    print(f"Total brand mentions:")
    for brand, count in total_mentions.items():
        print(f"  {brand}: {count}") 