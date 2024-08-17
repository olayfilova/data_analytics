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
eu_size = [36, 37, 38, 39, 40, 41, 42, 43, 44, 45]
us_size = [6, 6.5, 7, 7.5, 8, 8.5, 9, 9.5, 10, 10.5]


li_zip = list(zip(eu_size, us_size))
print(li_zip)

eu_size=40
us_size = next(filter(lambda x: x[0]== eu_size, li_zip))[1]
print(us_size)

us_size=7
eu_size = next(filter(lambda x: x[1]==us_size, li_zip))[0]
print(eu_size)