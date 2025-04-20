import random

print("\n=== 🔤 GUESS THE WORD 🔤 ===")
print(" ✨ Unscramble the letters to find the word ✨ ")

words = ["python","coding","game","computer","learn","university","favorite"]

while True:
    original_word = random.choice(words) #Randomly select a word from the word list
    letters = list(original_word) #Convert word to list of letters
    random.shuffle(letters) #Shuffle the letters
    scrambled = "".join(letters) #Convert list back to string

    print(f"\nScrambled word: {scrambled}")
    guess = input(" 🤔 What's the word?:").lower()

    if guess == original_word:
        print("🎉 Congrats! You win!")
    else:
        print(f"😢 Sorry,the word was {original_word}")
    again = input("Play again?(yes/no):").lower()
    if not again.startswith("y"):
        print(" 🥰 Thanks for playing!")
        break