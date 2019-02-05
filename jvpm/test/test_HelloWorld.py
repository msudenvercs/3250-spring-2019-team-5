import unittest
import jvpm.HelloWorld
from unittest.mock import patch, call

class TestHelloWorld(unittest.TestCase):
    @patch('builtins.print')
    def test_HelloWorld(self, mock_patch):
        jvpm.HelloWorld.HelloWorld()
        self.assertEqual(mock_patch.mock_calls, [
            call.write('Hello world'),
            call.write('Team 5 is:'),
            call.write('Brian Pedersen'),
            call.write('Jake Schnorr'),
            call.write('Megan Stucky'),
            call.write('James Thomas'),
            call.write('Nate Roberts'),
            call.write('John Shapiro'),
            call.write('Kelly Trujillo'),
        ])
