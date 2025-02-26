# Day 3: Control Flow, Loops, Exception Handling, Testing, and Debugging

## 1. Control Flow

### Definition
Control flow refers to the order in which statements are executed in a program. It allows you to make decisions and change the flow of execution using conditions.

### Explanation
In Python, control flow is managed with structures like `if`, `elif`, and `else`. These statements evaluate conditions (e.g., `x > 0`) and execute specific blocks of code based on whether the condition is true or false.

### Code Snippet
```python
# Example of control flow with if, elif, and else
age = 20
if age < 18:
    print("You are a minor.")
elif age >= 18 and age < 65:
    print("You are an adult.")
else:
    print("You are a senior.")
```
**Output**: `You are an adult.`  
**Try It**: Change `age` to 15 or 70 and run the code to see different outputs.

---

## 2. Loops

### Definition
Loops are used to repeat a block of code multiple times, either for a set number of iterations or until a condition is met.

### Explanation
Python supports two main types of loops: `for` (iterates over a sequence like a list) and `while` (repeats as long as a condition is true). Loops are useful for tasks like processing lists or waiting for user input.

### Code Snippet
```python
# Example of for and while loops
# For loop to print numbers 0 to 4
for i in range(5):
    print(f"Number: {i}")

# While loop to count down from 3
count = 3
while count > 0:
    print(f"Countdown: {count}")
    count -= 1
print("Blast off!")
```
**Output**:
```
Number: 0
Number: 1
Number: 2
Number: 3
Number: 4
Countdown: 3
Countdown: 2
Countdown: 1
Blast off!
```
**Try It**: Modify the range in the `for` loop or the condition in the `while` loop to experiment.

---

## 3. Exception Handling

### Definition
Exception handling is the process of managing errors or unexpected events (called exceptions) in a program to prevent it from crashing.

### Explanation
Python uses `try` and `except` blocks to catch and handle exceptions. This ensures the program can gracefully recover from errors like division by zero or file not found, improving reliability.

### Code Snippet
```python
# Example of exception handling
try:
    number = int(input("Enter a number: "))
    result = 10 / number
    print(f"Result: {result}")
except ValueError:
    print("Please enter a valid number!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
```
**Output**: (Depends on input)
- If input is "5": `Result: 2.0`
- If input is "0": `Cannot divide by zero!`
- If input is "abc": `Please enter a valid number!`
**Try It**: Enter different values (e.g., 0, a letter, a number) to see how exceptions are handled.

---

## 4. Testing

### Definition
Testing is the process of verifying that your code works as expected by running specific cases to check for correctness and bugs.

### Explanation
In Python, testing is often done using the `unittest` module. You write test cases to check functions or logic, ensuring the program behaves as intended before deployment.

### Code Snippet
```python
import unittest

def add_numbers(a, b):
    return a + b

class TestMathFunctions(unittest.TestCase):
    def test_add_numbers(self):
        self.assertEqual(add_numbers(2, 3), 5)
        self.assertEqual(add_numbers(-1, 1), 0)

if __name__ == '__main__':
    unittest.main()
```
**Output**: (Runs tests and shows success or failure)
- If successful: `.` (dot) and “OK” message.
- If failure: `F` and error details.
**Try It**: Add a new test case (e.g., `self.assertEqual(add_numbers(0, 0), 0)`) or modify a value to see a failure.

---

## 5. Debugging

### Definition
Debugging is the process of finding and fixing errors or bugs in your code to make it work correctly.

### Explanation
Python provides tools like the `pdb` module or IDE debuggers to step through code, inspect variables, and identify issues. Debugging helps you understand why a program fails and how to fix it.

### Code Snippet
```python
import pdb

def calculate_division(a, b):
    pdb.set_trace()  # Start debugger
    result = a / b
    return result

# Run with debugger
try:
    calculate_division(10, 0)
except ZeroDivisionError:
    print("Error caught during debugging!")

# Without debugger, just run to see the error
# calculate_division(10, 0)
```
**Output**: (With debugger)
- Pauses at `pdb.set_trace()`, allowing you to:
  - Type `n` (next) to step through code.
  - Type `p a` or `p b` to print variables.
  - Type `q` (quit) to exit.
- If division by zero, catches the exception with “Error caught during debugging!”.
**Try It**: Run with `pdb.set_trace()`, step through, and observe variable values. Uncomment the last line to see the error without debugging.
