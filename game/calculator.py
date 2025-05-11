import random

def add(x,y):
    return x + y

def substract(x,y):
    return x - y

def multiply(x,y):
    return x * y

def divide(x,y):
    if y == 0:
        return random.choice(["😮 Have you ever been kicked in the head by a donkey? Division by zero is not allowed！",
                              " 🙅‍♀️ Error: Cannot calculate. Just like your logic, it does not exist"])
    return x / y

def main():
    print("=== 🥰  Welcome to the Friendly Calculator 🥰 ===")
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
        print(random.choice(["Bro I am a calculator. You know what a calculator does, right? 🔪",
                             "If you make the same mistake again, I'll put your head on a leash 🪓"]))
        return

    if choice == "1":
        print(random.choice([f"{num1} + {num2} = {add(num1, num2)}\nThis calculation process is "
                             f"like using a nuclear bomb to kill"
              f" a mosquito - a bit of a waste of talent 🦟 ",
                             f"{num1} + {num2} = {add(num1, num2)}\nTry mental arithmetic next time,"
                             f" maybe it can exercise your brain 🧠"]))

    elif choice == "2":
        print(random.choice([f"{num1} - {num2} = {substract(num1, num2)}\n"
              f"Are you serious? You can calculate this number with your fingers. Do you really need the CPU"
                             f" to burn some power for you? 🔋",
                             f"{num1} - {num2} = {substract(num1, num2)}\n"
                             f"Congratulations! You have successfully proved the theory of human degeneration! "
                             f"Darwin is clapping in his coffin👏"]))

    elif choice == "3":
        print(random.choice([f"{num1} * {num2} = {multiply(num1, num2)}\n"
              f"You know that an ant’s brain capacity could handle this calculation, but you need a machine to help you? 🐜",
                             f"{num1} * {num2} = {multiply(num1, num2)}\nIs your IQ like your bank card balance, "
                             f"always close to 0 ? 🙂‍↔️"]))

    elif choice == "4":
        print(random.choice([f"{num1} / {num2} = {divide(num1, num2)}\n"
              f"Your math skills are so good that even Siri wants to turn off the phone automatically after hearing it 📱",
                             f"{num1} / {num2} = {divide(num1, num2)}\nThis calculator has automatically "
                             f"enabled the 'anti-idiot' mode to prevent you from lowering the average level 🤺"]))

    again = input("\n 💴 Trial ends. Please recharge VIP (yes/no):").lower()
    if not again.startswith("y"):
        print("Poor guy")
        return
    else:
        main()

main()