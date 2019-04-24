"""this file contains the OpCodes class"""
# utilizes NumPy package to handle 32 bit int over/underflow in Java
import numpy  # to get the java-like behavior for arithmetic

from jvpm.jvm_stack import JvmStack, pop_twice, push_twice
from jvpm.constant_pool_parser import ConstantPoolParser
from jvpm.method_table import MethodTable
# shuts off the overflow warnings from numpy
numpy.seterr(over="ignore", under="ignore")

class OpCodes():
    """This class interprets opcodes"""

    def __init__(self):
        """this is the constructor"""
        self.local_array = [0, 1, 2, 3]
        with open('jvpm/OpsTest.class', 'rb') as binary_file:
            self.data = bytes(binary_file.read())
        #
        self.table = {0x2a: [aload_0, 1],
                      0x59: [dup, 1],
                      0xb1: [ret, 2],
                      0x02: [iconst_m1, 1],
                      0x03: [iconst_0, 1],
                      0x04: [iconst_1, 1],
                      0x05: [iconst_2, 1],
                      0x06: [iconst_3, 1],
                      0x07: [iconst_4, 1],
                      0x08: [iconst_5, 1],
                      0x15: [iload, 1],
                      0x1a: [iload_0, 1],
                      0x1b: [iload_1, 1],
                      0x1c: [iload_2, 1],
                      0x1d: [iload_3, 1],
                      0x36: [istore, 1],
                      0x3b: [istore_0, 1],
                      0x3c: [istore_1, 1],
                      0x3d: [istore_2, 1],
                      0x3e: [istore_3, 1],
                      0x37: [lstore, 1],
                      0x3f: [lstore_0, 1],
                      0x40: [lstore_1, 1],
                      0x41: [lstore_2, 1],
                      0x42: [lstore_3, 1],
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
                      0xb2: [getstatic, 3],
                      0x12: [ldc, 2],
                      0xb6: [invokevirtual, 3],
                      0x91: [i2b, 1],
                      0x92: [i2c, 1],
                      0x87: [i2d, 1],
                      0x86: [i2f, 1],
                      0x16: [lload, 1],
                      0x1e: [lload_0, 1],
                      0x1f: [lload_1, 1],
                      0x20: [lload_2, 1],
                      0x21: [lload_3, 1],
                      0x79: [lshl, 1],
                      0x7b: [lshr, 1],
                      0x7f: [land, 1],
                      0x94: [lcmp, 1],
                      0x83: [lxor, 1],
                      0x96: [fcmpg, 1],
                      0x95: [fcmpl, 1],
                      0x76: [fneg, 1],
                      0x17: [fload, 1],
                      0x22: [fload_0, 1],
                      0x23: [fload_1, 1],
                      0x24: [fload_2, 1],
                      0x25: [fload_3, 1],
                      0x09: [lconst_0, 1],
                      0x0a: [lconst_1, 1],
                      0x0b: [fconst_0, 1],
                      0x0c: [fconst_1, 1],
                      0x0d: [fconst_2, 1],
                      0x8a: [l2d, 1],
                      0x89: [l2f, 1],
                      0x88: [l2i, 1],
                      0x8d: [f2d, 1],
                      0x8b: [f2i, 1],
                      0x8c: [f2l, 1],   
                      0x62: [fadd, 1],
                      0x66: [fsub, 1],
                      0x6a: [fmul, 1],
                      0x6e: [fdiv,1],
                      0x72: [frem, 1],
                      0x61: [ladd,1],
                      0x65: [lsub,1],
                      0x69: [lmul,1],
                      0x6d: [ldiv,1],
                      0x71: [lrem,1],
                      0x00: [not_implemented, 1]}
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
    """loads a reference from the data array onto stack"""
    self.stack.push_op(1)
    self.stack.pop_op()

def iload(self, index):
    """loads an int from local data array at <index> onto stack"""
    self.stack.push_op(self.local_array[index])

def iload_0(self):
    """loads an int from local data array at index 0 onto stack"""
    self.stack.push_op(self.local_array[0])

def iload_1(self):
    """loads an int from local data array at index 1 onto stack"""
    self.stack.push_op(self.local_array[1])

def iload_2(self):
    """loads an int from local data array at index 2 onto stack"""
    self.stack.push_op(self.local_array[2])

def iload_3(self):
    """loads an int from local data array at index 3 onto stack"""
    self.stack.push_op(self.local_array[3])

