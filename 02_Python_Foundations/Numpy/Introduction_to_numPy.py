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
