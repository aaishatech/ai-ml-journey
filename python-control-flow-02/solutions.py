# Q1. Write a program that takes salary as input. Using conditional statements, calculate the final tax rate based on these rules:
# If salary < 30,000 -> 5%
# If salary is 30,000 - 70,000 -> 15%
# If salary > 70,000 -> 25%

# salary = float(input("Enter salary: "))

# if(salary < 30000):
#     tax_rate = 0.05

# elif(salary >= 30000 and salary <= 70000):
#     tax_rate = 0.15

# else:
#     tax_rate = 0.25 

# tax = salary * tax_rate
# print("Tax rate:", tax_rate * 100, "%")    
# print("Tax amount:", tax)



# Q2. Write a function that takes two integers a and b and prints all even numbers between them(inclusive).

# def all_even(a, b):
#     for i in range(a, b + 1):
#         if(i % 2 == 0):
#             print(i)

# all_even(1, 10)


# Q3. Write a function that prints the digits of a number, n.
# For eg: n = 312, there are 3 digits in it 3, 1, and 2 & we need to print them.
# But as a beginner - it will 2, 1, 3 as methods are not cover
# [HINT: The right most digit of a number N is N % 10
#  and to remove the right most digit froma number, we can do N = N / 10]

# def print_digit(n):
    
#     while(n > 0):
#         last_digit = n % 10 
#         print(last_digit)
#         n = n // 10

# print_digit(312)


# Q4. Write a functionn that return the count the number of digit in a number, n.

# def count_digit(n):
#     count = 0
#     while(n > 0):
#         last_digit = n % 10 
#         count += 1
#         n = n // 10
#     print("The total digits are: ",count)

# count_digit(312)


# Q5. Write a function to return the sum of digits of a number n.

# def sum_digit(n):
#     total_sum = 0
#     while(n > 0):
#         last_digit = n % 10 
#         total_sum += last_digit
#         n = n // 10
#     print("The sum of digits are: ", total_sum)

# sum_digit(312)


# Q6. Write a program to print all numbers from 1 to 100 that are divisible by both 3 and 5.
# if( i % 15 == 0) alternate of if( (i % 3 == 0) and (i % 5 == 0)):


# def num(n):
#     for i in range(1, n + 1):
#         if( (i % 3 == 0) and (i % 5 == 0)):  
#             print(i)

# num(100)



# Q7. Design a program to continuously input the number n from the user & print if it is positive or negative until user enters "Quit".

# while True:
#      num = input("Enter num or ('quit'): ")
#      if(num == 'quit'):
#           break

#      num = int(num)

#      if(num > 0):
#           print("Positive number =", num)
#      elif(num < 0):
#           print("Negative number = ", num)
#      else:
#           print("ZERO")


# Q8. Let's create a simple calculator that performs airthmetic operations. Create a function calculator(a, b, operations) that performs addition, subtraction, multiplication, or division based on the operation parameter.
# [operation parameter can have values '+' , '-' , '*' , & '/']
#float value return ['/']

# def calculator(a, b, operation):

#     if(operation == '+'):
#         print("The addition is =",a + b)

#     elif(operation == '-'):
#         print("The subtraction is =",a - b)

#     elif(operation == '*'):
#         print("The multiplication is =",a * b)

#     elif(operation == '/'): 
#         if(b == 0):
#             print("Cannot divide by zero")
#         else:
#             print("The division is =",a / b)  

#     else:
#         print("Invalid Operator")

# calculator(10, 5, '+')



# Q9. Write a function is_prime(n) that returns True if n is a prime number and False otherwise, using a loop.

# [HINT - 

# 1. We only check the prime for 2 or numbers greater than 2.

# A  non-prime number, n, will always get divided by atleast one number in range [2, n-1].

# Eg - For number 9 weʼll check in range (2, 8) & itʼll get divided by 3. So  is 9 is non-prime & weʼll return false for it.

# For number 7 weʼll check in range (2, 6) & it wonʼt get divided by any. So 7 is prime & weʼll return true for it. ]


# num = int(input("Enter number: "))

# def is_prime(n):
#     if n <= 1:
#         return False
    
#     if n == 2 :
#         return True
    
#     for i in range(2 , n):
#         if n % i == 0:
#             return False

#     return True 
        
# print(is_prime(num))




# Q10. Letʼs create a “Number Guessing Game”.  Given a secret number (already decided by you), write a program that asks the user to guess it and prints:
 
# "Too high" if the guess is above the number
# "Too low" if the guess is below
# "Correct!" if the guess matche

# def guess_game(num):
#     while True:
#         guessNum = input("Enter number or 'quit': ")

#         if (guessNum == 'quit'):
#             break
        
#         guessNum = int(guessNum)

#         if(guessNum > num):
#             print("Too High")

#         elif(guessNum < num):
#             print("Too Low")

#         else:
#             print("correct = ", num)
#             break

# guess_game(60)