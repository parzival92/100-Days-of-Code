#num_char = len(input("What is your name?"))
#print("Your name has "+ num_char + " Characters")

#Above code produce error -- TypeError: can only concatenate str (not "int") to str
#print(type(num_char))

# Type Conversion

num_char = len(input("What is your name?"))
str_char = str(num_char)
print("Your name has "+ str_char + " Characters")