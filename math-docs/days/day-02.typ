#import "@preview/theorion:0.3.3": *
// #import cosmos.fancy: *
#import cosmos.rainbow: *
// #import cosmos.clouds: *
#show: show-theorion

#set heading(numbering: "1.")

== Introduction

Linear systems of equations form a core topic in linear algebra with widespread applications in mathematics, science, engineering, and technology. Solving linear systems efficiently is crucial, and among various techniques, _Gaussian elimination_ is one of the most effective and widely used.

== Linear Systems

#definition(title: [Linear System])[
    A system of linear equations consists of multiple linear equations involving the same set of variables:

    $
        cases(
            a_11 x_1 + a_12 x_2 + ... + a_1n x_n = b_1,
            a_21 x_1 + a_22 x_2 + ... + a_2n x_n = b_2,
            dots.v,
            a_"m1" x_1 + a_"m2" x_2 + ... + a_"mn" x_n = b_m
        )
    $


    Where:
    - $a_(i j)$ are the coefficients,
    - $x_j$ are the unknowns,
    - $b_i$ are the constants.
]

== Matrix Representation

#theorem(title: [Matrix Representation])[
    A linear system can be written compactly in matrix form as:

    $ A dot x = b $

    Where:
    - $A$: $m times n$ coefficient matrix
    - $x$: $n times 1$ unknown vector
    - $b$: $m times 1$ result vector
]

This representation is ideal for applying numerical methods.

=== Determinant of a Matrix

#definition(title: [Determinant of a Matrix])[
    The determinant of a square matrix $A$, denoted $det(A)$ or $|A|$, helps determine invertibility.
]

#definition(title: [Determinant of $2 times 2$ matrix])[
    $ det mat(a, b; c, d) = "ad" - "bc" $
]

=== Transpose of a Matrix

#definition(title: [Transpose of a Matrix])[
    The transpose of a matrix $A$, denoted $A^T$, swaps its rows and columns.
]

#example()[
    $ A = mat(1, 2, 3; 4, 5, 6) $
    $ A^T = mat(1, 4; 2, 5; 3, 6) $
]

=== Inverse of a Matrix

#definition(title: [Inverse of a Matrix])[
    A square matrix $A$ has an inverse $A^"-1"$ if:

    $ A dot A^(-1) = A^(-1) dot A = I $
]

Methods to compute $A^"-1"$:
- Augmented matrix (row operations)
- Adjoint method:
$ A^"-1" = 1 / det(A) dot "adj"(A) $

== Gaussian Elimination

#definition(title: [Gaussian Elimination])[
    A step-by-step method to reduce a matrix to upper triangular form, consisting of:

    + *Form the augmented matrix*: $[A | B]$
    + *Forward elimination*:
        - Identify pivot elements along the main diagonal
        - Use row operations to zero out entries below each pivot
    + *Back substitution*:
        - Solve for variables starting from the last row upward
]

#example()[
    Given the system:

    $
        cases(
            2x + 3y - z & = 5,
            4x + y + 2z & = 6,
            -2x + 5y + 3z & = 7
        )
    $

    + Augmented Matrix
        $
            mat(
                2, 3, -1, |, 5;
                4, 1, 2, |, 6;
                -2, 5, 3, |, 7;
            )
        $
    + Row Reduction
        - Normalize the first row
        - Eliminate entries below the pivot
        - Repeat for next rows
    + Back Substitution \
        Find values of $z$, then $y$, and finally $x$.
]

== Gauss–Jordan Elimination
#definition(title: [Row Echelon Form of Matrix])[
    A matrix is in _row echelon form_ if:

    - All nonzero rows are above zero rows
    - The leading entry (pivot) in each nonzero row is 1
    - Each pivot is to the right of the one in the row above
    - All entries below a pivot are 0
]
#example()[
    $
        mat(
            1, 2, -1, |, 4;
            0, 1, 3, |, -2;
            0, 0, 1, |, 5;
        )
    $
]

#definition(title: [Gauss–Jordan Elimination])[
    An extension of Gaussian Elimination that produces Reduced Row Echelon Form (RREF), consisting of:
    + Form the augmented matrix $[A | B]$
    + Use row operations to form leading 1s (pivots)
    + Zero out *both* above and below the pivot in each column
]

=== Advantages

- Simplifies solving linear systems
- Easy to implement algorithmically
- Helps identify inconsistent or dependent systems

=== Visual Representation

$
    mat(
        1, "", "", "";
        0, 1, "", *;
        0, 0, 0, 0;
    )
$

Interpretation:
- Zero row at the bottom
- Leading 1s at $A_(1 1)$ and $A_(2 2)$
- All entries below pivots are 0

#example()[
    Solving with Row Echelon Form (REF)

    We are given the system:

    $
        cases(
            x + y + z & = 6,
            2x + 3y + 7z & = 20,
            x + 3y + 4z & = 13
        )
    $

    + *Write the Augmented Matrix*
        $
            mat(
                1, 1, 1, |, 6;
                2, 3, 7, |, 20;
                1, 3, 4, |, 13;
            )
        $
    + *Row Reduction to Row Echelon Form*
        - Keep Row 1 as is.
        - Eliminate below the first pivot (Row 1, Col 1):
            $ R_2 := R_2 - 2 dot R_1 $
            $ R_3 := R_3 - R_1 $
        New matrix:
        $
            mat(
                1, 1, 1, |, 6;
                0, 1, 5, |, 8;
                0, 2, 3, |, 7;
            )
        $
        - Eliminate below the second pivot (Row 2, Col 2):
            $ R_3 := R_3 - 2 dot R_2 $

        Resulting Row Echelon Form:
        $
            mat(
                1, 1, 1, |, 6;
                0, 1, 5, |, 8;
                0, 0, -7, |, -9;
            )
        $
    + *Back Substitution* \
        From the last row:
        $ -7z = -9 -> z = 9 / 7 $
        Second row:
        $ y + 5z = 8 -> y = 8 - 5·(9 / 7) = 11 / 7 $
        First row:
        $ x + y + z = 6 -> x = 6 - 11 / 7 - 9 / 7 = 22 / 7 $

    *Final Answer:*
    $ x = 22 / 7, y = 11 / 7, z = 9 / 7 $
]
