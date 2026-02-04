# NOTE: Adding a new column based on existing data.
# Let's assume a project is 'Intense' if it takes more than 100 hours.
df['Is_Intense'] = df['Hours_Spent'] > 100

# NOTE: .apply() allows you to run a custom function on every row.
df['Name_Uppercase'] = df['Name'].apply(lambda x: x.upper())

print(df)
