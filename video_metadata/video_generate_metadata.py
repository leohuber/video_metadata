import os
import shutil
import sys
import json
from lib.video_slibrary_print_utils import print_green, print_red, print_blue
from lib.video_slibrary_metadata_utils import (
    get_metadata_all, generate_codec_info, get_date_created_and_identifier,
    get_make, get_model, get_source_image_height, get_source_image_width,
    get_video_frame_rate, get_compressor_name, get_gps, get_country_code,
    get_country, get_creator, get_state, get_city, get_sublocation,
    get_headline, get_title_suffix, get_description, get_copyright
)

VERSION = "DEVELOPMENT_VERSION"

# Check if the first argument is -v or --version
if len(sys.argv) > 1 and sys.argv[1] in ('-v', '--version'):
    print(f"{VERSION}")
    sys.exit(0)

def error_exit(message: str) -> None:
    print_red(message)
    sys.exit(1)

def check_file_exists(filename: str) -> None:
    if not os.path.exists(filename):
        error_exit(f"Could not find file: {filename}")

def generate_metadata(video_file: str) -> None:
    print_green(f"Processing file: {video_file}")

    # Check if video file exists
    check_file_exists(video_file)

    # Extract file extension
    extension = os.path.splitext(video_file)[1][1:].lower()

    date_created, identifier = get_date_created_and_identifier(video_file, extension)
    if date_created is None or identifier is None:
        error_exit("date_created or identifier is None. Exiting.")

    # Check if the file extension is either mov or mp4
    if extension not in ["mov", "mp4"]:
        error_exit(f"Unsupported file extension: {extension}. Only 'mov' and 'mp4' files are allowed.")
    
    # Rename the file to the identifier
    destination_file = f"{identifier}.{extension}"
    if os.path.abspath(video_file) != os.path.abspath(destination_file):
        os.rename(video_file, destination_file)
        video_file = destination_file

    # Meta data file names
    meta_file = f"{os.path.splitext(video_file)[0]}_meta.json"
    meta_all_file = f"{os.path.splitext(video_file)[0]}_meta_all.txt"

    metadata_fields = {
        "IDENTIFIER": identifier,
        "DATE_CREATED": date_created,
        "MAKE": get_make(video_file),
        "MODEL": get_model(video_file),
        "SOURCE_IMAGE_HEIGHT": get_source_image_height(video_file),
        "SOURCE_IMAGE_WIDTH": get_source_image_width(video_file),
        "VIDEO_FRAME_RATE": get_video_frame_rate(video_file),
        "COMPRESSOR_NAME": get_compressor_name(video_file),
        "GPS": get_gps(video_file),
        "CREATOR": get_creator(video_file),
        "COUNTRY_CODE": get_country_code(video_file),
        "COUNTRY": get_country(video_file),
        "STATE": get_state(video_file),
        "CITY": get_city(video_file),
        "SUBLOCATION": get_sublocation(video_file),
        "HEADLINE": get_headline(video_file),
        "TITLE_SUFFIX": get_title_suffix(video_file),
        "DESCRIPTION": get_description(video_file),
        "COPYRIGHT": get_copyright(video_file),
    }

    metadata = {}
    for key, value in metadata_fields.items():
        if value:
            metadata[key] = value
        else:
            print_green(f"Skipping {key} as it has no value.")

    codec_info = generate_codec_info(video_file)
    metadata['CODEC_INFO'] = codec_info

    # Write metadata to a JSON file
    with open(meta_file, 'w') as f:
        json.dump(metadata, f, indent=4)

    # Write all metadata to a text file
    meta_data_all = get_metadata_all(video_file)
    with open(meta_all_file, 'w') as f:
        f.write(meta_data_all)

    meta_file_zzz = "zzz_meta_data_template.json"
    if not os.path.exists(meta_file_zzz):
        meta_data = {
            "MAKE": "Canon - DEFAULT",
            "MODEL": "Canon EOS R6 - DEFAULT",
            "GPS": "-35.2975906, 149.1012676, 554 - DEFAULT",
            "CREATOR": "Leo Huber - DEFAULT",
            "COUNTRY_CODE": "CHE - DEFAULT",
            "COUNTRY": "Switzerland - DEFAULT",
            "STATE": "Zurich - DEFAULT",
            "CITY": "Zurich - DEFAULT",
            "SUBLOCATION": "Sublocation - DEFAULT",
            "HEADLINE": "Headline - DEFAULT",
            "TITLE_SUFFIX": "title_suffix - DEFAULT",
            "DESCRIPTION": "Description - DEFAULT",
            "COPYRIGHT": "Leo Huber - DEFAULT"
        }

        with open(meta_file_zzz, 'w') as f:
            json.dump(meta_data, f, indent=4)

# Check if the exiftool command is available in the system
if shutil.which('exiftool') is None:
    error_exit("Exiftool command not found. Please install it before running this script.")

# Check if at least one video file is provided as a command-line argument
if len(sys.argv) < 2:
    error_exit("No video file specified. Please provide at least one video file as an argument.")

for movie_file in sys.argv[1:]:
    generate_metadata(movie_file)