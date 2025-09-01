# 1. Print even and odd numbers from 1 to 10
# # Output:
# # 1 is odd
# # 2 is even
# # ...

for i in range(1,11):
    if i % 2 ==0:
        print(i,"is even")
    else:
        print(i,"is odd")

#add the sum of all the digits of a number
# num = '123'
# res = 0
# for i in range(len(num)):
#     res = res + int(num[i])

# 2. Count how many numbers between 1–50 are divisible by 3
# # Output: Total numbers divisible by 3: X
count=0
for i in range(1,51):
    if i % 3 == 0:
        count=count + 1
print("total num divisible by 3",count)



# 3. Check if numbers 1–20 are prime
# # Output: 2 is prime, 3 is prime, 4 is not prime, ...

# 4. Print "Fizz" for multiples of 3, "Buzz" for multiples of 5, and "FizzBuzz" for multiples of both
# # Output:
# # 1
# # 2
# # Fizz
# # 4
# # Buzz
# # ...
array=[9,15,12,25,45,8] 
for i in range(len(array)):
    num = array[i]
    if num % 3==0 and num % 5 ==0:
        print('fizzbuzz',num)
    elif num % 3 ==0:
        print("fizz",num)
    elif num % 5 ==0:
        print("buzz",num)
    elif num % 3==0 and num % 5 ==0:
        print('fizzbuzz',num)
    else:
        print("neither divisible by 3 nor 5",num)




# 5. Take a list of numbers and print only the positive ones
# # Example: [3, -1, 0, 7, -5] → Output: 3, 7 
example=[3,-1,0,7,-5]
for i in range(len(example)):
    ex= example[i]
    if ex > 0:
        print('number is pos:',ex)


# 6. Ask the user for 5 numbers and count how many are even
# # Output: Number of even numbers: X

oddEven = [int(input()) for i in range(5)]
for i in range(len((oddEven))):
     num= oddEven[i]
     if num % 2 ==0:
         print("number is even:",num)

# 7. Loop through a string and print only the vowels
# # Example: "Python" → Output: o
word="python"
for i in range(len(word)):
     iu= word[i]
     if iu == 'a'or iu == 'e'or iu == 'i' or iu == 'o' or iu == 'u':
         print('even word:',iu)


# 8. Check if a word entered by the user is a palindrome
# # Example: "madam" → Output: Palindrome

letter=input("enter a word to reverse:") 
reversedWord=""
count=len(letter)
flag=True
for i in range(count): 
    reversedWord=reversedWord + letter[count -i -1]
    print('reversed word',reversedWord)
for i in range(count):
   if reversedWord[i] != letter[i]:
       flag=False
       print('is not palindrom:',letter)
       break
if flag == True:
    print('is palindram',letter)

        

# 9. Find numbers from 1 to 100 that are divisible by both 2 and 7
# # Output: 14, 28, 42, ...

for i in range(1,101):
    if i % 14 == 0: #lcm(2,7):14 so divisible by 14
        print('divisible both by 2 and 7:',i)

# 10.  the user for 10 numbers and find the largest
# # Output: Largest number is: X
number_10=[int(input()) for i in range(10)]
for i in range(len(number_10)):
    largest=number_10[0]
for i in range(1,len(number_10)):
    if number_10[i] > largest:
        largest = number_10[i]

print('the largest number:', largest)

