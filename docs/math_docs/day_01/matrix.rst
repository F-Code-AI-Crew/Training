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

Row Echelon Form
----------------

To solve a matrix equation, we often convert the augmented matrix :math:`[A | B]` into **Row Echelon Form (REF)** using row operations.

A matrix is in row echelon form if:

- All nonzero rows are above any rows of all zeros.
- The leading entry of each nonzero row is 1 (called a **leading 1**).
- Each leading 1 is to the right of the leading 1 in the row above it.
- All entries below a leading 1 are zeros.

Example:

.. math::

    \begin{bmatrix}
    1 & 2 & -1 & | & 4 \\
    0 & 1 & 3 & | & -2 \\
    0 & 0 & 1 & | & 5
    \end{bmatrix}

This form helps in back-substitution to solve the system efficiently.

Advantages:
- Simplifies the solving process.
- Easy to implement algorithmically.
- Helps identify inconsistent or dependent systems.

Graphical Representation of Row Echelon Form
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Example:

The following matrix is in row echelon form:

.. math::

    \begin{bmatrix}
    1 & * & * & * \\
    0 & 1 & * & * \\
    0 & 0 & 0 & 0
    \end{bmatrix}

It has:
- One zero row (the third), which is below the nonzero rows.
- Pivot positions at :math:`(A_{11})` and :math:`(A_{22})`, where the leading 1s are located.

This structure satisfies all the conditions of row echelon form:
- Leading 1s move to the right as you move down the rows,
- Rows consisting entirely of zeros are at the bottom,
- All entries below a pivot are zeros.