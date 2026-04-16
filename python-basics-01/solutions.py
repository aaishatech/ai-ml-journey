# Q1. Write a program that asks the user for their name and age, then prints a sentence like:
# Hello Shardha, you are 21 year old!

# name = input("Enter name: ")
# age =  int(input("Enter age: "))

# print("Hello", name, ", You are", age, " years old!")


# Q2. Take two number as input from the user and print their sum, diffrence, product and quotient.

# a = int(input("Enter number 1: "))
# b = int(input("Enter number 2: ")) 

# sum = a + b
# difference = a - b
# product = a * b
# quotient = a / b

# print("Sum is = ",sum)
# print("Difference is = ", difference)
# print("Product is = ", product)
# print("Quotient is = ", quotient)

# Q3. Ask the user two integers and one float. Convert them all to floats and print their average

# first_int_val = float(input("Enter int value: "))
# second_int_val = float(input("Enter int value: "))

# float_val = float(input("Enter float value: "))

# avg = (first_int_val + second_int_val +float_val) / 3

# print("The avg is : ",avg)

# why - first and second value will be eneterd as int it automatically converts into float as question says.


# Q4. The user enters a string containing a number (e.g., "45"). Convert it to:
# an integer
# a float 
# a string again

# Print all three values with their types.

# val = input("Enter value '45' : ")


# int_val = int(val)
# float_val = float(val)
# str_val = str(val)

# print("Should be INT = ",int_val," | ",type(int_val))
# print("Should be FLOAT = ",float_val," | ",type(float_val))
# print("Should be STRING = ",str_val," | ",type(str_val))


# Q5. Evaluate and print the result of the following expression"
#  x = 10 + 3 * 2 ** 2

# x = 10 + 3 * 2 ** 2
# print(x)

# Why - Coz, first exponent 2 ** 2 will solve,  will become 4 and the exp will be 10 + 3 * 4 and then multiply 10 + 12 = 22 ans.


# Q6. Write the program to swap of two numbers enternd by user.
# a = int(input("Enter val a: "))  #5
# b = int(input("Enter val b: "))  #10

# temp = a
# a = b
# b = temp

# print("The val of a is = ", a)
# print("The val of b is = ", b)


# Q7. Ask the user a temperature in Celsius (string input). Convert it to float, then calculate and print temperature in Fahrenheit.
# Conversion fornula : FahrenheitTemp = (CelsiusTemp * (9/5)) + 32

# celsius = input("Enter temperature in Celsius: ")
# celsius = float(celsius)
# fahrenheit = (celsius * (9 / 5) + 32)
# print("Temperature in Fahrenheit: ", fahrenheit)


# Q8. Take the radius (r) as user input and print the area.
# Use the formula : Area = PI * r^2 (value of PI = 3.14)

# radius = float(input("Enter radius: "))
# PI = 3.14
# area = PI * radius * radius
# print("The area is = ",area)

# Q10. Take a decimal number as input (like 45.78) and ouput its:
# integer part - 45
# fractional part - .78

# number = float(input("Enter deciaml number: "))
# integer = int(number)
# fractional = number - integer

# print("The integer part is = ",integer, ", and The fractional part is =",fractional)
