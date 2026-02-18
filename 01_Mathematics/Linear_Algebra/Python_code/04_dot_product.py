# Generated from: 04_dot_product.ipynb
# Converted at: 2026-02-18T04:57:15.127Z
# Next step (optional): refactor into modules & generate tests with RunCell
# Quick start: pip install runcell

# 
# # 04 — Dot Product (Linear Algebra for AI/ML)
# 
# This notebook is a **core mathematical reference** for dot product.
# Dot product is fundamental to similarity, projections, ML models, and neural networks.
# 


# 
# ## 1. What is Dot Product?
# 
# The **dot product** (also called scalar product) of two vectors produces a **single scalar value**.
# 
# For vectors **a** and **b** of same dimension:
# 
# a · b = a₁b₁ + a₂b₂ + ... + aₙbₙ
# 


# 
# ## 2. Condition for Dot Product
# 
# Dot product is defined **only if both vectors have the same dimension**.
# 


import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print("a shape:", a.shape)
print("b shape:", b.shape)

#
# ## 3. Manual Dot Product Calculation
# 


dot_manual = sum(a[i] * b[i] for i in range(len(a)))
dot_manual

#
# ## 4. Dot Product Using NumPy
# 


np.dot(a, b)

a @ b

#
# ## 5. Geometric Interpretation
# 
# a · b = |a||b|cos(θ)
# 
# - If dot product > 0 → acute angle
# - If dot product = 0 → orthogonal vectors
# - If dot product < 0 → obtuse angle
# 


# Orthogonal vectors example
v1 = np.array([1, 0])
v2 = np.array([0, 1])

np.dot(v1, v2)

#
# ## 6. Dot Product as Projection
# 
# Projection of vector **a** onto **b**:
# 
# proj_b(a) = (a · b / b · b) * b
# 


a = np.array([3, 4])
b = np.array([1, 0])

projection = (np.dot(a, b) / np.dot(b, b)) * b
projection

#
# ## 7. Dot Product in Machine Learning
# 
# Dot product is everywhere in ML:
# 
# - Linear Regression:  y = w · x
# - Logistic Regression
# - Cosine similarity
# - Attention mechanism (Q · K)
# - Neural network neurons
# 
# A neuron = dot product + bias + activation
# 


# 
# ## 8. Example: Single Neuron Computation
# 


# Inputs and weights
x = np.array([0.5, 1.5, -0.5])
w = np.array([0.2, -0.4, 0.6])
b = 0.1

z = np.dot(w, x) + b
z

#
# ## 9. Common Mistakes
# 
# ❌ Confusing dot product with element-wise multiplication  
# ❌ Using vectors of different dimensions  
# ❌ Ignoring geometric meaning  
# 
# Always check **dimensions and intent**.
# 


# 
# ## 10. Summary
# 
# - Dot product → scalar output
# - Measures similarity & alignment
# - Foundation of ML and DL models
# - Used in projections, similarity, and neurons
#
