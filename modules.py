#math module and find square root of a number.

import math
a=int(input("enter the number :"))
print("square root:",math.sqrt(a))

#use math module to find factorial.

import math
a=int(input("enter the number:"))
print("factorial is :",math.factorial(a))

#display all functions in math module using help().

import math
help(math)

#generate a random number using random module.

import random
print ("random number :",random.random())

#generate random number between 1 and 100

import random
print("random number :",random.randint(1,100))

# create a user-defined module for addition.


def add (a,b):
    return a+b

# first create module file then open main program 

import sample2
print(sample2.add(10,3))

# create a module for arithmetic operations.

def add(a,b):
    return(a+b)
def sub(a,b):
    return(a-b)
def mul(a,b):
    return(a*b)
def div(a,b):
    return(a/b)

# main program #

import sample3
print(sample3.add(10,5))
print(sample3.sub(10,5))
print(sample3.mul(10,5))
print(sample3.div(10,5))








