import math
x1 = float(input("Enter the first x coordinate: "))
y1 = float(input("Enter the first y coordinate: "))
x2 = float(input("Enter the second x coordinate: "))
y2 = float(input("Enter the second y coordinate: "))

distance = math.sqrt (pow(x2 - x1, 2) + pow(y2 - y1, 2))

print ("The distance between the two points is:", f"{distance:.2f}")


"""
Relfection:

Using a library is more practical in terms of eficiency and convinience rather than writing all formulas down. At the same time, there are also lots and lots of formulas in which writing them down would take hours. Take \"import\" for example, there are a lot of code that continues after it like import math, import time, import sys, and many more.

"""