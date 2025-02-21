# Vector

- [x] Mathematics definition
- [x] Vector operation
- [x] Vector operation with matrix

Intuitively, a vector represents both magnitude and direction. They not only serve as basic elements in geometry but are also the carriers of information in many data-driven fields, including AI. Vectors are commonly used to represent data samples. Consider a dataset where each sample represents a house, it might include the number of bedrooms, number of levels, area, age, and price.

Formally, a vector is an element of a vector space - a set equipped with two operations:
- Addition: Combining two vectors to get another vector.
- Scalar Multiplication: Scaling a vector by a real number

# Vector space

A vector space $V$ is a collection of vectors that satisfy several axioms for vector addition and scalar multiplication. Some popular examples of vector spaces might include:
- $R^n$ - The set of all $n$ - dimentional real vectors
- $M_{m \times n}$ - The set of all matrices with the size of $m \times n$
- $P_n$ - The set of all polynomials of degree $\le n$

A subspace is a subset $U \subseteq  V$ that is itself a vector space.

Overall, talking about linear algebra, it is about vectors and how to manipulate them in their spaces.

Further discuss
- [ ] Basic algebraic structure
- [ ] Span and basis

# Linear transformation
- [x] Mathematics definition
- [x] Linear transformation with matrix
- [x] Common transformation

A mapping $\Phi: V \rightarrow W$ between vector spaces is called a linear transformation or linear mapping if it preserves vector addition and scalar multiplication:
- $\Phi(x + y) = \Phi(x) + \Phi(y)$
- $\Phi(\lambda x) = \lambda \Phi(x)$ for all $x, y \in V$ and $\lambda \in \mathbb{R}$.

Examples of linear transformation:
- Rotation and reflection
- Scailing
- Project a vector onto a line or plane

Further discuss
- [ ] Matrix representation of linear transformation & in change of basis
- [ ] Image and kernel

# [Làm sau] Introduction to SVMs

- [ ] Brief introduction to SVMs
- [ ] Vector and linear transformation in context of SVMs
- [ ] Demonstration

# Resources

- [Latex notes](https://www.overleaf.com/read/wbxsxkbxqtjq#bd1c10) vì markdown viết ma trận gớm quá

# References

- [Deisenroth, 2020, MML](https://mml-book.com/)
