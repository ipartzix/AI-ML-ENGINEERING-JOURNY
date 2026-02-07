import pandas as pd

data = {
    "Name": ["Partha", "Pritam", "Argha"],
    "Age": [21, 15, 16],
    "Marks": [90, None, 88]
}
df = pd.DataFrame(data)
print(df)
print()
df = pd.read_csv("data.csv")
print(df)
