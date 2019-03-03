"""this is a test for op_codes"""
import unittest
from unittest.mock import patch, call
import numpy
from jvpm.op_codes import iconst_m1, iconst_0, iconst_1, iconst_2
from jvpm.op_codes import iconst_3, iconst_4, iconst_5
from jvpm.op_codes import iadd, isub
from jvpm.op_codes import imul
from jvpm.op_codes import idiv, irem
from jvpm.op_codes import OpCodes
from jvpm.op_codes import iand, ineg, ior, ixor
numpy.warnings.filterwarnings("ignore")


class TestOpCodes(unittest.TestCase):
    """this class tests the op_codes class"""
    @patch('builtins.print')
    def test_op_codes(self, mock_patch):
        """this method performs the op code test"""
        op_code = OpCodes()
        op_code.parse_codes(0)
        self.assertEqual(mock_patch.mock_calls,
                         [call('istore_1'),
                          call('iconst_1'),
                          call('iconst_1'),
                          call('iconst_1'),
                          call('iconst_1'),
                          call('iconst_1'),
                          call('aload_0'),
                          call('invokespecial'),
                          call('return'),
                          call('iconst_1'),
                          call('istore_1'),
                          call('iinc'),
                          call('return')])

    def test_not_implmented(self):
        """this method tests the OpCodes class"""
        self.assertEqual(OpCodes().interpret(0), 'not implemented')

    def test_iconst_m1(self):
        """tests iconst_m1 method, expected value -1"""
        test = OpCodes()
        iconst_m1(test)
        self.assertEqual(test.stack.peek(), -1)

    def test_iconst_0(self):
        """tests iconst_0 method, expected value 0"""
        test = OpCodes()
        iconst_0(test)
        self.assertEqual(test.stack.peek(), 0)

    def test_iconst_1(self):
        """tests iconst_1 method, rexpected value 1"""
        test = OpCodes()
        iconst_1(test)
        self.assertEqual(test.stack.peek(), 1)

    def test_iconst_2(self):
        """tests iconst_2 method, expected value 2"""
        test = OpCodes()
        iconst_2(test)
        self.assertEqual(test.stack.peek(), 2)

    def test_iconst_3(self):
        """tests iconst_3 method, expected value 3"""
        test = OpCodes()
        iconst_3(test)
        self.assertEqual(test.stack.peek(), 3)

    def test_iconst_4(self):
        """tests iconst_4 method, expected value 4"""
        test = OpCodes()
        iconst_4(test)
        self.assertEqual(test.stack.peek(), 4)

    def test_iconst_5(self):
        """tests iconst_5 method, expected value 5"""
        test = OpCodes()
        iconst_5(test)
        self.assertEqual(test.stack.peek(), 5)

    def test_mph1(self):
        """a"""
        self.assertEqual(1 + 1, 2)
        with self.assertRaises(KeyError):
            OpCodes().interpret(1)

    def test_add_subtract(self):
        """tests the iadd and isub opcodes"""
        op_code = OpCodes()
        op_code.stack.push_op(numpy.int32(2000000000))
        op_code.stack.push_op(numpy.int32(1000000000))

        iadd(op_code)
        self.assertEqual(op_code.stack.peek(), -1294967296)
        op_code.stack.push_op(numpy.int32(10))
        op_code.stack.push_op(numpy.int32(3))
        isub(op_code)
        self.assertEqual(op_code.stack.peek(), 7)
    def test_multiply(self):
        """tests the imul opcode"""
        op_code = OpCodes()
        op_code.stack.push_op(numpy.int32(2000000000))
        op_code.stack.push_op(numpy.int32(1000000000))

        imul(op_code)
        self.assertEqual(op_code.stack.peek(), 1321730048)
    def test_divide(self):
        """tests the idiv opcode"""
        op_code = OpCodes()
        op_code.stack.push_op(numpy.int32(128))
        op_code.stack.push_op(numpy.int32(-3))

        idiv(op_code)
        self.assertEqual(op_code.stack.peek(), -42)
    def test_mod(self):
        """tests the irem opcode"""
        op_code = OpCodes()
        op_code.stack.push_op(numpy.int32(128))
        op_code.stack.push_op(numpy.int32(-3))

        irem(op_code)
        self.assertEqual(op_code.stack.peek(), 2)

    def test_iand(self):
        """ Test the iand opcode using 240 (1111 0000) and 15 (0000 1111).
        Expected result: 0 (0000 0000)
        """
        ops = OpCodes()
        ops.stack.push_op(240)
        ops.stack.push_op(15)
        iand(ops)
        self.assertEqual(ops.stack.peek(), 0)

    def test_ineg(self):
        """ Test the ineg opcode using 254.
        Expected result: -255
        """
        ops = OpCodes()
        ops.stack.push_op(254)
        ineg(ops)
        self.assertEqual(ops.stack.peek(), -255)

    def test_ior(self):
        """Test the ior opcode using 240 (1111 0000) and 15 (0000 1111)
        Expected result: 255 (1111 1111)
        """
        ops = OpCodes()
        ops.stack.push_op(240)
        ops.stack.push_op(15)
        ior(ops)
        self.assertEqual(ops.stack.peek(), 255)

    def test_ixor(self):
        """Test the ixor opcode using 255 (1111 1111) and 129 (1000 0001)
        Expected result: 126 (0111 1110)
        """
        ops = OpCodes()
        ops.stack.push_op(255)
        ops.stack.push_op(129)
        ixor(ops)
        self.assertEqual(ops.stack.peek(), 126)
