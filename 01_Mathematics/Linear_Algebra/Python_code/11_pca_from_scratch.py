# Generated from: 11_pca_from_scratch.ipynb
# Converted at: 2026-02-18T04:59:44.774Z
# Next step (optional): refactor into modules & generate tests with RunCell
# Quick start: pip install runcell

# # 11 — PCA from Scratch
# 
# Complete step-by-step Principal Component Analysis with mathematical intuition and NumPy implementation.


# ## 1. What is PCA?
# PCA is an unsupervised dimensionality reduction technique.
# 
# Goals:
# - Reduce dimensionality
# - Preserve maximum variance
# - Remove redundancy


# ## 2. Mathematical Idea
# PCA finds orthogonal directions (principal components) that maximize variance.
# These directions are eigenvectors of the covariance matrix.


import numpy as np

X = np.array([[2.5, 2.4],
              [0.5, 0.7],
              [2.2, 2.9],
              [1.9, 2.2],
              [3.1, 3.0],
              [2.3, 2.7],
              [2.0, 1.6],
              [1.0, 1.1],
              [1.5, 1.6],
              [1.1, 0.9]])

# ## 3. Step 1: Mean Centering


X_mean = np.mean(X, axis=0)
X_centered = X - X_mean
X_mean

# ## 4. Step 2: Covariance Matrix


cov_matrix = np.cov(X_centered.T)
cov_matrix

# ## 5. Step 3: Eigen Decomposition


eig_vals, eig_vecs = np.linalg.eig(cov_matrix)
eig_vals, eig_vecs

# ## 6. Step 4: Sort Eigenvalues


idx = np.argsort(eig_vals)[::-1]
eig_vals = eig_vals[idx]
eig_vecs = eig_vecs[:, idx]
eig_vals

# ## 7. Step 5: Projection


k = 1
W = eig_vecs[:, :k]
X_pca = X_centered @ W
X_pca[:5]

# ## 8. Explained Variance


explained_variance = eig_vals / np.sum(eig_vals)
explained_variance

# ## 9. PCA using SVD (Preferred in Practice)


U, S, Vt = np.linalg.svd(X_centered)
X_pca_svd = X_centered @ Vt.T[:, :1]
X_pca_svd[:5]

# ## 10. Interview & ML Facts
# - PCA is unsupervised
# - PCA maximizes variance
# - PCA reduces rank intentionally
# - SVD-based PCA is numerically stable


# ## 11. Summary
# PCA projects data onto directions of maximum variance for efficient representation.
