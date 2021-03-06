from unittest import TestCase
from calculator import actions


class TestAdd(TestCase):
    def test_add(self):
        self.assertEqual(actions.add(3, 9), 12)

    def test_add_with_negative_numbers(self):
        self.assertEqual(actions.add(-53, 9), -44)


class TestMultiply(TestCase):
    def test_multiply(self):
        self.assertEqual(actions.multiply(3, 9), 27)

    def test_multiply_negative_numbers(self):
        self.assertEqual(actions.multiply(-5, 35), -175)
