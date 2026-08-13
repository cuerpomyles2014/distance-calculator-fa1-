# Makes it so that it can import math related code (e.g. sqrt) which makes it able to use it.
import math

# Asks the user for the first x coordinate.
x1 = float(input("Enter the first x coordinate: "))

# Asks the user for the first y coordinate.
y1 = float(input("Enter the first y coordinate: "))

# Asks the user for the second x coordinate.
x2 = float(input("Enter the second x coordinate: "))

# Asks the user for the second y coordinate.
y2 = float(input("Enter the second y coordinate: "))

# Calculates the distance using the imported math code and the coordinates given. 
distance = math.sqrt (pow(x2 - x1, 2) + pow(y2 - y1, 2))

# Prints the calculated distance
print ("The distance between the two points is:", f"{distance:.2f}")


"""
Relfection:

Using a library is more practical in terms of eficiency and convinience rather than writing all formulas down. At the same time, there are also lots and lots of formulas in which writing them down would take hours. Take \"import\" for example, there are a lot of code that continues after it like import math, import time, import sys, and many more.

"""
