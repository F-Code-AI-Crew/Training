# Linear Algebra: Bases, Eigenvalues, and Eigenvectors

## Bases

### Definition
- A **basis** of a vector space is a set of vectors that is both:
  - **Linearly independent:** No vector in the set can be written as a linear combination of the others.
  - **Spanning:** Every vector in the space can be expressed as a linear combination of the basis vectors.

### Properties
- **Uniqueness of Representation:** Every vector in the space has a unique representation in terms of the basis.
- **Dimension:** The number of vectors in any basis of the space is the dimension of the vector space.

### Example
For the vector space $\R^2$, one common basis is:
```math
e_1 = \begin{bmatrix} 1 \\ 0 \end{bmatrix}, e_2 = \begin{bmatrix} 0 \\ 1 \end{bmatrix}
```
Any vector $\mathbf{v} = \begin{bmatrix} x \\ y \end{bmatrix}$ in $\R^2$ can be written as:
```math
\mathbf{v} = x\mathbf{e}_1 + y\mathbf{e}_2.
```

## Eigenvalues and Eigenvectors

### Definitions
Given a *square* matrix $\mathbf{A}$ of size $n \times n$. A nonzero vector $\mathbf{v}$ is called an **eigenvector** of $\mathbf{A}$ if there exists a scalar $\lambda$ (the **eigenvalue**) such that:
```math
  \mathbf{A}\mathbf{v} = \lambda \mathbf{v}.
```

### Geometric Interpretation
- **Eigenvectors** point in directions that remain invariant (or reverse direction) under the transformation defined by \(\mathbf{A} \).
- **Eigenvalues** describe the factor by which the eigenvector is scaled:
  - If $|\lambda| > 1$, the vector is stretched.
  - If $|\lambda| < 1$, it is shrunk.
  - If $\lambda$ is negative, the vector’s direction is reversed.

### Finding Eigenvalues and Eigenvectors

1. **Characteristic Equation:**  

    To find the eigenvalues, solve:

    ```math
    \det(\mathbf{A} - \lambda \mathbf{I}) = 0
    ```

2. **Eigenvectors:**  

    For each eigenvalue $\lambda$, solve:

    ```math
    (\mathbf{A} - \lambda \mathbf{I}) \mathbf{v} = \mathbf{0}
    ```

    to find the corresponding eigenvectors.

    ### Example

    Consider the matrix

    ```math
    \mathbf{A} = \begin{bmatrix} 4 & 1 \\ 2 & 3 \end{bmatrix}.
    ```

1. **Find Eigenvalues:**  

    The characteristic polynomial is

    ```math
    \det \left( \begin{bmatrix} 4-\lambda & 1 \\ 2 & 3-\lambda \end{bmatrix} \right) = (4-\lambda)(3-\lambda) - 2 = \lambda^2 - 7\lambda + 10.
    ```

    so the eigenvalues are $\lambda_1 = 2$ and $\lambda_2 = 5$.

2. **Find Eigenvectors:**
    - For $\lambda_1 = 2$:

    ```math
    (\mathbf{A} - 2\mathbf{I})v_1 = \mathbf{0} \\
    \Rightarrow\begin{bmatrix} 2 & 1 \\ 2 & 1 \end{bmatrix} \mathbf{v_1} = \mathbf{0} \\
    \Rightarrow v_1 = \begin{bmatrix} 1 \\ -2 \end{bmatrix}
    ```

    - For $\lambda_1 = 5$:

    ```math
    (\mathbf{A} - 5\mathbf{I})v_2 = \mathbf{0} \\
    \Rightarrow\begin{bmatrix} -1 & 1 \\ 2 & -2 \end{bmatrix} \mathbf{v_2} = \mathbf{0} \\
    \Rightarrow v_2 = \begin{bmatrix} 1 \\ 1 \end{bmatrix}
    ```

### Relationship Between Bases and Eigen-Decomposition

- When a matrix $\mathbf{A}$ has $n$ linearly independent eigenvectors, these eigenvectors form a basis for $\mathbb{R}^n$. This is often called an **eigenbasis**.
- With an eigenbasis, the matrix $\mathbf{A}$ can be diagonalized:

```math
\mathbf{A} = \mathbf{Q} \mathbf{\Lambda} \mathbf{Q}^{-1},
```

    - $\mathbf{\Lambda}$ is a diagonal matrix whose diagonal entries are the corresponding eigenvalues.

- This decomposition simplifies many matrix computations, such as computing matrix powers or exponentials.

### Additional properties

Let $\mathbf{A}$ be an arbitrary $n \times n$ matrix of complex numbers with eigenvalues $\lambda_1$, ..., $\lambda_n$

- ```math
tr(\mathbf(A)) = \sum_{i = 1}^n a_{ii} = \sum_{i = 1}^n \lambda_i
```

- ```math
det(\mathbf{A}) = \prod_{i = 1}^n \lambda_i
```
- The eigenvalues of $\mathbf{A}^k$ for $k \in N^*$ are $\lambda_1^k$, ..., $\lambda_n^k$
- $\mathbf{A}$ is invertible $\iff$ $\lambda_i \ne 0$ for all $i$
- If $\mathbf{A}$ is invertible, then the eigenvalues of $\mathbf{A}^{-1}$ are $\frac{1}{\lambda_1}$, ..., $\frac{1}{\lambda_n}$
