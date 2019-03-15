"""this file contains the OpCodes class"""
# utilizes NumPy package to handle 32 bit int over/underflow in Java
import numpy  # to get the java-like behavior for arithmetic

from jvpm.jvm_stack import JvmStack
from jvpm.constant_pool_parser import ConstantPoolParser
from jvpm.method_table import MethodTable
# shuts off the overflow warnings from numpy
numpy.seterr(over="ignore", under="ignore")


class OpCodes():
    """This class interprets opcodes"""

    def __init__(self):
        """this is the constructor"""
        with open('jvpm/Test.class', 'rb') as binary_file:
            self.data = bytes(binary_file.read())
        #
        self.table = {0x2a: [aload_0, 1],
                      0xb1: [ret, 2],
                      0x02: [iconst_m1, 1],
                      0x03: [iconst_0, 1],
                      0x04: [iconst_1, 1],
                      0x05: [iconst_2, 1],
                      0x06: [iconst_3, 1],
                      0x07: [iconst_4, 1],
                      0x08: [iconst_5, 1],
                      0x3c: [istore_1, 1],
                      0x84: [iinc, 3],
                      0xb7: [invokespecial, 3],
                      0x60: [iadd, 1],
                      0x64: [isub, 1],
                      0x68: [imul, 1],
                      0x6c: [idiv, 1],
                      0x70: [irem, 1],
                      0x7e: [iand, 1],
                      0x74: [ineg, 1],
                      0x80: [ior, 1],
                      0x82: [ixor, 1],
                      0X78: [ishl, 1],
                      0x7a: [ishr, 1],
                      0x7c: [iushr, 1],
                      0x00: [not_implemented, 1], 0xb2: [getstatic, 3], 0x12: [ldc, 2], 0xb6: [invokevirtual, 3]}
        self.byte_count = 0
        self.stack = JvmStack()
        self.constant_pool = []
        self.set_data(self.data)
# initialize the method table
        self.nmt = MethodTable()

    def parse_codes(self, op_start):
        """this method searches the binary for only the opcodes we know are in it"""
        self.byte_count = op_start
        while self.byte_count < len(self.data):
            if self.data[self.byte_count] in self.table.keys():
                self.interpret(self.data[self.byte_count])
            else:
                self.interpret(0)

    def interpret(self, value):
        """this is the method used to interpret a given opcode"""
        self.byte_count += self.table[value][1]
        return self.table[value][0](self)

    def set_data(self, data):
        """this method exists so that I can change the opcode data for testing"""
        self.data = data
# update the constant pool
        self.constant_pool = ConstantPoolParser(data).make_constant_pool()


def not_implemented(self):
    """this is a dummy function"""
    self.stack.push_op(1)
    self.stack.pop_op()
    return 'not implemented'


def aload_0(self):
    """this is a dummy method"""
    print('aload_0')
    self.stack.push_op(1)
    self.stack.pop_op()


def ret(self):
    """this function will eventually implement the ret opcode"""
    print('return')
    self.stack.push_op(1)
    self.stack.pop_op()


def iconst_m1(self):
    """implements iconst_m opcode, loads int -1 onto stack"""
    self.stack.push_op(-1)
    print('iconst_m1')


def iconst_0(self):
    """implements iconst_0 opcode, loads int 0 onto stack"""
    self.stack.push_op(0)
    print('iconst_0')


def iconst_1(self):
    """implements iconst_1 opcode, loads int 1 onto stack"""
    self.stack.push_op(1)
    print('iconst_1')


def iconst_2(self):
    """implements iconst_2 opcode, loads int 2 onto stack"""
    self.stack.push_op(2)
    print('iconst_2')


def iconst_3(self):
    """"implememts iconst_3 opcode, loads int 3 onto stack"""
    self.stack.push_op(3)
    print('iconst_3')


def iconst_4(self):
    """implements iconst_4 opcode, loads int 4 onto stack"""
    self.stack.push_op(4)
    print('iconst_4')


def iconst_5(self):
    """implements iconst_5 opcode, loads int 5 onto stack"""
    self.stack.push_op(5)
    print('iconst_5')


def istore_1(self):
    """this function implements the istore_1 opcode"""
    print('istore_1')
    self.stack.push_op(1)
    self.stack.pop_op()


def iinc(self):
    """this function implements the iinc opcode"""
    print('iinc')
    self.stack.push_op(1)
    self.stack.pop_op()


def invokespecial(self):
    """This function implements the invokespecial opcode"""
    byte_1 = self.data[self.byte_count + 1]
    byte_2 = self.data[self.byte_count + 2]
    print('invokespecial')
    return byte_1 + byte_2


