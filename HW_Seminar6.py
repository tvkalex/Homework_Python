# Задача 30: Заполните массив элементами арифметической прогрессии.
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.
# Ввод: 7 2 5
# Вывод: 7 9 11 13 15

a1 = int(input("Введите первый элемент арифметической прогрессии a1: "))
d = int(input("Введите разность элемента арифметической прогрессии d: "))
n = int(input("Введите количество элементов арифметической прогрессии n: "))

for i in range(n):
    print(a1 + i * d, end=' ')

# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)
# Ввод: [-5, 9, 0, 3, -1, -2, 1, 4,-2,10,2,0,-9,8,10,-9, 0, -5, -5, 7]
# Вывод: [1, 9, 13, 14, 19]

# list_1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# min_num = int(input("Введите минимальное значение элемента: "))
# max_num = int(input("Введите максимальное значение элемента: "))
# while min_num > max_num:
#     n = input("Вы ошиблись!\nМаксимальное значение элемента не может быть меньше минимального значения элемента: ")
#
# for i in range(len(list_1)):
#     if min_num <= list_1[i] <= max_num:
#         print(i, end=' ')

list_1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
min_number = 0
max_number = 10

for i in range(len(list_1)):
    if min_number <= list_1[i] <= max_number:
        print(i, end='\n')
