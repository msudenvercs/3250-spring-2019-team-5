"""this is a test for op_codes"""
# utilizes NumPy package to handle 32 bit int over/underflow in Java
import unittest
from unittest.mock import patch, call
import numpy
numpy.warnings.filterwarnings("ignore")
import jvpm.op_codes as ops

class TestOpCodes(unittest.TestCase):
    """this class tests the op_codes class"""
    @patch('builtins.print')
    def test_op_codes(self, mock_patch):
        """this method performs the op code test"""
        op_code = ops.OpCodes()
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

    def test_aload(self):
        """tests the aload opcode method"""
        test = ops.OpCodes()
        for i in range(0, len(test.local_array)):
            ops.aload(test, i)
            self.assertEqual(test.stack.peek(), test.local_array[i])

    def test_not_implmented(self):
        """this method tests the OpCodes class"""
        self.assertEqual(ops.OpCodes().interpret(0), 'not implemented')

    def test_iconst_m1(self):
        """tests iconst_m1 method, expected value -1"""
        test = ops.OpCodes()
        ops.iconst_m1(test)
        self.assertEqual(test.stack.peek(), -1)

    def test_iconst_0(self):
        """tests iconst_0 method, expected value 0"""
        test = ops.OpCodes()
        ops.iconst_0(test)
        self.assertEqual(test.stack.peek(), 0)

    def test_iconst_1(self):
        """tests iconst_1 method, expected value 1"""
        test = ops.OpCodes()
        ops.iconst_1(test)
        self.assertEqual(test.stack.peek(), 1)

    def test_iconst_2(self):
        """tests iconst_2 method, expected value 2"""
        test = ops.OpCodes()
        ops.iconst_2(test)
        self.assertEqual(test.stack.peek(), 2)

    def test_iconst_3(self):
        """tests iconst_3 method, expected value 3"""
        test = ops.OpCodes()
        ops.iconst_3(test)
        self.assertEqual(test.stack.peek(), 3)

    def test_iconst_4(self):
        """tests iconst_4 method, expected value 4"""
        test = ops.OpCodes()
        ops.iconst_4(test)
        self.assertEqual(test.stack.peek(), 4)

    def test_iconst_5(self):
        """tests iconst_5 method, expected value 5"""
        test = ops.OpCodes()
        ops.iconst_5(test)
        self.assertEqual(test.stack.peek(), 5)

    def test_iinc(self):
        """tests iinc method"""
        test = ops.OpCodes()
        for i in range(0, len(test.local_array)):
            ops.iinc(test, i, i)
            test.local_array[i] = i
            self.assertEqual(test.local_array[i], i)

    def test_istore(self):
        """tests istore method"""
        test = ops.OpCodes()
        test.stack.push_op(3)
        test.stack.push_op(2)
        test.stack.push_op(1)
        test.stack.push_op(0)
        for i in range(0, len(test.local_array)):
            ops.istore(test, i)
            self.assertEqual(test.local_array[i], i)

    def test_istore_0(self):
        """tests istore_0 method"""
        test = ops.OpCodes()
        test.stack.push_op(0)
        ops.istore_0(test)
        self.assertEqual(test.local_array[0], 0)

    def test_istore_1(self):
        """tests istore_1 method"""
        test = ops.OpCodes()
        test.stack.push_op(1)
        ops.istore_1(test)
        self.assertEqual(test.local_array[1], 1)

    def test_istore_2(self):
        """test istore_2 method"""
        test = ops.OpCodes()
        test.stack.push_op(2)
        ops.istore_2(test)
        self.assertEqual(test.local_array[2], 2)

    def test_istore_3(self):
        """tests istore_3 method"""
        test = ops.OpCodes()
        test.stack.push_op(3)
        ops.istore_3(test)
        self.assertEqual(test.local_array[3], 3)

    def test_lstore(self):
        """tests the lstore method for 64 bit longs"""
        test = ops.OpCodes()
        test.stack.push_op(numpy.int64(3), ops.push_twice)
        test.stack.push_op(numpy.int64(2), ops.push_twice)
        test.stack.push_op(numpy.int64(1), ops.push_twice)
        test.stack.push_op(numpy.int64(0), ops.push_twice)
        for i in range(0, len(test.local_array)):
            ops.lstore(test, i)
            self.assertEqual(test.local_array[i], numpy.int64(i))

    def test_fstore(self):
        """tests the fstore method for 32 bit floats"""
        test = ops.OpCodes()
        test.stack.push_op(numpy.float32(3), ops.push_twice)
        test.stack.push_op(numpy.float32(2), ops.push_twice)
        test.stack.push_op(numpy.float32(1), ops.push_twice)
        test.stack.push_op(numpy.float32(0), ops.push_twice)
        for i in range(0, len(test.local_array)):
            ops.fstore(test, i)
            self.assertEqual(test.local_array[i], numpy.float32(i))

    def test_lstore_0(self):
        """tests the lstore_0 opcode for 64 bit longs"""
        test = ops.OpCodes()
        test.stack.push_op(numpy.int64(0), ops.push_twice)
        ops.lstore_0(test)
        self.assertEqual(test.local_array[0], 0)

    def test_lstore_1(self):
        """tests the lstore_1 opcode for 64 bit longs"""
        test = ops.OpCodes()
        test.stack.push_op(numpy.int64(1), ops.push_twice)
        ops.lstore_1(test)
        self.assertEqual(test.local_array[1], 1)

    def test_lstore_2(self):
        """tests the lstore_2 opcode for 64 bit longs"""
        test = ops.OpCodes()
        test.stack.push_op(numpy.int64(2), ops.push_twice)
        ops.lstore_2(test)
        self.assertEqual(test.local_array[2], 2)

    def test_lstore_3(self):
        """tests the lstore_3 opcode for 64 bit longs"""
        test = ops.OpCodes()
        test.stack.push_op(numpy.int64(3), ops.push_twice)
        ops.lstore_3(test)
        self.assertEqual(test.local_array[3], 3)

    def test_fstore_0(self):
        """tests the fstore_0 opcode for 32 bit floats"""
        test = ops.OpCodes()
        test.stack.push_op(numpy.int64(0), ops.push_twice)
        ops.fstore_0(test)
        self.assertEqual(test.local_array[0], 0)

    def test_fstore_1(self):
        """tests the lstore_1 opcode for 32 bit floats"""
        test = ops.OpCodes()
        test.stack.push_op(numpy.float32(1), ops.push_twice)
        ops.fstore_1(test)
        self.assertEqual(test.local_array[1], 1)

    def test_fstore_2(self):
        """tests the fstore_2 opcode for 32 bit floats"""
        test = ops.OpCodes()
        test.stack.push_op(numpy.float32(2), ops.push_twice)
        ops.fstore_2(test)
        self.assertEqual(test.local_array[2], 2)

    def test_fstore_3(self):
        """tests the fstore_3 opcode for 32 bit floats"""
        test = ops.OpCodes()
        test.stack.push_op(numpy.float32(3), ops.push_twice)
        ops.fstore_3(test)
        self.assertEqual(test.local_array[3], 3)

    def test_iload(self):
        """tests iload method"""
        test = ops.OpCodes()
        #tests every load index from 0 to length
        for i in range(0, len(test.local_array)):
            ops.iload(test, i)
            self.assertEqual(test.stack.peek(), test.local_array[i])

    def test_iload_0(self):
        """tests iload_0 opcode"""
        test = ops.OpCodes()
        ops.iload_0(test)
        self.assertEqual(test.stack.peek(), test.local_array[0])

    def test_iload_1(self):
        """tests iload_1 opcode"""
        test = ops.OpCodes()
        ops.iload_1(test)
        self.assertEqual(test.stack.peek(), test.local_array[1])

    def test_iload_2(self):
        """tests iload_2 opcode"""
        test = ops.OpCodes()
        ops.iload_2(test)
        self.assertEqual(test.stack.peek(), test.local_array[2])

    def test_iload_3(self):
        """tests iload_3 opcode"""
        test = ops.OpCodes()
        ops.iload_3(test)
        self.assertEqual(test.stack.peek(), test.local_array[3])

    def test_mph1(self):
        """tests mph1 method"""
        self.assertEqual(1 + 1, 2)
        with self.assertRaises(KeyError):
            ops.OpCodes().interpret(1)

    def test_new(self):
        """tests new method"""
        test = ops.OpCodes()
        #new(test)

    def test_add_subtract(self):
        """tests the iadd and isub opcodes"""
        op_code = ops.OpCodes()
        op_code.stack.push_op(numpy.int32(2000000000))
        op_code.stack.push_op(numpy.int32(1000000000))
        ops.iadd(op_code)
        self.assertEqual(op_code.stack.peek(), -1294967296)
        op_code.stack.push_op(numpy.int32(10))
        op_code.stack.push_op(numpy.int32(3))
        ops.isub(op_code)
        self.assertEqual(op_code.stack.peek(), 7)

    def test_multiply(self):
        """tests the imul opcode"""
        op_code = ops.OpCodes()
        op_code.stack.push_op(numpy.int32(2000000000))
        op_code.stack.push_op(numpy.int32(1000000000))
        ops.imul(op_code)
        self.assertEqual(op_code.stack.peek(), 1321730048)

    def test_divide(self):
        """tests the idiv opcode"""
        op_code = ops.OpCodes()
        op_code.stack.push_op(numpy.int32(128))
        op_code.stack.push_op(numpy.int32(-3))
        ops.idiv(op_code)
        self.assertEqual(op_code.stack.peek(), -42)

    def test_mod(self):
        """tests the irem opcode"""
        op_code = ops.OpCodes()
        op_code.stack.push_op(numpy.int32(128))
        op_code.stack.push_op(numpy.int32(-3))
        ops.irem(op_code)
        self.assertEqual(op_code.stack.peek(), 2)

    def test_iand(self):
        """ Test the iand (Integer And) opcode """
        test_op_codes = ops.OpCodes()
        # iand (240 & 15) should produce (0)
        test_op_codes.stack.push_op(240)
        test_op_codes.stack.push_op(15)
        ops.iand(test_op_codes)
        self.assertEqual(test_op_codes.stack.pop_op(), 0)
        # iand (43,690 & 50,790) should produce (33314)
        test_op_codes.stack.push_op(43690)
        test_op_codes.stack.push_op(50790)
        ops.iand(test_op_codes)
        self.assertEqual(test_op_codes.stack.pop_op(), 33314)
        # iand (-2,147,483,647 & -1) should produce (-2,147,483,647)
        test_op_codes.stack.push_op(-2147483647)
        test_op_codes.stack.push_op(-1)
        ops.iand(test_op_codes)
        self.assertEqual(test_op_codes.stack.pop_op(), -2147483647)

    def test_ineg(self):
        """ Test the ineg (Integer Negate) opcode """
        test_op_codes = ops.OpCodes()
        # ineg(254) should produce (-255)
        test_op_codes.stack.push_op(254)
        ops.ineg(test_op_codes)
        self.assertEqual(test_op_codes.stack.pop_op(), -255)
        # ineg(0) should produce (-1)
        test_op_codes.stack.push_op(0)
        ops.ineg(test_op_codes)
        self.assertEqual(test_op_codes.stack.pop_op(), -1)
        # ineg(2,147,483,647) sould produce (-2,147,483,648)
        test_op_codes.stack.push_op(2147483647)
        ops.ineg(test_op_codes)
        self.assertEqual(test_op_codes.stack.pop_op(), -2147483648)

    def test_ior(self):
        """ Test the ior (Integer Or) opcode """
        test_op_codes = ops.OpCodes()
        # ior(240 | 15) should produce (255)
        test_op_codes.stack.push_op(240)
        test_op_codes.stack.push_op(15)
        ops.ior(test_op_codes)
        self.assertEqual(test_op_codes.stack.pop_op(), 255)
        # ior(2,147,483,647 | -2,147,483,648) should produce (-1)
        test_op_codes.stack.push_op(2147483647)
        test_op_codes.stack.push_op(-2147483648)
        ops.ior(test_op_codes)
        self.assertEqual(test_op_codes.stack.pop_op(), -1)

    def test_ixor(self):
        """ Test the ixor (Integer Exclusive Or) opcode """
        test_op_codes = ops.OpCodes()
        # ixor(255 ^ 129) should produce (126)
        test_op_codes.stack.push_op(255)
        test_op_codes.stack.push_op(129)
        ops.ixor(test_op_codes)
        self.assertEqual(test_op_codes.stack.peek(), 126)

    def test_ishl(self):
        """ Test the ishl (Integer Shift Left) opcode """
        test_op_codes = ops.OpCodes()
        test_op_codes.stack.push_op(0)
        test_op_codes.stack.push_op(0)
        ops.ishl(test_op_codes)
        self.assertEqual(test_op_codes.stack.pop_op(), 0)

        test_op_codes.stack.push_op(1)
        test_op_codes.stack.push_op(1)
        ops.ishl(test_op_codes)
        self.assertEqual(test_op_codes.stack.pop_op(), 2)

        test_op_codes.stack.push_op(1)
        test_op_codes.stack.push_op(3)
        ops.ishl(test_op_codes)
        self.assertEqual(test_op_codes.stack.pop_op(), 8)

        test_op_codes.stack.push_op(1)
        test_op_codes.stack.push_op(8)
        ops.ishl(test_op_codes)
        self.assertEqual(test_op_codes.stack.pop_op(), 256)

        test_op_codes.stack.push_op(8)
        test_op_codes.stack.push_op(4)
        ops.ishl(test_op_codes)
        self.assertEqual(test_op_codes.stack.pop_op(), 128)

        test_op_codes.stack.push_op(16)
        test_op_codes.stack.push_op(2)
        ops.ishl(test_op_codes)
        self.assertEqual(test_op_codes.stack.pop_op(), 64)

    def test_ishr(self):
        """ Test the ishr (Integer Arithmetic Shift Right) opcode """
        test_op_codes = ops.OpCodes()
        test_op_codes.stack.push_op(0)
        test_op_codes.stack.push_op(0)
        ops.ishr(test_op_codes)
        self.assertEqual(test_op_codes.stack.pop_op(), 0)

        test_op_codes.stack.push_op(8)
        test_op_codes.stack.push_op(3)
        ops.ishr(test_op_codes)
        self.assertEqual(test_op_codes.stack.pop_op(), 1)

        test_op_codes.stack.push_op(256)
        test_op_codes.stack.push_op(6)
        ops.ishr(test_op_codes)
        self.assertEqual(test_op_codes.stack.pop_op(), 4)
        test_op_codes.stack.push_op(16)
        test_op_codes.stack.push_op(3)
        ops.ishr(test_op_codes)
        self.assertEqual(test_op_codes.stack.pop_op(), 2)

        test_op_codes.stack.push_op(32)
        test_op_codes.stack.push_op(2)
        ops.ishr(test_op_codes)
        self.assertEqual(test_op_codes.stack.pop_op(), 8)

        test_op_codes.stack.push_op(16)
        test_op_codes.stack.push_op(2)
        ops.ishr(test_op_codes)
        self.assertEqual(test_op_codes.stack.pop_op(), 4)

    def test_iushr(self):
        """ Test the iushr (Logical Shift Right) opcode """
        test_op_codes = ops.OpCodes()
        # iushr(255 >>> 2) should produce (63)
        test_op_codes.stack.push_op(255)
        test_op_codes.stack.push_op(2)
        ops.iushr(test_op_codes)
        self.assertEqual(test_op_codes.stack.pop_op(), 63)
        # iushr(-1 >> 4) should produce (268,435,455)
        test_op_codes.stack.push_op(-1)
        test_op_codes.stack.push_op(4)
        ops.iushr(test_op_codes)
        self.assertEqual(test_op_codes.stack.pop_op(), 268435455)

    def test_i2b(self):
        """Test conversion of integer to byte dawg"""
        test_op_codes = ops.OpCodes()
        test_op_codes.stack.push_op(42)
        ops.i2b(test_op_codes)
        assert isinstance(test_op_codes.stack.peek(), numpy.int8)

    def test_i2c(self):
        """Test conversion of integer to byte"""
        test_op_codes = ops.OpCodes()
        test_op_codes.stack.push_op(33)
        ops.i2c(test_op_codes)
        assert isinstance(test_op_codes.stack.peek(), str)

    def test_i2d(self):
        """Test conversion of integer to double"""
        test_op_codes = ops.OpCodes()
        test_op_codes.stack.push_op(42)
        ops.i2d(test_op_codes)
        assert isinstance(test_op_codes.stack.peek(), numpy.float64)

    def test_i2f(self):
        """Test conversion of integer to float"""
        test_op_codes = ops.OpCodes()
        test_op_codes.stack.push_op(42)
        ops.i2f(test_op_codes)
        assert isinstance(test_op_codes.stack.peek(), numpy.float32)

    def test_i2l(self):
        """Test conversion of integer to long"""
        test_op_codes = ops.OpCodes()
        test_op_codes.stack.push_op(42)
        ops.i2l(test_op_codes)
        assert isinstance(test_op_codes.stack.peek(), numpy.int64)

    def test_i2s(self):
        """Test conversion of integer to short"""
        test_op_codes = ops.OpCodes()
        test_op_codes.stack.push_op(42)
        ops.i2s(test_op_codes)
        assert isinstance(test_op_codes.stack.peek(), numpy.int16)

    def test_dup(self):
        """Test dup"""
        test_op_codes = ops.OpCodes()
        test_op_codes.stack.push_op(15)
        ops.dup(test_op_codes)
        self.assertEqual(test_op_codes.stack.pop_op(), 15)
        self.assertEqual(test_op_codes.stack.pop_op(), 15)

        test_op_codes.stack.push_op(0)
        ops.dup(test_op_codes)
        self.assertEqual(test_op_codes.stack.pop_op(), 0)
        self.assertEqual(test_op_codes.stack.pop_op(), 0)

        test_op_codes.stack.push_op('foo')
        ops.dup(test_op_codes)
        self.assertEqual(test_op_codes.stack.pop_op(), 'foo')
        self.assertEqual(test_op_codes.stack.pop_op(), 'foo')

    def test_lload(self):
        """tests lload method"""
        test = ops.OpCodes()
        #tests every load index from 0 to length
        for i in range(0, len(test.local_array)):
            ops.lload(test, i)
            self.assertEqual(test.stack.pop_op(ops.pop_twice), test.local_array[i])

    def test_lload_0(self):
        """tests iload_0 opcode"""
        test = ops.OpCodes()
        ops.lload_0(test)
        self.assertEqual(test.stack.pop_op(ops.pop_twice), test.local_array[0])

    def test_lload_1(self):
        """tests iload_1 opcode"""
        test = ops.OpCodes()
        ops.lload_1(test)
        self.assertEqual(test.stack.pop_op(ops.pop_twice), test.local_array[1])

    def test_lload_2(self):
        """tests iload_2 opcode"""
        test = ops.OpCodes()
        ops.lload_2(test)
        self.assertEqual(test.stack.pop_op(ops.pop_twice), test.local_array[2])

    def test_lload_3(self):
        """tests iload_3 opcode"""
        test = ops.OpCodes()
        ops.lload_3(test)
        self.assertEqual(test.stack.pop_op(ops.pop_twice), test.local_array[3])

    def test_lshl(self):
        """Test lshl (long shift left)"""
        test_op_codes = ops.OpCodes()
        test_op_codes.stack.push_op(2, ops.push_twice)
        test_op_codes.stack.push_op(2)
        ops.lshl(test_op_codes)
        assert isinstance(test_op_codes.stack.peek(), numpy.int64)
        self.assertEqual(test_op_codes.stack.pop_op(ops.pop_twice), numpy.int64(8))

        test_op_codes.stack.push_op(2, ops.push_twice)
        test_op_codes.stack.push_op(66)
        ops.lshl(test_op_codes)
        assert isinstance(test_op_codes.stack.peek(), numpy.int64)
        self.assertEqual(test_op_codes.stack.pop_op(ops.pop_twice), numpy.int64(8))

    def test_lshr(self):
        """Test lshr (long shift right)"""
        test_op_codes = ops.OpCodes()
        test_op_codes.stack.push_op(42, ops.push_twice)
        test_op_codes.stack.push_op(3)
        ops.lshr(test_op_codes)
        assert isinstance(test_op_codes.stack.peek(), numpy.int64)
        self.assertEqual(test_op_codes.stack.pop_op(ops.pop_twice), numpy.int64(5))

        test_op_codes.stack.push_op(2, ops.push_twice)
        test_op_codes.stack.push_op(66)
        ops.lshr(test_op_codes)
        assert isinstance(test_op_codes.stack.peek(), numpy.int64)
        self.assertEqual(test_op_codes.stack.pop_op(ops.pop_twice), numpy.int64(0))

        test_op_codes.stack.push_op(-15, ops.push_twice)
        test_op_codes.stack.push_op(2)

        ops.lshr(test_op_codes)
        assert isinstance(test_op_codes.stack.peek(), numpy.int64)
        self.assertEqual(test_op_codes.stack.pop_op(ops.pop_twice), numpy.int64(-4))

    def test_land(self):
        """Test land (logical bitwise long AND)"""
        test_op_codes = ops.OpCodes()
        test_op_codes.stack.push_op(42)
        ops.i2l(test_op_codes)
        test_op_codes.stack.push_op(6)
        ops.i2l(test_op_codes)
        ops.land(test_op_codes)
        assert isinstance(test_op_codes.stack.peek(), numpy.int64)
        self.assertEqual(test_op_codes.stack.pop_op(ops.pop_twice), numpy.int64(2))

    def test_lcmp(self):
        """Test lcmp (compare 2 longs)"""
        test_op_codes = ops.OpCodes()
        test_op_codes.stack.push_op(41)
        ops.i2l(test_op_codes)
        test_op_codes.stack.push_op(42)
        ops.i2l(test_op_codes)
        ops.lcmp(test_op_codes)
        self.assertEqual(test_op_codes.stack.pop_op(), -1)

        test_op_codes.stack.push_op(43)
        ops.i2l(test_op_codes)
        test_op_codes.stack.push_op(42)
        ops.i2l(test_op_codes)

        ops.lcmp(test_op_codes)
        self.assertEqual(test_op_codes.stack.pop_op(), 1)

        test_op_codes.stack.push_op(42)
        ops.i2l(test_op_codes)
        test_op_codes.stack.push_op(42)
        ops.i2l(test_op_codes)
        ops.lcmp(test_op_codes)
        self.assertEqual(test_op_codes.stack.pop_op(), 0)

    def test_lxor(self):
        """test lxor (long exclusive or)"""
        test_op_codes = ops.OpCodes()
        test_op_codes.stack.push_op(7)
        ops.i2l(test_op_codes)
        test_op_codes.stack.push_op(6)
        ops.i2l(test_op_codes)
        ops.lxor(test_op_codes)
        assert isinstance(test_op_codes.stack.peek(), numpy.int64)
        self.assertEqual(test_op_codes.stack.pop_op(ops.pop_twice), numpy.int64(1))

        test_op_codes.stack.push_op(-7)
        ops.i2l(test_op_codes)
        test_op_codes.stack.push_op(-6)
        ops.i2l(test_op_codes)
        ops.lxor(test_op_codes)
        assert isinstance(test_op_codes.stack.peek(), numpy.int64)
        self.assertEqual(test_op_codes.stack.pop_op(ops.pop_twice), numpy.int64(3))

        test_op_codes.stack.push_op(-7)
        ops.i2l(test_op_codes)
        test_op_codes.stack.push_op(6)
        ops.i2l(test_op_codes)
        ops.lxor(test_op_codes)
        assert isinstance(test_op_codes.stack.peek(), numpy.int64)
        self.assertEqual(test_op_codes.stack.pop_op(ops.pop_twice), numpy.int64(-1))

    def test_fcmpg(self):
        """Test fcmpg (compare 2 floats)"""
        test_op_codes = ops.OpCodes()
        test_op_codes.stack.push_op(1/7)
        ops.i2f(test_op_codes)
        test_op_codes.stack.push_op(1/3)
        ops.i2f(test_op_codes)
        ops.fcmpg(test_op_codes)
        self.assertEqual(test_op_codes.stack.pop_op(), -1)

        test_op_codes.stack.push_op(1/3)
        ops.i2f(test_op_codes)
        test_op_codes.stack.push_op(1/7)
        ops.i2f(test_op_codes)
        ops.fcmpg(test_op_codes)
        self.assertEqual(test_op_codes.stack.pop_op(), 1)

        test_op_codes.stack.push_op(1/7)
        ops.i2f(test_op_codes)
        test_op_codes.stack.push_op(1/7)
        ops.i2f(test_op_codes)
        ops.fcmpg(test_op_codes)
        self.assertEqual(test_op_codes.stack.pop_op(), 0)

        test_op_codes.stack.push_op(numpy.nan)
        test_op_codes.stack.push_op(1/7)
        ops.i2f(test_op_codes)
        ops.fcmpg(test_op_codes)
        self.assertEqual(test_op_codes.stack.pop_op(), 1)

        test_op_codes.stack.push_op(1/7)
        test_op_codes.stack.push_op(numpy.nan)
        ops.i2f(test_op_codes)
        ops.fcmpg(test_op_codes)
        self.assertEqual(test_op_codes.stack.pop_op(), 1)

    def test_fcmpl(self):
        """Test fcmpl (compare 2 floats)"""
        test_op_codes = ops.OpCodes()
        test_op_codes.stack.push_op(1/7)
        ops.i2f(test_op_codes)
        test_op_codes.stack.push_op(1/3)
        ops.i2f(test_op_codes)
        ops.fcmpl(test_op_codes)
        self.assertEqual(test_op_codes.stack.pop_op(), -1)

        test_op_codes.stack.push_op(1/3)
        ops.i2f(test_op_codes)
        test_op_codes.stack.push_op(1/7)
        ops.i2f(test_op_codes)
        ops.fcmpl(test_op_codes)
        self.assertEqual(test_op_codes.stack.pop_op(), 1)

        test_op_codes.stack.push_op(1/7)
        ops.i2f(test_op_codes)
        test_op_codes.stack.push_op(1/7)
        ops.i2f(test_op_codes)
        ops.fcmpl(test_op_codes)
        self.assertEqual(test_op_codes.stack.pop_op(), 0)

        test_op_codes.stack.push_op(numpy.nan)
        test_op_codes.stack.push_op(1/7)
        ops.i2f(test_op_codes)
        ops.fcmpl(test_op_codes)
        self.assertEqual(test_op_codes.stack.pop_op(), -1)

        test_op_codes.stack.push_op(1/7)
        test_op_codes.stack.push_op(numpy.nan)
        ops.i2f(test_op_codes)
        ops.fcmpl(test_op_codes)
        self.assertEqual(test_op_codes.stack.pop_op(), -1)

    def test_fneg(self):
        """test fneg (negate a float)"""
        test_op_codes = ops.OpCodes()
        test_op_codes.stack.push_op(1/7)
        ops.i2f(test_op_codes)
        ops.fneg(test_op_codes)
        self.assertEqual(test_op_codes.stack.pop_op(), numpy.float32(-1/7))

        test_op_codes.stack.push_op(float("inf"))
        ops.i2f(test_op_codes)
        ops.fneg(test_op_codes)
        numpy.isneginf(test_op_codes.stack.pop_op())

        test_op_codes.stack.push_op(float("-inf"))
        ops.i2f(test_op_codes)
        ops.fneg(test_op_codes)
        numpy.isposinf(test_op_codes.stack.pop_op())

        test_op_codes.stack.push_op(0)
        ops.i2f(test_op_codes)
        ops.fneg(test_op_codes)
        numpy.negative(test_op_codes.stack.pop_op())

        test_op_codes.stack.push_op(numpy.nan)
        ops.fneg(test_op_codes)
        numpy.isnan(test_op_codes.stack.pop_op())

    def test_fload(self):
        """tests fload method"""
        test = ops.OpCodes()
        #tests every load index from 0 to length
        for i in range(0, len(test.local_array)):
            ops.fload(test, i)
            self.assertEqual(test.stack.pop_op(), test.local_array[i])

    def test_fload_0(self):
        """tests iload_0 opcode"""
        test = ops.OpCodes()
        ops.fload_0(test)
        self.assertEqual(test.stack.pop_op(), test.local_array[0])

    def test_fload_1(self):
        """tests fload_1 opcode"""
        test = ops.OpCodes()
        ops.fload_1(test)
        self.assertEqual(test.stack.pop_op(), test.local_array[1])

    def test_fload_2(self):
        """tests fload_2 opcode"""
        test = ops.OpCodes()
        ops.fload_2(test)
        self.assertEqual(test.stack.pop_op(), test.local_array[2])

    def test_fload_3(self):
        """tests fload_3 opcode"""
        test = ops.OpCodes()
        ops.fload_3(test)
        self.assertEqual(test.stack.pop_op(), test.local_array[3])

    def test_lconst_0(self):
        """test lconst_0 (pushes 0L to the stack)"""
        test_op_codes = ops.OpCodes()
        ops.lconst_0(test_op_codes)
        self.assertEqual(numpy.int64(0), test_op_codes.stack.pop_op(ops.pop_twice))

    def test_lconst_1(self):
        """test lconst_1 (pushes 1L to the stack)"""
        test_op_codes = ops.OpCodes()
        ops.lconst_1(test_op_codes)
        self.assertEqual(numpy.int64(1), test_op_codes.stack.pop_op(ops.pop_twice))

    def test_fconst_0(self):
        """test fconst_0 (pushes 0F to the stack)"""
        test_op_codes = ops.OpCodes()
        ops.fconst_0(test_op_codes)
        self.assertEqual(numpy.float32(0), test_op_codes.stack.pop_op())

    def test_fconst_1(self):
        """test fconst_1 (pushes 1F to the stack)"""
        test_op_codes = ops.OpCodes()
        ops.fconst_1(test_op_codes)
        self.assertEqual(numpy.float32(1), test_op_codes.stack.pop_op())

    def test_fconst_2(self):
        """test fconst_2 (pushes 2F to the stack)"""
        test_op_codes = ops.OpCodes()
        ops.fconst_2(test_op_codes)
        self.assertEqual(numpy.float32(2), test_op_codes.stack.pop_op())

    def test_l2d(self):
        """test l2d (long to double)"""
        test_op_codes = ops.OpCodes()
        ops.lconst_1(test_op_codes)
        ops.l2d(test_op_codes)
        assert isinstance(test_op_codes.stack.peek(), numpy.float64)
        self.assertEqual(numpy.float64(1), test_op_codes.stack.pop_op(ops.pop_twice))

    def test_l2f(self):
        """test l2d (long to float)"""
        test_op_codes = ops.OpCodes()
        ops.lconst_1(test_op_codes)
        ops.l2f(test_op_codes)
        assert isinstance(test_op_codes.stack.peek(), numpy.float32)
        self.assertEqual(numpy.float32(1), test_op_codes.stack.pop_op())

    def test_l2i(self):
        """test l2i (long to int)"""
        test_op_codes = ops.OpCodes()
        ops.lconst_1(test_op_codes)
        ops.l2i(test_op_codes)
        assert isinstance(test_op_codes.stack.peek(), numpy.int32)
        self.assertEqual(numpy.int(1), test_op_codes.stack.pop_op())

    def test_f2d(self):
        """test f2d (float to double)"""
        test_op_codes = ops.OpCodes()
        ops.fconst_1(test_op_codes)
        ops.f2d(test_op_codes)
        assert isinstance(test_op_codes.stack.peek(), numpy.float64)
        self.assertEqual(numpy.float64(1), test_op_codes.stack.pop_op(ops.pop_twice))

    def test_f2i(self):
        """test f2i (float to integer)"""
        test_op_codes = ops.OpCodes()
        ops.fconst_1(test_op_codes)
        ops.f2i(test_op_codes)
        assert isinstance(test_op_codes.stack.peek(), numpy.int32)
        self.assertEqual(numpy.int(1), test_op_codes.stack.pop_op())

    def test_f2l(self):
        """test f2l (float to long)"""
        test_op_codes = ops.OpCodes()
        ops.fconst_1(test_op_codes)
        ops.f2l(test_op_codes)
        assert isinstance(test_op_codes.stack.peek(), numpy.int64)
        self.assertEqual(numpy.int64(1), test_op_codes.stack.pop_op(ops.pop_twice))

    def test_fadd(self):
        """tests the fadd opcodes"""
        op_code = ops.OpCodes()
        op_code.stack.push_op(numpy.float32(0.0))
        op_code.stack.push_op(numpy.float32(0.0))
        ops.fadd(op_code)
        self.assertEqual(op_code.stack.peek(), 0.0)
        op_code.stack.push_op(numpy.float32(2.0))
        op_code.stack.push_op(numpy.float32(1.0))
        ops.fadd(op_code)
        self.assertEqual(op_code.stack.peek(), 3.0)
        op_code.stack.push_op(numpy.float32(2.15))
        op_code.stack.push_op(numpy.float32(1.40))
        ops.fadd(op_code)
        self.assertAlmostEqual(op_code.stack.peek(), 3.55, places=2)

    def test_fsub(self):
        """tests the fsub opcodes"""
        op_code = ops.OpCodes()
        op_code.stack.push_op(numpy.float32(0.0))
        op_code.stack.push_op(numpy.float32(0.0))
        ops.fsub(op_code)
        self.assertEqual(op_code.stack.peek(), 0.0)
        op_code.stack.push_op(numpy.float32(5.0))
        op_code.stack.push_op(numpy.float32(2.0))
        ops.fsub(op_code)
        self.assertEqual(op_code.stack.peek(), 3.0)

    def test_fmul(self):
        """tests the fmul opcode"""
        op_code = ops.OpCodes()
        op_code.stack.push_op(numpy.float32(2.0))
        op_code.stack.push_op(numpy.float32(3.0))
        ops.fmul(op_code)
        self.assertEqual(op_code.stack.peek(), 6.0)
        op_code.stack.push_op(numpy.float32(2.0))
        op_code.stack.push_op(numpy.float32(3.0))
        ops.fmul(op_code)
        self.assertEqual(op_code.stack.peek(), 6.0)

    def test_fdiv(self):
        """tests the fdiv opcode"""
        op_code = ops.OpCodes()
        op_code.stack.push_op(numpy.float32(4.0))
        op_code.stack.push_op(numpy.float32(2.0))
        ops.fdiv(op_code)
        self.assertEqual(op_code.stack.peek(), 2.0)

    def test_frem(self):
        """tests the irem opcode"""
        op_code = ops.OpCodes()
        op_code.stack.push_op(numpy.float32(0.0))
        op_code.stack.push_op(numpy.float32(0.0))
        ops.frem(op_code)
        self.assertEqual(op_code.stack.peek(), 0.0)
        op_code.stack.push_op(numpy.float32(5.0))
        op_code.stack.push_op(numpy.float32(5.0))
        ops.frem(op_code)
        self.assertEqual(op_code.stack.peek(), 0.0)

    def test_ladd(self):
        """tests the ladd opcodes"""
        op_code = ops.OpCodes()
        op_code.stack.push_op(numpy.int64(0), ops.push_twice)
        op_code.stack.push_op(numpy.int64(0), ops.push_twice)
        ops.ladd(op_code)
        self.assertEqual(op_code.stack.pop_op(ops.pop_twice), 0)
        op_code.stack.push_op(numpy.int64(2), ops.push_twice)
        op_code.stack.push_op(numpy.int64(1), ops.push_twice)
        ops.ladd(op_code)
        self.assertEqual(op_code.stack.pop_op(ops.pop_twice), 3)
        op_code.stack.push_op(numpy.int64(2), ops.push_twice)
        op_code.stack.push_op(numpy.int64(4), ops.push_twice)
        ops.ladd(op_code)
        self.assertEqual(op_code.stack.pop_op(ops.pop_twice), 6)

    def test_lsub(self):
        """tests the lsub opcodes"""
        op_code = ops.OpCodes()
        op_code.stack.push_op(numpy.int64(0), ops.push_twice)
        op_code.stack.push_op(numpy.int64(0), ops.push_twice)
        ops.lsub(op_code)
        self.assertEqual(op_code.stack.pop_op(ops.pop_twice), 0)
        op_code.stack.push_op(numpy.int64(5), ops.push_twice)
        op_code.stack.push_op(numpy.int64(2), ops.push_twice)
        ops.lsub(op_code)
        self.assertEqual(op_code.stack.pop_op(ops.pop_twice), 3)

    def test_lmul(self):
        """tests the lmul opcode"""
        op_code = ops.OpCodes()
        op_code.stack.push_op(numpy.int64(2), ops.push_twice)
        op_code.stack.push_op(numpy.int64(3), ops.push_twice)
        ops.lmul(op_code)
        self.assertEqual(op_code.stack.pop_op(ops.pop_twice), 6)
        op_code.stack.push_op(numpy.int64(-2), ops.push_twice)
        op_code.stack.push_op(numpy.int64(-3), ops.push_twice)
        ops.lmul(op_code)
        self.assertEqual(op_code.stack.pop_op(ops.pop_twice), 6)

    def test_ldiv(self):
        """tests the ldiv opcode"""
        op_code = ops.OpCodes()
        op_code.stack.push_op(numpy.int64(4), ops.push_twice)
        op_code.stack.push_op(numpy.int64(2), ops.push_twice)
        ops.ldiv(op_code)
        self.assertEqual(op_code.stack.pop_op(ops.pop_twice), 2)
        op_code.stack.push_op(numpy.int64(-4), ops.push_twice)
        op_code.stack.push_op(numpy.int64(2), ops.push_twice)
        ops.ldiv(op_code)
        self.assertEqual(op_code.stack.pop_op(ops.pop_twice), -2)

    def test_lrem(self):
        """tests the lrem opcode"""
        op_code = ops.OpCodes()
        op_code.stack.push_op(numpy.int64(0), ops.push_twice)
        op_code.stack.push_op(numpy.int64(0), ops.push_twice)
        ops.lrem(op_code)
        self.assertEqual(op_code.stack.pop_op(ops.pop_twice), 0)
        op_code.stack.push_op(numpy.int64(5), ops.push_twice)
        op_code.stack.push_op(numpy.int64(5), ops.push_twice)
        ops.lrem(op_code)
        self.assertEqual(op_code.stack.pop_op(ops.pop_twice), 0)
