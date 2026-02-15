#Object Oriented API 
import pandas as pd
import matplotlib.pyplot as plt

from Pyplot_API import data
print(data)
# Create figure and 3 subplots (1 row, 3 columns)
fig, axs = plt.subplots(1, 3, figsize=(10, 5))

# Print objects to see what they are
print("Figure object: - 02_Object_Oriented_API.py:11", fig)
print("Axes objects array: - 02_Object_Oriented_API.py:12", axs)
plt.show()