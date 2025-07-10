# class Parent:
#     def speak(self):
#         print("Speaking from Parent class")
# class Child(Parent):
#     pass

# c = Child()
# c.speak()


class Animal:
    def speak(self):
        print("Animal speaks")
class Dog(Animal):
    def speak(self):
        print("Dog barks")
class Cat(Animal):
    def speak(self):
        print("Cat meows")

d = Dog()
c= Cat()
d.speak()  # Output: Dog barks
c.speak()  # Output: Cat meows