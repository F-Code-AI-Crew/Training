# Linear Systems, Matrices, and Gaussian Elimination

## Introduction
Linear systems of equations are a fundamental topic in linear algebra with widespread applications in mathematics, science, engineering, and technology. Solving linear systems can be achieved through various methods, with Gaussian elimination being one of the most common and effective techniques.

## Linear Systems of Equations
A linear system of equations consists of a set of equations in the general form:

```math
\begin{cases}
  a_{11}x_1 + a_{12}x_2 + \dots + a_{1n}x_n = b_1 \\
  a_{21}x_1 + a_{22}x_2 + \dots + a_{2n}x_n = b_2 \\
  \vdots \\
  a_{m1}x_1 + a_{m2}x_2 + \dots + a_{mn}x_n = b_m
\end{cases}
```

where \(a_{ij}\) are the coefficients, \(x_j\) are the unknowns, and \(b_i\) are the constants.

## Matrix Representation
A linear system can be represented in matrix form as:

```math
A \cdot X = B
```

where:
- \(A\) is the coefficient matrix of size \(m \times n\),
- \(X\) is the unknown vector of size \(n \times 1\),
- \(B\) is the result vector of size \(m \times 1\).

This representation simplifies computations and facilitates the application of numerical methods.

## Gaussian Elimination
Gaussian elimination is a method that transforms the system into an upper triangular form using elementary row operations. The procedure consists of:

1. **Step 1: Convert to Augmented Matrix**
   
   Express the system as an augmented matrix \([A | B]\).

2. **Step 2: Transform the Matrix into Upper Triangular Form**
   
   - Select the pivot element on the main diagonal.
   - Use elementary row operations to eliminate elements below the pivot.
   - Repeat this process for the subsequent rows.

3. **Step 3: Solve the System by Back Substitution**
   
   - Once the matrix is in upper triangular form, the system can be solved efficiently by back-substituting from the last row upward.

## Example
Solve the linear system:

```math
\begin{cases}
  2x + 3y - z = 5 \\
  4x + y + 2z = 6 \\
  -2x + 5y + 3z = 7
\end{cases}
```

### Step 1: Represent in Augmented Matrix Form
```math
\left[
\begin{array}{ccc|c}
  2 & 3 & -1 & 5 \\
  4 & 1 & 2 & 6 \\
  -2 & 5 & 3 & 7
\end{array}
\right]
```

### Step 2: Convert to Upper Triangular Form
- Divide the first row by 2 to obtain a leading 1.
- Use the first row to eliminate elements below the first pivot.
- Continue this process for the subsequent rows.

### Step 3: Solve Using Back Substitution
Once the matrix is in upper triangular form, the unknowns can be found by solving from the last row upwards.

## Applications of Gaussian Elimination
Gaussian elimination is widely used for:
- Finding the inverse of a matrix
- Computing the determinant of a matrix
- LU decomposition
- Applications in computer graphics, digital signal processing, and data science

## Conclusion
Gaussian elimination is a powerful tool in linear algebra that provides an efficient approach to solving important computational problems. Understanding and applying this method is essential for various mathematical and engineering disciplines.
