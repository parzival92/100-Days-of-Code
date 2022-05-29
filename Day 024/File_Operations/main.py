# Print Content from file
""" file = open("myfile.txt")
contents = file.read()
print(contents)
file.close() """ # Free resources which are getting consumed 

# Open file with keyword

''' with open("myfile.txt") as file:
    contents = file.read()
    print(contents) 
'''

# Write File default mode read mode
# Write will overwrite on existing file use append to add content

'''
with open("newfile.txt",mode="w") as file:
    file.write("This file does not exist and it will get created as mode is write and it works only in write mode")

with open("myfile.txt",mode="a") as file:
    file.write("\nThis text got appended here")
'''
# Relative and Absolute Path
# Two directory back ../../
# One Directory back ../
with open("../../parz.txt",mode="w") as file:
    file.write("This file does not exist and it will get created as mode is write and it works only in write mode")




