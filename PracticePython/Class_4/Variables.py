# Python-এ ভ্যারিয়েবল তৈরি করতে হলে কেবল = ব্যবহার করলেই হয়, টাইপ লিখতে হয় না (Python নিজে টাইপ বুঝে নেয়)
age = 25
name = "Mehedi"
print(name, age)
# age হলো integer, name হলো string

pi = 3.1416
print("PI:", pi)
# pi হলো float ডেটা টাইপ

is_active = True
print("Active:", is_active)
# Boolean মান True/False ব্যবহার করা হয়।

fruits = ["Apple", "Mango", "Banana"]
person = {"name": "Hasan", "age": 30}
print(fruits, person)
# list হলো একাধিক মানের কালেকশন, আর dict হলো key-value আকারে ডেটা রাখার জন্য

x = 10
print("Before:", x, type(x))
x = "Now String"
print("After:", x, type(x))
# Python dynamically typed ভাষা, মানে ভেরিয়েবল টাইপ বদলাতে পারে