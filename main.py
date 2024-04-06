#Step 5

import random, os
from word import word_list
from art import logo, stages

print(logo)
random_word = random.choice(word_list)
print(random_word)

game_start = True
lives = 6

display = ["_" for i in range(len(random_word))]

while game_start:
    guess = input("Guess a letter: ").lower()  
    os.system('cls')
    if guess in display:
        print(f"You've already guessed {guess}")

    for position in range(len(random_word)):
        letter = random_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in random_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")        
        lives -= 1
        if lives == 0:
            game_start = False
            print("You lose.")


    print(f"{' '.join(display)}")

    if "_" not in display:
        game_start = False
        print("You win.")

    print(stages[lives])