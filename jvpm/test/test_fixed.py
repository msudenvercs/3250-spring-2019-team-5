from unittest import TestCase
from jvpm.parsing.Parser import Parser, Jvm
class TestFixed(TestCase):
    def test_parser_constructor(self):
        p = Parser(b"hello")
        self.assertEqual(p.code,b"hello")
        self.assertEqual(p.offset,0)
        self.assertEqual(type(p.jvm),Jvm)
    def test_get_bytes(self):
        p = Parser(b"hello")
        self.assertEqual(p.getBytes(2),b"he")
        self.assertEqual(p.offset,2)
    def test_fixed(self):
        p = Parser(b"1234567890")
        p.get_magic()
        p.get_minor_version()
        p.get_major_version()
        p.get_constant_pool_count()
        self.assertEqual(p.jvm.magic,b"1234")
        self.assertEqual(p.jvm.minor_version,b"56")
        self.assertEqual(p.jvm.major_version,b"78")
        self.assertEqual(p.jvm.constant_pool_count,b"90")
