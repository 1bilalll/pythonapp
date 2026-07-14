import random
from hangman_words import word_lists
from hangman2 import logo,stages

lives=6
print(logo)
chosen_words =random.choice(hangman_words.word_lists)
print(chosen_words)
placeholder =""
word_length =len(chosen_words)
for position in range(word_length):
    placeholder +="_"
print("word to guess"+placeholder)

game_over =False
correct_letters =[]

while not game_over:
    
    guess =input("guess a letter:").lower()
    if guess in correct_letters:
        print(f"you'v already guessed{guess}")
    display = ""
    for letter in chosen_words:
        if letter ==guess:
            display +=letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display +=letter
        else:
            display += "_"
    print("word to guess: "+display)

    if guess not in chosen_words:
        lives -=1
        if lives==0:
            game_over =True
            print("*****you lose***")
    if "_" not in display:
        game_over =True
        print("*****youwin***")
    print(stages[lives])        
