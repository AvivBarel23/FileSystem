from FileSystem import FileSystem
import unittest


class test(unittest.TestCase):
    def test(self):
        fs = FileSystem()

        #test1- ls on empty dir
        self.assertEqual(fs.ls("/"), [])

        #test2 - ls on nonhomogeneous dir
        fs.create_file("/a", "abcdefg")
        fs.mkdir("/b")
        self.assertEqual(fs.ls("/"), ["a","b"])

        #test3 - ls after create file
        fs.create_file("/b/c", "abcdefg")
        self.assertEqual(fs.ls("/b"), ["c"])

        #test4-ls on file
        self.assertEqual(fs.ls("/b/c"), ["c"])

        #test5-create_dirs_and_files
        fs.create_file("/b/foo/bar", "abcdefg")
        self.assertEqual(fs.ls("/b/foo"), ["bar"])


