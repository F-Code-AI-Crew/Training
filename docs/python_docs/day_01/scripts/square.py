def square(x: int) -> int:
    """
    Square a number.

    :param x: Input number.
    :type x: int
    :return: x square
    :rtype: int
    """
    
    result: int = x * x;

    return result


num: int = 10
num_squared: int = square(num)
print(num_squared)
