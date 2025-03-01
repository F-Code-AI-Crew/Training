## Limit

### Definition

The limit of a function is the value that a function approaches as the argument approaches some value.

```math
\lim_{x \to c} f(x) = L \\
```

$\iff \forall \epsilon > 0: \exist \delta > 0:$

```math
\forall x: |x - c| < \delta \Rightarrow |f(x) - L| < \epsilon
```
### Properties
..

### Example

```math
\lim_{x \to c} x^2 = c^2
```


$\forall \epsilon > 0:$ take $\delta = \min{  \{2c, \frac{\epsilon}{4c}\}}$
```math
\lvert x - c \rvert < \delta < 2c \Rightarrow \lvert x + c \rvert < 4c
```

```math
\lvert x^2 - c^2 \rvert = \lvert x - c \rvert \lvert x + c \rvert < \delta  \cdot 4c < \frac{\epsilon}{4c} \cdot 4c = \epsilon
```

```math
\Rightarrow \lim_{x \to c} x^2 = c^2
```

## Derivative

### Definition

The **derivative** of a function is the **rate of change** of a function with respect to a variable.

```math
f^{'}(x_0) = \lim_{h \to 0} \frac{f(x_0 + h) - f(x_0)}{h} = \lim_{x \to x_0} \frac{f(x) - f(x_0)}{x - x_0}
```

### Properties
...

### Example
```math
(\sin x)^{'} = \lim_{h \to 0} \frac{\sin(x + h) - \sin x}{h} \\
= \lim_{h \to 0} \frac{\sin x \cos h + \cos x \sin h - \sin x}{h} \\
= \cos x \lim_{h \to 0} \frac{\sin h}{h} + \sin x \lim_{h \to 0} \frac{\cos h - 1}{h} \\
= \cos x + \sin x \cdot \lim_{h \to 0} \frac{\sin h}{h} \cdot \lim_{h \to 0} \frac{-\sin h}{\cos h + 1} \\
= \cos x
```

## Partial Derivative

### Definition

The **partial derivative** of a function of several variables is its **derivative with respect to one of those variables**, with the **others** held **constant**

```math
\frac{\partial f}{\partial x_1} (x_1, ..., x_n) = \lim_{h \to 0} \frac{f(x_1 + h, x_2, ..., x_n) - f(x_1, ..., x_n)}{h}
```

### Properties

...

### Example

```math
\frac{\partial}{\partial x} (x^2 + y^2) = \lim_{h \to 0} \frac{(x+ h)^2 + y^2 - x^2 - y^2}{h} = \lim_{h \to 0} \frac{(x + h)^2}{h} = 2x
```

## Gradient

### Definition
The **gradient** of a scalar-valued differentiable function f of several variables is the vector field (or vector-valued function) $\nabla f$ whose value at a point p gives **the direction and the rate of fastest increase**.

### Properties
...

### Example

```math
\nabla (x^2 + y^2) = [2x \text{  } 2y]^T
```
