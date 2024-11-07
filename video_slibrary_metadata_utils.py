# FILE: metadata_utils.py

import subprocess

def get_date_created_and_identifier(video_file, extension, model):
    DATE_CREATED = None
    IDENTIFIER = None

    # Check if we are processing a QuickTime container
    if extension == "mov":
        # Try to get CreationDate
        datec = subprocess.getoutput(f"exiftool -q -q -b -api largefilesupport=1 -CreationDate '{video_file}'")
        if datec:
            DATE_CREATED = datec
            IDENTIFIER = DATE_CREATED[:19].replace(' ', '_').replace(':', '')
        else:
            # Try to get CreateDate
            datec = subprocess.getoutput(f"exiftool -q -q -b -api largefilesupport=1 -CreateDate '{video_file}'")
            if datec:
                DATE_CREATED = datec
                IDENTIFIER = DATE_CREATED[:19].replace(' ', '_').replace(':', '')

    # Check if we are processing an MP4 container
    if extension == "mp4":
        if model == "Canon EOS R6":
            # Get SubSecCreateDate for Canon R6
            datec = subprocess.getoutput(f"exiftool -q -q -b -api largefilesupport=1 -SubSecCreateDate '{video_file}'")
            if datec:
                DATE_CREATED = datec
                IDENTIFIER = DATE_CREATED[:19].replace(' ', '_').replace(':', '')
        else:
            # Try to get CreateDate
            datec = subprocess.getoutput(f"exiftool -q -q -b -api largefilesupport=1 -CreateDate '{video_file}'")
            if datec:
                DATE_CREATED = datec
                IDENTIFIER = DATE_CREATED[:19].replace(' ', '_').replace(':', '')

    return DATE_CREATED, IDENTIFIER