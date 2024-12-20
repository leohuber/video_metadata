import datetime
import json
import sys
import shutil
import os
import subprocess
from video_metadata.lib.video_slibrary_metadata_utils import get_metadata_all
from video_metadata.lib.video_slibrary_print_utils import print_green, print_red, print_blue

def error_exit(message) -> None:
	print_red(message)
	sys.exit(1)

def check_file_exists(file_path) -> None:
	if not os.path.isfile(file_path):
		error_exit(f"Could not find file: {file_path}")

def set_meta_info(video_file) -> None:

	print_green(f"Processing file: {video_file}")

	extension = os.path.splitext(video_file)[1].lower()

	meta_file = os.path.splitext(video_file)[0] + '_meta.json'
	check_file_exists(meta_file)

	meta_file_all = os.path.splitext(video_file)[0] + '_meta_all.txt'
	check_file_exists(meta_file_all)

	# Load meta data from the meta file
	with open(meta_file) as f:
		meta_data = json.load(f)
	
	# Load default meta data from a template file and overwrite the values with the values from default meta data file
	template_file = os.path.join(os.path.dirname(video_file), "zzz_meta_data_template.json")
	if os.path.isfile(template_file):
		with open(template_file) as f:
			template_data = json.load(f)
			meta_data.update(template_data)

	# mandatory values
	identifier = meta_data.get('IDENTIFIER')
	date_created = meta_data.get('DATE_CREATED')
	make = meta_data.get('MAKE')
	model = meta_data.get('MODEL')
	creator = meta_data.get('CREATOR')
	country_code = meta_data.get('COUNTRY_CODE')
	country = meta_data.get('COUNTRY')
	state = meta_data.get('STATE')
	city = meta_data.get('CITY')
	sublocation = meta_data.get('SUBLOCATION')
	headline = meta_data.get('HEADLINE')
	title_suffix = meta_data.get('TITLE_SUFFIX').lower()
	description = meta_data.get('DESCRIPTION')
	copyright = meta_data.get('COPYRIGHT')

	# Check if variables are not None and string values do not contain 'default' (case insensitive)
	if identifier is None or (isinstance(identifier, str) and 'default' in identifier.lower()):
		error_exit(f"Invalid value for IDENTIFIER: {identifier}")
	if date_created is None or (isinstance(date_created, str) and 'default' in date_created.lower()):
		error_exit(f"Invalid value for DATE_CREATED: {date_created}")
	if make is None or (isinstance(make, str) and 'default' in make.lower()):
		error_exit(f"Invalid value for MAKE: {make}")
	if model is None or (isinstance(model, str) and 'default' in model.lower()):
		error_exit(f"Invalid value for MODEL: {model}")
	if creator is None or (isinstance(creator, str) and 'default' in creator.lower()):
		error_exit(f"Invalid value for CREATOR: {creator}")
	if country_code is None or (isinstance(country_code, str) and 'default' in country_code.lower()):
		error_exit(f"Invalid value for COUNTRY_CODE: {country_code}")
	if country is None or (isinstance(country, str) and 'default' in country.lower()):
		error_exit(f"Invalid value for COUNTRY: {country}")
	if state is None or (isinstance(state, str) and 'default' in state.lower()):
		error_exit(f"Invalid value for STATE: {state}")
	if city is None or (isinstance(city, str) and 'default' in city.lower()):
		error_exit(f"Invalid value for CITY: {city}")
	if sublocation is None or (isinstance(sublocation, str) and 'default' in sublocation.lower()):
		error_exit(f"Invalid value for SUBLOCATION: {sublocation}")
	if headline is None or (isinstance(headline, str) and 'default' in headline.lower()):
		error_exit(f"Invalid value for HEADLINE: {headline}")
	if title_suffix is None or (isinstance(title_suffix, str) and ('default' in title_suffix.lower() or ' ' in title_suffix)):
		error_exit(f"Invalid value for TITLE_SUFFIX: {title_suffix}")
	if description is None or (isinstance(description, str) and 'default' in description.lower()):
		error_exit(f"Invalid value for DESCRIPTION: {description}")
	if copyright is None or (isinstance(copyright, str) and 'default' in copyright.lower()):
		error_exit(f"Invalid value for COPYRIGHT: {copyright}")

	# optional values
	gps = meta_data.get('GPS')
	source_image_height = meta_data.get('SOURCE_IMAGE_HEIGHT')
	source_image_width = meta_data.get('SOURCE_IMAGE_WIDTH')
	video_frame_rate = meta_data.get('VIDEO_FRAME_RATE')
	compressor_name = meta_data.get('COMPRESSOR_NAME')
	codec_data = meta_data.get('CODEC_INFO')
	if gps is not None:
		if isinstance(gps, str) and 'default' in gps.lower():
			error_exit(f"Invalid value for GPS: {gps}")
	if source_image_height is not None:
		if isinstance(source_image_height, str) and 'default' in source_image_height.lower():
			error_exit(f"Invalid value for SOURCE_IMAGE_HEIGHT: {source_image_height}")
	if source_image_width is not None:
		if isinstance(source_image_width, str) and 'default' in source_image_width.lower():
			error_exit(f"Invalid value for SOURCE_IMAGE_WIDTH: {source_image_width}")
	if video_frame_rate is not None:
		if isinstance(video_frame_rate, str) and 'default' in video_frame_rate.lower():
			error_exit(f"Invalid value for VIDEO_FRAME_RATE: {video_frame_rate}")
	if compressor_name is not None:
		if isinstance(compressor_name, str) and 'default' in compressor_name.lower():
			error_exit(f"Invalid value for COMPRESSOR_NAME: {compressor_name}")

	# Rename files if necessary
	def rename_file(old_name, new_name):
		if old_name != new_name:
			os.rename(old_name, new_name)
			return new_name
		return old_name

	video_file = rename_file(video_file, os.path.join(os.path.dirname(video_file), f"{identifier}_{title_suffix}{extension}"))
	meta_file = rename_file(meta_file, os.path.join(os.path.dirname(meta_file), f"{identifier}_{title_suffix}_meta.json"))
	meta_file_all = rename_file(meta_file_all, os.path.join(os.path.dirname(meta_file_all), f"{identifier}_{title_suffix}_meta_all.txt"))

	print_green("Creating backup of the original files ...")

	# Create backup directory if it doesn't exist
	backup_dir = os.path.join(os.path.dirname(video_file), "backup")
	os.makedirs(backup_dir, exist_ok=True)

	# add time stamp to file names
	current_time_suffix = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
	destination_file = f"{identifier}_{title_suffix}-{current_time_suffix}{extension}"
	destination_meta_file = f"{identifier}_{title_suffix}-{current_time_suffix}_meta.json"
	destination_meta_file_all = f"{identifier}_{title_suffix}-{current_time_suffix}_meta_all.txt"

	# Copy the original file to the backup directory
	shutil.copy(video_file, os.path.join(backup_dir, destination_file))
	shutil.copy(meta_file, os.path.join(backup_dir, destination_meta_file))
	shutil.copy(meta_file_all, os.path.join(backup_dir, destination_meta_file_all))

	print_green("Deleting old xmp metadata ...")

	# Delete xmp metadata
	cmd = ['exiftool', '-api', 'largefilesupport=1', '-overwrite_original', '-xmp=', video_file]
	result = subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
	if result.returncode != 0:
		error_exit(f"Could not delete xmp metadata with command: {' '.join(cmd)}")

	print_green("Updating metadata ...")

	commands = []

	if gps:
		commands.append(['exiftool', '-api', 'largefilesupport=1', '-overwrite_original', f'-GPSCoordinates={gps}', video_file])
	if source_image_height:
		commands.append(['exiftool', '-api', 'largefilesupport=1', '-overwrite_original', '-xmp:VideoFrameSizeUnit=pixels', f'-xmp:VideoFrameSizeH={source_image_height}', video_file])
	if source_image_width:
		commands.append(['exiftool', '-api', 'largefilesupport=1', '-overwrite_original', '-xmp:VideoFrameSizeUnit=pixels', f'-xmp:VideoFrameSizeW={source_image_width}', video_file])
	if video_frame_rate:
		commands.append(['exiftool', '-api', 'largefilesupport=1', '-overwrite_original', f'-xmp:VideoFrameRate={video_frame_rate}', video_file])
	if compressor_name:
		commands.append(['exiftool', '-api', 'largefilesupport=1', '-overwrite_original', f'-xmp:VideoCompressor={compressor_name}', video_file])
	
	commands.append(['exiftool', '-api', 'largefilesupport=1', '-overwrite_original',
				f'-xmp:ShotDate={date_created}',
				f'-xmp:DateTimeOriginal={date_created}',
				f'-xmp:CountryCode={country_code}',
				f'-xmp:Country={country}',
				f'-xmp:State={state}',
				f'-xmp:City={city}',
				f'-xmp:Location={sublocation}',
				f'-xmp:Title={identifier}_{title_suffix}',
				f'-xmp:Headline={identifier}_{headline}',
				f'-xmp:Description={description}',
				f'-xmp:DateCreated={date_created}',
				f'-xmp:Creator={creator}',
				f'-xmp:Marked=True',
				f'-xmp:Rights={copyright}',
				f'-xmp:ImageDescription={description}',
				f'-xmp:LocationShownCountryCode={country_code}',
				f'-xmp:LocationCreatedCountryCode={country_code}',
				f'-xmp:LocationShownCountryName={country}',
				f'-xmp:LocationCreatedCountryName={country}',
				f'-xmp:LocationShownProvinceState={state}',
				f'-xmp:LocationCreatedProvinceState={state}',
				f'-xmp:LocationShownCity={city}',
				f'-xmp:LocationCreatedCity={city}',
				f'-xmp:LocationShownSublocation={sublocation}',
				f'-xmp:LocationCreatedSublocation={sublocation}',
				f'-xmp:DigitalSourceType=http://cv.iptc.org/newscodes/digitalsourcetype/digitalCapture',
				f'-Model={model}',
				f'-Make={make}',
				video_file])

	comment = ""
	for key, value in codec_data.items():
		comment += f"{value}\n"
	comment = comment.rstrip('\n')
	commands.append(['exiftool', '-api', 'largefilesupport=1', '-overwrite_original', f'-xmp:LogComment={comment}', video_file])

	for cmd in commands:
		result = subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
		if result.returncode != 0:
			error_exit(f"Could not update metadata with command: {' '.join(cmd)}")
			
	# Update all metadata fields
	meta_data_all = get_metadata_all(video_file)
	# Write all metadata to a text file
	with open(meta_file_all, 'w') as f:
		f.write(meta_data_all)
		
def set_metadata_for_files(video_files: list) -> None:
    for video_file in video_files:
        set_meta_info(video_file)