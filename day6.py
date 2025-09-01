# Lists

# Store 5 numbers in a list and print the largest and smallest.
# number=[]
# for i in range(5):
#     number.append(int(input('enter number:')))
# largest = number[0]
# smallest = number[0]

# for num in number:
#     if num > largest:
#         largest = num
#     if num < smallest:
#         smallest = num
# print('smallest:',smallest)
# print('largest:',largest)



# Write a program to calculate the sum of all elements in a list.
# numbers=[]
# for i in range(5):
#     numbers.append(int(input('enter number:')))
# total=0
# for i in range(len(numbers)):
#     total=total + numbers[i]
# print('total:',total)

# Write a program to remove duplicates from a list.
# numbers=[]
# for i in range(5):
#     numbers.append(int(input('enter number:')))
# withoutdupli=[]
# for i in range(len(numbers)):
#     if numbers[i]  not in withoutdupli:
#         withoutdupli.append(numbers[i])
# print('original list:',numbers)
# print('without duplicate:',withoutdupli)

# Take 2 lists of numbers and print their common elements.
# num1=[int(input('enter number:')) for i in range(10)]
# num2=[int(input('enter number:')) for i in range(10)]
# common = []

# for i in num1:
#     if i in num2 and i not in common:  # avoid duplicates
#         common.append(i)
# print("common:",common)



# Write a program to create a new list that contains only even numbers from the original list.
# num=[int(input('enter number:'))for i in range(10)]
# even=[]
# for i in range(len(num)):
#     if num[i] % 2 == 0 :
#         even.append(num[i])
# print('original:',num)
# print('even:',even)


# Loops

# Print the multiplication table of a given number.


# Write a program to find the sum of first 50 natural numbers using a for loop.
# total = 0

# for i in range(1, 51):   # loop from 1 to 50
#     total += i

# print("The sum of the first 50 natural numbers is:", total)

# Print all even numbers between 1 and 100 using a while loop.
# num = 2   

# while num <= 100:
#     print(num)
#     num += 2 

# Write a program to check if a number is prime (basic version).
number=int(input('enter number:'))
if  number > 1:
    for i in range(2,number):
        if number % i == 0:
            print('number is not:',number)
            break
    else:
        print('is prime number:',number)
else:
    print('is not prime number:',number)
    

# Count how many vowels are present in a given string.



# Write a function that takes a list and returns the first element.
# def first_element(my_list):
#      return my_list[0]
# number=[]
# for i in range(5):
#     number.append(int(input('enter number:')))
# print(first_element(number))


# Write a function that takes a list and returns the last element.

# Write a function that takes a number n and prints numbers from 1 to n.
# def print_numbers(n):
#     for i in range(1, n + 1):
#         print(i)
# print(print_numbers(6))


# Write a function that returns the square of a number.
# def square(num):
#     return num * num
# print(square(12))

# Write a function that returns the cube of a number.
def cube(number):
    return number * number * number
print(cube(36))

