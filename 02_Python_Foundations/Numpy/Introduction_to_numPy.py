import numpy as np

# Standard alias for Numerical Python; used for high-performance vector/matrix operations
# and as the foundation for most AI-ML libraries (Scikit-learn, TensorFlow, etc.).

print("Numpy Learning ")

lis_t = [1, 2, 3, 4]
x = np.array([1, 2, 3, 4])
print(x)
print(lis_t)
print(type(x))  # <class 'numpy.ndarray'>
print(type(lis_t))  # <class 'list'>

# %timeit [j**4 for j in range(1,9)] # it use to se time to execution for single line
# %%timeit [j**4 for j in range(1,9)] # it is use to see full code execution time

print("For create an NumPy array we use the function np.array()")
x = [1, 2, 3, 4, 5, 6, 7]
y = np.array(x)
print(y)

# This is the 1st method to create an array

p = np.array([4, 6, 7, 8, 9])
print(p)

# This is another method to create an array

print("========User input array:=========")
l = []
for i in range(1, 5):
    int1 = int(input("Enter num:-"))
    l.append(int1)
print(np.array(l))

print("-----------Dimensions of Array------------")
print(f"1-D Array ------> [ 1 2 3 4 ]\n"
      f"2-D Array ------> [[ 1 2 3 4 ]]\n"
      f"3-D Array ------> [[[ 1 2 3 4]]]\n"
      f"Higher Dimensional Arrays-----> increase []\n")

print("print or know the Dimensions of Array w use ' .ndim ' ")
print(y.ndim)
