import os
import tomllib

from typing import Any
from tqdm import tqdm
from photodir import PhotoDir
from generate_stats import generate_stats, generate_csv, generate_month_stats
from fitsfile import FitsFile

ignore_dirs: list[str] = []
config: dict[str, Any] = {}
files: list[FitsFile] = []  # list of FitsFile

def main():
    config = init_general_config()
    photo_dir = get_photo_dir(config)
    init_dir_config(photo_dir)
    print(f"ignore dirs: {ignore_dirs}")
    subdirs = get_subdirs(photo_dir)
    eval_dirs(photo_dir, subdirs)
    print_stats()
    
def init_general_config() -> dict[str, Any]:
    with open("stats.config.toml", "rb") as f:
        cfg = tomllib.load(f)
    files_section = cfg["files"]
    ignore_dirs.extend(files_section["excludedirs"])
    return cfg

def init_dir_config(dir: str):
    cfgfile = os.path.join(dir, "stats-config.toml")
    if os.path.exists(cfgfile):
        with open(cfgfile, "rb") as f:
            cfg = tomllib.load(f)
        try:
            files_section = cfg["files"]
            ignore_dirs.extend(files_section["excludedirs"]) 
        except:
            pass 

def get_photo_dir(config: dict[str, Any]) -> str:
    files_section = config["files"]
    try:
        default_dir = files_section["defaultdir"]
    except:
        default_dir = os.path.join(os.getcwd(), "testdata")

    default_dir = input(f"Input photo dir [{default_dir}]: ") or default_dir   
    return default_dir

def get_subdirs(dir: str) -> list[str]:
    evaldirs = os.listdir(dir)
    subdirs = [dir for dir in evaldirs if dir not in ignore_dirs]
    return subdirs

def eval_dirs(rootdir: str, subdirs: list[str]):
    for subdir in tqdm(subdirs, desc ="processing directories", write_bytes=False):
        dir = os.path.join(rootdir, subdir)
        if os.path.isdir(dir):
            eval_dir(dir)

def eval_dir(dir: str):
   pdir = PhotoDir(dir)
   files.extend(pdir.photos)

def print_stats():
    print('-' * 80)
    generate_csv(files)
    print('-' * 80)
    generate_month_stats(files)
    
main()
