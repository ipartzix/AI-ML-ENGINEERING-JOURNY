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
print("2. 2-D data")
data = {
    "Name": ["Partha", "Pritam", "Argha"],
    "age": [21, 15, 16],
    "Marks": [90, 99, 80]
}
df = pd.DataFrame(data)
print(df)
"""
2. 2-D data
     Name  age  Marks
0  Partha   21     90
1  Pritam   15     99
2   Argha   16     80

"""
