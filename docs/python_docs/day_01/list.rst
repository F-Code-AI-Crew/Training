====
List
====

Python `List` functions like an array, with much more power 
and flexibility like holding multiple types of variables, 
dynamic allocation, etc. Lists could be created using square
brackets:

.. code-block:: python

    [1, 2, 3]
    ["Code", "the", "dream"]
    [1, "one", 2, "two", 3, "three"]


---------------
List operations
---------------

1. Access and update by index

.. code-block:: python

    fruits = ["apple", "banana", "cherry"]
    #                      ^
    #            0         1         2
    
``fruits[1]`` will return the value at the index `1` - the 
string "banana".

In Python, you could access the trailing element using negative 
index e.g. to get ``cherry``, use ``fruits[-1]``

.. code-block:: python

    fruits = ["apple", "banana", "cherry"]
    #                                ^
    #           -3        -2        -1


2. Insert

The ``list.append`` method adds an item to the end of the list:

.. code-block:: python

    fruits = ["apple", "banana", "cherry"]
    fruits.append("mango")

The ``list.insert`` method insert an item to the given index

.. code-block:: python

    fruits.insert(1, "watermelon")

3. Remove

You can remove items from a list using several methods:

- ``list.remove(value)``  removes the **first matching** value:

.. code-block:: python

    fruits = ["apple", "banana", "cherry"]
    fruits.remove("banana")

- ``list.pop(index)`` removes and returns the item at the given index (default is the last item):

.. code-block:: python

    fruits.pop()  # Removes "cherry"
    fruits.pop(0)  # Removes "apple"

- ``del``  deletes an item by index:

.. code-block:: python

    del fruits[1]  # Deletes apple

- ``list.clear`` method empties the list

4. List slicing

List slicing allows you to extract a **portion** (or "slice") 
of a list using the `start:stop:step` syntax.

.. code-block:: python

    numbers: list[int] = [10, 20, 30, 40, 50]
    slice_1: list[int] = numbers[1:4]  # [20, 30, 40]


---------------------
More list operations?
---------------------

Python provides a **comprehensive set of methods** for working 
with lists, documented in the official `List API documentation <https://docs.python.org/3/tutorial/datastructures.html#more-on-lists>`_

You can also access documentation **offline** using the built-in 
`pydoc` tool, or through **code editors and IDEs** that provide 
inline docs using the Python source code & LSP.

.. code-block:: shell

    python -m pydoc list.append

    Help on method_descriptor in list:

    list.append = append(self, object, /) unbound builtins.list method
        Append object to the end of the list.

You'll explore **more list operations and methods** through hands-on 
**problem sets**.
