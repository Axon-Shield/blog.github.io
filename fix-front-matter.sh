#!/bin/bash

# Script to fix front matter in all Jekyll posts
# - Remove original_url and author fields
# - Convert categories and tags to proper YAML format

echo "🔧 FIXING FRONT MATTER IN ALL BLOG POSTS"
echo "========================================"
echo ""

# Counter for processed files
processed=0
total=$(ls -1 /Users/dancvrcek/my-jekyll-site/_posts/*.md | wc -l | tr -d ' ')

echo "📊 Processing $total blog posts..."
echo ""

for post in /Users/dancvrcek/my-jekyll-site/_posts/*.md; do
    filename=$(basename "$post")
    echo "📝 Processing: $filename"
    
    # Create backup
    cp "$post" "$post.bak"
    
    # Use sed to fix the front matter
    # 1. Remove original_url line
    # 2. Remove author line  
    # 3. Convert categories from [array] to YAML array format
    # 4. Convert tags from [array] to YAML array format
    
    sed -i '' \
        -e '/^original_url:/d' \
        -e '/^author:/d' \
        -e 's/^categories: \[\(.*\)\]/categories:\n  - \1/' \
        -e 's/^tags: \[\(.*\)\]/tags:\n  - \1/' \
        -e 's/, /\\n  - /g' \
        "$post"
    
    # Clean up any remaining comma issues in the YAML arrays
    sed -i '' \
        -e '/^  - /s/, /\\n  - /g' \
        "$post"
    
    processed=$((processed + 1))
    echo "   ✅ Fixed front matter"
done

echo ""
echo "🎉 COMPLETED: Fixed front matter in $processed posts"
echo "📁 Backups created with .bak extension"
echo ""
echo "🔍 SAMPLE OF FIXED FRONT MATTER:"
echo "================================"
head -15 /Users/dancvrcek/my-jekyll-site/_posts/2025-09-10-we-forget-that-cyber-defense-is-hard-apologies.md
