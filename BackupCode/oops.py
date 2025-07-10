class Person:
    def __init__(self,name, age):
        self.name = name
        self.age = age
        print("Person created")
        
    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")


p1 = Person("Mohit",30)
p1.display()
# print(p1.name)
# print(p1.age)


