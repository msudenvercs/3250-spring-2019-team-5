"""test"""
from unittest import TestCase
from jvpm.jvm_stack import JvmStack, push_twice, pop_twice
class TestDoublePushPop(TestCase):
    """test"""
    def test_double_stack_ops(self):
        """test"""
        stack = JvmStack()
        stack.push_op(27, push_twice)
        stack.push_op("the sky is blue", push_twice)
        stack.push_op([[]], push_twice)
        self.assertEqual(stack.stack, [27, None, "the sky is blue", None, [[]], None])
        self.assertEqual(stack.peek(), [[]])
        stack.pop_op(pop_twice)
        self.assertEqual(stack.peek(), "the sky is blue")
        stack.pop_op(pop_twice)
        self.assertEqual(stack.peek(), 27)
        stack.pop_op(pop_twice)
        self.assertEqual(stack.stack, [])
