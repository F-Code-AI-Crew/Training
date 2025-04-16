Variable
----------

Create a variable in python

.. code-block:: python

    var_name = value
    num = 10
    name = "F-Code"

To show a value or the contents of a variable in the console, 
use the ``print`` function:

.. code-block:: python

    print(num)
    print(name)

When naming a variable in Python, keep these rules in mind:

* Must start with a letter or the underscore character
* Cannot start with a number
* Can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
* Case sensitive
* Cannot be any of the Python keywords

.. tip::
    Naming convention - `PEP8 <https://peps.python.org/pep-0008/#function-and-variable-names>`_

    * Function names should be lowercase, with words separated by underscores as necessary to improve readability.
    * Variable names follow the same convention as function names.

Operation
----------

Python provides a range of built-in operators that let you 
perform calculations and comparisons directly with your data. 
These operators work with numbers, variables, and expressions 
to build more complex logic. In this section, we'll explore 
two main groups of operators:

* Arithmetic operators - used for performing mathematical operations like addition and division.

* Comparison operators - used to compare values and return True or False.

Understanding how these operators behave is essential to writing effective and accurate Python code.



Arithmetic
~~~~~~~~~~

.. list-table::
    :widths: 20 60
    :header-rows: 1

    * - Operator
      - Name
    * - ``+``
      - Addition
    * - ``-``
      - Subtraction
    * - ``*``
      - Multiplication
    * - ``/``
      - Division
    * - ``**``
      - Power
    * - ``%``
      - Remainder

Comparison
~~~~~~~~~~~

.. list-table::
    :widths: 20 60
    :header-rows: 1

    * - Operator
      - Name
    * - ``==``
      - Equal
    * - ``!=``
      - Not equal
    * - ``>``
      - Greater than
    * - ``<``
      - Less than
    * - ``>=``
      - Greater than or equal to
    * - ``<=``
      - Less than or equal to

.. note::
    Python is both 

  * Strongly typed: No implicit conversions e.g. **str** to **int**
  * Dynamically typed: variables don't have fixed types, but values do; Types are implied in the run-time

Not like C, this could give you a faster prototyping, especially during 
brainstorming, because you don't really need to declare the type of 
a variable e.g. you could simply write  ``num = 10`` without saying
it's an integer.

This flexibility speeds up writing code early on, but it comes with trade-offs:
as your codebase grows much larger and involves collaboration, 
**lack of explicit type can make it harder to read, debug, and maintain**. 
Being clear about the types can make teamwork and long-term development much easier. 
This could be achieved by:

* Type hint w/ IDE support
* Informative comments & documentation

Data types
~~~~~~~~~~~

Python has a variety of built-in data types, grouped into the 
following categories:

.. list-table::
   :header-rows: 1
   :widths: 20 60

   * - Category
     - Types
   * - Text Type
     - ``str``
   * - Numeric Types
     - ``int``, ``float``, ``complex``
   * - Sequence Types
     - ``list``, ``tuple``, ``range``
   * - Mapping Type
     - ``dict``
   * - Set Types
     - ``set``, ``frozenset``
   * - Boolean Type
     - ``bool``
   * - Binary Types
     - ``bytes``, ``bytearray``, ``memoryview``

To add type (type hint) when declaring a variable using this 
format: 

.. code-block:: python

    x: int = 10
    pi_number: float = 3.14
    name: str = "F-Code"


.. Note::
   Does this force your variable to always be that type?

   **Short answer:** No. Type hints are just *hints* - 
   Python won't enforce them at runtime. Then why make a fuss?

  Using clear and descriptive variable names can often eliminate 
  the need for extra documentation, combining good naming with 
  type hints makes your code even more robust and self-explanatory.