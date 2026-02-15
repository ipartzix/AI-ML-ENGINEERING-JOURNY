import pandas as pd
import matplotlib.pyplot as plt

data ={
    "Year":[2020,2021,2022,2023],
    "Sales":[100,150,200,250],
    "Profit":[20,30,40,50],
    "Expenses":[90,120,160,200]
}
df= pd.DataFrame(data)

plt.plot(df["Year"], df["Sales"], label="Sales")
plt.plot(df["Year"], df["Profit"], label="Profit")
plt.plot(df["Year"], df["Expenses"], label="Expenses")

plt.xlabel("Year")
plt.ylabel("Amount")
plt.title("Company Performance Over Years")
plt.legend()   # IMPORTANT to display labels
plt.grid()
plt.savefig(r"D:\AI ML ENGINEERING JOURNY\02_Python_Foundations\05_Matplotlib\Company Performance Over Years.jpg")
plt.show()
