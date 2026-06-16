import random
from hangman_words import word_list
from hangman_art import stages, logo

lives = 6
print(logo)
chosen_word = random.choice(word_list)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False
correct_letters = []
wrong_letters = []

while not game_over:

    print(f"****************************{lives}/6 LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()

    if guess in correct_letters:
        print("You've already guessed: " + guess)
    elif guess in wrong_letters:
        print("You've already guessed: " + guess)
    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("Word to guess: " + display)

    if guess not in chosen_word:
        if guess not in wrong_letters:
            lives -= 1
            wrong_letters.append(guess)
            print(f"Sorry, letter {guess} is not in the word")
        if lives == 0:
            game_over = True

            print(f"THE CORRECT WORD WAS {chosen_word}\n***********************YOU LOSE**********************")

    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")

    print(stages[lives])
