class Vehicle:
     def __init__(self, make , model):
        self.make = make
        self.model = model
     def moves(self):
        print("The vehicle moves on the road.") 
     def stops(self):
        print("The vehicle stops at the traffic light.")

     def get_make_model(self):
       print(f"Make: {self.make}, Model: {self.model} ")

my_car = Vehicle('Tesla', 'Space X')
print(my_car.make)
print(my_car.model)
my_car.moves() 
my_car.stops()   
my_car.get_make_model() 

new_car = Vehicle('Toyota', 'Corolla')
new_car.moves()
new_car.get_make_model()

class temhert:
    def __init__(self, ketsla, negra):
        self.ketsla = ketsla
        self.negra = negra
    def kene(self):
       print("Time to kene")
    def zema(self):
       print("Time to zema")
nebiyu = temhert('Merata', 'yebe')
print(nebiyu.ketsla)
nebiyu.kene()
nebiyu.zema()

class Car(Vehicle):
    def __init__(self, make, model, year):
        super().__init__(make, model)
        self.year = year

    def moves(self):
       print("The car moves on the road.")
    def stops(self):
       print("The car stops at the traffic light.")
    def get_make_model(self):
        print(f"Make: {self.make}, Model: {self.model}, Year: {self.year} ")
class Truck(Vehicle):
   def moves(self):
       print("The truck moves on the road.")
   def stops(self):
       print("The truck stops at the traffic light.")
class Motorcycle(Vehicle):
    def moves(self):
         print("The motorcycle moves on the road.")
    def stops(self):
            print("The motorcycle stops at the traffic light.")
class Bicycle(Vehicle):
    pass 

happy_car = Car('Honda', 'Civic', '2000')
happy_car.moves()
happy_car.stops()
happy_car.get_make_model()
happy_truck = Truck('Ford', 'F-150')
happy_truck.moves()
happy_truck.stops()
happy_truck.get_make_model()
happy_motorcycle = Motorcycle('Yamaha', 'MT-07')
happy_motorcycle.moves()
happy_motorcycle.stops()
happy_motorcycle.get_make_model()
happy_bicycle = Bicycle('Giant', 'Escape 3')
happy_bicycle.moves()
happy_bicycle.stops()
happy_bicycle.get_make_model()
