import numpy as np

# Raw feature values
features = np.array([1200, 1500, 1800, 2000, 2500])

# Min-Max Normalization
normalized = (features - np.min(features)) / (np.max(features) - np.min(features))

print("Normalized features:", normalized)
