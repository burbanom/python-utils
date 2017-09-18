from __future__ import print_function
import os
import sys
import fnmatch
import mmap

def clean_files(path,pattern):
    all_files = os.listdir(path)
    filtered = fnmatch.filter(all_files,pattern+"*")
    for element in filtered:
        os.remove(os.path.join(path,element))


def find_files(path,target):
    matches = []
    for root, subFolders, files in os.walk(path):
        if target in files:
            matches.append(root)
    return matches

def find_dirs_files_pattern(path,pattern):
    matches = []
    for root, dirnames, filenames in os.walk(path):
        for filename in fnmatch.filter(filenames, pattern):
            matches.append([root,filename])
    return matches

def return_value(filename,pattern):
    if type(pattern) is str:
        pattern = pattern.encode()
    with open(filename, "r") as fin:
        # memory-map the file, size 0 means whole file
        m = mmap.mmap(fin.fileno(), 0, prot=mmap.PROT_READ)
        #                             prot argument is *nix only
        i = m.rfind(pattern)
        try:
            m.seek(i)             # seek to the location
        except ValueError:
            return np.nan
        line = m.readline()   # read to the end of the line
    return float(line.split()[-1])


