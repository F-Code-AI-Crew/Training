Matrix Representation
----------------------

To streamline the process of solving a linear system, we convert the system into **matrix form**, which is concise and well-suited for computation:

.. math::

    A \cdot X = B

Where:

- **A** is the **coefficient matrix** of size :math:`m \times n`, containing the coefficients of the variables from each equation in the system.
- **X** is the **column vector of unknowns** of size :math:`n \times 1`, representing the variables :math:`x_1, x_2, \dots, x_n`.
- **B** is the **result or constants vector** of size :math:`m \times 1`, holding the constants from the right-hand side of each equation.

Example
^^^^^^^

Consider the following linear system of 3 equations with 3 unknowns:

.. math::

    \begin{cases}
    2x + 3y - z = 5 \\
    -x + 7y + 2z = 3 \\
    4x - y + 6z = 12
    \end{cases}

This can be written in matrix form as:

.. math::

    \begin{bmatrix}
    2 & 3 & -1 \\
    -1 & 7 & 2 \\
    4 & -1 & 6
    \end{bmatrix}
    \cdot
    \begin{bmatrix}
    x \\
    y \\
    z
    \end{bmatrix}
    =
    \begin{bmatrix}
    5 \\
    3 \\
    12
    \end{bmatrix}

Advantages of Matrix Representation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- **Compactness**: Makes large systems easier to manage.
- **Computational Efficiency**: Allows application of algorithms such as Gaussian elimination, LU decomposition, or iterative solvers.
- **Scalability**: Can be implemented easily in software for automated solving (e.g., using NumPy in Python or MATLAB).
- **Foundation for Advanced Topics**: Forms the basis for more complex concepts such as eigenvalues, vector spaces, and matrix factorizations.