x = lambda a : a +10
print(x(5))

y = lambda a, b : a * b
print(y(5,6))

z = lambda a, b ,c : a*b*c
print(z(4,5,6))

def myfunc(n):
    return lambda a : a * n 

mydoubler = myfunc(3)
print(mydoubler(11))

def myfunc1(n):
    return lambda a : a * n

mydoub = myfunc1(5)

print(mydoub(10))
print(mydoub(11))

