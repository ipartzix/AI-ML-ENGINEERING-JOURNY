# Generated from: 07_backpropagation_math.ipynb
# Converted at: 2026-02-18T08:43:10.648Z
# Next step (optional): refactor into modules & generate tests with RunCell
# Quick start: pip install runcell

# # Backpropagation (Math for Machine Learning)
# 
# **Purpose:** Understand how gradients are computed efficiently in neural networks using the chain rule.


# ## What is Backpropagation?
# Backpropagation is an algorithm to compute **gradients of the loss with respect to model parameters**.
# 
# It applies the **chain rule repeatedly** from output layer to input layer.


# ## Simple Neural Network Example
# Consider a single neuron:
# 
# $$ z = wx + b $$
# $$ \hat{y} = z $$
# $$ L = (y - \hat{y})^2 $$


def forward(x, w, b):
    z = w * x + b
    return z


def loss(y, y_hat):
    return (y - y_hat) ** 2


x, w, b, y = 2.0, 1.5, 0.5, 4.0
y_hat = forward(x, w, b)
print('Prediction:', y_hat)
print('Loss:', loss(y, y_hat))

# ## Backward Pass (Derivatives)
# Using chain rule:
# 
# $$ \frac{dL}{dw} = \frac{dL}{d\hat{y}} \cdot \frac{d\hat{y}}{dz} \cdot \frac{dz}{dw} $$
# $$ \frac{dL}{db} = \frac{dL}{d\hat{y}} \cdot \frac{d\hat{y}}{dz} \cdot \frac{dz}{db} $$


dL_dyhat = -2 * (y - y_hat)
dyhat_dz = 1
dz_dw = x
dz_db = 1

dL_dw = dL_dyhat * dyhat_dz * dz_dw
dL_db = dL_dyhat * dyhat_dz * dz_db

print('dL/dw:', dL_dw)
print('dL/db:', dL_db)

# ## Parameter Update (Gradient Descent)
# $$ w = w - \eta \frac{dL}{dw} $$
# $$ b = b - \eta \frac{dL}{db} $$


lr = 0.1
w_new = w - lr * dL_dw
b_new = b - lr * dL_db

print('Updated w:', w_new)
print('Updated b:', b_new)

# ## Computational Graph View
# Backpropagation works by moving backward through the computational graph, multiplying local gradients.


# ## Why Backpropagation Matters
# - Enables training of deep neural networks
# - Efficient: avoids redundant computations
# - Used in all modern DL frameworks (PyTorch, TensorFlow)


# ## Summary
# - Backpropagation = chain rule + gradients
# - Computes parameter updates efficiently
# - Core algorithm behind deep learning
# 
# **This notebook completes the calculus foundation for ML/DL.**
