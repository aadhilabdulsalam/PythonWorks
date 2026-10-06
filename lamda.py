#lambda function
from functools import reduce

#square of a number

#
# sq=lambda x:x**2
# print("sqaure=",sq(4))
#cube of a number
# sq=lambda x:x**3
# print(sq(3))
# #length of a string
# s=lambda a:len(a)
# print(s("hello"))
#name attribute of a dictionary
# s=lambda a:a['name']
# print(s({'name':'arun','age':32}))
#first character of a string
# s=lambda a:a[0]
# print(s("AADHIL"))
# #last element of a list
# s=lambda a:a[-1]
# print(s([1,2,3,4]))
#sum of 2 number
# s=lambda a,b:b+a
# print(s(1,2))
# #sum of 3 number
# s=lambda a,b,c:a+b+c
# print(s(12,34,21))
# #product of four number
# s=lambda a,b,c,d:a*b*c*d
# print(s(1,4,2,3))
#create a newlist with square of alist
#   MAP
# l=[1,2,3,4]
# print(list(map(lambda a:a**2,l)))
# print(set(map(lambda a:a**2,l)))
# print(tuple(map(lambda a:a**2,l)))
# #create a new list of cubes
# print(list(map(lambda a:a**3,l)))
# # create a new list of square roots
# l=[25,36,81,100]
# print(list(map(lambda a:a**0.5,l)))
# #create a new list of length
# colors=['red','green','blue','yellow','black']
#
# #create a new list of first character
# print(list(map(lambda a:a[0],colors)))
# #create a new list of first characters
#
# #create a new list of last characters
# print(list(map(lambda a:a[-1],colors)))
# #create a new list of reverse of each elemnt
# print(list(map(lambda a:a[::-1],colors)))
# #Given a list
# l=[23,78,12,56]
# #Add 10 to each element in the given sequence
# print(list(map(lambda a:a+10,l)))
# ##given a list of dictionaries
# l=[{'empid':100,'name':'arun','salary':20000,'email':'arun@gmail.com'},
#    {'empid':101,'name':'amal','salary':25000,'email':'amal@gmail.com'},
#    {'empid':102,'name':'anu','salary':30000,'email':'anu@gmail.com'}]
# #
# # # create a new list of emails
# print(list(map(lambda a:a['email'],l)))


#                                       FILTER FUNCTION
#create a new list of even number from the given the list

# l=[1,2,3,4,5,6,7,8,9,10]
# print(list(filter(lambda a:a%2==0,l)))

#given a list
# l=[23,67,90,12,45,52]
# #number greater than 50
# print(list(filter(lambda a:a>50,l))

#given a list of fruits
# f=['apple','orange','grapes','pineapple','grapes']
# #fruitname whose length is greater than 5
# print(list(filter(lambda n:len(n)>5,f)))
# #given alist
# l=[34,78,96,23,12,15]
# #number divisible by 3 and 5
# print(list(filter(lambda a:a%3==0 and a%5==0,l)))

#                  REDUCE  FUNCTION

#sum of a list
l=[1,2,3,4]
import functools
print(reduce(lambda a,b:a+b,l,0))
#product of a list
print(reduce(lambda a,b:a*b,l,1))
