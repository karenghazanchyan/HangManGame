import random

def hang_man():
    personages = [
        "   ------------------- \n   |                 |\n   0                 |\n                     |\n                     |\n                     |\n                     |\n                     |\n                     |\n                     |\n______________________________",
        "   ------------------- \n   |                 |\n   0                 |\n   |                 |\n                     |\n                     |\n                     |\n                     |\n                     |\n                     |\n______________________________",
        "   ------------------- \n   |                 |\n   0                 |\n  /|                 |\n                     |\n                     |\n                     |\n                     |\n                     |\n                     |\n______________________________",
        "   ------------------- \n   |                 |\n   0                 |\n  /|\                |\n                     |\n                     |\n                     |\n                     |\n                     |\n                     |\n______________________________",
        "   ------------------- \n   |                 |\n   0                 |\n  /|\                |\n  /                  |\n                     |\n                     |\n                     |\n                     |\n                     |\n______________________________",
        "   ------------------- \n   |                 |\n   0                 |\n  /|\                |\n  / \                |\n                     |\n                     |\n                     |\n                     |\n                     |\n______________________________"
    ]

    words = ["Mercedes", "BMW", "Tesla", "Lada", "McLaren", "Opel", "Ferrari", "Lamborghini", "Bugatti","Toyota",]

    word = random.choice(words).lower()

    guessed_letters = set()
    wrong_guesses = 0
    print(word)
    print("_ " * len(word))

    while wrong_guesses < len(personages):
        letter = input("Enter a letter: ").lower()

        if letter in guessed_letters:
            print("You've already guessed that letter. Try again.")
            continue

        guessed_letters.add(letter)

        if letter in word:
            for char in word:
                if char in guessed_letters:
                    print(char, end=" ")
                else:
                    print("_", end=" ")
            print()

            if all(char in guessed_letters for char in word):
                print("----------------------------------------")
                print("Congratulations! You guessed the word:", word)
                break
        else:
            wrong_guesses = wrong_guesses + 1
            print(personages[wrong_guesses - 1])

    if wrong_guesses == len(personages):
        print("----------------------------------------")
        print("Sorry, you lost! The word was:", word)


print("HANGMAN GAME")
print("The computer has chosen a word. You need to guess it by entering one letter at a time.")

hang_man()
