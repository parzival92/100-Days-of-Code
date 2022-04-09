#Example: List 
# You are going to write a program that will select a random name from a list of names. The person selected will have to pay for everybody's food bill.

import random

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆
start_index = 0
end_index = len(names) -1
random_choice =random.randint(start_index,end_index)
print(f"{names[random_choice]} is going to buy the meal today!")
