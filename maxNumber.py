#This is the naive approach where we will compare two numbers using if-else statement and will print the output accordingly.
# Python program to find the
# maximum of two numbers


def maximum(a, b):
    if a >= b:
        return a
    else:
        return b


# Driver code
a = 2
b = 4
print(maximum(a, b))


#This function is used to find the maximum of the values passed as its arguments.
# Python program to find the
# maximum of two numbers


a = 2
b = 4

maximum = max(a, b)
print(maximum)

#This operator is also known as conditional expression are operators that evaluate something based on a condition being true or false. It simply allows testing a condition in a single line
# Python program to find the
# maximum of two numbers

# Driver code
a = 2
b = 4

# Use of ternary operator
print(a if a >= b else b)

# This code is contributed by AnkThon

#Method: Using lambda function
# python code to find maximum of two numbers

a=2;b=4
maximum = lambda a,b:a if a > b else b
print(f'{maximum(a,b)} is a maximum number')

#Method : Using sort() method

# Python program to find the
# maximum of two numbers
a = 2
b = 4
x=[a,b]
x.sort()
print(x[-1])