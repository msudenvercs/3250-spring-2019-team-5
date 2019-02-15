"""this file contains the OpCodes class"""
class OpCodes():
    """This class is used for the interpretation of opcodes"""
    def __init__(self):
        """this is the constructor"""
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
