# Generated from: 06_loss_functions_derivatives.ipynb
# Converted at: 2026-02-18T08:42:57.815Z
# Next step (optional): refactor into modules & generate tests with RunCell
# Quick start: pip install runcell

# # Loss Functions & Their Derivatives (Calculus for Machine Learning)
# 
# **Purpose:** Understand how loss functions quantify error and how their derivatives guide learning.


# ## Loss Function Overview
# A loss function measures prediction error. Training minimizes this loss using gradients.


# ## Mean Squared Error (MSE)
# $$ L = (y - \hat{y})^2 $$


import matplotlib.pyplot as plt
import numpy as np

e = np.linspace(-5, 5, 100)
loss_mse = e ** 2

plt.figure()
plt.plot(e, loss_mse)
plt.xlabel('Error')
plt.ylabel('Loss')
plt.title('Mean Squared Error')
plt.show()

# ## Mean Absolute Error (MAE)
# $$ L = |y - \hat{y}| $$


loss_mae = np.abs(e)

plt.figure()
plt.plot(e, loss_mae)
plt.xlabel('Error')
plt.ylabel('Loss')
plt.title('Mean Absolute Error')
plt.show()

# ## Binary Cross-Entropy
# $$ L = -[y\log(\hat{y}) + (1-y)\log(1-\hat{y})] $$


p = np.linspace(0.01, 0.99, 100)
loss_ce = -np.log(p)

plt.figure()
plt.plot(p, loss_ce)
plt.xlabel('Predicted Probability')
plt.ylabel('Loss')
plt.title('Binary Cross-Entropy (y=1)')
plt.show()

# ## ML Connection
# - Loss derivatives determine gradient direction
# - Different tasks require different losses
# - Combined with backpropagation for training


# ## Summary
# - Loss functions measure error
# - Derivatives enable optimization
# - Essential for regression and classification
