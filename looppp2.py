#for loop
# s="hello"
# for i in s
#     print(i)

# colors=['red','green','blue']
# for i in colors:
#     print(i)

# s={10,20,30}
# for i in s:
# #     print(i)
#
# d={'a':10,'b':20,'c':30}               #dictionary
# for i in d:
#     print(d.values())
#     print(i)


# t=(12,78,34,50)           #tuple
# for i in t:
#     print(i)
# l=[56,89,34,10]
# for i in l:              #list
#     print(i)
# l=[12,34,56,89,16,69,33]
#print each number in a list
# for i in l:
#     print(i)
# #print even numbers in the list
# l=[12,34,56,89,16,69,33]
# for i in l:
#     if(i%2==0):
#         print(i)
#print those numbers that are divisible by 5
# l=[12,34,56,89,16,69,33]
# for i in l:
#     if(i%5==0):
#         print(i)
# #print those numbers that contains digit '3'
# l=[12,34,56,89,16,69,33]
# for i in l:
#     if('3' in str(i)):
#         print(i)
#sum of list
# l=[12,34,56,89,16,69,33]
# sum=0
# for i in l:
#     sum=sum+i
#
# print(sum)
#count of even numbers in a list
# l=[12,34,56,89,16,69,33]
# count=0
# for i in l:
#     if(i%2==0):
#      count=count+1
# print(count)
#product of list
# l=[12,34,56,89,16,69,33]
# product=1
# for i in l:
#     product=product*i
# print(product)
# #print squares of each numbers
# l=[12,34,56,89,16,69,33]
# for i in l:
#         print(i**2)
#given a list
# l=[12,4.5,6.8,30,"arun","hello"]
#print floating point numbers
# for i in l:
#         if(type(i)==float):
#                 print(i)
# #print string values:
# for i in l:
#         if(type(i)==str):
#                 print(i)
#print numbers:
# for i in l:
#         if(type(i)==int):
#                 print(i)
#2.given a dictionary
# d={'a':23,'b':25,'c':28,'d':30,'e':22}
# # print only even values
# for i in d.values():
#     if(i%2==0):
#         print(i)
# 3.Given a list of colors=['red','green','blue','orange','black']
# colors=['red','green','blue','orange','black']
#print starting letter of each color
# for i in colors:
#         print(i[0])
#print last letter of each color
# for i in colors:
#         print(i[-1])
#print reverse of each color
# for i in colors:
#         print(i[::-1])
# #print all colors containing letter 'b'
# for i in colors:
#         if('b' in i):
#             print
#Range function
#1,2,3,4,5
# for i in range(1,6):
#     print(i,end=" ")
#1,3,5,7,9,11
# for i in range(1,12,2):
#     print(i,end=" ")
#2,4,6,8,10
# for i in range(2,11,2):
#     print(i,end=" ")
#100,200,300,400,500
# for i in range(100,501,100):
#     print(i,end=" ")
#5,4,3,2,1
# for i in range(5,0,-1):
#     print(i,end=" ")
#3,6,9,12,15,18,21
# for i in range(3,22,3):
#     print(i,end=" ")
#1,4,9,16,25,36
# for i in range(1,7):
#      print(i**2)
# #print all three digit number
# for i in range(100,1000):
#     print(i,end=" ")
# #print all number divisible by 3 in the range 100-200
# for i in range(100,200):
#     if(i%3==0):
#       print(i)
#1,8,27,64,125
# for i in range(1,7):
#      print(i**3)
# #print each number in a list
# l=[12,13,34,78]
# for i in l:
#     print(i)
#print each digit in a number
# n=1234
# s=str(n)
# for i in s:
#     print(i)
#sum of a list
# l=[1,2,3,4]
# sum=0
# for i in l:
#     sum=sum+i
# print(sum)
# #sum of digit in  a sum
# n=1234
# s=str(n)
# for i in s:
#     s=s+i
# print(sum)
#reverse of a string without using slice operator
# s="hello"
# rev=""
# for i in s:
#     rev=i+rev
# print(rev)
# reverse a number
# n=1234
# s=str(n)
# rev=""
# for i in s:
#     rev=i+rev
# print(rev)
#given a list
# l=[1,2,3,4]
# # print square of each  number
# for i in l:
#     print(i**2)
# # #create a new set
# new=set()
# for i in l:
#     new.add(i)
# print(new)
# #create a dictionary where keys are numbers and values are square of each number
# d={1:1,2:4,3:9,4:16}
# new={}
# for i in l:
#     new[i]=i**2
# print(new)
#loop control statement

# s="hello"
# for i in s:
#     if(i=="l"):
#         continue
#     print(i)
colors=['red','green','blue','yellow','black','orange']
#print all colours

#print the first color starting with 'b'
# for i in colors:
#     if(i[0]=="b"):
#         print(i)
#         break
#print all colors except color starting with 'b'
# for i in colors:
#     if(i[0]!="b"):
#         print(i)
#         continue
#print all color contains letter 'n'
# for i in colors:
#     if('n' in i):
#         print(i)
#         break
# print all colors except color contain letter'n'
# for i in colors:
#     if ('n' not in i) :
#         print(i)
#         continue
# #Given a list l=[1,2,3,4]
# # create a new list with squares of each element
# l=[1,2,3,4]
# new=[]
# for i in l:
#     new.append(i**2)
# print(new)
#Given a list l=[12,67,59,23]
#create a list with elements whose value is greater than 50.
# create a new set with elements whose value is greater than 50
# l=[12,67,59,23]
# # new=[]
# # for i in l:
# #     if(i>50):
# #       new.append(i)
# # print(new)
# new=set()
# for i in l:
#     if(i>50):
#         new.add(i)
# print(new)
#Given a list l=[1,2,3,4]
#create a new dictionary where keys are numbers and values are squares of each number
# l=[1,2,3,4]
# new={}
# for i in l:
#     new[i]=i**2
# print(new)
# ##create a list of 5 random numbers
# new=[]
# for i in range(5):
#     n=int(input("enter the  number"))
#     new.append(n)
# print(new)
#Find the factors of a number
# num=int(input("enter a number"))
# for i in range(1,num+1):
#     if(num%i==0):
#         print(i)

#find the armstrong number
# n=int(input("enter a number"))
# s=str(n)
# l=len(s)
# sum=0
# for i in s:
#     sum=sum+int(i)**l
# if(sum==n):
#     print(" is a armstrong number ")
# else:
#     print("not a armstrong number")

#find the fibinocci series
# a=0
# b=1
# for i in range(1,21):
#     print(a)
#     a,b=b,a+b
# else statement in loop
# for i in range(1,11):
#     if(i==5):
#         break
#     print(i)
# else:
#     print("hello")
#write a program to chck the number is prime or not
# num=int(input("enter a number"))
# if(num>1):
#   for i in range(2,num):
#     if(num%i==0):
#         print("not prime")
#         break
#   else:
#     print("prime")
# else:
#     print("number is neither prime or composite")
#check whether a number is a perfect or not
# num=int(input("enter a number"))
# sum=0
# for i in range(1,num):
#     if(num%i==0):
#         sum=sum+i
# if(sum==num):
#         print("perfect number")
# else:
#         print('not ')
