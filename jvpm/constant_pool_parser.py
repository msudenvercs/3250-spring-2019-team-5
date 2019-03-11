"""This module will,  given the class file data,  parse out the constant pool"""


class ConstantPoolParser:
    """constant pool parser"""

    def __init__(self, data):
        """Constructor"""
        self.data = data
# compute the constant pool count since it is used later.
        self.count = (self.data[8] << 8) + self.data[9]
# we start at offset 10 since there are 10 bytes before the start of the
# constant pool.
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
        result = None
# if this is a utf-8 constant, then get the length and grab that many bytes.
        if tag == 1:
            length_high = self.data[self.offset + 1]
            length_low = self.data[self.offset + 2]
            length = (length_high << 8) + length_low
# now, grab the tag, the 2-byte length field, and the number of bytes
# indicated by that field.
            total_bytes = length + 3
            result = self.data[self.offset:self.offset + total_bytes]
# don't forget to increment offset.
            self.offset += total_bytes
# otherwise, look up the number of bytes to grab as before.
        else:
            length = self.table[tag]
            result = self.data[self.offset:self.offset + length]
            self.offset += length
        return result

    def get_all_constants(self):
        """gets count-1 constants from the constant pool,
taking into account the fact that long and double take up 2 entries"""
# constant pool entries start at index 1, so index 0 is filled with a
# dummy value.
        pool = [None]
# We don't know how many constants there actually are,
# so the pool shall be filled via the following algorithm:
# 1. Does pool contain count entries?
# 2. If so, exit
# 3. If not, go to step 4.
# 4. let tag = the first byte of the constant.
# 5. append constant to pool.
# 6. if tag is 5 or 6, then append a dummy value of none to the pool
# 7. Go back to step 1.
        while len(pool) != self.count:
            constant = self.get_single_constant()
            pool.append(constant)
            tag = constant[0]
            if tag in [5, 6]:
                pool.append(None)
        return pool
