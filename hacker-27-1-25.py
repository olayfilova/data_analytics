import numpy as np

X, Y = map(int, input().split())

array = np.array([list(map(int, input().split())) for i in range(X)])

mean_res = np.mean(array, axis=1)
var_res = np.var(array, axis=0)
std_res = round(np.std(array), 11)

print(mean_res)
print(var_res)
print(std_res)


A = np.array([1, 2, 3])  # First vector
B = np.array([4, 5, 6])  # Second vector

cross_product = np.cross(A, B)  # Calculate the cross product
print(cross_product)
