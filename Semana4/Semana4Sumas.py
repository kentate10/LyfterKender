#pruebas Sumas

sum_string  = 'kender' + 'Tate'
print(sum_string)
#-------------------------------#
#str+int 
number = 4
sum_str_int = 'kender' + str(number)
print(sum_str_int)
#-------------------------------#
#int+str
number_str = '4'
sum_int_str = 4  + int(number_str)
print(sum_int_str)
#-------------------------------#
#list+list
sample_list = ['Kender', 'Keylor', 'Dereck', 'Valeria']
sample_list2 = ['Ash','Aly','Brianna']
print(f'Lista 1 {sample_list}, Lista 2 {sample_list2}')
sum_list = sample_list2 + sample_list
print(sum_list)
#-------------------------------#
#str+list
sum_string_li = 'Braulio, ' + ', '.join(sample_list)  
print(sum_string_li)
#-------------------------------#
#float + list
sum_float_int = 3.33 + 4
print(sum_float_int)
#-------------------------------#
#boolean+boolean
sum_bool = False + True
sum_bool2 = True  + True
sum_bool3 = False  + False
print(sum_bool, sum_bool2, sum_bool3)