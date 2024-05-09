immutable_var = 1, True, 'string'
print(immutable_var)
# immutable_var[0] = 254 #Изменять значения можно в списках. Кортеж данную функцию не поддерживает!
mutable_list = ['one', 'two', 'three']
mutable_list[0] = 1
print(mutable_list)