import random
#Modes
print("We have 3 types of modes in game: which one do you selct: 'Easy' , 'Medium' , 'Hard' ")

start = True
# start = False
lives = 0
while start == True:
    #input for mode
    mode_ = True
    while mode_ == True:
        mode = input("Type E for Easy , M for Medium and H for Hard : \n").lower()
        if mode == 'e' or mode == 'm' or  mode == 'h':
            if mode == 'e':
                mode = "Easy"
                lives += 12
            elif mode == 'm':
                mode = "Medium" 
                lives += 8
            elif mode == 'h':
                mode = "Hard"
                lives += 4
            else: 
                print("You type wrong. Read carefully")
                continue
            print(f"Your Mode is {mode}")
            print(f"Your lives are {lives}")
            mode_ = False
    
    #making list
    number = []
    for val in range(0,101):
        number.append(val)
    print(number)

    #Generate random number
    Guess_num = random.choice(number)
    print(Guess_num)
    
    #main function for input of user to guessing input and telling hints
    Game = True
    while Game:
        Guessing = int(input("Guess the number from 0-100: \n"))
        if Guessing == Guess_num:
            print(f"Congrats you find number which is {Guess_num}")
            Game = False
        else:
            if Guessing < Guess_num:
                print("Low")
            if Guessing > Guess_num:
                print("High")
            lives -= 1
            print(f"Remaining lives are {lives}")
            if lives == 0:
                Game = False
                print("You lose your lives")
    #input for again match
    End = True
    while End == True:
        Again = input("Can you play Again (Type 'y' for yes or 'n' for no): \n").lower()
        if Again == 'y':
            start = True
            End =  False
            print("I think You love it..")
        elif Again == 'n':
            start = False
            End = False
            print("Bye")
        else:
            print("You typed wrong word.. Type again")
