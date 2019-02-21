"""

This is a simple program James created so we could have something to demo at the end of sprint 2
and will not be included in the final product.

"""
#https://stackoverflow.com/questions/23417941/import-error-no-module-named-does-exist
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from jvpm.class_file import ClassFile
#the main program
def main():
    """hack to make pylint shut up"""
    file_name = input("Which file do you wish to parse? ")
    class_file = ClassFile(file_name)
    magic = class_file.get_magic()
    minor = class_file.get_minor()
    major = class_file.get_major()
    constant_pool_count = class_file.get_constant_pool_count()
    output_string = b"The magic number is "+magic
    output_string += b" The minor version is "+minor
    output_string += b" The major version is "+major
    output_string += b" The constant pool count is "+constant_pool_count
    print(output_string)
if __name__ == "__main__":
    main()
