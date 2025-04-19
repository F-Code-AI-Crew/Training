Function
------------

Functions: reusable blocks of code that perform specific tasks.

Define a function
~~~~~~~~~~~~~~~~~~~~~~~~~~

Python function syntax:

.. code-block:: python

    def function_name():
        # Function body

.. tip::

    (1 more time) Naming convention - `PEP8 <https://peps.python.org/pep-0008/#function-and-variable-names>`_

    * Function names should be lowercase, with words separated by underscores as necessary to improve readability.
    * Variable names follow the same convention as function names.

Example

.. literalinclude:: scripts/function/simple.py
    :language: python
    :start-after: # -- start func_simple --
    :end-before: # -- end func_simple --
    :linenos:


Call a function
~~~~~~~~~~~~~~~~

To call a function, use the function name followed by parentheses e.g. ``function_name()``.

Example:

.. literalinclude:: scripts/function/simple.py
    :language: python
    :start-after: # -- start call func_simple --
    :end-before: # -- start call func_simple --
    :linenos:


Output:

.. code-block:: text

    Day 1
    Wake up
    Learn Python
    Code
    Python is fast
    Don't understand Python
    Eat
    Sleep
    Day 2
    Wake up
    Learn Python
    Code
    Python is fast
    Don't understand Python
    Eat
    Sleep
    ...


Parameters
~~~~~~~~~~~

Parameters enhance the reusability of a function in computation, modularizing code, etc.

.. literalinclude:: scripts/function/four.py
   :language: python
   :start-after: # -- start add_four_nr --
   :end-before: # -- end add_four_nr --
   :linenos:

Do things a bit more complex

.. literalinclude:: scripts/function/four.py
   :language: python
   :start-after: # -- start complex_four_nr --
   :end-before: # -- end complex_four_nr --
   :linenos:


Return
~~~~~~~

A function can also return a result that can be stored or used elsewhere in your program, instead of just
printing the result out to the console

.. literalinclude:: scripts/function/four.py
   :language: python
   :start-after: # -- start complex_four --
   :end-before: # -- end complex_four --
   :linenos:


Now the result of ``complex_four`` could be stored in a variable, used in other computation.

.. literalinclude:: scripts/function/four.py
   :language: python
   :start-after: # -- start call complex_four --
   :end-before: # -- end call complex_four --
   :linenos:


Scope
~~~~~~

Python follows the **LEGB rules** for scope. Today let's focus on **L** and **G** rule, which is super close to
C rules for scoping.

In short

* **L** - Local: Accessible in a code block, function 
* **G** - Global: Accessible in the program, script, and module

Docstring
-----------

A docstring (short for documentation string) is a special kind of string used to describe what a function, 
class, or module does. It's placed right after the ``def`` or ``class`` line and is enclosed in triple 
quotes (""" or ''').

Python reads this string at runtime, which means tools like IDEs, linters, and documentation generators 
(like Sphinx) can access it to help users understand your code more easily.

.. literalinclude:: scripts/function/four.py
   :language: python
   :start-after: # -- start complex_four_wd --
   :end-before: # -- end complex_four_wd --
   :linenos:

Docstrings can also be leveraged to automatically generate documentation using tools like Sphinx, MkDocs, 
and others. 

By including the following directive in your ``.rst`` file (restructuredtext file extension), Sphinx will 
automatically locate the function and generate nicely formatted documentation based on its docstring:

.. code-block:: restructuredtext

    .. autofunction:: function.four.complex_four_wd

The resulting documentation might look like this:

.. autofunction:: function.four.complex_four_wd


.. note::
    Being clear about the types can make teamwork and long-term development much easier. 
    This could be achieved by:

    * Type hint w/ IDE support
    * Informative comments & documentation
