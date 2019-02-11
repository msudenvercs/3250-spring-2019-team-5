#this file contains all classes that represent the types of constants discussed in section 4.4 of the java language specification (relating to the constant pool of the class file format)
#the class Constant is the class from which all constant types will derive
class Constant:
    def __init__(self):
        pass
#I have discovered that long and double constants take 2 entries in the constant pool. To solve this, I will create a method named add_to_pool. This method will take an array in which the constant pool will be stored. By default, the constant will simply be added to the array. However, for long and double, it will be overridden such that it adds the constant as well as the dummy value None to the constant pool. Technically, I could have chosen any value to go in that second slot since it is never used, but I have chosen None so that if the second slot somehow gets used, an exception will be thrown.
    def add_to_pool(self,pool):
        pool.append(self)
class ConstClass(Constant):
    def __init__(self,name_index):
        self.name_index = name_index
class ConstFieldRef(Constant):
    def __init__(self,class_index,name_and_type_index):
        self.class_index = class_index
        self.name_and_type_index = name_and_type_index
class ConstMethodRef(Constant):
    def __init__(self,class_index,name_and_type_index):
        self.class_index = class_index
        self.name_and_type_index = name_and_type_index
class ConstInterfaceMethodRef(Constant):
    def __init__(self,class_index,name_and_type_index):
        self.class_index = class_index
        self.name_and_type_index = name_and_type_index
class ConstString(Constant):
    def __init__(self,string_index):
        self.string_index = string_index
class ConstInteger(Constant):
    def __init__(self,chars): #I'm doing this to avoid potential name conflicts with the python bytes type
        self.chars = chars
class ConstFloat(Constant):
    def __init__(self,chars):
        self.chars = chars
class ConstLong(Constant):
    def __init__(self,high_bytes,low_bytes):
        self.high_bytes = high_bytes
        self.low_bytes = low_bytes
    def add_to_pool(self,pool):
        pool.append(self)
        pool.append(None)
class ConstDouble(Constant):
    def __init__(self,high_bytes,low_bytes):
        self.high_bytes = high_bytes
        self.low_bytes = low_bytes
    def add_to_pool(self,pool):
        pool.append(self)
        pool.append(None)

class ConstNameAndType(Constant):
    def __init__(self,name_index,descriptor_index):
        self.name_index = name_index
        self.descriptor_index = descriptor_index
class ConstUtf8(Constant):
    def __init__(self,length,chars):
        self.length = length
        self.chars = chars
class ConstMethodHandle(Constant):
    def __init__(self, reference_kind, reference_index):
        self.reference_kind = reference_kind
        self.reference_index = reference_index
class ConstMethodType(Constant):
    def __init__(self,descriptor_index):
        self.descriptor_index = descriptor_index
class ConstInvokeDynamic(Constant):
    def __init__(self,bootstrap_method_attr_index,name_and_type_index):
        self.bootstrap_method_attr_index = bootstrap_method_attr_index
        self.name_and_type_index = name_and_type_index
