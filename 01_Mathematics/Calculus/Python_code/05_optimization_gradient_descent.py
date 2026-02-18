# Generated from: 05_optimization_gradient_descent.ipynb
# Converted at: 2026-02-18T08:42:47.121Z
# Next step (optional): refactor into modules & generate tests with RunCell
# Quick start: pip install runcell

# # Optimization & Gradient Descent (Calculus for Machine Learning)
# 
# **Purpose:** Learn how gradients are used to minimize loss functions and train ML models.


# ## Optimization in Machine Learning
# Optimization means **finding parameters that minimize a loss function**.
# 
# Most ML training problems are optimization problems.


# ## Loss Function Example
# Consider a simple loss function:
# 
# $$ L(w) = w^2 $$
# 
# The minimum occurs where the gradient is zero.


import matplotlib.pyplot as plt
import numpy as np

w = np.linspace(-5, 5, 100)
loss = w ** 2

plt.figure()
plt.plot(w, loss)
plt.xlabel('w')
plt.ylabel('L(w)')
plt.title('Loss Function L(w) = w^2')
plt.show()


# ## Gradient Descent Idea
# Gradient descent updates parameters in the **opposite direction of the gradient**.
# 
# $$ w = w - \eta \frac{dL}{dw} $$
# 
# Where $\eta$ is the learning rate.


def gradient_descent(start, lr, steps):
    w = start
    history = []
    for _ in range(steps):
        grad = 2 * w
        w = w - lr * grad
        history.append(w)
    return history


path = gradient_descent(start=4.0, lr=0.1, steps=20)
print('Final w:', path[-1])

# ## Visualization of Gradient Descent
# Shows how parameters move toward the minimum.


plt.figure()
plt.plot(w, loss)
plt.scatter(path, [p ** 2 for p in path], color='red')
plt.xlabel('w')
plt.ylabel('L(w)')
plt.title('Gradient Descent Path')
plt.show()

# ## Learning Rate Effect
# - Too small → slow convergence
# - Too large → divergence
# - Proper value → fast convergence


# ## ML Connection
# - All optimizers (SGD, Adam) are based on gradient descent
# - Neural networks minimize loss using this principle


# ## Summary
# - Optimization = loss minimization
# - Gradient descent uses gradients to learn
# - Core algorithm behind ML training
