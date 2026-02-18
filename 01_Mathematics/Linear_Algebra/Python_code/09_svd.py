# Generated from: 09_svd.ipynb
# Converted at: 2026-02-18T04:59:12.971Z
# Next step (optional): refactor into modules & generate tests with RunCell
# Quick start: pip install runcell

# # 09 — Singular Value Decomposition (SVD)
# 
# Authoritative notes for AI/ML, data compression, and dimensionality reduction.


# ## 1. Definition
# For any matrix A ∈ ℝ^(m×n):
# 
# A = U Σ Vᵀ
# 
# - U: left singular vectors (orthonormal)
# - Σ: diagonal matrix of singular values
# - Vᵀ: right singular vectors (orthonormal)


# ## 2. Key Properties
# - SVD exists for **any** matrix
# - Singular values ≥ 0
# - Works for square and rectangular matrices


import numpy as np

A = np.array([[3, 1, 1],
              [-1, 3, 1]])

U, S, Vt = np.linalg.svd(A)
U, S, Vt

# ## 3. Geometric Interpretation
# Transformation = Rotation → Scaling → Rotation


# ## 4. Relation with Eigenvalues
# Singular values = √(eigenvalues of AᵀA)


np.sqrt(np.linalg.eigvals(A.T @ A))

# ## 5. Rank using SVD
# Rank = number of non-zero singular values


np.linalg.matrix_rank(A)

# ## 6. Low-Rank Approximation
# Used in PCA, noise reduction, compression


k = 1
Ak = U[:, :k] @ np.diag(S[:k]) @ Vt[:k, :]
Ak

# ## 7. ML Applications
# - PCA
# - Recommendation systems
# - Image compression
# - Latent Semantic Analysis


# ## 8. Interview Facts
# - SVD always exists
# - Zero singular value ⇒ rank deficient
# - More stable than eigen decomposition


# ## 9. Summary
# SVD is the backbone of dimensionality reduction and modern ML pipelines.
