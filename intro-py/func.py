def tp():
    return 28, "abd", 34.6

a, b, c = tp()
t = tp()

print(a, b, c)
print(t)

# Generators - 1

def mygen():
    yield 42

g = mygen()
print(next(g))

# 2

def mygen():
    for i in range(1,5):
        yield i
g = mygen()
print(next(g))
print(next(g))
print(next(g))
print(next(g))

def fib(n):
    result = []
    a, b = 0 , 1
    while a < n:
        result.append(a)
        a, b, = b, a+b
    return result
print(fib(100))

def rec_fib(n):
    if n<=1:
        return n
    return rec_fib(n-1) + rec_fib(n-2)

print(rec_fib(10))

# lambda

def exp():
    return lambda: 98

print(exp())
print(exp()())

def exp(x):
    return lambda y: y**x

print(exp(2)(4))