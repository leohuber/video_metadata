import subprocess
import shlex
from typing import Optional, Tuple, Dict

def get_date_created_and_identifier(video_file: str, extension: str) -> Tuple[Optional[str], Optional[str]]:
  date_created = None
  identifier = None

  date_tags = {
    "mov": ["CreationDate", "CreateDate"],
    "mp4": ["SubSecCreateDate", "CreateDate"]
  }

  for tag in date_tags.get(extension, []):
    result = subprocess.run(
      ["exiftool", "-q", "-q", "-b", "-api", "largefilesupport=1", f"-{tag}", shlex.quote(video_file)],
      stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
    )
    datec = result.stdout.strip()
    if datec:
      date_created = datec
      identifier = date_created[:19].replace(' ', '_').replace(':', '')
      break

  return date_created, identifier

def get_metadata_all(video_file: str) -> str:
  result = subprocess.run(
    ["exiftool", "-a", "-G0:1", "-api", "largefilesupport=1", shlex.quote(video_file)],
    stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
  )
  return result.stdout.strip()

def get_make(video_file: str) -> str:
  result = subprocess.run(
    ["exiftool", "-q", "-q", "-b", "-api", "largefilesupport=1", "-Make", shlex.quote(video_file)],
    stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
  )
  return result.stdout.strip() or 'Apple - DEFAULT'

def get_model(video_file: str) -> str:
  result = subprocess.run(
    ["exiftool", "-q", "-q", "-b", "-api", "largefilesupport=1", "-Model", shlex.quote(video_file)],
    stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
  )
  return result.stdout.strip() or 'iPhone 11 Pro - DEFAULT'

def get_source_image_height(video_file: str) -> str:
  result = subprocess.run(
    ["exiftool", "-q", "-q", "-b", "-api", "largefilesupport=1", "-SourceImageHeight", shlex.quote(video_file)],
    stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
  )
  return result.stdout.strip()

def get_source_image_width(video_file: str) -> str:
  result = subprocess.run(
    ["exiftool", "-q", "-q", "-b", "-api", "largefilesupport=1", "-SourceImageWidth", shlex.quote(video_file)],
    stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
  )
  return result.stdout.strip()

def get_video_frame_rate(video_file: str) -> str:
  result = subprocess.run(
    ["exiftool", "-q", "-q", "-b", "-api", "largefilesupport=1", "-VideoFrameRate", shlex.quote(video_file)],
    stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
  )
  return result.stdout.strip()

def get_compressor_name(video_file: str) -> str:
  result = subprocess.run(
    ["exiftool", "-q", "-q", "-b", "-api", "largefilesupport=1", "-CompressorName", shlex.quote(video_file)],
    stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
  )
  return result.stdout.strip()

def get_gps(video_file: str) -> str:
  result = subprocess.run(
    ["exiftool", "-q", "-q", "-b", "-api", "largefilesupport=1", "-GPSCoordinates", shlex.quote(video_file)],
    stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
  )
  gps = result.stdout.strip()
  return gps.replace(' ', ', ') if gps else '-35.2975906, 149.1012676, 554 - DEFAULT'

def get_country_code(video_file: str) -> str:
  result = subprocess.run(
    ["exiftool", "-q", "-q", "-b", "-api", "largefilesupport=1", "-CountryCode", shlex.quote(video_file)],
    stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
  )
  return result.stdout.strip() or 'CHE - DEFAULT'

def get_country(video_file: str) -> str:
  result = subprocess.run(
    ["exiftool", "-q", "-q", "-b", "-api", "largefilesupport=1", "-Country", shlex.quote(video_file)],
    stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
  )
  return result.stdout.strip() or 'Switzerland - DEFAULT'

def get_creator(video_file: str) -> str:
  result = subprocess.run(
    ["exiftool", "-q", "-q", "-b", "-api", "largefilesupport=1", "-Creator", shlex.quote(video_file)],
    stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
  )
  return result.stdout.strip() or 'Leo Huber - DEFAULT'

def get_state(video_file: str) -> str:
  result = subprocess.run(
    ["exiftool", "-q", "-q", "-b", "-api", "largefilesupport=1", "-State", shlex.quote(video_file)],
    stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
  )
  return result.stdout.strip() or 'Zurich - DEFAULT'

def get_city(video_file: str) -> str:
  result = subprocess.run(
    ["exiftool", "-q", "-q", "-b", "-api", "largefilesupport=1", "-City", shlex.quote(video_file)],
    stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
  )
  return result.stdout.strip() or 'Zurich - DEFAULT'

def get_sublocation(video_file: str) -> str:
  result = subprocess.run(
    ["exiftool", "-q", "-q", "-b", "-api", "largefilesupport=1", "-Location", shlex.quote(video_file)],
    stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
  )
  return result.stdout.strip() or 'Sublocation - DEFAULT'

def get_headline(video_file: str) -> str:
  result = subprocess.run(
    ["exiftool", "-q", "-q", "-b", "-api", "largefilesupport=1", "-Headline", shlex.quote(video_file)],
    stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
  )
  return result.stdout.strip() or 'Headline - DEFAULT'

def get_title_suffix(video_file: str) -> str:
  result = subprocess.run(
    ["exiftool", "-q", "-q", "-b", "-api", "largefilesupport=1", "-Title", shlex.quote(video_file)],
    stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
  )
  title_suffix = result.stdout.strip()
  return title_suffix.partition('_')[-1] if title_suffix else 'Title Suffix - DEFAULT'

def get_description(video_file: str) -> str:
  result = subprocess.run(
    ["exiftool", "-q", "-q", "-b", "-api", "largefilesupport=1", "-Description", shlex.quote(video_file)],
    stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
  )
  return result.stdout.strip() or 'Description - DEFAULT'

def get_copyright(video_file: str) -> str:
  result = subprocess.run(
    ["exiftool", "-q", "-q", "-b", "-api", "largefilesupport=1", "-Rights", shlex.quote(video_file)],
    stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
  )
  return result.stdout.strip() or 'Leo Huber - DEFAULT'

def get_mediainfo(video_file: str, stream: str, parameter: str) -> str:
  command = ['mediainfo', '-f', f'--Output={stream};%{parameter}%', shlex.quote(video_file)]
  result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
  return result.stdout.strip()

def generate_codec_info(video_file: str) -> Dict[str, str]:
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
  if (hdr_format):
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