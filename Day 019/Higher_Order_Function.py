"""
    A function is called Higher Order Function if it contains other
    functions as a parameter or returns a
    function as an output i.e,
    the functions that operate with another function are known as Higher order Functions.
    It is worth knowing that this higher order function is applicable for functions and
    methods as well that takes functions as a parameter or returns a function as a result.
    Python too supports the concepts of higher order functions.
 """

def add(n1,n2):
    return n1+n2

def substract(n1,n2):
    return n1-n2

def multiply(n1,n2):
    return n1*n2

def divide(n1,n2):
    return n1/n2

def calculate(n1,n2,func):
    return func(n1,n2)

print(calculate(2,3,multiply))
print(calculate(2,3,add))
print(calculate(2,3,substract))
print(calculate(2,3,divide))