from sys import argv
from os import walk
from os.path import getctime
from os.path import getmtime
from os.path import join
from json import dumps

def process_directory(d: str, fe: str):
    output = []
    for directory, subdirs, files in walk(d):
        for file in files:
            if fe != "*" and not file.endswith(fe):
                continue
            filepath = join(directory, file)
            ctime = getctime(filepath)
            mtime = getmtime(filepath)
            output.append({
                "filename": file,
                "createtime": str(ctime),
                "modifytime": str(mtime)
            })
            print(f"Added \"{file}\"")
    return output

if __name__ == "__main__":
    if len(argv) != 4:
        print("Usage: python extract.py <root-directory> <filename-match-regex> <output-filename>")
        exit(1)
    rootdir = argv[1]
    fileext = argv[2]
    outfile = argv[3]

    filedata = process_directory(rootdir, fileext)
    if len(filedata) == 0:
        print("No files were found!")
        exit(2)
    
    with open(outfile, "w") as of:
        of.write(dumps(filedata))
    print(f"Successfully created timestamps of {len(filedata)} files!")