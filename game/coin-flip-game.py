import random

print(" 🎮 COIN FLIP GAME 🎮 ")
print(" Guess heads or tails ✨ ")

while True:
    guess = input("Enter your guess（heads/tails)\n(enter 'q' any time to quit):").lower()

    if guess == 'q':
        break

    if guess != 'heads' and guess != 'tails':
       print("Please enter 'heads' or 'tails'")
       continue

    flip = random.choice(['heads','tails'])

    print(f"\n🪙 Coin shows {flip}")

    if guess == flip:
        print("You won! You guessed correctly 🎉")
    else:
        print("😭 Sorry,wrong guess. Try again! 🍀")

    again = input("\n🔁 Try again? yes/no:").lower()
    if not again.startswith('y'):
        print("Goodbye!")
        break
