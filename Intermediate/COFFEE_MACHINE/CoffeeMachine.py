#First Intermediate Project
from Data import MENU
from Data import resources

#Print for knowledge for user
print("For Machine off : Type 'Off'")
print("For Report of Resources: Type 'Report'")
print("For Prices of Coffee: Trype 'Prices'")

#prices of coins
quarters = 0.25
dimes = 0.10
nickles = 0.05
pennies = 0.01

#profit
profit = 0 


#Fuction for Resources Deduction
def Resource_check_deduct(Coffee_name):
    coffee_ = Coffee_name

    #Function for Deduct Resources
    def Deduct_Resources():
        global resources
        resources["water"] -= water
        resources["milk"] -= milk
        resources["coffee"] -= coffee
        


    #Main
    water  = MENU[coffee_]["ingredients"]["water"]
    milk   = MENU[coffee_]["ingredients"]["milk"]
    coffee = MENU[coffee_]["ingredients"]["coffee"]
    if resources["water"] < water or resources["milk"] < milk or resources["coffee"] < coffee:
        print("Low Resources")
        #convert this in function
        # print(f"Water  : {resources["water"]} ml")
        # print(f"Milk   : {resources["milk"]} ml")
        # print(f"Coffee : {resources["coffee"]} g")
        print_resources("water")
        print_resources("milk")
        print_resources("coffee")
    else:
        #  quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
        print("Enter the Coins Quantity")
        quarter = float(input("How many quarters: "))
        dime = float(input("How many dimes: "))
        nickle = float(input("How many nickles: "))
        pennie = float(input("How many pennies: "))
        Total_user_money = (quarters * quarter) + (dimes * dime) + (nickles * nickle) + (pennies * pennie)
        if Total_user_money < MENU[coffee_]["cost"]:
            print("You dont have enough money")
            print(f"Your change is {Total_user_money}")
            #Use function there
            # print(f"Espresso   : {MENU["espresso"]["cost"]} $")
            # print(f"Latte      : {MENU["latte"]["cost"]} $")
            # print(f"Cappuccino : {MENU["cappuccino"]["cost"]} $")
            print_Cost("espresso")
            print_Cost("latte")
            print_Cost("cappuccino")
        else:
            print(f"Enjoy Your Coffee {coffee_}") 
            print(Total_user_money)
            print(MENU[coffee_]["cost"])
            change = Total_user_money - MENU[coffee_]["cost"]
            print(f"Your change is {change}")
            Deduct_Resources()
            global profit
            profit += float(MENU[coffee_]["cost"])

        
#Fuction for print Resources
def print_resources(resource):
    print(f"{resource}  :  {resources[f"{resource}"]}")

#Function for print Cost
def print_Cost(coffee):
    print(f"{coffee}  :  {MENU[f"{coffee}"]["cost"]} $")




is_Machine = True
while is_Machine:
    Main = input("What would you like? (espresso/latte/cappuccino):").lower()
    if Main == "report":
        print("Report: ")
        # print(f"Water  : {resources["water"]} ml")
        # print(f"Milk   : {resources["milk"]} ml")
        # print(f"Coffee : {resources["coffee"]} g")
        print_resources("water")
        print_resources("milk")
        print_resources("coffee")
        print(f"Profit : {profit} $")
    elif Main == "prices":
        # print(f"Espresso   : {MENU["espresso"]["cost"]} $")
        # print(f"Latte      : {MENU["latte"]["cost"]} $")
        # print(f"Cappuccino : {MENU["cappuccino"]["cost"]} $")
        print_Cost("espresso")
        print_Cost("latte")
        print_Cost("cappuccino")

    elif Main == "off":
        print("Machine is off")
        is_Machine = False
    elif Main == "espresso":
        print("Espresso")
        Resource_check_deduct("espresso")
    elif Main == "latte":
        print("Latte")
        Resource_check_deduct("latte")
    elif Main == "cappuccino":
        print("Cappuccino")
        Resource_check_deduct("cappuccino")
    else:
        print("You Type Wrong !! Try Again")


# print(MENU["espresso"]["ingredients"]["coffee"])


 