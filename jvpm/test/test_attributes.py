from unittest import TestCase
from jvpm.parsing.Parser import *
class TestAttributes(TestCase):
    def test_attributes(self):
        p = Parser(b"fu\x00\x00\x00\x05hellonb\x00\x00\x00\x07goodbyell\x00\x00\x00\x20the sun will come out tomorrow  ")
        attributes = p.get_jvm_attributes(3)
        a = p.jvm.attributes[0]
        self.assertEqual(type(a),Attribute)
        self.assertEqual(a.attribute_name_index,b"fu")
        self.assertEqual(a.attribute_length,b"\x00\x00\x00\x05")
        self.assertEqual(a.info,b"hello")
        a = p.jvm.attributes[1]
        self.assertEqual(type(a),Attribute)
        self.assertEqual(a.attribute_name_index,b"nb")
        self.assertEqual(a.attribute_length,b"\x00\x00\x00\x07")
        self.assertEqual(a.info,b"goodbye")
        a = p.jvm.attributes[2]
        self.assertEqual(type(a),Attribute)
        self.assertEqual(a.attribute_name_index,b"ll")
        self.assertEqual(a.attribute_length,b"\x00\x00\x00\x20")
        self.assertEqual(a.info,b"the sun will come out tomorrow  ")
        l = len(b"fu\x00\x00\x00\x05hellonb\x00\x00\x00\x07goodbyell\x00\x00\x00\x20the sun will come out tomorrow  ")
        self.assertEqual(p.offset,l)
