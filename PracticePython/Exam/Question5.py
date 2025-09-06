# একটি প্রোগ্রাম লিখো যেখানে ইউজার 1-7 এর মধ্যে একটি সংখ্যা দিবে আর প্রোগ্রামটি সেই দিনের নাম দেখাবে (1= Monday, 2 = Tuesday..........7 = Sunday)

# সংখ্যা ইনপুট
day = int(input("Enter a number (1-7): "))

# dictionary ব্যবহার করে দিনের নাম দেখানো
days = {
    1: "Monday",
    2: "Tuesday",
    3: "Wednesday",
    4: "Thursday",
    5: "Friday",
    6: "Saturday",
    7: "Sunday"
}

# আউটপুট
if day in days:
    print(days[day])
else:
    print("Invalid input! Please enter a number between 1 and 7.")
