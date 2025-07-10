# class Car:
#     car_company = "TATA"
#     def __init__(self, model, color):
#         self.model = model
#         self.color = color
#         print("Car created")

# s1 = Car("Nexon", "Red")
# print(s1.model, s1.color)
# s2 = Car("Safari", "Black")
# print(s2.model, s2.color)
# print(Car.car_company)

# class Student:
#     def __init__(self, name):
#         self.name = name

#     def hello(self):
#         print("Hello", self.name)

# s1 = Student("Mohit")
# print(s1.name)
# s1.hello()


class Student:
    @staticmethod #decorator
    def college():
        print("IIT Delhi")

Student.college()  # Calling the static method without creating an instance
