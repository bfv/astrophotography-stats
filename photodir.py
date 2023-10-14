import os, pathlib
import glob
from fitsfile import FitsFile

class PhotoDir:

    def __init__(self, dir):
        self.rootdir = dir
        self.photos = []
        self.parse_dir(dir)

    def parse_dir(self, dir):
        print("parse:", dir)
        files = self.get_files(dir, ["fit", "fits"])
        for file in files:
            file = FitsFile(file)
            if file.is_fits :
                self.photos.append(file)

    def test(self, filename):
        ext = pathlib.Path(filename).suffix
        print(f"{filename} -> {ext}")

    def get_files(self, dir, extensions) -> []:
        files = []
        #for mask in masks:
        path = pathlib.Path(dir)
        for ext in extensions:
            for file in path.rglob(f"*.{ext}"):
                files.append(file.absolute())
        return files
            


