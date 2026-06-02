#Black Jack Game
import random
#Card
# card = [2,3,4,5,6,7,8,9,10,'Q','J','K','A']
card = [2,3,4,5,6,7,8,9,10,10,10,10,11]


#input for starting game
start = input("Can we start the game... Type 'y' for start or 'n' for not:\n").lower()





#function for pass or hit
def calculate_sum(cards):
    total = sum(cards)
    A = cards.count(11)
    while total > 21 and A:
        total -= 10
        A -= 1
    return total


#Check the sum
def hit(user_sum , dealer_sum):
    if dealer_sum > 21:
        print("You Win")
        print(f"Dealer sum are : {dealer_sum}")
    elif user_sum > 21:
        print(user_sum)
        print("Out")
        print(dealer_sum)
    elif user_sum < 21 and user_sum > dealer_sum:
        print("You win")
    elif user_sum == dealer_sum:
        print("Draw")
        print(dealer_sum)
    else:
        print("Dealer Win")
        print(dealer_sum)


#function of sum and main
def final():
    Final = ""
    while Final != "stand" and Final != "hit":
        main = input("You can stand or hit: \n").lower()
        Final = main
        # user_sum = ""
        # dealer_sum = ""
    if Final == "stand":
        user_sum = calculate_sum(User)
        print(user_sum)
        dealer_sum = calculate_sum(Dealer)
        print(dealer_sum)
        hit(user_sum , dealer_sum)
    if Final == "hit":
        User.append(random.choice(card))
        print("Yours Cards are :")
        print(User)
        print("Dealer Cards are :")
        print(f"[{Dealer[0]}],")
        # print("hit")
        hit(calculate_sum(User) , calculate_sum(Dealer))
        final()

        


#Start game
if start == 'y':
    Game = 1
    User = []
    Dealer = []
    while Game == 1:
        print("Yours Cards are :")
        User.append(random.choice(card))
        User.append(random.choice(card))
        print(User)
        print("Dealer Cards are :")
        Dealer.append(random.choice(card))
        Dealer.append(random.choice(card))
        print(f"[{Dealer[0]}, ]")
        if calculate_sum(Dealer) < 17:
            Dealer.append(random.choice(card))
            print("Dealer can hit")
        final()
        End = input("Can you play again (Type 'yes' or 'no') :\n").lower()
        if End == "yes":
            User = []
            Dealer = []
        else:
            Game = 0
            print("OK:)")
            

#if not
elif start == "n":
    print("OK:)")

else:
    print("you type wrong word")
    print("Bye")

