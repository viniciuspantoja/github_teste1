from math import pi
from unittest import TestCase, main

from app import circles, squares


class PyramidTests(TestCase):

    def test_circle(self):
        # test cases where r >= 0
        self.assertEqual(circles(0), 0)
        self.assertEqual(circles(1), pi)
        self.assertEqual(circles(2), pi * (2 **2))

    def test_values(self):
        # Let's raise the error values where
        self.assertRaises(ValueError, circles, -2)
        self.assertRaises(ValueError, squares, 0)


    def test_squares(self):
        self.assertEqual(squares(1),1)
        self.assertEqual(squares(2),4)



if __name__ == "__main__":
    main()
