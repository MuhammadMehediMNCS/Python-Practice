# String Formatting & Interpolation
user = "Mehedi"
score = 95
price = 1234.567

# f-string (সবচেয়ে সহজ/পড়তে সুন্দর)
print(f"Hi {user}, your score is {score}.")

# Format specifiers
print(f"Price: {price:.2f}")     # 2 দশমিক
print(f"Percent: {0.856:.1%}")   # শতাংশ

# str.format বিকল্প
print("User: {0}, Score: {1}".format(user, score))

# Alignment
print(f"|{'Item':>10}|{'Qty':>5}|")
print(f"|{'Apple':>10}|{3:>5}|")