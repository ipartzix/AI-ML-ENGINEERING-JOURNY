import pandas as pd

data = {
    "Name": ["Partha", "Pritam", "Argha"],
    "Age": [21, 15, 16],
    "Marks": [90, 99, 28]
}
df = pd.DataFrame(data)
print(df)

# df["Passed"]=df["Marks"]>40
# print(df)
df["Result"] = "Fail"
# Creates a new column named Result
# Assigns "Fail" to every row
# This is called broadcasting


df.loc[df["Marks"] > 30, "Result"] = "Pass"  # loc[row_condition, column]
# Only rows matching the condition get updated
# Other rows remain unchanged

print(df)

# Boolean conditions + column names → ALWAYS use loc
# Integer positions only → use iloc
