.. TODO: Anchor links to these tools


Setup Environment
==================

According to the current (May 2025) `Status of Python versions <https://devguide.python.org/versions/>`_,
consider to install version between 3.9 and 3.12.

Python interpreter
-------------------

Minimal python interpreter (CPython) setup

.. tab-set::

    .. tab-item:: Windows

        Official python launcher for windows: https://www.python.org/downloads/

        Choose a binary from the official website under the **"Looking for a specific release?"**

        .. image:: /_static/images/misc/windows_binary.png
            :alt: Recent python releases
        
        The binary includes a CPython interpreter for the selected version, along with the 
        Python Launcher - a tool for managing multiple Python versions on Windows. In this 
        guide, I'll download the ``3.12.10`` version.

        .. image:: /_static/images/misc/pylauncher_start.png
            :alt: Python launcher start windows
        
        On the first screen of the installer, choose **"Install Now"**, and make sure to 
        leave the "Add python.exe to PATH" unchecked. After the installation, you will 
        have CPython ``3.12.10`` and python launcher in your machine. To verify that the 
        installation was successful, open a new PowerShell window and run

        .. code-block:: powershell

            py --list
        
        This command should display the installed Python interpreter(s). You can repeat 
        this process to install additional CPython versions on your machine.

        .. code-block:: powershell

            -V:3.12 *        Python 3.13 (64-bit)

    .. tab-item:: Linux/WSL/MacOS

        ``pyenv`` - a simple python version manager.

        Follow the official guide on https://github.com/pyenv/pyenv to install pyenv 
        on your machine. In the installing python version step, skip the global setting as below

        .. code-block:: shell

            pyenv install 3.12.10
        
        To verify if the installation was successfully, open a new shell and run

        .. code-block:: powershell
            
            pyenv versions
        
        This command should display the installed Python interpreter(s). You can repeat 
        this process to install additional CPython versions on your machine.

        .. code-block:: shell

            * system (set by /home/user/.pyenv/version)
            3.12.10

Virtual environment
--------------------

Isolate project environment from the global one.

.. tab-set::

    .. tab-item:: Windows

        In you project directory, run

        .. code-block:: powershell

            py -3.12 -m venv .venv
            .\.venv\Scripts\activate
        
        You have created a virtual environment for your project and activated it. In 
        case your powershell does not display the environment notation, check the 
        interpreter source by running

        .. code-block:: powershell

            (Get-Command python).Source
        
        This command will return the path to the python interpreter binary inside 
        ``.venv`` directory that you created. The output should looks like below

        .. code-block:: powershell

            Path\To\Your\Project\.venv\Scripts\python.exe

    .. tab-item:: Linux/WSL/MacOS

        In your project directory, run

        .. code-block:: shell

            pyenv local 3.12.10
            python -m venv .venv
            source .venv/bin/activate
        
        You have created a virtual environment for your project and activated it. In 
        case your shell does not display the environment notation (not likely to happen btw), 
        check the interpreter source by running

        .. code-block:: shell

            which python
        
        This command will return the path to the python interpreter binary inside 
        ``.venv`` directory that you created. The output should looks like below

        .. code-block:: shell

            Path/To/Your/Project/.venv/bin/python


To deactivate the virtual environment, run 

.. code-block:: shell

    deactivate


Text editor/IDE
-------------------

At this point, use any editor or IDE you're comfortable with. If you're using one of 
the two listed below, there are some extensions that can enhance your workflow.

1. `Visual Studio Code <https://code.visualstudio.com/>`_. Ensure to install following extensions:

* `Python <https://marketplace.visualstudio.com/items?itemName=ms-python.python>`_: Complete pack for editting python code
* `Mypy Type Checker <https://marketplace.visualstudio.com/items?itemName=ms-python.mypy-type-checker>`_: Enhance type checking

2. `PyCharm <https://www.jetbrains.com/pycharm/>`_. Ensure to install following plugin:

* `Mypy <https://plugins.jetbrains.com/plugin/11086-mypy>`_: Enhance type checking

Optional
---------

Notable tools that you might want to use

* `uv <https://github.com/astral-sh/uv>`_ - A blazingly fast project and package manager. Ideal for daily use, and especially useful for projects that require an optimized setup.
* `anaconda <https://www.anaconda.com/>`_ - A comprehensive distribution for Python and R. It's quite heavy, but widely used and includes everything you need for scientific computing and data analysis.
