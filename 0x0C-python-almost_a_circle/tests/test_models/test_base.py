#!/usr/bin/python3
"""
test_base module
"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """
    test class -> Base class
    """

    def test_0(self):
        """
        test 0
        """

        b1 = Base()
        self.assertEqual(b1.id, 1)

        b1 = Base()
        self.assertEqual(b1.id, 2)

        b1 = Base()
        self.assertEqual(b1.id, 3)

        b2 = Base(12)
        self.assertEqual(b2.id, 12)

        b3 = Base()
        self.assertEqual(b3.id, 4)

if __name__ == '__main__':
    unittest.main
