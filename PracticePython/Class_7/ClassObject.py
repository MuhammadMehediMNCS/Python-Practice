# Classes & Objects
class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def drive(self):
        print(f"{self.brand} is driving.\nColor is {self.color}")

# Object তৈরি
car1 = Car("Toyota", "Red")
car1.drive()

car2 = Car("BMW", "Black")
car2.drive()


# ব্যাখ্যা :
# class → ক্লাস তৈরি করার জন্য ব্যবহৃত হয়।

# object (car1, car2) → ক্লাসের instance।

# method → ক্লাসের ভেতরের function।