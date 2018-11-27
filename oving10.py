import unittest
import sys

# Uncomment below for testing only, comment out before upload
from oving8 import RLEString

class Assignment8Tests(unittest.TestCase):
    class string_inheritor(str):
        pass
        
    strings = ["hhazzzellnuutt", "aaaaa", "hei", "sjokolade", "teststring", "stuff", string_inheritor("test")]
    compressed = ["2h1a3z1e2l1n2u2t", "5a", "1h1e1i", "1s1j1o1k1o1l1a1d1e", "1t1e1s1t1s1t1r1i1n1g", "1s1t1u2f", "1t1e1s1t"]

    invalid_strings = ["", "^", ",", "...,.,.,.,a", 232, 4+2j]
    
    def test_compress(self):
        for s,c in zip(self.strings, self.compressed):
            RLE = RLEString(s)
            before = str(RLE)
            RLE.compress()
            after = str(RLE)
            self.assertEqual(before, s)
            self.assertEqual(after, c)

    def test_decompress(self):
        for s,c in zip(self.strings, self.compressed):
            RLE = RLEString("dummy")
            RLE._RLEString__mystring = c
            RLE._RLEString__iscompressed = True
            before = str(RLE)
            RLE.decompress()
            after = str(RLE)
            self.assertEqual(before, c)
            self.assertEqual(after, s)

    def test_whole(self):
        for s,c in zip(self.strings, self.compressed):
            RLE = RLEString(s)
            before = str(RLE)
            RLE.compress()
            middle = str(RLE)
            RLE.decompress()
            after = str(RLE)
            self.assertEqual(before, s)
            self.assertEqual(middle, c)
            self.assertEqual(after, s)

    def test_double_compress(self):
        RLE = RLEString("dummy")
        RLE.compress()
        with self.assertRaises(ValueError):
            RLE.compress()
    
    def test_double_decompress(self):
        RLE = RLEString("dummy")
        RLE.compress()
        RLE.decompress()
        with self.assertRaises(ValueError):
            RLE.decompress()

    def test_decompress_without_compressing(self):
        RLE = RLEString("dummy")
        with self.assertRaises(ValueError):
            RLE.decompress()

    def test_invalid_strings(self):
        for i in self.invalid_strings:
            with self.assertRaises(ValueError):
                RLEString(i)

if __name__ == '__main__':
    # Start the unit test
    unittest.main(verbosity=2)
