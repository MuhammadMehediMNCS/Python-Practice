# Array এর মতো কাজ করে list
numbers = [10, 20, 30]

# Accessing & updating
print("First:", numbers[0])
numbers[1] = 50

# Iterating with for loop
for i in range(len(numbers)):
    print("Index", i, ":", numbers[i])




# List Practice with Class
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

students = [
    Student("Mehedi", 22),
    Student("Rahim", 25),
    Student("Karim", 23)
]

for s in students:
    print(f"{s.name} is {s.age} years old")




# Nested loop with For
for i in range(1, 4):
    for j in range(1, 4):
        print(i * j, end="\t")
    print()
