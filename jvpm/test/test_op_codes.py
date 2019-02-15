"""this is a test"""
import unittest
from jvpm.op_codes import OpCodes
class TestOpCodes(unittest.TestCase):
    """this class tests the OpCodes class"""
    def test_not_implmented(self):
        """this method tests the OpCodes class"""
        self.assertEqual(OpCodes().interpret(0), 'not implemented')

    def test_mph1(self):
        """a"""
        self.assertEqual(OpCodes().mph1(), OpCodes().table)
        with self.assertRaises(KeyError):
            OpCodes().interpret(1)
