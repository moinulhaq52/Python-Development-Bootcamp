import data
import art
import random

New_data = {}   #for not choosing the same information again
score = 0       #score in Game

Game = True
print("Welcom to Higher Lower Game by Moin")
print(art.logo)
while Game ==  True:
    A = random.choice(data.data)
    while Game == True:
        print(f"Name is {A["name"]} , Country is {A["country"]} , Field is {A["description"]}")
        print(art.vs)

        B = random.choice(data.data)
        if A==B:
            B = random.choice(data.data)
        print(f"Name is {B["name"]} , Country is {B["country"]} , Field is {B["description"]}")


        
        value = input("Type 'A' or 'B' for telling the gratest:").lower()
        # print("Hello")
        if value == "a":
            if A["follower_count"] > B["follower_count"]:
                print("Well Done You Pass this")
                print("A is Gretest")
                score += 1
            else:
                print("You loss")
                Game = False
        elif value == "b":
            if B["follower_count"] > A["follower_count"]:
                print("B is Gretest")
                score +=1
                A = B
            else:
                print("You loss")
                Game = False
        else:
            print("You put Wrong")
    print(f"Your score is {score}")
    Game =  False

# print(New_data.items())
