import random

def choose_word():
    words = [
        ("python", "A popular programming language."),
        ("hangman", "The name of this game."),
        ("program", "A set of instructions that a computer follows."),
        ("computer", "An electronic device that can perform tasks."),
        ("keyboard", "An input device used to type characters."),
        ("mouse", "An input device used to point and click."),
        ("monitor", "An output device that displays information."),
        ("software", "Programs and operating information used by a computer."),
    ]
    return random.choice(words)

def display_word(word, guessed_letters):
    displayed_word = ""
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter + " "
        else:
            displayed_word += "_ "
    return displayed_word.strip()

def hangman():
    word, hint = choose_word()
    guessed_letters = []
    attempts_left = 6  # You can adjust this as per the difficulty level

    print("Welcome to Hangman!")
    print("Hint:", hint)
    print(display_word(word, guessed_letters))

    while True:
        print("\nAttempts left:", attempts_left)
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("Good guess!")
        else:
            print("Oops! That letter is not in the word.")
            attempts_left -= 1

        print(display_word(word, guessed_letters))

        if all(letter in guessed_letters for letter in word):
            print("Congratulations! You guessed the word:", word)
            break

        if attempts_left == 0:
            print("You ran out of attempts! The word was:", word)
            break


hangman()
