import nose
import unittest

from color import color


class ColorTest(unittest.TestCase):

    def test_red(self):

        got = color.red('hi')
        expected = '\x1b[;31mhi\x1b[0m'

        self.assertEqual(got, expected)
