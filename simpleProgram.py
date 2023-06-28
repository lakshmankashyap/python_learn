import operator

# Add Two numbers
num1 = 1
num2 = 2

# Adding two numbers
sum = num1 + num2

# Printing Value
print(f"Sum of {num1} and {num2} is {sum}")

# Adding two numbers with user input
numb1 = input("First Number: ")
numb2 = input("Second Number: ")

#Adding two numbers
# User might also enter float numbers
sumIn = float(numb1) + float(numb2)

# Display the sum
# will print value in float
print("The sum of {0} and {1} is {2}".format(numb1, numb2, sumIn))

txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49))

txt1 = "My name is {fname}, I'm {age}".format(fname = "John", age = 36)
txt2 = "My name is {0}, I'm {1}".format("John",36)
txt3 = "My name is {}, I'm {}".format("John",36)

# To define a function that take two integers
# Defining add function and returning the result
# and return the sum of those two numbers
def add(a, b):
    return a+b

#initializing the variables
numbe1 = 10
numbe2 = 5

#function calling and store the result into sum_of_twonumbers
sum_of_twonumbers = add(numbe1, numbe2)

#To print the result
print("Sum of {0} and {1} is {2};" .format(numbe1, numbe2, sum_of_twonumbers))

#Add two numbers in Python using operator.add() method
# Python3 program to add two numbers

numbem1 = 15
numbem2 = 12

# Adding two nos

su = operator.add(numbem1, numbem2)

# printing values
print("Sum of {0} and {1} is {2}" .format(numbem1, numbem2, su))

#Adding two number using lambda function
# Define a lambda function to add two numbers
#A lambda function is a small anonymous function.
#A lambda function can take any number of arguments, but can only have one expression.


add_numbers = lambda x, y: x + y

# Take input from the user
num1 = 1
num2 = 2

# Call the lambda function to add the two numbers
result = add_numbers(num1, num2)

# Print the result
print("The sum of", num1, "and", num2, "is", result)



