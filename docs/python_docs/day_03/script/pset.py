# -- start count word --
def count_word_freq(text: str) -> dict:
    """
    Count word frequency in txt file (ignore punctuation and case) and print the top 10 most frequent words.

    Parameters
    ----------
    text : str
        String of content from a text file.

    Returns
    -------
    dict
        The top 10 most frequent words in key-value pairs (key is the word and value is the frequency).

    Examples
    --------
    >>> count_word_freq("This is a sample text. This text is simple. Simple text is easy to analyze.")
    {'is': 3, 'text': 3, 'this': 2, 'simple': 2, 'a': 1, 'sample': 1, 'easy': 1, 'to': 1, 'analyze': 1}

    Note
    ----
    - Count how often each word appears (ignore punctuation and case).
    - Store counts in a dictionary and print the top 10 most frequent words.
    """
    # Your code starts here
    result: dict = {}
    # Your code ends here
    return result
# -- end count word --

# -- start grade calculator --
def grade_calculator(raw_grade: list[dict]) -> list[dict]:
    """
    Compute average score per student and per subject from a list of score records.

    Parameters
    ----------
    raw_grade: list of dictionary
        Each dictionary contains a student's name, subject, and score with keys: "Name", "Subject", and "Score".

    Returns
    -------
    list[dict]
        The first dictionary contains the average score per student.
        The second dictionary contains the average score per subject.

    Examples
    --------
    >>> grade_calculator([
    {"Name": "Alice", "Subject": "Math", "Score": 85}, 
    {"Name": "Bob", "Subject": "Math", "Score": 78}, 
    {"Name": "Alice", "Subject": "Science", "Score": 90}, 
    {"Name": "Bob", "Subject": "Science", "Score": 82}
    ])
    [{"Alice": 87.5, "Bob": 80}, {"Math": 81.5, "Science": 86}]
    --------

    Note
    ----
    - Calculate the average score per student: 
        Alice = (85 + 90) / 2 = 87.5
        Bob = (78 + 82) / 2 = 80
    - Calculate the average score per subject: 
        Math = (85 + 78 ) / 2 = 81.5
        Science =  (90 + 82) / 2 = 86
    """
    # Your code starts here
    result: list = []
    # Your code ends here
    return result
# -- end grade calculator --

# -- start flatten json --
def flatten_json(nested_dict: dict[str, dict[str, str]]) -> dict:
    """
    Convert nested dictionary to flat dictionary using dot-separated keys.

    Parameters
    ----------
    nested_dict : dictionary of dictionary
        A dictionary that may contain nested dictionaries as values.

    Returns
    -------
    dict
        A flattened dictionary where nested keys are concatenated using dots.

    Examples
    --------
    >>> flatten_json({"user": { "name": "Alice", "info": { "email": "alice@example.com", "age": 25}}})
    {"user.name": "Alice", "user.info.email": "alice@example.com", "user.info.age": 25}

    Note
    ----
    - The keys in the resulting dictionary are formed by joining nested keys with dots.
    - {"user": { "name": "Alice"}}: the key path "user" -> "name" becomes "user.name".
    - {"user": {"info": {"email": "alice@example.com"}}}: the key path "user" -> "info" -> "email" becomes "user.info.email".
    - {"user": {"info": {"age": 25}}}: the key path "user" -> "info" -> "age" becomes "user.info.age"
    """
    # Your code starts here
    result: dict = {}
    # Your code ends here
    return result
# -- end flatten json --