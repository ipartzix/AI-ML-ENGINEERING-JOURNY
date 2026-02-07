import pandas as pd

data = {
    "Name": ["Partha", "Pritam", "Argha"],
    "Age": [21, 15, 16],
    "Marks": [90, None, 88]
}
df = pd.DataFrame(data)
print(df)
print()

df = df[df["Marks"] > 70]  # True  → keep row
# False → drop row

print(df)
# Now pandas uses that True / False mask to filter rows.
