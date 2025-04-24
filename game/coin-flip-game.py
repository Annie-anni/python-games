import random

print(" 🎮 COIN FLIP GAME 🎮 ")
print(" Guess heads or tails ✨ ")

while True:
    guess = input("Enter your guess（heads/tails)\n(enter 'q' any time to quit):").lower()

    if guess == 'q':
        print(random.choice(["You are so skilled at giving up, do you do this often? 😏",
                             "Your keyboard: Q key wear +100%, other keys: brand new",
                             "Do you disappear like this in real life? Like when your takeaway arrives?",
                             "You quit faster than Bolt sprints, are you considering switching to track and field?"]))
        break

    if guess != 'heads' and guess != 'tails':
       print(random.choice(["❓ Are you typing in Morse code? I only know 'heads' and 'tails'",
                            "🌌 Your vocabulary is wider than the universe... but here it's just 'heads' or 'tails'",
                            "🙄 You can’t even tell the difference between 'heads and tails', and you still want to guess the coin?",
                            "📉 Your input accuracy is lower than a monkey typing randomly",
                            "⚠️ According to Section 3 of the Coin Act, input must be 'Heads'' or 'Tails'",
                            "🔐 Safety Tips: Random input may cause the coin to become angry"]))
       continue

    flip = random.choice(['heads','tails'])

    print(f"\n🪙 Coin shows {flip}")

    if guess == flip:
        print(random.choice(["Won? You must have peeked at my source code 😤",
                             "Okay you won.Human luck +1, AI let down +10086 🙄",
                             "You won? (AI falls into deep thought) This is impossible... My algorithm is flawless!",
                             "💻 System prompt: Anomaly detected... You must have cheated!",
                             "⚠️ Warning: Player victory is a temporary BUG and will be fixed soon..."]))
    else:
        print(random.choice(["🌚 Don't lose heart! At least you managed to avoid the correct answer~",
                             "💡 Tip: There are only two sides to a coin... and you totally missed the right side",
                             "🎯 Your accuracy... reminds me of a blindfolded monkey shooting arrows",
                             "🦧 The accuracy of the gorilla's random keystroke experiment is higher than yours",
                             "😌 My IQ is beyond your reach~",
                             "😜 My algorithm has already predicted your failure.",
                             "😎 Failure is the mother of success...but you may not see your child today"]))

    again = input(random.choice(["\n🔮 The crystal ball shows: You will lose even more miserably "
                  "in the next game... Do you want to verify? (Y/N):",
                                 "🦮 Do you need a guide dog to help you find the ‘right option’? (Y/N)"])).lower()
    if not again.startswith('y'):
        print(random.choice(["GAME OVER...Just like your love is short-lived",
                             "👹 I have reported your cowardly behavior to the God of Gaming",
                             "🪦 Reason for game ending: Players can’t afford to lose"]))
        break
