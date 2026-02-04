import pandas as pd

# Creating a small DataFrame from a dictionary for practice
data = {
    'Name': ['Partha', 'Rahul', 'Ananya', 'Sayan'],
    'Project': ['Attendance App', 'E-commerce', 'Nature Tracker', 'IoT Sensor'],
    'Hours_Spent': [120, 80, 95, 110],
    'Status': ['In Progress', 'Completed', 'In Progress', 'Planning']
}

df = pd.DataFrame(data)

# NOTE: .head(n) shows the first n rows. Great for a quick glimpse of the structure.
print(df.head(2))

# NOTE: .info() is vital for AI-ML; it shows data types and if any values are missing (nulls).
df.info()

# NOTE: .describe() gives statistical summaries (mean, std, min, max) of numerical columns.
print(df.describe())
