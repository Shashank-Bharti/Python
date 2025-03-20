# GLOBAL VARIABLES BELOW
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.50,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.50,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.00,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

dime = 0.10
penny = 0.01
nickel = 0.05
quarter = 0.25

money = 0
def check_resources(option):
    if option == 'report':
        print(f"Remaining resources are :\nWater :{resources['water']}ml\nMilk :{resources['milk']}ml\nCoffee :{resources['coffee']}g \nMoney: ${money}")
    elif option == '1': #espresso
        if all(MENU["espresso"].get(key, 0) <= resources[key] for key in resources):
            print(f"Order Cost : ${MENU['espresso']['cost']:.2f}")
            return True
        
        else:
            return False
            
    elif option == '2': #latte
        if all(MENU["latte"].get(key, 0) <= resources[key] for key in resources):
            print(f"Order Cost : ${MENU['latte']['cost']:.2f}")
            return True
    
        else:
            return False
            
    elif option == '3': #cappuccino
    
        if all(MENU["cappuccino"].get(key, 0) <= resources[key] for key in resources):
            print(f"Order Cost : ${MENU['cappuccino']['cost']:.2f}")
            return True
        else:
            return False
    else:
        return "invalid"

    

#TODO-1 ask user to choose b/w espresso/latte/cappucino
user_choice = input("1. espresso\n2. latte \n3. cappuccino\nWhat would you like to order? : ")

# TODO-1.5 Check if resources are availiable for the chosen option ,
# if yes --> proceed to pay req if not --> end program print Sorry resources are not sufficient

if check_resources(user_choice) != False:
    print("Please insert coins.")
else:
    print("Resources for this order can't be fulfilled")

    
# TODO-2 Require payment for the chosen coffee how many dimes /quarters/penny /nickel ,store it to -->paid money 

# TODO-3 if req pay is == paid money --> start making coffee ,
# if req pay > paid amt : insufficient amount paid --> returns money loops back to todo 2 ,
# if paid > req amount deduct coffee price from paid amt and return the remaining money --> Start making coffee

# TODO-4 make a secret report command to give details of money in machine , and resources left 