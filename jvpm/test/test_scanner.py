import unittest
from jvpm.op_codes import OpCodes
from jvpm.method_table import scanner, nextInt

class TestScanner(unittest.TestCase):
    """class to test the scanner"""        
    def test_scanner(self):
        """method to test the scanner"""
        stack = OpCodes()
        stack.stack.push_op(0)
        stack.stack.push_op(0)
        scanner(stack)
        self.assertEqual(stack.stack.pop_op(), 'scanner')

    def test_nextInt(self):
        """method to test the scanner"""
        stack = OpCodes()
        stack.stack.push_op(0)
        nextInt(stack)
        self.assertEqual(stack.stack.pop_op(), 0)

        