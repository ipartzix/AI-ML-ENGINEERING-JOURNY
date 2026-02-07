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
print("""

1️⃣ df.isna()
What it does

Detects missing values

Returns a boolean DataFrame

True → value is missing (NaN, None, pd.NA)

False → value exists

Example
df.isna()

Output (example)
    Name    Age   Marks
0  False  False  False
1  False  False   True
2  False  False  False

Use case

Data inspection

Debugging datasets

Before cleaning data

👉 Does NOT modify the DataFrame

2️⃣ df.dropna()
What it does

Removes rows (or columns) containing missing values

Default: drops rows

df.dropna()

Default behavior

If any column in a row has NaN → row is deleted ❌

Example result
    Name   Age  Marks
0  Partha  21   90
2  Argha  16   28

Important options
df.dropna(axis=1)      # drop columns with NaN
df.dropna(how="all")   # drop only if all values are NaN
df.dropna(subset=["Marks"])


👉 Returns a new DataFrame (original unchanged unless inplace=True)

3️⃣ df.fillna()
What it does

Replaces missing values

Keeps all rows

You choose the replacement value

Example
df.fillna(0)

    Name    Age  Marks
0  Partha  21   90
1  Pritam  15    0
2  Argha  16   28

Common real-world usage
df["Marks"].fillna(df["Marks"].mean())
df.fillna(method="ffill")
df.fillna(method="bfill")


👉 Preferred in ML pipelines (dropping data often loses information)

Side-by-side comparison 🔥
Method	Purpose	Modifies Data?	Typical Use
isna()	Detect missing	❌ No	Inspection
dropna()	Remove missing	⚠️ Yes	Cleaning raw data
fillna()	Replace missing	⚠️ Yes	ML / analytics
Critical ML Insight (important for you) ⚠️🤖

Never blindly use dropna() in ML

You may lose valuable samples

Prefer fillna() with:

mean / median (numerical)

mode (categorical)

One-line summary

isna() → find

dropna() → delete

fillna() → repair

If you want, next I can explain:

pd.NA vs NaN

Why NaN > 80 is always False

Best missing-value strategy for AI/ML datasets

Say it.
""")
