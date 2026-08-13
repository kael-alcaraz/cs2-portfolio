import math
x1 = float(input("Please input x1: "))
x2 = float(input("Please input x2: "))
y1 = float(input("Please input y1: "))
y2 = float(input("Please input y2: "))
dist = math.sqrt(pow(x2-x1, 2) + pow(y1-y2, 2))
print(f"The distance between the two points is: {dist:.2f}.")
# Reflection
# The math library helped simplify my program by providing me with the sqrt function, providing me with an easy way to solve for the Euclidean distance formula.
# I would have needed to use power functions and a 0.5 on top such as pow() or **, which takes longer to write, and is more inefficient.
# We have tools, and so we should use them for their intended purpose, so that is why libraries are more practical.
