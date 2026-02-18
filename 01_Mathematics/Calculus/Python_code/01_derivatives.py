# Generated from: 01_derivatives.ipynb
# Converted at: 2026-02-18T08:41:24.517Z
# Next step (optional): refactor into modules & generate tests with RunCell
# Quick start: pip install runcell

# # Derivatives (Calculus for Machine Learning)
# 
# **Purpose:** Understand how change is measured and how derivatives drive optimization in ML.


# ## 1. What is a Derivative?
# A derivative measures the **rate of change** of a function with respect to its input.
# 
# In ML, derivatives tell us **how much the loss changes when parameters change**.


import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-5, 5, 100)
y = x ** 2

plt.figure()
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('f(x) = x^2')
plt.title('Function f(x) = x^2')
plt.show()

# ## 2. Geometric Interpretation
# The derivative at a point is the **slope of the tangent line** at that point.


x0 = 2
y0 = x0 ** 2
slope = 2 * x0

tangent_y = slope * (x - x0) + y0

plt.figure()
plt.plot(x, y, label='f(x) = x^2')
plt.plot(x, tangent_y, '--', label='Tangent at x=2')
plt.scatter([x0], [y0])
plt.legend()
plt.title('Derivative as Slope of Tangent')
plt.show()


# ## 3. Numerical vs Analytical Derivative
# Numerical derivative approximates change using small differences.
# Analytical derivative uses exact mathematical formulas.


def numerical_derivative(f, x, h=1e-5):
    return (f(x + h) - f(x - h)) / (2 * h)


f = lambda x: x ** 2
print('Numerical derivative at x=2:', numerical_derivative(f, 2))
print('Analytical derivative at x=2:', 2 * 2)

# ## 4. Why Derivatives Matter in ML
# - Used to minimize loss functions
# - Core of gradient descent
# - Foundation of backpropagation


# ## 5. Key Takeaways
# - Derivative = rate of change
# - Geometrically = slope of tangent
# - ML uses derivatives to learn parameters
# 
# **This notebook completes the derivative foundation for ML.**
