from functions_helper import is_anagram
import unittest


class TestIsAnagramNegative(unittest.TestCase):

    def test_is_anagram_int_input_bad_option(self):

        is_error_was_catch = False

        try:

            is_anagram('World', 5)

        except TypeError:
            is_error_was_catch = True

        assert is_error_was_catch, 'There was no error TypeError'

    def test_is_anagram_int_input(self):

        with self.assertRaises(TypeError):
            is_anagram('World', 5)

        with self.assertRaises(TypeError):  # очікує TypeError в коді який нижче під with
            is_anagram('World', 'asd')

    def test_is_anagram_int_input_without_error(self):

        with self.assertRaises(TypeError):  # очікує TypeError в коді який нижче під with
            is_anagram('World', 'asd')


    def test_is_anagram_int_input_wrong_error(self):
        with self.assertRaises(ValueError):
            is_anagram('World', 5)
