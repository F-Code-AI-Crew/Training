Testing
=======

Automated testing is essential for **ensuring code quality**, catching bugs early, and making refactoring safer. This chapter introduces basic testing concepts and two popular Python testing frameworks.

Why Test?
~~~~~~~~~

- **Ensure code quality**: Verify that functions and classes behave as expected.  
- **Detect errors early**: Prevent regressions when making changes.  
- **Improve design**: Writing tests often leads to more modular, maintainable code.  

Basic Types of Testing
~~~~~~~~~~~~~~~~~~~~~~

1. **Unit Testing**  
   Tests individual functions or classes in isolation.  
2. **Integration Testing**  
   Tests combined components or modules working together.  

Introduction to `unittest`
~~~~~~~~~~~~~~~~~~~~~~~~~~

Python’s built‑in testing framework.

Writing Test Cases
------------------

1. Create a test file (e.g. `test_math.py`).  
2. Import `unittest` and your code under test.

.. code-block:: python

    import unittest
    from my_module import add, divide

3. Inherit `unittest.TestCase` and define methods starting with `test_`:

.. code-block:: python

    class TestMath(unittest.TestCase):

        def test_add(self):
            self.assertEqual(add(2, 3), 5)

        def test_divide_by_zero(self):
            with self.assertRaises(ZeroDivisionError):
                divide(10, 0)

Assert Methods
--------------

- `assertEqual(a, b)`  
- `assertTrue(x)` / `assertFalse(x)`  
- `assertRaises(exc, func, *args)`  

Organizing Test Suites
----------------------

You can group tests in multiple `TestCase` classes across files. Use a top-level directory `tests/`:


Running Tests
-------------

- **Command line**:

  .. code-block:: shell

      python -m unittest discover

- **Specific file**:

  .. code-block:: shell

      python -m unittest tests.test_math

- **In IDE**: Most editors (VSCode, PyCharm) detect and run `unittest` automatically.

Introduction to `pytest`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

`pytest` is a third‑party framework with a simpler syntax and powerful features.

Advantages
- Less boilerplate (no need to subclass).  
- Rich plugin ecosystem.  

Writing Tests
-------------

1. Create a file named `test_*.py` (e.g. `test_math.py`).  
2. Write plain functions starting with `test_`:

.. code-block:: python

    import pytest
    from my_module import multiply

    def test_multiply():
        assert multiply(2, 3) == 6

Fixtures
--------

`pytest` fixtures provide setup/teardown:

.. code-block:: python

    import pytest
    from my_module import Database

    @pytest.fixture
    def db():
        db = Database()
        yield db
        db.close()

    def test_query(db):
        result = db.query("SELECT 1")
        assert result == 1

Running `pytest`
----------------

.. code-block:: shell

    pytest            # runs all tests
    pytest -q         # quiet output
    pytest tests/     # tests in specific folder

Writing Tests for Previous Chapters
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Control flow**: Test edge cases for `if/elif/else`.  
- **Loops**: Verify loops produce correct lists or sums.  
- **Exceptions**: Ensure exceptions are raised correctly.  

Example: Testing a `factorial` function

.. code-block:: python

    def factorial(n: int) -> int:
        if n < 0:
            raise ValueError("n must be >= 0")
        return 1 if n < 2 else n * factorial(n-1)

    # unittest
    class TestFactorial(unittest.TestCase):
        def test_factorial(self):
            self.assertEqual(factorial(5), 120)
        def test_negative(self):
            with self.assertRaises(ValueError):
                factorial(-1)

    # pytest
    def test_factorial_pytest():
        assert factorial(5) == 120
    def test_negative_pytest():
        import pytest
        with pytest.raises(ValueError):
            factorial(-1)

Test-Driven Development (TDD)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

TDD is the practice of writing tests **before** code:

1. **Write a failing test** for a new feature.  
2. **Implement minimal code** to pass the test.  
3. **Refactor** while ensuring tests still pass.  

Benefits:
- Clarifies requirements.  
- Ensures thorough coverage.  
- Encourages simple design.  

Additional Resources
~~~~~~~~~~~~~~~~~~~~~

- `unittest` documentation:  
  https://docs.python.org/3/library/unittest.html  
- `pytest` documentation:  
  https://docs.pytest.org/en/stable/  
- TDD guide:  
  https://realpython.com/tdd-python/  
