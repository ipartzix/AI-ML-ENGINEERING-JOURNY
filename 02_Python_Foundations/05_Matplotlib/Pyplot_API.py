import pandas as pd 
import matplotlib.pyplot as plt 

# Univariate - Numerical
data = {
    "Salary": [120000, 34000, 77000, 760000, 32000,54000, 670000, 45000, 13400, 29000]
}

df = pd.DataFrame(data)
print(df.head(5))

# Line plot 
plt.plot(df["Salary"],color="red",marker="o",linestyle= ":",linewidth=2)
plt.grid()
plt.show()

# Histogram
plt.hist(df["Salary"],bins =5 ,color="green")
plt.show()

#Boxplot
plt.boxplot(df["Salary"])
plt.show()

#Univarite : Categorical
df["dept"]=["HR","IT","FINANCE","ENGINEER","CA","DOCTOR","TEACHER","IPS","IAS","ARMY"]
print(df.head())
df.info()

#Pie chart:
count =df["dept"].value_counts()
plt.pie(count,labels=count.index,autopct="%1.1f",explode=[0,0.1]+[0]*8) # type: ignore
# Pie chart: each value in 'explode' controls how far a slice moves outward.
# 0 → normal position (no shift)
# 0.1 → slice moves 10% of the radius away from the center
# Length of 'explode' must equal number of slices (one value per slice)
# Example: explode=[0, 0.1] + [0]*8 → only second slice is highlighted

plt.show()

# countplot
plt.bar(count.index, count, color=["green","blue","black","red","purple","orange","cyan","magenta","yellow","gray"])
plt.xticks(rotation=90)   # rotate labels
plt.tight_layout()        # adjust spacing
plt.show()