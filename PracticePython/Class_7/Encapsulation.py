# Encapsulation (ডেটা লুকানো)
class Person:
    def __init__(self, age):
        self.__age = age   # private field

    # Getter
    def get_age(self):
        return self.__age

    # Setter
    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Invalid age!")

p = Person(25)
print(p.get_age())  # Getter
p.set_age(30)       # Setter
print(p.get_age())






# Real life Inheritance and Encapsulation Example
class BankAccount:
    def __init__(self):
        self.__balance = 0

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
        else:
            print("Insufficient balance!")

    def get_balance(self):
        return self.__balance

class SavingsAccount(BankAccount):
    def __init__(self):
        super().__init__()
        self.interest_rate = 0.05

    def add_interest(self):
        self.deposit(self.get_balance() * self.interest_rate)

# ব্যবহার
s = SavingsAccount()
s.deposit(1000)
s.add_interest()
print(s.get_balance())
