import subprocess
import os

def get_date_created_and_identifier(video_file, extension):
    date_created = None
    identifier = None

    # Check if we are processing a QuickTime container
    if extension == "mov":
        # Try to get CreationDate
        datec = subprocess.getoutput(f"exiftool -q -q -b -api largefilesupport=1 -CreationDate '{video_file}'")
        if datec:
            date_created = datec
            identifier = date_created[:19].replace(' ', '_').replace(':', '')
        else:
            # Try to get CreateDate
            datec = subprocess.getoutput(f"exiftool -q -q -b -api largefilesupport=1 -CreateDate '{video_file}'")
            if datec:
                date_created = datec
                identifier = date_created[:19].replace(' ', '_').replace(':', '')

    # Check if we are processing an MP4 container
    if extension == "mp4":
        # Try SubSecCreateDate
        datec = subprocess.getoutput(f"exiftool -q -q -b -api largefilesupport=1 -SubSecCreateDate '{video_file}'")
        if datec:
            date_created = datec
            identifier = date_created[:19].replace(' ', '_').replace(':', '')
        # Try to get CreateDate
        if not date_created:
            datec = subprocess.getoutput(f"exiftool -q -q -b -api largefilesupport=1 -CreateDate '{video_file}'")
            if datec:
                date_created = datec
                identifier = date_created[:19].replace(' ', '_').replace(':', '')

    return date_created, identifier

def get_metadata_all(video_file):
   return subprocess.getoutput(f"exiftool -a -G0:1 -api largefilesupport=1 '{video_file}'")

def get_make(video_file):
    return subprocess.getoutput(f"exiftool -q -q -b -api largefilesupport=1 -Make '{video_file}'") or 'Apple - DEFAULT'

def get_model(video_file):
    return subprocess.getoutput(f"exiftool -q -q -b -api largefilesupport=1 -Model '{video_file}'") or 'iPhone 11 Pro - DEFAULT'

def get_source_image_height(video_file):
    return subprocess.getoutput(f"exiftool -q -q -b -api largefilesupport=1 -SourceImageHeight '{video_file}'")

def get_source_image_width(video_file):
    return subprocess.getoutput(f"exiftool -q -q -b -api largefilesupport=1 -SourceImageWidth '{video_file}'")

def get_video_frame_rate(video_file):
    return subprocess.getoutput(f"exiftool -q -q -b -api largefilesupport=1 -VideoFrameRate '{video_file}'")

def get_compressor_name(video_file):
    return subprocess.getoutput(f"exiftool -q -q -b -api largefilesupport=1 -CompressorName '{video_file}'")

def get_gps(video_file):
    gps = subprocess.getoutput(f"exiftool -q -q -b -api largefilesupport=1 -GPSCoordinates '{video_file}'")
    if gps:
        return gps.replace(' ', ', ')
    else:
        return '-35.2975906, 149.1012676, 554 - DEFAULT'

def get_country_code(video_file):
    return subprocess.getoutput(f"exiftool -q -q -b -api largefilesupport=1 -CountryCode '{video_file}'") or 'CHE - DEFAULT'

def get_country(video_file):
    return subprocess.getoutput(f"exiftool -q -q -b -api largefilesupport=1 -Country '{video_file}'") or 'Switzerland - DEFAULT'

def get_creator(video_file):
    return subprocess.getoutput(f"exiftool -q -q -b -api largefilesupport=1 -Creator '{video_file}'") or 'Leo Huber - DEFAULT'

def get_state(video_file):
    return subprocess.getoutput(f"exiftool -q -q -b -api largefilesupport=1 -State '{video_file}'") or 'Zurich - DEFAULT'

def get_city(video_file):
    return subprocess.getoutput(f"exiftool -q -q -b -api largefilesupport=1 -City '{video_file}'") or 'Zurich - DEFAULT'

def get_sublocation(video_file):
    return subprocess.getoutput(f"exiftool -q -q -b -api largefilesupport=1 -Location '{video_file}'") or 'Sublocation - DEFAULT'

def get_headline(video_file):
    return subprocess.getoutput(f"exiftool -q -q -b -api largefilesupport=1 -Headline '{video_file}'") or 'Headline - DEFAULT'

def get_title_suffix(video_file):
    title_suffix = subprocess.getoutput(f"exiftool -q -q -b -api largefilesupport=1 -Title '{video_file}'")
    if title_suffix:
        return title_suffix.partition('_')[-1]
    else:
        return 'Title Suffix - DEFAULT'

def get_description(video_file):
    return subprocess.getoutput(f"exiftool -q -q -b -api largefilesupport=1 -Description '{video_file}'") or 'Description - DEFAULT'

def get_copyright(video_file):
    return subprocess.getoutput(f"exiftool -q -q -b -api largefilesupport=1 -Rights '{video_file}'") or 'Leo Huber - DEFAULT'

def get_mediainfo(video_file, stream, parameter):
  command = ['mediainfo', '-f', f'--Output={stream};%{parameter}%', video_file]
  result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
  return result.stdout.strip()

