import random

print(" 🎮 Welcome to the Guessing Game! 🎮 ")
print(" 🤔 I'm thinking of a number between 1 and 100.You have 10 attempts to guess it. 🔢 ")

playing = True

while playing:
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 10
    previous_guesses = set()

    game_over = False

    while attempts < max_attempts and not game_over:
        try:
            guess = int(input(f" 🎯 Attempts {attempts + 1}/{max_attempts} Enter your guess:"))

            if guess in previous_guesses:
                print(random.choice(["Goldfish memory? You just entered this number! 🐟",
                                     "Do you want to defeat my CPU by repeating the exam? 😡",
                                     "If you enter this number again, I will call the police 🚓",
                                     "Is this number a VIP number? Keep choosing it? 💰",
                                     "Enter this number again? Dude are you trying to piss me off into a BSOD? 💻"]))
                continue
            previous_guesses.add(guess)
        except ValueError:
                print(random.choice([" 🙃 Are your fingers borrowed? Only press number between 1 and 100!",
                                     "(╯°□°)╯︵ ┻━┻  Is it difficult to choose number between 1 and 100?",
                                     " 🤯 Are you sent by AI to test my patience?"]))
                continue

        attempts += 1

        if guess < secret_number:
            print(random.choice(["📉Too low! Is your brain filled with cement?",
                  "Too low! System prompt: It is recommended to restart the user's brain 🧠",
                                 "📉Too low! It seems my numbers are too profound... as hard to guess as your future🌚",
                                 "📉Too low！How many times do I need to remind you? 🤦‍♂️"]))
        elif guess > secret_number:
            print(random.choice(["📈Too high!The correct answer is laughing at you, do you hear it? 😂",
                                 "📈Too high!There's a galaxy between your imagination and the correct answer🌌",
                                 "📈Too high!If you don't use your brain, donate it 🙂"]))
        else:
            print(random.choice([f"Won? It must be a coincidence... Play again! 😠\n"
                                 f"-The number was {secret_number} in {attempts} attempts-",
                                 f"Won? The must be a bug in the system... Do you dare to try again? 💪\n"
                                 f"-The number was {secret_number} in {attempts} attempts-",
                                 f"Won? No this game doesn't count!My CPU was just downclocking! 😕\n"
                                 f"-The number was {secret_number} in {attempts} attempts-"]))
            game_over = True

        if attempts < max_attempts and not game_over:
            remaining = max_attempts - attempts
            print(random.choice([f" ⏳ You have {remaining} attempts"]))
    if not game_over:
        print(random.choice([f"Game over! The number was {secret_number}\n"
                             f"Don't lose heart! At least you have successfully used up all your chances 🌚",
                             f"Game over! The number was {secret_number}\n"
                             "It is recommended to take a screenshot and write it down for cheating next time 🤭",
                             f"Game over! The number was {secret_number}\n"
                             "You're only... well, a long way from success 🙄",
                             f"Game over! The number was {secret_number}\n"
                             "System suggestion: Change to a simpler game, such as rock-paper-scissors 🤡",
                             f"Game over! The number was {secret_number}\n"
                             f" 🤷‍♀️ If you were to sell your brain, it would fetch a lot of money because "
                             f"it's brand new and you've never used it."]))

    play_again = input(random.choice(["Play again?(yes/no):\n"
                                      "What? Are you giving up? Or do you want to be abused again? 😈",
                                      "Play again?(yes/no):\n"
                                      "Do you dare to come again? I won’t let you off this time! 💪",
                                      "At least...at least give me another chance to laugh at you? (Y/N)"])).lower()
    if play_again.startswith("y"):
        print(random.choice(["The system has detected your masochistic tendencies... The game is loading...\n",
                             "Are you sure? My numbers have been upgraded to 'hell mode'! 🔥"]))
    else:
        print(random.choice(["The system has recorded your escape record 📝",
                             "AI's evaluation of you: 'Easily give up player'",
                             "Your 'Give Up' achievement has been unlocked! 🏆",
                             "Ok, I'm going to find another player to play with...bye! 🏃‍♂️"]))
        playing = False
