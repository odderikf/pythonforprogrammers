## Imports here:
import sys
import os
from collections import Counter
from functools import reduce
import re

## Part 1 - Listing files
#
def getfilelist(pathname):
    txts = []
    for dirpath, dirnames, filenames in os.walk(pathname):
        for filename in filenames:
            if filename[-4:] == ".txt":
                txts.append(os.path.join(dirpath,filename))
    return sorted(txts)

## Part 2 - Dictionary of word frequencies
#
def getwordfreqs(filename):
    counter = Counter()
    with open(filename) as file:
        contents = file.read()
    words = [s.lower() for s in re.findall("[A-Za-z]+", contents)]
    counter = Counter(words)
    return counter


## Part 3 - Most frequent words common to all dictionaries
#
def getcommonwords(dicts):
    commonWords = [
        {i[0] for i in dicct.most_common(10)} # extract the words out of most_common(10)
            for dicct in dicts] # for every book 
    return reduce( lambda i,j: i.intersection(j), commonWords) # filter out any that aren't common

dictsList = []
# Get the list of files

for f in getfilelist("books"):
    # Get word frequencies
    dictsList.append(getwordfreqs(f))

# Get common words
for w in getcommonwords(dictsList):
    print(w)
