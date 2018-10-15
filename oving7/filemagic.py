#!/usr/bin/python3

import sys
import os

magic_bytes = {
    b'\xFF\xD8\xFF\xE0': "JPEG",
    b'\x89\x50\x4E\x47\x0D\x0A\x1A\x0A': "PNG",
    b'\x49\x49\x2A\x00': "TIFF",
    b'\x47\x49\x46\x38\x39\x61': "GIF89a"
}


def findtype(filename):
    candidates = list(magic_bytes.keys())
    with open(filename, 'rb') as file:  # read bytes, bc going byte by byte
        pos = 0
        while candidates:  # break and return None if no candidate matches
            byte = file.read(1)  # read a single byte
            for i, bstr in enumerate(candidates):
                if pos == len(bstr):  # you've matched every byte of an entire magic bytestring
                    return magic_bytes[bstr]
                elif bstr[pos] != byte[0]:  # it doesn't match, so pop it off
                    candidates.pop(i)
            pos += 1  # keep going through new positions in the bytestrings
    return None


def sort_files(files):
    for category in files:
        try:  # Easier to ask for forgiveness than permission.
            os.mkdir(category)  # make directory if not exists
        except FileExistsError:
            pass  # it's fine for the directory to already exist
        for file in files[category]:
            filepath, filename = os.path.split(file)  # get filename
            os.rename(file, os.path.join(category, filename))


def main():
    files = dict()  # make dict for the categories mapping to list of files in them
    if len(sys.argv) > 1:
        for filepath in sys.argv[1:]:  # for every file passed as argument
            typ = findtype(filepath)
            print("File", filepath, "is of type", typ)
            if typ in files:
                files[typ].append(filepath)  # add to category
            else:
                files[typ] = [filepath]  # make category and add to category

        sort_files(files)


if __name__ == "__main__":
    main()
