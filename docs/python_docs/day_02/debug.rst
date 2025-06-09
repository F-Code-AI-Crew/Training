Debugging
=========

In programming, **bugs** are errors that cause a program to behave incorrectly or crash. Debugging is the process of finding and fixing these bugs.

Types of Errors
---------------

1. **Syntax Errors**: Mistakes in code structure, detected before execution.

.. code-block:: python

    if x == 5
        print("Missing colon")

2. **Runtime Errors**: Errors that occur during execution (e.g., division by zero).

.. code-block:: python

    result = 10 / 0  # ZeroDivisionError

3. **Logical Errors**: The program runs but produces incorrect results due to flawed logic.

.. code-block:: python

    def average(a: int, b: int) -> float:
        return (a + b) / 3  # Incorrect formula


Using print for Debugging
-------------------------

A simple and common way to debug is to print the values of variables:

.. code-block:: python

    def greet(name: str) -> str:
        print(f"Debug: name = {name}")  # Debug print
        return f"Hello, {name}!"

    greet("Alice")


Using Debugger in IDEs
----------------------

Modern IDEs like **VSCode** and **PyCharm** provide powerful visual debuggers:

- **Breakpoints**: Pause execution at a specific line.
- **Step Into**: Move into a function call.
- **Step Over**: Execute the current line and move to the next.
- **Step Out**: Finish the current function and return to the caller.
- **Watch Window**: Monitor specific variables.
- **Call Stack**: View the sequence of function calls.


Using the pdb Module
--------------------

Python has a built-in debugger called ``pdb``:

.. code-block:: python

    import pdb

    def divide(a: int, b: int) -> float:
        pdb.set_trace()
        return a / b

    divide(10, 2)

When run, it opens an interactive prompt:

- `n`: next line  
- `c`: continue  
- `q`: quit  
- `p variable`: print variable's value  


Understanding Tracebacks
------------------------

When an exception occurs, Python provides a **traceback** — a detailed report of the call stack leading to the error.

.. code-block:: python

    def f1():
        return 10 / 0

    def f2():
        f1()

    f2()

The traceback will show the exact file, line number, and function call that caused the error.


Effective Debugging Techniques
------------------------------

- Reproduce the bug consistently.
- Use `print()` or logging to inspect variables.
- Minimize code to isolate the issue.
- Use a debugger (pdb or IDE).
- Read tracebacks carefully to locate the source.
- Check assumptions (types, values, ranges).

Additional Resources
--------------------

Check the official Python documentation on `pdb <https://docs.python.org/3/library/pdb.html>`_
