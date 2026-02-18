# Generated from: 01_vectors.ipynb
# Converted at: 2026-02-18T04:54:48.299Z
# Next step (optional): refactor into modules & generate tests with RunCell
# Quick start: pip install runcell

# # 01 — VECTORS (Linear Algebra for Machine Learning)
# 
# This notebook is  **authoritative study note** for vectors. Use YouTube only to *support* this document, not replace it.
# 
# ---
# 
# ## 1. What is a Vector?
# 
# A **vector** is an ordered collection of numbers representing a point, direction, or feature list.
# 
# In Machine Learning:
# 
# * One data sample = **one vector**
# * Model weights = **vector**
# * Prediction = **dot product of vectors**
# 
# Mathematically: (\mathbf{x} = [x_1, x_2, ..., x_n]^T)
# 
# Geometric view (2D):
# 
# ```
# ^ y
# |        ● (x1, x2)
# |      ↗
# |    ↗  vector
# |  ↗
# +------------------> x
# ```
# 
# ---
# 
# ## 2. Scalars vs Vectors
# 
# * **Scalar**: single number (temperature, learning rate)
# * **Vector**: ordered list (features, embeddings)
# 
# Example:
# 
# * Scalar: (\alpha = 0.01)
# * Vector: (\mathbf{x} = [2, -1, 4])
# 
# ---
# 
# ## 3. Vector Dimensions
# 
# The **dimension** of a vector is the number of components.
# 
# * 2D → (\mathbb{R}^2)
# * 3D → (\mathbb{R}^3)
# * ML data → (\mathbb{R}^n) (high-dimensional)
# 
# Example:
# 
# * Word-count vector for 10,000 words → (\mathbb{R}^{10000})
# 
# ---
# 
# ## 4. Zero Vector and Unit Vector
# 
# ### Zero Vector
# 
# A vector with all components zero. (\mathbf{0} = [0, 0, 0])
# 
# * Has no direction
# * Acts as additive identity
# 
# ### Unit Vector
# 
# A vector with magnitude = 1. (\hat{v} = \frac{\mathbf{v}}{||\mathbf{v}||})
# 
# Graphical intuition:
# 
# ```
# Original vector:  ------>
# Unit vector:      -->
# (same direction, length = 1)
# ```
# 
# Used in:
# 
# * Normalization
# * Cosine similarity
# * Gradient direction
# 
# ---
# 
# ## 5. Norm (Magnitude) of a Vector
# 
# The **norm** measures vector length.
# 
# ### L2 Norm (Euclidean norm)
# 
# (||\mathbf{x}||_2 = \sqrt{x_1^2 + x_2^2 + ... + x_n^2})
# 
# ### L1 Norm
# 
# (||\mathbf{x}||_1 = |x_1| + |x_2| + ... + |x_n|)
# 
# ML meaning:
# 
# * L2 → smooth optimization
# * L1 → sparsity (feature selection)
# 
# ---
# 
# ## 6. Distance Between Two Vectors
# 
# Distance = norm of their difference. (d(\mathbf{x}, \mathbf{y}) = ||\mathbf{x} - \mathbf{y}||_2)
# 
# Graphical idea:
# 
# ```
# ● x
# |\
# | \
# |  \  distance
# |   \
# ●----● y
# ```
# 
# Used in:
# 
# * KNN
# * Clustering
# * Similarity search
# 
# ---
# 
# ## 7. Sparsity in Vectors
# 
# A **sparse vector** has many zeros.
# 
# Example (bag-of-words): ([0, 0, 3, 0, 0, 1, 0, ...])
# 
# Why it matters:
# 
# * Saves memory
# * Faster computation
# * Common in NLP & recommender systems
# 
# ---
# 
# ## 8. Vector Addition
# 
# (\mathbf{a} + \mathbf{b} = [a_1+b_1, a_2+b_2, ...])
# 
# Graphical intuition (head-to-tail):
# 
# ```
# ----> a
#      ----> b
# --------------> a+b
# ```
# 
# ---
# 
# ## 9. Scalar Multiplication
# 
# (c\mathbf{v} = [cv_1, cv_2, ...])
# 
# Effect:
# 
# * Scales magnitude
# * Keeps or flips direction
# 
# ---
# 
# ## 10. Dot Product (Most Important)
# 
# (\mathbf{a} \cdot \mathbf{b} = a_1b_1 + a_2b_2 + ...)
# 
# Geometric meaning: (\mathbf{a} \cdot \mathbf{b} = ||a|| ||b|| \cos(\theta))
# 
# Interpretations:
# 
# * Measures similarity
# * Measures alignment
# * Core of prediction in ML
# 
# In ML: (y = \mathbf{w} \cdot \mathbf{x})
# 
# ---
# 
# ## 11. Angle Between Vectors
# 
# (\cos(\theta) = \frac{\mathbf{a} \cdot \mathbf{b}}{||a|| ||b||})
# 
# Used in:
# 
# * Cosine similarity
# * Text embeddings
# * Attention mechanisms
# 
# ---
# 
# ## 12. Projection of One Vector onto Another
# 
# Projection of (a) onto (b): (\text{proj}_b(a) = \frac{a \cdot b}{b \cdot b} b)
# 
# Graphical idea:
# 
# ```
# a
# |\
# | \  projection
# |  \
# |   ----> b
# ```
# 
# Why it matters:
# 
# * Least squares
# * Linear regression
# * Optimization
# 
# ---
# 
# ## 13. Orthogonality
# 
# Two vectors are **orthogonal** if: (\mathbf{a} \cdot \mathbf{b} = 0)
# 
# Meaning:
# 
# * No shared information
# * Independent directions
# 
# In ML:
# 
# * Decorrelated features
# * Stable optimization
# 
# ---
# 
# ## 14. Vectors as ML Data
# 
# | Concept     | Vector Meaning    |
# | ----------- | ----------------- |
# | Data sample | Feature vector    |
# | Weights     | Parameter vector  |
# | Prediction  | Dot product       |
# | Loss        | Distance or error |
# 
# ---
# 
# ## 15. Mental Model (Important)
# 
# Think of ML as:
# 
# > Aligning weight vectors with data vectors to minimize error.
# 
# Everything else builds on this.
# 
# ---
# 
# ## 16. What Comes Next
# 
# After mastering this file:
# 
# * Matrices = stacked vectors
# * Matrix-vector multiplication
# * Linear systems
# 
# Do not move forward until this file feels **boringly obvious**.
#
