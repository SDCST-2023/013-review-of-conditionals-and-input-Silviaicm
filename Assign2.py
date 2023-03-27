"""
Write a program that does the following:
Asks the user to enter in 2 numbers that can be float values
Ask the user if one of the numbers is the hypotenuse of a right triangle
Calculates the length of the missing side and rounds it to 1 decimal place.
"""
import math 

print("Input lengths of shorter triangle sides:")
a = float(input("a: "))
b = float(input("b: "))
d=input("Is one of the values the hypotenous?")
if d=="yes" and a>b:
    c=(a**2 - b**2)**(1/2)
if d=="yes" and b>a:
    c=(b**2 - a**2)**(1/2)
else:
    c = (a**2 + b**2)**(1/2)
print("The length of the hypotenuse is:", round(c,1))


