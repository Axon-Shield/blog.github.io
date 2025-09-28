#!/usr/bin/env python3

import os
from PIL import Image, ImageDraw, ImageFont
import textwrap

def create_placeholder_image(width, height, text, output_path):
    """Create a placeholder image with text"""
    # Create image with light gray background
    img = Image.new('RGB', (width, height), color='#f0f0f0')
    draw = ImageDraw.Draw(img)
    
    # Try to use a default font, fallback to basic if not available
    try:
        font = ImageFont.truetype("/System/Library/Fonts/Arial.ttf", 24)
    except:
        try:
            font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 24)
        except:
            font = ImageFont.load_default()
    
    # Wrap text to fit image width
    wrapped_text = textwrap.fill(text, width=30)
    
    # Get text bounding box
    bbox = draw.textbbox((0, 0), wrapped_text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    
    # Center the text
    x = (width - text_width) // 2
    y = (height - text_height) // 2
    
    # Draw text
    draw.text((x, y), wrapped_text, fill='#666666', font=font)
    
    # Save image
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    img.save(output_path, 'JPEG', quality=85)
    
    return True

def main():
    print("🖼️  CREATING PLACEHOLDER IMAGES FOR MISSING FILES")
    print("===============================================")
    print("")
    
    # Read the missing image paths
    with open('/tmp/image_paths.txt', 'r') as f:
        image_paths = [line.strip() for line in f.readlines()]
    
    created_count = 0
    
    for i, image_path in enumerate(image_paths):
        local_path = f"/Users/dancvrcek/my-jekyll-site{image_path}"
        
        # Skip if file already exists
        if os.path.exists(local_path):
            print(f"[{i+1}/{len(image_paths)}] ✅ Already exists: {image_path}")
            continue
        
        print(f"[{i+1}/{len(image_paths)}] 🎨 Creating placeholder: {image_path}")
        
        # Extract meaningful text from path
        filename = os.path.basename(image_path)
        name_without_ext = os.path.splitext(filename)[0]
        display_text = name_without_ext.replace('-', ' ').replace('_', ' ').title()
        
        # Create placeholder image
        if create_placeholder_image(800, 600, display_text, local_path):
            print(f"   ✅ Created: {local_path}")
            created_count += 1
        else:
            print(f"   ❌ Failed to create: {local_path}")
    
    print("")
    print(f"🎉 COMPLETED: Created {created_count} placeholder images")
    print("")
    print("📝 NEXT STEPS:")
    print("1. These are placeholder images with text")
    print("2. You can replace them with actual images later")
    print("3. Images are sized 800x600 pixels")
    print("4. All images are saved as JPEG format")

if __name__ == "__main__":
    main()
