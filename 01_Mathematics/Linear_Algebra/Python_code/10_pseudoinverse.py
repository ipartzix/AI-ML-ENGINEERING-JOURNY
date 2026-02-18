# Generated from: 10_pseudoinverse.ipynb
# Converted at: 2026-02-18T04:59:34.201Z
# Next step (optional): refactor into modules & generate tests with RunCell
# Quick start: pip install runcell

# # 10 — Moore–Penrose Pseudoinverse
# 
# Essential concept for least squares, regression, and modern ML optimization.


# ## 1. Why Pseudoinverse?
# For non-square or singular matrices, normal inverse does not exist.
# The **pseudoinverse** provides a generalized inverse.


# ## 2. Definition
# The Moore–Penrose pseudoinverse of matrix A is denoted as:
# 
# A⁺
# 
# It satisfies four Penrose conditions ensuring uniqueness.


# ## 3. Connection with SVD
# If:
# A = U Σ Vᵀ
# 
# Then:
# A⁺ = V Σ⁺ Uᵀ
# 
# Where Σ⁺ is obtained by taking reciprocal of non-zero singular values.


import numpy as np

A = np.array([[1, 2],
              [3, 4],
              [5, 6]])

A_pinv = np.linalg.pinv(A)
A_pinv

# ## 4. Least Squares Solution
# For Ax = b (overdetermined system):
# 
# x = A⁺ b


b = np.array([7, 8, 9])
x = A_pinv @ b
x

# ## 5. Relation to Normal Equation
# If A has full column rank:
# 
# A⁺ = (AᵀA)⁻¹ Aᵀ


np.allclose(A_pinv, np.linalg.inv(A.T @ A) @ A.T)

# ## 6. Why ML Uses Pseudoinverse
# - Linear regression closed-form solution
# - Handles non-square data matrices
# - Stable under noise
# - Used internally with SVD


# ## 7. Numerical Stability
# Pseudoinverse avoids instability caused by near-zero eigenvalues.


# ## 8. Interview Facts
# - Always exists
# - Reduces to inverse if matrix is square and full rank
# - Computed using SVD in practice


# ## 9. Summary
# The pseudoinverse is a universal inverse enabling solutions to real-world ML systems.
