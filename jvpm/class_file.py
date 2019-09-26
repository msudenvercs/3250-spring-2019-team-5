"""This class reads in a class file and does some basic parsing."""


class ClassFile():
    """Reads in a class file and does some basic parsing."""

    def __init__(self, name):
        """Construct a new instance of ClassFile."""
        with open(name, 'rb') as binary_file:
            self.data = binary_file.read()

    def get_magic(self):
        """Get the magic number."""
        return self.data[0:4]

    def get_minor(self):
        """Get the minor version."""
        return self.data[4:6]

    def get_major(self):
        """Get the major version."""
        return self.data[6:8]

    def get_constant_pool_count(self):
        """Get the bytes of the constant pool count."""
        return self.data[8:10]
