import hexdump
"""this file contains the OpCodes class"""
class OpCodes():
    """This class is used for the interpretation of opcodes"""
    def __init__(self):
        """this is the constructor"""
        with open ('Test.class', 'rb') as binary_file:
            self.data = binary_file.read()
        self.table = {0x00: not_implemented}


    def interpret(self, value):
        """this is the method used to interpret a given opcode"""
        return self.table[value]()

    def mph1(self):
        """method to make pylint shut up"""
        return self.table

def not_implemented():
    """this is a dummy method"""
    return 'not implemented'

if __name__ == '__main__':
    c = OpCodes()
    iWantItAll = hexdump.hexdump(c.data, result = 'return')
    s = 10
    e = 58
    goodgood = ''
    for i in range(0, int((len(iWantItAll)/66))):
        goodgood += iWantItAll[s: e] + '\n'
        s += 77
        e += 77

    print(goodgood)
    for i, j in enumerate(goodgood, 1):
        print(hex(j))
        
        if i == 0x2a:
            print('aload_0')
        if i == 0xb1:
            print('return')
        if i == 0x04:
            print('iconst_1')
        if i == 0x3c:
            print('istore_1')
        if i == 0x84:
            print('iinc')
        if i == 0xb7:
            print('invokespecial')