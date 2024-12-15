import click
import sys
import shutil
from video_cleanup_metadata import cleanup_metadata_files
from video_date_util import print_dates_for_movies
from video_generate_metadata import generate_metadata_for_files
from lib.video_slibrary_print_utils import print_green, print_red, print_blue
from lib.video_slibrary_file_utils import expand_path_video

__version__ = "DEVELOPMENT_VERSION"

def error_exit(message: str) -> None:
    print_red(message)
    sys.exit(1)

@click.group()
@click.version_option(__version__)
def cli():
    # Check if the exiftool command is available in the system
    if shutil.which('exiftool') is None:
        error_exit("Exiftool command not found. Please install it before running this script.")
    pass

@cli.command()
@click.argument('directory', type=click.Path(exists=True, file_okay=False, dir_okay=True))
def cleanup_metadata(directory):
    """Cleanup metadata from a directory.
    
    DIRECTORY is the directory where the metadata files are located.
    """
    cleanup_metadata_files(directory)

@cli.command()
@click.argument('paths', nargs=-1, type=click.Path(exists=True, file_okay=True, dir_okay=True))
def print_dates(paths):
    """Print dates from video files in a directory.
    
    PATHS is the directory or file path where the video files are located. Only .mp4 and .mov files are allowed."""
    for path in paths:
        files = expand_path_video(path)
        if files:
            print_dates_for_movies(files)


@cli.command()
@click.argument('paths', nargs=-1, type=click.Path(exists=True, file_okay=True, dir_okay=True))
def generate(paths):
    """Generate metadata templates from video files provided.
    
    PATHS is the directory or file path where the video files are located. Only .mp4 and .mov files are allowed."""
    for path in paths:
        files = expand_path_video(path)
        if files:
            generate_metadata_for_files(files)

if __name__ == '__main__':
    cli()