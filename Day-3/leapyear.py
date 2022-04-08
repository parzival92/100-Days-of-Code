# Write a program that works out whether if a given year is a leap year. A normal year has 365 days, leap years have 366, with an extra day in February. 
# The reason why we have leap years is really fascinating, this video does it more justice:

#Logic
# Start >> if year cleanly divisible by 4 >> if no >> its not leap year >> if yes >> year cleanly divisible by 100>
# if no >> leap year >> if yes >> year is cleanly divisible by 400 >> if no >> not leap >> if yes leap year

# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year.")
        else:
            print("Not leap year")
    else:
        print("Leap year.")
else:
    print("Not leap year.")

