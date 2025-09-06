# একজনের বয়স ইনপুট নিন যদি বয়স ১৮ এর সমান হয় তবে প্রিন্ট করবে "You are Eligible to vote." নাহলে "Not Eligible"

# বয়স ইনপুট
age = int(input("Enter your age: "))

# শর্ত চেক
if age == 18:
    print("You are Eligible to vote.")
else:
    print("Not Eligible")
