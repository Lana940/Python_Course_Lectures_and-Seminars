# 1. Напишите программу, которая принимает на вход число N и 
# выдаёт последовательность из N членов.
    
#     *Пример:*
#     - Для N = 5: 1, -3, 9, -27, 81

number = int(input("Введите число: "))
numbers = [1]

for i in range (number - 1):
    num = (numbers[i] * -3)
    numbers.append(num)
print(numbers)


