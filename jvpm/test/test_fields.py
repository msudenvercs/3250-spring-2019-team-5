from unittest import TestCase
from jvpm.parsing.Parser import *
class TestFields(TestCase):
    def test_fields(self):
        data = b"hello \x00\x00"
        data_length = len(data)
        p = Parser(data)
        p.get_fields(1)
        self.assertEqual(len(p.jvm.fields),1)
        field = p.jvm.fields[0]
        self.assertEqual(type(field),Field)
        self.assertEqual(field.access_flags,b"he")
        self.assertEqual(field.name_index,b"ll")
        self.assertEqual(field.descriptor_index,b"o ")
        self.assertEqual(field.attributes_count,b"\x00\x00")
        self.assertEqual(field.attributes,[])
        self.assertEqual(p.offset,data_length)
