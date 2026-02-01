import numpy as np

# Data structure: [restaurant_id, 2021, 2022, 2023, 2024]
sales_data = np.array([
    [1, 150000, 180000, 220000, 250000],  # Paradise Biryani
    [2, 120000, 140000, 160000, 190000],  # Beijing Bites
    [3, 200000, 230000, 260000, 300000],  # Pizza Hub
    [4, 180000, 210000, 240000, 270000],  # Burger Point
    [5, 160000, 185000, 205000, 230000]  # Chai Point
])

print("==== Zomato sales analysis ==== ")
print("\n Sales data shape", sales_data.shape)
print("\n Sample data for 1st 3 restau: ", sales_data[0:3])

print("Total sales per year ")
print(np.sum(sales_data, axis=0))
yearly_total = np.sum(sales_data[:, 1:], axis=0)
print(yearly_total)

# Minimum sales per restaurant
min_sales = np.min(sales_data[:, 1:], axis=1)
print(min_sales)
