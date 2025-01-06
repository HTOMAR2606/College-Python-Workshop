import math
a=int(input("Enter the value of first side of triangle:"))
b=int(input("Enter the value of second side of triangle:"))
c=int(input("Enter the value of third side of triangle:"))

s=(a+b+c)/2
area= math.sqrt(s*(s-a)*(s-b)*(s-c))
print("Area of the triangle is:",area)