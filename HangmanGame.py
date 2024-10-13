import random
words = ["python", "hangman", "game", "code", "fun", "challenge"]
word = random.choice(words)
guessed_letters = ["_"] * len(word)
max_incorrect_guesses = 6
incorrect_guesses = 0
while True:
    print(" ".join(guessed_letters))
    print(f"Incorrect guesses: {incorrect_guesses}/{max_incorrect_guesses}")
    guess = input("Guess a letter: ")
    if guess in word:
        for i, letter in enumerate(word):
            if letter == guess:
                guessed_letters[i] = guess
    else:
        incorrect_guesses += 1
        print("Incorrect guess!")
    if "_" not in guessed_letters:
        print("Congratulations, you won!")
        break
    if incorrect_guesses >= max_incorrect_guesses:
        print(f"Game over! The word was {word}.")
        break