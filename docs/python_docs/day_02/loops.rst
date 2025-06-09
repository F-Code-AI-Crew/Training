Loops
=====

Loops in Python allow you to execute a block of code repeatedly, either a known number of times or until a condition is met.

For Loop
~~~~~~~~

The `for` loop iterates over an **iterable** (like a list, tuple, string, range, or dictionary).

Syntax:

.. code-block:: python

    for item in iterable:
        # do something with item

Looping through common iterables:

.. code-block:: python

    # List
    for fruit: str in ["apple", "banana", "cherry"]:
        print(fruit)

    # Tuple
    for coord: int in (0, 1, 2):
        print(coord)

    # String
    for char:str in "hello":
        print(char)

    # range()
    for i in range(5):
        print(i)  # 0, 1, 2, 3, 4

    # Dictionary
    ages: dict[str, int] = {"Alice": 30, "Bob": 25}
    
    # iterates over keys
    for name in ages:
        print(name, ages[name])
    
    # or using items() to get key-value pairs
    for name, age in ages.items():
        print(name, age)

Break and Continue
~~~~~~~~~~~~~~~~~~

- `break` exits the loop immediately.
- `continue` skips to the next iteration.

.. code-block:: python

    for i: int in range(10):
        if i == 5:
            break       # stops the loop when i == 5
        if i % 2 == 0:
            continue    # skips even numbers
        print(i)        # prints 1, 3

For Loop with Else
~~~~~~~~~~~~~~~~~~

The `else` block runs **only if** the loop completes without encountering `break`.

.. code-block:: python

    for i: int in range(3):
        print(i)
    else:
        print("Done without break")

List Comprehension
~~~~~~~~~~~~~~~~~~

A concise way to build lists from iterables.

Syntax:

.. code-block:: python

    [ expression for item in iterable if condition ]

Example:

.. code-block:: python

    squares: list[int] = [x*x for x in range(6)]      # [0, 1, 4, 9, 16, 25]
    evens: list[int]  = [x for x in range(10) if x%2==0]  # [0, 2, 4, 6, 8]

While Loop
~~~~~~~~~~

Repeats a block **while** a condition is `True`.

Syntax:

.. code-block:: python

    while condition:
        # do something

Loop termination condition: when `condition` becomes `False`.

.. code-block:: python

    count: int = 3
    while count > 0:
        print(count)
        count -= 1

Break and Continue in While
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    n: int = 0
    while True:
        n += 1
        if n == 3:
            continue    # skip printing 3
        if n > 5:
            break       # exit when n > 5
        print(n)        # prints 1, 2, 4, 5

While Loop with Else
~~~~~~~~~~~~~~~~~~~~

`else` executes if the loop terminates **without** `break`:

.. code-block:: python

    i: int = 0
    while i < 3:
        print(i)
        i += 1
    else:
        print("Finished cleanly")

Nested Loops
~~~~~~~~~~~~

You can place loops inside loops for multi-dimensional iteration:

.. code-block:: python

    for i: int in range(3):
        for j: int in range(2):
            print(f"i={i}, j={j}")

Applications of Loops
~~~~~~~~~~~~~~~~~~~~~

- **Iterating lists**:

  .. code-block:: python

      names: list[str] = ["Anna", "Ben", "Cara"]
      for name: str in names:
          print(name.upper())

- **Calculating sum**:

  .. code-block:: python

      total: int = 0
      for num: int in [1, 2, 3, 4]:
          total += num
      print(total)  # 10

- **Searching**:

  .. code-block:: python

      target: int = 7
      found: bool = False
      for x: int in range(10):
          if x == target:
              found = True
              break
      print("Found!" if found else "Not found")

- **Processing strings**:

  .. code-block:: python

      text: str = "Hello World"
      vowels: list[str] = [ch for ch in text if ch.lower() in "aeiou"]
      print(vowels)  # ['e', 'o', 'o']

Additional Resources
~~~~~~~~~~~~~~~~~~~~

- Official Python docs on loops:  
  https://docs.python.org/3/tutorial/controlflow.html#for  
  https://docs.python.org/3/tutorial/controlflow.html#while  
