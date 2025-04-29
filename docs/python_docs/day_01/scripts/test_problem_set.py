import pytest
from .problem_set import *


def test_get_second_last():
    test_1_input = [1.2, 3.4, 5.6, 7.8, 9.0]
    test_1_output = 174.24
    assert get_second_last(test_1_input) == test_1_output

    test_2_input = [2.999, 4.999, 6.999, 8.999, 10.999]
    test_2_output = 255.94
    assert get_second_last(test_2_input) == test_2_output

    test_3_input = [10.05, 15.05, 20.05]
    test_3_output = 906.01
    assert get_second_last(test_3_input) == test_3_output

    test_4_input = [-2.0, -1.0, 0.0, 1.0, 2.0]
    test_4_output = 1.0
    assert get_second_last(test_4_input) == test_4_output

    test_5_input = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
    test_5_output = 1.69
    assert get_second_last(test_5_input) == test_5_output


def test_get_first_three_reversed():
    test_1_input = [10.0, 20.0, 30.0, 40.0, 50.0]
    test_1_output = [30.0, 20.0, 10.0]
    assert get_first_three_reversed(test_1_input) == test_1_output

    test_2_input = [2.999, 4.999, 6.999, 8.999, 10.999]
    test_2_output = [6.999, 4.999, 2.999]
    assert get_first_three_reversed(test_2_input) == test_2_output

    test_3_input = [10.05, 15.05, 20.05]
    test_3_output = [20.05, 15.05, 10.05]
    assert get_first_three_reversed(test_3_input) == test_3_output

    test_4_input = [-2.0, -1.0, 0.0, 1.0, 2.0]
    test_4_output = [0.0, -1.0, -2.0]
    assert get_first_three_reversed(test_4_input) == test_4_output

    test_5_input = [0.0, 0.0, 0.0, 1.0]
    test_5_output = [0.0, 0.0, 0.0]
    assert get_first_three_reversed(test_5_input) == test_5_output


def test_modify_list():
    test_1_input = [1, 2, 3, 4, 5, 6]
    test_1_output = [99, 1, 2, 'hello', 3, 5, 'lemon', 'strawberry']
    assert modify_list(test_1_input) == test_1_output

    test_2_input = [11, 22, 33, 44, 55, 66, 77, 88, 99]
    test_2_output = [99, 11, 22, "hello", 33, 55, 66, 77, 88, "lemon", "strawberry"]
    assert modify_list(test_2_input) == test_2_output

    test_3_input = [-4.0, -3.0, -2.0, -1.0, 0.0, 1.0, 2.0, 3.0, 4.0]
    test_3_output = [99, -4.0, -3.0, "hello", -2.0, 0.0, 1.0, 2.0, 3.0, "lemon", "strawberry"]
    assert modify_list(test_3_input) == test_3_output

    test_4_input = [9.9, 8.8, 7.7, 6.6, 5.5, 4.4]
    test_4_output = [99, 9.9, 8.8, 'hello', 7.7, 5.5, 'lemon', 'strawberry']
    assert modify_list(test_4_input) == test_4_output

    test_5_input = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.0]
    test_5_output = [99, 0.1, 0.2, 'hello', 0.3, 0.5, 0.6, 0.7, 0.8, 0.9, 'lemon', 'strawberry']
    assert modify_list(test_5_input) == test_5_output


def test_access_3d_elements():
    test_1_input = [[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]]
    test_1_output = {"first_2D": [[1, 2, 3], [4, 5, 6]], "last_row_first_2D": [4, 5, 6], "last_element_first_row_last_2D": 9}
    assert access_3d_elements(test_1_input) == test_1_output

    test_2_input = [[[1, 2, 3]]]
    test_2_output = {"first_2D": [[1, 2, 3]], "last_row_first_2D": [1, 2, 3], "last_element_first_row_last_2D": 3}
    assert access_3d_elements(test_2_input) == test_2_output

    test_3_input = [[[1, 2], [3, 4], [5, 6]], [[7, 8], [9, 10], [11, 12]]]
    test_3_output = {"first_2D": [[1, 2], [3, 4], [5, 6]], "last_row_first_2D": [5, 6], "last_element_first_row_last_2D": 8}
    assert access_3d_elements(test_3_input) == test_3_output

    test_4_input = [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
    test_4_output = {"first_2D": [[1, 2, 3]], "last_row_first_2D": [1, 2, 3], "last_element_first_row_last_2D": 9}
    assert access_3d_elements(test_4_input) == test_4_output

    test_5_input = [[[1]], [[2]], [[3]]]
    test_5_output = {"first_2D": [[1]], "last_row_first_2D": [1], "last_element_first_row_last_2D": 3}
    assert access_3d_elements(test_5_input) == test_5_output


def test_calc_area_of_trapezoid():
    test_1_input = (8, 16, 12)
    test_1_output = 144.0
    assert calc_area_of_trapezoid(*test_1_input) == test_1_output

    test_2_input = (10, 20, 5)
    test_2_output = 75.0
    assert calc_area_of_trapezoid(*test_2_input) == test_2_output

    test_3_input = (7, 13, 3)
    test_3_output = 30.0
    assert calc_area_of_trapezoid(*test_3_input) == test_3_output

    test_4_input = (12, 18, 7)
    test_4_output = 105.0
    assert calc_area_of_trapezoid(*test_4_input) == test_4_output

    test_5_input = (6, 14, 2)
    test_5_output = 20.0
    assert calc_area_of_trapezoid(*test_5_input) == test_5_output
