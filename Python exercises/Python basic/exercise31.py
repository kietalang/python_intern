# First way
# #Import math Library
# import math

# #find the  the greatest common divisor of the two integers
# print (math.gcd(3, 6))

def gcd(a, b):
    # if a = 0 => gcd(a,b) = b
    # if b = 0 => gcd(a,b) = a
    if (a == 0 or b == 0):
        return a + b

    while (a != b):
        if (a > b):
            a -= b # a = a - b
        else:
            b -= a
   
    return a # return a or b because a and b has the same values now


print(gcd(3, 6))