def ret(self):
    """this function will eventually implement the ret opcode"""
    self.stack.push_op(1)
    self.stack.pop_op()

def iconst_m1(self):
    """implements iconst_m opcode, loads int -1 onto stack"""
    self.stack.push_op(-1)

def iconst_0(self):
    """implements iconst_0 opcode, loads int 0 onto stack"""
    self.stack.push_op(0)

def iconst_1(self):
    """implements iconst_1 opcode, loads int 1 onto stack"""
    self.stack.push_op(1)

def iconst_2(self):
    """implements iconst_2 opcode, loads int 2 onto stack"""
    self.stack.push_op(2)

def iconst_3(self):
    """"implememts iconst_3 opcode, loads int 3 onto stack"""
    self.stack.push_op(3)

def iconst_4(self):
    """implements iconst_4 opcode, loads int 4 onto stack"""
    self.stack.push_op(4)

def iconst_5(self):
    """implements iconst_5 opcode, loads int 5 onto stack"""
    self.stack.push_op(5)
def istore(self, index):
    """loads an int from stack into local array at <index>"""
    self.local_array[index] = self.stack.pop_op()

def istore_0(self):
    """this function implements the istore_0 opcode"""
    self.local_array[0] = self.stack.pop_op()

def istore_1(self):
    """this function implements the istore_1 opcode"""
    self.local_array[1] = self.stack.pop_op()
    self.stack.push_op(1)
    self.stack.pop_op()

def istore_2(self):
    """this function implements the istore_2 opcode"""
    self.local_array[2] = self.stack.pop_op()

def istore_3(self):
    """this function implements the istore_3 opcode"""
    self.local_array[3] = self.stack.pop_op()

def lstore(self, index):
    """implements the lstore opcode for 64 bit longs"""
    self.local_array[index] = self.stack.pop_op(pop_twice)

def lstore_0(self):
    """implements lstore_0 opcode, loads 64 bit long 0 into local array"""
    self.local_array[0] = self.stack.pop_op(pop_twice)

def lstore_1(self):
    """implements lstore_1 opcode, loads 64 bit long 1 into local array"""
    self.local_array[1] = self.stack.pop_op(pop_twice)

def lstore_2(self):
    """implements lstore_2 opcode, loads 64 bit long 2 into local array"""
    self.local_array[2] = self.stack.pop_op(pop_twice)

def lstore_3(self):
    """implements lstore_3 opcode, loads 64 bit long 3 into local array"""
    self.local_array[3] = self.stack.pop_op(pop_twice)

def iinc(self):
    """this function implements the iinc opcode"""
    self.stack.push_op(1)
    self.stack.pop_op()

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

def i2b(self):
    """convert int on top of stack to byte, and push it(to the stack)"""
    convert_this = self.stack.pop_op()
    self.stack.push_op(numpy.int8(convert_this))

def i2c(self):
    """convert int on top of stack to character, and push it. Push it real good"""
    convert_this = self.stack.pop_op()
    self.stack.push_op(chr(convert_this))

def i2d(self):
    """convert int on top of stack to double, and p-p-push it real good"""
    convert_this = self.stack.pop_op()
    self.stack.push_op(numpy.float64(convert_this))

def i2f(self):
    """convert int on top of stack to float, and push it to the stack."""
    convert_this = self.stack.pop_op()
    self.stack.push_op(numpy.float32(convert_this))

def i2l(self):
    """convert int on top of stack to long, and push it to the stack."""
    convert_this = self.stack.pop_op()
    self.stack.push_op(numpy.int64(convert_this), push_twice)

def i2s(self):
    """convert int on top of stack to short, and push. it. to. the. stack."""
    convert_this = self.stack.pop_op()
    self.stack.push_op(numpy.int16(convert_this))

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
    methodref = self.constant_pool.lookup_constant(self.data[self.byte_count - 2:self.byte_count])
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

def invokespecial(self):
    """This function implements the invokespecial opcode"""
    # byte_1 = self.data[self.byte_count + 1]
    # byte_2 = self.data[self.byte_count + 2]
    # return byte_1 + byte_2
    invokevirtual(self)

def new(self):
    """Find the constant representing the class to be instantiated, then STACK IT"""
    addr1 = self.data[self.byte_count-2]
    addr2 = self.data[self.byte_count-1]
    new_constant = self.constant_pool.lookup_constant(addr1|addr2)
    self.stack.push_op(new_constant)

