# Generated from: 12_rank_independence.ipynb
# Converted at: 2026-02-18T05:00:01.430Z
# Next step (optional): refactor into modules & generate tests with RunCell
# Quick start: pip install runcell

# # 07-1 — Rank & Linear Independence
# 
# Core Linear Algebra concepts for AI/ML and Core CS.


# ## 1. Rank of a Matrix
# The **rank** of a matrix is the maximum number of **linearly independent** rows or columns.
# 
# Formally:
# Rank(A) = dimension of column space = dimension of row space.


# ### Why Rank Matters in ML
# - Determines if data is redundant
# - Used in feature selection
# - Decides invertibility
# - Critical in PCA, regression, optimization


import numpy as np

A = np.array([[1, 2, 3],
              [2, 4, 6],
              [1, 1, 1]])

np.linalg.matrix_rank(A)

# ## 2. Linear Dependence vs Independence
# A set of vectors {v₁, v₂, ..., vₙ} is:
# - **Linearly Independent** if only trivial solution exists
# - **Linearly Dependent** if one vector can be written as a combination of others


# ### Mathematical Definition
# c₁v₁ + c₂v₂ + ... + cₙvₙ = 0
# 
# If all cᵢ = 0 → Independent
# Else → Dependent


v1 = np.array([1, 2])
v2 = np.array([2, 4])

np.linalg.matrix_rank(np.column_stack((v1, v2)))

# ## 3. Rank and Linear Independence Relationship
# - Rank = number of linearly independent columns
# - If rank < number of columns → dependence exists
# - Full rank matrix → no redundancy


# ## 4. Row Rank vs Column Rank
# Important theorem:
# 
# **Row Rank = Column Rank**
# 
# This holds for all matrices.


# ## 5. Full Rank Matrix
# - Square matrix: rank = n
# - Rectangular matrix:
#   - Full column rank: rank = number of columns
#   - Full row rank: rank = number of rows


B = np.eye(3)
np.linalg.matrix_rank(B)

# ## 6. Rank and Determinant
# - det(A) ≠ 0 → full rank → invertible
# - det(A) = 0 → rank deficient → non-invertible


np.linalg.det(B)

# ## 7. Rank in Machine Learning Context
# - Feature matrices
# - Covariance matrices
# - Weight matrices
# - Gradient descent stability
# - Data leakage detection


# ## 8. Common Interview Facts
# - Rank ≤ min(rows, columns)
# - Rank reveals redundancy
# - Rank invariant under transpose
# - PCA reduces rank intentionally


# ## 9. Summary
# - Rank measures independent information
# - Linear independence prevents redundancy
# - ML models fail on rank-deficient data
