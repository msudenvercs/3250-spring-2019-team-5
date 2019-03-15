"""This module contains implementations of native methods like println"""


class MethodTable:
    """This module contains implementations of native methods like println"""

    def __init__(self):
        """constructor"""
        self.table = {
            "java/io/PrintStream.println(Ljava/lang/String;)V": println,
            "java/io/PrintStream.println(I)V": println}

    def call(self, op_codes, official_name):
        """calls a method from the table based on its name.
op_codes is the OpCodesObject that will be used to run the method"""
        self.table[official_name](op_codes)


def println(op_codes):
    to_be_printed = op_codes.stack.pop_op()
# not used, but required so future opcodes work properly
    op_codes.stack.pop_op()
# and finally, the big print!
    print(to_be_printed)
