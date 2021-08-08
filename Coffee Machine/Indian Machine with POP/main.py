import data

def insertCoins(coffeetype):
    print("Enter Coins: ")
    coin10 = int(input("How many ₹10 coin?: "))
    coin5 = int(input("How many ₹5 coin?: "))
    coin2 = int(input("How many ₹2 coin?: "))
    coin1 = int(input("How many ₹1 coin?: "))
    mymoney = data.resources["money"]
    mymoney = coin1 + 2*coin2 + 5*coin5 + 10*coin10
    if mymoney < data.MENU[coffeetype]["cost"]:
        print("Sorry that's not enough money.\nMoney refunded.")
    elif mymoney > data.MENU[coffeetype]["cost"]:
        data.resources["water"] -= data.MENU[coffeetype]["ingredients"]["water"]
        data.resources["coffee"] -= data.MENU[coffeetype]["ingredients"]["coffee"]
        data.resources["money"] += data.MENU[coffeetype]["cost"]
        print(f"Here is ₹{mymoney - data.MENU[coffeetype]['cost']} in change.\nHere is your {coffeetype}. Enjoy!")
    else:
        data.resources["water"] -= data.MENU[coffeetype]["ingredients"]["water"]
        data.resources["coffee"] -= data.MENU[coffeetype]["ingredients"]["coffee"]
        data.resources["money"] += data.MENU[coffeetype]["cost"]
        print(f"Here is your {coffeetype}. Enjoy!")

def makecoffee(userchoice):
    if userchoice == "espresso":
        if data.resources["water"] < data.MENU[userchoice]["ingredients"]["water"]:
            print("Sorry there is not enough water.")
        elif data.resources["coffee"] < data.MENU[userchoice]["ingredients"]["coffee"]:
            print("Sorry there is not enough coffee.")
        else:
            insertCoins(userchoice)
    else:
        if data.resources["water"] < data.MENU[userchoice]["ingredients"]["water"]:
            print("Sorry there is not enough water.")
        elif data.resources["milk"] < data.MENU[userchoice]["ingredients"]["milk"]:
            print("Sorry there is not enough milk.")
        elif data.resources["coffee"] < data.MENU[userchoice]["ingredients"]["coffee"]:
            print("Sorry there is not enough coffee.")
        else:
            insertCoins(userchoice)

stayOn = True
while stayOn == True:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if choice == "espresso" or choice == "latte" or choice == "cappuccino":
        print(f"Your order is an {choice.capitalize()}☕☕")

    if choice == "espresso":
        print(data.resources)
        makecoffee("espresso")
    elif choice == "latte":
        makecoffee("latte")
    elif choice == "cappuccino":
        makecoffee("cappuccino")
    elif choice == "report":
        print(f"Water: {data.resources['water']}")
        print(f"Milk: {data.resources['milk']}")
        print(f"Coffee: {data.resources['coffee']}")
        print(f"Money: {data.resources['money']}")
    elif choice == "off":
        print("Coffee Machine Shutting Down!")
        stayOn = False

