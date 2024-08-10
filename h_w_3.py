my_list = [10, 9, 1, 2, 8, 7, 3, 4, 6, 5]
num = -1
num2 = [-2, -5, -7]


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
#1.c
my_list+=[-1]
print(my_list)
#2.c
my_list[len(my_list):] = list(num2)

#3
srch_set = (set([-2, -10]) & set(my_list))

#5
ind_7 = next((i for i, k in enumerate(my_list) if k ==7), None)

#8
rev_ers= sorted(my_list[::-1])


print(f'2.\t {my_list}')
print(f"3.\t {srch_set} exists in the Data")
print(f"5.\t index, you ask for is {ind_7}")
print(f"8.\t {rev_ers}")