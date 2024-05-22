def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)
print_params()
values_list = ['one', True, 3]
values_dict = { 'a' : 1, 'b' : 'строка', 'c' : True}
print_params(*values_list)
print_params(**values_dict)
values_list_2 = ['two', False]
print_params(*values_list_2, 42)