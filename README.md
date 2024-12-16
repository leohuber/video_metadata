# Video MetaData
Scripts for managing meta data for video files

## Installation
1. Install Media Info CLI from [Media Info](https://mediaarea.net/en/MediaInfo)
2. Install Exiftool from [Exiftool](https://exiftool.org)
3. Download .gz file from latest release and install usinge the command 'pip install'

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

`CreateDate` is likely the most accurate timestamp, especially for videos directly from a digital camera, as it often matches `TrackCreateDate` and `MediaCreateDate`. The `TrackCreateDate` and `MediaCreateDate` tags might be used to track the creation of individual video or sound tracks, which can be useful when editing and combining multiple clips.

Note that the `CreateDate`, `TrackCreateDate`, and `MediaCreateDate` tags are recorded in UTC time. However, some cameras may not adhere to this specification, leading to incorrect timestamps. The `CreationDate` tag, which includes a timezone and is set to the local time where the video was taken, is part of the QuickTime Keys Tags and requires ExifTool version 11.39+ to edit. Additionally, some versions of the Apple Photos app may display incorrect times if the `Quicktime:CreationDate` or `Quicktime:DateTimeOriginal` tags lack a timezone. ExifTool version 12.13+ will automatically add the local timezone if it is missing when writing.

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
