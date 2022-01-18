"""Списки же можно изменять — добавлять и удалять элементы
в любой удобный момент."""

empty_list = [ ]
weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
big_birds = ['emu', 'ostrich', 'cassowary']
first_names = ['Graham', 'John', 'Terry', 'Terry', 'Michael']
leap_years = [2000, 2004, 2008]

a = 'developer'
l1 = list(a)
print(l1)

day = '9/19/2019'
l2 = day.split('/')
print(l2)

l3 = l1[5]
print(l3)

# Добавляем элемент в конец списка с помощью функции append()
l2.append('year')
print (l2)

# Добавляем элемент на определенное место с помощью функции insert()
l2.insert(2, "month")
print (l2)

# Изменяем элемент с помощью конструкции [смещение]
l2[1] = 23
print(l2)

# Удаляем заданный элемент с помощью оператора del
del l2[2]
print(l2)

# Удаляем элемент по значению с помощью функции remove()
l2.remove('year')
print(l2)

# Получаем и удаляем заданный элемент с помощью функции pop()
l2.pop()
print(l2)

# Проверяем на наличие элемента в списке с помощью оператора in
print(23 in l2)

# Итерируем по нескольким последовательностям с помощью функции zip()

for list1, list2 in zip(l1,l2):
    print(l1, " ", l2)

days = ['Monday', 'Tuesday', 'Wednesday']
fruits = ['banana', 'orange', 'peach']
drinks = ['coffee', 'tea', 'beer']
desserts = ['tiramisu', 'ice cream', 'pie', 'pudding']
for day, fruit, drink, dessert in zip(days, fruits, drinks, desserts):
    print(day, ": drink", drink, "eat", fruit, "enjoy", dessert)

    