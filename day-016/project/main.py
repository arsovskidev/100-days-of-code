from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# * https://docs.google.com/document/d/e/2PACX-1vTragRHILyj76AvVgpWeOlEaLBXoxPM_43SdEyffIKtOgarj42SoSAsK6LwLAdHQs2qFLGthRZds6ok/pub

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()


def proccess(order):
    if order == "report":
        coffee_maker.report()
        money_machine.report()
        return True

    drink = menu.find_drink(order)
    if drink != None:
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(
            drink.cost
        ):
            coffee_maker.make_coffee(drink)


while True:
    request = input(f"What would you like? ({menu.get_items()}): ")
    proccess(request)
