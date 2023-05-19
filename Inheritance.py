# Parent Class
# Child Class

class Inheritance:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname

    def myfunc(self):
        print(self.fname, self.lname)

p = Inheritance("Sunny","Goli")
p.myfunc()