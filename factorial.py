def factorial(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return n*factorial(n-1)


result = factorial(3)
result1 = factorial(4)
result2 = factorial(5)
print(f"The factorial of 3 is {result}")
print(f"The factorial of 4 is, {result1}")
print(f"The factorial of 5 is {result2}")


# Python 3 program to find
# factorial of given number
def factorial(n):
    if n < 0:
        return 0
    elif n == 0 or n == 1:
        return 1
    else:
        fact = 1
        while (n > 1):
            fact *= n
            n -= 1
        return fact


# Driver Code
num = 5
print("Factorial of", num, "is",
      factorial(num))


# Python 3 program to find
# factorial of given number

# Function to find factorial of given number
def factorial(n):
    res = 1

    for i in range(2, n + 1):
        res *= i
    return res


# Driver Code
num = 5
print("Factorial of", num, "is",
      factorial(num))


# Python 3 program to find
# factorial of given number

def factorial(n):
    # single line to find factorial
    return 1 if (n == 1 or n == 0) else n * factorial(n - 1)


# Driver Code
num = 5
print("Factorial of", num, "is",
      factorial(num))

# This code is contributed