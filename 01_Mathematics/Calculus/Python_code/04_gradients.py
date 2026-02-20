"""
Gradients (Calculus for Machine Learning)

Purpose:
Understand gradients as vectors of partial derivatives.
Gradients drive optimization in ML and deep learning.
"""

import numpy as np
import matplotlib.pyplot as plt


# ==========================================================
# Core Multivariable Function
# ==========================================================

def surface_function(x: np.ndarray, y: np.ndarray) -> np.ndarray:
    """Return f(x, y) = x^2 + y^2"""
    return x ** 2 + y ** 2


# ==========================================================
# Analytical Gradient
# ==========================================================

def gradient(x: float, y: float) -> np.ndarray:
    """
    Gradient of f(x, y) = x^2 + y^2

    ∇f = [2x, 2y]
    """
    return np.array([2 * x, 2 * y])


# ==========================================================
# Numerical Gradient (Verification)
# ==========================================================

def numerical_gradient(f, x: float, y: float, h: float = 1e-5) -> np.ndarray:
    """Compute numerical gradient using central difference."""
    dfdx = (f(x + h, y) - f(x - h, y)) / (2 * h)
    dfdy = (f(x, y + h) - f(x, y - h)) / (2 * h)
    return np.array([dfdx, dfdy])


# ==========================================================
# Visualization: Gradient Field
# ==========================================================

def plot_gradient_field() -> None:
    """Plot gradient vector field of f(x, y) = x^2 + y^2."""
    x = np.linspace(-4, 4, 20)
    y = np.linspace(-4, 4, 20)
    X, Y = np.meshgrid(x, y)

    U = 2 * X
    V = 2 * Y

    plt.figure()
    plt.quiver(X, Y, U, V)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Gradient Field of f(x, y) = x^2 + y^2")
    plt.grid(True)
    plt.show()


# ==========================================================
# Execution Entry Point
# ==========================================================

def main() -> None:
    x0, y0 = 1, 2

    analytical = gradient(x0, y0)
    numerical = numerical_gradient(surface_function, x0, y0)

    print(f"Analytical Gradient at ({x0},{y0}): {analytical} - 04_gradients.py:78")
    print(f"Numerical Gradient at ({x0},{y0}): {numerical} - 04_gradients.py:79")

    plot_gradient_field()


if __name__ == "__main__":
    main()