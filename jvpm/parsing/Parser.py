#this class represents the parser for jvpm. Given a bytes object read from a class file, it will construct a Jvm instance with all the state necessary to execute the program in the class file. Note that I will only be extracting the fields; executing the code is beyond the scope of this sprint.
from jvpm.parsing.constant_types import *
class Parser:
    def __init__(self,code):
        self.code = code
        self.offset = 0 #this field tracks where I am in the class file relative to the start.
        self.jvm = Jvm()
#the lookup table for retrieving a constant from the constant pool.
        self.constant_table = {b"\x07":cf_class,
        b"\x09": cf_fieldRef,
        b"\x0a":cf_methodRef,
        b"\x0b":cf_interfaceMethodRef,
        b"\x08":cf_string,
        b"\x03":cf_integer,
        b"\x04":cf_float,
        b"\x05":cf_long,
        b"\x06":cf_double,
        b"\x0c":cf_nameAndType,
        b"\x01":cf_utf8,
        b"\x0f":cf_methodHandle,
        b"\x10":cf_methodType,
        b"\x12":cf_invokeDynamic}
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
#this method gets the interfaces implemented by this class. Each interface is a 2-byte index into the constant pool that refers to an interface.
    def get_interfaces(self):
        raw_bytes = self.jvm.interfaces_count
        num_interfaces = 256*raw_bytes[0]+raw_bytes[1]
        interfaces = []
        for i in range(num_interfaces):
            interfaces.append(self.getBytes(2))
        self.jvm.interfaces = interfaces
    def get_fields_count(self):
        self.jvm.fields_count = self.getBytes(2)
    def get_methods_count(self):
        self.jvm.methods_count = self.getBytes(2)
    def get_attributes_count(self):
        self.jvm.attributes_count = self.getBytes(2)
#gets one constant from the bytecode
    def get_constant(self):
#because I don't want to have a huge if-else statement, I will store the functions to get each type of constant in a lookup table indexed by the tag. Then, I will get the tag, look up the function, and then call it. I am allowed to do this because in python, functions are objects.
        tag = self.getBytes(1)
        return self.constant_table[tag](self)
#the prior method retrieves a single constant, but now I will retrieve all of the constants from the class file.
    def get_all_constants(self):
#The number of constants to retrieve is equal to constant_pool_count-1. The java language specification states that indexes into the constant pool begin at 1. To solve both of these problems, I will initialize the first element of the array to be used as the constant pool with a first element of None.
        constants = [None]
#convert the constant_pool_count to a number
        constant_pool_length = 256*self.jvm.constant_pool_count[0]+self.jvm.constant_pool_count[1]
#I know I am done retrieving constants when the length of the constant pool array reaches constant_pool_count
        while len(constants) != constant_pool_length: #I can rely on this field since it always comes before the actual constants in the class file.
            self.get_constant().add_to_pool(constants)
#now, store it in the jvm object for later use.
        self.jvm.constant_pool = constants
#gets the number of attributes indicated by count. This method will be used later in the parsing of fields and methods
    def get_attributes(self,count):
        attributes = []
        for i in range(count):
            attribute_name_index = self.getBytes(2)
            attribute_length = self.getBytes(4)
            a = (1<<24)*attribute_length[0]
            b = (1<<16)*attribute_length[1]
            c = (1<<8)*attribute_length[2]
            d = attribute_length[3]
            info = self.getBytes(a+b+c+d)
            attributes.append(Attribute(attribute_name_index,attribute_length,info))
        self.jvm.attributes = attributes
#this class represents a single attribute.
class Attribute:
    def __init__(self,attribute_name_index,attribute_length,info):
        self.attribute_name_index = attribute_name_index
        self.attribute_length = attribute_length
        self.info = info
class Jvm:
    def __init__(self):
        pass
#these functions get individual constant types.
def cf_class(p):
    return ConstClass(p.getBytes(2))
#I am only using temporary variables here because I don't know the order in which python evaluates function parameters; since they don't have any meaning outside the method, I will just call them a, b, ETC.
def cf_fieldRef(p):
    a = p.getBytes(2)
    b = p.getBytes(2)
    return ConstFieldRef(a,b)
def cf_methodRef(p):
    a = p.getBytes(2)
    b = p.getBytes(2)
    return ConstMethodRef(a,b)
def cf_interfaceMethodRef(p):
    a = p.getBytes(2)
    b = p.getBytes(2)
    return ConstInterfaceMethodRef(a,b)
def cf_string(p):
    return ConstString(p.getBytes(2))
def cf_integer(p):
    return ConstInteger(p.getBytes(4))
def cf_float(p):
    return ConstFloat(p.getBytes(4))
def cf_long(p):
    high = p.getBytes(4)
    low = p.getBytes(4)
    return ConstLong(high,low)
def cf_double(p):
    high = p.getBytes(4)
    low = p.getBytes(4)
    return ConstDouble(high,low)
def cf_nameAndType(p):
    a = p.getBytes(2)
    b = p.getBytes(2)
    return ConstNameAndType(a,b)
def cf_utf8(p):
    length = p.getBytes(2)
    length_as_num = 256*length[0]+length[1]
    chars = p.getBytes(length_as_num)
    return ConstUtf8(length,chars)
def cf_methodHandle(p):
    kind = p.getBytes(1)
    index = p.getBytes(2)
    return ConstMethodHandle(kind,index)
def cf_methodType(p):
    return ConstMethodType(p.getBytes(2))
def cf_invokeDynamic(p):
    a = p.getBytes(2)
    b = p.getBytes(2)
    return ConstInvokeDynamic(a,b)
