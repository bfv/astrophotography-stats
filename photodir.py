import os

from pathlib import Path
from fitsfile import FitsFile
from target import get_target_info

class PhotoDir:

    def __init__(self, dir: str):
        self.rootdir = dir
        self.photos: list[FitsFile] = []
        self.target = self.__get_object_name(dir)
        self.parse_dir(dir)

    def parse_dir(self, dir: str):
        files = self.get_files(dir, ["fit", "fits"])
        for f in files:
            try:
                file = FitsFile(f, target=self.target)
                if file.is_fits :
                    self.photos.append(file)
            except:
                pass
            
    def test(self, filename: str):
        ext = Path(filename).suffix
        print(f"{filename} -> {ext}")

    def get_files(self, dir: str, extensions: list[str]) -> list[Path]:
        files: list[Path] = []
        #for mask in masks:
        path = Path(dir)
        for ext in extensions:
            for file in path.rglob(f"*.{ext}"):
                files.append(file.absolute())
        return files
    
    def __get_object_name(self, dir: str) -> str:
        object_name = get_target_info(dir)
        return object_name


