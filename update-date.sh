#!/bin/bash

# Script to update blog post dates
# Usage: ./update-date.sh "post-filename-without-extension" "YYYY-MM-DD"

if [ $# -ne 2 ]; then
    echo "Usage: $0 <post-filename-without-extension> <new-date-YYYY-MM-DD>"
    echo "Example: $0 'cyber-defense-strategy-aligning-security-with-business-objectives' '2025-03-15'"
    exit 1
fi

POST_NAME="$1"
NEW_DATE="$2"

# Find the post file (it might have any date prefix)
POST_FILE=$(find _posts/ -name "*${POST_NAME}.md" | head -1)

if [ -z "$POST_FILE" ]; then
    echo "Error: Could not find post file for '$POST_NAME'"
    exit 1
fi

echo "Found post: $POST_FILE"

# Extract the old date prefix from filename
OLD_DATE_PREFIX=$(basename "$POST_FILE" | grep -o '^[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]')
echo "Old date prefix: $OLD_DATE_PREFIX"

# Create new filename
NEW_FILENAME="_posts/${NEW_DATE}-${POST_NAME}.md"
echo "New filename: $NEW_FILENAME"

# Update the date in the front matter
sed -i.bak "s/^date: [0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]/date: $NEW_DATE/" "$POST_FILE"

# Rename the file if the date changed
if [ "$POST_FILE" != "$NEW_FILENAME" ]; then
    mv "$POST_FILE" "$NEW_FILENAME"
    echo "Renamed file from $POST_FILE to $NEW_FILENAME"
fi

echo "Updated date to $NEW_DATE"
echo "Backup created as ${POST_FILE}.bak"
