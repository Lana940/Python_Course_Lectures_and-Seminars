print('hello world')

# тип данных и переменные : int, float, boolean, str, list, None(можно присвоить переменной чтоб использовать ее дальше в коде)
a = 123
b = 1.23
s = 'hello world' #\n перенос на новую строку

print(s) 
print(a,'-',b, '-',s )
print('{} - {} - {}'.format(a,b,s ))
print('{1} - {2} - {0}'.format(a, b, s)) # по индексам поменять местами можно
print(f'{a} - {b} - {s}') 

f = True
print(f)

list =[1,5,2,5,5,1]
list = ['1', '2', '3','5','hello']  #'для строки'
col = [1,2,3]
print(list)
print(col)


ПО УМОЛЧАНИЮ СТРОКИ
print('Введите а');
a = input() 
print('Write b');
b = input()
print(a, '+', b, '=',  a+b)  20 + 41 = 2041
print('{} {}}'.format(a, b))
print(f'{a} {b}')

ДЛЯ ЦЕЛОГО ЧИСЛА

print('Введите а');
a = float(input()) 
print('Write b');
b = float(input())
print(a, '+', b, '=',  a+b)

+, -, *, /, %, //, **

**, ⊕, ⊖, *, /, //, %, +, -
( ) Скобки меняют приоритет

a = 12
b =  5
c = a // b # // 2 деления для вывода рез-та в целых числах, не 1,5 а 1 и тд
print(c)

a = 1.3123155446
b =  3
c = round(a * b, 7)
print(c)

Сокращенные операции присваивания 

а += 5
а *= 5

Логические операции
>, >=, <, <=, ==, !=
not, and, or – не путать с &, |,
^
Кое-что ещё: is, is not, in, not in 

a = 1 < 4 and 5 > 2
print(a)

a = 'qwe'
b = 'qwe'
print (a == b)

a = 1 < 3 < 5
print(a)

func = 1
t = 4
x = 123

print(func < t > x)

f = 1 > 2 or 4 < 6
print(f)

f = [1,2,3,4]
print(f)
print(2 in f)

f = [1,2,3,4]
# print(f)
# print(not 2 in f)

is_Odd = f[0] % 2 == 0 # = not f[0] % 2
print(is_Odd)

a = int(input('a = '))
b = int(input('b = '))
if a>b:
    print(a)
else:
    print(b)    

Logicheskiy Operator

username = input (' Put the name: ')
if username == 'Masha':
    print('Ura eto zhe Masha!')
elif username == 'Marina':
    print('Yq tak zhdala Was, Marina!')
elif username == 'Ilnar':
    print('Ilnar - TOP!')
else:
    print('Privet, ', username)

   WHILE

original = 23
inverted = 0
while original != 0:
    inverted = inverted * 10 + (original % 10)
    original //= 10
print(inverted)

original = 23
inverted = 0
while original != 0:
    inverted = inverted * 10 + (original % 10)
    original //= 10
    print(original)
else:
    print('Pozhaluy hvatit')
print(inverted)


#       FOR
for i in 1,2,3,4,5:
    print(i**2)

list = [1,2,3,4,15,5]
for j in list:
    print(j)


  RANGE  укажет последовательность

r = range (10)
for i in r:
    print(i)  

for i in range(1,10, 2):  # 1 - 10 диапазон, а 2 шаг
    print(i)

for i in 'qwe -rty':  # 1 - 10 диапазон, а 2 шаг
    print(i)

СТРОКИ
text = 'съешь ещё этих мягких французских булок'
print(len(text)) # 39
print('ещё' in text) # True
print(text.isdigit()) # False
print(text.islower()) # True
print(text.replace('ещё','ЕЩЁ')) #
for c in text:
 print(c)

Список – пронумерованная, изменяемая коллекция
объектов произвольных типов

numbers = [1, 2, 3, 4, 5]
print(numbers)            # [1, 2, 3, 4, 5]
ran = range(1, 6)
print(type(ran))

numbers = list(ran)
print(type(numbers))

print(numbers)          # [1, 2, 3, 4, 5]
numbers[0] = 10
print(f'{len(numbers)} len')
print(numbers)           # [10, 2, 3, 4, 5]
for i in numbers:
 i *= 2
 print(i)              # [20, 4, 6, 8, 10]
print(numbers)           # [10, 2, 3, 4, 5]

colors = ['red', 'green', 'blue']
for e in colors:
 print(e) # red green blue
for e in colors:
 print(e*2) # redred greengreen blueblue
colors.append('gray') # добавить в конец
print(colors == ['red', 'green', 'blue', 'gray']) # True
colors.remove('red') #del colors[0] # удалить элемент

Функции

def f(x):
 if x == 1:
     return 'Целое'

 elif x == 2.3:
    return 23
 else:
     return

arg = 1
print(f(arg))
print(type(f(arg)))
