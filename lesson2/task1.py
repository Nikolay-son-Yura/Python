# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11
import re  # найдено на просторах интернета, с точкой под коментом

number = float(input("Введите число: "))
number = str(number)
x = re.split("[.,]+", number)  # тут или через тчк или через зпт
# x = number.split(".")
whole = int(x[0])
fraction = int(x[1])
sum_num = 0
while whole != 0:
    sum_num = sum_num + (whole % 10)
    whole //= 10
while fraction != 0:
    sum_num = sum_num + (fraction % 10)
    fraction //= 10
print(int(sum_num))
