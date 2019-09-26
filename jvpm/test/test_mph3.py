"""tests the filler method"""
from unittest import TestCase
from jvpm.method_table import MethodTable


class TestMph3(TestCase):
    """tests the filler method"""
    def test_filler(self):
        """tests the filler method"""
        self.assertEqual(MethodTable().mph3(), len(MethodTable().table))
