import os
import pathlib
import sys

from db import DB


def start_search(start_dir, max_depth):
    db = DB()
    depth = 0
    root = start_dir
    if max_depth == -1:
        max_depth = sys.maxsize
    db.add_folder(start_dir, depth)
    print("starting")
    # test
    # test/aa  depth=2
    # test/bb  depth=3
    # thats a problem, 
    
    # len(path.parents) -1 = depth of path/file
    # I should use this instead
    while depth < max_depth:
        print("depth is", depth)
        result = db.get_folder()
        print(result)
        if not result:
            break
        else:
            root = result.path
        for item in os.listdir(root):
            path = os.path.join(root, item)
            if os.path.isfile(path):
                db.add_file(path, depth, item)
            if os.path.isdir(path):
                db.add_folder(path, depth)
        depth += 1
    print(db.data.values())
