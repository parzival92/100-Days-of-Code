print('''
*******************************************************************************
 _ _ _                 _             _   _ 
(_) | |               (_)           | | (_)
 _| | |_   _ _ __ ___  _ _ __   __ _| |_ _ 
| | | | | | | '_ ` _ \| | '_ \ / _` | __| |
| | | | |_| | | | | | | | | | | (_| | |_| |
|_|_|_|\__,_|_| |_| |_|_|_| |_|\__,_|\__|_|
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

choice1=input('You\'re at a crossroad. Where do you want to go? Type "left" or "right').lower()

if choice1 == "left":
    choice2=input('\'You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.\'').lower()
    if choice2 == "wait":
        choice3=input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?").lower()
        if choice3 == "red":
            print("Its room full of fire.Game Over")
        elif choice3 == "yellow":
            print("Yayyyyyyyyy !!! You found the treasure")
        elif choice3 == "blue":
            print("Its room full of fire.Game Over")

    else:
        print("Attacked by tryout!Game Over")
else:
    print("You fell into the hole.Game Over")


