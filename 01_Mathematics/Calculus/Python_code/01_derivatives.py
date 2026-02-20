"""
Derivatives (Calculus for Machine Learning)

Purpose:
Understand rate of change and how derivatives drive optimization in ML.
"""

import numpy as np
import matplotlib.pyplot as plt


# ==========================================================
# Core Math Functions
# ==========================================================

def quadratic_function(x: np.ndarray) -> np.ndarray:
    """Return f(x) = x^2"""
    return x ** 2


def analytical_derivative(x: float) -> float:
    """Return analytical derivative of f(x) = x^2 → 2x"""
    return 2 * x


def numerical_derivative(f, x: float, h: float = 1e-5) -> float:
    """
    Compute numerical derivative using central difference formula.
    """
    return (f(x + h) - f(x - h)) / (2 * h)


# ==========================================================
# Visualization Functions
# ==========================================================

def plot_function(x: np.ndarray) -> None:
    """Plot the quadratic function."""
    y = quadratic_function(x)

    plt.figure()
    plt.plot(x, y)
    plt.xlabel("x")
    plt.ylabel("f(x) = x^2")
    plt.title("Function Plot")
    plt.grid(True)
    plt.show()


def plot_tangent(x: np.ndarray, x0: float) -> None:
    """Plot function and tangent line at a given point."""
    y = quadratic_function(x)
    y0 = quadratic_function(x0)
    slope = analytical_derivative(x0)

    tangent_line = slope * (x - x0) + y0

    plt.figure()
    plt.plot(x, y, label="f(x) = x^2")
    plt.plot(x, tangent_line, "--", label=f"Tangent at x={x0}")
    plt.scatter([x0], [y0])
    plt.legend()
    plt.title("Derivative as Tangent Slope")
    plt.grid(True)
    plt.show()


# ==========================================================
# Execution Entry Point
# ==========================================================

def main() -> None:
    x = np.linspace(-5, 5, 100)
    x0 = 2

    plot_function(x)
    plot_tangent(x, x0)

    num_deriv = numerical_derivative(quadratic_function, x0)
    ana_deriv = analytical_derivative(x0)

    print(f"Numerical derivative at x={x0}: {num_deriv} - 01_derivatives.py:82")
    print(f"Analytical derivative at x={x0}: {ana_deriv} - 01_derivatives.py:83")


if __name__ == "__main__":
    main()