# Generated from: 07_angle_similarity.ipynb
# Converted at: 2026-02-18T04:58:29.779Z
# Next step (optional): refactor into modules & generate tests with RunCell
# Quick start: pip install runcell

# # 07 — Angle Between Vectors & Similarity (Linear Algebra for AI/ML)


# 
# ## 1. Angle Between Two Vectors
# 
# The angle between vectors measures **directional similarity**.
# 
# Formula:
# cos(θ) = (a · b) / (‖a‖ ‖b‖)
# 


import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

cos_theta = np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))
cos_theta

#
# ## 2. Interpreting the Angle
# 
# - cos(θ) = 1 → same direction
# - cos(θ) = 0 → orthogonal
# - cos(θ) = -1 → opposite direction
# 


# Orthogonal vectors
v1 = np.array([1, 0])
v2 = np.array([0, 1])

np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))


# 
# ## 3. Cosine Similarity
# 
# Cosine similarity measures **similarity independent of magnitude**.
# 
# Used heavily in:
# - NLP
# - Recommendation systems
# - Search engines
# 


# Cosine similarity function
def cosine_similarity(x, y):
    return np.dot(x, y) / (np.linalg.norm(x) * np.linalg.norm(y))


cosine_similarity(a, b)

#
# ## 4. Angle vs Distance
# 
# - Angle → direction similarity
# - Distance → absolute separation
# 
# Two vectors can be far apart but still similar in direction.
# 


x1 = np.array([1, 1])
x2 = np.array([10, 10])

np.linalg.norm(x1 - x2), cosine_similarity(x1, x2)

#
# ## 5. ML Applications
# 
# - Text similarity (TF-IDF, embeddings)
# - Clustering in high dimensions
# - Attention mechanisms
# - Feature comparison
# 


# 
# ## 6. Common Mistakes
# 
# ❌ Forgetting normalization  
# ❌ Using cosine similarity when magnitude matters  
# ❌ Dividing by zero vectors  
# 
# Always normalize carefully.
# 


# 
# ## 7. Summary
# 
# - Angle quantifies direction
# - Cosine similarity ∈ [-1, 1]
# - Scale-invariant similarity measure
# - Critical in ML & AI systems
#
