from unittest import TestCase
import core.arithmetics as arth


class ArithmeticsTest(TestCase):

    def test_add(self):
        expected = 8
        actual = arth.add(3, 5)
        self.assertEqual(expected, actual)
        # some edge cases:
        self.assertEqual(0, arth.add(0, 0))
        self.assertEqual(-5, arth.add(-2, -3))
        self.assertEqual(1, arth.add(-2, 3))

    def test_sub(self):
        # typical value:
        self.assertEqual(7, arth.sub(10, 3))
        # some edge case values
        self.assertEqual(0, arth.sub(0, 0))
        self.assertEqual(-1, arth.sub(-3, -2))
        self.assertEqual(5, arth.sub(3, -2))

    def test_mul(self):
        # typical value:
        self.assertEqual(30, arth.mul(10, 3))
        # some edge case values
        self.assertEqual(0, arth.mul(0, 0))
        self.assertEqual(6, arth.mul(-3, -2))
        self.assertEqual(-6, arth.mul(3, -2))

    def test_div(self):
        # typical value:
        self.assertEqual(25, arth.div(100, 4))
        # some edge case values
        self.assertEqual(5, arth.div(-10, -2))
        self.assertEqual(-5, arth.div(10, -2))

    def test_avg(self):
        self.assertEqual(5, arth.get_avg(4, 5, 6))
