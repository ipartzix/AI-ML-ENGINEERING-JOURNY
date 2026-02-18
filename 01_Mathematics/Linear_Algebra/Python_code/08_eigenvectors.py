# Generated from: 08_eigenvectors.ipynb
# Converted at: 2026-02-18T04:59:02.051Z
# Next step (optional): refactor into modules & generate tests with RunCell
# Quick start: pip install runcell

# # 08 — Eigenvalues & Eigenvectors
# 
# Foundational concept for PCA, transformations, and deep learning intuition.


# ## 1. What is an Eigenvector?
# For a square matrix A, a non-zero vector v is an **eigenvector** if:
# 
# A v = λ v
# 
# Where λ is the **eigenvalue**.


# ### Interpretation
# - Eigenvectors indicate **directions** that do not change under transformation
# - Eigenvalues indicate **scaling factor** along that direction


# ## 2. Eigenvalue Equation
# (A − λI)v = 0
# 
# Non-trivial solution exists only if:
# 
# |A − λI| = 0


import numpy as np

A = np.array([[2, 1],
              [1, 2]])

values, vectors = np.linalg.eig(A)
values, vectors

# ## 3. Properties of Eigenvalues
# - Defined only for square matrices
# - Matrix can have real or complex eigenvalues
# - Symmetric matrices → real eigenvalues


# ## 4. Geometric Intuition
# Eigenvectors remain on the same line after transformation.
# Only their magnitude changes.


# ## 5. Eigenvectors and Linear Independence
# - Eigenvectors corresponding to distinct eigenvalues are linearly independent


# ## 6. Diagonalization
# If A has n independent eigenvectors:
# 
# A = PDP⁻¹
# 
# Where D is diagonal matrix of eigenvalues


P = vectors
D = np.diag(values)
np.allclose(A, P @ D @ np.linalg.inv(P))

# ## 7. Eigenvalues in Machine Learning
# - PCA (principal directions)
# - Covariance matrix analysis
# - Stability of optimization
# - Graph Laplacians
# - Recommendation systems


# ## 8. Eigenvalues vs Singular Values
# - Eigenvalues apply to square matrices
# - Singular values apply to all matrices
# - SVD is more numerically stable


# ## 9. Common Interview Facts
# - λ = 0 ⇒ matrix is singular
# - Trace = sum of eigenvalues
# - Determinant = product of eigenvalues


# ## 10. Summary
# - Eigenvectors define invariant directions
# - Eigenvalues define strength of transformation
# - Core tool behind dimensionality reduction
