#!/usr/bin/env python3

import os; import glob

# Adapt if needed
test_footage_mov = "/Volumes/Media/video/03_meta_test_footage/**/*"

# Find all movie files in the current directory
files = glob.glob('*.mp4') + \
    glob.glob('*.MP4') + \
    glob.glob('*.mov') + \
    glob.glob('*.MOV') + \
    glob.glob('*.mts') + \
    glob.glob('*.MTS')

# Delete each file
for file in files:
    os.remove(file)

# Copy files from test_footage_mov to current directory
for file in glob.glob(test_footage_mov, recursive=True):
    os.copy(file, "./")

# Remove txt files
txt_files = glob.glob('*.txt')
for file in txt_files:
    os.remove(file)
