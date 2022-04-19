################## Scope ######################

enemies = 1
def increase_enemies():
    enemies = 2
    print(f"enemy inside function: {enemies}")

increase_enemies()
print(f"enemy outside function: {enemies}")

####################################### There is no block scope ######################################

enemies = ["skeleton","Zombie","Alien"]

game_level = 3
if game_level <5:
    new_enemy = enemies[0] # Accessible outside if scope

print(new_enemy)

####################################### Modifying Global Scope ##############################

enemies = 1
def increase_enemies():
    #enemies += 2 # Erro: UnboundLocalError: local variable 'enemies' referenced before assignment
    #global enemies # Use global to user global variable
    
    print(f"enemy inside function: {enemies}")
    return enemies +1 # return is better 

enemies =increase_enemies()
print(f"enemy outside function: {enemies}")

######################### Global Constants #############################################

PI = 3.14159
URL = "https://google.com"

def cal():
    print(PI) # Use Uppercase to define Ccnstants

cal()