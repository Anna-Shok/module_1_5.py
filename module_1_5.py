immutable_var = 5, 'apple', 1, True
print(immutable_var)

#immutable_var[2] = 10
#print(immutable_var)
#ERROR
#При выполнении данной операции, нам всегда программа будет выдавать ошибку, так как кортеж - это неизменяемый вид данных.

mutable_list = [ 5, True, 'banana' ]
mutable_list[0] = 10
mutable_list[1] = False
mutable_list[2] = 'apple'
print(mutable_list)