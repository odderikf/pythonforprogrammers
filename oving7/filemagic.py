import sys
import os


def findtype(filename):
    magic_bytes = {
        b'\xFF\xD8\xFF\xE0': "JPEG",
        b'\x89\x50\x4E\x47\x0D\x0A\x1A\x0A': "PNG",
        b'\x49\x49\x2A\x00': "TIFF",
        b'\x47\x49\x46\x38\x39\x61': "GIF89a"
    }
    candidates = list(magic_bytes.keys())
    with open(filename, 'rb') as file:
        pos = 0
        while candidates:  # break and return None if no candidate matches
            byte = file.read(1)  # read a single byte
            for i, bstr in enumerate(candidates):
                if pos == len(bstr):  # you've matched every byte of an entire magic bytestring
                    return magic_bytes[bstr]
                elif bstr[pos] != byte[0]:  # it doesn't match, so pop it off
                    candidates.pop(i)
            pos += 1  # keep going through new positions in the bytestrings

def sort_files(filenames):
    pass

def main():
    if len(sys.argv) > 1:
        for file in sys.argv[1:]:
            print(findtype(file))
    else:
        for filename in os.listdir("images"):
            print(filename, findtype(os.path.join("images", filename)))


if __name__ == "__main__":
    main()
