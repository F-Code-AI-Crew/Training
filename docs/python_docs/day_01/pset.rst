Problem set
-------------

1. List operations
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: text
    
    .. literalinclude:: scripts/problem_set.py
    :language: python
    :start-after: # -- start list_operations --
    :end-before: # -- end list_operations --
    :linenos:

Input:

.. code-block:: python

    print(list_operations([30, 20, 50, 40, 10]))

Output:

.. code-block:: text

    {"first_number": 30, "last_number": 10, "reversed": [10, 40, 50, 20, 30], "sorted": [10, 20, 30, 40, 50]}

2. List manipulation
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: text
    
    .. literalinclude:: scripts/problem_set.py
    :language: python
    :start-after: # -- start modify_list --
    :end-before: # -- end modify_list --
    :linenos:

Input:

.. code-block:: python
    print(modify_list([10, 20, 30, 40, 50]))

Output:

.. code-block:: text

    [10, 20, "hello", 30, "lemon", "strawberry"]

3. Access 3D NumPy array
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: text
    
    .. literalinclude:: scripts/problem_set.py
    :language: python
    :start-after: # -- start access_3d_elements --
    :end-before: # -- end access_3d_elements --
    :linenos:

Input:

.. code-block:: python

    array_3D = [[[1, 2, 3], [4, 5, 6]],
                [[7, 8, 9], [10, 11, 12]]]
    access_3d_elements(array_3D)

Output:

.. code-block:: text

    {"first_2D": [[1, 2, 3],[4, 5, 6]], "last_row_first_2D": [4, 5, 6], "last_element_first_row_last_2D": 9}

4. Calculate the area of trapezoid
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: text
    
    .. literalinclude:: scripts/problem_set.py
    :language: python
    :start-after: # -- start calc_area_of_trapezoid --
    :end-before: # -- end calc_area_of_trapezoid --
    :linenos:

Input:

.. code-block:: python

    calc_area_of_trapezoid(8, 16, 12)

Output:

.. code-block:: text

    144.0