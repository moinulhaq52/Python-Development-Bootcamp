from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

#Object for using Classes in Main
coffeemaker = CoffeeMaker()
menu = Menu()
moneymachine = MoneyMachine()

#Main Function
Start = True
while Start:
    Main = input("What would you like? (espresso/latte/cappuccino):").lower()
    if Main == "report":
        coffeemaker.report()
        moneymachine.report()
    elif Main == "off":
        print("Machine Off")
        Start = False
    elif menu.find_drink(Main) != None:
        item = menu.find_drink(Main)
        if coffeemaker.is_resource_sufficient(item) and moneymachine.make_payment(item.cost):
                coffeemaker.make_coffee(item)
