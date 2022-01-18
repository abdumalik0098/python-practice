from functools import reduce

num = range(2,5)
res = reduce(lambda x,y: x*y, num)
print(res)