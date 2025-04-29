# -- start get second last --
def get_second_last(nums: list[float]) -> float:
    """
    Get the 2nd last element of the list after some modifications.

    Parameters
    ----------
    nums : list of float
        A list containing at least 3 real numbers.

    Returns
    -------
    float
        The second-to-last element after being increased by the average of the list,
        raised to the power of 2, and rounded to 2 decimal places.

    Examples
    --------
    >>> get_second_last([1.2, 3.4, 5.6, 7.8, 9.0])
    174.24

    Note
    ----
    - Average = (1.2+3.4+5.6+7.8+9.0)/5 = 5.4
    - 2nd last = 7.8
    - (7.8 + 5.4) = 13.2
    - 13.2 ** 2 = 174.24
    - round to 2 decimal places = 174.24
    """
    # Your code starts here
    result: float = float("-inf")
    # Your code ends here
    return result
# -- end get second last --


# -- start get first three ---
def get_first_three_reversed(nums: list[float]) -> list[float]:
    """
    Return the first three elements of the list in reverse order.

    Parameters
    ----------
    nums : list of float
        A list containing at least 3 real numbers.

    Returns
    -------
    list of float
        A new list containing the first three elements of `nums`, in reverse order.

    Examples
    --------
    >>> get_first_three_reversed([10.0, 20.0, 30.0, 40.0, 50.0])
    [30.0, 20.0, 10.0]

    Note
    ----
    - Start: [10.0, 20.0, 30.0, 40.0, 50.0]
    - Take the first three elements: [10.0, 20.0, 30.0]
    - Reverse those elements: [30.0, 20.0, 10.0]
    """
    # Your code starts here
    result: list[float] = []
    # Your code ends here
    return result
# -- end get first three ---


# -- start modify_list --
def modify_list(my_list: list) -> list:
    """
    Modify a list of elements by applying multiple list operations in sequence.

    Parameters
    ----------
    my_list : list
        A list containing at least five elements.

    Returns
    -------
    list
        The updated list after the following modifications:
        - Remove the last element of the list.
        - Insert the string "hello" at index 2.
        - Extend the list by adding two new elements: "lemon" and "strawberry" at the end.
        - Remove the element at index 4.
        - Insert the number 99 at the beginning of the list (index 0).

    Examples
    --------
    >>> modify_list([1, 2, 3, 4, 5, 6])
    [99, 1, 2, 'hello', 3, 5, 'lemon', 'strawberry']

    Note
    ----
    - Start: [1, 2, 3, 4, 5, 6]
    - Remove last element (6): [1, 2, 3, 4, 5]
    - Insert "hello" at index 2: [1, 2, 'hello', 3, 4, 5]
    - Extend with ["lemon", "strawberry"]: [1, 2, 'hello', 3, 4, 5, 'lemon', 'strawberry']
    - Remove element at index 4 (element 4): [1, 2, 'hello', 3, 5, 'lemon', 'strawberry']
    - Insert 99 at beginning: [99, 1, 2, 'hello', 3, 5, 'lemon', 'strawberry']
    """

    # Your code starts here
    result: list = []
    # Your code ends here
    return result
# -- end modify_list --


# -- start access_3d_elements --
def access_3d_elements(array_3d: list) -> dict:
    """
    Access specific elements from a 3D array.

    Parameters
    ----------
    array_3d: list
        A 3-dimensional array.

    Returns
    -------
    dict
        Selected elements from the 3D array.
        - The first 2D array.
        - The last row of the first 2D array.
        - The last element in the the first row of the last 2D array.

    Examples
    --------
    >>> access_3d_elements([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
    {"first_2D": [[1, 2, 3],[4, 5, 6]], "last_row_first_2D": [4, 5, 6], "last_element_first_row_last_2D": 9}

    Note
    ----
    - The first 2D array: [[1, 2, 3],[4, 5, 6]]
    - The last row of the first 2D array: [4, 5, 6]
    - The last element in the the first row of the last 2D array: 9
    """

    # Your code here
    return {
        "first_2D": None,
        "last_row_first_2D": None,
        "last_element_first_row_last_2D": None, 
    }
# -- end access_3d_elements --


# -- start calc_area_of_trapezoid --
def calc_area_of_trapezoid(a: int, b: int, h: int) -> float:
    """
    Calculate the area of trapezoid.

    Parameters
    ----------
    a: int 
        Length of base 1.
    b: int
        Length of base 2.
    h: int
        Height of trapezoid.

    Returns
    ----------
    float
        The area of trapezoid.

    Examples
    --------
    >>> calc_area_of_trapezoid(8, 16, 12)
    144.0

    Note
    ----
    - Area = ((8 + 16) / 2) * 12 = 144.0
    """

    # Your code here
    return 0.
# -- end calc_area_of_trapezoid --


def main():
    # Test your code here
    pass


if __name__== "__main__":
    main()
