# x=[1,2,3,4]     (to print an element in a list)
# c=2           
# c in x               (in operator is used to print true or false based on the value present in the list)
# print(c)


# x=[1,2,3,4]         (element present in a list true or false)
# c=5 in x  #true/false
# print(c)



# list=[2,5,9,2,3,6,4,5,3,4,9,3]        (deleting duplicates)
# result=[]
# for i in list:
#     if i not in result:
#         result.append(i)
# print(result)    


# x=[1,2,3,4]  
# c=5
# if(c in x):
#     print('element found')
# else:
#     print('element not found')


# list=[1,2,3,4]
# print('before clear',list)              (1st method-clear a list)
# list.clear()
# print('after clear',list)


# list = [1, 2, 3, 4]
# print('before clear', list)          (2nd method-clear a list)
# list = []
# print('after clear', list)


# list=[1,2,3,4]
# print('before clear',list)              (3rd method-clear a list)
# list *=0                       (*=0 is used to clear a list)
# print('after clear',list)


# list=[1,2,3,4]
# print('before clear',list)              (4th method-clear a list)
# del list[:]                      
# print('after clear',list)


# a = [1, 2, 3]                               (copy w/o reference)
# b = a[:]
# b[1] = 4
# print(b, a)


# a=[1,2,3,4]                                  (1st-copying a list)
# b=a
# print(b)


# a=[1,2,3]
# b=[]                                      (2nd-copying a list)
# b.extend(a)
# print(b)


# a=[1,2,3,4]                                  (3rd-copying a list)
# b=list(a)                                     (list() method) 
# print(b)


# a = [1, 2, 3]                                 (4th-copying a list)
# b = a.copy()                                  (copy() method)
# print(b)

 
# a=[1,2,3,4,5]                                 (5th-copying a list)
# b=[i for i in a]                     (after looping the element is stored in 'i' and then stored in 'b')
# print(b)
