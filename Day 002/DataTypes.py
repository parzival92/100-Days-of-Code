# Write a program that adds the digits in a 2 digit number. e.g. 
# if the input was 35, then the output should be 3 + 5 = 8
#Example Input
#39
#Example Output
#3 + 9 = 12
#12

two_digit_number = input("Type a two digit number")
first_digit = int(two_digit_number[0])
second_digit = int(two_digit_number[1])
result = first_digit + second_digit
print(result)