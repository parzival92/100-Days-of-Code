#In the starting code, you'll find the solution from the Leap Year challenge. 
# First, convert this function is_leap() so that instead of printing "Leap year." or "Not leap year." 
# it should return True if it is a leap year and return False if it is not a leap year.
#You are then going to create a function called days_in_month() which will take a year and a month as inputs, e.g.
# days_in_month(year=2022, month=2)

def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False

def days_in_month(y,m):
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  leap = is_leap(y)
  print(leap)
  if leap:
      month_days[1] = 29
      return month_days[m-1]
  else:
      return month_days[m-1]

 
#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(y=year, m=month)
print(days)