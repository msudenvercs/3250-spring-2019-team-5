import unittest
import sys
import jvpm.HelloWorld
from unittest.mock import Mock, call

class TestHelloWorld(unittest.TestCase):
    def test_HelloWorld(self):
        sys.stdout = unittest.mock.Mock()
        jvpm.HelloWorld.HelloWorld()
        sys.stdout.assert_has_calls(
            [
                call.write('Hello world'),
                call.write('\n'),
                call.write('Team 5 is:'),
                call.write('\n'),
                call.write('Brian Pedersen'),
                call.write('\n'),
                call.write('Jake Schnorr'),
                call.write('\n'),
                call.write('Megan Stucky'),
                call.write('\n'),
                call.write('James Thomas'),
                call.write('\n'),
                call.write('Nate Roberts'),
                call.write('\n'),
                call.write('John Shapiro'),
                call.write('\n'),
		call.write('Kelly Trujillo'),
                call.write('\n'),
            ]
        )
