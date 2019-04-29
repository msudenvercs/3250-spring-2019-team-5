"""test constant pool"""
from unittest import TestCase
from jvpm.constant_pool_parser import ConstantPoolParser


class TestCp(TestCase):
    """test constant pool"""

    def test_cp(self):
        """test constaant pool"""
        constant_pool = ConstantPoolParser(
            b"abcdefgh\x00\x11\x03abcd\x04abcd\x05abcdefgh\x06abcdefgh\x07ab\x08ab" +
            b"\x09abcd\x0aabcd\x0babcd\x0cabcd\x0fabc\x10ab\x12abcd\x01\x00\x0aabcdefghij")
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
        self.assertEqual(
            constant_pool.get_single_constant(),
            b"\x01\x00\x0aabcdefghij")
        self.assertEqual(constant_pool.offset, 89)
# reset the parser so that I can test my get_all_constants method.
        constant_pool.offset = 10
        pool = constant_pool.get_all_constants()
        self.assertEqual(pool,
                         [None,
                          b"\x03abcd",
                          b"\x04abcd",
                          b"\x05abcdefgh",
                          None,
                          b"\x06abcdefgh",
                          None,
                          b"\x07ab",
                          b"\x08ab",
                          b"\x09abcd",
                          b"\x0aabcd",
                          b"\x0babcd",
                          b"\x0cabcd",
                          b"\x0fabc",
                          b"\x10ab",
                          b"\x12abcd",
                          b"\x01\x00\x0aabcdefghij"])
        self.assertEqual(constant_pool.offset, 89)
