import pandas as pd

data = {
    "Name": ["Partha", "Pritam", "Argha"],
    "Age": [21, 15, 16],
    "Marks": [90, 99, 28]
}
df = pd.DataFrame(data)
print(df)
print()
df["Marks"] = df["Marks"] + 5
print(df)
