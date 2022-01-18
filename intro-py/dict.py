"""Словарь очень похож на список, но порядок элементов в нем не имеет значения и они
не выбираются смещением, таким как 0 и 1. Вместо этого для каждого значения вы
указываете связанный с ним уникальный ключ"""


d1 = { "Iphone": '13', 'Samsung': 'A15', 'Nokia': '3310'}
d2 = dict(name="Jack", lname="London", course = 3)

for key in d1.keys():
    print(key)

for value in d1.values():
    print(value)

for item in d1.items():
    print(item)

d2['course'] = 4
print(d2)

d4 = d1['Nokia']
d5 = d1.get('Samsung')
print(d4, d5)

