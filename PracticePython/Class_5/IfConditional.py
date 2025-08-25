# Check Leap Year
year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a Leap Year")
else:
    print(f"{year} is NOT a Leap Year")




# Largest of 3 Numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

largest = a if (a > b and a > c) else (b if b > c else c)

print(f"Largest number is: {largest}")