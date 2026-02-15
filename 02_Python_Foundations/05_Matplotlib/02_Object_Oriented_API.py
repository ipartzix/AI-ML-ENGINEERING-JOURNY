#Object Oriented API 
import pandas as pd
import matplotlib.pyplot as plt

from Pyplot_API import data
print(data)
# Create DataFrame
df = pd.DataFrame(data)


# Add Age column
df["Age"] = [22, 34, 55, 66, 33, 30, 31, 26, 28, 38]
# Sort by Age
sort_age = df.sort_values("Age")


# Create figure and 3 subplots (1 row, 3 columns)
fig, axs = plt.subplots(1, 3, figsize=(10, 5))

# Print objects
print("Figure object: - 02_Object_Oriented_API.py:21", fig)
print("Axes objects array: - 02_Object_Oriented_API.py:22", axs)

# Example plot on first subplot
axs[0].plot(sort_age["Age"], df["Salary"], color="red", marker="*", linewidth=2)
axs[0].set_title("Age vs Salary")

plt.show()