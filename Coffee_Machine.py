MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money = 0

espresso = 1.50
latte = 2.50
cappuccino = 3.00

pennies = 0.01
dimes = 0.10
nickles = 0.05
quarters = 0.25

machine_on = True

# TODO 1: print report

while machine_on:

    ask_coffee = input("What would you like to have? (espresso/latte/cappuccino): ").lower()

    if ask_coffee == "report":
        print(f"Water: {resources['water']}")
        print(f"Milk: {resources['milk']}")
        print(f"Coffee: {resources['coffee']}")
        print(f"Money: ${money}")

    # TODO 2: check resources sufficient


    def sufficient_resources():
        if ask_coffee == "espresso":
            quarters_received = int(input("How many quarters? $"))
            dimes_received = int(input("How many dimes? $"))
            nickles_received = int(input("How many nickles? $"))
            pennies_received = int(input("How many pennies? $"))
            money_received = (quarters_received * quarters) + (dimes_received * dimes) + (nickles_received * nickles) +\
                             (pennies_received * pennies)
            change_given = round(money_received - espresso, 2)
            if money_received < espresso:
                print("Sorry that's not enough money. Money refunded.")
            else:
                print(f"Here is your ${change_given} in change.\nHere is your espresso. Enjoy!")

        elif ask_coffee == "latte":
            quarters_received = int(input("How many quarters? $"))
            dimes_received = int(input("How many dimes? $"))
            nickles_received = int(input("How many nickles? $"))
            pennies_received = int(input("How many pennies? $"))
            money_received = (quarters_received * quarters) + (dimes_received * dimes) + (nickles_received * nickles) +\
                             (pennies_received * pennies)
            change_given = round(money_received - latte, 2)
            if money_received < latte:
                print("Sorry that's not enough money. Money refunded.")
            else:
                print(f"Here is your ${change_given} in change.\nHere is your latte. Enjoy!")

        elif ask_coffee == "cappuccino":
            quarters_received = int(input("How many quarters? $"))
            dimes_received = int(input("How many dimes? $"))
            nickles_received = int(input("How many nickles? $"))
            pennies_received = int(input("How many pennies? $"))
            money_received = (quarters_received * quarters) + (dimes_received * dimes) + (nickles_received * nickles) +\
                             (pennies_received * pennies)
            change_given = round(money_received - cappuccino, 2)
            if money_received < cappuccino:
                print("Sorry that's not enough money. Money refunded.")
            else:
                print(f"Here is your ${change_given} in change.\nHere is your cappuccino. Enjoy!")

    if ask_coffee == "off":
        machine_on = False





    sufficient_resources()


# TODO 3: process coins


# TODO 4: check transaction successful
# TODO 5: make coffee
