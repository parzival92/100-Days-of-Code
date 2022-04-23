from data import MENU,resources

# Print Report
# Check resources sufficient?
# Process Coins
# Check Transaction Sucessfull
# Make Coffee

IS_ON =True
MONEY=0

def is_resources_sufficient(order_ingredients):
    '''Return Resources are sufficient'''
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True


def process_coin():
    '''Return the total calculated from coin inserted'''
    print("Please insert coins.")
    total = int(input("How many 10rs")) * 10
    total += int(input("How many 20rs")) * 20
    total += int(input("How many 50rs")) * 50
    total += int(input("How many 100rs")) * 100
    return total


def is_transaction_sucessful(money_recieved,drink_cost):
    '''Return True when the payment is accepted or false if money is insufficient'''
    if money_recieved >= drink_cost:
        change = round(money_recieved-drink_cost,2)
        print(f"Here is change: {change}")
        global MONEY
        MONEY += drink_cost
        return True
    else:
        print("Sorry that's not enough money. MoneY refunded")
        return False


def make_coffee(drink_name,order_ingredients):
    '''Deduct the required ingredients from resources'''
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕")

while IS_ON:
    user_choice = input("What would like? (espresso/latte/cappucino): ").lower()

    if user_choice == 'off':
        IS_ON = False


    elif user_choice == 'report':
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffe: {resources['coffee']}g")
        print(f"Money: Rs{MONEY}")

    else:
        drink = MENU[user_choice]
        if is_resources_sufficient(drink["ingredients"]):
            payment = process_coin()
            if is_transaction_sucessful(payment,drink["cost"]):
                make_coffee(user_choice,drink["ingredients"])
