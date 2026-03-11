#Print numbers from 1 to 10 using a for loop

for i in range(1, 11):
    print(i)

#Print even numbers from 1 to 50

for i in range(1, 51):
    if i % 2 == 0:
        print(i)

#Print odd numbers from 1 to 50

for i in range(1, 51):
    if i % 2 != 0:
        print(i)

#Find the sum of numbers from 1 to 100

total = 0
for i in range(1, 101):
    total += i
print("Sum:", total)

#Print multiplication table of a number

a = int(input("Enter a number: "))

for i in range(1, 11):
    print(a, "x", i, "=", a * i)

#Count numbers in a list

n = [10, 20, 30, 40, 50]
count = 0

for num in n:
    count += 1

print("Total numbers:", count)

#Print all elements in a list using a for loop


n = [10, 20, 30, 40, 50]

for num in n:
    print(n)

#Count vowels in a string

string = input("Enter a string: ")
vowels = "aeiouAEIOU"
count = 0

for char in string:
    if char in vowels:
        count += 1

print("Number of vowels:", count)

#Print numbers in reverse order from 10 to 1

for i in range(10, 0, -1):
    print(i)

#Find factorial of a number using for loop

num = int(input("Enter a number: "))
factorial = 1

for i in range(1, num + 1):
    factorial *= i

print("Factorial:", factorial)

#Find the largest number in a list

a = [10, 45, 23, 89, 12]
largest = a[0]

for num in a:
    if num > largest:
        largest = num

print("Largest number:", largest)

#Count the number of digits in a number

a =int(input("Enter a number: "))
count = 0

while a != 0:
    a //= 10
    count += 1

print("Number of digits:", count)

#Print square of numbers from 1 to 10

for i in range(1, 11):
    print(i, "square is", i * i)

#Print cube of numbers from 1 to 10
    
for i in range(1, 11):
    print(i, "cube is", i * i * i)

#Find sum of elements in a list

numbers = [10, 20, 30, 40, 50]
total = 0

for num in numbers:
    total += num

print("Sum of elements:", total)

       #--- END ---#
















