import numpy as np

X, Y = map(int, input().split())

array = np.array([list(map(int, input().split())) for _ in range(X)])
row_min = np.min(array, axis=1)
result = np.max(row_min)
print(result)
