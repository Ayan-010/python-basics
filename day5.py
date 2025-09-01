# 🔹 String Questions (1–10)

# Count how many vowels are in a string.
# word=input('enter a word:')
# count=0
# for i in range(len(word)):
#     char=word[i]
#     if char == 'a' or char == 'e' or char == 'i' or char == 'u' or char == 'o':
#      count=count + 1
# print('vowel_count:', count)

# Count how many consonants are in a string.
# txt=input('enter a word:')
# count=0
# for i in range(len(txt)):
#     char=txt[i]
#     if char != 'a' and  char != 'e' and  char != 'i' and  char != 'u' and char != 'o':
#         count=count + 1
#         print('count:',count,"char:",char)
# print('consonant_count:', count)



# Reverse a string using a for loop.
# text=input('enter a word:')
# reverse=''
# count=len(text)
# for i in range(len(text)):
#      reverse=reverse + text[count - i - 1]
# print('reverse word:',reverse)
     


# Check if a string is a palindrome.
# text=input('enter a word:')
# reverse=''
# count=len(text)
# for i in range(len(text)):
#      reverse=reverse + text[count - i - 1]
# print('reverse word:',reverse)

# flag=True
# for i in range(len(text)):
#      if text[i] != reverse[i]:
#           flag=True
#           print('is not palindrum:')
#           break
# else:
#      print('is palindrum:')
          


# Count how many times a character 'a' appears in a string.
# word=input('enter a word:')
# count=0
# for i in range(len(word)):
#     char=word[i]
#     if char == 'a':
#         count=count + 1
# print('number of a:',count)


# Remove all spaces from a string.
# word=input('enter a word:')
# word_withoutspace=word.replace('','_')
# print('withoutspace:',word_withoutspace)


# Find the first repeating character in a string.


# Convert all lowercase letters to uppercase (without using .upper()).



# Print all characters of a string except vowels.
# word=input("enter a word:")
# for i in range(len(word)):
#     char=word[i]
#     if char != 'a' and char != 'e' and char != 'i' and char != 'o' and char !='u':
        
#         print('consonant:',char)


# Print the index of the first occurrence of a character (like 'e') in a string.
# word=input('enter a word:')
# char=input('search for letter:')
# for i in range(len(word)):
#     if word[i] == char:
#         print('index is:',i)
#     else:
#      print('not found:')



#  Array (List) Questions (11–20)

# Find the maximum number in a list.
# number=[int(input('enter number:')) for i in range(10)]
# largest_number=number[0]
# for i in range(len(number)):
#     if number[i] > largest_number :
#         largest_number=number[i]
# print('largest num :',largest_number)


# Find the minimum number in a list.
# number=[int(input('enter a number:')) for i  in range(5)]
# smallest_num=number[0]
# for i in range(len(number)):
#     if number[i] < smallest_num:
#         smallest_num=number[i]
# print('smallet number:',smallest_num)






# Count how many even numbers are in a list.
# number=[int(input('enter number:')) for i in range(5)]
# count=0
# for i in range(len(number)):
#     if i % 2 == 0 :
#         count= count + 1
# print('even:', count)

# Count how many odd numbers are in a list.

# Reverse a list using a loop.
# number=[int(input()) for i in range(5)]
# reversed=[]
# count=len(number)
# for i in range(len(number)):
#      reversed.append(number[count - i - 1])
# print('reversed:', reversed)



# Print all numbers in a list that are greater than 10.




# Count how many times a number (say 5) appears in a list.

# Print only the positive numbers from a list.

# Find the sum of all numbers in a list.

# Find the product (multiplication) of all numbers in a list.
def add_two(a, b):
    print('sum is',a+b)

# add_two(2,3)