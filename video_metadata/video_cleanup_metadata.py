import glob
import os
from video_metadata.lib.video_slibrary_print_utils import print_green, print_red, print_blue

def cleanup_metadata_files(directory):
    print_green("Starting the cleanup process of metadata .json files ...")

    # Use glob to find all .json and .txt files in the specified directory
    all_files = glob.glob(os.path.join(directory, '*.json')) + glob.glob(os.path.join(directory, '*.txt'))
    print_green(f"Found {len(all_files)} .json and .txt files to remove.")

    # Loop through each file path found
    for file_path in all_files:
        print_green(f"Removing file: {file_path}")
        os.remove(file_path)

    print_green("Cleanup process completed.")
