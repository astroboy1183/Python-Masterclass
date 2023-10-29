# Day 7 : (Day 6 is the reeborg program, at http://reeborg.ca)
import random
from hangman import hangman_stages
from word_list import word_list,logo
print('''  
Welcome to the Hangman Game

''')
print(logo)

# word_list = ["aardvark","baboon","camel"]
end_of_game = False

chosen_word = random.choice(word_list)
print(chosen_word)

lives=6
display = ["_" for letter in chosen_word]

# print(display)


while not end_of_game:
    guess = input("Guess the letter: ").lower()

    if guess in display:
        print(f"You have guessed the word {guess}")

    for i in range(len(chosen_word)):
        if chosen_word[i]==guess:
            display[i] = guess
    if guess not in chosen_word:
        print("You guessed the wrong word. you lose a life.")
        lives-=1
        if lives==0:
            end_of_game=True
            print("You lose!")

    print(display)

    if "_" not in display:
        end_of_game=True
        print("You win!")
    print(hangman_stages[lives])

