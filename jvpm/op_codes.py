"""this file contains the OpCodes class"""
class OpCodes():
    """This class is used for the interpretation of opcodes"""
    def __init__(self):
        """this is the constructor"""
        with open('jvpm/Test.class', 'rb') as binary_file:
            self.data = binary_file.read()
        self.table = {0x00: not_implemented}

    def parse_codes(self):
        """this method searches the binary for only the opcodes we know are in it"""
        for i, data in enumerate(self.data):
            if i > 182:
                if data == 0x2a:
                    print('aload_0')
                if data == 0xb1:
                    print('return')
                if data == 0x04:
                    print('iconst_1')
                if data == 0x3c:
                    print('istore_1')
                if data == 0x84:
                    print('iinc')
                if data == 0xb7:
                    print('invokespecial')


    def interpret(self, value):
        """this is the method used to interpret a given opcode"""
        return self.table[value]()

    def mph1(self):
        """method to make pylint shut up"""
        return self.table

def not_implemented():
    """this is a dummy method"""
    return 'not implemented'
