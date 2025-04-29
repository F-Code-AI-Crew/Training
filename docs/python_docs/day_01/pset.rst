Problem set
-------------

Get second last
~~~~~~~~~~~~~~~~

.. autofunction:: problem_set.get_second_last

Get first three reversed
~~~~~~~~~~~~~~~~~~~~~~~~~

.. autofunction:: problem_set.get_first_three_reversed

Modify list
~~~~~~~~~~~

.. autofunction:: problem_set.modify_list


Access 3D NumPy array
~~~~~~~~~~~~~~~~~~~~~~~~~

.. literalinclude:: scripts/problem_set.py
    :language: python
    :start-after: # -- start access_3d_elements --
    :end-before: # -- end access_3d_elements --
    :linenos:

Input:

.. code-block:: python

    array_3D = [[[1, 2, 3], [4, 5, 6]],
                [[7, 8, 9], [10, 11, 12]]]
    print(access_3d_elements(array_3D))

Output:

.. code-block:: text

    {"first_2D": [[1, 2, 3],[4, 5, 6]], "last_row_first_2D": [4, 5, 6], "last_element_first_row_last_2D": 9}

Calculate the area of trapezoid
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: text
    
    .. literalinclude:: scripts/problem_set.py
    :language: python
    :start-after: # -- start calc_area_of_trapezoid --
    :end-before: # -- end calc_area_of_trapezoid --
    :linenos:

Input:

.. code-block:: python

    print(calc_area_of_trapezoid(8, 16, 12))

Output:

.. code-block:: text

    144.0
