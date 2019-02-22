"""test stack"""
from unittest import TestCase
from jvpm.jvm_stack import JvmStack
class TestStack(TestCase):
    """test stack"""
    def test_constructor(self):
        """test the constructor"""
        stack = JvmStack()
        self.assertEqual(stack.stack, [])
    def test_push(self):
        """test the push_op method"""
        stack = JvmStack()
        stack.push_op(1)
        self.assertEqual(stack.stack, [1])
    def test_pop(self):
        """tests the pop_op method"""
        stack = JvmStack()
        stack.push_op(1)
        self.assertEqual(stack.pop_op(), 1)
        with self.assertRaises(IndexError):
            stack.pop_op()
    def test_peek(self):
        """test the peek method"""
        stack = JvmStack()
        stack.push_op(1)
        stack.push_op(2)
        self.assertEqual(stack.peek(), 2)
        stack.pop_op()
        self.assertEqual(stack.peek(), 1)
        stack.pop_op()
        with self.assertRaises(IndexError):
            stack.peek()
