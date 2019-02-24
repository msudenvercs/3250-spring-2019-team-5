"""this file contains the OpCodes class"""
import numpy #to get the java-like behavior for arithmetic

from jvpm.jvm_stack import JvmStack

#shuts off the overflow warnings from numpy
numpy.seterr(all="ignore")
class OpCodes():
    """This class is used for the interpretation of opcodes"""
    def __init__(self):
        """this is the constructor"""
        with open('jvpm/Test.class', 'rb') as binary_file:
            self.data = bytes(binary_file.read())
        self.table = {0x2a: aload_0,
                      0xb1: ret,
                      0x04: iconst_1,
                      0x3c: istore_1,
                      0x84: iinc,
                      0xb7: invokespecial,
                      0x60: iadd,
                      0x64: isub,
                      0x00: not_implemented}
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
        return self.table[value](self)

def not_implemented(self):
    """this is a dummy function"""
    self.byte_count += 1
    return 'not implemented'

def aload_0(self):
    """this is a dummy method"""
    print('aload_0')
    self.byte_count += 1

def ret(self):
    """this function will eventually implement the ret opcode"""
    self.byte_count += 1
    print('return')

def iconst_1(self):
    """this function implements the iconst_1 opcode"""
    self.byte_count += 1
    print('iconst_1')

def istore_1(self):
    """this function implements the istore_1 opcode"""
    self.byte_count += 1
    print('istore_1')

def iinc(self):
    """this function implements the iinc opcode"""
    self.byte_count += 1
    print('iinc')

def invokespecial(self):
    """This function implements the invokespecial opcode"""
    byte_1 = self.data[self.byte_count + 1]
    byte_2 = self.data[self.byte_count + 2]
    self.byte_count += 3
    print('invokespecial')
    return byte_1+byte_2
def iadd(self):
    """implements the iadd opcode"""
    val2 = self.stack.pop_op()
    val1 = self.stack.pop_op()
    self.stack.push_op(val1+val2)
    self.byte_count += 1
def isub(self):
    """implements the isub opcode"""
    val2 = self.stack.pop_op()
    val1 = self.stack.pop_op()
    self.stack.push_op(val1-val2)
    self.byte_count += 1
if __name__ == '__main__':
    OP = OpCodes()
    OP.parse_codes(183)
