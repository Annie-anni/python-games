import random

print(" 🎮 Welcome to the Guessing Game! 🎮 ")
print(" 🤔 I'm thinking of a number between 1 and 100.You have 10 attempts to guess it. 🔢 ")

playing = True

while playing:
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 10

    game_over = False

    while attempts < max_attempts and not game_over:
        try:
            guess = int(input(f" 🎯 Attempts {attempts + 1}/{max_attempts} Enter your guess:"))
        except ValueError:
            print(" ❌ Please enter a valid number")
            continue

        attempts += 1

        if guess < secret_number:
            print("Too low! Try again higher number! ⬆️ ")
        elif guess > secret_number:
            print("Too higher! Try again lower number! ⬇️")
        else:
            print(f" 🎉 Congrats! You guessed the number in {secret_number} in {attempts} attempts！")
            game_over = True

        if attempts < max_attempts and not game_over:
            print(f" ⏳ You have {max_attempts - attempts} attempts left! ")
    if not game_over:
        print(f" 😭 Game over! The number was {secret_number}")

    play_again = input(" 😊 Would you like to play again?(yes/no):").lower()
    if play_again.startswith("y"):
        print(" 🥰 New game starting...\n")
    else:
        print("Thanks for playing!Goodbye！👋")
        playing = False
