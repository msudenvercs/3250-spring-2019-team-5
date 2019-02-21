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
        op_code.parse_codes()
        self.assertEqual(mock_patch.mock_calls, [
            call.write('aload_0'),
            call.write('invokespecial'),
            call.write('return'),
            call.write('iconst_1'),
            call.write('istore_1'),
            call.write('iinc'),
            call.write('return')
        ])
    def test_not_implmented(self):
        """this method tests the OpCodes class"""
        self.assertEqual(OpCodes().interpret(0), 'not implemented')

    def test_mph1(self):
        """a"""
        self.assertEqual(OpCodes().mph1(), OpCodes().table)
        with self.assertRaises(KeyError):
            OpCodes().interpret(1)
