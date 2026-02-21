"""
Calculus Summary for Machine Learning

Purpose:
Consolidate essential calculus concepts required
for machine learning and deep learning.
"""


# ==========================================================
# Core Derivative Rules
# ==========================================================

def derivative_square(x: float) -> float:
    """d/dx (x^2) = 2x"""
    return 2 * x


def partial_derivative_x(x: float, y: float) -> float:
    """∂/∂x (x^2 + y^2) = 2x"""
    return 2 * x


def gradient(x: float, y: float):
    """Gradient ∇f = [2x, 2y]"""
    return [2 * x, 2 * y]


# ==========================================================
# Optimization Update Rule
# ==========================================================

def gradient_descent_step(theta: float, grad: float, lr: float) -> float:
    """
    Parameter update rule:
    θ = θ - η ∇L
    """
    return theta - lr * grad


# ==========================================================
# Chain Rule
# ==========================================================

def chain_rule_example(x: float) -> float:
    """
    Example:
    y = (3x + 1)^2

    dy/dx = 2(3x + 1) * 3
    """
    return 2 * (3 * x + 1) * 3


# ==========================================================
# Conceptual Mapping: Calculus → ML
# ==========================================================

CALCULUS_TO_ML = {
    "Derivatives": "Measure rate of change of loss",
    "Partial Derivatives": "Used for multi-parameter models",
    "Chain Rule": "Backpropagation through layers",
    "Gradients": "Direction of steepest increase",
    "Gradient Descent": "Optimization algorithm",
    "Loss Functions": "Quantify prediction error",
    "Backpropagation": "Efficient gradient computation"
}


# ==========================================================
# Execution Entry Point
# ==========================================================

def main():
    print("Derivative of x^2 at x=3: - 08_calculus_summary.py:75", derivative_square(3))
    print("Partial derivative at (1,2): - 08_calculus_summary.py:76", partial_derivative_x(1, 2))
    print("Gradient at (1,2): - 08_calculus_summary.py:77", gradient(1, 2))
    print("Chain rule example at x=2: - 08_calculus_summary.py:78", chain_rule_example(2))

    print("\nCalculus → ML Mapping: - 08_calculus_summary.py:80")
    for concept, meaning in CALCULUS_TO_ML.items():
        print(f"{concept}: {meaning} - 08_calculus_summary.py:82")


if __name__ == "__main__":
    main()