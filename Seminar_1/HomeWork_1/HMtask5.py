# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

# Пример:

# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

# AB = √(x2 - x1)2 + (y2 - y1)2


x1 = int(input("x1 - "))
y1 = int(input("y1 - "))
x2 = int(input("x2 - "))
y2 = int(input("y2 - "))
distanceofpoints = None

distanceofpoints = round(((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5 , 2)

print(distanceofpoints)

