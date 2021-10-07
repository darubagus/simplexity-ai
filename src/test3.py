import numpy as np

matrix = np.arange(42).reshape(6, 7)
print(matrix)
x = np.fliplr(matrix)
print(np.diagonal(matrix, offset=1))
print(np.diagonal(x, offset=1))

