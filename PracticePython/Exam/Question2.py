# ইউজারের কাছ থেকে একটি সংখ্যা ইনপুট নিয়ে সেটা জোড় নাকি বিজোড় সংখ্যা প্রমাণ করো

# ইউজারের কাছ থেকে সংখ্যা ইনপুট
number = int(input("Enter a number: "))

# জোড় নাকি বিজোড় চেক করা
if number % 2 == 0:
    print(f"{number} is an Even number")
else:
    print(f"{number} is an Odd number")
