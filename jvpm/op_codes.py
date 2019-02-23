"""this file contains the OpCodes class"""
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
                      0x00: not_implemented}
        self.byte_count = 0

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
    self.byte_count += 1
    return 'not implemented'

def aload_0(self):
    """this is a dummy method"""
    print('aload_0')
    self.byte_count +=1

def ret(self):
    self.byte_count += 1
    print('return')

def iconst_1(self):
    self.byte_count += 1
    print('iconst_1')

def istore_1(self):
    self.byte_count += 1
    print('istore_1')

def iinc(self):
    self.byte_count += 1
    print('iinc')

def invokespecial(self):
    byte_1 = self.data[self.byte_count + 1]
    byte_2 = self.data[self.byte_count + 2]
    self.byte_count += 3
    byte_1 + byte_2
    print('invokespecial')
    

if __name__ == '__main__':
    op = OpCodes()
    op.parse_codes(183)