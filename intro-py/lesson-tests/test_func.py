def getname(name, lname, middle=None):
    if middle:
        fullname = f'{name} {middle} {lname}'
    else:
        fullname = f'{name} {lname}'

    return fullname.title()
