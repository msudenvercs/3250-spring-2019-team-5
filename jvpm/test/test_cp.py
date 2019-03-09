"""test constant pool"""
from unittest import TestCase
from jvpm.constant_pool_parser import ConstantPoolParser


class TestCp(TestCase):
    """test constant pool"""

    def test_cp(self):
        """test constaant pool"""
        constant_pool = ConstantPoolParser(
            b"abcdefghij\x03abcd\x04abcd\x05abcdefgh\x06abcdefgh\x07ab\x08ab\x09abcd\x0aabcd\x0babcd\x0cabcd\x0fabc\x10ab\x12abcd")
        self.assertEqual(constant_pool.get_single_constant(), b"\x03abcd")
        self.assertEqual(constant_pool.offset, 15)
        self.assertEqual(constant_pool.get_single_constant(), b"\x04abcd")
        self.assertEqual(constant_pool.offset, 20)
        self.assertEqual(constant_pool.get_single_constant(), b"\x05abcdefgh")
        self.assertEqual(constant_pool.offset, 29)
        self.assertEqual(constant_pool.get_single_constant(), b"\x06abcdefgh")
        self.assertEqual(constant_pool.offset, 38)
        self.assertEqual(constant_pool.get_single_constant(), b"\x07ab")
        self.assertEqual(constant_pool.offset, 41)
        self.assertEqual(constant_pool.get_single_constant(), b"\x08ab")
        self.assertEqual(constant_pool.offset, 44)
        self.assertEqual(constant_pool.get_single_constant(), b"\x09abcd")
        self.assertEqual(constant_pool.offset, 49)
        self.assertEqual(constant_pool.get_single_constant(), b"\x0aabcd")
        self.assertEqual(constant_pool.offset, 54)
        self.assertEqual(constant_pool.get_single_constant(), b"\x0babcd")
        self.assertEqual(constant_pool.offset, 59)
        self.assertEqual(constant_pool.get_single_constant(), b"\x0cabcd")
        self.assertEqual(constant_pool.offset, 64)
        self.assertEqual(constant_pool.get_single_constant(), b"\x0fabc")
        self.assertEqual(constant_pool.offset, 68)
        self.assertEqual(constant_pool.get_single_constant(), b"\x10ab")
        self.assertEqual(constant_pool.offset, 71)
        self.assertEqual(constant_pool.get_single_constant(), b"\x12abcd")
        self.assertEqual(constant_pool.offset, 76)
