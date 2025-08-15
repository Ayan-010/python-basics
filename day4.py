# Beginner For Loop Practice Problems
# 1. Print numbers from 1 to 10



# for i in range(1,11):
#   print(i)

# 2. Print even numbers from 2 to 20



# for i in range(2 ,21 ,2):
#   print(i)

# 3. Print the squares of numbers from 1 to 5



# for i in range(1,6):
#     print(i**2)

# 4. Print each letter in a word
# word = "Python"
# for letter in word:
#     print(letter)
 


# word="Python" 
# for i in range(len(word)):
#   print(word[i]) 

# 5. Sum of numbers from 1 to 100
res=0
for i in range(1,101):
  res=res + i

print(res)

even=0
for i in range(0,101,2):
  even=even + i
print("sum of even number is",even)
 


# 6. Print a multiplication table (e.g., for 5)
# for i in range(1, 11):
#     print(f"5 x {i} = {5 * i}")

# for i in range(1,11):
#   print(i * 5)

# 7. Print elements of a list
fruits = ["apple", "banana", "cherry"]
for i in range(len(fruits)):
  print(fruits[i])


# 8. Reverse a string
word =input("enter a word to reverse:") 
reversedWord=""
count=len(word)
for i in range(count):
  reversedWord=reversedWord + word[count -i -1]
  print(reversedWord, i)
print("reversed word is",reversedWord)






# 9. Find factorial of a number (e.g., 5)
num=int(input("enter a number to cal fact:"))
fact=1
for i in range(1,num+1):
  fact=fact * i
print("factorial:",fact)


# 10. Print stars pattern


 