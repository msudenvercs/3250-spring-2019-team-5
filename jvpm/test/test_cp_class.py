"""tests constant pool class"""
from unittest import TestCase
from jvpm.constant_pool import ConstantPool
from jvpm.constant_pool_parser import ConstantPoolParser
from jvpm.jvm_stack import JvmStack
from jvpm.op_codes import OpCodes


class TestCpClass(TestCase):
    """tests constant pool class"""

    def test_make_constant_pool(self):
        """tests the making of constant pools"""
        cp_parser = ConstantPoolParser(b"abcdefgh\x00\x01")
        pool = cp_parser.make_constant_pool()
        self.assertEqual(pool.constants, [None])
        self.assertEqual(type(pool), ConstantPool)

    def test_constant_pool_constructor(self):
        """tests the constant pool constructor"""
        pool = ConstantPool([])
        self.assertEqual(type(pool), ConstantPool)
        self.assertEqual(pool.constants, [])

    def test_lookup_constant(self):
        """Tests the looking up of constants"""
# I know that the constant pool will contain bytes objects, but I'm just
# testing whether the right entry is returned here.
        pool = ConstantPool(list(range(65536)))
        constant = pool.lookup_constant(b"\xff\xfe")
# tests if this is really unsigned big-endian order.
        self.assertEqual(constant, 65534)

    def test_load_constant(self):
        """tests the loading of constants"""
        stack = JvmStack()
        pool = ConstantPool([b"\x03\xff\xff\xff\xfe", b"\x08\x00\x05hello"])
        pool.load_constant(b"\x00\x00", stack)
        pool.load_constant(b"\x00\x01", stack)
        self.assertEqual(stack.pop_op(), "hello")
        self.assertEqual(stack.pop_op(), -2)

    def test_set_data(self):
        """tests set_data method"""
        op_codes = OpCodes()
        op_codes.constant_pool = []
        op_codes.set_data(b"abcdefgh\x00\x01")
        self.assertEqual(op_codes.constant_pool.constants, [None])
