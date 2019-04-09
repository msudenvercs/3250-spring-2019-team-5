"""this is a test for Scanner"""
import unittest
from unittest.mock import patch
from jvpm.op_codes import OpCodes
from jvpm.method_table import scanner, next_int

class TestScanner(unittest.TestCase):
    """class to test the scanner"""
    def test_scanner(self):
        """method to test the scanner"""
        stack = OpCodes()
        stack.stack.push_op(0)
        stack.stack.push_op(0)
        scanner(stack)
        self.assertEqual(stack.stack.pop_op(), 'scanner')

    def test_next_int(self):
        """method to test the scanner"""
        stack = OpCodes()
        stack.stack.push_op(0)
        with patch("builtins.input", side_effect=["10"]):
            next_int(stack)
        self.assertEqual(stack.stack.pop_op(), 10)
