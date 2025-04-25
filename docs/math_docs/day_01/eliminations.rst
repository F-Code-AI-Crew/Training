Gaussian Elimination
^^^^^^^^^^^^^^^^^^^^^

**Gaussian elimination** is a method for solving systems of linear equations. It transforms the system’s augmented matrix into an **upper triangular form** using a sequence of row operations. Once in this form, the system is solved using **back-substitution**.

Steps:

1. **Form the augmented matrix** of the system.
2. **Use row operations** to create zeros below the leading coefficient (pivot) in each column.
3. **Continue this process** for all rows until an upper triangular matrix is formed.
4. **Back-substitute** to find the values of the unknowns.

.. math::

    \begin{bmatrix}
    a_{11} & a_{12} & \dots & a_{1n} & | & b_1 \\
    0 & a_{22}' & \dots & a_{2n}' & | & b_2' \\
    \vdots & \vdots & \ddots & \vdots & & \vdots \\
    0 & 0 & \dots & a_{nn}'' & | & b_n''
    \end{bmatrix}

Gauss-Jordan Elimination
^^^^^^^^^^^^^^^^^^^^^^^^^

**Gauss-Jordan elimination** is an extension of Gaussian elimination. It reduces the augmented matrix not only to upper triangular form but further into **reduced row echelon form (RREF)**, where every pivot is 1 and all other entries in the pivot’s column are zero.

Steps:

1. **Form the augmented matrix**.
2. Use **row operations** to create leading 1’s (pivots).
3. **Eliminate all other entries** in the pivot’s column to zero (both above and below).
4. The resulting matrix has the form:

.. math::

    \begin{bmatrix}
    1 & 0 & 0 & | & x_1 \\
    0 & 1 & 0 & | & x_2 \\
    0 & 0 & 1 & | & x_3
    \end{bmatrix}

Advantages:
- Gauss-Jordan gives the **final solution directly**, without back-substitution.
- It is often used in **computer algorithms** for matrix inversion and solving linear systems.

Both methods are core to numerical linear algebra and are widely used in engineering, physics, and computer science.
