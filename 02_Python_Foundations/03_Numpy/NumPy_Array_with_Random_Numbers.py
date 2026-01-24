import numpy as np

# rand() = the function is used to generate a random value between 0 to 1 .
print("For creating 1D arr")
arr = np.random.rand(3)

print(arr)
print()
arr1 = np.random.rand(2, 4)
print(arr1)

arr3 = np.random.rand(2, 4, 5)
print(arr3)

# randn() =the function is used to generate a random value close to zero
# it may return positive or negative number as well
print("Use od randn() function ")
arrn = np.random.randn(5)
print(arrn)
