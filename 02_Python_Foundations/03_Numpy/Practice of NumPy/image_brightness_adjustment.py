import numpy as np

# Simulated grayscale image (0–255)
image = np.random.randint(0, 256, size=(5, 5))

# Increase brightness
brightness_factor = 30
bright_image = np.clip(image + brightness_factor, 0, 255)

print("Original Image:\n", image)
print("Brightened Image:\n", bright_image)
