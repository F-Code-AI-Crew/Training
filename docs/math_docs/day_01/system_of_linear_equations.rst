System of Linear Equations
---------------------------

Introduction
^^^^^^^^^^^^

A **linear equation** in variables \(x_1, x_2, \dots, x_n\) is an equation of the form:

.. math::

    a_1x_1 + a_2x_2 + \cdots + a_nx_n = b

where:
- \(a_1, a_2, \dots, a_n\) are known coefficients,
- \(x_1, x_2, \dots, x_n\) are unknown variables,
- \(b\) is a constant term.

Definition of a System
^^^^^^^^^^^^^^^^^^^^^^

A **system of linear equations** is a collection of one or more linear equations involving the same set of variables. It can be written in the general form:

.. math::

    \begin{cases}
    a_{11}x_1 + a_{12}x_2 + \cdots + a_{1n}x_n = b_1 \\
    a_{21}x_1 + a_{22}x_2 + \cdots + a_{2n}x_n = b_2 \\
    \vdots \\
    a_{m1}x_1 + a_{m2}x_2 + \cdots + a_{mn}x_n = b_m
    \end{cases}

where:
- \(a_{ij}\) are the known coefficients of the system,
- \(x_j\) are the unknowns,
- \(b_i\) are the constant terms on the right-hand side.

Types of Solutions
^^^^^^^^^^^^^^^^^^

Depending on the relationships among the equations, a system of linear equations may have:

- **A unique solution**: The equations intersect at exactly one point (consistent and independent).
- **No solution**: The equations represent parallel lines or planes that never intersect (inconsistent).
- **Infinitely many solutions**: The equations represent the same geometric object (dependent system).

Graphical Interpretation
^^^^^^^^^^^^^^^^^^^^^^^^

In two or three dimensions, each linear equation can be interpreted geometrically as a line or a plane:

- Two lines intersecting at a single point → **one unique solution**.
- Two lines that are parallel and never intersect → **no solution**.
- Two overlapping lines (i.e., the same line) → **infinitely many solutions**.

The intersection points (if any) represent the solutions to the system of equations.

.. image:: /_static/images/math_day_01/system_linear_equations_graph.png
   :alt: Graph of a system of linear equations
   :align: center
   :width: 500px