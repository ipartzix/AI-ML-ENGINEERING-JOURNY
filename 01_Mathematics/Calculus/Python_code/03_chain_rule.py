"""
Chain Rule (Calculus for Machine Learning)

Purpose:
Understand how derivatives propagate through composed functions.
This is the mathematical backbone of backpropagation.
"""

import numpy as np
import matplotlib.pyplot as plt


# ==========================================================
# Function Definitions
# ==========================================================

def inner_function(x: float) -> float:
    """g(x) = 3x + 1"""
    return 3 * x + 1


def outer_function(u: float) -> float:
    """f(u) = u^2"""
    return u ** 2


def composed_function(x: float) -> float:
    """y = f(g(x)) = (3x + 1)^2"""
    return outer_function(inner_function(x))


# ==========================================================
# Analytical Derivative via Chain Rule
# ==========================================================

def analytical_derivative(x: float) -> float:
    """
    dy/dx = dy/du * du/dx
          = 2(3x + 1) * 3
    """
    return 2 * inner_function(x) * 3


# ==========================================================
# Numerical Derivative (Verification)
# ==========================================================

def numerical_derivative(f, x: float, h: float = 1e-5) -> float:
    """Central difference approximation."""
    return (f(x + h) - f(x - h)) / (2 * h)


# ==========================================================
# Visualization
# ==========================================================

def plot_composed_function() -> None:
    """Plot y = (3x + 1)^2."""
    x = np.linspace(-3, 3, 100)
    y = composed_function(x)

    plt.figure()
    plt.plot(x, y)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("y = (3x + 1)^2")
    plt.grid(True)
    plt.show()


# ==========================================================
# Multivariable Chain Rule Example
# ==========================================================

def multivariable_chain_rule_example(t: float) -> float:
    """
    Example:
    z = x^2 + y^2
    x = t
    y = 2t

    dz/dt = ∂z/∂x * dx/dt + ∂z/∂y * dy/dt
    """
    x = t
    y = 2 * t

    dz_dx = 2 * x
    dz_dy = 2 * y

    dx_dt = 1
    dy_dt = 2

    return dz_dx * dx_dt + dz_dy * dy_dt


# ==========================================================
# Execution Entry Point
# ==========================================================

def main() -> None:
    x0 = 2

    print(f"Analytical dy/dx at x={x0}: {analytical_derivative(x0)} - 03_chain_rule.py:103")
    print(f"Numerical dy/dx at x={x0}: {numerical_derivative(composed_function, x0)} - 03_chain_rule.py:104")

    print(f"Multivariable chain rule at t=1: {multivariable_chain_rule_example(1)} - 03_chain_rule.py:106")

    plot_composed_function()


if __name__ == "__main__":
    main()