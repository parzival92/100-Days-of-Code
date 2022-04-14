# Review: 
# Create a function called greet(). 
# Write 3 print statements inside the function.
# Call the greet() function and run your code.


def greet(name):
    print(f"Namaste {name}")
    print(f"Hello {name}")
    print(f"ola {name}")

name = input("Enter your name: ")
greet(name)

# Function with one more than 1 input

def greet_with(name,location):
    print(f"Hello {name}")
    print(f"What is it like in {location}")

greet_with("Parzival","Oasis")