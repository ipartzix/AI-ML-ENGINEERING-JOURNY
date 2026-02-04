# NOTE: Checking for missing values. Returns a boolean map of the data.
print(df.isnull().sum())

# NOTE: .fillna() replaces missing values (NaN) with something else (like 0 or the mean).
# df['Hours_Spent'] = df['Hours_Spent'].fillna(0)

# NOTE: .drop_duplicates() ensures your AI doesn't learn from redundant data.
df = df.drop_duplicates()
