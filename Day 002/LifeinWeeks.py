#Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.
#It will take your current age as the input and output a message with our time left in this format:
#You have x days, y weeks, and z months left.
# Where x, y and z are replaced with the actual calculated numbers.

# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

diff_age = 90 - int(age)

left_days = diff_age * 365
left_weeks = diff_age * (365//7)
left_month = diff_age * 12
# Use f string to insert int value into string
print(f"You have {left_days} days, {left_weeks} weeks, and {left_month} months left.")