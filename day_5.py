# Create a list of 4 colors and change the 2nd item.
color=['red','blue','green','orange']
color[2]='silver'
print(color[1])
print(color[-1])
# Print the last item using a negative index.
# Start with pets = ["cat", "dog"]

# Append "parrot", remove "cat", print final list and its length.
pets=["cat","dog"]
pets.append("parrot")
pets.remove("cat")
print(pets)
print(len(pets))

# Given letters = ['a','b','c','d','e','f']:
# Print ['b','c','d'] using slicing.
# Print every second letter.
# Print the list reversed.

letters=["a","b","c","d","e","f"]
print(letters[1:4])
print(letters[::2])
print(letters[::-1])


# 1) Store 5 fruits in a list and print them one by one
fruit=["apple","orange","dragonfruit","banana","pear"]
i=0
while i <len(fruit):
    print(fruit[i])
    i += 1

#   List cleaner
# Start with items = [" pen ", " book", "pencil ", " eraser "]
# Strip spaces from each item and print the cleaned list.
items=[" pen ", " book", "pencil ", " eraser "]
clean_item=[]
for i in items:
    clean_item.append(i.strip())
print(clean_item)

# lice sampler
# Given nums = [1,2,3,4,5,6,7,8,9]
# Print:
# Middle three numbers
# All odd positions
# Reversed except the first and last

num=[1,2,3,4,5,6,7,8,9]
print(num[4:7])
print(num[::2])
num.remove(1)
num.remove(9)
print(num[::-1])

# Inventory helper
# Start with inv = []
# Append 3 items from the user (input)
# Remove one item (only if it exists), then print final list + count.

# inv=[]
# for i in range(5):
#     inv.append(input('enter inv:'))
# remove=input('remove inv:')
# if remove in inv:
#     inv.remove(remove)
# print('final inv:',inv,"count:",len(inv))



# Beginner Function Questions in Python
# Write a function that takes your name as input and prints a greeting.

# def greet(name):
#     print("how are you ",name)


# greet('zunaid')
# name=input('enter your name:')
# greet(name)
# # Write a function that takes two numbers and returns their sum.
# def sum(a,b):
#     return a + b
# result=sum(10,20)
# print(result)

# # Write a function that takes two numbers and returns their product.
# def product(a,b):
#     return a * b
# pro=product(20,11)
# print(pro)
# # Write a function that checks if a number is even or odd.
# def check(a):
#     if a % 2 == 0:
#         return "even"
#     else:
#         return "odd"
# print(check(10))
    
# # Write a function that takes a string and prints it in uppercase.
# def str(sentence):
#     return sentence.upper()
# sentence=input('enter your sentence:')
# print(str(sentence))

# # Write a function that returns the length of a list.
# def list_length(list):
#     return len(list)
# list=[]
# for i in range(3):
#     list.append(input('enter list:'))
# print(list_length(list))

# Write a function that takes a list of numbers and returns the largest number.
# def find_number(number):
#     largest=number[0]
#     for i in range(len(number)):
#         if number[i]  > largest:
#             largest = number[i]
#     return largest
# number=[]
# for i in range(5):
#     number.append(int(input('enter number:')))
# print("the largest number:",find_number(number))

# Write a function that takes a list of numbers and returns the smallest number.
# def small_number(number):
#     smallest=number[0]
#     for i in range(len(number)):
#         if number[i] <smallest:
#              smallest=number[i]
#     return smallest
# number=[]
# for i in range(5):
#     number.append(int(input('enter number')))
# print('smallest number:',small_number(number))

# Write a function that counts how many times the letter "a" appears in a word.
def count_a(word):
    count=0
    for i in range(len(word)):
        if word[i] == "a":
            count += 1
    return count
word=input('enter a word:')
print('count:',count_a(word))

