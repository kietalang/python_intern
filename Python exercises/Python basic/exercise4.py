# Python program which accepts the radius of a circle from the user and compute the area
# import the pi class from the math module
from math import pi

r = float(input ("Input radius: "))
area = pi * r**2

print("r = " + str(r))
print ("Area = " + str(area))

