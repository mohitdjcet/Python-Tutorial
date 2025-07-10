class BankAccount:
    def __init__(self,name,balance):
        self.name = name
        self.__balance = balance  # Private attribute
    def deposit(self, amount):
        self.__balance += amount
    def getBalance(self):
        return self.__balance

acc = BankAccount("Mohit", 1000)
acc.deposit(500)
print(acc.getBalance()) 
# print(acc.__balance)