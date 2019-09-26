"""tests the case where the stack is empty"""
from unittest import TestCase
from jvpm.jvm_stack import JvmStack, EmptyStackError


class TestStackEmpty(TestCase):
    """tests the case where the stack is empty"""
    def test_stack_empty(self):
        """tests the case where the stack is empty"""
        jvm_stack = JvmStack()
        with self.assertRaises(EmptyStackError):
            jvm_stack.pop_op()
