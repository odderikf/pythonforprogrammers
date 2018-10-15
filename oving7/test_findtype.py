import os
import filemagic
import unittest


class TestFindtype(unittest.TestCase):

    def test_png(self):
        for png in os.listdir("images"):
            if png.endswith(".png"):
                ftype = filemagic.findtype(os.path.join("images", png))
                self.assertEqual(ftype, "PNG")

    def test_jpg(self):
        for jpg in os.listdir("images"):
            if jpg.endswith(".jpg") or jpg.endswith(".jpeg"):
                ftype = filemagic.findtype(os.path.join("images", jpg))
                self.assertEqual(ftype, "JPEG")

    def test_tif(self):
        for tif in os.listdir("images"):
            if tif.endswith(".tif") or tif.endswith(".tiff"):
                ftype = filemagic.findtype(os.path.join("images", tif))
                self.assertEqual(ftype, "TIFF")

    def test_gif89a(self):
        self.assertEqual(1,0)
        for gif in os.listdir("images"):
            if gif.endswith(".gif"):
                ftype = filemagic.findtype(os.path.join("images", gif))
                self.assertEqual(ftype, "GIF89a")


if __name__ == "__main__":
    unittest.main()
