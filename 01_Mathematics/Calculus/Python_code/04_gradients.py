# Generated from: 04_gradients.ipynb
# Converted at: 2026-02-18T08:42:31.370Z
# Next step (optional): refactor into modules & generate tests with RunCell
# Quick start: pip install runcell

# # Gradients (Calculus for Machine Learning)
# 
# **Purpose:** Understand gradients as the core mathematical object used to optimize ML and DL models.


# ## Gradient Definition
# For a multivariable function, the gradient is a vector of partial derivatives.
# 
# $$ \nabla f = [ \partial f/\partial x, \partial f/\partial y ] $$


# ## Example Function
# $$ f(x, y) = x^2 + y^2 $$


def gradient(x, y):
    return [2 * x, 2 * y]


print('Gradient at (1,2):', gradient(1, 2))

# ## Geometric Interpretation
# The gradient points in the direction of the steepest increase of the function.


import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-4, 4, 20)
y = np.linspace(-4, 4, 20)
X, Y = np.meshgrid(x, y)
U = 2 * X
V = 2 * Y

plt.figure()
plt.quiver(X, Y, U, V)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Gradient Field of f(x,y)=x^2+y^2')
plt.show()

# ## Gradient in ML
# - Used to update model parameters
# - Computed via backpropagation
# - Drives optimization algorithms


# ## Summary
# - Gradient is a vector of partial derivatives
# - Indicates direction and rate of change
# - Core concept in ML optimization
