Row Echelon Form Matrix
=======================

To solve a matrix equation, we often convert the augmented matrix :math:`[A | B]` into **Row Echelon Form (REF)** using row operations.

Definition
----------

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

Advantages
----------

- Simplifies the solving process.
- Easy to implement algorithmically.
- Helps identify inconsistent or dependent systems.

Graphical Representation of Row Echelon Form
--------------------------------------------

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

Solving a System Using Row Echelon Form
---------------------------------------

To solve a system of linear equations using the **Row Echelon Form**, follow these steps:

1. **Form the Augmented Matrix**  
   Combine the coefficient matrix \( A \) and the constants vector \( B \) into an augmented matrix \( [A | B] \).

2. **Apply Elementary Row Operations**  
   Use the following operations to convert the matrix into row echelon form:
   - Swap two rows.
   - Multiply a row by a nonzero scalar.
   - Add or subtract a multiple of one row to another row.

3. **Achieve Row Echelon Form**  
   Continue row operations until the matrix meets the criteria:
   - Leading 1s appear progressively to the right.
   - Zeros below each pivot (leading 1).
   - Rows of all zeros are at the bottom.

4. **Perform Back-Substitution**  
   Once in REF, solve from the bottom up:
   - Start with the last non-zero row (typically only one variable).
   - Substitute that solution into the equation above it.
   - Continue until all variables are solved.

**Example**

Given system:

.. math::

    \begin{aligned}
    x + 2y - z &= 4 \\
    2y + 3z &= -2 \\
    z &= 5
    \end{aligned}

Augmented matrix in REF:

.. math::

    \begin{bmatrix}
    1 & 2 & -1 & | & 4 \\
    0 & 1 & 3 & | & -2 \\
    0 & 0 & 1 & | & 5
    \end{bmatrix}

Back-substitution:

.. math::

    z = 5 \\
    y + 3z = -2 \Rightarrow y = -2 - 3(5) = -17 \\
    x + 2y - z = 4 \Rightarrow x = 4 - 2(-17) + 5 = 43

**Final solution:**

.. math::

    x = 43,\quad y = -17,\quad z = 5