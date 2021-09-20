import data


def proccess(order):
    def print_report():
        print(f"Water: {data.resources.get('water')}ml")
        print(f"Milk: {data.resources.get('milk')}ml")
        print(f"Coffee: {data.resources.get('coffee')}g")
        print(f"Money: ${data.resources.get('money')}")

    if order == "report":
        print_report()
        return True

    if order in list(data.MENU):
        resources = data.resources

        ingredients = data.MENU.get(order).get("ingredients")
        price = float(data.MENU.get(order).get("cost"))

        for key in list(ingredients):
            if int(ingredients.get(key)) > int(resources.get(key)):
                print(f"Sorry, there is not enough {key}.")
                return False

        print("Please insert coins.")
        quarters = int(input("How many quarters?: ")) * 0.25
        dimes = int(input("How many dimes?: ")) * 0.10
        nickles = int(input("How many nickles?: ")) * 0.05
        pennies = int(input("How many pennies?: ")) * 0.01

        total = quarters + dimes + nickles + pennies

        if total > price:
            change = total - price
            resources.update({"money": int(resources.get("money")) + price})
            print(f"Here is ${change} in change.")
        elif price > total:
            print(f"You don't have enough money.")
            return False

        for key in list(ingredients):
            resources.update({key: int(resources.get(key)) - int(ingredients.get(key))})

        print(f"Here is your {order} ☕ Enjoy!")
        return True
    else:
        print(f"Please select valid order.")
        return False


while True:
    request = input("What would you like? (espresso/latte/cappuccino): ")
    proccess(request)
