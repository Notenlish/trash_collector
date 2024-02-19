from pathlib import Path

def depth_from_folder_path(path: str):
    return len(Path(path).parents)

def depth_from_file_path(path: str):
    return len(Path(path).parents) - 1
