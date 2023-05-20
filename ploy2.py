class Vehicle:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Move")

#Inheritance
class car(Vehicle):
    pass

#Inheritance
class boat(Vehicle):
    def move(self):
        print("sail")

#Inheritance
class plane(Vehicle):
    def move(self):
        print("Fly")

c1 = car("Ford","001")
b1 = boat("Mercedes","Mer-001")
p1 = plane("Airbus","0012")

#c1.move()
#b1.move()
#p1.move()

for x in (c1,b1,p1):
    print(x.brand)
    print(x.model)
    x.move()