import numpy as np

# Daily returns (%)
returns = np.array([0.5, -0.2, 1.0, 0.3, -0.4, 0.8])

volatility = np.std(returns)
expected_return = np.mean(returns)

print("Expected Return:", expected_return)
print("Risk (Volatility):", volatility)
