# Practice Set 1 – Name & Age Formatter
# Ask for:

# First name and last name

# Age (integer)

# Join names into one string, print in uppercase & lowercase

# Show total character count (excluding spaces)

# Calculate birth year (assuming current year = 2025)

# Print using f-strings

first_name=input('first name:')
print('first name is' ,first_name)
last_name=input('last name:')
print('last name is ',last_name)
result= first_name + ' ' + last_name
print('full name is: ', result)
count=len(result)
print(count)
age=int(input('age:'))
current_year = 2025
birth_year=current_year-age
print('birth year is:',birth_year)


# Practice Set 2 – Sentence Analyzer
# Ask the user for:

# A sentence

# Remove extra spaces (.strip())

# Replace spaces with hyphens

# Count total characters with and without spaces

# Convert to uppercase and lowercase

# Print results with f-strings

sentence=input('sentence:')
print('sentence:',sentence.upper())
count=len(sentence)
print(count)
print('char lenth without space', len(sentence.replace(' ', '')))

# Practice Set 3 – Number Magic
# Ask for:

# One positive number and one negative number

# Show:

# Absolute value of each

# Rounded values (2 decimal places)

# Each number raised to the power of 3

# Print results with f-strings

positive_num=int(input('number:'))
print('positive:',pow(3,positive_num))
negative_num=float(input('number:'))
print('negative:',pow(3,negative_num* -1))


# Practice Set 4 – Rectangle Geometry
# Ask for:
# Length and width
# Calculate:
# Area & perimeter
# Square root of the area (math.sqrt())
# Print all rounded to 2 decimal places

length=float(input('length:'))
print('lenth:',round(length,2))
width=float(input('width:'))
print('width:',round(width,2))
area=length*width
print('area:',round(area,2))
import math
result=math.sqrt(area)
print(result)
perimeter=int(2 * (length+width))
print('perimeter:',perimeter) 

# Practice Set 5 – Circle Geometry
# Ask for:
# Radius
# Calculate:
# Area (math.pi * r ** 2)
# Circumference (2 * math.pi * r)
# Square root of the area
# Print all results rounded to 2 decimal places

import math 
radius=int(input('radius:'))
print('radius:',radius)
area=math.pi * radius ** 2
print('area:',round(area,2))
circumference= 2 *math.pi * radius
print('circum:',round(circumference,2))
squrt_area=math.sqrt(area)
print('sqrtarea:',round(squrt_area))

# Practice Set 6 – BMI Calculator
# Ask for:
# Height in meters (float)
# Weight in kg (float)
# Calculate BMI = weight / (height ** 2)
# Round BMI to 2 decimal places
# Print:
# BMI value
# Health category:
# < 18.5: Underweight
# 18.5–24.9: Normal
# 25–29.9: Overweight
# ≥ 30: Obese

height=float(input('height:'))
weight=float(input('weight:'))
calculated_BMI=weight / (height ** 2)
print('BMI:',round(calculated_BMI,2))
 # comparison mathematical type equetion
# a > b 
# a < b 
# a == b 
# a >= b 
# a <= b
if calculated_BMI < 18.5:
    print('underweight')
    #perform task1
    #perform task2
    #perform task3'= 
if calculated_BMI > 18.5 and calculated_BMI < 24.9:
    print('normal')
if calculated_BMI > 25 and calculated_BMI <29.9:
   print('overweight')
if calculated_BMI >= 30:
 print('obese')

# Practice Set 7 – Travel Cost Calculator
# Ask for:
# Distance in km
# Fuel efficiency (km per liter)
# Fuel price per liter
# Calculate:
# Total liters needed
# Total cost
# Print results using f-strings and rounding

total_distance=int(input('distance:'))
fuel_efficiency=int(input('km per litre:'))
fuel_price_liter=int(input('price/liter:'))
total_liter_needed= total_distance / fuel_efficiency
print('total_liter_needed;',total_liter_needed)
total_cost=total_liter_needed * (fuel_price_liter)
print('total_cost:',total_cost)


# Practice Set 8 – Temperature Converter
# Ask for:
# Temperature in Celsius
# Convert to:
# Fahrenheit → (C * 9/5) + 32
# Kelvin → C + 273.15
# Print all results rounded to 2 decimal places

temperature_celsius=float(input('temp_celsius'))
fahrenhiet=(temperature_celsius *9/5) + 32
print('fahrenhiet:',fahrenhiet)
kelvin=temperature_celsius + 273.15
print('kelvin;',kelvin)


# Practice Set 9 – Shopping Bill
# Ask for:
# Price of 3 items
# Calculate:
# Total cost
# Average price
# Total with 18% tax
# Print results with f-strings

price_of_1st=float(input('price of 1st:'))
price_of_2nd=float(input('price of 2nd:'))
price_of_3rd=float(input('price of 3rd:'))
total_cost=price_of_1st + price_of_2nd + price_of_3rd
print('total cost:',total_cost)
average_price=(price_of_1st + price_of_2nd + price_of_3rd) / 3
print('average price:',average_price)
tax_rate=18/100
final_price=total_cost * (1 + tax_rate)
print(final_price)


# Practice Set 10 – Time Converter
# Ask for:
# Time in minutes
# Convert to:
# Hours
# Seconds
# Print results with f-string
time_in_min=int(input('time in min:'))
convert_to_hour=time_in_min / 60
print('convert_to_hour:',convert_to_hour)
convert_to_sec=time_in_min * 60
print('convert_to_sec:',convert_to_sec)