#!/usr/bin/env python3
"""
Script to extract publication dates from AxonShield blog posts
Usage: python3 extract-dates.py
"""

import requests
from bs4 import BeautifulSoup
from datetime import datetime
import time
import sys

# Blog posts that need date extraction (still have 2025-09-28)
BLOG_POSTS = [
    ("beyond-the-dashboard-why-your-soc-needs-a-human-centered-command-center", "https://axonshield.com/beyond-the-dashboard-why-your-soc-needs-a-human-centered-command-center"),
    ("bridging-the-cyber-talent-gap-with-axon-shield-support", "https://axonshield.com/bridging-the-cyber-talent-gap-with-axon-shield-support"),
    ("building-cyber-service", "https://axonshield.com/building-cyber-service"), 
    ("cost-benefit-analysis-and-tco-of-waf-deployment-models", "https://axonshield.com/cost-benefit-analysis-and-tco-of-waf-deployment-models"),
    ("cyber-defense-strategy-aligning-security-with-business-objectives", "https://axonshield.com/cyber-defense-strategy-aligning-security-with-business-objectives"),
    ("data-driven-strategy-dns-security-analysis", "https://axonshield.com/data-driven-strategy-dns-security-analysis"),
    ("deep-dive-into-dns-the-internets-super-smart-address-book", "https://axonshield.com/deep-dive-into-dns-the-internets-super-smart-address-book"),
    ("dns-at-the-edge-performance-security-and-strategic-advantage", "https://axonshield.com/dns-at-the-edge-performance-security-and-strategic-advantage"),
    ("dns-resiliency-and-first-step-to-transform-your-cyber-defense", "https://axonshield.com/dns-resiliency-and-first-step-to-transform-your-cyber-defense"),
    ("from-hoststxt-to-modern-internet-infrastructure", "https://axonshield.com/from-hoststxt-to-modern-internet-infrastructure"),
    ("from-walled-garden-to-axon-fusion-zone", "https://axonshield.com/from-walled-garden-to-axon-fusion-zone"),
    ("how-we-designed-automated-certificate-lifecycle-management-20-years-of-iteration", "https://axonshield.com/how-we-designed-automated-certificate-lifecycle-management-20-years-of-iteration"),
    ("prevent-v-detect-it-is-all-about-effort-i-mean-ai", "https://axonshield.com/prevent-v-detect-it-is-all-about-effort-i-mean-ai"),
    ("reclaim-control-over-your-cyber-defense-empowerment-over-fear", "https://axonshield.com/reclaim-control-over-your-cyber-defense-empowerment-over-fear"),
    ("the-business-case-for-modern-certificate-lifecycle-management", "https://axonshield.com/the-business-case-for-modern-certificate-lifecycle-management"),
    ("the-convergence-of-cyber-security-origins-of-axon-shield", "https://axonshield.com/the-convergence-of-cyber-security-origins-of-axon-shield-from-technical-experts-to-efficient-delivery-of-cyber-security"),
    ("the-science-of-digital-fingerprinting-for-waf-integration", "https://axonshield.com/the-science-of-digital-fingerprinting-for-waf-integration"),
    ("waf-for-microservices-and-serverless-mastering-accuracy-in-modern-architectures", "https://axonshield.com/waf-for-microservices-and-serverless-mastering-accuracy-in-modern-architectures"),
    ("we-forget-that-cyber-defense-is-hard-apologies", "https://axonshield.com/we-forget-that-cyber-defense-is-hard-apologies")
]

def extract_date_from_page(url):
    """Extract publication date from AxonShield blog post page"""
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Try multiple selectors to find the date
        date_selectors = [
            'span.blog-list-item-date',
            '.blog-list-item-date',
            '[class*="date"]',
            'time',
            '.published',
            '.post-date',
            '.entry-date'
        ]
        
        for selector in date_selectors:
            elements = soup.select(selector)
            for element in elements:
                date_text = element.get_text().strip()
                if date_text and len(date_text) > 3:  # Basic validation
                    return date_text
        
        return None
        
    except Exception as e:
        print(f"Error extracting date from {url}: {e}")
        return None

def convert_date_to_jekyll_format(date_str):
    """Convert various date formats to YYYY-MM-DD"""
    if not date_str:
        return None
    
    # Clean up the date string
    date_str = date_str.strip()
    
    # Try different date formats
    formats = [
        '%m/%d/%Y',      # 5/3/2025
        '%m/%d/%y',      # 5/3/25
        '%B %d, %Y',     # May 3, 2025
        '%b %d, %Y',     # May 3, 2025
        '%Y-%m-%d',      # 2025-05-03
        '%d/%m/%Y',      # 3/5/2025 (day/month/year)
    ]
    
    for fmt in formats:
        try:
            parsed_date = datetime.strptime(date_str, fmt)
            return parsed_date.strftime('%Y-%m-%d')
        except ValueError:
            continue
    
    return None

def main():
    print("🔍 Extracting publication dates from AxonShield blog posts...")
    print("=" * 70)
    
    results = []
    found_dates = 0
    
    for i, (post_slug, url) in enumerate(BLOG_POSTS, 1):
        print(f"\n[{i}/{len(BLOG_POSTS)}] {post_slug}")
        print(f"URL: {url}")
        
        date = extract_date_from_page(url)
        jekyll_date = convert_date_to_jekyll_format(date) if date else None
        
        if jekyll_date:
            print(f"✅ Found date: {date} → {jekyll_date}")
            results.append((post_slug, jekyll_date))
            found_dates += 1
        else:
            print(f"❌ No date found")
            results.append((post_slug, None))
        
        # Be respectful to the server
        time.sleep(2)
    
    # Print summary
    print("\n" + "=" * 70)
    print(f"📊 SUMMARY: Found dates for {found_dates}/{len(BLOG_POSTS)} posts")
    print("=" * 70)
    print("\n🚀 Copy and run these commands to update your posts:")
    print("-" * 50)
    
    for post_slug, jekyll_date in results:
        if jekyll_date:
            print(f'./update-date.sh "{post_slug}" "{jekyll_date}"')
        else:
            print(f'# ❌ No date found for: {post_slug}')
    
    print(f"\n✅ Ready to update {found_dates} posts!")

if __name__ == "__main__":
    # Check if required packages are available
    try:
        import requests
        from bs4 import BeautifulSoup
    except ImportError:
        print("❌ Required packages not found. Install with:")
        print("pip install requests beautifulsoup4")
        sys.exit(1)
    
    main()