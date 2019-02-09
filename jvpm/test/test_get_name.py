from unittest import TestCase
from jvpm.parsing import get_name
class TestGetName(TestCase):
    get_name.input = lambda x: "test.class"
    def test_get_name(self):
        self.assertEqual(get_name.get_name(),"test.class")
