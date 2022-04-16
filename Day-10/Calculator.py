logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""
#Calculator

#Add
def add(n1,n2):
    return n1+n2
#Substract
def substract(n1,n2):
    return n1-n2
#Multiply
def multiply(n1,n2):
    return n1*n2
#Divide
def divide(n1,n2):
    return n1/n2

operations = {
                "+" : add,
                "-" : substract,
                "*" : multiply,
                "/" : divide
}
def calculator():
    print(logo)
    num1 = float(input("What is the first number?: "))

    for op in operations:
        print(op)


    should_continue = False

    while not should_continue:
        operation_symbol = input("Pick the operation symbol above: ")
        num2 = float(input("What is the next number?: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1,num2)

        print(f"{num1} {operation_symbol} {num2} ={answer}")
        cont =input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start new calulation.: ").lower()
        if cont == 'y':
            num1 = answer
        else:
            should_continue = True
            calculator()
    
calculator()

