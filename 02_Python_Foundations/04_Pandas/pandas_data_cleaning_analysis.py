import numpy as np
import pandas as pd

# Create sample dataset
data = {
    "Employee_ID": [1, 2, 3, 4, 5, 6],
    "Name": ["Rahul", "Anita", "Vikas", "Pooja", "Suresh", "Kavya"],
    "Department": ["IT", "HR", "IT", "Finance", "HR", "IT"],
    "Salary": [55000, 48000, np.nan, 62000, 50000, np.nan],
    "Experience_Years": [2, 3, 1, 5, 4, 2]
}

df = pd.DataFrame(data)

print("Original Data:")
print(df)

# Check missing values
print("\nMissing values:")
print(df.isnull().sum())

# Fill missing salary with mean salary
df["Salary"].fillna(df["Salary"].mean(), inplace=True)

# Add salary category
df["Salary_Level"] = pd.cut(
    df["Salary"],
    bins=[0, 50000, 60000, 100000],
    labels=["Low", "Medium", "High"]
)
# Department-wise analysis
dept_salary = df.groupby("Department")["Salary"].agg(["mean", "max", "min"])
print("\nDepartment-wise Salary Analysis:")
print(dept_salary)
