# Generated from: 03_chain_rule.ipynb
# Converted at: 2026-02-18T08:42:11.726Z
# Next step (optional): refactor into modules & generate tests with RunCell
# Quick start: pip install runcell

# # Chain Rule (Calculus for Machine Learning)
# 
# **Purpose:** Understand how derivatives flow through composed functions, which is the mathematical backbone of backpropagation.


# ## Chain Rule Concept
# The chain rule is used when a function is composed of multiple functions.
# 
# If:
# $$ y = f(g(x)) $$
# Then:
# $$ \frac{dy}{dx} = \frac{dy}{dg} \cdot \frac{dg}{dx} $$
# 
# In ML, models are compositions of many functions (layers).


# ## Simple Example
# Consider:
# $$ y = (3x + 1)^2 $$


import numpy as np


def g(x):
    return 3 * x + 1


def f(u):
    return u ** 2


def dy_dx(x):
    return 2 * (3 * x + 1) * 3


print('dy/dx at x=2:', dy_dx(2))

# ## Computational Graph View
# The chain rule can be visualized as a flow of derivatives through a graph.
# 
# Each node passes gradients backward to the previous node.


import matplotlib.pyplot as plt

x = np.linspace(-3, 3, 100)
y = (3 * x + 1) ** 2

plt.figure()
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('y = (3x + 1)^2')
plt.show()

# ## Multivariable Chain Rule
# For multivariable functions:
# 
# $$ z = f(x, y), \quad x = g(t), \quad y = h(t) $$
# 
# $$ \frac{dz}{dt} = \frac{\partial z}{\partial x}\frac{dx}{dt} + \frac{\partial z}{\partial y}\frac{dy}{dt} $$
# 
# This form is heavily used in neural networks.


# ## Chain Rule in Neural Networks
# - Each layer applies a function
# - Gradients flow backward using the chain rule
# - Enables efficient training of deep models


# ## Summary
# - Chain rule handles composed functions
# - Core mechanism behind backpropagation
# - Without chain rule, deep learning is impossible
# 
# **This notebook completes the chain rule foundation for ML.**
