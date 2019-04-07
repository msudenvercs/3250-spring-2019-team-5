import unittest
from jvpm.jvm_stack import JvmStack
from jvpm.method_table import scanner

class TestScanner(unittest.TestCase):
    """class to test the scanner"""        
    def test_scanner(self):
        """method to test the scanner"""
        stack = JvmStack()
        stack.push_op(0)
        stack.push_op(0)
        scanner(stack)
        self.assertEqual(stack.pop_op(), 'scanner')
        