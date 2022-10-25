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


resources["money"] = 0


def coffee_machine():
    choice = input("What would you like? Espresso, Latte, or Cappuccino? ").lower()
    if choice == "off":
        return
    if choice == "report":
        print_report()
        coffee_machine()
    else:  # Got the logic working here, we get the money to reduce
        total_paid = calculate_total()
        while total_paid >= MENU[choice]["cost"]:
            if total_paid > MENU[choice]["cost"]:
                change = total_paid - MENU[choice]["cost"]
                resources["money"] += MENU[choice]["cost"]
                print(f"You have successfully paid for you coffee with a change of ${change}")
            elif total_paid == MENU[choice]["cost"]:
                print(f"You have successfully paid ${total_paid}")
                resources["money"] += MENU[choice]["cost"]
            water = MENU[choice]["ingredients"]["water"]
            coffee = MENU[choice]["ingredients"]["coffee"]
            resources["water"] -= water
            resources["coffee"] -= coffee
            # print(resources["coffee"])
            if choice == 'latte' or choice == 'cappuccino':
                milk = MENU[choice]["ingredients"]["milk"]
                resources["milk"] -= milk
            coffee_machine()
        print(f"${total_paid} is not enough for your coffee, try again!")
        coffee_machine()


coffee_machine()
