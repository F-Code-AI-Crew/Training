import numpy as np

# -- start list_operations --
def list_operations(my_list: list) -> dict:
    """
    Perform operations on a list of fruits.

    Parameters:
        my_list (list): A list of numbers with minimum three elements.

    Returns:
        dict: Results of various operations on the list.
        - The first number of the list
        - The last number of the list
        - The list in reverse order using slicing
        - The sorted list
    """   
    # Your code here
    return {
        "full_list":  ,
        "first_fruit":  ,
        "last_fruit":  ,
        "middle_three":  ,
        "reversed":  ,
        "sorted":
        }
# -- end list_operations --


# -- start modify_list --
def modify_list(my_list: list) -> dict:
    """
    Modify a list of fruits with common list operations.

    Parameters:
        my_list (list): A list of numbers with minimum five elements.

    Returns:
        dict: The new lists after each modification.
        - Add 'lemon' to the end of my_list
        - Insert 'strawberry' to index 2 of my_list
        - Delete one fruit index 4 of my_list
        - Remove one fruit from the end of my_list
    """
    # Your code here
    added = 
    inserted =
    removed = 
    del_indexed =

    return { 
        "added": added,
        "inserted": inserted,
        "removed": removed,
         "del_indexed": del_indexed,
    }
# -- end modify_list --


# -- start create_arrays --
def create_arrays() -> dict:
    """
    Create a 1D NumPy array with numbers from 1 to 12 and reshape the array into 2D and 3D forms.
        
    Returns:
        dict: Contains 1D array, 2D array of shape (3,4), and 3D array of shape (2,2,3).
    """
    # Your code here
    array_1d = 
    array_2d = 
    array_3d = 

    return {
    "1D": array_1d,
    "2D": array_2d,
    "3D": array_3d
    }
# -- end create_arrays --


# -- start access_3d_elements --
def access_3d_elements(array_3d: np.ndarray) -> dict:
    """
    Access specific elements from a 3D NumPy array.

    Parameters:
        array_3d (np.ndarray): A 3-dimensional NumPy array.

    Returns:
        dict: Selected elements from the 3D array.
        - The first 2D array
        - The second row of the first 2D array
        - The last element in the the first row of the last 2D array
    """
    # Your code here
    return {
        "first_2D":  ,
        "second_row_first_2D":  ,
        "last_element_first_row_last_2D": 
    }
# -- end access_3d_elements --


# -- start calc_area_of_trapezoid --
def calc_area_of_trapezoid(a: int, b: int, h: int) -> float:
    """
    Calculate the area of trapezoid.

    Parameters:
        a (int): Length of base 1.
        b (int): Length of base 2.
        h (int): Height of the trapezoid.

    Returns:
        float: Area of trapezoid
    """
    # Your code here
    pass
# -- end calc_area_of_trapezoid --


def main():
    # Test your code here
    pass


if __name__=="_main_":
    main()
