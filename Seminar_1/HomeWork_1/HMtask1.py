
# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:

# - 6 -> да
# - 7 -> да
# - 1 -> нет

DayOfWeek = int(input('Put the number:'))

if DayOfWeek > 5: 
    print('Congratulations, it is a Weekend!')
else:
    print(' Bad for you, it is a Working day :(')    
