import os
from lib.video_slibrary_print_utils import print_green, print_red, print_blue

def print_dates(movie_files):
    for movie_file in movie_files:
        print_green(f"Getting dates for video file: {movie_file}")
        os.system(f'exiftool -G0:1 -s -time:all "{movie_file}"')
