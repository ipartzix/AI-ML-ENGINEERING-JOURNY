import numpy as np

# Sensor readings (some faulty negative values)
temperature = np.array([22.5, 23.0, -99.0, 24.1, 23.8, -99.0, 25.0])

# Replace faulty values with mean of valid data
valid_data = temperature[temperature > 0]
clean_mean = np.mean(valid_data)

temperature[temperature < 0] = clean_mean

print("Cleaned temperature data:", temperature)
