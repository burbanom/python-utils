#!/usr/bin/env python
from __future__ import print_function
import os
import sys
import argparse
import fnmatch

def read_args():
	parser = argparse.ArgumentParser( description = "find files in directory structure" ) 
        parser.add_argument( "--path", "-p", metavar = "STR", type=str, required = True, help="The path where to look for the file")
        parser.add_argument( "--filename", "-f", metavar = "STR", type=str, required = True, help="The filename to look for")
	return parser.parse_args()

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

if __name__ == '__main__':

  args = read_args()
  path = args.path
  target = args.filename
  les_files = find_files(path,target)
  for le_file in les_files:
      print(le_file)

  pattern = 'ENERGY| Total FORCE_EVAL ( QS ) energy (a.u.)'
  les_files = find_dirs_files_patern(path,pattern)
  for le_file in les_files:
      print(le_file)

