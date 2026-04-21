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
# [HINT: The right most digit of a number N is N % 10
#  and to remove the right most digit froma number, we can do N = N / 10]

# def print_digit(n):
    
#     while(n > 0):
#         last_digit = n % 10 
#         print(last_digit)
#         n = n // 10

# print_digit(312)


# Q4. Write a functionn that return the count the number of digit in a number, n.
# Q5. Write a function to return the sum of digits of a number n.
# Q6. Write a program to print all numbers from 1 to 100 that are divisible by both 3 and 5.
# Q7. Design a program to continuously inpyt the number n from the user & print if it is positive or negative until user enters "Quit".
# Q8. Let's create a simple calculator that performs airthmetic operations. Create a function calculator(a, b, operations) that performs addition, subtraction, multiplication, or division based on the operation parameter.
# [operation parameter can have values '+' , '-' , '*' , & '/']
# Q9. Write a function is_prime(n) that returns True if n is a prime number and False otherwise, using a loop.
# [HINT - 1. We only check the prime for 2 or numbers greater than 2.]
