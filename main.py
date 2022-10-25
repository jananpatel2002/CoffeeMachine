from data import MENU, resources


def calculate_total():
    pennies = float(input("How many pennies? "))
    nickel = float(input("How many nickels? "))
    dime = float(input("How many dimes? "))
    quarter = float(input("How many quarters? "))
    return round(((pennies * .01) + (nickel * .05) + (dime * .10) + (quarter * .25)), 2)


def print_report():
    for item in resources:
        if item == "coffee":
            print(f"{item.capitalize()}: {resources[item]}g")
        elif item == "money":
            print(f"{item.capitalize()}: ${resources[item]}")
        else:
            print(f"{item.capitalize()}: {resources[item]}ml")


def find_low_ingredient(items, milk, coffee, water):
    if (items["milk"]) - milk < 0:
        return "Not enough milk!"
    elif (items["water"]) - water < 0:
        return "Not enough water!"
    elif (items["coffee"]) - coffee < 0:
        return "Not enough coffee"
    else:
        return "Enough Ingredients"


resources["money"] = 0


def coffee_machine():
    total_paid = 0
    choice = input("What would you like? Espresso, Latte, or Cappuccino? ").lower()
    if choice == "off":
        return
    if choice == "report":
        print_report()
        coffee_machine()
    else:  # Got the logic working here, we get the money to reduce

        water = MENU[choice]["ingredients"]["water"]
        coffee = MENU[choice]["ingredients"]["coffee"]
        if choice == 'latte' or choice == 'cappuccino':
            milk = MENU[choice]["ingredients"]["milk"]
            if find_low_ingredient(resources, milk, coffee, water) == "Enough Ingredients":
                total_paid = calculate_total()
            else:
                print(find_low_ingredient(resources, milk, coffee, water))
                coffee_machine()
        if choice == 'espresso':
            if not resources["water"] - water < 0 and not resources["coffee"] - coffee < 0:
                total_paid = calculate_total()
            else:
                print(find_low_ingredient(resources, 0, coffee, water))
                coffee_machine()

        while total_paid >= MENU[choice]["cost"]:
            if total_paid > MENU[choice]["cost"]:
                change = total_paid - MENU[choice]["cost"]
                resources["money"] += MENU[choice]["cost"]
                print(f"You have successfully paid for you coffee with a change of ${round(change, 2)},"
                      f" here is your {choice.capitalize()}")
            elif total_paid == MENU[choice]["cost"]:
                print(f"You have successfully paid ${total_paid}, here is your {choice.capitalize()}")
                resources["money"] += MENU[choice]["cost"]
            resources["water"] -= water
            resources["coffee"] -= coffee
            # print(resources["coffee"])
            coffee_machine()
        print(f"${total_paid} is not enough for your coffee, try again!")
        coffee_machine()


coffee_machine()
