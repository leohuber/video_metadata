#!/bin/bash

# Adapat if needed
test_footage="/Volumes/Media/video/03_test_footage/mp4/*"

rm -f *.mp4
rm -f *.txt

cp $test_footage ./
