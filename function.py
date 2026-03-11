#function to add two numbers
def add(a,b):
 return a+b
print(add (10,11))

#function to subtract two numbers

def subtract(a,b):
 return a-b
print(subtract(10,11))

#function to multiply two numbers.

def multiple(a,b):
 return a*b
print(multiple(10,11))

#function to divide two numbers.

def divide(a,b):
 return a/b
print(divide(10,11))

#function to find the square of a number

a=int(input("enter a nunber"))
def square (num):
    return num*num
print("square is:",square(a))

#check whether a number is even or odd.

a=int(input("enter the first number"))
b=int(input("enter the second number"))
result=0
def demo(a,b):
    for i in range (a,b):
        if i%2==0:
            print(i,"is even number")
        else:
            print(i,"is odd numbber")
demo(a,b)

#find the largest of two numbers.

a=int(input("enter the  first number"))
b=int(input("enter the second number"))
def largest_num(a,b):
    if a>b:
        print("the largest numbar is :",a)
    else:
        print("the largest number is :",b)
largest_num(a,b)

#count vowels in a string.

a=input("enter the string")
def vowels_string(s):
    vowels="aeiouAEIOU"
    for i in (s):
        if i in vowels:
            print(i)
vowels_string(a)

#reverse a string.

a=input("enter the string")
def demo(a):
    print(a[::-1])
demo(a)

#find factorial of a number

a=int(input("enter the number"))
def demo(a):
    fact=1
    for i in range(1,a+1):
        fact=fact*i
        print("factorial is:",fact)
demo(a)

#find sum of list elements.

def sum_list(numbers):
    total=0
    for i in numbers:
        total=total+i
    print("sum of list :",total )
a=[10,14,16,20,25,30]
sum_list(a)

#find maximum number in a list.

a=[12,32,16,54,886,92,234,765]
def function(a):
    max_val=a[0]
    for i in a:
        if i >max_val:
            max_val=i
    return max_val
print("maximum number is:",function(a))


#check whether a number is prime.

num=int(input("enter the nunber"))
def prime(n):
    for i in (2,n):
        if n%2==0:
            print(num,": is not prime number")
        else:
            print("prime number is :",num)   
prime(num)

#count characters in a string

a=input(" enter the string ")
def count(s):
    return len(s)
print("number of characters",count(a))

#return multiplication table of a number.

a=int(input("enter the number :"))
def table(n):
    for i in range (1,11):
        print(i,"x",n,"=",n*i)
table(a)
