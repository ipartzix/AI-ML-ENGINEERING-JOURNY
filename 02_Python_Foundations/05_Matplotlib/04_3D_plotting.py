import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import os

# Data
data = {
    "Year": [2020, 2021, 2022, 2023],
    "Sales": [100, 150, 200, 250],
    "Profit": [20, 30, 40, 50],
    "Expenses": [90, 120, 160, 200]
}

df = pd.DataFrame(data)

# Create 3D figure
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

# 3D Line Plot
ax.plot(df["Year"], df["Sales"], df["Profit"], marker='o')

# Labels
ax.set_xlabel("Year")
ax.set_ylabel("Sales")
ax.set_zlabel("Profit")
ax.set_title("3D Plot: Year vs Sales vs Profit")

# Target save path
save_path = r"D:\AI ML ENGINEERING JOURNY\02_Python_Foundations\05_Matplotlib\3D_Plot.png"

# Save image
plt.savefig(save_path, dpi=300)

print("Image saved at: - 04_3D_plotting.py:35", save_path)

plt.show()
