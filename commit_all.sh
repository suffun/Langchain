#!/bin/bash

set -e

echo "Checking for uncommitted files..."

# Get all modified/untracked files
files=$(git status --porcelain | awk '{print substr($0,4)}')

if [ -z "$files" ]; then
    echo "No uncommitted files found."
    exit 0
fi

while IFS= read -r file; do

    echo ""
    echo "======================================"
    echo "Processing: $file"
    echo "======================================"

    # Stage only this file
    git add -- "$file"

    # Create a meaningful commit message based on the filename
    filename=$(basename "$file")
    name="${filename%.*}"

    case "$name" in
        text_loader)
            message="Add text document loader"
            ;;
        pdf_loader)
            message="Add PDF document loader"
            ;;
        directory_loader)
            message="Add directory document loader"
            ;;
        webBase_loader)
            message="Add web document loader"
            ;;
        CSV_loader)
            message="Add CSV document loader"
            ;;
        lazy_loader)
            message="Add lazy document loader"
            ;;
        cricket_players)
            message="Add cricket player dataset"
            ;;
        *)
            message="Add $filename"
            ;;
    esac

    echo "Committing: $message"

    git commit -m "$message"

    echo "Pushing $filename..."

    git push

    echo "Done: $filename"

done <<< "$files"

echo ""
echo "======================================"
echo "All files committed and pushed!"
echo "======================================"