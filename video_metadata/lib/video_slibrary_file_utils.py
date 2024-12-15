import os

def expand_path_video(path):
    video_files = []
    if os.path.isdir(path):
        for root, _, files in os.walk(path):
            for file in files:
                if file.lower().endswith(('.mp4', '.mov')):
                    video_files.append(os.path.join(root, file))
    elif os.path.isfile(path) and path.lower().endswith(('.mp4', '.mov')):
        video_files.append(path)
    return video_files