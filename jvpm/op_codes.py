"""this file contains the OpCodes class"""
import numpy #to get the java-like behavior for arithmetic

from jvpm.jvm_stack import JvmStack

#shuts off the overflow warnings from numpy
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
                      0x15: [iload, 1],
                      0x1a: [iload_0, 1],
                      0x1b: [iload_1, 1],
                      0x1c: [iload_2, 1],
                      0x1d: [iload_3, 1],
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
                      0x91: [i2b, 1],
                      0x92: [i2c, 1],
                      0x87: [i2d, 1],
                      0x86: [i2f, 1],
                      0x00: [not_implemented, 1]}
        self.byte_count = 0
        self.stack = JvmStack()
    def parse_codes(self, op_start):
        """this method searches the binary for only the opcodes we know are in it"""
        self.byte_count = op_start
        while self.byte_count < len(self.data):
            if self.data[self.byte_count] in {0x2a, 0xb1, 0x04, 0x3c, 0x84, 0xb7}:
                self.interpret(self.data[self.byte_count])
            else:
                self.interpret(0)

    def interpret(self, value):
        """this is the method used to interpret a given opcode"""
        self.byte_count += self.table[value][1]
        return self.table[value][0](self)

def not_implemented(self):
    """this is a dummy function"""
    return 'not implemented'

def aload_0(self):
    """loads a reference from the data array onto stack"""
    print('aload_0')

def iload(self, index):
    """loads an int from local data array at <index>"""
    self.stack.push_op(self.data[index])

def iload_0(self):
    """loads an int from local data array at index 0"""
    self.stack.push_op(self.data[0])

def iload_1(self):
    """loads an int from local data array at index 1"""
    self.stack.push_op(self.data[1])

def iload_2(self):
    """loads an int from local data array at index 2"""
    self.stack.push_op(self.data[2])

def iload_3(self):
    """loads an int from local data array at index 3"""
    self.stack.push_op(self.data[3])

def ret(self):
    """this function will eventually implement the ret opcode"""
    print('return')

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

def iinc(self):
    """this function implements the iinc opcode"""
    print('iinc')

def invokespecial(self):
    """This function implements the invokespecial opcode"""
    byte_1 = self.data[self.byte_count + 1]
    byte_2 = self.data[self.byte_count + 2]
    print('invokespecial')
    return byte_1+byte_2

def iadd(self):
    """implements the iadd opcode"""
    val2 = numpy.int32(self.stack.pop_op())
    val1 = numpy.int32(self.stack.pop_op())
    self.stack.push_op(val1+val2)

def isub(self):
    """implements the isub opcode"""
    val2 = numpy.int32(self.stack.pop_op())
    val1 = numpy.int32(self.stack.pop_op())
    self.stack.push_op(val1-val2)

def imul(self):
    """implements the imul opcode"""
    val2 = numpy.int32(self.stack.pop_op())
    val1 = numpy.int32(self.stack.pop_op())
    self.stack.push_op(val1*val2)

def idiv(self):
    """implements the idiv opcode"""
    val2 = numpy.int32(self.stack.pop_op())
    val1 = numpy.int32(self.stack.pop_op())
    self.stack.push_op(numpy.int32(val1/val2))

#irem will be implemented in terms of the other operations.
#a%b = a-(a/b)*b
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
    self.stack.push_op(numpy.int64(convert_this))

def i2s(self):
    """convert int on top of stack to short, and push. it. to. the. stack."""
    convert_this = self.stack.pop_op()
    self.stack.push_op(numpy.int16(convert_this))
