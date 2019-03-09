"""This module will,  given the class file data,  parse out the constant pool"""


class ConstantPoolParser:
    """constant pool parser"""

    def __init__(self, data):
        """Constructor"""
        self.data = data
        # we start at offset 10 since there are 10 bytes before the start of
        # the constant pool.
        self.offset = 10
        # the following table indicates the number of bytes to grab for each
        # constant type based on its tag.
        self.table = {
            3: 5,
            4: 5,
            5: 9,
            6: 9,
            7: 3,
            8: 3,
            9: 5,
            10: 5,
            11: 5,
            12: 5,
            15: 4,
            16: 3,
            18: 5}

    def get_single_constant(self):
        """gets the appropriate number of bytes for 1 item of the constant pool depending on its
tag"""
        tag = self.data[self.offset]
#if this is a utf-8 constant, then get the length and grab that many bytes.
        if tag == 1:
            length_high = self.data[self.offset+1]
            length_low = self.data[self.offset+2]
            length = (length_high<<8)+length_low
#now, grab the tag, the 2-byte length field, and the number of bytes indicated by that field.
            total_bytes = length+3
            result = self.data[self.offset:self.offset+total_bytes]
#don't forget to increment offset.
            self.offset += total_bytes
            return result
#otherwise, look up the number of bytes to grab as before.
        else:
            length = self.table[tag]
            result = self.data[self.offset:self.offset + length]
            self.offset += length
            return result
