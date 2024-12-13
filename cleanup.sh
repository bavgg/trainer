#!/bin/bash

# Define the directory to clean (current directory in this example)
TARGET_DIR="."

# Files and directories to exclude (wildcards are handled)
EXCEPTIONS=("train.py" "predict.py" "requirements.txt" "config.yaml" "cleanup.sh" "runs" "data/images/*.jpg" "data/labels/*.txt")

# Create a temporary file list of items to keep
KEEP_LIST=$(mktemp)
for pattern in "${EXCEPTIONS[@]}"; do
  find "$TARGET_DIR" -path "$TARGET_DIR/$pattern" >> "$KEEP_LIST" 2>/dev/null
done

# Convert the keep list into a grep-friendly pattern
KEEP_PATTERN=$(awk '{print "^" $0 "$"}' "$KEEP_LIST" | tr '\n' '|')
KEEP_PATTERN="${KEEP_PATTERN%|}" # Remove trailing '|'

# Remove all files/directories not in the keep list
find "$TARGET_DIR" -mindepth 1 -maxdepth 1 | grep -vE "$KEEP_PATTERN" | while read -r item; do
  echo "Removing: $item"
  rm -rf "$item"
done

# Clean up the temporary file
rm "$KEEP_LIST"

mkdir -p data/images data/labels

