"""
Backpropagation (Mathematical Foundation for Neural Networks)

Purpose:
Compute gradients of loss with respect to model parameters
using the chain rule.
"""

import numpy as np


# ==========================================================
# Forward Pass
# ==========================================================

def forward(x: float, w: float, b: float) -> float:
    """
    Single neuron forward pass:
    z = wx + b
    y_hat = z (identity activation)
    """
    return w * x + b


# ==========================================================
# Loss Function
# ==========================================================

def mse_loss(y_true: float, y_pred: float) -> float:
    """Mean Squared Error."""
    return (y_true - y_pred) ** 2


def mse_gradient(y_true: float, y_pred: float) -> float:
    """dL/dy_hat for MSE."""
    return -2 * (y_true - y_pred)


# ==========================================================
# Backward Pass (Backpropagation)
# ==========================================================

def backward(x: float, y_true: float, w: float, b: float):
    """
    Compute gradients using chain rule.
    Returns gradients for w and b.
    """

    # Forward computation
    y_hat = forward(x, w, b)

    # Local gradients
    dL_dyhat = mse_gradient(y_true, y_hat)
    dyhat_dz = 1.0
    dz_dw = x
    dz_db = 1.0

    # Chain rule
    dL_dw = dL_dyhat * dyhat_dz * dz_dw
    dL_db = dL_dyhat * dyhat_dz * dz_db

    return dL_dw, dL_db


# ==========================================================
# Parameter Update
# ==========================================================

def update_parameters(w: float, b: float, dL_dw: float, dL_db: float, lr: float):
    """Gradient descent parameter update."""
    w_new = w - lr * dL_dw
    b_new = b - lr * dL_db
    return w_new, b_new


# ==========================================================
# Execution Entry Point
# ==========================================================

def main():
    # Sample data point
    x = 2.0
    y_true = 4.0

    # Initial parameters
    w = 1.5
    b = 0.5
    lr = 0.1

    # Forward pass
    y_hat = forward(x, w, b)
    loss = mse_loss(y_true, y_hat)

    print(f"Initial Prediction: {y_hat} - 07_backpropagation_math.py:94")
    print(f"Initial Loss: {loss} - 07_backpropagation_math.py:95")

    # Backward pass
    dL_dw, dL_db = backward(x, y_true, w, b)

    print(f"dL/dw: {dL_dw} - 07_backpropagation_math.py:100")
    print(f"dL/db: {dL_db} - 07_backpropagation_math.py:101")

    # Update parameters
    w, b = update_parameters(w, b, dL_dw, dL_db, lr)

    print(f"Updated w: {w} - 07_backpropagation_math.py:106")
    print(f"Updated b: {b} - 07_backpropagation_math.py:107")


if __name__ == "__main__":
    main()