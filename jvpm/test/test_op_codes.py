"""this is a test"""
import unittest
from jvpm.op_codes import OpCodes
from unittest.mock import patch, call
class TestOpCodes(unittest.TestCase):
    @patch('builtins.print')
    def test_op_codes(self, mock_patch):
        oc = OpCodes()
        oc.parse_codes()
        self.assertEqual(mock_patch.mock_calls, [
            call.write('aload_0'),
            call.write('invokespecial'),
            call.write('return'),
            call.write('iconst_1'),
            call.write('istore_1'),
            call.write('iinc'),
            call.write('return')
        ])
    """this class tests the OpCodes class"""
    def test_not_implmented(self):
        """this method tests the OpCodes class"""
        self.assertEqual(OpCodes().interpret(0), 'not implemented')

    def test_mph1(self):
        """a"""
        self.assertEqual(OpCodes().mph1(), OpCodes().table)
        with self.assertRaises(KeyError):
            OpCodes().interpret(1)