def dup(self):
    """pop first value on the stack, duplicate and push back onto stack"""
    value = self.stack.pop_op()
    dup_val = value
    self.stack.push_op(value)
    self.stack.push_op(dup_val)

def lload(self, index):
    """loads a long from local long data array at <index> onto stack"""
    self.stack.push_op(numpy.int64(self.local_array[index]), push_twice)

def lload_0(self):
    """loads a long from local long data array at index 0 onto stack"""
    self.stack.push_op(numpy.int64(self.local_array[0]), push_twice)

def lload_1(self):
    """loads a long from local long data array at index 1 onto stack"""
    self.stack.push_op(numpy.int64(self.local_array[1]), push_twice)

def lload_2(self):
    """loads a long from local long data array at index 2 onto stack"""
    self.stack.push_op(numpy.int64(self.local_array[2]), push_twice)

def lload_3(self):
    """loads a long from local long data array at index 3 onto stack"""
    self.stack.push_op(numpy.int64(self.local_array[3]), push_twice)

def lshl(self):
    """pop a long and an int and shift the long bitwise left by the low 6 bits
    of the int (0-63) and push the result back to the stack"""
    zero_to_sixty_three_mask = 0x3f
    int_val = self.stack.pop_op() & zero_to_sixty_three_mask
    long_val = self.stack.pop_op(pop_twice)
    self.stack.push_op(numpy.int64(long_val) << int_val, push_twice)

def lshr(self):
    """pop a long and an int and shift the long bitwise right by the low 6 bits
    of the int (0-63) and push the result back to the stack"""
    zero_to_sixty_three_mask = 0x3f
    int_val = self.stack.pop_op() & zero_to_sixty_three_mask
    long_val = self.stack.pop_op(pop_twice)
    self.stack.push_op(numpy.int64(long_val) >> int_val, push_twice)

def land(self):
    """pop 2 longs, AND them and push the result to the stack"""
    val2 = self.stack.pop_op(pop_twice)
    val1 = self.stack.pop_op(pop_twice)
    self.stack.push_op(numpy.int64(val1 & val2), push_twice)

def lcmp(self):
    """pop 2 values and push 1 if val1>val2, 0 if val1=val2, -1 if val1<val2"""
    val2 = self.stack.pop_op(pop_twice)
    val1 = self.stack.pop_op(pop_twice)
    val1 -= val2
    if val1 == 0:
        self.stack.push_op(0)
    else:
        self.stack.push_op((val1/abs(val1)))

def lxor(self):
    """pop 2 long, xor them, and push the result"""
    val2 = self.stack.pop_op(pop_twice)
    val1 = self.stack.pop_op(pop_twice)
    self.stack.push_op(numpy.int64(val1 ^ val2), push_twice)

def fcmph(self, nan_spec):
    """helper function to reduce duplication.
nan_spec is the value to push if at least one of the values is not a number"""
    val2 = self.stack.pop_op()
    val1 = self.stack.pop_op()
    if numpy.isnan(val1) or numpy.isnan(val2):
        self.stack.push_op(nan_spec)
    else:
        val1 -= val2
        if val1 == 0:
            self.stack.push_op(0)
        else:
            self.stack.push_op((val1/abs(val1)))

def fcmpg(self):
    """pop 2 values and push 1 if val1>val2, 0 if val1=val2, -1 if val1<val2,
    1 if val1 or val2 is NaN"""
    fcmph(self, 1)

def fcmpl(self):
    """pop 2 values and push 1 if val1>val2, 0 if val1=val2, -1 if val1<val2,
    -1 if val1 or val2 is NaN"""
    fcmph(self, -1)

def fneg(self):
    """pop a float and push the negation to the stack"""
    self.stack.push_op(numpy.negative(self.stack.pop_op()))

def lconst_0(self):
    """push 0L to the stack"""
    self.stack.push_op(numpy.int64(0), push_twice)

def lconst_1(self):
    """push 1L to the stack"""
    self.stack.push_op(numpy.int64(1), push_twice)

def fconst_0(self):
    """push 0F to the stack"""
    self.stack.push_op(numpy.float32(0))

def fconst_1(self):
    """push 1F to the stack"""
    self.stack.push_op(numpy.float32(1))

def fconst_2(self):
    """push 2F to the stack"""
    self.stack.push_op(numpy.float32(2))

def fload(self, index):
    """loads a float from local float data array at <index> onto stack"""
    self.stack.push_op(numpy.float32(self.local_array[index]))

