"""tests ldc and getstatic"""
from unittest import TestCase
from jvpm.op_codes import OpCodes


class TestLdcGetstatic(TestCase):
    """tests ldc and getstatic"""
    def test_getstatic(self):
        """tests ldc and getstatic"""
        op_codes = OpCodes()
        op_codes.set_data(
            b"abcdefgh\x00\x05\x03\xff\xff\xff\xff\x08\x00\x02" +
            b"\x01\x00\x05hello\x07ab\xb2\x00\x04\x12\x01")
        op_codes.parse_codes(len(op_codes.data) - 5)
        self.assertEqual(len(op_codes.stack.stack), 2)
        self.assertEqual(op_codes.stack.pop_op(), -1)
        self.assertEqual(op_codes.stack.pop_op(), b"\x07ab")
