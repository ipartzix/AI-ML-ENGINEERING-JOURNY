# NOTE: Selecting a single column returns a 'Series'.
names = df['Name']

# NOTE: Filtering rows based on a condition.
# Think of this like a SQL 'WHERE' clause.
busy_projects = df[df['Hours_Spent'] > 100]

# NOTE: Using .loc to select specific rows and columns by label.
# Format: df.loc[row_index, column_name]
sayan_project = df.loc[3, 'Project']

print(busy_projects)
