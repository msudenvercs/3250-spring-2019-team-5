"""tests invokevirtual"""
from unittest import TestCase
from unittest.mock import Mock, call
import sys
import base64
from jvpm.op_codes import OpCodes


class TestInvokeVirtual(TestCase):
    """tests invokevirtual"""

    def test_print_string(self):
        """tests the printing of strings"""
        data = bytes("""
yv66vgAAADQAHQoABgAPCQAQABEIABIKABMAFAcAFQcAFgEABjxpbml0PgEAAygpVgEABENvZGUB
AA9MaW5lTnVtYmVyVGFibGUBAARtYWluAQAWKFtMamF2YS9sYW5nL1N0cmluZzspVgEAClNvdXJj
ZUZpbGUBAAdIdy5qYXZhDAAHAAgHABcMABgAGQEAC0hlbGxvIHdvcmxkBwAaDAAbABwBAAJIdwEA
EGphdmEvbGFuZy9PYmplY3QBABBqYXZhL2xhbmcvU3lzdGVtAQADb3V0AQAVTGphdmEvaW8vUHJp
bnRTdHJlYW07AQATamF2YS9pby9QcmludFN0cmVhbQEAB3ByaW50bG4BABUoTGphdmEvbGFuZy9T
dHJpbmc7KVYAIQAFAAYAAAAAAAIAAQAHAAgAAQAJAAAAHQABAAEAAAAFKrcAAbEAAAABAAoAAAAG
AAEAAAABAAkACwAMAAEACQAAACUAAgABAAAACbIAAhIDtgAE
""", encoding="utf-8")
        code = base64.decodebytes(data)
        op_codes = OpCodes()
        op_codes.set_data(code)
        sys.stdout = Mock()
        op_codes.parse_codes(370)
        self.assertTrue(sys.stdout.has_calls(
            [call.write("hello world"), call.write("\n")]))

    def test_print_int(self):
        """tests the printing of ints"""
        data = bytes(
            """yv66vgAAADQAGwoABQAOCQAPABAKABEAEgcAEwcAFAEABjxpbml0PgEAAygpVgEABENvZGUBAA9M
aW5lTnVtYmVyVGFibGUBAARtYWluAQAWKFtMamF2YS9sYW5nL1N0cmluZzspVgEAClNvdXJjZUZp
bGUBAAdIaS5qYXZhDAAGAAcHABUMABYAFwcAGAwAGQAaAQACSGkBABBqYXZhL2xhbmcvT2JqZWN0
AQAQamF2YS9sYW5nL1N5c3RlbQEAA291dAEAFUxqYXZhL2lvL1ByaW50U3RyZWFtOwEAE2phdmEv
aW8vUHJpbnRTdHJlYW0BAAdwcmludGxuAQAEKEkpVgAhAAQABQAAAAAAAgABAAYABwABAAgAAAAd
AAEAAQAAAAUqtwABsQAAAAEACQAAAAYAAQAAAAEACQAKAAsAAQAIAAAAJAACAAEAAAAIsgACB7YA
Aw==
""", encoding="utf-8")
        code = base64.decodebytes(data)
        op_codes = OpCodes()
        op_codes.set_data(code)
        sys.stdout = Mock()
        op_codes.parse_codes(336)
        self.assertTrue(sys.stdout.has_calls(
            [call.write("4"), call.write("\n")]))
