# #Hangman Game
import random
import Img_Hangman

print("WELCOME TO MOIN GAMES")
print("    H A N G M A N    ")
word_list = ["aardvark", "baboon", "camel","Crocodile" , "Elephant" , "Apple" , "Cat" , "Nuclear" , "Aeroplane" , "Pakistan"]
# word_list = ["apple"]

word = random.choice(word_list)
word = word.lower()

#Printing Underscore equal to word
guess_word = ["_"]
for val in range(len(word)-1):
    guess_word = guess_word + ["_"]
print("".join(guess_word))

wrong_word = [""]

Game = False
lives = 7
while not Game == True:
    guess = input("Guess the word: ").lower()

    display = " " 
    if guess in guess_word or guess in wrong_word:
        print("You Type this first . Try another word")
    else:
        if guess in word:
            for val in range(len(word)):
                if word[val] == guess:
                    guess_word[val] = guess
            print("You Guess the character in word")
            if not '_' in guess_word:
                Game = True
        else:
            lives = lives -1
            wrong_word.append(guess)
            print(f"You type wrong character. Your lives are {lives}")
            print(Img_Hangman.stages[lives])
            if lives == 0:
                Game = True

    print("".join(guess_word))
    

if "_" not in guess_word:
    print("Congratulations, you won!")
else:
    print("Game over! \nThe word was:", word)
