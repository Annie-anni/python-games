import random

def add(x,y):
    return x + y

def substract(x,y):
    return x - y

def multiply(x,y):
    return x * y

def divide(x,y):
    if y == 0:
        return "Error! Division by zero is not allowed"
    return x / y

def main():
    print("=== 🚬 Welcome to the Friendly Calculator 🚬 ===")
    print("Select operation:")
    print("1. ➕ Addition")
    print("2. ➖ Subtraction")
    print("3. ✖️ Multiplication")
    print("4. ➗ Division")

    while True:
        choice = input("Enter choice(1-4):")
        if choice not in ["1","2","3","4"]:
            print(random.choice([" 🤦 Is it difficult to enter 1,2,3,4?",
                                 "The option you entered is like ordering a washing machine at a pizza place"
                                 " - it's not on the menu 📋 ",
                                 "Wow This choice is as reasonable as using a banana to make a phone call 🍌"]))

        else:
            break
    try:
        num1 = float(input("Enter first number:"))
        num2 = float(input("Enter second number:"))
    except ValueError:
        print(random.choice(["Bro I am a calculator. You know what a calculator does, right?",
                             "If you make the same mistake again, I'll put your head on a leash."]))
        return

    if choice == "1":
        print(f"{num1} + {num2} = {add(num1, num2)}")

    elif choice == "2":
        print(f"{num1} - {num2} = {substract(num1, num2)}")

    elif choice == "3":
        print(f"{num1} * {num2} = {multiply(num1, num2)}")

    elif choice == "4":
        print(f"{num1} / {num2} = {divide(num1, num2)}")

    again = input("\n 💴 Trial ends. Please recharge VIP (yes/no):").lower()
    if not again.startswith("y"):
        print("Poor guy")
        return
    else:
        main()

main()