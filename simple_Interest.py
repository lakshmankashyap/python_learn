'''
    EXAMPLE1:
    Input : P = 10000
            R = 5
            T = 5
    Output :2500.0
    We need to find simple interest on
    Rs. 10,000 at the rate of 5% for 5
    units of time.

    EXAMPLE2:
    Input : P = 3000
            R = 7
            T = 1
    Output :210.0
'''


# Python3 program to find simple interest
# for given principal amount, time and
# rate of interest.


def simple_interest(p, t, r):
    print('The principal is', p)
    print('The time period is', t)
    print('The rate of interest is', r)

    si = (p * t * r) / 100

    print('The Simple Interest is', si)
    return si


# Driver code
simple_interest(8, 6, 8)


#Method: Taking input from user.


def simple_interest(p, t, r):
    print('The principal is', p)
    print('The time period is', t)
    print('The rate of interest is', r)

    si = (p * t * r) / 100

    print('The Simple Interest is', si)


# Driver code
P = int(input("Enter the principal amount :"))
T = int(input("Enter the time period :"))
R = int(input("Enter the rate of interest :"))
simple_interest(P, T, R)