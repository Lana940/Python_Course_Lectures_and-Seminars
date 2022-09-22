# colors = ['red', 'green', 'blue']
# data = open('file.txt', 'a')
# #data.writelines(colors) #произвели запись без пробела
# data.write('\nLine 2\n')
# data.write('Line 13\n')
# data.close()


# #Другой вариант записи где data.close() происходит автоматически:
# # with open('file.txt', 'w') as data:
# #      data.write('line 1\n')
# #       data.write('line 2\n')

# exit() # <- позволяет не выполнять скрипт ниже нее
path = 'file.txt'
data = open(path, 'r')
for line in data:
    print(line)
data.close()