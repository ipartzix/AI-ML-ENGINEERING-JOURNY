import pandas as pd

data = {
    "Name": ["Partha", "Pritam", "Argha"],
    "Age": [21, 15, 16],
    "Marks": [90, None, 88]
}
df = pd.DataFrame(data)
print(df)
print()
# read operation
df = pd.read_csv("data.csv")
print(df)
# write operation
df.to_csv("output.csv", index=False)
print(df)
