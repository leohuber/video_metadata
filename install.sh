#!/bin/bash

# Check if the script has write permissions on the directory /usr/local/bin
if [ ! -w /usr/local/bin ]; then
    echo "Error: No write permissions for /usr/local/bin"
    echo "Please run this script with sudo"
    exit 1
fi

# Remove old files if they exist
if ls /usr/local/bin/video_* 1> /dev/null 2>&1; then
    rm -f /usr/local/bin/video_*
fi

# Copy new files
cp video_cleanup_metadata /usr/local/bin/
cp video_generate_metadata /usr/local/bin/
cp video_set_metadata /usr/local/bin/
cp video_slibrary_metadata_utils.py /usr/local/bin/
cp video_slibrary_print_utils.py /usr/local/bin/
cp video_date_util /usr/local/bin/
