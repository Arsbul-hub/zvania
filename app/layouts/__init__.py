import os
from os.path import isfile, basename
from config import Config


def get_all_layouts():
    all_paths = os.walk(Config.LAYOUTS_PATH)
    all_layouts_paths = []
    for path, dirs, files in all_paths:
        for file_name in files:
            file_path = os.path.join(path, file_name)
            if basename(file_path).split(".")[-1] == "kv":
                all_layouts_paths.append(file_path)

    return all_layouts_paths
