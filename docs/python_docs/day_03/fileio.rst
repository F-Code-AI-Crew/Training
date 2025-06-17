==================
File I/O in Python
==================

--------------------
What is File I/O?
--------------------
File I/O (Input/Output) refers to reading data from and writing data to files. 
In Python, this is done using built-in functions.

-----------------
Opening a File
-----------------
**Syntax:**

.. code-block:: python

   file = open('filename', 'mode')

**Common modes:**
- `'r'`: Read (default mode)
- `'w'`: Write (creates new or overwrites existing file)
- `'a'`: Append (adds to the end of the file)
- `'b'`: Binary mode (e.g., 'rb', 'wb')
- `'x'`: Create a new file, fails if file exists

----------------------
Reading from a File
----------------------
.. code-block:: python

   file = open('example.txt', 'r')
   content = file.read()
   file.close()

**Other methods:**

- ``readline()``: Reads one line at a time

  .. code-block:: python

     with open('example.txt', 'r') as file:
         line1 = file.readline()
         line2 = file.readline()
         print("First line:", line1.strip())
         print("Second line:", line2.strip())

- ``readlines()``: Returns a list of all lines

  .. code-block:: python

     with open('example.txt', 'r') as file:
         lines = file.readlines()
         print("All lines as list:")
         for i, line in enumerate(lines, 1):
             print(f"Line {i}: {line.strip()}")

--------------------
Writing to a File
--------------------
.. code-block:: python

   file = open('example.txt', 'w')
   file.write("Hello, World!\\n")
   file.close()

Use `'a'` mode to append data instead of overwriting.


---------------------------
Using ``with`` Statement
---------------------------
Automatically manages file closing.

.. code-block:: python

   with open('example.txt', 'r') as file:
       content = file.read()

----------------------------------
Working with Files Line-by-Line
----------------------------------
.. code-block:: python

   with open('example.txt', 'r') as file:
       for line in file:
           print(line.strip())

-------------------------------------
Checking File Existence (Optional)
-------------------------------------
.. code-block:: python

   import os
   if os.path.exists("example.txt"):
       print("File exists.")
   else:
       print("File not found.")

-----------------------
File Methods Summary
-----------------------
Below are commonly used file object methods in Python:

- ``read(size=-1)``: Reads and returns up to `size` bytes. If `size` is omitted or negative, reads until end of file.
  
  Example:
  .. code-block:: python

     content = file.read(100)  # Read first 100 bytes

- ``write(string)``: Writes the specified string to the file. Only works in write or append mode.

  Example:
  .. code-block:: python

     file.write("Hello, World!\\n")

- ``close()``: Closes the file. After closing, file operations will raise an error.

  Example:
  .. code-block:: python

     file.close()

- ``seek(offset, whence=0)``: Moves the file pointer to the given byte offset.
  - `offset`: number of bytes
  - `whence`: optional; 0 (default) means start of file, 1 means current position, 2 means end of file

  Example:
  .. code-block:: python

     file.seek(0)  # Move to the beginning of file

- ``tell()``: Returns the current file pointer position in bytes.

  Example:
  .. code-block:: python

     position = file.tell()

------------------
Binary File I/O
------------------

**Write a Binary File**

.. code-block:: python

    data = bytes([120, 3, 255, 0, 100]) 

    with open('example.bin', 'wb') as file:
        file.write(data)

**Read a Binary File**

.. code-block:: python

    with open('example.bin', 'rb') as file:
        content = file.read()
    print("Binary content:", content)

---------------------------
Example in Some of Project
---------------------------

**Reading Annotation File**

.. code-block:: text

    0--Parade/0_Parade_Parade_0_194.jpg
    5
    111 425 122 127 0 1 0 0 0 1 
    209 347 70 103 0 1 0 0 0 0 
    368 252 89 133 0 1 0 0 0 0 
    555 282 89 100 0 1 0 0 0 1 
    707 252 92 133 0 1 0 0 0 0 

.. code-block:: python

    annotations = {}

    with open('wider_face_val_bbx_gt.txt', 'r') as file:
        lines = [line.strip() for line in file if line.strip() != ""]

    idx = 0
    while idx < len(lines):
        image_path = lines[idx]
        idx += 1

        num_faces = int(lines[idx])
        idx += 1

        boxes = []
        for _ in range(num_faces):
            box = lines[idx].split()
            box = list(map(int, box[:4]))
            boxes.append(box)
            idx += 1

        annotations[image_path] = boxes
