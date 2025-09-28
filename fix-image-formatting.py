#!/usr/bin/env python3

import os
import re
import glob

def fix_image_formatting(file_path):
    """Fix image formatting to match nexus post exactly"""
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
    
    # Find the image markdown in the content
    image_match = re.search(r'!\[([^\]]*)\]\(([^)]+)\)', post_content)
    if not image_match:
        return False
    
    alt_text = image_match.group(1)
    image_path = image_match.group(2)
    
    # Remove the existing image from content
    post_content = re.sub(r'!\[([^\]]*)\]\(([^)]+)\)\n*', '', post_content)
    
    # Create proper formatting like nexus post
    # 1. Empty line after front matter
    # 2. Image on its own line
    # 3. Caption in italics (extracted from alt text)
    # 4. Empty line after caption
    
    # Create a nice caption from the alt text
    caption = alt_text.replace('-', ' ').replace('_', ' ').title()
    
    # Format the image section exactly like nexus post
    image_section = f"\n![{alt_text}]({image_path})\n*{caption}*\n\n"
    
    # Add the formatted image section at the beginning of content
    new_content = image_section + post_content
    
    # Reconstruct the file
    new_content = f"---\n{front_matter}\n---{new_content}"
    
    # Write back to file
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    return True

def main():
    print("🔧 FIXING IMAGE FORMATTING TO MATCH NEXUS POST")
    print("==============================================")
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
        
        if fix_image_formatting(file_path):
            print("   ✅ Fixed image formatting")
            processed += 1
        else:
            print("   ⚠️  No changes needed or error")
    
    print("")
    print(f"🎉 COMPLETED: Fixed image formatting in {processed} posts")
    print("")
    print("🔍 SAMPLE OF UPDATED FORMAT:")
    print("============================")
    
    # Show sample of updated content
    sample_file = "/Users/dancvrcek/my-jekyll-site/_posts/2025-09-10-we-forget-that-cyber-defense-is-hard-apologies.md"
    if os.path.exists(sample_file):
        with open(sample_file, 'r', encoding='utf-8') as f:
            content = f.read()
            # Show first 20 lines
            lines = content.split('\n')
            for i, line in enumerate(lines[:20]):
                print(f"{i+1:2d}| {line}")

if __name__ == "__main__":
    main()
