#!/bin/bash

# Adapat if needed
test_footage_mov="/Volumes/Media/video/03_test_footage/**/*"

rm -f *.MP4
rm -f *.mp4
rm -f *.mov
rm -f *.MOV
rm -f *.mts
rm -f *.MTS

cp $test_footage_mov ./

# Remove txt files
rm -f *.txt
