#!/bin/bash

echo "Starting the script..."

# Movie file directory of movies to be copied
test_footage_mov="CHANGE_ME"

if [ "$test_footage_mov" == "CHANGE_ME" ]; then
    echo "Error: The variable 'test_footage_mov' is still set to 'CHANGE_ME'. Please set it to the directory with the test footage."
    exit 1
fi

# Remove the backup directory if it exists
backup_directory="./backup"
if [ -d "$backup_directory" ]; then
    echo "Removing backup directory: $backup_directory"
    rm -rf "$backup_directory"
else
    echo "No backup directory found to remove."
fi

file_extensions=("*.mp4" "*.MP4" "*.mov" "*.MOV" "*.mts" "*.MTS")
# Delete files with specified extensions in the current directory
for ext in "${file_extensions[@]}"; do
    find ./ -type f -name "$ext" -exec rm {} +
done

# Remove json and txt files in the current directory
rm -f ./*.json
rm -f ./*.txt

# Copy files from test_footage_mov to current directory
for ext in "${file_extensions[@]}"; do
    find "$test_footage_mov" -type f -name "$ext" -exec cp {} ./ \;
done

echo "Script completed."
