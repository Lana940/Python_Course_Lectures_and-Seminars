
# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:

# - 6 -> да
# - 7 -> да
# - 1 -> нет

# DayOfWeek = int(input('Put the number:'))

# if 6 <= DayOfWeek <= 7: 
#     print('Congratulations, it is a Weekend!')
# elif 0 < DayOfWeek < 6: 
#     print(' Bad for you, it is a Working day :(')    
# else: 
#     print('The number is out of week range, try another number')


num = int(input('Put the day of the week: '))

list = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
if num == (6 or 7):
    print(f'{list[num - 1]} day off')
else: 
    print(f'{list[num - 1]} working day')

