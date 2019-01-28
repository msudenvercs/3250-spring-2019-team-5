import unittest
import sys
import jvpm.HelloWorld
from unittest.mock import Mock, call

class TestHelloWorld(unittest.TestCase):
    def test_HelloWorld(self):
        sys.stdout = unittest.mock.Mock()
        jvpm.HelloWorld.HelloWorld()
        sys.stdout.assert_has_calls(
            [call.write('Hello world'), call.write('\n')],
            [call.write('Brian Pedersen'), call.write('\n')]
            [call.write('Jake Schnorr'), call.write('\n')]
            [call.write('Megan Stucky'), call.write('\n')]
        )
