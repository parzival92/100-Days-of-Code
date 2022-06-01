""" Take a look inside file1.txt and file2.txt. They each contain a bunch of numbers, each number on a new line.

You are going to create a list called result which contains the numbers that are common in both files.

e.g. if file1.txt contained:

1
2
3
and file2.txt contained:

2
3
4
result = [2, 3] """
from unittest import result



with open("file1.txt") as file1:
    file1_data =file1.readlines()
        

with open("file2.txt") as file2:
    file2_data =file2.readlines()

result = [int(new_item) for new_item in file1_data if new_item in file2_data]  
# Write your code above 👆

print(result)