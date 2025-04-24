import random

print("\n=== 🔤 GUESS THE WORD 🔤 ===")
print(" ✨ Unscramble the letters to find the word ✨ ")

words = ["python","coding","game","computer","learn","university","favorite",
                "guitar", "puzzle", "jacket", "rabbit",
    "garden", "rocket", "dragon", "planet", "orange",
    "monkey", "turtle", "coffee", "window", "bottle"]

while True:
    original_word = random.choice(words) #Randomly select a word from the word list
    letters = list(original_word) #Convert word to list of letters
    random.shuffle(letters) #Shuffle the letters
    scrambled = "".join(letters) #Convert list back to string

    print(f"\nScrambled word: {scrambled}")
    guess = input(" 🤔 What's the word?:").lower()

    if guess == original_word:
        print(random.choice(["Correct! 😤 Next game, my vocabulary will be upgraded to Shakespeare level",
                             "🐍 You guessed python... but you still can't escape my ridicule"]))
    else:
        print(random.choice([f"📉 Your vocabulary makes me want to donate a dictionary to you.\nThe word was {original_word}",
                             f"🤏 Is that all? My grandma can guess better than you.\nThe word was {original_word}"]))
    again = input("🍕 You can lose 3 more games before the pizza is delivered! Continue? (Y/N):").lower()
    if not again.startswith("y"):
        print(random.choice(["🧻 Your game records have been used as toilet paper raw materials",
                             "📉 Your luck value is permanently -10 for running away"]))
        break