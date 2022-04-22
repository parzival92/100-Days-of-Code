from art import vs
from art import logo
print(logo)

from game_data import data
import random

continue_game = False
score = 0
while not continue_game:
    compare_A = random.choice(data)
    print(f"You're right! Current score: {score}")
    print(f"Compare A: {compare_A['name']}, a {compare_A['description']}, from {compare_A['country']}")
    print(vs)
    compare_B = random.choice(data)
    print(f"Compare B: {compare_B['name']}, a {compare_B['description']}, from {compare_B['country']}")
    user_choice = input("Who has more followers? Type 'A' or 'B': ").lower()
    if user_choice == 'a':
        if compare_A['follower_count'] > compare_B['follower_count']:
            score +=1
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            continue_game = True
    elif user_choice == 'b':
        if compare_B['follower_count'] > compare_A['follower_count']:
            score +=1
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            continue_game = True



