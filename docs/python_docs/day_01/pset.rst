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


Output:

.. code-block:: text


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


Output:

.. code-block:: text


3. Create and reshape NumPy array
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: text
    
    .. literalinclude:: scripts/problem_set.py
    :language: python
    :start-after: # -- start create_arrays --
    :end-before: # -- end create_arrays --
    :linenos:

Input:

.. code-block:: python

    arrays = create_arrays()
    print("Arrays:", arrays)

Output:

.. code-block:: text


4. Access 3D NumPy array
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: text
    
    .. literalinclude:: scripts/problem_set.py
    :language: python
    :start-after: # -- start access_3d_elements --
    :end-before: # -- end access_3d_elements --
    :linenos:

Input:

.. code-block:: python

    array_3D = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
                [[10, 25, 6], [7, 8, 29], [15, 11, 52]],
                [[82, 56, 100], [22, 24, 5], [99, 46, 12]],
            ]
    access_3d_elements(array_3D)

Output:

.. code-block:: text

    first_2D: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    second_row_first_2D: [4, 5, 6]
    last_element_first_row_last_2D: 100

5. Calculate the area of trapezoid
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

    144
