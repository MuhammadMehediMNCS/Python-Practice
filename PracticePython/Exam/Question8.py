# একটি Person ক্লাস তৈরি করুন যেখানে নাম এবং বয়স থাকবে। এরপর Student নামে আর একটি ক্লাস তৈরি করুন যেটি Person থেকে Inheritene করবে এবং সেখানে অতিরিক্ত student_id রাখবেন

# Parent Class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


# Child Class
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)  # Parent class এর constructor কল করা
        self.student_id = student_id

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Student ID: {self.student_id}")


# Main part
s1 = Student("Mehedi Hasan", 22, 101)

# তথ্য প্রিন্ট
s1.display_info()
