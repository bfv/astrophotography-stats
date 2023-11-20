import os
import tomllib
from photodir import *
from generate_stats import *

ignore_dirs = []
config = {}
files = []

def main():
    config = init_config()
    #print(config)
    photo_dir = get_photo_dir(config)
    subdirs = get_subdirs(photo_dir)
    eval_dirs(photo_dir, subdirs)
    #print("files found:", len(files))
    print_stats()
    
def init_config() -> {}:
    with open("stats.config.toml", "rb") as f:
        cfg = tomllib.load(f)
    files_section = cfg["files"]
    ignore_dirs.extend(files_section["excludedirs"])
    return cfg

def get_photo_dir(config) -> str:
    files_section = config["files"]
    try:
        default_dir = files_section["defaultdir"]
    except:
        default_dir = os.path.join(os.getcwd(), "testdata")

    default_dir = input(f"Input photo dir [{default_dir}]: ") or default_dir   
    return default_dir

def get_subdirs(dir) -> []:
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

def print_stats():
    generate_stats(files)
        
main()
