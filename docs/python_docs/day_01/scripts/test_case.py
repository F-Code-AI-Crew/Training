import pytest
from problem_set import *
def test_get_second_last():
    assert get_second_last([1.2, 3.4, 5.6, 7.8, 9.0]) == 174.24
    assert get_second_last([2.999, 4.999, 6.999, 8.999, 10.999]) == 255.94
    assert get_second_last([10.05, 15.05, 20.05]) == 906.01
    assert get_second_last([-2.0, -1.0, 0.0, 1.0, 2.0]) == 1.0
    assert get_second_last([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]) == 1.69

def test_get_first_three_reversed():
    assert get_first_three_reversed([10.0, 20.0, 30.0, 40.0, 50.0]) == [30.0, 20.0, 10.0]
    assert get_first_three_reversed([2.999, 4.999, 6.999, 8.999, 10.999]) == [6.999, 4.999, 2.999]
    assert get_first_three_reversed([10.05, 15.05, 20.05]) == [20.05, 15.05, 10.05]
    assert get_first_three_reversed([-2.0, -1.0, 0.0, 1.0, 2.0]) == [0.0, -1.0, -2.0]
    assert get_first_three_reversed([0.0, 0.0, 0.0, 1.0]) == [0.0, 0.0, 0.0]

def test_modify_list():
    assert modify_list([1, 2, 3, 4, 5, 6]) == [99, 1, 2, 'hello', 3, 5, 'lemon', 'strawberry']
    assert modify_list([11, 22, 33, 44, 55, 66, 77, 88, 99]) == [99, 11, 22, "hello", 33, 55, 66, 77, 88, "lemon", "strawberry"]
    assert modify_list([-4.0, -3.0, -2.0, -1.0, 0.0, 1.0, 2.0, 3.0, 4.0]) == [99, -4.0, -3.0, "hello", -2.0, 0.0, 1.0, 2.0, 3.0, "lemon", "strawberry"]
    assert modify_list([9.9, 8.8, 7.7, 6.6, 5.5, 4.4]) == [99, 9.9, 8.8, 'hello', 7.7, 5.5, 'lemon', 'strawberry']
    assert modify_list([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.0]) == [99, 0.1, 0.2, 'hello', 0.3, 0.5, 0.6, 0.7, 0.8, 0.9, 'lemon', 'strawberry']

def test_access_3d_elements():
    assert access_3d_elements([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]]) == {"first_2D": [[1, 2, 3],[4, 5, 6]], "last_row_first_2D": [4, 5, 6], "last_element_first_row_last_2D": 9}
    assert access_3d_elements([[[1, 2, 3]]]) == {"first_2D": [[1, 2, 3]], "last_row_first_2D": [1, 2, 3], "last_element_first_row_last_2D": 3}
    assert access_3d_elements([[[1, 2], [3, 4], [5, 6]], [[7, 8], [9, 10], [11, 12]]]) == {"first_2D": [[1, 2], [3, 4], [5, 6]], "last_row_first_2D": [5, 6], "last_element_first_row_last_2D": 8}
    assert access_3d_elements([[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]) == {"first_2D": [[1, 2, 3]], "last_row_first_2D": [1, 2, 3], "last_element_first_row_last_2D": 9}
    assert access_3d_elements([[[1]],[[2]],[[3]]]) == {"first_2D": [[1]], "last_row_first_2D": [1], "last_element_first_row_last_2D": 3}

def test_calc_area_of_trapezoid():
    assert calc_area_of_trapezoid(8, 16, 12) == 144.0
    assert calc_area_of_trapezoid(10, 20, 5) == 75.0
    assert calc_area_of_trapezoid(7, 13, 3) == 30.0
    assert calc_area_of_trapezoid(12, 18, 7) == 105.0
    assert calc_area_of_trapezoid(6, 14, 2) == 20.0