def generate_codec_info(video_file):

  codec_info = {}

  # Format
  format_fields = [
    get_mediainfo(video_file, 'Video', 'Format'),
    get_mediainfo(video_file, 'Video', 'Format/Info'),
    get_mediainfo(video_file, 'Video', 'Format_Profile'),
    get_mediainfo(video_file, 'Video', 'Format_Settings')
  ]
  format_fields = [field for field in format_fields if field]
  if format_fields:
    codec_info['FORMAT_FIELDS'] = f"Format: {', '.join(format_fields)}"

  # HDR Format
  hdr_format = get_mediainfo(video_file, 'Video', 'HDR_Format/String')
  if hdr_format:
    codec_info['HDR_FORMAT'] = f"HDR Format: {hdr_format}"

  # Pixel Format
  pixel_fields = [
    f"ColorSpace={get_mediainfo(video_file, 'Video', 'ColorSpace')}",
    f"ChromaSubsampling={get_mediainfo(video_file, 'Video', 'ChromaSubsampling/String')}",
    f"BitDepth={get_mediainfo(video_file, 'Video', 'BitDepth/String')}"
  ]
  pixel_fields = [field for field in pixel_fields if field.split('=')[1]]
  if pixel_fields:
    codec_info['PIXEL_FORMAT'] = f"Pixel Format: {', '.join(pixel_fields)}"

  # Frame Rate
  framerate_fields = [
    f"Mode={get_mediainfo(video_file, 'Video', 'FrameRate_Mode')}",
    f"Rate={get_mediainfo(video_file, 'Video', 'FrameRate')}",
    f"Min={get_mediainfo(video_file, 'Video', 'FrameRate_Minimum')}",
    f"Max={get_mediainfo(video_file, 'Video', 'FrameRate_Maximum')}"
  ]
  framerate_fields = [field for field in framerate_fields if field.split('=')[1]]
  if framerate_fields:
    codec_info['FRAMERATE_FIELDS'] = f"Frame Rate: {', '.join(framerate_fields)}"

  # Scan Type
  scan_fields = [
    f"Type={get_mediainfo(video_file, 'Video', 'ScanType')}",
    f"StoreMethod={get_mediainfo(video_file, 'Video', 'ScanType_StoreMethod')}",
    f"ScanOrder={get_mediainfo(video_file, 'Video', 'ScanOrder/String')}"
  ]
  scan_fields = [field for field in scan_fields if field.split('=')[1]]
  if scan_fields:
    codec_info['SCAN_FIELDS'] = f"Scan Type: {', '.join(scan_fields)}"

  # Bit Rate
  bitrate_fields = [
    f"Mode={get_mediainfo(video_file, 'Video', 'BitRate_Mode')}",
    f"Rate={get_mediainfo(video_file, 'Video', 'BitRate/String')}",
    f"Min={get_mediainfo(video_file, 'Video', 'BitRate_Minimum/String')}",
    f"Max={get_mediainfo(video_file, 'Video', 'BitRate_Maximum/String')}"
  ]
  bitrate_fields = [field for field in bitrate_fields if field.split('=')[1]]
  if bitrate_fields:
    codec_info['BITRATE_FIELDS'] = f"Bit Rate: {', '.join(bitrate_fields)}"
  
  # Color
  color_fields = [
    f"Primaries={get_mediainfo(video_file, 'Video', 'colour_primaries')}",
    f"TransferCharacteristics={get_mediainfo(video_file, 'Video', 'transfer_characteristics')}",
    f"MatrixCoefficients={get_mediainfo(video_file, 'Video', 'matrix_coefficients')}"
  ]
  color_fields = [field for field in color_fields if field.split('=')[1]]
  if color_fields:
    codec_info['COLOR_FIELDS'] = f"Color: {', '.join(color_fields)}"

  # Dimensions
  dimension_fields = [
    f"Height={get_mediainfo(video_file, 'Video', 'Height')}",
    f"Width={get_mediainfo(video_file, 'Video', 'Width')}",
    f"AspectRatio={get_mediainfo(video_file, 'Video', 'DisplayAspectRatio/String')}",
    f"Rotation={get_mediainfo(video_file, 'Video', 'Rotation')}"
  ]
  dimension_fields = [field for field in dimension_fields if field.split('=')[1]]
  if dimension_fields:
    codec_info['DIMENSION_FIELDS'] = f"Dimensions: {', '.join(dimension_fields)}"

  # Audio
  audio_fields = [
    f"Format={get_mediainfo(video_file, 'Audio', 'Format')}",
    f"BitRate={get_mediainfo(video_file, 'Audio', 'BitRate/String')}",
    f"SamplingRate={get_mediainfo(video_file, 'Audio', 'SamplingRate/String')}",
    f"Channels={get_mediainfo(video_file, 'Audio', 'Channel(s)')}",
    f"Layout={get_mediainfo(video_file, 'Audio', 'ChannelLayout')}"
  ]
  audio_fields = [field for field in audio_fields if field.split('=')[1]]
  if audio_fields:
    codec_info['AUDIO_FIELDS'] = f"Audio: {', '.join(audio_fields)}"

  return codec_info