#this class represents the parser for jvpm. Given a bytes object read from a class file, it will construct a Jvm instance with all the state necessary to execute the program in the class file. Note that I will only be extracting the fields; executing the code is beyond the scope of this sprint.
class Parser:
    def __init__(self,code):
        self.code = code
        self.offset = 0 #this field tracks where I am in the class file relative to the start.
        self.jvm = Jvm()
    def getBytes(self,n): #this method gets n bytes from the current position in the code.
        chars = self.code[self.offset:self.offset+n]
        self.offset += n
        return chars
    def get_magic(self): #gets the magic number.
        self.jvm.magic = self.getBytes(4)
    def get_minor_version(self):
        self.jvm.minor_version = self.getBytes(2)
    def get_major_version(self):
        self.jvm.major_version = self.getBytes(2)
    def get_constant_pool_count(self):
        self.jvm.constant_pool_count = self.getBytes(2)
    def get_access_flags(self):
        self.jvm.access_flags = self.getBytes(2)
    def get_this_class(self):
        self.jvm.this_class = self.getBytes(2)
    def get_superclass(self):
        self.jvm.superclass = self.getBytes(2)
    def get_interfaces_count(self):
        self.jvm.interfaces_count = self.getBytes(2)
class Jvm:
    def __init__(self):
        pass
