# Video MetaData
Scripts for managing meta data for video files

## Installation
1. Install Media Info CLI from [Media Info](https://mediaarea.net/en/MediaInfo)
2. Install Exiftool from [Exiftool](https://exiftool.org)
3. Download zip file from latest release and run the script install.sh (sudo)

## Scripts

### `video_cleanup_metadata`
This script cleans up metadata files in the current directory. It searches for all `.json` and `.txt` files and removes them. The script provides feedback on the number of files found and removed.

**Output:**
- Removes `.json` and `.txt` files in the current directory.

### `video_generate_metadata`
This script generates metadata for video files. It processes each provided video file, extracts metadata using `exiftool` and `mediainfo`, and writes the metadata to JSON and text files.  The script also creates a default metadata template if it doesn't exist. The JSON file and the default template can be used to edit the metadata and set it using the script `video_set_metadata`.

**Output:**
- JSON file containing extracted metadata.
- Text file containing all metadata with group levels 0 and 1.

### `video_set_metadata`
This script sets metadata for video files based on provided metadata files. It processes each provided video file, updates its metadata using `exiftool`, and creates backups of the original files (video & metadata). The script ensures that mandatory metadata fields are valid and renames files if necessary.

**Output:**
- Updates metadata of the video files.
- Creates backups of the original files.

### `video_date_util`
This script retrieves and prints all date-related metadata for the provided video files. It uses `exiftool` to extract the date information and displays it in a structured format.

**Output:**
- Prints all date-related metadata for each provided video file.

## Comparing MetaData before and after an update

The script `video_set_metadata` creates a copy of the complete dump of the available metadata before and after the update. The backup of the metadata dump after the update can be found in the backup directory. To compare the metadata before and after the update perform the following command `vim -d backup/file2.txt file1.txt`

## Exiftool Group Names
ExifTool uses group names to categorize metadata tags based on their location and context. Groups are organized into families, and each group has a name that helps identify where a tag comes from.

### Group Families:

- Family 0 (General Location): Broad categories like EXIF, IPTC, XMP.
- Family 1 (Specific Location): More specific namespaces or schemas within the general category, like XMP-dc, XMP-xmp.

### Differences Between XMP and XMP-dc
XMP Group:
- Represents: The overall XMP metadata block in the file.
- Group Family: 0 (General Location).
- Usage: When you reference XMP, you're addressing the XMP metadata as a whole without specifying a particular schema.

XMP-dc Group:
- Represents: The Dublin Core schema within XMP.
- Group Family: 1 (Specific Location).
- Usage: When you specify XMP-dc, you're targeting the dc (Dublin Core) schema specifically.

## Exiftool Command Line Arguments

### General Options
- `-q`: Quiet processing. Suppresses normal messages.
- `-q -q`: Extra quiet processing. Suppresses all messages.
- `-b`: Output data in binary format.
- `-api largefilesupport=1`: Enables support for large files.
- `-overwrite_original`: Overwrites the original file with the new metadata.
- `-a`: Allow duplicate tag names in the output.
- `-G0:1`: Print family 0 and family 1 group name for each tag.

## Dates

One minor nitpick, these tags are not EXIF tags, they are Quicktime tags (all EXIF is Metadata, but not all Metadata is EXIF). You can add -G1 to your command to see the group they belong too. Additionally, if you add -a to your command, you will probably see that TrackCreateDate and MediaCreateDate are duplicated, one for each track in the file (video, audio, etc).
CreateDate is probably the most accurate, but if the video is coming directly from a digital camera of some sort, it is probably the same value as TrackCreateDate and MediaCreateDate.
Video metadata isn't my expertise, but I would guess that Track/MediaCreateDate leaves open the possibility of keeping track of an earlier created video/sound track and muxing them together for a final product. Something that might pop up if you are editing various video clips together.

One thing to take note of is that these three tags are supposed to be recorded in UTC time. See fifth paragraph on the Exiftool Quicktime tag page. The trouble is that some cameras, mostly any camera that is not aware of the current time zone, do not adhere to the specs, so the time that appears in the above tags may not at first seem to be the correct time.
CreationDate is different. It includes a timezone, is supposed to be set to the local time where the video was taken, and is part of the QuickTime Keys Tags. It requires exiftool ver 11.39+ to edit. Also of note is that some versions of the Apple Photos app will display wildly inaccurate time if the Quicktime:CreationDate or Quicktime:DateTimeOriginal tags do not include a time zone (see third image in this exiftool forum post). Exiftool ver 12.13+ will automatically add the local time zone if one is not included when writing.

More information:
* https://exiftool.org/TagNames/QuickTime.html (check 5th paragraph)
* https://superuser.com/questions/1285914/what-is-the-difference-between-the-exif-tags-createdate-creationdate-etc#1285932

## Exiftool Tags used

### Date and Time
- `-CreateDate`: Sets and extracts the creation date of the file.
- `-DateTimeOriginal`: Sets and extracts the original date and time when the file was created.
- `-SubSecCreateDate`: Sets and extracts the creation date with sub-second precision.
- `-xmp:DateTimeOriginal`: Sets and extracts the XMP original date and time tag.
- `-xmp:ShotDate`: Sets and extracts the XMP shot date tag.

### Camera Information
- `-Model`: Sets and extracts the camera model used to create the file.
- `-Make`: Sets and extracts the camera make used to create the file.

### Location Information
- `-GPSCoordinates`: Sets and extracts the GPS coordinates.
- `-UserData:GPSCoordinates`: Sets and extracts the GPS coordinates in the user data.
- `-xmp:LocationShownCountryCode`: Sets and extracts the XMP location shown country code tag.
- `-xmp:LocationCreatedCountryCode`: Sets and extracts the XMP location created country code tag.
- `-xmp:LocationShownCountryName`: Sets and extracts the XMP location shown country name tag.
- `-xmp:LocationCreatedCountryName`: Sets and extracts the XMP location created country name tag.
- `-xmp:LocationShownProvinceState`: Sets and extracts the XMP location shown province/state tag.
- `-xmp:LocationCreatedProvinceState`: Sets and extracts the XMP location created province/state tag.
- `-xmp:LocationShownCity`: Sets and extracts the XMP location shown city tag.
- `-xmp:LocationCreatedCity`: Sets and extracts the XMP location created city tag.
- `-xmp:LocationShownSublocation`: Sets and extracts the XMP location shown sublocation tag.
- `-xmp:LocationCreatedSublocation`: Sets and extracts the XMP location created sublocation tag.

### Descriptive Information
- `-xmp:ImageDescription`: Sets and extracts the XMP image description tag.
- `-xmp:Title`: Sets and extracts the XMP title tag.
- `-xmp:Headline`: Sets and extracts the XMP headline tag.
- `-xmp:Description`: Sets and extracts the XMP description tag.
- `-xmp:Creator`: Sets and extracts the XMP creator tag.
- `-xmp:Marked`: Sets and extracts the XMP marked tag.
- `-xmp:Rights`: Sets and extracts the XMP rights tag.
- `-Rights`: Sets and extracts the copyright information.
- `-Headline`: Sets and extracts the headline information.
- `-Title`: Sets and extracts the title information.
- `-Description`: Sets and extracts the description information.
- `-CountryCode`: Sets and extracts the country code information.
- `-Country`: Sets and extracts the country information.
- `-State`: Sets and extracts the state information.
- `-City`: Sets and extracts the city information.
- `-Location`: Sets and extracts the location information.
- `-Creator`: Sets and extracts the creator information.

### Video Information
- `-xmp:VideoFrameSizeH`: Sets and extracts the XMP video frame size height tag.
- `-xmp:VideoFrameSizeW`: Sets and extracts the XMP video frame size width tag.
- `-xmp:VideoFrameRate`: Sets and extracts the XMP video frame rate tag.
- `-xmp:VideoCompressor`: Sets and extracts the XMP video compressor tag.
- `-xmp:VideoFrameSizeUnit`: Sets and extracts the XMP video frame size unit tag.

### Miscellaneous
- `-xmp:DigitalSourceType`: Sets and extracts the XMP digital source type tag.

