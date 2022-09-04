2. НАпишите программу, которая на вход принимает 5 чисел и находит максимальное из них 
   Примеры:
    
    - 1, 4, 8, 7, 5 -> 8
    - 78, 55, 36, 90, 2 -> 90

Zapolnili massiv(list) Создание списка:
my_list = []
for i in range(5):
    num = int(input('--> '))
    my_list.append(num)
print(my_list)

Автоматическая функция Питона 

my_list = [3,5,1,2,8]
print(max(my_list))

my_list = [ - 3,5,1,2, -8]
maxx = my_list[0]
for item in my_list:  #срез т.е проверк от 2 ел до 4 for item in my_list[1: 4]:
    if item > maxx:
        maxx = item
print(maxx)

поиск индекса наибольшего елемента
my_list = [3, 5, 1, 2, 8]
maxx = my_list[0]
maxx_i = 0
for i in range(1, len(my_list)):
    if my_list[i] > maxx:
        maxx = my_list[i]
        maxx_i = i

print(maxx, maxx_i)






list = [1,4,8,7,5]
max = list[0]

i = 1
while i < 5:
    if max < list[i]:
        max = list[i] 
    i += 1
print(max)


num_1 = int(input('Введите число 1: '))
num_2 = int(input('Введите число 2: '))
num_3 = int(input('Введите число 3: '))
num_4 = int(input('Введите число 4: '))
num_5 = int(input('Введите число 5: '))
max = num_1
if max < num_2:
    max = num_2
if max < num_3:
    max = num_3
if max < num_4:
    max = num_4
if max < num_5:
    max = num_5
print(max)



