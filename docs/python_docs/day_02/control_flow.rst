Control Flow
------------

In Python, **control flow statements** allow you to direct the execution
of code depending on conditions. This is essential for creating logic in your programs.

Conditional Statements
~~~~~~~~~~~~~~~~~~~~~~

Python uses `if`, `elif`, and `else` to control the flow based on boolean conditions.

Syntax:

.. code-block:: python

    if condition1:
        # do something
    elif condition2:
        # do something else
    else:
        # do another thing

Example 1: Simple `if` statement

.. code-block:: python

    age: int = 20
    if age >= 18:
        print("You are an adult.")

Example 2: `if-elif-else` with comparison operators

.. code-block:: python

    score: int = 85

    if score >= 90:
        print("Grade: A")
    elif score >= 80:
        print("Grade: B")
    elif score >= 70:
        print("Grade: C")
    else:
        print("Grade: F")

Using Logical Operators
~~~~~~~~~~~~~~~~~~~~~~~

You can combine multiple conditions using logical operators:
- `and`: True if **both** conditions are true.
- `or`: True if **either** condition is true.
- `not`: Inverts the boolean value.

Example 3: Combining conditions

.. code-block:: python

    temperature: int = 25
    weather: str = "sunny"

    if temperature > 20 and weather == "sunny":
        print("Let's go for a picnic!")

Example 4: Using `not`

.. code-block:: python

    is_raining: bool = False

    if not is_raining:
        print("You don't need an umbrella.")

Nested If Statements
~~~~~~~~~~~~~~~~~~~~

Python allows you to nest `if` statements inside each other for more complex logic.

Example 5: Nested conditions

.. code-block:: python

    score: int = 88

    if score >= 80:
        if score >= 90:
            print("Excellent")
        else:
            print("Very Good")
    else:
        print("Needs Improvement")

Indentation is critical in nested ifs — each level must be indented correctly.

Extra Tips and Tools
~~~~~~~~~~~~~~~~~~~~~

- Use `input()` and `int()` or `float()` to build interactive programs:

.. code-block:: python

    age = int(input("Enter your age: "))
    if age < 18:
        print("Access denied.")

- Use `pass` if a block needs to be empty temporarily:

.. code-block:: python

    if age > 100:
        pass  # We'll handle this later

Explore more about Python control flow from the official guide:

`Python Control Flow Documentation <https://docs.python.org/3/tutorial/controlflow.html>`_


