import pandas as pd

data = {
    "Name": ["Partha", "Pritam", "Argha"],
    "Age": [21, 15, 16],
    "Marks": [90, 99, 80]
}
df = pd.DataFrame(data)
print(df)
print("____df.head(n) View top rows First n rows (data preview) count start f4rom 1 not 0____")
print(df.head(2))

print("____df.info() Data summary Data types, non-null counts, memory usage___")
print(df.info())

print("____df.describe() Statistics Count, mean, std, min, quartiles, max____")
print(df.describe())

print("____df.shape Size (rows, columns)_____")
print(df.shape())
