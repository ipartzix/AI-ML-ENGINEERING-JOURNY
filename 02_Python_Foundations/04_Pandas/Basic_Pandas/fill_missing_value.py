import pandas as pd

data = {
    "Name": ["Partha", "Pritam", "Argha"],
    "Age": [21, 15, 16],
    "Marks": [90, None, 28]
}
df = pd.DataFrame(data)
print(df)
print()
print("_______________ Check missing value______________")
print(df.isnull())
print()

print(df.isnull().sum())
print(f"use isnull() to detect missing values and"
      f" isnull().sum() to quantify them per column before preprocessing.")
print()
# print("_______________Remove Missing Values___________________")
# df = df.dropna()  # dropna() does NOT modify the DataFrame in place by default
# # so we create a new variable called df and store the value
# print(df)
print()
print("____________________Fill Missing Values___________________")
df = df.fillna(0)
print(df)
# usually do EITHER dropna() OR fillna() — not both
