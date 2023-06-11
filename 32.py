# Задача 32: Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

list_1 = []
n = int(input('enter number of elements: '))
for i in range(n):
  list_1.append(int(input(f'enter {i} element massiv: ')))
print(list_1)
min = int(input('enter min: '))
max = int(input('enter max: '))
for i in range(len(list_1)):
  if min <= list_1[i] <= max:
    print(i)
