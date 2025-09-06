# একটি অ্যারে/লিস্টে ৫টি সংখ্যা রাখো। Exception Handelling ব্যবহার করুন এবং এরপর লুপ ব্যবহার করে সবগুলো ডিসপ্লে করুন

try:
    # লিস্ট তৈরি (৫টি সংখ্যা)
    numbers = [10, 20, 30, 40, 50]

    # লুপ ব্যবহার করে সংখ্যা প্রিন্ট করা
    print("Numbers in the list:")
    for num in numbers:
        print(num)

except Exception as e:
    # যদি কোনো Exception ঘটে
    print("An error occurred:", e)

finally:
    print("Program finished.")
