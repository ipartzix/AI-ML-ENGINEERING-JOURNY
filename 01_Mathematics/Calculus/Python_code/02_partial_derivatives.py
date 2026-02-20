"""
Partial Derivatives (Calculus for Machine Learning)

Purpose:
Measure change with respect to one variable while holding others constant.
Core foundation for gradient-based optimization in ML.
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
# Analytical Partial Derivatives
# ==========================================================

def dfdx(x: float, y: float) -> float:
    """Analytical ∂f/∂x for f(x, y) = x^2 + y^2"""
    return 2 * x


def dfdy(x: float, y: float) -> float:
    """Analytical ∂f/∂y for f(x, y) = x^2 + y^2"""
    return 2 * y


# ==========================================================
# Numerical Partial Derivatives (Central Difference)
# ==========================================================

def numerical_dfdx(f, x: float, y: float, h: float = 1e-5) -> float:
    """Numerical approximation of ∂f/∂x using central difference."""
    return (f(x + h, y) - f(x - h, y)) / (2 * h)


def numerical_dfdy(f, x: float, y: float, h: float = 1e-5) -> float:
    """Numerical approximation of ∂f/∂y using central difference."""
    return (f(x, y + h) - f(x, y - h)) / (2 * h)


# ==========================================================
# Visualization
# ==========================================================

def plot_surface() -> None:
    """Plot 3D surface of f(x, y) = x^2 + y^2."""
    x = np.linspace(-4, 4, 50)
    y = np.linspace(-4, 4, 50)
    X, Y = np.meshgrid(x, y)
    Z = surface_function(X, Y)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")
    ax.plot_surface(X, Y, Z, alpha=0.7)

    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("f(x, y)")
    ax.set_title("Surface Plot: f(x, y) = x^2 + y^2")

    plt.show()


# ==========================================================
# Execution Entry Point
# ==========================================================

def main() -> None:
    x0, y0 = 1, 2

    print(f"Analytical ∂f/∂x at ({x0},{y0}): {dfdx(x0, y0)} - 02_partial_derivatives.py:80")
    print(f"Analytical ∂f/∂y at ({x0},{y0}): {dfdy(x0, y0)} - 02_partial_derivatives.py:81")

    print(f"Numerical ∂f/∂x at ({x0},{y0}): {numerical_dfdx(surface_function, x0, y0)} - 02_partial_derivatives.py:83")
    print(f"Numerical ∂f/∂y at ({x0},{y0}): {numerical_dfdy(surface_function, x0, y0)} - 02_partial_derivatives.py:84")

    plot_surface()


if __name__ == "__main__":
    main()