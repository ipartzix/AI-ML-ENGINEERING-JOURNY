import pandas as pd

data = {
    "Name": ["Partha", "Pritam", "Argha"],
    "Age": [21, 15, 16],
    "Marks": [90, None, 88]
}
df = pd.DataFrame(data)
print(df)
print()

print()
print(df.sort_values(by="Marks", ascending=True))
print()
print(df.sort_values(by="Marks", ascending=False))
