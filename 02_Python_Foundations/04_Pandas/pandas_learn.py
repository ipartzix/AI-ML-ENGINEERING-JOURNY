import pandas as pd

print(pd.__version__)
data = {
    "Student_ID": [101, 102, 103, 104, 105],
    "Name": ["Amit", "Riya", "Sohan", "Neha", "Karan"],
    "Marks": [78, 85, 62, 90, 55],
    "Branch": ["CSE", "CSE", "ECE", "CSE", "ME"]
}
df = pd.DataFrame(data)

# Display DataFrame
print("Original DataFrame:")
print(df)

# Basic statistics
print("\nStatistics:")
print(df["Marks"].describe())

# Filter students with marks >= 75
high_scorers = df[df["Marks"] >= 75]
print("\nStudents with Marks >= 75:")
print(high_scorers)

# Add a new column (Pass/Fail)
df["Result"] = df["Marks"].apply(lambda x: "Pass" if x >= 60 else "Fail")

print("\nDataFrame with Result column:")
print(df)
