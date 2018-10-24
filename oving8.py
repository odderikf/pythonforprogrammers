import re
class RLEString:
    # An alphanumeric character, and that specific character 0 or more additional times
    __compress_pattern = re.compile(r"([A-Za-z])\1*")
    re.split("PATTERN", "STRING")
    pattern = re.compile("PATTERN")
    pattern.split("STRING")
    # match any amount of numbers
    __decompress_pattern = re.compile(r"[0-9]+")
    def compress(self):
        if self.iscompressed():
            raise ValueError("Already compressed")
        # fetch the actual matched groups for every match.
        # tldr splits the string into sequences of the same character
        matches = [s.group() for s in self.__compress_pattern.finditer(self.__mystring)]
        # encode as length of the sequence and then the character of the sequence
        self.__mystring = "".join([str(len(i))+i[0] for i in matches])
        self.__iscompressed = True
        
    def decompress(self):
        if not self.iscompressed():
             raise ValueError("Not compressed")
        # for each pair of count and character in the compressed string, write that character [count] times
        counts = self.__decompress_pattern.findall(self.__mystring)
        strings = self.__decompress_pattern.split(self.__mystring)[1:] # skip the empty first result
        self.__mystring = "".join([int(count)*char for count,char in zip(counts, strings)])
        self.__iscompressed = False
        
    def iscompressed(self):
        return self.__iscompressed
    
    def __init__(self, s):
        try:
            if not s.isalpha():
                raise ValueError("string is not alphanumeric")
        except AttributeError:
            raise ValueError("Not a string. No s.isalpha()")
        self.__mystring = s
        self.__iscompressed = False
    
    def __str__(self):
        return self.__mystring
