#!/usr/bin/env python3

import os
import re
import glob

def remove_layout_lines(file_path):
    """Remove layout lines from Jekyll post front matter"""
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
    
    # Parse and remove layout lines
    lines = front_matter.split('\n')
    new_lines = []
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
            
        # Skip layout lines
        if line.startswith('layout:'):
            continue
            
        # Keep all other lines
        new_lines.append(line)
    
    # Reconstruct the file
    new_front_matter = '\n'.join(new_lines)
    new_content = f"---\n{new_front_matter}\n---{post_content}"
    
    # Write back to file
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    return True

def main():
    print("🔧 REMOVING LAYOUT LINES FROM ALL BLOG POSTS")
    print("============================================")
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
        
        if remove_layout_lines(file_path):
            print("   ✅ Removed layout line")
            processed += 1
        else:
            print("   ⚠️  No changes needed or error")
    
    print("")
    print(f"🎉 COMPLETED: Removed layout lines from {processed} posts")
    print("")
    print("🔍 SAMPLE OF UPDATED FRONT MATTER:")
    print("=================================")
    
    # Show sample of updated content
    sample_file = "/Users/dancvrcek/my-jekyll-site/_posts/2025-05-28-the-science-of-digital-fingerprinting-for-waf-integration.md"
    if os.path.exists(sample_file):
        with open(sample_file, 'r', encoding='utf-8') as f:
            content = f.read()
            # Show first 15 lines
            lines = content.split('\n')
            for i, line in enumerate(lines[:15]):
                print(f"{i+1:2d}| {line}")

if __name__ == "__main__":
    main()
