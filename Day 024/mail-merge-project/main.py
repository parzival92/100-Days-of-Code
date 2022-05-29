#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: This method will help you: https://www.w3schools.com/python/ref_string_strip.asp


PLACEHOLDER = "[name]"
with open("./Input/Names/invited_names.txt") as names_file:
    names_list = names_file.readlines()
    names_chec = names_list

    
with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    for name in names_list:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER,stripped_name)
        with open(f"./Output/ReadyToSend/letters_for_{stripped_name}.txt",mode='w') as sendfile:
            sendfile.write(new_letter)
        names_list = names_chec
