#!/bin/bash

# Adapat if needed
test_footage="/Volumes/Media/video/03_test_footage/quicktime/*"

rm -f *.mov
rm -f *.mts
rm -f *.txt

cp $test_footage ./
