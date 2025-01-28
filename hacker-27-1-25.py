import numpy as np

X, Y = map(int, input().split())

array = np.array([list(map(int, input().split())) for i in range(X)])

mean_res = np.mean(array, axis=1)
var_res = np.var(array, axis=0)
std_res = round(np.std(array), 11)

print(mean_res)
print(var_res)
print(std_res)


A = np.array(list(map(int, input().split())))
B = np.array(list(map(int, input().split())))

inner_product = np.inner(A, B)
print(inner_product)

outer_product = np.outer(A, B)
print(outer_product)
