# x=input("enter string:")             (palindrome string)
# y=x[::-1]
# if(y==x):
#     print("palindrome")
# else:
#     print("not a palindrome")    



# i=int(input("enter a number:"))        (reverse a number)
# rev=0
# while(i>0):
#     rev=(rev*10)+i%10
#     i=i//10
# print(rev)    



# i = int(input("enter a number:"))          (palindrome number)
# rev = 0
# x = i
# while(i > 0):
#     rev = (rev*10)+i % 10
#     i = i//10
# if(x == rev):
#     print("palindrome")
# else:
#     print("not a palindrome")


# x = int(input("enter fiest no.:"))          (swapped positions of two numbers)
# y = int(input("enter first no.:"))
# temp = x
# x = y
# y = temp
# print("the swapped no. are ", x, y)



# x = int(input("enter a prime no.:"))        (prime number)
# count = 0
# if(x > 1):
#     for i in range(1, x+1):
#         if(x % i) == 0:
#             count = count+1
# if(count == 2):
#     print("prime no.")
# else:
#     print("no prime no.")


# x = int(input("enter a no.:"))              (factorial)
# y = 1
#for i in range(1, x+1):
#     y = y*i
#print(y)


# def factorial(n):
#     if(n ==0 or n==1):
#         return 1
#     else:
#         return n*factorial(n-1)              (recurssive method for factorial)

# num = 7
# print(factorial(num))


# def factorial(n):
#     return 1 if(n ==0 or n==1) else n* factorial(n-1)      (ternary operator)
# num = 4
# print(factorial(num))
