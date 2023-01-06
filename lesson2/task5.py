# Реализуйте алгоритм перемешивания списка. (рандомно поменять местами элементы списка между собой)


import random

numb = int(input('Введите число '))
def fill_list(n): 
    new_list = [random.randint(-n, n)]
    for i in range(1, n):
        new_list.append(random.randint(-n, n))
        i += 1
    return new_list
lst1=fill_list(numb)
print(lst1)

def mix_list(lst):
    for i in range(len(lst)):
        index_aleatory = random.randint(0, len(lst) - 1)
        temp = lst[i]
        lst[i] = lst[index_aleatory]
        lst[index_aleatory] = temp
    return lst
print(mix_list(lst1))