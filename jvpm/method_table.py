"""This module contains implementations of native methods like println"""


class MethodTable:
    """This module contains implementations of native methods like println"""

    def __init__(self):
        """constructor"""
        self.table = {
            "java/io/PrintStream.println(Ljava/lang/String;)V": println,
            "java/io/PrintStream.println(I)V": println,
            "java/util/Scanner.<init>(Ljava/io/InputStream;)V": scanner,
            "java/util/Scanner.nextInt()I": next_int}

    def call(self, op_codes, official_name):
        """calls a method from the table based on its name.
op_codes is the OpCodesObject that will be used to run the method"""
        self.table[official_name](op_codes)
    def mph3(self):
        """pylint, quit complaining"""
        return len(self.table)

def println(op_codes):
    """This function causes the jvm to print to the screen"""
    to_be_printed = op_codes.stack.pop_op()
# not used, but required so future opcodes work properly
    op_codes.stack.pop_op()
# and finally, the big print!
    print(to_be_printed)

def scanner(stack):
    """take the top two items off the stack and push a scanner object on the stack"""
    stack.stack.pop_op()
    stack.stack.pop_op()
    stack.stack.push_op('scanner')

def next_int(stack):
    """take the top element of the stack,
read in an int and pushes that int onto the stack"""
    stack.stack.pop_op()
    i = int(input())
    stack.stack.push_op(i)
