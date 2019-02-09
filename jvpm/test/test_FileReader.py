from unittest import TestCase
from jvpm.parsing import FileReader
from unittest.mock import mock_open, patch
class TestFileReader(TestCase):
    def test_constructor(self):
        f = FileReader.FileReader("x.class")
        self.assertEqual(f.name,"x.class")
    def test_read(self):
        with patch("builtins.open",mock_open(read_data=b"hello")) as code:
            self.assertEqual(FileReader.FileReader("builtins.open").read(),b"hello")
