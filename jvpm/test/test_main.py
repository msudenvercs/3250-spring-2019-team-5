"""test main"""
import sys
from unittest import TestCase
from unittest.mock import call, Mock, mock_open, patch
import jvpm.main
class TestMain(TestCase):
    """test main"""
    def test_main(self):
        """test main"""
        self.assertEqual(47+36, 83)
        sys.stdout = Mock()
        mock_object = mock_open(read_data=b'\xCA\xFE\xBA\xBE\x00\x00\x004\x00\x1d')
        with patch("builtins.input", return_value="Test.class"),\
patch("builtins.open", mock_object):
            jvpm.main.main()
        sys.stdout.assert_has_calls([call.write(r"b'The magic number is \xca\xfe\xba\xbe"
                                                r" The minor version is \x00\x00"
                                                r" The major version is \x004"
                                                r" The constant pool count is \x00\x1d'"),\
call.write("\n")])
