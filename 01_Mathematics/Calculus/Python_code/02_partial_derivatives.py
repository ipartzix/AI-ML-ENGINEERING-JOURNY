# Generated from: 02_partial_derivatives.ipynb
# Converted at: 2026-02-18T08:41:55.035Z
# Next step (optional): refactor into modules & generate tests with RunCell
# Quick start: pip install runcell

# # Partial Derivatives (Calculus for Machine Learning)
# 
# **Purpose:** Measure change with respect to one variable while others remain constant.


# ## Partial Derivative Definition
# A partial derivative applies to multivariable functions and measures how the output changes when only one variable changes.
# 
# Machine learning models rely on partial derivatives to update each parameter.


# ## Example Function
# $$ f(x, y) = x^2 + y^2 $$


def f(x, y):
    return x ** 2 + y ** 2


def dfdx(x, y):
    return 2 * x


def dfdy(x, y):
    return 2 * y


print('∂f/∂x at (1,2):', dfdx(1, 2))
print('∂f/∂y at (1,2):', dfdy(1, 2))

# ## Geometric Interpretation
# Partial derivatives represent slopes of a surface in one direction.


import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-4, 4, 50)
y = np.linspace(-4, 4, 50)
X, Y = np.meshgrid(x, y)
Z = X ** 2 + Y ** 2

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, alpha=0.7)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('f(x,y)')
ax.set_title('Surface: f(x,y) = x^2 + y^2')
plt.show()


# ## Numerical Partial Derivatives
# Used when analytical derivatives are difficult to compute.


def numerical_dfdx(f, x, y, h=1e-5):
    return (f(x + h, y) - f(x - h, y)) / (2 * h)


def numerical_dfdy(f, x, y, h=1e-5):
    return (f(x, y + h) - f(x, y - h)) / (2 * h)


print('Numerical ∂f/∂x at (1,2):', numerical_dfdx(f, 1, 2))
print('Numerical ∂f/∂y at (1,2):', numerical_dfdy(f, 1, 2))

# ## ML Connection
# - Each parameter update uses a partial derivative
# - Gradients are collections of partial derivatives
# - Backpropagation depends on partial derivatives


# ## Summary
# - Partial derivatives apply to multivariable functions
# - They measure directional change
# - They are foundational for optimization in ML
