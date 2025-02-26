## Limit

### Definition

 Limit is the value that a function (or sequence) approaches as the argument (or index) approaches some value.

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


$\forall \epsilon > 0:$ take $\delta = \min{\{2c, \frac{\epsilon}{4c}\}}$
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

Derivative is the rate of change of a function with respect to a variable.

```math
f^{'}(x_0) = L \iff \lim_{h \to 0} \frac{f(x_0 + h) - f(x_0)}{h} = L \iff \lim_{x \to x_0} \frac{f(x) - f(x_0)}{x - x_0}
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
