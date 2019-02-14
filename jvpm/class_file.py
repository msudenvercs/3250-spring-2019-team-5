class ClassFile():
    def __init__(self,name):
        with open(name, 'rb') as binary_file:
            self.data = binary_file.read()

    def get_magic(self):
        return self.data[0:4]

    def get_minor(self):
        return self.data[4:6]

    def get_major(self):
        return self.data[6:8]

    def get_constant_pool_count(self):
        return self.data[8:10]
