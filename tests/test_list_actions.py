from unittest import TestCase
from calculator import list_actions


class TestListAdd(TestCase):
    def test_list_add(self):
        self.assertEqual(list_actions.add([1, 2, 3]), 6)

    def test_list_add_with_negative_numbers(self):
        self.assertEqual(list_actions.add([-11, 2, 3]), -6)


class TestListMultiply(TestCase):
    def test_list_multiply(self):
        self.assertEqual(list_actions.multiply([1, 2, 3, 4]), 24)

    def test_list_multiply_negative_numbers(self):
        self.assertEqual(list_actions.multiply([1, 2, 3, -4]), -24)
