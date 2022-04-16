



import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_images = [rock,paper,scissors]
#Write your code below this line 👇

your_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
computer_choose = random.randint(0,2)
if your_choice >=3 or your_choice<0:
    print("You typed an invalid no.")
else:
    print(game_images[your_choice])
print("computer_choose:")
print(game_images[computer_choose])
if your_choice >=3 or your_choice<0:
    print("You typed an invalid no.")
elif your_choice ==0 and computer_choose ==2:
    print("You win!")
elif your_choice ==2 and computer_choose ==0:
    print("You Loose!")
elif your_choice == computer_choose:
    print("It's a Draw")
elif computer_choose > your_choice:
    print("You lose!!")
elif your_choice>computer_choose:
    print("You Win!!")
elif your_choice >=3 or your_choice<0:
    print("You typed an invalid no.")


    