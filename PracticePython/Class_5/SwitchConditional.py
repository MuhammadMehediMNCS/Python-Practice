# Simple ATM Menu System
balance = 1000

while True:
    print("\nATM Menu:")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print(f"Your Balance: {balance}")
    elif choice == 2:
        deposit = float(input("Enter amount to deposit: "))
        balance += deposit
        print(f"Deposited {deposit}. New Balance: {balance}")
    elif choice == 3:
        withdraw = float(input("Enter amount to withdraw: "))
        if withdraw <= balance:
            balance -= withdraw
            print(f"Withdrawn {withdraw}. New Balance: {balance}")
        else:
            print("Insufficient funds!")
    elif choice == 4:
        print("Thank you for using ATM.")
        break
    else:
        print("Invalid Choice!")




# Simple Quiz with Scoring
score = 0

answer = input("1. What is the capital of Bangladesh? ")
if answer.lower() == "dhaka":
    score += 1

answer = input("2. 5 + 3 = ? ")
if answer == "8":
    score += 1

answer = input("3. Which language is used for .NET? ")
if answer.lower() in ["c#", "csharp"]:
    score += 1

print(f"\nYour Score: {score}/3")