#!/usr/bin/env python3

import os
import re
import glob

def update_image_format(file_path):
    """Update image format to match nexus post style"""
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
    
    # Extract image path from front matter
    image_path = None
    lines = front_matter.split('\n')
    new_lines = []
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
            
        # Check if this is an image line
        if line.startswith('image:'):
            image_path = line.split('image:')[1].strip()
            # Skip this line (remove it from front matter)
            continue
        else:
            new_lines.append(line)
    
    # If we found an image path, add it to the content
    if image_path:
        # Extract filename for alt text
        filename = os.path.basename(image_path)
        name_without_ext = os.path.splitext(filename)[0]
        # Create a nice alt text from the filename
        alt_text = name_without_ext.replace('-', ' ').replace('_', ' ').title()
        
        # Add image at the beginning of content
        image_markdown = f"![{alt_text}]({image_path})\n"
        post_content = image_markdown + post_content
    
    # Reconstruct the file
    new_front_matter = '\n'.join(new_lines)
    new_content = f"---\n{new_front_matter}\n---{post_content}"
    
    # Write back to file
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    return True

def main():
    print("🔧 UPDATING IMAGE FORMAT TO MATCH NEXUS POST")
    print("=============================================")
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
        
        if update_image_format(file_path):
            print("   ✅ Updated image format")
            processed += 1
        else:
            print("   ⚠️  No changes needed or error")
    
    print("")
    print(f"🎉 COMPLETED: Updated image format in {processed} posts")
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
