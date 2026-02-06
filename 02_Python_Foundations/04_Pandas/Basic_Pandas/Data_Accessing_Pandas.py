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
print(df[["Name", "Marks"]])
print(df[["Name", "Age", "Marks"]])
