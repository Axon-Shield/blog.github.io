#!/usr/bin/env python3

import os
import re
import glob

def fix_yaml_arrays(file_path):
    """Fix YAML array formatting in a Jekyll post file"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Fix the malformed YAML arrays
    # Replace patterns like "- item\n  - item" with proper YAML
    content = re.sub(
        r'categories:\n- ([^\n]+)\\n  - ([^\n]+)',
        r'categories:\n  - \1\n  - \2',
        content
    )
    
    content = re.sub(
        r'tags:\n- ([^\n]+)\\n  - ([^\n]+)',
        r'tags:\n  - \1\n  - \2',
        content
    )
    
    # Fix any remaining \n patterns in the content
    content = content.replace('\\n  - ', '\n  - ')
    content = content.replace('\\n', '\n')
    
    # Write back to file
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return True

def main():
    print("🔧 FIXING YAML ARRAY FORMATTING")
    print("===============================")
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
        
        if fix_yaml_arrays(file_path):
            print("   ✅ Fixed YAML formatting")
            processed += 1
        else:
            print("   ⚠️  No changes needed")
    
    print("")
    print(f"🎉 COMPLETED: Fixed YAML formatting in {processed} posts")
    print("")
    print("🔍 SAMPLE OF FIXED FRONT MATTER:")
    print("================================")
    
    # Show sample of fixed content
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
