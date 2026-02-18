# Generated from: 03_matrix_multiplication.ipynb
# Converted at: 2026-02-18T04:56:20.594Z
# Next step (optional): refactor into modules & generate tests with RunCell
# Quick start: pip install runcell

# 
# # 03 — Matrix Multiplication (Linear Algebra for AI/ML)
# 
# This notebook is a **complete, exam + ML‑oriented reference** for matrix multiplication.
# Use videos only to support this notebook, not replace it.
# 


# 
# ## 1. What is Matrix Multiplication?
# 
# Matrix multiplication is a binary operation that produces a new matrix by **combining rows of the first matrix with columns of the second matrix**.
# 
# If:
# - A is of shape **(m × n)**
# - B is of shape **(n × p)**
# 
# Then:
# - Result C = A × B has shape **(m × p)**
# 
# ⚠️ Multiplication is **not commutative**:
# A × B ≠ B × A (in general)
# 


# 
# ## 2. Condition for Matrix Multiplication
# 
# Matrix multiplication is defined **only if**:
# Number of columns in A = Number of rows in B
# 


# 
# ## 3. Manual (Element‑Wise) Understanding
# 
# Each element of result matrix:
# 
# C[i][j] = Σ (A[i][k] × B[k][j])
# 
# This is **row × column dot product**
# 


C = A @ B
C


# 
# ## 4. Step‑by‑Step Manual Calculation (Educational)
# 
# Let's compute multiplication manually using loops.
# 


def manual_matrix_multiply(A, B):
    result = [[0] * len(B[0]) for _ in range(len(A))]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]
    return result


manual_matrix_multiply(A.tolist(), B.tolist())

#
# ## 5. Matrix Multiplication Using NumPy
# 
# NumPy provides **optimized vectorized operations**.
# 


np.matmul(A, B)

A.dot(B)

#
# ## 6. Important Properties
# 
# 1. **Associative**
#    (A × B) × C = A × (B × C)
# 
# 2. **Distributive**
#    A × (B + C) = A×B + A×C
# 
# 3. **Not Commutative**
#    A × B ≠ B × A
# 


# 
# ## 7. Identity Matrix
# 
# I × A = A × I = A
# 


I = np.eye(3)
A2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

I @ A2

#
# ## 8. Matrix Multiplication in Machine Learning
# 
# Matrix multiplication is the **core of ML and DL**.
# 
# Examples:
# - Linear Regression:  y = XW
# - Neural Networks:   Z = W·X + b
# - Attention Mechanism
# - CNNs and Transformers
# 
# Without matrix multiplication, **AI does not exist**.
# 


# 
# ## 9. Example: Linear Model Computation
# 


# Feature matrix (samples × features)
X = np.array([[1, 2],
              [3, 4],
              [5, 6]])

# Weights (features × output)
W = np.array([[0.1],
              [0.2]])

# Prediction
y = X @ W
y

#
# ## 10. Common Errors
# 
# ❌ Shape mismatch  
# ❌ Confusing dot product with element‑wise multiplication  
# ❌ Assuming commutativity  
# 
# Always **check dimensions first**.
# 


# 
# ## 11. Summary
# 
# - Matrix multiplication = row × column dot product
# - Dimension compatibility is mandatory
# - Backbone of AI/ML computations
# - Must be mastered deeply
#
