#check whether a number is prime or not.

a=int(input("enter the number"))
count=0
for i in range(1,a+1):
    if a%i==0:
        count+=1
if count==2:
    print("prime number")
else:
    print("not a prime number")
