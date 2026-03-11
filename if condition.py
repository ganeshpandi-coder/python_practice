a=int(input("enter a number"))
if a>0:
    print("positive number")
else:
    print("negative number")
    
#----------#

a=int(input("enter a number"))
if a%2==0:
    print("even number is:",a)
else:
    print("odd number is:",a)

#----------#

a=int(input("enter a first number"))
b=int(input("enter a  second number"))
if a>b:
    print("largest number is :",a)
else:
    print("largest number is :",b)

#-----------#

a=int(input("enter a first number"))
b=int(input("enter a  second number"))
c=int(input("enter a third number"))
if a>b and a>c:
      print("largest number is :",a)
elif b>c:
    print("largest number is :",b)
else:
     print("largest number is :",c)

#-----------#

a=int(input("enter a number"))
if a%5==0 and a%11==0:
    print("divisible by 5 and 11")
else:
    print("not divisible by 5 and 11")

#------------#

year=int(input("enter a year is :"))
if year%400==0:
    print("leap year")
else:
    print(" not a leap year")

#-------------#

a=input("enter a character:")
if a.lower()in['a','e','i','o','u']:
    print("vowels")
else:
    print("consonant")


#----------#

a=int(input("enter a number"))
if a%3==0 and a%7==0:
    print("multiple of 3 and 7")
else:
    print("not multiple of 3 and 7")

#------------#

a=int(input("enter a number :"))
if 100<=abs(a)<=999:
    print("three digit number")
else:
    print("not a three digit number")

#-----------#

a=int(input("enter a number :"))
if a>100:
    print("number is greater than 100")
else:
    print("number is not greater than 100")

    






























    
