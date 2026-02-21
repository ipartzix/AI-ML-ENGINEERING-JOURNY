"""
Optimization & Gradient Descent

Purpose:
Demonstrate how gradients minimize a loss function.
Core principle behind ML model training.
"""

import numpy as np
import matplotlib.pyplot as plt


# ==========================================================
# Loss Function Definition
# ==========================================================

def loss_function(w: np.ndarray) -> np.ndarray:
    """L(w) = w^2"""
    return w ** 2


def loss_gradient(w: float) -> float:
    """dL/dw = 2w"""
    return 2 * w


# ==========================================================
# Gradient Descent Optimizer
# ==========================================================

def gradient_descent(start: float, learning_rate: float, steps: int):
    """
    Perform gradient descent on L(w) = w^2.
    Returns history of parameter values.
    """
    w = start
    history = [w]

    for _ in range(steps):
        grad = loss_gradient(w)
        w = w - learning_rate * grad
        history.append(w)

    return np.array(history)


# ==========================================================
# Visualization Functions
# ==========================================================

def plot_loss_curve():
    """Plot loss surface L(w) = w^2."""
    w = np.linspace(-5, 5, 200)
    loss = loss_function(w)

    plt.figure()
    plt.plot(w, loss)
    plt.xlabel("w")
    plt.ylabel("L(w)")
    plt.title("Loss Function: L(w) = w^2")
    plt.grid(True)
    plt.show()


def plot_descent_path(path: np.ndarray):
    """Visualize gradient descent trajectory."""
    w = np.linspace(-5, 5, 200)
    loss = loss_function(w)

    plt.figure()
    plt.plot(w, loss)
    plt.scatter(path, loss_function(path))
    plt.xlabel("w")
    plt.ylabel("L(w)")
    plt.title("Gradient Descent Optimization Path")
    plt.grid(True)
    plt.show()


# ==========================================================
# Execution Entry Point
# ==========================================================

def main():
    start_value = 4.0
    learning_rate = 0.1
    steps = 20

    path = gradient_descent(start_value, learning_rate, steps)

    print(f"Initial w: {start_value} - 05_optimization_gradient_descent.py:91")
    print(f"Final w: {path[1]} - 05_optimization_gradient_descent.py:92")
    print(f"Final loss: {loss_function(path[1])} - 05_optimization_gradient_descent.py:93")

    plot_loss_curve()
    plot_descent_path(path)


if __name__ == "__main__":
    main()