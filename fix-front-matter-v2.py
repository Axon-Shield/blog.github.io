#!/usr/bin/env python3

import os
import re
import glob

def fix_front_matter(file_path):
    """Fix front matter in a Jekyll post file"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Split into front matter and content
    if not content.startswith('---'):
        return False
    
    parts = content.split('---', 2)
    if len(parts) < 3:
        return False
    
    front_matter = parts[1].strip()
    post_content = parts[2]
    
    # Parse front matter lines
    lines = front_matter.split('\n')
    new_lines = []
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
            
        # Skip original_url and author lines
        if line.startswith('original_url:') or line.startswith('author:'):
            continue
            
        # Convert categories from [array] to YAML array
        if line.startswith('categories: ['):
            # Extract the array content
            match = re.match(r'categories: \[(.*)\]', line)
            if match:
                items = [item.strip() for item in match.group(1).split(',')]
                new_lines.append('categories:')
                for item in items:
                    new_lines.append(f'  - {item}')
            continue
            
        # Convert tags from [array] to YAML array
        if line.startswith('tags: ['):
            # Extract the array content
            match = re.match(r'tags: \[(.*)\]', line)
            if match:
                items = [item.strip() for item in match.group(1).split(',')]
                new_lines.append('tags:')
                for item in items:
                    new_lines.append(f'  - {item}')
            continue
            
        # Keep other lines as-is
        new_lines.append(line)
    
    # Reconstruct the file
    new_front_matter = '\n'.join(new_lines)
    new_content = f"---\n{new_front_matter}\n---{post_content}"
    
    # Write back to file
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    return True

def main():
    print("🔧 FIXING FRONT MATTER IN ALL BLOG POSTS (V2)")
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
        
        # Create backup
        backup_path = file_path + '.bak'
        if not os.path.exists(backup_path):
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            with open(backup_path, 'w', encoding='utf-8') as f:
                f.write(content)
        
        # Fix the front matter
        if fix_front_matter(file_path):
            print("   ✅ Fixed front matter")
            processed += 1
        else:
            print("   ⚠️  No changes needed or error")
    
    print("")
    print(f"🎉 COMPLETED: Fixed front matter in {processed} posts")
    print("📁 Backups created with .bak extension")
    print("")
    print("🔍 SAMPLE OF FIXED FRONT MATTER:")
    print("================================")
    
    # Show sample of fixed content
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
