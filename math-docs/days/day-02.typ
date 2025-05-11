#set heading(numbering: "1.")

= Introduction

Linear systems of equations form a core topic in linear algebra with widespread applications in mathematics, science, engineering, and technology. Solving linear systems efficiently is crucial, and among various techniques, _Gaussian elimination_ is one of the most effective and widely used.

= Linear Systems

A linear system of equations consists of multiple linear equations involving the same set of variables:

$
    cases(
        a_11 x_1 + a_12 x_2 + ... + a_1n x_n = b_1,
        a_21 x_1 + a_22 x_2 + ... + a_2n x_n = b_2,
        dots.v,
        a_"m1" x_1 + a_"m2" x_2 + ... + a_"mn" x_n = b_m
    )
$


Where:
- $a_"ij"$ are the coefficients,
- $x_j$ are the unknowns,
- $b_i$ are the constants.

= Matrix Representation

A linear system can be written compactly in matrix form as:

$ A dot X = B $

Where:
- $A$: $m times n$ coefficient matrix
- $X$: $n times 1$ unknown vector
- $B$: $m times 1$ result vector

This representation is ideal for applying numerical methods.

== Determinant of a Matrix

The determinant of a square matrix $A$, denoted $det(A)$ or $|A|$, helps determine invertibility.

For a $2 times 2$ matrix:
$ det mat(a, b; c, d) = "ad" - "bc" $

== Transpose of a Matrix

The transpose of a matrix $A$, denoted $A^T$, swaps its rows and columns.

Example:
$ A = mat(1, 2, 3; 4, 5, 6) $
$ A^T = mat(1, 4; 2, 5; 3, 6) $

== Inverse of a Matrix

A square matrix $A$ has an inverse $A^"-1"$ if:

$ A dot A^"-1" = I $, where $det(A) != 0$

Methods to compute $A^"-1"$:
- Augmented matrix (row operations)
- Adjoint method: $A^"-1" = 1 / det(A) dot "adj"(A)$

= Gaussian Elimination

A step-by-step method to reduce a matrix to upper triangular form:

== Steps:

1. *Form the augmented matrix*: $[A | B]$
2. *Forward elimination*:
    - Identify pivot elements along the main diagonal
    - Use row operations to zero out entries below each pivot
3. *Back substitution*:
    - Solve for variables starting from the last row upward

== Example

Given the system:

$cases(
    2x + 3y - z & = 5,
    4x + y + 2z & = 6,
    -2x + 5y + 3z & = 7
)$

=== Step 1: Augmented Matrix

$mat(
    2, 3, -1, |, 5;
    4, 1, 2, |, 6;
    -2, 5, 3, |, 7;
)$

=== Step 2: Row Reduction

- Normalize the first row
- Eliminate entries below the pivot
- Repeat for next rows

=== Step 3: Back Substitution

Find values of $z$, then $y$, and finally $x$.

= Gauss–Jordan Elimination

An extension of Gaussian Elimination that produces Reduced Row Echelon Form (RREF):

== Steps:

- Form the augmented matrix $[A | B]$
- Use row operations to form leading 1s (pivots)
- Zero out *both* above and below the pivot in each column

== Resulting Form:

$mat(
    1, 0, 0, |, x_1;
    0, 1, 0, |, x_2;
    0, 0, 1, |, x_3;
)$

= Row Echelon Form (REF)

A matrix is in _row echelon form_ if:

- All nonzero rows are above zero rows
- The leading entry (pivot) in each nonzero row is 1
- Each pivot is to the right of the one in the row above
- All entries below a pivot are 0

== Example

$mat(
    1, 2, -1, |, 4;
    0, 1, 3, |, -2;
    0, 0, 1, |, 5;
)$

== Advantages

- Simplifies solving linear systems
- Easy to implement algorithmically
- Helps identify inconsistent or dependent systems

== Visual Representation

$mat(
    1, "", "", "";
    0, 1, "", *;
    0, 0, 0, 0;
)$

Interpretation:
- Zero row at the bottom
- Leading 1s at $A_{11}$ and $A_{22}$
- All entries below pivots are 0

== Solving with Row Echelon Form (REF)
We are given the system:

$cases(
    x + y + z & = 6,
    2x + 3y + 7z & = 20,
    x + 3y + 4z & = 13
)$

*Step 1: Write the Augmented Matrix*

$mat(
    1, 1, 1, |, 6;
    2, 3, 7, |, 20;
    1, 3, 4, |, 13;
)$

*Step 2: Row Reduction to Row Echelon Form*

- Keep Row 1 as is.
- Eliminate below the first pivot (Row 1, Col 1):

$R_2 := R_2 - 2·R_1$

$R_3 := R_3 - R_1$

New matrix:

$mat(
    1, 1, 1, |, 6;
    0, 1, 5, |, 8;
    0, 2, 3, |, 7;
)$

- Eliminate below the second pivot (Row 2, Col 2):

$R_3 := R_3 - 2·R_2$

Resulting Row Echelon Form:

$mat(
    1, 1, 1, |, 6;
    0, 1, 5, |, 8;
    0, 0, -7, |, -9;
)$

*Step 3: Back Substitution*

From the last row:

$ -7z = -9 -> z = 9 / 7 $

Second row:

$ y + 5z = 8 -> y = 8 - 5·(9 / 7) = 11 / 7 $

First row:

$ x + y + z = 6 -> x = 6 - 11 / 7 - 9 / 7 = 22 / 7 $

== Final Answer:

$ x = 22 / 7, y = 11 / 7, z = 9 / 7 $
