# n1=0
# n2=1
# print(n1)
# print(n2)
# for i in range(2,15):        (fibonicca series)
#     sum=n1+n2
#     print(sum)
#     n1=n2
#     n2=sum


# x=[1,2,3,4,5]
# print(sum(x))          (sum of elements in an list)
# (if we want to add or sub a no.)
# print(sum(x, 10)) or print(sum(x, -10))


# x = [1, 2, 3, 4, 5]      (sum w/o function)
# sum = 0
# for i in x:
#     sum = sum+i
# print(sum)


# x = [23, 67, 3, 90, 45, 23]
# x.sort()                             (largest no. & smallest no.)
# print(x)
# print(x[-1])
# print(x[0])


# x=[1,2,3,40,5]                (length of list)
# print(len(x))

# x=[1,2,3,40,54,89]
# count=0
# for i in x:
#     count=count+1               (length of list w/o function)
# print(count)


# x = [23, 56, 12, 7, 9, 76]
# temp = x[0]
# x[0] = x[5]                        (swapping first and last element)
# x[5] = temp
# print(x)
            #OR
# x[0], x[-1] = x[-1], x[0]


# x = ['geeks', 'for', 'geeks', 'geeks']          (frequency of a word)
# word = 'geeks'
# count = 0
# for i in x:
#     if(word == i):
#         count = count+1
# print(count)


# x = ['for', 'to', 'for', 'and', 'for', 'all']       (remove all occuring words)
# while x.count('for') > 0:
#     x.remove('for')
# print(x)
