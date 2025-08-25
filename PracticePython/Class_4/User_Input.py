name = input("Enter your name: ")
print("Hello,", name)
# input() দিয়ে ইউজারের কাছ থেকে ডেটা নেওয়া হয়

age = int(input("Enter your age: "))
print("You are", age, "years old")
# ইনপুট সবসময় string হয়, তাই int() দিয়ে কনভার্ট করতে হয়

price = float(input("Enter product price: "))
print("Price is:", price)
# এখানে float কনভার্সন হচ্ছে

city = input("Enter city: ")
print(f"You live in {city}")
# f-string ব্যবহার করে সুন্দরভাবে আউটপুট ফরম্যাট করা যায়

a, b = input("Enter two numbers: ").split()
print("Sum:", int(a) + int(b))
# split() দিয়ে একসাথে একাধিক ইনপুট নেওয়া হচ্ছে




x = 10     # int
y = 2.5    # float
result = x + y
print("Result:", result, "| Type:", type(result))
# এখানে int + float করলে Python নিজেই float এ কনভার্ট করেছে (implicit conversion)

num = "100"
num_int = int(num)
print("Converted:", num_int)
# string → int কনভার্সন

pi = 3.99
print("Int:", int(pi))
# float → int করলে দশমিক বাদ যায়

fruits = ["Apple", "Mango"]
print(tuple(fruits))
# list → tuple কনভার্সন