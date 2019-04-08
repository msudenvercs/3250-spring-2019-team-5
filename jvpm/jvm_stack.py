"""This class implements the operand stack for the jvm"""
class JvmStack:
    """JvmStack"""
    def __init__(self):
        """Constructor. Initializes the stack to be empty"""
        self.stack = []
    def push_op(self, obj):
        """pushes one operand onto the top of the stack"""
        self.stack.append(obj)
    def pop_op(self):
        """Pops one object off of the stack and then returns it"""
        if self.stack:
            return self.stack.pop()
        raise EmptyStackError("Can't pop from an empty stack")
    def peek(self):
        """returns the top element of the stack without popping it.
This doesn't seem useful now,
but it is one of the standard stack operations that might be useful later
"""
        return self.stack[-1]
class EmptyStackError(Exception):
    """error raised when there is an empty stack"""
