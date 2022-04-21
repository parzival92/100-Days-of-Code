# Fix the code so that it works and when you hit submit it should pass all the tests.

year = int(input("Which year do you want to check?")) # Error: Use int to typecast as input will be str type

if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Leap year.")
    else:
      print("Not leap year.")
  else:
    print("Leap year.")
else:
  print("Not leap year.")