import os

def expand_path_video(path):
    video_files = []
    if os.path.isdir(path):
        for root, _, files in os.walk(path):
            for file in files:
                if file.lower().endswith(('.mp4', '.mov')):
                    video_files.append(os.path.join(root, file))
        if not video_files:
            print(f"No video files (mp4, mov) found in path {path}.")
    elif os.path.isfile(path) and path.lower().endswith(('.mp4', '.mov')):
        video_files.append(path)
    else:
        print(f"Invalid path or file: {path}")
    return video_files
