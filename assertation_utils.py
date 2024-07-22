def compare_numbers_with_delta(number1, number2, delta=0, msg=None):
    """

    :param number1: int | float
    :param number2:  int | float
    :param delta: int
    """
    if not msg:
        msg = f'Expected {number2} between {number1 - delta} and {number1 + delta}'
    assert number1 - delta <= number2 <= number1 + delta, msg


if __name__ == '__main__':
    print('file assert utils ')