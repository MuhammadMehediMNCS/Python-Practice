# Inheritance
# Base Class
class Animal:
    def eat(self):
        print("Animal is eating...")

# Derived Class
class Cat(Animal):
    def bark(self):
        print("Cat is Miaowing...")

cat = Cat()
cat.eat()   # Base class থেকে
cat.bark()  # Own method
