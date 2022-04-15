logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
# define our clear function
# import call method from subprocess module
import os

def clear():
    os.system('cls')  # on windows


print(logo)

def find_highest_record(bidding_record):
    highest_bid =0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with the bid of highest amount of ${highest_bid}")
continue_bid = True
bid_details = {}
while continue_bid:
    name = input("Enter your Name?: ")
    bid = int(input("What's your Bid?: $"))
    
    bid_details[name] = bid
    add_bid = input("Are there any other bidders? Type 'Yes' to continue and 'No' to exit!!!\n").lower()
    if add_bid == "no":
        continue_bid = False
        find_highest_record(bid_details)
    elif add_bid == "yes":
        clear()




