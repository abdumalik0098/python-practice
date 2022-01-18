s1 = "Malik"
s2 = "Class '4a'"
s3 = '''I am django developer
I love Python'''

print(s1)
print(s2)
print(s3)

s4 = str(235)
print(s4)

s5 = "Malik"
s6 = "Khidirov"
print(s5+s6)
print(s5+' '+s6)
# Размножаем строки с помощью символа *
s7 = 'Say me! ' * 5
print(s7)
# Извлекаем символ с помощью символов [ ]
s8 = s5[3] + s6[-5]
print(s8)

# Извлекаем подстроки,используя разделение: Оператор [ начало : конец : шаг]

s9 = s5[:] + " " + s6[:3] + ' '+ s2[4:] + ' ' + s3[6:20:3]
print(s9)

# Измеряем длину строки с помощью функции len()
s10 = len(s9)
print(s10)

# Разделяем строку с помощью функции split()

s11 = s3.split()
print(s11)

for item in s11:
    print(item)

# Объединяем строки с помощью функции join()
s12  = s1 + " ".join(s2)
print(s12)

# Регистр
s13 = 'calm it'
s13 = s13.capitalize()
print(s13)
s13 = s13.title()
print(s13)
s13 = s13.upper()
print(s13)
s13 = s13.lower()
print(s13)


# Самый новый стиль: f-строки
thing = 'wereduck'
place = 'werepond'
print(f'The {thing} is in the {place}')

