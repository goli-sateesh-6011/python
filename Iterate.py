mytuple=('mango','Apple','Pineapple')
myit =  iter(mytuple)
print(next(myit))

for x in mytuple:
    print(x)


class Mynumbers:
    def __iter__(self):
        self.a = 1
        return self
    
    def __next__(self):
        x = self.a
        self.a += 1
        return x
    
myclass = Mynumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))