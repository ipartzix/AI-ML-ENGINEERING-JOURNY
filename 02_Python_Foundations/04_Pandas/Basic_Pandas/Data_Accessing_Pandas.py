import pandas as pd

data = {
    "Name": ["Partha", "Pritam", "Argha"],
    "Age": [21, 15, 16],
    "Marks": [90, 99, 80]
}
df = pd.DataFrame(data)
print(df)

print("----For Access Columns----")
print(df["Name"])
print("----------------------------------")
print(df[["Name", "Marks"]])
print("---------------------------------")
print(df[["Name", "Age", "Marks"]])

print("------------------------------------")

print("_____________Access Rows_____________")
print("Using iloc (index based)")
print(df.iloc[0])
print("df.iloc[0] print the 1st row ")

print(df.iloc[0:2])
print("df.iloc[0:2] print the 1st two  row ")
