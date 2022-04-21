# Fix Bug


for number in range(1, 101):
  if number % 3 == 0 and number % 5 == 0:  # use and in place of or 
    print("FizzBuzz")
  elif number % 3 == 0: # use elif as it will check every if is used 
    print("Fizz")
  elif number % 5 == 0:
    print("Buzz")
  else:
    print(number)  #Remove Square