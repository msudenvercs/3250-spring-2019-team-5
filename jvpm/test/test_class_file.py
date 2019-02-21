"""this is a test"""
import unittest
from unittest.mock import mock_open, patch
from jvpm.class_file import ClassFile
class TestClassFile(unittest.TestCase):
    """this class tests the ClassFileClass"""
    def setUp(self):
        """set up the test"""
        mock_object = mock_open(read_data=b'\xCA\xFE\xBA\xBE\x00\x00\x004\x00\x0f')
        with patch('builtins.open', mock_object):
            self.class_file = ClassFile('jvpm/Test.class')

    def test_magic(self):
        """tests the get_magic method"""
        self.assertEqual(self.class_file.get_magic(), b'\xCA\xFE\xBA\xBE')

    def test_minor(self):
        """tests the get_minor method"""
        self.assertEqual(self.class_file.get_minor(), b"\x00\x00")

    def test_major(self):
        """tests the get_major method"""
        self.assertEqual(self.class_file.get_major(), b'\x004')

    def test_constant_pool_count(self):
        """tests the get_constant_pool_count method"""
        self.assertEqual(self.class_file.get_constant_pool_count(), b"\x00\x0f")
