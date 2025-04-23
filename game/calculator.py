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
    print("===🧮 Simple Calculator 🧮===")
    print("Select operation:")
    print("1. ➕ Addition")
    print("2. ➖ Subtraction")
    print("3. ✖️ Multiplication")
    print("4. ➗ Division")

    while True:
        choice = input("Enter choice(1-4):")
        if choice not in ["1","2","3","4"]:
            print(" 🤦‍♂️ Invalid input. Please enter a num between 1 and 4")
        else:
            break
    try:
        num1 = float(input("Enter first number:"))
        num2 = float(input("Enter second number:"))
    except ValueError:
        print("🙅‍♀️ Error! Please enter valid numbers!")
        return

    if choice == "1":
        print(f"{num1} + {num2} = {add(num1, num2)}")

    elif choice == "2":
        print(f"{num1} - {num2} = {substract(num1, num2)}")

    elif choice == "3":
        print(f"{num1} * {num2} = {multiply(num1, num2)}")

    elif choice == "4":
        print(f"{num1} / {num2} = {divide(num1, num2)}")

    again = input("\n😉 Do you want to perform another calculation?(yes/no):").lower()
    if not again.startswith("y"):
        print("Thanks for using calculator! Goodbye 👋")
        return
    else:
        main()

main()