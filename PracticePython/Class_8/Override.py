# Real Life Example 1 : Payment System
from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CreditCardPayment(Payment):
    def pay(self, amount):
        print(f"Paid {amount} using Credit Card.")

class PayPalPayment(Payment):
    def pay(self, amount):
        print(f"Paid {amount} using PayPal.")

payment1 = CreditCardPayment()
payment1.pay(100)

payment2 = PayPalPayment()
payment2.pay(200)




# Real Life Example 2 : Animal Sound
class Animal:
    def sound(self):
        print("Animal makes a sound.")

class Dog(Animal):
    def sound(self):
        print("Dog barks.")

class Cat(Animal):
    def sound(self):
        print("Cat meows.")

a1 = Dog()
a1.sound()  # Dog barks.

a2 = Cat()
a2.sound()  # Cat meows.




# Demo App : Transport System
from abc import ABC, abstractmethod

# Abstract Base Class
class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    def fuel_type(self):  # optional override
        print("Fuel type: Unknown")

# Child class 1
class Car(Vehicle):
    def start(self):
        print("Car started.")
    def stop(self):
        print("Car stopped.")
    def fuel_type(self):
        print("Fuel type: Petrol")

# Child class 2
class Bike(Vehicle):
    def start(self):
        print("Bike started.")
    def stop(self):
        print("Bike stopped.")
    def fuel_type(self):
        print("Fuel type: Petrol")

# Child class 3
class Bus(Vehicle):
    def start(self):
        print("Bus started.")
    def stop(self):
        print("Bus stopped.")
    def fuel_type(self):
        print("Fuel type: Diesel")

# Polymorphism in action
vehicles = [Car(), Bike(), Bus()]
for v in vehicles:
    v.start()
    v.fuel_type()
    v.stop()