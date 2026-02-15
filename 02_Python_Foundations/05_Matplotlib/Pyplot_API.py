import pandas as pd 
import matplotlib.pyplot as plt 

# Univariate - Numerical
data = {
    "Salary": [120000, 34000, 77000, 760000, 32000,54000, 670000, 45000, 13400, 29000]
}

df = pd.DataFrame(data)
print(df.head(5))

# Line plot 
plt.plot(df["Salary"],color="red",marker="o",linestyle= ":",linewidth="2")
plt.grid()
plt.show()

# Histogram
plt.hist(df["Salary"],bins =5 ,color="green")
plt.show()

#Boxplot
plt.boxplot(df["Salary"])
plt.show()