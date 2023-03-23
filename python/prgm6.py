# b = 1                                     (interview question)
# s = 10*b
# g = 5*s
# ta = 2*g+1*s+5*b
# tb = 1*g+0*s+25*b
# tc = 0*g+10*s+1*b
# if ta > tb and ta > tc:
#     print('ta')
# elif tb > ta and tb > tc:
#     print('tb')
# else:
#     print('tc')



# import time
# str=input('Enter your name : ')
# hours = int(time.strftime('%H'))                               (greetings)
# if(hours>=0 and hours<=11):
#   print("Hello ",str.capitalize(),", Good Morning ")
# elif(hours>=12 and hours<=17):
#   print("Hello ",str.capitalize(),", Good Afternoon ")
# else:
#   print("Hello ",str.capitalize(),", Good Evening ")



# a = int(input("Enter any number : "))                       (recurrsive fibonnica)
# def fibonacci(n):
#     if (n == 1 or n == 0):
#         return n
#     else:
#         return fibonacci(n-1)+fibonacci(n-2)
# for i in range(a):
#     print(fibonacci(i))


# x=input("enter a no.")                                    (try and except method)
# rev=0
# try:
#     i=int(x)
#     while(i>0):
#         rev=(rev*10)+i%10
#         i=i//10
#     print(rev)
# except:
#     print("invalid input")


# x="earth"                                                (Anagram)
# y="thera"
# if len(x)!=len(y):
#     print("not anagram")
# else:
#     if sorted(x)==sorted(y):
#         print("anagram")
#     else:
#         print("not a anagram")
