# Заполните массив элементами арифметической прогрессии. 
# Её первый элемент, разность и количество элементов нужно 
# ввести с клавиатуры. Формула для получения n-го члена прогрессии:
# an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.
a1 = int(input('enter first element: '))
d = int(input('enter step: '))
n = int(input('enter end element: '))
list_1 = []
for i in range(n):
  list_1.append(a1 + i * d)
print(list_1)
for i in list_1:
  print(i)