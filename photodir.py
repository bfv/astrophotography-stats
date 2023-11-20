import os, pathlib
import glob
from fitsfile import FitsFile

class PhotoDir:

    def __init__(self, dir):
        self.rootdir = dir
        self.photos = []
        self.target = self.__get_object_name(dir)
        self.parse_dir(dir)

    def parse_dir(self, dir):
        files = self.get_files(dir, ["fit", "fits"])
        for file in files:
            try:
                file = FitsFile(file, target=self.target)
                if file.is_fits :
                    self.photos.append(file)
            except:
                pass
            
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
    
    def __get_object_name(self, dir) -> str:
        object_name = os.path.basename(os.path.normpath(dir))
        return object_name


