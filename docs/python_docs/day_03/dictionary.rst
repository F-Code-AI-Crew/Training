======================
Dictionaries in Python
======================

------------------------
What is a Dictionary?
------------------------
A dictionary in Python is an unordered collection of data in a key-value pair format. Dictionaries are mutable and indexed by keys, which can be any immutable type.

**Syntax:**

.. code-block:: python

   my_dict = {
       "name": "Alice",
       "age": 30,
       "city": "New York"
   }

------------------------
Creating a Dictionary
------------------------
You can create a dictionary in several ways:

.. code-block:: python

   # Using curly braces
   student = {"name": "John", "grade": "A"}

   # Using the dict() constructor
   student = dict(name="John", grade="A")

---------------------
Accessing Elements
---------------------
Use the key inside square brackets or the ``get()`` method.

.. code-block:: python

   name = student["name"]
   grade = student.get("grade")

---------------------
Modifying Elements
---------------------
You can update a value using the assignment operator.

.. code-block:: python

   student["grade"] = "A+"

------------------
Adding Elements
------------------
To add a new key-value pair:

.. code-block:: python

   student["age"] = 20

--------------------
Removing Elements
--------------------
Several methods can be used:

.. code-block:: python

   del student["age"]
   student.pop("grade")
   student.clear()  # Removes all items

---------------------
Dictionary Methods
---------------------
Common methods used with dictionaries:

.. code-block:: python

   keys = student.keys()
   values = student.values()
   items = student.items()

---------------------------------
Iterating Through a Dictionary
---------------------------------

.. code-block:: python

   for key, value in student.items():
       print(key, value)

----------------------
Nested Dictionaries
----------------------

.. code-block:: python

   people = {
       "person1": {"name": "Alice", "age": 25},
       "person2": {"name": "Bob", "age": 30}
   }

----------------------------
Dictionary Comprehension
----------------------------

.. code-block:: python

   squares = {x: x*x for x in range(5)}

----------------------------
Real-Life Usage Examples
----------------------------

**Machine Learning: Feature Representation**

Dictionaries are used for encoding features before passing to models.

.. code-block:: python

   sample = {
       "age": 29,
       "gender": "female",
       "income": 45000
   }

   features = {
       "age": sample["age"],
       "gender_female": 1 if sample["gender"] == "female" else 0,
       "income": sample["income"]
   }

**Chatbot Intent Mapping**

Mapping user intents to bot responses using dictionaries.

.. code-block:: python

   intents = {
       "greeting": "Hello! How can I help you today?",
       "farewell": "Goodbye! Have a great day.",
       "thanks": "You're welcome!"
   }

   user_input = "greeting"
   print(intents.get(user_input, "Sorry, I didn’t understand that."))

**Configuration Settings**

Storing application settings in dictionaries for easy access and modification.

.. code-block:: python

   config = {
       "debug": True,
       "database_uri": "sqlite:///mydb.db",
       "max_connections": 20
   }

   if config["debug"]:
       print("Debug mode is ON")
