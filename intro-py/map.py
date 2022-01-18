values = [12, 3, 56, 7]
mapped = map(lambda x: x+10, values)
list2 = list(mapped)
print(list2)
list2 = list(mapped)
print(list2)


def exp(x):
    return lambda y: y**x

a=2
funcs = (exp(x) for x in range(1,9))
list3 = list(map(lambda f: f(a), funcs))
print(list3)