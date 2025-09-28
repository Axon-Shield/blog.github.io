#!/usr/bin/env python3

import os
import re
import glob
from datetime import datetime

def update_date_format(file_path):
    """Update date format to include time component"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if file has front matter
    if not content.startswith('---'):
        return False
    
    # Split into front matter and content
    parts = content.split('---', 2)
    if len(parts) < 3:
        return False
    
    front_matter = parts[1].strip()
    post_content = parts[2]
    
    # Parse and update the date line
    lines = front_matter.split('\n')
    new_lines = []
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
            
        # Check if this is a date line with just YYYY-MM-DD format
        if line.startswith('date: ') and re.match(r'date: \d{4}-\d{2}-\d{2}$', line):
            # Extract the date
            date_str = line.split('date: ')[1]
            # Convert to ISO format with time and timezone
            new_date = f"{date_str}T05:00:00-04:00"
            new_lines.append(f"date: {new_date}")
        else:
            new_lines.append(line)
    
    # Reconstruct the file
    new_front_matter = '\n'.join(new_lines)
    new_content = f"---\n{new_front_matter}\n---{post_content}"
    
    # Write back to file
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    return True

def main():
    print("🔧 UPDATING DATE FORMAT TO INCLUDE TIME")
    print("======================================")
    print("")
    
    # Find all markdown files in _posts
    posts_dir = "/Users/dancvrcek/my-jekyll-site/_posts"
    md_files = glob.glob(os.path.join(posts_dir, "*.md"))
    
    print(f"📊 Processing {len(md_files)} blog posts...")
    print("")
    
    processed = 0
    for file_path in md_files:
        filename = os.path.basename(file_path)
        print(f"📝 Processing: {filename}")
        
        if update_date_format(file_path):
            print("   ✅ Updated date format")
            processed += 1
        else:
            print("   ⚠️  No changes needed or error")
    
    print("")
    print(f"🎉 COMPLETED: Updated date format in {processed} posts")
    print("")
    print("🔍 SAMPLE OF UPDATED DATE FORMAT:")
    print("=================================")
    
    # Show sample of updated content
    sample_file = "/Users/dancvrcek/my-jekyll-site/_posts/2025-09-10-we-forget-that-cyber-defense-is-hard-apologies.md"
    if os.path.exists(sample_file):
        with open(sample_file, 'r', encoding='utf-8') as f:
            content = f.read()
            # Show first 15 lines
            lines = content.split('\n')
            for i, line in enumerate(lines[:15]):
                print(f"{i+1:2d}| {line}")

if __name__ == "__main__":
    main()
