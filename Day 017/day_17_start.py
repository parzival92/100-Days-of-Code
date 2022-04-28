class User:
    """Class User is used to create user using object"""
    def __init__(self,user_id,username): #Constructor
        #parameter means you need to provide arguments
        # Initialize Attributes
        print("Constructor is being called")
        self.user_id = user_id  #Attribute pased as paramater
        self.username = username
        self.followers = 0
        self.following = 0
      
    def follow(self, user):
        """ Follow method """
        user.followers +=1
        self.following +=1           

user_1 = User("001","parzival")
user_2 = User("002","Jack")
user_1.follow(user_2)

print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)