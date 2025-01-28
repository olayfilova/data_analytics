import numpy as np
from itertools import product

X, Y = map(int, input().split())
arr = np.array([list(map(int, input().split())) for _ in range(X)])
sum_result = np.sum(arr, axis=0)
prod_result = np.prod(sum_result)

print(prod_result)
##
list1 = [1, 2]
list2 = ['a', 'b']

result = product(list1, list2)
print(list(result))
##
X, Y = map(int, input().split())

array = np.array([list(map(int, input().split())) for _ in range(X)])
sum_result = np.sum(array, axis=0)
product_result = np.prod(sum_result)
print(product_result)
