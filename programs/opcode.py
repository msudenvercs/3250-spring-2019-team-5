import unittest
from unittest.mock import mock_open, patch

class ClassFile():
    def __init__(self):
        with open('test.class', 'rb') as binary_file:
            self.data = binary_file.read()

    def get_magic(self):
        magic = ""
        for i in range(4):
            magic += format(self.data[i], '02X')
        return magic

    def get_minor(self):
        return self.data[4] + self.data[5]

    def get_major(self):
        return self.data[6] + self.data[7]

if '__main__' == __name__:
    cf = ClassFile()
    print(cf.get_magic())

class OpCodes():
    def __init__(self):
        self.table = {0x00: self.not_implemented}

    def not_implemented(self):
        return 'not implemented'

    def interpret(self, value: object) -> object:
        return self.table[value]()

class TestClassFile(unittest.TestCase):
    #\xCA\xFE\xBA\xBE\x00\x01\x02\x03\' + \
    def setUp(self):
        m = unittest.mock.mock_open(read_data=b'\xca\xfe\xba\xbe\x00\x00\x00\x34\x00\x0f\x0a\x00\x03\x00\x0c\x07' +
                                              b'\x00\x0d\x07\x00\x0e\x01\x00\x06\x3c\x69\x6e\x69\x74\x3e\x01\x00' +
                                              b'\x03\x28\x29\x56\x01\x00\x04\x43\x6f\x64\x65\x01\x00\x0f\x4c\x69' +
                                              b'\x6d\x61\x69\x6e\x01\x00\x16\x28\x5b\x4c\x6a\x61\x76\x61\x2f\x6c' +
                                              b'\x61\x6e\x67\x2f\x53\x74\x72\x69\x6e\x67\x3b\x29\x56\x01\x00\x0a' +
                                              b'\x53\x6f\x75\x72\x63\x65\x46\x69\x6c\x65\x01\x00\x0b\x73\x69\x6d' +
                                              b'\x53\x6f\x75\x72\x63\x65\x46\x69\x6c\x65\x01\x00\x0b\x73\x69\x6d' +
                                              b'\x70\x6c\x65\x2e\x6a\x61\x76\x61\x0c\x00\x04\x00\x05\x01\x00\x04' +
                                              b'\x74\x65\x73\x74\x01\x00\x10\x6a\x61\x76\x61\x2f\x6c\x61\x6e\x67' +
                                              b'\x2f\x4f\x62\x6a\x65\x63\x74\x00\x20\x00\x02\x00\x03\x00\x00\x00' +
                                              b'\x00\x00\x02\x00\x00\x00\x04\x00\x05\x00\x01\x00\x06\x00\x00\x00' +
                                              b'\x1d\x00\x01\x00\x01\x00\x00\x00\x05\x2a\xb7\x00\x01\xb1\x00\x00' +
                                              b'\x00\x01\x00\x07\x00\x00\x00\x06\x00\x01\x00\x00\x00\x01\x00\x08' +
                                              b'\x00\x08\x00\x09\x00\x01\x00\x06\x00\x00\x00\x1e\x00\x01\x00\x02' +
                                              b'\x00\x00\x00\x06\x04\x3c\x84\x01\x01\xb1\x00\x00\x00\x01\x00\x07' +
                                              b'\x00\x00\x00\x06\x00\x01\x00\x00\x00\x01\x00\x01\x00\x0a\x00\x00' +
                                              b'00\x02\x00\x0b')
        with patch(__name__ + '.open', m):
            self.cf = ClassFile()

    def test_magic(self):
        self.assertEqual(self.cf.get_magic(), 'CAFEBABE')

    def test_minor(self):
        self.assertEqual(self.cf.get_minor(), 1)

    def test_major(self):
        self.assertEqual(self.cf.get_major(), 5)

class TestOpCodes(unittest.TestCase):
    def test_not_implmented(self):
        self.assertEqual(OpCodes().interpret(0), 'not implemented')
        with self.assertRaises(KeyError):
            OpCodes().interpret(1)
