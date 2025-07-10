# class Person:
#     def __init__(self,name):
#         self.name = name
#     def __str__(self):
#         return f"Person: {self.name}"
    
# p = Person("Mohit")
# print(p)  # This will call the __str__ method and print "Person: Mohit"

# class Basket:
#     def __init__(self, items):
#         self.items = items
#     def __len__(self):
#         return len(self.items)
    
# b = Basket(["apple", "banana", "cherry"])
# print(len(b))

# class Numbers:
#     def __init__(self,values):
#         self.values = values
#     def __add__(self,other):
#         return Numbers(self.values + other.values)
    
# num1 = Numbers(10)
# num2 = Numbers(5)
# result = num1 + num2
# print(result.values) 


# class Book:
#     def __init__(self,title):
#         self.title = title
#     def __eq__(self, other):
#         return self.title == other.title
    
# book1 = Book("1984")
# book2 = Book("1984")
# print(book1 == book2) 

class MyList:
    def __init__(self,data):
        self.data = data
    def __getitem__(self, index):
        return self.data[index]

m1 = MyList([1, 2, 3, 4, 5])
print(m1[2]) 