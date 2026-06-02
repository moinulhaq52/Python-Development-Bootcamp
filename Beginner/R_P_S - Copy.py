import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
print("Welcome")
print("Game is Rock Paper Scissors")
Game_val = ["rock" , "paper" , "scissors"]
computer = random.choice(Game_val)
# print(computer)

user = int(input("Type '0' for rock , '1' for paper and '2' for scissor: "))
if user == 0:
    print("You choose rock")
    print(rock)
    print(f"Computer choose {computer}")
    if computer == "rock":
        print(rock)
        print("Match Draw")
    elif computer == "scissors":
        print(scissors)
        print("You Won")
    else:
        print(paper)
        print("You lose")
elif user == 1:
    print("You choose paper")
    print(paper)
    print(f"Computer choose {computer}")
    print(computer)
    if computer == "paper":
        print(paper)
        print("Match Draw")
    elif computer == "rock":
        print(rock)
        print("You Won")
    else:
        print(scissors)
        print("You lose")
elif user == 2:
    print("You choose scissors")
    print(scissors)
    print(f"Computer choose {computer}")
    if computer == "scissors":
        print(scissors)
        print("Match Draw")
    elif computer == "paper":
        print(paper)
        print("You Won")
    else:
        print(rock)
        print("You lose")
else:
    print("You type invalid number")
    print("Game Over")