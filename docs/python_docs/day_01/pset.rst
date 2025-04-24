Problem set
-------------

1. List operations
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python
    
    def list_operations(fruits: list) -> dict:
        """
        Perform operations on a list of fruits.

        Parameters:
            fruits (list): A list of fruit names.

        Returns:
            dict: Results of various operations on the list.
            - The entire list
            - The first fruit
            - The last fruit
            - The middle three fruits
            - The list in reverse order using slicing
            - The sorted list
        """
        
        # Your code here
        return = {
            "full_list":  ,
            "first_fruit":  ,
            "last_fruit":  ,
            "middle_three":  ,
            "reversed":  ,
            "sorted":
        }


    # Test case
    fruits = ['apple', 'cherry', 'orange', 'elderberry', 'banana']
    print("List Operations:", list_operations(fruits))

2. List manipulation
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    def modify_list(fruits: list) -> dict:
        """
        Modify a list of fruits with common list operations.

        Parameters:
            fruits (list): A list of fruit names.

        Returns:
            dict: The list after each modification step.
            - Add 'lemon' to the list
            - Insert 'strawberry' to the second index
            - Remove one fruit from the list
            - Delete one fruit from the fourth index
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

    
    # Test case
    fruits = ['apple', 'cherry', 'orange', 'elderberry', 'banana']
    print("Modified Lists:", modify_list(fruits))

3. NumPy Exercises – Array Dimensions
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    import numpy as np

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

    def access_3d_elements(array_3d: np.ndarray) -> dict:
        """
        Access specific elements from a 3D NumPy array.

        Parameters:
            array_3d (np.ndarray): A 3-dimensional NumPy array.

        Returns:
            dict: Selected elements from the 3D array.
            - The first 2D array
            - The second row of the first 2D array
            - The last element in the last 2D array
        """

        # Your code here
        return {
            "first_2D":  ,
            "second_row_first_2D":  ,
            "last_element_last_2D": 
        }


    # Test case
    arrays = create_arrays()
    print("Arrays:", arrays)
    print("Accessed 3D Elements:", access_3d_elements(arrays["3D"]))


4. Arithmetic operations
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    def calculate(a: int, b: int) -> dict:
        """
        Perform arithmetic operations of two numbers.

        Parameters:
            a (int): First number.
            b (int): Second number.

        Returns:
            dict: Results of addition, subtraction, multiplication, float division, and integer division.
        """

        # Your code here
        return {
            "add": ,
            "subtract":  ,
            "multiply":  ,
            "float_divide":  ,
            "int_divide":
        } 

    
    # Test case
    print("Calculation:", calculate(10, 3))
