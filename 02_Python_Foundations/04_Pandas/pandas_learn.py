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
