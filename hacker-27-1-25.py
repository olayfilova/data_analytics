import numpy as np

X, Y = map(int, input().split())

array = np.array([list(map(int, input().split())) for i in range(X)])

mean_res = np.mean(array, axis=1)
var_res = np.var(array, axis=0)
std_res = round(np.std(array), 1)

print(mean_res)
print(var_res)
print(std_res
