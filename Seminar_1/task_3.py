# 1. Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N
    
#     *Примеры:* 
    
#     - 5 -> -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5
# 2. Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.
    
#     *Примеры:*
    
#     - 6,78 -> 7
#     - 5 -> нет
#     - 0,34 -> 3
# 3. Напишите программу, которая принимает на вход число и проверяет, кратно ли оно 5 и 10 или 15, но не 30

# # 1.
# n = int(input('Введите число N: '))
# for i in range(-n, n + 1):
#      print(f'*{i}* ')

#  2 zadacha через индекс в строке
# number = input("Input number: ")

# print(number[-2])

# number = input("Input number: ")
# print(number.split('.')[1][0])


# number = float(input("Input number: "))
# number *= 10
# print(number)
# number = int(number)
# print(number)
# print(number % 10)


# 3 zadacha
num=int(input("Введите число: "))
if (num%5==0) and (num%10==0):
    print ("число ", num, "Кратно 5 и 10")
if (num%15==0) and (num%30!=0):
    print ("число ", num, "Кратно 15, но не кратно 30")


2 вариант
num = int(input("Введите число: "))
if ((num % 5 == 0) and (num % 10 == 0)) or ((num % 15 == 0) and (num % 30 != 0)):
    print("Да")
else:
    print("Нет")




# # num_2 = (input('введите число N:'))
# # print()

# N = int(input('введите число N:'))
# if N % 5 = 0:
#     print(N is 'Odd')