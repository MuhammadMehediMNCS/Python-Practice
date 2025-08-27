# Python-এ সরাসরি access modifier নেই। কিন্তু naming convention দিয়ে বোঝানো হয়:
# public → সবার জন্য

# _protected → কেবল ক্লাস ও সাবক্লাসের জন্য (by convention)

# __private → শুধু সেই ক্লাসের ভেতরে (name mangling হয়)
class Person:
    def __init__(self, name, age, gender):
        self.name = name          # public
        self._gender = gender     # protected
        self.__age = age          # private




# Declaring and Calling Methods
class MathOperations:
    def add(self, *args):
        """একাধিক সংখ্যাকে যোগ করবে (variable arguments)"""
        return sum(args)

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Denominator cannot be zero!")
        return a / b

    @staticmethod
    def power(a, b):
        return a ** b

    # Dunder method (__call__ দিয়ে object কে function-এর মতো ব্যবহার)
    def __call__(self, a, b):
        return self.add(a, b)


math = MathOperations()

print("Addition (2 params):", math.add(5, 7))
print("Addition (multi params):", math.add(2, 3, 4, 5))

print("Subtraction:", math.subtract(10, 3))
print("Multiplication:", math.multiply(4, 6))

try:
    print("Division:", math.divide(10, 0))
except Exception as e:
    print("Error:", e)

print("Power:", MathOperations.power(2, 5))

# Object কে function-এর মতো ব্যবহার
print("Using __call__:", math(10, 20))