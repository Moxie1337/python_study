import numpy as np

a = np.arange(8).reshape((2, 2, 2))

print(a)

print(np.max(a))

print(np.max(a, axis = 0))

print(np.max(a, axis = (0, 1)))

print(np.max(a, axis = (0, 1, 2)))