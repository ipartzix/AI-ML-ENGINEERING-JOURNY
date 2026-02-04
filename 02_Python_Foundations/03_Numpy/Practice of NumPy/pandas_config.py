import pandas as pd

# 1. Create a simple DataFrame
df = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie"],
    "Hours_Spent": [50, 120, 200]
})

# 2. Basic operations
df["Is_Intense"] = df["Hours_Spent"] > 100
df["Name_Uppercase"] = df["Name"].str.upper()

# 3. Display results
print("Pandas Version:", pd.__version__)
print("\nDataFrame Output:")
print(df)

# 4. Simple assertion checks
assert df.shape == (3, 4)
assert df["Is_Intense"].sum() == 2
assert df["Name_Uppercase"].iloc[0] == "ALICE"

print("\n✅ Pandas is working correctly.")
