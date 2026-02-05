import pandas as pd
print("Pandas has 2 main data structure ")
print("1. 1D data")
s = pd.Series([10, 20, 30, 44, 67])
print(s)
# is is like single column | similar to array or list
"""
1. 1D data
0    10
1    20
2    30
3    44
4    67
dtype: int64

"""
print("2. 2-D data")  # All lists must have the same length (here, length = 3), otherwise Pandas will throw an error
data = {
    "Name": ["Partha", "Pritam", "Argha"],
    "age": [21, 15, 16],
    "Marks": [90, 99, 80]
}
df = pd.DataFrame(data)  # converts the dictionary into a tabular structure.
print(df)
"""
2. 2-D data
     Name  age  Marks
0  Partha   21     90
1  Pritam   15     99
2   Argha   16     80

Each key becomes a column.

Each list element aligns row-wise by index.

| Index | Name   | age | Marks |
| ----- | ------ | --- | ----- |
| 0     | Partha | 21  | 90    |
| 1     | Pritam | 15  | 99    |
| 2     | Argha  | 16  | 80    |


Index → Row identifier (0, 1, 2)

Columns → Name, age, Marks

Rows → Individual student records
"""
print("-----------understanding the row ,coluimns and index-----------")
print("index:---------")
print(df.index)
print("columns:-------")
print(df.columns)
print("shape----------")
print(df.shape)

print()
print("------------------------view data-------------------------")

print("---head---")
print(df.head())

print("---tail---")
print(df.tail())

print("---info---")
df.info()
print("---describe---")
df.describe()
"""
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 3 entries, 0 to 2
Data columns (total 3 columns):
 0   Name    3 non-null object
 1   age     3 non-null int64
 2   Marks   3 non-null int64

"""