def iadd(self):
    """implements the iadd opcode"""
    val2 = numpy.int32(self.stack.pop_op())
    val1 = numpy.int32(self.stack.pop_op())
    self.stack.push_op(val1 + val2)


def isub(self):
    """implements the isub opcode"""
    val2 = numpy.int32(self.stack.pop_op())
    val1 = numpy.int32(self.stack.pop_op())
    self.stack.push_op(val1 - val2)


def imul(self):
    """implements the imul opcode"""
    val2 = numpy.int32(self.stack.pop_op())
    val1 = numpy.int32(self.stack.pop_op())
    self.stack.push_op(val1 * val2)


def idiv(self):
    """implements the idiv opcode"""
    val2 = numpy.int32(self.stack.pop_op())
    val1 = numpy.int32(self.stack.pop_op())
    self.stack.push_op(numpy.int32(val1 / val2))

# irem will be implemented in terms of the other operations.
# a%b = a-(a/b)*b


def irem(self):
    """implements the irem opcode"""
    val2 = numpy.int32(self.stack.pop_op())
    val1 = numpy.int32(self.stack.pop_op())
    self.stack.push_op(val1)
    self.stack.push_op(val1)
    self.stack.push_op(val2)
    idiv(self)
    self.stack.push_op(val2)
    imul(self)
    isub(self)


def iand(self):
    """ Perform bitwise AND on the top two operands on the stack. """
    this_val = self.stack.pop_op()
    that_val = self.stack.pop_op()
    self.stack.push_op(this_val & that_val)


def ineg(self):
    """ Perform bitwise NOT on the top operand on the stack. """
    not_this = self.stack.pop_op()
    self.stack.push_op(~not_this)


def ior(self):
    """ Perform bitwise OR on the top two operands on the stack. """
    this_val = self.stack.pop_op()
    that_val = self.stack.pop_op()
    self.stack.push_op(this_val | that_val)


def ixor(self):
    """ Perform bitwise XOR on the top two operands on the stack. """
    this_val = self.stack.pop_op()
    that_val = self.stack.pop_op()
    self.stack.push_op(this_val ^ that_val)


def ishl(self):
    """implements the shl opcode"""
    val2 = self.stack.pop_op()
    val1 = self.stack.pop_op()
    self.stack.push_op(val1 << val2)

# implementing  shlr


def ishr(self):
    """implements the shl opcode"""
    val2 = self.stack.pop_op()
    val1 = self.stack.pop_op()
    self.stack.push_op(val1 >> val2)


def iushr(self):
    """ Perform bitwise LOGICAL SHIFT RIGHT on the top two operands on the stack. """
    this_val = self.stack.pop_op()
    that_val = self.stack.pop_op()
    val = 0
    if that_val >= 0:
        val = that_val >> this_val
    else:
        val = (that_val & 0xffffffff) >> this_val
        print(str(val))
    self.stack.push_op(val)


def getstatic(self):
    """This is a stub implementation of getstatic.
It will be expanded in the future if we start loading other classes."""
    index = self.data[self.byte_count - 2:self.byte_count]
    self.constant_pool.load_constant(index, self.stack)


def ldc(self):
    """implements ldc"""
# take into account the fact that the index for ldc is a single byte
    index = b"\x00" + self.data[self.byte_count - 1:self.byte_count]
    self.constant_pool.load_constant(index, self.stack)


def invokevirtual(self):
    """implements invokevirtual"""
# look up the method to be invoked.
    index = self.data[self.byte_count - 2:self.byte_count]
    methodref = self.constant_pool.lookup_constant(index)
# get the name of the class for this method.
    classref = self.constant_pool.lookup_constant(methodref[1:3])
    utf8_index = classref[1:]
    utf8_const = self.constant_pool.lookup_constant(utf8_index)
    classname = utf8_const[3:].decode("utf-8")
# after all that pointer chasing, we still have to do it again to get the
# name and type of the method
    nat_index = methodref[3:]
    nat_const = self.constant_pool.lookup_constant(nat_index)
    methodname_index = nat_const[1:3]
    methodname_const = self.constant_pool.lookup_constant(methodname_index)
    methodname = methodname_const[3:].decode("utf-8")
    methodtype_index = nat_const[3:]
    methodtype_const = self.constant_pool.lookup_constant(methodtype_index)
    methodtype = methodtype_const[3:].decode("utf-8")
# finally, we can invoke the method!
    official_name = classname + "." + methodname + methodtype
    self.nmt.call(self, official_name)
