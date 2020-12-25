# First way
# #Import math Library
# import math

# find the greatest common divisor of the two integers

def gcd(a, b):
    # if a = 0 => gcd(a,b) = b or reverse
    if (a == 0 or b == 0):
        return a + b

    while (a != b):
        if (a > b):
            a -= b
        else:
            b -= a
   
    return a # return a or b because a and b has the same values now

# find the least common multiple
def lcm(a, b):
    return int((a / gcd(a, b)) * b)


print(gcd(3, 6))
print(lcm(3, 6))