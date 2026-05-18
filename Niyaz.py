# 1. Print Numbers from 1 to 20 Using While Loop
i = 1
while i <= 20:
    print(i)
    i += 1


# 2. Print Numbers from 1 to 20 Using For Loop
for i in range(1, 21):
    print(i)


# 3. Print All Even Numbers Between 1 to 50
for i in range(1, 51):
    if i % 2 == 0:
        print(i)


# 4. Print All Odd Numbers Between 1 to 50
for i in range(1, 51):
    if i % 2 != 0:
        print(i)


# 5. Print Numbers from 30 to 1 in Reverse Order
for i in range(30, 0, -1):
    print(i)


# 6. Print Your Name 10 Times Using Loop
for i in range(10):
    print("Your Name")


# 7. Print All Numbers Divisible by 3 from 1 to 100
for i in range(1, 101):
    if i % 3 == 0:
        print(i)


# 8. Print All Numbers Divisible by 5 and 7 from 1 to 100
for i in range(1, 101):
    if i % 5 == 0 and i % 7 == 0:
        print(i)


# 9. Find the Sum of Numbers from 1 to 50
total = 0
for i in range(1, 51):
    total += i
print("Sum =", total)


# 10. Find the Sum of Even Numbers from 1 to 100
total = 0
for i in range(1, 101):
    if i % 2 == 0:
        total += i
print("Sum of even numbers =", total)


# 11. Multiplication Table of 7
for i in range(1, 11):
    print("7 x", i, "=", 7 * i)


# 12. Multiplication Table of Any Number
number = int(input("Enter a number: "))
for i in range(1, 11):
    print(number, "x", i, "=", number * i)


# 13. Count How Many Even Numbers Are There Between 1 and 200
count = 0
for i in range(1, 201):
    if i % 2 == 0:
        count += 1
print("Total even numbers =", count)


# 14. Count How Many Odd Numbers Are There Between 1 and 200
count = 0
for i in range(1, 201):
    if i % 2 != 0:
        count += 1
print("Total odd numbers =", count)


# 15. Find Factorial of a Number Using Loop
number = int(input("Enter a number: "))
factorial = 1
for i in range(1, number + 1):
    factorial *= i
print("Factorial =", factorial)


# 16. Reverse a Given Number
number = int(input("Enter a number: "))
reverse = 0
while number > 0:
    digit = number % 10
    reverse = reverse * 10 + digit
    number = number // 10
print("Reversed number =", reverse)


# 17. Find Sum of Digits of a Number
number = int(input("Enter a number: "))
total = 0
while number > 0:
    digit = number % 10
    total += digit
    number = number // 10
print("Sum of digits =", total)


# 18. Count Total Number of Digits in a Number
number = int(input("Enter a number: "))
count = 0
if number == 0:
    count = 1
else:
    while number > 0:
        count += 1
        number = number // 10
print("Total digits =", count)


# 19. Print Square of Numbers from 1 to 15
for i in range(1, 16):
    print("Square of", i, "=", i * i)


# 20. Print Cube of Numbers from 1 to 12
for i in range(1, 13):
    print("Cube of", i, "=", i * i * i)


# 21. Check Whether a Number Is Positive, Negative, or Zero
number = int(input("Enter a number: "))
if number > 0:
    print("Positive number")
elif number < 0:
    print("Negative number")
else:
    print("Zero")


# 22. Check If a Number Is Even or Odd
number = int(input("Enter a number: "))
if number % 2 == 0:
    print("Even number")
else:
    print("Odd number")


# 23. Find the Largest Number Among Three Numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
if a >= b and a >= c:
    print("Largest number =", a)
elif b >= a and b >= c:
    print("Largest number =", b)
else:
    print("Largest number =", c)


# 24. Check If a Year Is Leap Year or Not
year = int(input("Enter a year: "))
if year % 400 == 0:
    print("Leap year")
elif year % 4 == 0 and year % 100 != 0:
    print("Leap year")
else:
    print("Not a leap year")


# 25. Print All Vowels from a Given String
text = input("Enter a string: ")
for char in text:
    if char.lower() in "aeiou":
        print(char)


# 26. Count Vowels and Consonants in a String
text = input("Enter a string: ")
vowels = 0
consonants = 0
for char in text:
    if char.isalpha():
        if char.lower() in "aeiou":
            vowels += 1
        else:
            consonants += 1
print("Vowels =", vowels)
print("Consonants =", consonants)


# 27. Print Characters of a String One by One Using Loop
text = input("Enter a string: ")
for char in text:
    print(char)


# 28. Reverse a String Using Loop Without Slicing
text = input("Enter a string: ")
reverse = ""
for char in text:
    reverse = char + reverse
print("Reversed string =", reverse)


# 29. Find the Largest Number from a List of 10 Numbers
numbers = []
for i in range(10):
    num = int(input("Enter a number: "))
    numbers.append(num)
largest = numbers[0]
for num in numbers:
    if num > largest:
        largest = num
print("Largest number =", largest)


# 30. Find the Smallest Number from a List of 10 Numbers
numbers = []
for i in range(10):
    num = int(input("Enter a number: "))
    numbers.append(num)
smallest = numbers[0]
for num in numbers:
    if num < smallest:
        smallest = num
print("Smallest number =", smallest)


# 31. Print Star Pattern
rows = [1, 2, 1, 2, 3]
for i in rows:
    print("*" * i)


# 32. Print Reverse Star Pattern
rows = [3, 2, 1, 2, 1]
for i in rows:
    print("*" * i)


# 33. Print Number Pattern
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end="")
    print()


# 34. Print Repeated Number Pattern
for i in range(5, 0, -1):
    for j in range(i):
        print(i, end=" ")
    print()


# 35. Create a List of 10 Numbers and Print Sum and Average
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
total = 0
for num in numbers:
    total += num
average = total / len(numbers)
print("Sum =", total)
print("Average =", average)


# 36. Count How Many Numbers Are Greater Than 50 in a List
numbers = [12, 65, 78, 34, 90, 45, 51, 20, 88, 49]
count = 0
for num in numbers:
    if num > 50:
        count += 1
print("Numbers greater than 50 =", count)


# 37. Take 5 Student Names and Marks, Then Print Average Marks
total_marks = 0
for i in range(5):
    name = input("Enter student name: ")
    marks = float(input("Enter marks: "))
    total_marks += marks
average = total_marks / 5
print("Average marks =", average)


# 38. Create a Dictionary of 5 Students and Print All Names and Marks
students = {
    "Rahim": 85,
    "Karim": 78,
    "Nadia": 92,
    "Sadia": 88,
    "Hasan": 81
}
for name, marks in students.items():
    print(name, ":", marks)


# 39. Take a Sentence and Count How Many Words Are There
sentence = input("Enter a sentence: ")
words = sentence.split()
print("Total words =", len(words))


# 40. Create Separate Even and Odd Number Lists
numbers = [10, 15, 22, 33, 40, 51, 62, 73, 84, 95]
even_numbers = []
odd_numbers = []
for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)
    else:
        odd_numbers.append(num)
print("Even numbers =", even_numbers)
print("Odd numbers =", odd_numbers)