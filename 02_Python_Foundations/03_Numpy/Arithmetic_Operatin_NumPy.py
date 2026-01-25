import numpy as np

print("Arithmetic Operation ")

print("normal method like + , - , *, /, %")

var1 = np.array([1, 2, 3, 4])
var2 = np.array([9, 8, 7, 6])

print("add")
var_add = var1 + var2
print(var_add)

print("sub")
varsub = var1 - var2
print(varsub)

print("mul")
varmal = var1 * var2
print(varmal)

print("div")
vardiv = var1 / var2
print(vardiv)

print("modulo")
varmod = var1 % var2
print(varmod)
print("power")
var_power = var1 ** var2
print(var_power)

print("Using function")

print("add")
var_add1 = np.add(var1, var2)
print(var_add1)

print("sub")
varsub1 = np.subtract(var1, var2)
print(varsub1)

print("mul")
varmal1 = np.multiply(var1, var2)
print(varmal1)

print("div")
vardiv1 = np.divide(var1, var2)
print(vardiv1)

print("modulo")
varmod1 = np.mod(var1, var2)
print(varmod1)

print("2D array ")
v1 = np.array([[1, 2, 3, 4], [1, 3, 5, 6]])
v2 = np.array([[1, 2, 3, 4], [1, 3, 5, 6]])

a = v1 + v2
print(a)

r = np.reciprocal(v1)
print(r)
