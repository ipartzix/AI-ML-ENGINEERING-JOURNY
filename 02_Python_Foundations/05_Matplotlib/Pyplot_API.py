import pandas as pd
import matplotlib.pyplot as plt

# Univariate - Numerical
data = {
    "Salary": [120000, 34000, 77000, 760000, 32000, 54000, 670000, 45000, 13400, 29000]
}

df = pd.DataFrame(data)
print(df.head(5))

# Line plot
plt.plot(df["Salary"], color="red", marker="o", linestyle=":", linewidth=2)
plt.grid()
plt.show()

# Histogram
plt.hist(df["Salary"], bins=5, color="green")
plt.show()

# Boxplot
plt.boxplot(df["Salary"])
plt.show()

# Univarite : Categorical
df["dept"] = [
    "HR",
    "IT",
    "FINANCE",
    "ENGINEER",
    "CA",
    "DOCTOR",
    "TEACHER",
    "IPS",
    "IAS",
    "ARMY",
]
print(df.head())
df.info()

# Pie chart:
count = df["dept"].value_counts()
plt.pie(count, labels=count.index, autopct="%1.1f", explode=[0, 0.1] + [0] * 8)  # type: ignore
# Pie chart: each value in 'explode' controls how far a slice moves outward.
# 0 → normal position (no shift)
# 0.1 → slice moves 10% of the radius away from the center
# Length of 'explode' must equal number of slices (one value per slice)
# Example: explode=[0, 0.1] + [0]*8 → only second slice is highlighted

plt.show()

# countplot
plt.bar(
    count.index,
    count,
    color=[
        "green",
        "blue",
        "black",
        "red",
        "purple",
        "orange",
        "cyan",
        "magenta",
        "yellow",
        "gray",
    ],
)
plt.xticks(rotation=90)  # rotate labels
plt.tight_layout()  # adjust spacing
plt.show()

# Bivariate -numerical
df["Age"] = [22, 34, 55, 66, 33, 30, 31, 26, 28, 38]
print(df.head())

#Scatter Plot:
plt.scatter(df["Age"],df["Salary"],color="blue")
plt.show()

sort_age =df.sort_values("Age") # we are short the age for better visualization 

#line Plot:
plt.plot(sort_age["Age"],df["Salary"],color="red",marker="*",linewidth=2)
plt.grid()
plt.show()

#Bar Chart
plt.bar(sort_age["Age"],df["Salary"],color="red",align="edge")
plt.show()

#Bivariate : Numerical -categorical 
print("# box plot is a way to represent the numerical and categorical collumn\n another way is pie chart - Pyplot_API.py:93")
# pie chart :
salary_by_dept=df.groupby("dept")["Salary"].sum()
print(salary_by_dept)
plt.pie(salary_by_dept,labels=salary_by_dept.index, autopct="%1.2f",shadow=True) # type: ignore # t
plt.axis("equal")
plt.show()

#Multivariate Analysis :
df["experience"] = [1,2,3,4,5,6,7,8,9,10]
df.head()

#Bubble Plot: 3 numerical value 
plt.scatter(df["Age"],df["Salary"],s=df["experience"]*10,color ="blue",edgecolors="black")
plt.title("Age vs Salary vs Experience")
plt.xlabel("Age")
plt.ylabel("Salary")
plt.grid()
plt.show()

# 2 numerical value 
plt.scatter(
    df["Age"],
    df["Salary"],
    c=df["dept"].map({
        "HR":"blue","IT":"red","FINANCE":"green","ENGINEER":"skyblue",
        "CA":"yellow","DOCTOR":"black","TEACHER":"red","IPS":"green",
        "IAS":"purple","ARMY":"orange"
    })
)
plt.title("Age vs Salary vs Experience")
plt.xlabel("Age")
plt.ylabel("Salary")
plt.grid()
plt.show()
