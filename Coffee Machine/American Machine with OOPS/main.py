from typing import Optional
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

stay_on = True

while stay_on == True:
    options = menu.get_items()
    choice = input(f"What would you like ({options}): ").lower()
    if choice == "off":
        stay_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    elif choice == "espresso" or choice == "latte" or choice == "cappuccino":
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
    else:
        print("Wrong Input!")