from collections import namedtuple
from  dataclasses import dataclass
import sys
import binascii



# S= 'hello world'
# sum =0
# for i in S:
#     print(ord(i))
#     sum += ord(i)
# print(sum)
#
# ascii_code = []
# for i in S:
#     ascii_code.append(ord(i))
# print(ascii_code)
#
# ascii_code2 = list(map(ord, S))
# print(ascii_code2)
#
# ascii_code3=[ord(i) for i in S]
# print(ascii_code3)


# for i in range (50) :
#     print(f'hello {i}\n\a')

# D = {"a":1, '2':2, "b":'hey', "1":"g"}
# print(list(sorted(D)))
# print(sorted(D))

# L = [1, 2, 4, 8, 16, 32, 64]
# X=5
# found = False
# i=0
#
# while i < len(L):
#     if 2 ** X == L[i] :
#         print('at index', i)
#         break
#     i = i+1
# else:
#         print(X, 'not found')



# L = [1, 2, 4, 8, 16, 32, 64]
# X=5
# for i, v in enumerate(L):
#     if 2 ** X  == v:
#         print("index ==",i)
#         break
# else:
#     print(X, " not here")

L = [1, 2, 4, 8, 16, 32, 64]
X=5

# for i in L:
#     if 2 **X  == i:
#         print( "index =)", L.index(i)) #if 2 ** X == L[i] else (X, " not here")  ])
#         break
# else:
#         print(X, " not here")
#
#
# res = [2**i for i in L]
# print(res)

# res = [('index@', L.index(i) ) for i in L if 2 ** X == i]
# print(res)

res = [f"indx@ {i}" for i in range(len(L)) if 2 ** X == L[i]]
print(res)

print(res[0] if res else f"{2 ** X}not here")











# point = namedtuple('Point', ['x', 'y'])
# p= point(x=11, y=22)
# print(p)


# @dataclass
# class InventoryItems:
#     name: str
#     unit_price: float
#     quantity_on_hand: int = 0
#
#     def total_cost(self):
#         return self.unit_price * self.quantity_on_hand
#
#
#
# print(InventoryItems('Bike', 560, 2).total_cost())
#
# print(len(dir(sys)))
# print(len([x for x in dir(sys) if not x.startswith('__')]))
# print(len([x for x in dir(sys) if not x[0]=="_"]))
# print(len(dir([])), len([x for x in dir([]) if not x.startswith('__')]))
# print(len(dir('')), len([x for x in dir('') if not x.startswith('__')]))
# print([x for x in dir(list) if not x.startswith("__")])
# print([x for x in dir(dict) if not x.startswith("__")])
#
# def dir_x(x):
#     return [x for x in dir() if not x.startswith("__")]
#
#
# print(help(sys))




###1
# def conv_temperature(temp_val: float, scale='C_to_F'):
#     if scale =='C_to_F':
#         res = (temp_val*1.8)+32
#         return res
#     elif scale =='F_to_C':
#         res=(temp_val-32)/1.8
#         return(res)
#     else:
#         raise ValueError('''Choose "C_to_F" - celsius to fahrenheit, or "F_to_C" - fahrenheit to celsius''')
#
#
# val =conv_temperature(25, 'F_to_C')
# print(val)


##2
# eu_size = [36, 37, 38, 39, 40, 41, 42, 43, 44, 45]
# us_size = [6, 6.5, 7, 7.5, 8, 8.5, 9, 9.5, 10, 10.5]
#
#
# li_zip = list(zip(eu_size, us_size))
# print(li_zip)
#
#
#
# eu_size=40
# us_size = next(filter(lambda x: x[0]== eu_size, li_zip))[1]
# print(us_size)
#
# us_size=7
# eu_size = next(filter(lambda x: x[1]==us_size, li_zip))[0]
# print(eu_size)