def fload_0(self):
    """loads a float from local float data array at index 0 onto stack"""
    self.stack.push_op(numpy.float32(self.local_array[0]))

def fload_1(self):
    """loads a float from local float data array at index 1 onto stack"""
    self.stack.push_op(numpy.float32(self.local_array[1]))

def fload_2(self):
    """loads a float from local float data array at index 2 onto stack"""
    self.stack.push_op(numpy.float32(self.local_array[2]))

def fload_3(self):
    """loads a float from local float data array at index 3 onto stack"""
    self.stack.push_op(numpy.float32(self.local_array[3]))

def l2d(self):
    """convert long to double"""
    self.stack.push_op(numpy.float64(self.stack.pop_op(pop_twice)), push_twice)

def l2i(self):
    """convert long to int"""
    self.stack.push_op(numpy.int32(self.stack.pop_op(pop_twice)))

def l2f(self):
    """convert long to int"""
    self.stack.push_op(numpy.float32(self.stack.pop_op(pop_twice)))

def f2d(self):
    """convert float to double"""
    self.stack.push_op(numpy.float64(self.stack.pop_op()), push_twice)

def f2i(self):
    """convert float to int"""
    self.stack.push_op(numpy.int32(self.stack.pop_op()))

def f2l(self):
    """convert float to long"""
    self.stack.push_op(numpy.int64(self.stack.pop_op()), push_twice)

def fadd(self):
    """implements the fadd opcode"""
    val2 = numpy.float32(self.stack.pop_op())
    val1 = numpy.float32(self.stack.pop_op())
    self.stack.push_op(val1 + val2)

def ladd(self):
    """implements the ladd opcode"""
    val2 = numpy.int64(self.stack.pop_op(pop_twice))
    val1 = numpy.int64(self.stack.pop_op(pop_twice))
    self.stack.push_op(val1 + val2, push_twice)

def fsub(self):
    """implements the fsub opcode"""
    val2 = numpy.float32(self.stack.pop_op())
    val1 = numpy.float32(self.stack.pop_op())
    self.stack.push_op(val1 - val2)

def lsub(self):
    """implements the fsub opcode"""
    val2 = numpy.int64(self.stack.pop_op(pop_twice))
    val1 = numpy.int64(self.stack.pop_op(pop_twice))
    self.stack.push_op(val1 - val2, push_twice)

def fmul(self):
    """implements the fmul opcode"""
    val2 = numpy.float32(self.stack.pop_op())
    val1 = numpy.float32(self.stack.pop_op())
    self.stack.push_op(val1 * val2)

def lmul(self):
    """implements the fsub opcode"""
    val2 = numpy.int64(self.stack.pop_op(pop_twice))
    val1 = numpy.int64(self.stack.pop_op(pop_twice))
    self.stack.push_op(val1 * val2, push_twice)

def fdiv(self):
    """implements the fdiv opcode"""
    val2 = numpy.float32(self.stack.pop_op())
    val1 = numpy.float32(self.stack.pop_op())
    self.stack.push_op(numpy.float32(val1 / val2))

def ldiv(self):
    """implements the fsub opcode"""
    val2 = numpy.int64(self.stack.pop_op(pop_twice))
    val1 = numpy.int64(self.stack.pop_op(pop_twice))
    self.stack.push_op(numpy.int64(val1 / val2), push_twice)

# frem will be implemented in terms of the other operations.
# a%b = a-(a/b)*b
def frem(self):
    """implements the frem opcode"""
    val2 = numpy.float32(self.stack.pop_op())
    val1 = numpy.float32(self.stack.pop_op())
    if val2 == 0:
        self.stack.push_op(val2)
    else:
        self.stack.push_op(val1)
        self.stack.push_op(val1)
        self.stack.push_op(val2)
        fdiv(self)
        self.stack.push_op(val2)
        fmul(self)
        fsub(self)

def lrem(self):
    """implements the frem opcode"""
    val2 = numpy.int64(self.stack.pop_op(pop_twice))
    val1 = numpy.int64(self.stack.pop_op(pop_twice))
    if val2 == 0:
        self.stack.push_op(val2, push_twice)
    else:
        self.stack.push_op(val1, push_twice)
        self.stack.push_op(val1, push_twice)
        self.stack.push_op(val2, push_twice)
        ldiv(self)
        self.stack.push_op(val2, push_twice)
        lmul(self)
        lsub(self)