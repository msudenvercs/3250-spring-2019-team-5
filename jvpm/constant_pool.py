"""This class represents the constant pool parsed from a class file"""
import struct


class ConstantPool:
    """This class represents the constant pool parsed from a class file"""

    def __init__(self, constants):
        """constructor"""
        self.constants = constants
# the following table contains functions that load various kinds of
# operands onto the stack.
        self.load_table = {
            3: ConstantPool.load_int,
            8: ConstantPool.load_string}

    def lookup_constant(self, index):
        """Looks up a constant in the constant pool.
Index is a string of two bytes that determines which entry in the constant pool will be returned.
Let b1 and b2 be the bytes of index.
Then, this method shall return the constant at index (b1<<8)+b2"""
# the index is an unsigned short in big-endian byte order
        numeric_index = struct.unpack(">H", index)[0]
        return self.constants[numeric_index]

    def load_constant(self, index, stack):
        """Loads a constant onto the stack according to its type
Index shall have the same meaning as in lookup_constant.
Stack shall be the stack onto which the constant shall be loaded.
the constant shall always be loaded on top of the stack"""
        constant = self.lookup_constant(index)
        tag = constant[0]
        if tag in self.load_table.keys():
            self.load_table[tag](self, constant, stack)
        else:
            stack.push_op(constant)

    def load_int(self, constant, stack):
        """loads an int onto the stack"""
# integer constants are signed and big-endian.
        decoded = struct.unpack(">i", constant[1:])[0]
        stack.push_op(decoded)
#use self to make pylint happy
        self.constants.append(1)
        self.constants.pop()

    def load_string(self, constant, stack):
        """loads a string onto the stack"""
# first get the index of the actual utf-8 contents
        string_index = constant[1:]
# now get the actual contents at that index
        real_utf8 = self.lookup_constant(string_index)
# now retrieve the actual string as before
        decoded = real_utf8[3:].decode("utf-8")
        stack.push_op(decoded)
