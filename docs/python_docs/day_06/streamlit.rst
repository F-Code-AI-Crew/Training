==================
Introduction to Streamlit
==================

--------------------
What is Streamlit?
--------------------
Streamlit is an open-source Python framework that allows developers to build interactive and data-driven web applications with minimal effort. It is designed primarily for machine learning and data science applications, providing an easy way to create user interfaces without requiring extensive knowledge of web development.

--------------------
Why Use Streamlit?
--------------------
- **Simplicity**: Streamlit enables quick and easy creation of web applications using only Python scripts.
- **No Frontend Experience Needed**: Unlike Flask or Django, Streamlit does not require HTML, CSS, or JavaScript knowledge.
- **Rapid Prototyping**: Developers can quickly visualize data and test machine learning models with an interactive interface.
- **Automatic UI Generation**: Streamlit automatically infers UI components from Python functions, making the development process more intuitive.

--------------------
Installation
--------------------
To install Streamlit, simply run:

.. code-block:: python

    %pip install streamlit

To verify the installation, run:

.. code-block:: python

    streamlit hello

This will launch an example Streamlit application in your web browser.

--------------------
Writing Your First Streamlit App
--------------------
1. Create a Python file, e.g., `app.py`, and add the following code:

.. code-block:: python

    import streamlit as st

    st.title("Hello, Streamlit!")
    st.write("This is a simple Streamlit app.")

2. Run the application:

.. code-block:: python

    streamlit run app.py

This will open a new tab in your default web browser displaying your Streamlit application.

--------------------
Key Features and Components
--------------------
**Displaying Text**

- `st.title("Title")` - Creates a large title.
- `st.header("Header")` - Creates a header.
- `st.subheader("Subheader")` - Creates a subheader.
- `st.write("Some text")` - Displays text or data.
- `st.markdown("**Bold text**")` - Supports Markdown syntax.
- `st.code("print(a + b)")` - Display a code block.
- `st.html("<p>HTML code</p>")` - Insert HTML to your application.

**Interactive Widgets**

- `st.button("Click Me")` - Creates a button.
- `st.checkbox("Check this box")` - Creates a checkbox.
- `st.radio("Choose one", ["A", "B", "C"])` - Creates a radio button.
- `st.selectbox("Select an option", ["Option 1", "Option 2"])` - Creates a dropdown.
- `st.slider("Pick a number", 0, 100)` - Creates a slider.
- `st.text_input("Enter text")` - Creates a text input field.
- `st.numer_input("Label, min_value=0, max_value=10, step=1")` - Creates a number input field.

**Displaying Data**

- `st.dataframe(dataframe)` - Displays a pandas DataFrame.
- `st.table(dataframe)` - Displays data in a static table.
- `st.json(json_data)` - Displays JSON data in a formatted way.

**Charts and Visualizations**

- `st.line_chart(data)` - Creates a line chart.
- `st.bar_chart(data)` - Creates a bar chart.
- `st.area_chart(data)` - Creates an area chart.
- `st.pyplot(fig)` - Displays Matplotlib figures.
- `st.plotly_chart(fig)` - Displays Plotly figures.

**Uploading and Downloading Files**

- `st.file_uploader("Upload a file")` - Allows users to upload files.
- `st.download_button("Download", data)` - Creates a file download button.

--------------------
Example: A Simple Data Dashboard
--------------------

.. code-block:: python

    import streamlit as st
    import pandas as pd
    import matplotlib.pyplot as plt

    data = pd.DataFrame({
        "Category": ["A", "B", "C", "D"],
        "Values": [10, 20, 30, 40]
    })

    st.title("Simple Data Dashboard")
    st.write("This dashboard displays sample data.")

    st.table(data)

    fig, ax = plt.subplots()
    ax.bar(data["Category"], data["Values"], color=['blue', 'green', 'red', 'purple'])
    st.pyplot(fig)


For further learning, refer to the official documentation: `Streamlit Docs <https://docs.streamlit.io/>`

For a concise overview, check out the cheat-sheet: `Streamlit Cheat Sheet <https://cheat-sheet.streamlit.app/>`