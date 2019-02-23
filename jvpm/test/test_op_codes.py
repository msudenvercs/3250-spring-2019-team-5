"""this is a test for op_codes"""
import unittest
from unittest.mock import patch, call
from jvpm.op_codes import OpCodes
class TestOpCodes(unittest.TestCase):
    """this class tests the op_codes class"""
    @patch('builtins.print')
    def test_op_codes(self, mock_patch):
        """this method performs the op code test"""
        op_code = OpCodes()
        op_code.parse_codes(0)
        self.assertEqual(mock_patch.mock_calls,
[call('istore_1'),
 call('iconst_1'),
 call('iconst_1'),
 call('iconst_1'),
 call('iconst_1'),
 call('iconst_1'),
 call('aload_0'),
 call('invokespecial'),
 call('return'),
 call('iconst_1'),
 call('istore_1'),
 call('iinc'),
 call('return')])
    def test_not_implmented(self):
        """this method tests the OpCodes class"""
        self.assertEqual(OpCodes().interpret(0), 'not implemented')

    def test_mph1(self):
        """a"""
        self.assertEqual(1+1,2)
        with self.assertRaises(KeyError):
            OpCodes().interpret(1)
