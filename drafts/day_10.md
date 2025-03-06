# Backpropagation

Backpropagation is an algorithm used in training neural networks that computes the gradient of the loss function with respect to each weight by applying the chain rule.

It “propagates” errors from the output layer back to the input layer so that each weight can be adjusted in the direction that minimizes the overall error.

`Simple example`

# Newton method

The Newton Method is an iterative optimization technique used to find the roots of a function. In one-dimensional optimization, it updates the current estimate as

`Formula goes here`

As the goal of training is optimize the a function f(x), Newton method could be integrated to find the root of f'(x) as an approach to find min of f(x).

# Hessian

For multiple variable, Newton method could be generalized by using the Hessian matrix to calculate the parameters' updates.

`Formula goes here`

In order to evaluate the minimum of the function in this method, we calculate the eigenvalue of the Hessian matrix to decide if it is concave up, or concave down, or neither.
