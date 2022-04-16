#Example : Randomization
#Remember to use the random module
#Hint: Remember to import the random module here at the top of the file. 🎲
import random	 

rand_num = random.randint(0,1)

if rand_num == 0:
    print("Tails")
else:
    print("Heads")