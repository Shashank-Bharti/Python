from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

m = Menu()
cm = CoffeeMaker()
mm = MoneyMachine()

is_working = True
while is_working != False:
    order = input(f"What would you like to order?\n{m.get_items()}\nType here-> ").lower()
    
    if order == 'report':
        cm.report()
        mm.report()
    elif order == 'off':
        print("Machine has been turned off")
        is_working = False
    else:
       drink = m.find_drink(order)
       
       if cm.is_resource_sufficient(drink=drink) and mm.make_payment(drink.cost):
           cm.make_coffee(drink)
           