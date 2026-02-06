import pandas as pd

data = {
    "Name": ["Partha", "Pritam", "Argha"],
    "Age": [21, 15, 16],
    "Marks": [90, None, 28]
}
df = pd.DataFrame(data)
print(df)
print()

print(df.isnull())
print()

print(df.isnull().sum())
