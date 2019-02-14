import unittest
from unittest.mock import mock_open, patch
from jvpm.class_file import ClassFile
class TestClassFile(unittest.TestCase):
    def setUp(self):
        m = mock_open(read_data=b'\xCA\xFE\xBA\xBE\x00\x00\x004\x00\x1d')
        with patch(__name__ + '.open', m):
            self.cf = ClassFile('Test.class')

    def test_magic(self):
        self.assertEqual(self.cf.get_magic(), b'\xCA\xFE\xBA\xBE')

    def test_minor(self):
        self.assertEqual(self.cf.get_minor(), b"\x00\x00")

    def test_major(self):
        self.assertEqual(self.cf.get_major(), b'\x004')

    def test_constant_pool_count(self):
        self.assertEqual(self.cf.get_constant_pool_count(),b"\x00\x1d")

