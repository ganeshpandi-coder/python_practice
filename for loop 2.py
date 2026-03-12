# Fibonacci series up to n terms
n = int(input("Enter number : "))

a, b = 0, 1
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b

#Sum of digits of a number
num = int(input("Enter a number: "))
sum = 0
while num > 0:
    digit = num % 10
    sum += digit
    num //= 10
print("Sum of digits:", sum)

#Reverse a number using loop

num = int(input("Enter a number: "))
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num //= 10

print("Reversed number:", reverse)

#Count number of vowels in a string

string = input("Enter a string: ")
vowels = "aeiouAEIOU"
count = 0
for ch in string:
    if ch in vowels:
        count += 1
print("Number of vowels:", count)

#Largest element in a list

numbers = [10, 25, 7, 45, 32]
largest = numbers[0]
for num in numbers:
    if num > largest:
        largest = num
print("Largest element:", largest)

#Second largest number in a list

numbers = [10, 25, 7, 45, 32]
largest = second = -999999
for num in numbers:
    if num > largest:
        second = largest
        largest = num
    elif num > second and num != largest:
        second = num
print("Second largest:", second)

#Remove duplicates from a list using loop

numbers = [1, 2, 2, 3, 4, 4, 5]
unique = []
for num in numbers:
    if num not in unique:
        unique.append(num)
print("List without duplicates:", unique)

#Count frequency of characters in a string

string = input("Enter a string: ")
a = {}
for ch in string:
    if ch in a:
        a[ch] += 1
    else:
        a[ch] = 1
print(a)

#Multiplication table from 1 to 10

for i in range(1, 11):
    for j in range(1, 11):
        print(i * j, end="\t")
    print()
    
#Sum of all even numbers in a list

n = [1, 2, 3, 4, 5, 6]
sum_even = 0

for num in n:
    if num % 2 == 0:
        sum_even += num
print("Sum of even numbers:", sum_even)

#Square of each element in a list

n = [1, 2, 3, 4, 5]

for num in n:
    print(num ** 2)
    
#Common elements in two
    
a1 = [1, 2, 3, 4]
a2= [3, 4, 5, 6]
common = []
for num in a1:
    if num in a2:
        common.append(num)
print("Common elements:", common)

#Maximum and minimum values in a

numbers = [10, 25, 7, 45, 32]
max_val = min_val = numbers[0]
for num in numbers:
    if num > max_val:
        max_val = num
    if num < min_val:
        min_val = num
print("Maximum:", max_val)
print("Minimum:", min_val)

#Star pyramid pattern

n = int(input("Enter number of rows: "))
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))
    
#Star pyramid pattern

a=input("Enter a sentence: ")
n = a.split()
print("Number of words:", len(n))























