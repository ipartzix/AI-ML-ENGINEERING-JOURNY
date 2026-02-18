# Generated from: 06_projections.ipynb
# Converted at: 2026-02-18T04:58:11.910Z
# Next step (optional): refactor into modules & generate tests with RunCell
# Quick start: pip install runcell

# # 06 — Vector Projections (Linear Algebra for AI/ML)


# 
# ## What is Vector Projection?
# 
# Projection measures how much of vector **a** lies in the direction of **b**.
# 


# 
# ## Formula
# 
# proj_b(a) = (a · b / b · b) b ,  b ≠ 0
# 


import numpy as np

a = np.array([3, 4])
b = np.array([1, 0])
(np.dot(a, b) / np.dot(b, b)) * b

#
# ## Unit Vector Form
# 
# If u = b / ||b|| then proj_b(a) = (a · u)u
# 


b = np.array([3, 4])
u = b / np.linalg.norm(b)
a = np.array([5, 2])
(np.dot(a, u)) * u

#
# ## Least Squares Interpretation
# 
# Linear regression predictions are projections.
# 


X = np.array([[1], [2], [3]])
y = np.array([2, 2.5, 3])
P = X @ np.linalg.inv(X.T @ X) @ X.T
P @ y

#
# ## Summary
# 
# Projection is central to regression, PCA, and ML geometry.
#
