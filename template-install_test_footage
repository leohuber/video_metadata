#!/usr/bin/env python3

import os
import glob

print("Starting the script...")

# Movie file directory of movies to be copied
test_footage_mov = "/Volumes/Media/video/03_meta_test_footage/**/*"

# File extensions to delete
file_extensions = ['*.mp4', '*.MP4', '*.mov', '*.MOV', '*.mts', '*.MTS']

print("Searching for movie files with extensions: " + ", ".join(file_extensions))
files = []
for ext in file_extensions:
    files.extend(glob.glob(ext))

# Delete each file
print(f"Found {len(files)} movie files. Deleting them...")
for file in files:
    os.remove(file)

# Copy files from test_footage_mov to current directory
print("Copying test footage from: " + test_footage_mov)
for file in glob.glob(test_footage_mov, recursive=True):
    os.copy(file, "./")

# Remove txt files
print("Removing all .txt files in the current directory...")
txt_files = glob.glob('*.txt')
for file in txt_files:
    os.remove(file)