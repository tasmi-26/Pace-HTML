# a=[1,2,3,4,5]                      
# product=1                               (product)
# for i in a:
#     product=product*i       
# print(product)


# import numpy                    (product-importing numpy function)
# a=[1,2,3,4,5]
# b=numpy.prod(a)
# print(b)


# x='WELCOME TO PYTHON PROGRAMMING'          (reversing)
# a=x.split()
# y=a[-1::-1]
# print(" " .join(y))                        (PROGRAMMING PYTHON TO WELCOME)


# x='WELCOME TO PYTHON PROGRAMMING'          (substring)
# y='PYTHON'
# if y in x:
#     print(y)


# x='hello world'                          (substring)
# y="hello"
# for i in x:
#     if(y in x):
#         print("Present")
#     else:
#         print("Absent")
#     break


# x='hello world'
# y='world'
# print(x.find(y))           # 6 is the position where world starts
# if(x.find(y) == -1):       #-1 is the default value if the word is not present in the string
#     print('absent')
# else:
#     print('present')
 

# x='hello welcoming'        (length of string)
# count=0
# for i in x:         or   while x[count:]:
#     count=count+1
# print(count)


# x = input('enter string:')           (frequency of characters in a string)
# d = dict()
# for i in x:
#     if i in d:
#         d[i] = d[i]+1
#     else:
#         d[i] = 1
# print(d)


# def frequency(word):                    (frequency of characters in a string using functions)
#     freq = {}
#     for i in word:
#         if i in freq:
#             freq[i] = freq[i]+1
#         else:
#             freq[i] = 1
#     return freq
# print(frequency("pace wisdom solutions"))


# x = "10"
# y = "80"
# z = "30"
# if x > y and x > z:
#     print(x, "is largest")                    (largest among 3)
# elif y > x and y > z:
#     print(y, "is largest")
# else:
#     print(z, "is largest")



