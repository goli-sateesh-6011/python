class iter1:
    def __iter__(self):
        self.a = 1
        return self
    
    def __next__(self):
        if self.a <= 20:
            x =self.a
            self.a += 1
            return x
        else:
            raise StopIteration
        

it = iter1()
myiter = iter(it)

for x in myiter:
    print(x)