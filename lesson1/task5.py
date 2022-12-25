# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21
import math
num_A_X = int(input('Введите координаты точки A по оси Х : '))
num_A_Y = int(input('Введите координаты точки A по оси Y : '))
num_B_X = int(input('Введите координаты точки B по оси Х : '))
num_B_Y = int(input('Введите координаты точки B по оси Y : '))
square_X = num_B_X - num_A_X
square_X = square_X**2
square_Y = num_B_Y - num_A_Y
square_Y = square_Y**2



distance= math.sqrt(square_X + square_Y)
print(distance)