"""
Loss Functions & Their Derivatives

Purpose:
Understand how loss functions quantify prediction error
and how their derivatives drive optimization.
"""

import numpy as np
import matplotlib.pyplot as plt


# ==========================================================
# Mean Squared Error (MSE)
# ==========================================================

def mse_loss(y_true: np.ndarray, y_pred: np.ndarray) -> np.ndarray:
    """Mean Squared Error: (y - y_hat)^2"""
    return (y_true - y_pred) ** 2


def mse_gradient(y_true: np.ndarray, y_pred: np.ndarray) -> np.ndarray:
    """Derivative of MSE with respect to y_pred."""
    return -2 * (y_true - y_pred)


# ==========================================================
# Mean Absolute Error (MAE)
# ==========================================================

def mae_loss(y_true: np.ndarray, y_pred: np.ndarray) -> np.ndarray:
    """Mean Absolute Error: |y - y_hat|"""
    return np.abs(y_true - y_pred)


def mae_gradient(y_true: np.ndarray, y_pred: np.ndarray) -> np.ndarray:
    """
    Subgradient of MAE.
    Note: Not differentiable at zero.
    """
    return np.sign(y_pred - y_true)


# ==========================================================
# Binary Cross-Entropy (BCE)
# ==========================================================

def binary_cross_entropy(y_true: np.ndarray, y_pred: np.ndarray) -> np.ndarray:
    """
    Binary Cross-Entropy Loss:
    -[y log(p) + (1-y) log(1-p)]

    Includes numerical stability clipping.
    """
    epsilon = 1e-9
    y_pred = np.clip(y_pred, epsilon, 1 - epsilon)
    return -(y_true * np.log(y_pred) + (1 - y_true) * np.log(1 - y_pred))


def bce_gradient(y_true: np.ndarray, y_pred: np.ndarray) -> np.ndarray:
    """
    Derivative of BCE with respect to y_pred.
    """
    epsilon = 1e-9
    y_pred = np.clip(y_pred, epsilon, 1 - epsilon)
    return (y_pred - y_true) / (y_pred * (1 - y_pred))


# ==========================================================
# Visualization
# ==========================================================

def plot_regression_losses():
    error = np.linspace(-5, 5, 200)
    y_true = np.zeros_like(error)
    y_pred = error

    plt.figure()
    plt.plot(error, mse_loss(y_true, y_pred))
    plt.title("Mean Squared Error")
    plt.xlabel("Error")
    plt.ylabel("Loss")
    plt.grid(True)
    plt.show()

    plt.figure()
    plt.plot(error, mae_loss(y_true, y_pred))
    plt.title("Mean Absolute Error")
    plt.xlabel("Error")
    plt.ylabel("Loss")
    plt.grid(True)
    plt.show()


def plot_binary_cross_entropy():
    p = np.linspace(0.01, 0.99, 200)
    y_true = np.ones_like(p)

    plt.figure()
    plt.plot(p, binary_cross_entropy(y_true, p))
    plt.title("Binary Cross-Entropy (y=1)")
    plt.xlabel("Predicted Probability")
    plt.ylabel("Loss")
    plt.grid(True)
    plt.show()


# ==========================================================
# Execution Entry Point
# ==========================================================

def main():
    plot_regression_losses()
    plot_binary_cross_entropy()


if __name__ == "__main__":
    main()