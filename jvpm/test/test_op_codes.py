"""this is a test for op_codes"""
# utilizes NumPy package to handle 32 bit int over/underflow in Java
import unittest
from unittest.mock import patch, call
import numpy
from jvpm.op_codes import OpCodes
from jvpm.op_codes import dup
from jvpm.op_codes import iconst_m1, iconst_0, iconst_1, iconst_2
from jvpm.op_codes import iconst_3, iconst_4, iconst_5
from jvpm.op_codes import iload, iload_0, iload_1, iload_2, iload_3
from jvpm.op_codes import istore, istore_0, istore_1, istore_2, istore_3
from jvpm.op_codes import iadd, isub, imul, idiv, irem
from jvpm.op_codes import iand, ineg, ior, ixor, ishr, ishl, iushr
from jvpm.op_codes import i2b, i2c, i2d, i2f, i2l, i2s
from jvpm.op_codes import lshl, lshr, land, lcmp, lushr
numpy.warnings.filterwarnings("ignore")


class TestOpCodes(unittest.TestCase):
    """this class tests the op_codes class"""
    @patch('builtins.print')
    def test_op_codes(self, mock_patch):
        """this method performs the op code test"""
        op_code = OpCodes()
        op_code.parse_codes(143)
        # self.assertEqual(mock_patch.mock_calls, [call('iconst_0'),
        #                                          call('iconst_4'),
        #                                          call('iconst_4'),
        #                                          call('iconst_3'),
        #                                          call('istore_1'),
        #                                          call('iconst_0'),
        #                                          call('iconst_1'),
        #                                          call('iconst_1'),
        #                                          call('iconst_1'),
        #                                          call('iconst_2'),
        #                                          call('iconst_1'),
        #                                          call('iconst_m1'),
        #                                          call('iconst_0'),
        #                                          call('iconst_m1'),
        #                                          call('iconst_1'),
        #                                          call('iconst_2'),
        #                                          call('iconst_3'),
        #                                          call('iconst_2'),
        #                                          call('aload_0'),
        #                                          call('invokespecial'),
        #                                          call('return'),
        #                                          call('iconst_4'),
        #                                          call('iconst_3'),
        #                                          call('iconst_5'),
        #                                          call('iconst_5'),
        #                                          call('iconst_3'),
        #                                          call('iconst_m1'),
        #                                          call('iconst_3'),
        #                                          call('iconst_1'),
        #                                          call('istore_1'),
        #                                          call('iinc'),
        #                                          call('return'),
        #                                          call('iconst_4'),
        #                                          call('iconst_3'),
        #                                          call('iconst_m1'),
        #                                          call('idiv')])

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
        """tests iconst_1 method, expected value 1"""
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

    def test_istore(self):
        """tests istore method"""
        test = OpCodes()
        length = len(test.local_array)
        test.stack.push_op(3)
        test.stack.push_op(2)
        test.stack.push_op(1)
        test.stack.push_op(0)
        for i in range(0, length):
            istore(test, i)
            self.assertEqual(test.local_array[i], i)

    def test_istore_0(self):
        """tests istore_0 method"""
        test = OpCodes()
        test.stack.push_op(0)
        istore_0(test)
        self.assertEqual(test.local_array[0], 0)

    def test_istore_1(self):
        """tests istore_1 method"""
        test = OpCodes()
        test.stack.push_op(1)
        istore_1(test)
        self.assertEqual(test.local_array[1], 1)

    def test_istore_2(self):
        """test istore_2 method"""
        test = OpCodes()
        test.stack.push_op(2)
        istore_2(test)
        self.assertEqual(test.local_array[2], 2)

    def test_istore_3(self):
        """tests istore_3 method"""
        test = OpCodes()
        test.stack.push_op(3)
        istore_3(test)
        self.assertEqual(test.local_array[3], 3)

    def test_iload(self):
        """tests iload method"""
        test = OpCodes()
        #tests every load index from 0 to length
        length = len(test.local_array)
        for i in range(0, length):
            iload(test, i)
            self.assertEqual(test.stack.peek(), test.local_array[i])

    def test_iload_0(self):
        """tests iload_0 opcode"""
        test = OpCodes()
        iload_0(test)
        self.assertEqual(test.stack.peek(), test.local_array[0])

    def test_iload_1(self):
        """tests iload_1 opcode"""
        test = OpCodes()
        iload_1(test)
        self.assertEqual(test.stack.peek(), test.local_array[1])

    def test_iload_2(self):
        """tests iload_2 opcode"""
        test = OpCodes()
        iload_2(test)
        self.assertEqual(test.stack.peek(), test.local_array[2])

    def test_iload_3(self):
        """tests iload_3 opcode"""
        test = OpCodes()
        iload_3(test)
        self.assertEqual(test.stack.peek(), test.local_array[3])

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
        """ Test the iand (Integer And) opcode """
        ops = OpCodes()
        # iand (240 & 15) should produce (0)
        ops.stack.push_op(240)
        ops.stack.push_op(15)
        iand(ops)
        self.assertEqual(ops.stack.pop_op(), 0)
        # iand (43,690 & 50,790) should produce (33314)
        ops.stack.push_op(43690)
        ops.stack.push_op(50790)
        iand(ops)
        self.assertEqual(ops.stack.pop_op(), 33314)
        # iand (-2,147,483,647 & -1) should produce (-2,147,483,647)
        ops.stack.push_op(-2147483647)
        ops.stack.push_op(-1)
        iand(ops)
        self.assertEqual(ops.stack.pop_op(), -2147483647)

    def test_ineg(self):
        """ Test the ineg (Integer Negate) opcode """
        ops = OpCodes()
        # ineg(254) should produce (-255)
        ops.stack.push_op(254)
        ineg(ops)
        self.assertEqual(ops.stack.pop_op(), -255)
        # ineg(0) should produce (-1)
        ops.stack.push_op(0)
        ineg(ops)
        self.assertEqual(ops.stack.pop_op(), -1)
        # ineg(2,147,483,647) sould produce (-2,147,483,648)
        ops.stack.push_op(2147483647)
        ineg(ops)
        self.assertEqual(ops.stack.pop_op(), -2147483648)

    def test_ior(self):
        """ Test the ior (Integer Or) opcode """
        ops = OpCodes()
        # ior(240 | 15) should produce (255)
        ops.stack.push_op(240)
        ops.stack.push_op(15)
        ior(ops)
        self.assertEqual(ops.stack.pop_op(), 255)
        # ior(2,147,483,647 | -2,147,483,648) should produce (-1)
        ops.stack.push_op(2147483647)
        ops.stack.push_op(-2147483648)
        ior(ops)
        self.assertEqual(ops.stack.pop_op(), -1)

    def test_ixor(self):
        """ Test the ixor (Integer Exclusive Or) opcode """
        ops = OpCodes()
        # ixor(255 ^ 129) should produce (126)
        ops.stack.push_op(255)
        ops.stack.push_op(129)
        ixor(ops)
        self.assertEqual(ops.stack.peek(), 126)

    def test_ishl(self):
        """ Test the ishl (Integer Shift Left) opcode """
        ops = OpCodes()
        ops.stack.push_op(0)
        ops.stack.push_op(0)
        ishl(ops)
        self.assertEqual(ops.stack.pop_op(), 0)

        ops.stack.push_op(1)
        ops.stack.push_op(1)
        ishl(ops)
        self.assertEqual(ops.stack.pop_op(), 2)

        ops.stack.push_op(1)
        ops.stack.push_op(3)
        ishl(ops)
        self.assertEqual(ops.stack.pop_op(), 8)

        ops.stack.push_op(1)
        ops.stack.push_op(8)
        ishl(ops)
        self.assertEqual(ops.stack.pop_op(), 256)

        ops.stack.push_op(8)
        ops.stack.push_op(4)
        ishl(ops)
        self.assertEqual(ops.stack.pop_op(), 128)

        ops.stack.push_op(16)
        ops.stack.push_op(2)
        ishl(ops)
        self.assertEqual(ops.stack.pop_op(), 64)

    def test_ishr(self):
        """ Test the ishr (Integer Arithmetic Shift Right) opcode """
        ops = OpCodes()
        ops.stack.push_op(0)
        ops.stack.push_op(0)
        ishr(ops)
        self.assertEqual(ops.stack.pop_op(), 0)

        ops.stack.push_op(8)
        ops.stack.push_op(3)
        ishr(ops)
        self.assertEqual(ops.stack.pop_op(), 1)

        ops.stack.push_op(256)
        ops.stack.push_op(6)
        ishr(ops)
        self.assertEqual(ops.stack.pop_op(), 4)
        ops.stack.push_op(16)
        ops.stack.push_op(3)
        ishr(ops)
        self.assertEqual(ops.stack.pop_op(), 2)

        ops.stack.push_op(32)
        ops.stack.push_op(2)
        ishr(ops)
        self.assertEqual(ops.stack.pop_op(), 8)

        ops.stack.push_op(16)
        ops.stack.push_op(2)
        ishr(ops)
        self.assertEqual(ops.stack.pop_op(), 4)

    def test_iushr(self):
        """ Test the iushr (Logical Shift Right) opcode """
        ops = OpCodes()
        # iushr(255 >>> 2) should produce (63)
        ops.stack.push_op(255)
        ops.stack.push_op(2)
        iushr(ops)
        self.assertEqual(ops.stack.pop_op(), 63)
        # iushr(-1 >> 4) should produce (268,435,455)
        ops.stack.push_op(-1)
        ops.stack.push_op(4)
        iushr(ops)
        self.assertEqual(ops.stack.pop_op(), 268435455)

    def test_i2b(self):
        """Test conversion of integer to byte dawg"""
        ops = OpCodes()
        ops.stack.push_op(42)
        i2b(ops)
        assert isinstance(ops.stack.peek(), numpy.int8)

    def test_i2c(self):
        """Test conversion of integer to byte"""
        ops = OpCodes()
        ops.stack.push_op(33)
        i2c(ops)
        assert isinstance(ops.stack.peek(), str)

    def test_i2d(self):
        """Test conversion of integer to double"""
        ops = OpCodes()
        ops.stack.push_op(42)
        i2d(ops)
        assert isinstance(ops.stack.peek(), numpy.float64)

    def test_i2f(self):
        """Test conversion of integer to float"""
        ops = OpCodes()
        ops.stack.push_op(42)
        i2f(ops)
        assert isinstance(ops.stack.peek(), numpy.float32)

    def test_i2l(self):
        """Test conversion of integer to long"""
        ops = OpCodes()
        ops.stack.push_op(42)
        i2l(ops)
        assert isinstance(ops.stack.peek(), numpy.int64)

    def test_i2s(self):
        """Test conversion of integer to short"""
        ops = OpCodes()
        ops.stack.push_op(42)
        i2s(ops)
        assert isinstance(ops.stack.peek(), numpy.int16)

    def test_dup(self):
        """Test dup"""
        ops = OpCodes()
        ops.stack.push_op(15)
        dup(ops)
        self.assertEqual(ops.stack.pop_op(), 15)
        self.assertEqual(ops.stack.pop_op(), 15)

        ops.stack.push_op(0)
        dup(ops)
        self.assertEqual(ops.stack.pop_op(), 0)
        self.assertEqual(ops.stack.pop_op(), 0)

        ops.stack.push_op('foo')
        dup(ops)
        self.assertEqual(ops.stack.pop_op(), 'foo')
        self.assertEqual(ops.stack.pop_op(), 'foo')

    def test_lshl(self):
        """Test lshl (long shift left)"""
        ops = OpCodes()
        ops.stack.push_op(2)
        ops.stack.push_op(2)
        lshl(ops)
        assert isinstance(ops.stack.peek(), numpy.int64)
        self.assertEqual(ops.stack.pop_op(), numpy.int64(8))

        ops.stack.push_op(66)
        ops.stack.push_op(2)
        lshl(ops)
        assert isinstance(ops.stack.peek(), numpy.int64)
        self.assertEqual(ops.stack.pop_op(), numpy.int64(8))

    def test_lshr(self):
        """Test lshr (long shift right)"""
        ops = OpCodes()
        ops.stack.push_op(3)
        ops.stack.push_op(42)
        lshr(ops)
        assert isinstance(ops.stack.peek(), numpy.int64)
        self.assertEqual(ops.stack.pop_op(), numpy.int64(5))

        ops.stack.push_op(66)
        ops.stack.push_op(2)
        lshr(ops)
        assert isinstance(ops.stack.peek(), numpy.int64)
        self.assertEqual(ops.stack.pop_op(), numpy.int64(0))

        ops.stack.push_op(2)
        ops.stack.push_op(-15)
        lshr(ops)
        assert isinstance(ops.stack.peek(), numpy.int64)
        self.assertEqual(ops.stack.pop_op(), numpy.int64(-4))

    def test_land(self):
        """Test land (logical bitwise long AND)"""
        ops = OpCodes()
        ops.stack.push_op(42)
        i2l(ops)
        ops.stack.push_op(6)
        i2l(ops)
        land(ops)
        assert isinstance(ops.stack.peek(), numpy.int64)
        self.assertEqual(ops.stack.pop_op(), numpy.int64(2))

    def test_lcmp(self):
        """Test lcmp (compare 2 longs)"""
        ops = OpCodes()
        ops.stack.push_op(42)
        i2l(ops)
        ops.stack.push_op(41)
        i2l(ops)
        lcmp(ops)
        self.assertEqual(ops.stack.pop_op(), -1)

        ops.stack.push_op(42)
        i2l(ops)
        ops.stack.push_op(43)
        i2l(ops)
        lcmp(ops)
        self.assertEqual(ops.stack.pop_op(), 1)

        ops.stack.push_op(42)
        i2l(ops)
        ops.stack.push_op(42)
        i2l(ops)
        lcmp(ops)
        self.assertEqual(ops.stack.pop_op(), 0)

    def test_lushr(self):
        """test lushr (bitwise logical shift right with zero extension)"""
        ops = OpCodes()
        ops.stack.push_op(3)
        ops.stack.push_op(42)
        lushr(ops)
        assert isinstance(ops.stack.peek(), numpy.int64)
        self.assertEqual(ops.stack.pop_op(), numpy.int64(5))

        ops.stack.push_op(66)
        ops.stack.push_op(2)
        lushr(ops)
        assert isinstance(ops.stack.peek(), numpy.int64)
        self.assertEqual(ops.stack.pop_op(), numpy.int64(0))

        ops.stack.push_op(2)
        ops.stack.push_op(-15)
        lushr(ops)
        assert isinstance(ops.stack.peek(), numpy.int64)
        self.assertEqual(ops.stack.pop_op(), numpy.int64(-4))
