import numpy as np

v = np.array([3, 2, 3, 4, 5, 4, 7, 4, 2])
print(f"minimum", np.min(v))
print(f"maximum", np.max(v))
print(f"minimum position", np.argmin(v))  # it say the position of minimum
print(f"maximum position", np.argmax(v))  # it say the position of maximum

v2 = np.array([[1, 4, 5, 8], [6, 7, 9, 3]])
print(f"maximum", np.max(v2,
                         1))  # we need pass the axis =0,1 if we want to pass column se pass 0 and if we want to pass row we sent 1
print(f"minimum", np.min(v2, 0))
print(f"minimum position", np.argmin(v2, 1))

print(f"sqrt", np.sqrt(v))

print(f"Sin", np.sin(v))
print(f"cos", np.cos(v))

print(f"cumsum", np.cumsum(v))
