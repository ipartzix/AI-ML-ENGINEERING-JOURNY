# Generated from: 05_norms_distance.ipynb
# Converted at: 2026-02-18T04:57:39.235Z
# Next step (optional): refactor into modules & generate tests with RunCell
# Quick start: pip install runcell

# 
# # 05 — Vector Norms & Distance (Linear Algebra for AI/ML)
# 
# This notebook covers **vector norms and distance measures**, which are critical for
# optimization, similarity, clustering, regularization, and ML algorithms.
# 


# 
# ## 1. What is a Norm?
# 
# A **norm** measures the *magnitude* or *length* of a vector.
# 
# For a vector **x = [x₁, x₂, ..., xₙ]**, a norm returns a **non-negative scalar**.
# 


# 
# ## 2. L2 Norm (Euclidean Norm)
# 
# Formula:
# ‖x‖₂ = √(x₁² + x₂² + ... + xₙ²)
# 
# Most commonly used norm in ML.
# 


import numpy as np

x = np.array([3, 4])
np.linalg.norm(x)

#
# ## 3. L1 Norm (Manhattan Norm)
# 
# Formula:
# ‖x‖₁ = |x₁| + |x₂| + ... + |xₙ|
# 
# Used in **L1 regularization (Lasso)** → sparsity.
# 


np.linalg.norm(x, ord=1)

#
# ## 4. L∞ Norm (Max Norm)
# 
# Formula:
# ‖x‖∞ = max(|x₁|, |x₂|, ..., |xₙ|)
# 
# Used in robustness analysis.
# 


np.linalg.norm(x, ord=np.inf)

#
# ## 5. General p-Norm
# 
# ‖x‖ₚ = ( Σ |xᵢ|ᵖ )^(1/p)
# 


# p = 3 norm
np.linalg.norm(x, ord=3)

#
# ## 6. Distance Between Two Vectors
# 
# Distance measures *how far apart* two vectors are.
# 


# 
# ### Euclidean Distance (L2 Distance)
# 
# d(x, y) = ‖x − y‖₂
# 


x = np.array([1, 2])
y = np.array([4, 6])

np.linalg.norm(x - y)

#
# ### Manhattan Distance (L1 Distance)
# 
# d(x, y) = ‖x − y‖₁
# 


np.linalg.norm(x - y, ord=1)

#
# ### Chebyshev Distance (L∞ Distance)
# 


np.linalg.norm(x - y, ord=np.inf)

#
# ## 7. Norms & Distance in Machine Learning
# 
# Applications:
# - KNN → distance metrics
# - K-Means → Euclidean distance
# - Gradient descent → step size magnitude
# - Regularization:
#     • L1 → sparsity
#     • L2 → weight decay
# 


# 
# ## 8. Example: Distance-Based Classification (KNN intuition)
# 


# Simple distance comparison
point = np.array([2, 3])
class_A = np.array([1, 2])
class_B = np.array([6, 7])

dist_A = np.linalg.norm(point - class_A)
dist_B = np.linalg.norm(point - class_B)

dist_A, dist_B

#
# ## 9. Common Mistakes
# 
# ❌ Mixing norm and distance  
# ❌ Forgetting absolute values in L1  
# ❌ Assuming all distances behave the same  
# 
# Choose metrics based on problem nature.
# 


# 
# ## 10. Summary
# 
# - Norm → magnitude of a vector
# - Distance → separation between vectors
# - L1, L2, L∞ are most important
# - Backbone of clustering, KNN, optimization
#
