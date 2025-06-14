import pytest
from pset import *


def test_count_word_freq():
    test_1_input = "This is a sample text. This text is simple. Simple text is easy to analyze."
    test_1_output = {'is': 3, 'text': 3, 'this': 2, 'simple': 2, 'a': 1, 'sample': 1, 'easy': 1, 'to': 1, 'analyze': 1}
    assert count_word_freq(test_1_input) == test_1_output

    test_2_input = "The quick brown fox jumps over the lazy dog. The dog was not amused."
    test_2_output = {'the': 3, 'dog': 2, 'quick': 1, 'brown': 1, 'fox': 1, 'jumps': 1, 'over': 1, 'lazy': 1, 'was': 1, 'not': 1}
    assert count_word_freq(test_2_input) == test_2_output

    test_3_input = "One 1 two 2 three 3 four 4 five 5 six 6 seven 7 eight 8 nine 9"
    test_3_output = {'one': 1, '1': 1, 'two': 1, '2': 1, 'three': 1, '3': 1, 'four': 1, '4': 1, 'five': 1, '5': 1}
    assert count_word_freq(test_3_input) == test_3_output

    test_4_input = "Hello World! This is a Test. The year is 2025? HELLO again, world; test this: 1, 2, 3..."
    test_4_output = {'hello': 2, 'world': 2, 'this': 2, 'is': 2, 'test': 2, 'a': 1, 'the': 1, 'year': 1, '2025': 1, 'again': 1}
    assert count_word_freq(test_4_input) == test_4_output

    test_5_input = """This is a sample text with a lot  duplicated   spaces or            tabs.
    Some address is 12 Thanh Thai Street, District 10, HCMC.
    Another address is 34 Thanh Thai St, D10, Ho Chi Minh City.
    Some texts are special such as "double quoted text" and 'single quoted text'. Some have mixed "It's all good!".
    Some proper names such as Alex Smith, or Mike Brown, or Jen K. Lee, or Andy P Tran."""
    test_5_output = {'some': 4, 'or': 4, 'is': 3, 'text': 3, 'a': 2, 'address': 2, 'thanh': 2, 'thai': 2, 'such': 2, 'as': 2}

    assert count_word_freq(test_5_input) == test_5_output

def test_grade_calculator():
    test_1_input = [{"Name": "Alice", "Subject": "Math", "Score": 85}, {"Name": "Bob", "Subject": "Math", "Score": 78}, {"Name": "Alice", "Subject": "Science", "Score": 90}, {"Name": "Bob", "Subject": "Science", "Score": 82}]
    test_1_output = [{"Alice": 87.5, "Bob": 80.0}, {"Math": 81.5, "Science": 86.0}]
    assert grade_calculator(test_1_input) == test_1_output

    test_2_input = [{"Name": "Dana", "Subject": "Math", "Score": 100}, {"Name": "Jack", "Subject": "Math", "Score": 0}, {"Name": "Jack", "Subject": "English", "Score": 0}, {"Name": "Dana", "Subject": "English", "Score": 80}]
    test_2_output = [{"Dana": 90.0, "Jack": 0.0}, {"Math": 50.0, "English": 40.0}]
    assert grade_calculator(test_2_input) == test_2_output

    test_3_input = [{"Name": "Eve", "Subject": "Physics", "Score": 95}, {"Name": "Frank", "Subject": "Physics", "Score": 85}, {"Name": "Grace", "Subject": "Physics", "Score": 70}]
    test_3_output = [{"Eve": 95.0, "Frank": 85.0, "Grace": 70.0}, {"Physics": 83.3}]
    assert grade_calculator(test_3_input) == test_3_output

    test_4_input = [{"Name": "Hank", "Subject": "Biology", "Score": 88}, {"Name": "Ivy", "Subject": "Biology", "Score": 92}, {"Name": "Hank", "Subject": "Math", "Score": 85}, {"Name": "Ivy", "Subject": "Math", "Score": 87}, {"Name": "Hank", "Subject": "English", "Score": 80}]
    test_4_output = [{"Hank": 84.3, "Ivy": 89.5}, {"Biology": 90.0, "Math": 86.0, "English": 80.0}]
    assert grade_calculator(test_4_input) == test_4_output

    test_5_input = [{"Name": "Mia", "Subject": "Math", "Score": 90}, {"Name": "Mia", "Subject": "Science", "Score": 85}, {"Name": "Noah", "Subject": "Math", "Score": 80}, {"Name": "Noah", "Subject": "Science", "Score": 75}, {"Name": "Olivia", "Subject": "Math", "Score": 70}, {"Name": "Olivia", "Subject": "Science", "Score": 65}]
    test_5_output = [{"Mia": 87.5, "Noah": 77.5, "Olivia": 67.5}, {"Math": 80.0, "Science": 75.0}]
    assert grade_calculator(test_5_input) == test_5_output

def test_flatten_json():
    test_1_input = {"user": { "name": "Alice", "info": { "email": "alice@example.com", "age": 25}}}
    test_1_output = {"user.name": "Alice", "user.info.email": "alice@example.com", "user.info.age": 25}
    assert flatten_json(test_1_input) == test_1_output

    test_2_input = {"company": {"employee": {"name": "Dana", "id": 1234}}}
    test_2_output = {"company.employee.name": "Dana", "company.employee.id": 1234}
    assert flatten_json(test_2_input) == test_2_output

    test_3_input = {"x": {"y": 1, "z": {"p": 2, "q": 3}}, "m": 4, "a": {"b": {"c": {"d": {"e": 5}}}}}
    test_3_output = {"x.y": 1, "x.z.p": 2, "x.z.q": 3, "m": 4, "a.b.c.d.e": 5}
    assert flatten_json(test_3_input) == test_3_output

    test_4_input = {"a": {"b1": {"c1": 1}, "b2": {"c2": 2}}, "d": {"e": 3}}
    test_4_output = {"a.b1.c1": 1, "a.b2.c2": 2, "d.e": 3}
    assert flatten_json(test_4_input) == test_4_output

    test_5_input = {"data": {"id": 10, "valid": True, "tags": ["a", "b"], "info": None}}
    test_5_output = {"data.id": 10, "data.valid": True, "data.tags": ["a", "b"], "data.info": None}

    assert flatten_json(test_5_input) == test_5_output