# *args 

def add(*args):
    print(args[0]) # Access elements at first position
    sum = 0
    for n in args:
        sum += n
    return sum

print(add(2,41,69,89,7,3,5,7,2,5,2))
    
# **kwargs - Keyword arguments - Converts into disctionary

def calculate(n,**kwargs):
    print(kwargs)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(2,add=3,multiply=5)


class Car:

    def __init__(self,**kw):
        self.make = kw["make"]
        self.model = kw.get("model") # Will return if no model arg is present

my_car =Car(make="Nissan")
print(my_car.model)