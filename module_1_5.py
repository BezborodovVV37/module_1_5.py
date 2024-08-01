immutable_var= 1,2,3,4, True, 'Привет'
print(immutable_var)
mutable_list=([1.2,3,4,5])
print(mutable_list)
(mutable_list)[0]=20
print(mutable_list)
immutable_var[0]=2#кортеж не поддерживает обращение по элементам.
print(immutable_var )

