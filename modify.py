from sys import argv
import os
from json import loads
from datetime import datetime

def find_file(ctf: dict, filename):
    for item in ctf:
        if item["filename"] == filename:
            return item
    return {}

def modify_time(tsfname, d):
    if not os.path.exists(tsfname):
        print(f"Error: timestamp file \"{tsfname}\" does not exist!")
        exit(2)
    f = open(tsfname, "r")
    tsfile = loads(f.read())
    count = 0
    for directory, subdirs, files in os.walk(d):
        for file in files:
            dat = find_file(tsfile, file)
            if len(dat) == 0:
                print(f"Skipping file \"{file}\" as time data was not found!")
                continue
            ctime = float(dat["createtime"])
            mtime = float(dat["modifytime"])
            os.utime(os.path.join(directory, file), (ctime, mtime))
            count += 1
    print(f"Modified timestamps of {count} files!")

if __name__ == "__main__":
    if len(argv) != 3:
        print("Usage: python modify.py <creation-times-file> <root-directory>")
        exit(1)
    
    tsfname = argv[1]
    rootdir = argv[2]

    modify_time(tsfname, rootdir)