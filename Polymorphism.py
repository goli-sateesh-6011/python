class car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Move")

class boat:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Sail")

class plane:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Fly")

    
car1 = car("Ford","M1")
boat1 = boat("mercedes","M01")
plane1 = plane("Airbus","0023")

for w in (car1,boat1,plane1):
    w.move()


