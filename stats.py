import os
import tomllib
from photodir import PhotoDir

ignore_dirs = []
config = {}
files = []

def main():
    init_config()
    photo_dir = get_photo_dir()
    subdirs = get_subdirs(photo_dir)
    eval_dirs(photo_dir, subdirs)
    

def init_config():
    with open("stats.config.toml", "rb") as f:
        config = tomllib.load(f)
    files_section = config["files"]
    ignore_dirs.extend(files_section["excludedirs"])

def get_photo_dir() -> str:
    default_dir = os.path.join(os.getcwd(), "testdata")
    photo_dir = input(f"Input photo dir [{default_dir}]: ") or default_dir
    return photo_dir

def get_subdirs(dir) -> []:
    print(f"analyse: {dir}")
    evaldirs = os.listdir(dir)
    subdirs = [i for i in evaldirs if i not in ignore_dirs]
    return subdirs

def eval_dirs(rootdir, subdirs):
    for subdir in subdirs:
        dir = os.path.join(rootdir, subdir)
        eval_dir(dir)

def eval_dir(dir):
   pdir = PhotoDir(dir)
   files.extend(pdir.photos)


main()
