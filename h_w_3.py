import pickle
import random

####extra
li = []
# i=0
# while i <6:
#     li.append(0)
#     i+=1
#
# print(li)

# for i in range (6):
#     li.append(0)
# print(li)
# dict_1={}
# dict_1 ={"a" : 0,
#         "b": 0}
#
# print(dict_1)
# dict_1['a']=1
# dict_1['b']=1
# print(dict_1)
#
# dict_1=dict([('a',2), ("b",2)])
# print(dict_1)
#
# dict_1=dict.fromkeys(['a','b', 'c'], (1,2,3))
# print(dict_1)
#
# dict_1 ={k:0 for k in [1,2,3]}
# print(dict_1)
# dict_1={k:random.randint(1,100) for k in ['a','b','c']}
# print(dict_1)
#
# dict_1.setdefault()


# 1.
# my_t=(5,2,3)
# my_t=(16,)+my_t[1:]
#
# print(my_t)
# print(dir())
# print(eval(str(my_t)))
# print(isinstance(my_t, tuple))

# val = 2 ** 16
# print(val)
# val_1 = 2 / 5, 2 / 5.0
# print(type(val_1), val_1)
# val = 'spam' + 'eggs'
# print(val)
# s = 'ham'
# print('eggs' + s)
# print(s * 5)
# print(s[:0])
# print("green {0}s and {1}s".format('eggs', s))
# # print(('x',) [0])
# print(('x', 'y')[1])
# my_list = [1, 2, 3] + [4, 5, 6]
# print((my_list))
# print(my_list, my_list[:0], my_list[:], my_list[-2], my_list[-2:])
# print(([1, 2, 3] + [4, 5, 6])[2:4])
# print(my_list[2], my_list[3])
# my_list.reverse()
# print(my_list)
# my_list.sort()
# print(my_list)
# print(my_list.index(2))
# print({"a": 1, "b": 2}["b"])
# D = {"x": 1, "y": 2, "z": 3}
# print(D)
# D["w"] = 0
# print(D["w"])
# print(D["x"] + D["w"])
# print(str(D["x"]) + str(D["w"]))
# D[(1, 2, 3,)] = 4
# print(D[(1, 2, 3)])
# print(list(D.keys()), list(D.values()), (1, 2, 3) in D)
#
#
# #2
# L=[0,1,2,3]
# print(L[-1000:100])
# print(L[3:1])

# 3
# L_1 = [1, 2, 3, 4]
# L_1[2] = []
# print(L_1)
# L_1[2:3] = []
# print(L_1)
# del L_1[0]
# print(L_1)
# del L_1[1:]
# print(L_1)
# L_1[1:2] = 1, 2,
# print(L_1)

# 4
# D = {1: 'a',
#      2: 'b',
#      3: 'c'
#      }
# print(D)
#
# D = {v: k for k, v in D.items()}
# print(D)
#
# D['d'] = 'spa'
# print(D)
#
# print(D['d'])
# new_D = {k: v for v, k in D.items()}
# print(new_D)


# 5
# var="a"+["a","a"]
# print(var)
# var = ["a","a"]+(1,2,3)
# print(var)
# var={'a':1}+ "a"
# print(var)
# var ='sap' +"ra"
# print(var[:5])
# S="spam"
# print(S[0][0][0][0][0])
# S = list(S)
# print(S)
# # print(S[0][0][0][0][0])

S = "spam"
var = S[0] + 'l' + S[2:]
print(var)
var = S.replace(S[1], 'l')
print(var)
print(list(S))
var = list(S)
print(var)
var[1] = 'l'
print(var)

person = {"name": {"f_name": 'Valery', "mid": "K", "second_name": "Glory"},
          "age": 19,
          "occupation": "manager",
          "address": {"country": "SP", "city": "Valencia", "CCode": 3200},
          "email": "Glory@gmail.com",
          "mobile": '00224213382014'}

print(person['name']["mid"], person['name']["f_name"])
person['name']["second_name"] = "Chloe"
print(person['name']['second_name'])
person['age'] = 23,

person['occupation'] = 'social worker'
for k, v in person.items():
    if k in 'email':
        v = v.replace('gmail', 'mail')
        print(v)

print(person['email'])

print(person["age"], person['occupation'])

# output=open("my_file", 'r')


# import sys
#
# sys.stdout.write('hello wallet\n')
#
# log = sys.stdout
# sys.stdout = open('b.txt', 'a')
# print('s')
# print('hello', file=log)
# print('z')


y=3
x = y //2
while x > 1:
    if y% x == 0:
            print(x, "has factor", y)
            break
    x -= 1
else:
    print(y, "is spam")



# def match(num):
#         found = False
#         x = ('10', '20', '30')
#         while x and not found:
#             if match(x[0]):
#                 print("Ni")
#                 found = True
#             else:
#                 x = x[1:]
#         if not found:
#             print("not found")
#
# my_x= ('0','1','2','3','4','5')
# print(match(my_x))

from functools import reduce
def a_b(a:int,b:int, *args, **kwargs):
        val = args
        val2 = kwargs
        # print(val[:1])
        res = a+b + reduce(lambda x,y:x+y, args)
        return (res)



print(a_b(1,2,3,4,  r=16, w='w' ))



# eval()
# print(dir(exec()))


# E=dict.fromkeys(['a','b', 'c'], ('1', '2' ,'3') )
# print(E)
#
# F ={k:1 for k in['a','b', 'c']}
# print(F)


############################################
# my_list = [10, 9, 1, 2, 8, 7, 3, 4, 6, 5]
# num = -1
# num2 = [-2, -5, -7]


# #1.a
# def append_obj_num(obj: list, number: int):
#     obj.append(number)
#     return obj
#
#
# print(append_obj_num(my_list, num))
#
#
# #2.a
# def extend_list(obj: list, input: list):
#     obj.extend(input)
#     return obj
#
#
# print(extend_list(my_list, num2))
#
#
# #3.a
# my_list.insert(2, 9)
#
# #4.a
# var, var1, var2 = my_list.count(1), my_list.count(9), my_list.count(-10)
# print(var, var1, var2)
#
# #5.a
# res = my_list.index(7)
# print(res)
#
# #6.a
# var3 = -2
# var4 = -10
# if var3 in my_list:
#     print(f'{var3} is in the list {my_list}')
# if var3 not in my_list:
#     print(f'{var3} is not in the list {my_list}')
# if var4 in my_list:
#     print(f'{var4} is in the list {my_list}')
# if var4 not in my_list:
#     print(f'{var4} is not in the list {my_list}')
#
#
# #7.a
# my_list.sort()
# print(my_list)
#
# #8.a
# my_list.reverse()
# print(my_list)


##########################################################
##########################################################


##########################################################
##########################################################
# 1.c
# my_list+=[-1]
# print(my_list)
# #2.c
# my_list[len(my_list):] = list(num2)

# 3
# srch_set = (set([-2, -10]) & set(my_list))
#
# #5
# ind_7 = next((i for i, k in enumerate(my_list) if k ==7), None)
#
# #8
# rev_ers= sorted(my_list[::-1])
#
#
# print(f'2.\t {my_list}')
# print(f"3.\t {srch_set} exists in the Data")
# print(f"5.\t index, you ask for is {ind_7}")
# print(f"8.\t {rev_ers}")
