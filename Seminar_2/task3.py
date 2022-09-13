# 3. Напишите программу, в которой пользователь будет задавать две 
# строки, а программа - определять количество вхождений одной строки в другой.

# *Пример:*
# 'Я люблю Питон!'
# 'лю'

x = str(input('Input string 1 '))
y = str(input('Input string 2 '))

result = x.count(y)
print(result)

# variant bez funcii:

a = input('введите строку: ')
b = input('введите подстроку: ')
count = 0

for i in range (0, len(a) - len(b)):
    if b == a[i: i + len(b)]:
        count += 1
print(f'{count} раз')



