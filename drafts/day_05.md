# File I/O and Dictionary in Python

## File Input and Output (I/O) in Python
File I/O in Python allows reading from and writing to files, which is essential for data persistence.

### Opening a File
Python uses the `open()` function to open a file.
```python
file = open("example.txt", "r")  # Open file in read mode
```
Modes available for opening a file:
- `'r'` - Read mode (default, file must exist)
- `'w'` - Write mode (creates a new file or truncates an existing file)
- `'a'` - Append mode (adds data to the end of a file)
- `'b'` - Binary mode (used with other modes, e.g., `'rb'` for reading binary files)
- `'x'` - Exclusive creation mode (fails if the file exists)

### Reading a File
```python
with open("example.txt", "r") as file:
    content = file.read()  # Reads entire file
    print(content)
```
Other reading methods:
- `read(size)`: Reads specified number of bytes.
- `readline()`: Reads a single line.
- `readlines()`: Reads all lines into a list.

### Writing to a File
```python
with open("example.txt", "w") as file:
    file.write("Hello, Python!")
```
- `writelines()` can write multiple lines from a list.

### Appending to a File
```python
with open("example.txt", "a") as file:
    file.write("\nAppended text")
```

## Working with Dictionaries in Python
A dictionary is an unordered, mutable collection of key-value pairs.

### Creating a Dictionary
```python
person = {"name": "Alice", "age": 25, "city": "New York"}
```

### Accessing Dictionary Elements
```python
print(person["name"])  # Alice
```
Using `.get()` method avoids errors if the key does not exist:
```python
print(person.get("job", "Not Available"))
```

### Modifying a Dictionary
```python
person["age"] = 26  # Update value
person["job"] = "Engineer"  # Add new key-value pair
```

### Removing Elements
```python
del person["city"]
job = person.pop("job")  # Removes and returns the value
```

### Looping Through a Dictionary
```python
for key, value in person.items():
    print(f"{key}: {value}")
```

### Dictionary Methods
- `keys()`: Returns a list of keys.
- `values()`: Returns a list of values.
- `items()`: Returns a list of key-value pairs.
- `update()`: Merges another dictionary.

### Storing Dictionary Data in a File
Using `json` module for saving and loading dictionary data:
```python
import json

# Writing dictionary to a JSON file
with open("data.json", "w") as file:
    json.dump(person, file)

# Reading dictionary from a JSON file
with open("data.json", "r") as file:
    loaded_data = json.load(file)
```
This approach ensures that dictionary data is stored persistently.

## Conclusion
File I/O and dictionaries are essential in Python programming. File handling allows data storage and retrieval, while dictionaries provide a flexible way to store and manipulate structured data. Combining both, we can efficiently manage and persist complex data structures.

