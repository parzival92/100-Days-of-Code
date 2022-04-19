#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import random


logo = """
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_|  
"""


def check_answer(guess,answer,num_of_chance):
    if guess > answer:
        print("Too high")
        return num_of_chance -1
    elif guess < answer:
        print("Too Low")
        return num_of_chance -1
    else:
        print(f"You got it! The answer was {answer}.")

def set_difficulty():
    difficulty = input("Choose a difficulty.Type 'easy' or 'hard': ").lower()
    num_of_chance = 0
    if difficulty == 'easy':
        num_of_chance = 11
        return num_of_chance - 1
    elif difficulty == 'hard':
        num_of_chance = 6
        return num_of_chance - 1
    else:
        print("Wrong Input")

def game():
  print(logo)
  #Choosing a random number between 1 and 100.
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")
  num = []
  for number in range(1,101):
    num.append(number)

  answer = random.choice(num)
  print(f"Pssst, the correct answer is {answer}") 

  num_of_chance = set_difficulty()
  #Repeat the guessing functionality if they get it wrong.
  guess = 0
  while guess != answer:
    print(f"You have {num_of_chance} attempts remaining to guess the number.")

    #Let the user guess a number.
    guess = int(input("Make a guess: "))

    #Track the number of turns and reduce by 1 if they get it wrong.
    num_of_chance = check_answer(guess, answer, num_of_chance)
    if num_of_chance == 0:
      print("You've run out of guesses, you lose.")
      return
    elif guess != answer:
      print("Guess again.")


game()