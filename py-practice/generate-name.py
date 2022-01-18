import sys, random

print("Добро пожаловать в 'Подбор имен для напарника.'\п")

first = ('Baby Oil1', 'Bowel Noises', 'Boxelder', "Bud 'Lite' ",
'Butterbean', 'Buttermilk', 'Buttocks', 'Chad',
'Chesterfield', 'Chewy', 'Chigger", "Cinnabuns', 'Cleet',
'Cornbread', 'Crab Meat', 'Crapps', 'Dark Skies',
'Dennis Clawhammer', 'Dicman', 'Elphonso', 'Fancypants',
'Figgs', 'Foncy', 'Gootsy', 'Greasy Jim', 'Huckleberry',
'Huggy', 'Ignatious', 'Jimbo', "Joe 'Pottin Soil'", 'Johnny',
'Lemongrass', 'Lil Debil', 'Longbranch', '"Lunch Money"',
'Mergatroid', '"Mr Peabody"', 'Oil-Сап', 'Oinks',
'Old Scratch', 'Ovaltine', 'Pennywhistle', 'Pitchfork Ben')

last = ('Appleyard', 'Bigmeat', 'Bloominshine', 'Boogerbottom',
'Breedslovetrout', 'Butterbaugh', 'Clovenhoof', 'Clutterbuck',
'Cocktoasten', 'Endicott', 'Fewhairs', 'Gooberdapple', 'Kingfish', 'Listenbe',
'M’Bernbo', 'Nettles', 'Noseworthy', 'Olivetti', 'Outerbridge', 'Overpeck', 'Overturf', 'Oxhandler')

while True:
    firstName = random.choice(first)
    lastName = random.choice(last)
    print("\n\n")
    print("{} {}".format(firstName, lastName), file=sys.stderr)
    print("\n\n")
    try_again = input("\nПопробуете еще? (Нажмите Enter либо n, чтобы выйти) \n ")
    if try_again.lower() == "n":
        break
input("\nНажмите Enter для завершения работы.")