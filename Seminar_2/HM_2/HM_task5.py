# Реализуйте алгоритм перемешивания списка.:

import random

n = int(input("введите размер списка: "))
random_list = [] 
for i in range(0, n): 
    random_list.append(random.randint(-n,n))
print(random_list)

for i in range(n):
    j = random.randint(0, n-1)
    element = random_list.pop(j)
    random_list.append(element)

print(random_list)





# Examples of methods for list shuffle :

# random.shuffle(random_list)  - integrated Python list shuffle method
# print(random_list) 

# new_arr = random.sample(random_list, 5)  - in random.sample() - we can also specify the number of sampled elements that we want to get as a result
# print(new_arr) 

# or new_list = random.sample(random_list, len(random_list))  - for the whole length of the list 
# print(new_list) 