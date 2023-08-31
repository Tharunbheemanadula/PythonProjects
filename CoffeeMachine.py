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

money_earned=0


def checking_resources(drink_ingridents):
     for item in drink_ingridents:
         if drink_ingridents[item]>resources[item]:
             print(f"Sorry {item} are not enough ")
             return False
     return True
def processCoins():
    """Return total calculated"""
    print("please insert coins")
    total=int(input("how many quarters?:"))*0.25
    total += int(input("how many dimes?:")) * 0.1
    total += int(input("how many nickles?:")) * 0.05
    total += int(input("how many pennies?:")) * 0.01
    return total

def isTransactionSuccesfull(monyReceived ,drink_cost):
    if monyReceived>drink_cost:
        change=round(monyReceived-drink_cost,2)
        print(f"Here is your change ${change}")
        global money_earned
        money_earned+=drink_cost
        return True
    else:
        print(f"Sorry that's not enough money, Money refunded,cost  of drink is {drink_cost}")
        return False



def make_drink(choice,ingredients):
    for item in ingredients:
        resources[item]-=ingredients[item]
    print(f"Here is your {choice}🍵🍵☕")
is_on=True

while is_on:
    user_input=input("What would you like? (espresso/latte/cappuccino):")

    if user_input=="off":
        is_on =False
    elif user_input == "report":
        print(f"water available:{resources['water']}")
        print(f" milk available:{resources['milk']}")
        print(f"coffee available:{resources['coffee']}")
        print(f"Profit earned:{money_earned}")
    else:
        drink=MENU[user_input]
        if checking_resources(drink["ingredients"]):
            payment=processCoins()
            if isTransactionSuccesfull(payment,drink["cost"]):
                make_drink(user_input,drink['ingredients'])



