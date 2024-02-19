import os
import pathlib
import sys
from utils import depth_from_folder_path

from db import DB, File, Folder


def start_search(start_dir, max_depth):
    db = DB()
    root = start_dir
    depth = depth_from_folder_path(start_dir)
    if max_depth == -1:
        max_depth = sys.maxsize
    db.add_folder(start_dir)
    print("starting")
    while depth < max_depth:
        result = db.get_folder()
        if not result:
            break
        
        root = result.path
        depth = result.depth
        # print(result)
        # print("depth is", depth)
        
        for item in os.listdir(root):
            path = os.path.join(root, item)
            if os.path.isfile(path):
                db.add_file(path, item)
            if os.path.isdir(path):
                db.add_folder(path)
    
    results = db.sort_by_type(Folder)
    print(results)
