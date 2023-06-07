# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)
import random
a = int(input('Введите количество элементов списка -> '))
min = int(input('Введите нижний диапазон списка -> '))
max = int(input('Введите верхний диапазон списка -> '))
list_1 = list()
list_2 = list()

for i in range(a):
    list_1.append(random.randint(1, 25))
    if list_1[i] < max and list_1[i] > min:
        list_2.append(i)
print(list_1)
print(list_2)

