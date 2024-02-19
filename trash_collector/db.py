import os


class BaseItem:
    def __init__(self, path: str, depth: int) -> None:
        self.path = path
        self.depth = depth
        self.size = self._get_size(path)

    def _get_size(self, path):
        return os.stat(path).st_size

    def __repr__(self) -> str:
        return f"< {self.path} >"

    def __lt__(self, other):
        return self.size < other.size


class File(BaseItem):
    def __init__(self, path: str, depth: int, file_name: str) -> None:
        super().__init__(path, depth)
        self.file_name = file_name

    def __repr__(self) -> str:
        return f"<File {self.path} >"


class Folder(BaseItem):
    def __init__(self, path, depth) -> None:
        super().__init__(path, depth)
        self.searched = False

    def __repr__(self) -> str:
        return f"<Folder {self.path} >"


class DB:
    def __init__(self) -> None:
        self.data: dict[int, list[BaseItem]] = {}

    def add_file(self, path, depth, file_name):
        try: self.data[depth]
        except: self.data[depth] = []
        self.data[depth].append(File(path, depth, file_name))

    def add_folder(self, path, depth):
        try: self.data[depth]
        except: self.data[depth] = []
        self.data[depth].append(Folder(path, depth))

    def get_folder(self):
        for i in self.data.keys():
            for value in self.data[i]:
                if type(value) == Folder and not value.searched:
                    value.searched = True
                    return value
        return None
