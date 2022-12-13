# total=0
# for i in range(1,21):
#     total += i
#     print(total)

# n=int(input("enter he number: "))
# total = 0
# for i in range(1,n+1):
#   total+=i
# print(total)  
# 
# 
#  
# total = 0
# num = input("Enter a number : ")
# for i in range(0,len(num)):
#   total += int(num[i])
#   print(total)

# name = input("enter your name : ")
# temp = ""
# for i in range(0, len(name)):
#   if name[i] not in temp:
#       print(f"{name[i]}:{name.count(name[i])}")
#       temp = name[i]

# i=0
# for i in range(1,11):
#   if i == 6:
#     break
#   print(i)


# winning_number = 55
# guess = 1
# number = int(input("guess a number between 1 and 100 : "))
# game_over = False

# while not game_over:
#   if number == winning_number:
#     print(f"you win, and you guessed this number in {guess} times")
#     game_over =True
#   else:
#     if number < winning_number:
#       print("too low")
#       guess += 1
#       number = int(input("guess again : "))
#     else:
#       print("too high")
#       guess += 1
#       number = int(input("guess agin : "))

# def add_three(a,b,c):
#   return a+b+c

# print(add_three(5,5,5))


# a="chandan"
# print(a[-1])

# def is_even(num):
#     if num%2 == 0:
#         return True
#     else:
#         return False
# print(is_even(9))

# def greater(a,b):
#     if a>b:
#         return a
#     else:
#         return b

# num1 = int(input("enter first number "))
# num2 = int(input("enter second number "))
# bigger = greater(num1,num2)
# print(f"{bigger} is greater")

# def greatest(a,b,c):
#     if a>b and a>c:
#         return a
#     elif b>a and b>c:
#         return b
#     else:
#         return c
# print(greatest(10,20,30))

# def is_palindrom(word):
#     reversed_word = word[::-1]
#     if word == reversed_word:
#         return True
#     else:
#         return False
# print(is_palindrom("madam"))
# print(is_palindrom("madam"))

# def is_palindrom(word):
#     return word == word[::-1]
# print(is_palindrom("name"))
# print(is_palindrom("horse"))


# def func():
#     x = 7
#     return x
# print(func())
# print(x)

# mixed=["hello","hen",2,5,5]
# mixed[1:] = ["two","five"]
# print(mixed)

# fruits = []
# fruits.append("mango")
# fruits.append("grapes")
# print(fruits)

# fruits1 = ['orange','apple','pear']
# fruits2 = ['orange','apple','pear']
# print(fruits1 == fruits2)
# print(fruits1 is fruits2)

# user_info = 'harshit'.split()
# print(user_info)

#name,age= input("enter your name and age").split(',')
#print(name)
# print(age)

# user_info = ['harshit','24']
# print(','.join(user_info))

fruits = ['orange','apple','pear','banana','kiwi']
for fruit in fruits:
    print(fruit)

i=0
while i < len(fruits):
    print(fruits[i])
    i += 1