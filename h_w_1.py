# #2a
# type = type(2*3)
# print(f"TYPE IS {type}, and result is {(2*3)}")

# #b
# val_1 = 3
# val_2 = 3 
# val_3 = 8
# val_4 = 3

# res = (val_1 * val_2 + val_3)/val_4
# print(res, type)

# #c
# val_1 = 8
# val_2 = 3
# res = val_1//val_2
# print(res, type)

# #d
# res2 = (val_1) % (val_2)
# print(res2, type)

# #e
# res = 5**2
# print(res, type)

# #f
# val_1 = 'Hello'
# val_2 = 'Word'
# print((val_1 + val_2), type)


# #3
# str_1 = 'INPUT'
# str_2 = "TOTAL"


#4a
input_list = ["abcdeqwertyuiopasdfg", "12345678901234567890", '09876543210987654321', 'the weather is not hot,']
for i in input_list:
    print(i[:10])


#b
start_from = 3
length_numb = 10
input_str = "1134567890123456789"


def from_x_plus_y(input_str: str, start_from: int, length_numb: int):
    if len(input_str) < 12:
        print("for proceeding min length in the input should be  12")

    start_x = start_from - 1
    end_y = start_x + length_numb

    if end_y > len(input_str):
        print("The 'length_num' input is longer than the 'input_numb'. Please try again")
    return input_str[start_x:end_y]


# print(from_x_plus_y(input_str, 3, 10))


#b.list
input_list = ["abcdeqwertyuiopasdfg", "12345678901234567890", '09876543210987654321', 'the weather is not hot,']


def from_x_plus_y_list(input_list: list, start_from: int, length_numb: int):
    res = []
    for i in input_list:
        if len(i) < 12:
            print("for proceeding min length in the input should be  12")
        start = start_from - 1
        end = start_from + length_numb
        res.append(i[start:end])

    return res


print(from_x_plus_y_list(input_list, start_from, length_numb))


#c,d
print([i[-10:] for i in input_list])
print([i[::-1] for i in input_list])


# e
for i in input_list:
    if input_list.index(i) % 2 == 0:
        print(i[::2])

print(i[1::2])
