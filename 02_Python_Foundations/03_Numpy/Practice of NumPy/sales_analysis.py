import numpy as np

# Monthly sales data (in ₹ thousands)
sales = np.array([120, 135, 150, 145, 160, 170, 180, 175, 165, 155, 140, 130])

# Basic analytics
total_sales = np.sum(sales)
average_sales = np.mean(sales)
max_sale = np.max(sales)
best_month = np.argmax(sales) + 1

print("Total yearly sales:", total_sales)
print("Average monthly sales:", average_sales)
print("Best month:", best_month, "with sales:", max_sale)
