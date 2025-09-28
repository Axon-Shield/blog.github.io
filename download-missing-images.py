#!/usr/bin/env python3

import os
import requests
import re
from urllib.parse import urljoin, urlparse
from bs4 import BeautifulSoup

def get_original_url_from_slug(slug):
    """Get the original AxonShield URL for a post slug"""
    return f"https://axonshield.com/{slug}"

def extract_images_from_page(url):
    """Extract image URLs from a webpage"""
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        
        images = []
        # Look for img tags
        for img in soup.find_all('img'):
            src = img.get('src')
            if src:
                # Convert relative URLs to absolute
                if src.startswith('/'):
                    src = urljoin(url, src)
                images.append(src)
        
        return images
    except Exception as e:
        print(f"Error extracting images from {url}: {e}")
        return []

def download_image(image_url, local_path):
    """Download an image from URL to local path"""
    try:
        # Create directory if it doesn't exist
        os.makedirs(os.path.dirname(local_path), exist_ok=True)
        
        response = requests.get(image_url, timeout=30)
        response.raise_for_status()
        
        with open(local_path, 'wb') as f:
            f.write(response.content)
        
        print(f"✅ Downloaded: {local_path}")
        return True
    except Exception as e:
        print(f"❌ Failed to download {image_url}: {e}")
        return False

def main():
    print("🔍 DOWNLOADING MISSING IMAGES FROM ORIGINAL AXONSHIELD POSTS")
    print("============================================================")
    print("")
    
    # Read the image paths we need
    with open('/tmp/image_paths.txt', 'r') as f:
        image_paths = [line.strip() for line in f.readlines()]
    
    # Get all post slugs from filenames
    posts_dir = "/Users/dancvrcek/my-jekyll-site/_posts"
    post_files = [f for f in os.listdir(posts_dir) if f.endswith('.md')]
    
    # Extract slugs from filenames (remove date prefix)
    slugs = []
    for post_file in post_files:
        if post_file.startswith('2024-') or post_file.startswith('2025-'):
            # Remove date prefix and .md extension
            slug = post_file.split('-', 3)[3].replace('.md', '')
            slugs.append(slug)
    
    print(f"📊 Found {len(slugs)} posts to check for images")
    print("")
    
    downloaded_count = 0
    total_images = len(image_paths)
    
    for i, image_path in enumerate(image_paths):
        local_path = f"/Users/dancvrcek/my-jekyll-site{image_path}"
        
        # Skip if file already exists
        if os.path.exists(local_path):
            print(f"[{i+1}/{total_images}] ✅ Already exists: {image_path}")
            continue
        
        print(f"[{i+1}/{total_images}] 🔍 Looking for: {image_path}")
        
        # Try to find the original post for this image
        found = False
        for slug in slugs:
            original_url = get_original_url_from_slug(slug)
            print(f"   Checking: {original_url}")
            
            # Extract images from the page
            page_images = extract_images_from_page(original_url)
            
            # Look for a matching image
            for page_image in page_images:
                # Check if this image might match our path
                if any(keyword in page_image.lower() for keyword in image_path.lower().split('/')[-1].split('-')):
                    print(f"   🎯 Found potential match: {page_image}")
                    if download_image(page_image, local_path):
                        downloaded_count += 1
                        found = True
                        break
            
            if found:
                break
        
        if not found:
            print(f"   ❌ Could not find source for: {image_path}")
    
    print("")
    print(f"🎉 COMPLETED: Downloaded {downloaded_count} missing images")
    print(f"📊 Total images processed: {total_images}")

if __name__ == "__main__":
    main()
