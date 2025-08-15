# Day 3 Advanced Practice Problem
# Task:
# Write a program that will:

# Ask the user to enter:

# Their full name

# A sentence

# A radius (number)

# Perform the following:

# Print the name in uppercase and lowercase

# Remove extra spaces from the name

# Replace all spaces in the sentence with -

# Show the sentence length (with and without spaces)

# Use abs(), round(), and pow() on a number from the user

# Calculate:

# Area of a circle using math.pi

# Square root of the area using math.sqrt()

# Print all results using f-strings
name=input("enter your full name: ")
print(name.strip())
str=input("sentence: ")
print("length with space", len(str))
strWitoutSpace = str.replace(" ","")
print(str.replace(" ",""))
print("length without space", len(strWitoutSpace))
radius=input("radius: ")
print(radius)
number=float(input("number:"))
print('absolute value of numbr is: ', abs(number))
number2=float(input("number2:"))
print('roundoff:',round(number2))
base=int(input('base:'))
power=int(input('power:'))
print('result:',pow(base,power))
import math
radius=4
area=math.pi*radius*radius
print('area is', area)
sqrt_area=math.sqrt(area)
print('squrtarea',sqrt_area)
