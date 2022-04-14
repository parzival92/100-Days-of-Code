

from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


# def encrypt(plain_text,shift_amount):
#     # list_encode = []
#     # for i in range(0,len(plain_text)):
#     #     index = 0
#     #     for j in range(0,len(alphabet)):
#     #         if plain_text[i] == alphabet[j]:
#     #             index = j + shift_amount
#     #             list_encode[i] = alphabet[index]
#     # print(f"The index is{list_encode}")
#     cipher_text = ""
#     for letter in plain_text:
#         position =alphabet.index(letter)
#         new_position = position + shift_amount
#         cipher_text += alphabet[new_position]
#     print(f"The Cipher text is {cipher_text}")
        
        
# def decrypt(cipher_text,shift_amount):
#   plain_text = ""
#   for letter in cipher_text:
#       position = alphabet.index(letter)
#       new_position = position - shift_amount
#       plain_text += alphabet[new_position]
#   print(f"The decode text is {plain_text}")

def caeser(start_text,shift_amount,direction):
    end_text = ""
    if direction == "decode":
            shift_amount *= -1
    for letter in start_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = position + shift_amount
            end_text +=alphabet[new_position]
        else:
            end_text += letter
    print(f"The {direction} text is {end_text}")

should_continue = True

while should_continue:
    
    print(logo)
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26

    caeser(start_text=text,shift_amount=shift,direction=direction)  
    result = input("Type 'yes' if you want to go again.Otherwise type ''no'.\n").lower()
    if result == "no":
        should_continue= False
        print("Goodbye")

# if direction == "encode":
#     encrypt(plain_text= text,shift_amount =shift)
# elif direction == "decode":
#     decrypt(cipher_text=text,shift_amount=shift)