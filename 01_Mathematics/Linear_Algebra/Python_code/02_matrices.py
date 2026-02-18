# Generated from: 02_matrices.ipynb
# Converted at: 2026-02-18T04:56:48.141Z
# Next step (optional): refactor into modules & generate tests with RunCell
# Quick start: pip install runcell

# # 02 — MATRICES (Linear Algebra for Machine Learning)
# 
# Authoritative reference notes for AI/ML.
# 


# ## 1. What is a Matrix?
# A **matrix** is a 2D arrangement of numbers in rows and columns.
# 
# Notation: A ∈ R^(m×n)


# ## 2. Types of Matrices
# - Row Matrix
# - Column Matrix
# - Square Matrix
# - Zero Matrix
# - Identity Matrix
# - Diagonal Matrix
# - Symmetric Matrix
# - Orthogonal Matrix


# ## 3. Matrix Operations
# ### Addition & Subtraction
# Conditions: Same dimensions
# 
# ### Scalar Multiplication
# Multiply each element by a scalar


import numpy as np

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

A + B, A - B, 2 * A

# ## 4. Matrix Multiplication
# Condition: (m×n)·(n×p)


A @ B

# ## 5. Transpose
# Aᵀ flips rows into columns


A.T

# ## 6. Determinant
# Indicates matrix invertibility


np.linalg.det(A)

# ## 7. Inverse Matrix
# A⁻¹ exists only if det(A) ≠ 0


np.linalg.inv(A)

# ## 8. Rank of Matrix
# Number of linearly independent rows/columns


np.linalg.matrix_rank(A)

# ## 9. Eigenvalues & Eigenvectors
# Core concept for PCA and transformations


vals, vecs = np.linalg.eig(A)
vals, vecs

# ## 10. Matrix Norms
# Measure magnitude


np.linalg.norm(A)

# ## 11. Matrices in Machine Learning
# - Dataset representation
# - Weight matrices
# - Transformations
# - Covariance matrices


# ## 12. Common Interview Notes
# - Matrix multiplication is NOT commutative
# - det(A)=0 ⇒ no inverse
# - Eigenvectors define directions, eigenvalues define magnitude
