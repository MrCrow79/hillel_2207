import unittest


import sys
import pathlib
# print(str(pathlib.Path(__file__)))  # path to current file
# print(str(pathlib.Path(__file__).parent.parent))  # path to 2 folder up
# print(sys.path)
sys.path.insert(0, str(pathlib.Path(__file__).parent.parent)) # add path of project to system paths


from assertation_utils import compare_numbers_with_delta


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


class TestMy(unittest.TestCase):  # наслідування

    def test_factorial_simple(self):
        result = factorial(5)
        #
        # raise ValueError('My value error')
        # assert result == 121, 'Somthing happens'  # (result == 121) return Bool
        # my_list = [1, 2, 3]
        #
        # assert True
        # assert False
        # assert my_list # assert bool(my_list)
        # # assert False -> raise AssertationError('Somthing happens')
        # # assert True -> does None

        expected_result = 121

        assert result == expected_result, f'expected {expected_result} but we have {result}'
        self.assertEqual(121, result)  # assert 121 == result

    def test_factoial_almost_equal(self):
        result = factorial(5)

        expected_result = 100

        self.assertAlmostEquals(expected_result, result, delta=10)

    def test_factoial_almost_equal_custom_assert(self):
        result = factorial(5)

        expected_result = 100

        compare_numbers_with_delta(result, expected_result, delta=20)

    def test_example_comparing_list_of_dicts(self):

        expected = [
            {'id': 10,
             'name': 'Alex'},
            {'id': 11,
             'name': 'Alex'},
            {'id': 12,
             'name': 'Alex'},
            {'id': 14,
             'name': 'Alex'},
            {'id': 15,
             'name': 'Alex'},
        ]

        actual = [
            {'id': 10,
             'name': 'Alex'},
            {'id': 11,
             'name': 'Alex'},
            {'id': 12,
             'name': 'Alex'},
            {'id': 13,
             'name': 'Alex'},
            {'id': 15,
             'name': 'Alex'},
        ]

        self.assertEqual(expected, actual)


    def test_example_crate_user(self):

        result = api_call.create_user()  # повертає респонс з сервера dict з {'id': 10, 'User_name': 'Ivan'}


        self.assertEqual(result.status_code, 201)
        self.assertEqual(result.json()['User_name'], 'Ivan')


if __name__ == '__main__':  # буде виконано в випадку запуску цього файла на виконання
    unittest.main(verbosity=2)  # буде збирати і запускати всі тести
    unittest.main(verbosity=2)  # verbosity == console command -v
