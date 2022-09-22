# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных пользователем через пробел позициях.

n = int(input("Введите длину списка: "))

for i in range(-n, n + 1):
    my_list = [(-n, n + 1)] # tak sgen spisok ot -5 do 5 iz 11 elem

print(my_list)

import random

n = int(input('введите число: '))
random_list = [] 
for i in range(0, n): 
    random_list.append(random.randint(-n,n))
print(random_list)


# # num_1 = input(' введите index элемента: ')

# # print(num_1.split())

# # mult = 1
# # mult *= random_list[num_1]
# # print(mult)



