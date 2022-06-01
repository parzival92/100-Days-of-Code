""" Instructions
You are going to use Dictionary Comprehension to create a dictionary called result that takes each word in the given sentence and calculates the number of letters in each word.

Try Googling to find out how to convert a sentence into a list of words.

Do NOT Create a dictionary directly. Try to use Dictionary Comprehension instead of a Loop.

Example Output
{
'What': 4, 
'is': 2, 
'the': 3, 
'Airspeed': 8, 
'Velocity': 8, 
'of': 2, 
'an': 2, 
'Unladen': 7, 
'Swallow?': 8
} """


from unittest import result


sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# Don't change code above 👆

# Write your code below:
split_sentence = sentence.split()

result ={word:len(word) for word in split_sentence}

print(result)

# Looping in Dictionary
student_dict = {
    "student" : ["Angela","James","Lily"],
    "score" : [56,76,98]
}
for (key,value) in student_dict.items():
    #print(value)
    pass

#Looping through Pandas

import pandas

student_data_frame = pandas.DataFrame(student_dict)
#Loop through Data frame
for (key,value) in student_data_frame.items():
    print(key)
    print("-------------------------------")

#Loop through row
for(index,row) in student_data_frame.iterrows():
    if row.student == "Angela":
        print(row.score)
