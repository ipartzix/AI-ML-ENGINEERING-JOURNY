import pandas as pd

data = {
    "Name": ["Partha", "Pritam", "Argha"],
    "Age": [21, 15, 16],
    "Marks": [90, 99, 28]
}
df = pd.DataFrame(data)
print(df)
print()
print("---------------Drop Column--------------")
df.drop("Age", axis=1, inplace=True)
print(df)
print()
print("----------------Drop Row----------------")
df.drop(0, axis=0, inplace=True)
print(df)

# axis=0 → row | axis=1 → column
