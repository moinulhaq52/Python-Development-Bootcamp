print("Welcome to Secret Auction 2025")
dictionary = {}
def user_input():
    name = input("Enter Your name:\n")
    bid = int(input("Enter Your Bid:\n"))
    dictionary[name] = bid
    other = input("Is there another who want to bid: Type 'yes' or 'not \'").lower()
    if other == "yes":
        print("\n"*50)
        user_input()
    else:
        greater = 0
        new_name = "ABC"
        for key in dictionary:
            if greater < dictionary[key]:
                greater = dictionary[key]
                # print(greater)
                new_name = key
            else:
                # print(greater)
                pass
        print(f"{new_name} , {greater}")

user_input()

