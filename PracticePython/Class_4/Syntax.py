# Syntax মানে হলো প্রোগ্রাম লেখার নিয়ম বা কাঠামো
# Python-এ indentation (tab/space) খুব গুরুত্বপূর্ণ
# def দিয়ে function তৈরি করা হয়, এখানে যোগফল বের হচ্ছে
# class হলো অবজেক্ট বানানোর কাঠামো। Car ক্লাস দিয়ে একটা অবজেক্ট তৈরি করা হলো
# Beginner: Simple Hello World
print("Hello, Python!")

# Example 2: Basic Arithmetic
print(5 + 3)

# Advanced: Class structure
class Car:
    def __init__(self, brand):
        self.brand = brand
    def show(self):
        print(f"Car brand: {self.brand}")

my_car = Car("Toyota")
my_car.show()



# print() হলো আউটপুট দেখানোর জন্য Python-এর বেসিক ফাংশন
# Python দিয়ে সরাসরি গণনা করা যায় (এখানে ৫+৩ = ৮)
# "#" দিয়ে শুরু হলে সেটা comment, Python এক্সিকিউট করে না