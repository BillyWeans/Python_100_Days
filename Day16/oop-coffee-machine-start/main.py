from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


def run_machine(user_order):

    user_order = input(f"What would you like? ({menu.get_items()}): ").lower()

    if user_order == "off":
        return user_order

    if user_order == "report":
        coffee_maker.report()
        money_machine.report()
        return user_order

    drink = menu.find_drink(user_order)

    # Drink does not exist
    if not drink:
        return user_order

    if not coffee_maker.is_resource_sufficient(drink):
        return user_order

    if not money_machine.make_payment(drink.cost):
        return user_order

    coffee_maker.make_coffee(drink)


money_machine = MoneyMachine()
menu = Menu()
coffee_maker = CoffeeMaker()
order = ""

while not order == "off":
    order = run_machine(order)
