# Object-Oriented Programming (OOP) in Python

Todo:
- [ ] Property decorator in encapsulation
- [ ] Update inheritance
    - [ ] More types of inheritance
    - [ ] MRO mechanism
- [ ] Update better overiding example in polymorphism
- [ ] Add data model
- [ ] Add dunder methods

## Introduction
Object-Oriented Programming (OOP) is a programming paradigm that organizes code using objects and classes. Python fully supports OOP, enabling efficient code reuse and modularity.

## Key OOP Concepts
### 1. **Classes and Objects**
- A **class** is a blueprint for creating objects.
- An **object** is an instance of a class.

#### Defining a Class and Creating an Object
```python
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def display_info(self):
        print(f"Car: {self.brand} {self.model}")

# Creating an object
car1 = Car("Toyota", "Corolla")
car1.display_info()
```

### 2. **Encapsulation**
Encapsulation is the practice of keeping data and methods together within a class while restricting direct access to internal variables. The goal of encapsulation is to hide data and complexity.

These are convention of access notation, although Python does not restrict access to these components.
- Default access: `var`
- Protected access: `_var`
- Private access: `__var` (could be accessed by name mangling)

#### Private and Public Attributes
```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private attribute
    
    def deposit(self, amount):
        self.__balance += amount
    
    def get_balance(self):
        return self.__balance

account = BankAccount(1000)
account.deposit(500)
print(account.get_balance())  # 1500
```

### 3. **Inheritance**
Inheritance allows a class to inherit attributes and methods from another class.

#### Example of Inheritance
```python
class Vehicle:
    def __init__(self, brand):
        self.brand = brand
    
    def show_brand(self):
        print(f"Brand: {self.brand}")

class Car(Vehicle):  # Inheriting from Vehicle
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model
    
    def display_info(self):
        print(f"Car: {self.brand} {self.model}")

car1 = Car("Honda", "Civic")
car1.display_info()
```

### 4. **Polymorphism**
Polymorphism allows different classes to use the same method name but implement it differently, often in subclass inherited from one or multiple superclass. This could be achieved by overriding and overloading.

#### Example of Polymorphism
```python
class Animal:
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"

animals = [Dog(), Cat()]
for animal in animals:
    print(animal.make_sound())
```

### 5. **Abstraction**
Abstraction hides implementation details and only exposes essential functionality. The goal of abstraction is to simplify objectives. In Python, we could use `abstract base class` mechanism to implement this concept.

#### Example of Abstraction
```python
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "Bark!"

dog = Dog()
print(dog.make_sound())
```

## Conclusion
OOP in Python provides powerful features like encapsulation, inheritance, polymorphism, and abstraction. By leveraging these principles, developers can write more structured, reusable, and maintainable code.
