# class Bird:
#     def make_sound(self):
#         print("Chirp")

# class Cat:
#     def make_sound(self):
#         print("Meow")

# for animal in [Bird(), Cat()]:
#     animal.make_sound() 


class Employee:
    def work(self):
        print("Employee is working")
class Developer(Employee):
    def work(self):
        print("Developer is coding")
class Manager(Employee):
    def work(self):
        print("Manager is managing")

for emp in [Developer(), Manager()]:
    emp.work() 