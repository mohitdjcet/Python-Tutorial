# class Vehicle:
#     def __init__(self):
#         self.engine = False
#         self.brk = False

#     def start_engine(self):
#         self.engine = True
#         self.brk = True
#         print("Car started.")

# car1 = Vehicle()
# car1.start_engine()

from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

class Car(Vehicle):
    def start_engine(self):
        print("Car started.")
        
car = Car()
car.start_engine()
