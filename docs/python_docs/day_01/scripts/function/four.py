# -- start add_four_nr --
def add_four_nr(a: int, b: int, c: int, d: int):
    result: int = a + b + c + d
    print(result)
# -- end add_four_nr --


# -- start complex_four_nr --
def complex_four_nr(a: int, b: int, c: int, d: int):
    result: float = (a * b) - (c / (d ** 2))
    print(result)
# -- end complex_four_nr --


# -- start complex_four --
def complex_four(a: int, b: int, c: int, d: int) -> float:
    result: float = (a * b) - (c / (d ** 2))
    return result
# -- end complex_four --


# -- start complex_four_wd --
def complex_four_wd(a: int, b: int, c: int, d: int) -> float:
    """
    Perform a composite arithmetic operation on four integers.

    This function calculates the result of the expression:
    (a * b) - (c / (d ** 2))

    :param a: The first integer operand, used in multiplication.
    :type a: int
    :param b: The second integer operand, used in multiplication.
    :type b: int
    :param c: The third integer operand, used as the dividend in division.
    :type c: int
    :param d: The fourth integer operand, squared and used as the divisor.
    :type d: int

    :return: The result of (a * b) - (c / (d ** 2))
    :rtype: float
    """
    result: float = (a * b) - (c / (d ** 2))
    return result
# -- end complex_four_wd --


def main():
    # -- start call complex_four_nr --
    print("Complex call 1")    
    complex_four_nr(3, 5, 7, 11)
    print("Complex call 2")
    complex_four_nr(67, 23, 44, 20)
    # -- end call complex_four_nr --

    # -- start call complex_four --
    complex_four_result: float = complex_four(67, 23, 44, 20)
    print("Result / 3.14 = ", complex_four_result / 3.14)
    # -- end call complex_four --



if __name__=="__main__":
    main()
