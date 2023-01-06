# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в отдельном списке( пример n=4, lst1=[4,-2,1,3] - списко на основе n, а позиции элементов lst2=[3,1].
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
# тут произведение элиментов списка
# lst1=[4,-2,1,3]
# lst2=[3,1]
# print(lst1)
# print(lst2)
# mult=1
# i=0
# while i< len(lst2):
#     mult *=lst1[lst2[i]]
#     print(lst1[lst2[i]])
#     i+=1
# print('произведение элиментов ', mult)