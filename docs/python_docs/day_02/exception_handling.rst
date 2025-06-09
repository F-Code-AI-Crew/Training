Exception Handling
==================

Python provides a robust mechanism for **handling runtime errors** (exceptions) so that programs can recover, clean up resources, or fail gracefully instead of crashing.

Introduction to Exceptions
~~~~~~~~~~~~~~~~~~~~~~~~~~

Exceptions are errors that occur during execution and interrupt normal program flow.

**Common types of exceptions:**

- `TypeError` – Operation applied to an inappropriate type.

  .. code-block:: python

      x = "10" + 5  # TypeError

- `ValueError` – Correct type, but inappropriate value.

  .. code-block:: python

      int("hello")  # ValueError

- `IndexError` – Index out of range in a list or sequence.

  .. code-block:: python

      [1, 2, 3][5]  # IndexError

- `KeyError` – Dictionary key not found.

  .. code-block:: python

      {"name": "Alex"}["age"]  # KeyError

- `FileNotFoundError` – Trying to open a non‑existent file.

  .. code-block:: python

      open("missing.txt")  # FileNotFoundError


Why handle exceptions?
~~~~~~~~~~~~~~~~~~~~~~

- **Prevent crashes** and display user‑friendly error messages.  
- **Allow fallback or recovery** for expected errors (e.g. network failure, missing input).  
- **Clean up resources** (files, network connections, database connections) reliably.

**Common practices for exception handling:**

1. **Catch specific exceptions first**  
   Handle each known error type separately to provide tailored recovery or messaging.

2. **Group related exceptions**  
   If multiple exceptions share the same handling logic, catch them together:

   .. code-block:: python

       except (FileNotFoundError, PermissionError) as e:
           log_error(e)
           print("Cannot access file.")

3. **Use a general fallback**  
   After all specific handlers, add `except Exception as e:` to catch any unexpected errors.  
   Typically log or re‑raise this exception so developers notice:

   .. code-block:: python

       except Exception as e:
           log_traceback(e)
           raise

4. **Use `else` for success logic**  
   Code in `else` runs only if no exception occurred, keeping success and error branches separate.

The try…except Structure
~~~~~~~~~~~~~~~~~~~~~~~~

Basic syntax:

.. code-block:: python

    try:
        # risky code
    except SomeException:
        # handler code

Catch a specific exception:

.. code-block:: python

    try:
        result = 10 / 0
    except ZeroDivisionError:
        print("You can't divide by zero!")

Multiple except blocks:

.. code-block:: python

    try:
        n = int(input("Enter a number: "))
        result = 100 / n
    except ValueError:
        print("That's not a number.")
    except ZeroDivisionError:
        print("Can't divide by zero.")
    except Exception as e:
        print("Unexpected error:", e)


Else Block
~~~~~~~~~~

Code inside `else` runs **only if** no exception occurred:

.. code-block:: python

    try:
        x = int("123")
    except ValueError:
        print("Conversion failed.")
    else:
        print("Conversion successful:", x)


Finally Block
~~~~~~~~~~~~~

Code inside `finally` runs **regardless** of what happened—exception, return, or normal exit. Useful for cleanup:

.. code-block:: python

    try:
        conn = open_connection()
    except ConnectionError:
        print("Cannot connect.")
    finally:
        conn.close()


Raising Exceptions with `raise`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can deliberately throw exceptions:

.. code-block:: python

    def set_age(age: int):
        if age < 0:
            raise ValueError("Age cannot be negative.")
        print("Age set to", age)

    set_age(-1)

Chaining exceptions:

.. code-block:: python

    try:
        1 / 0
    except ZeroDivisionError as e:
        raise RuntimeError("Custom error message") from e

Additional Resources
~~~~~~~~~~~~~~~~~~~~

- Official tutorial on errors and exceptions:  
  https://docs.python.org/3/tutorial/errors.html  
- Built‑in Exception Reference:  
  https://docs.python.org/3/library/exceptions.html  
