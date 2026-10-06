from unittest import result  #function definition




# def addition():
#     "Addition of Two number"
#     num1=int(input("Enter a number"))
#     num2=int(input("Enter an another number"))
#     sum=num1+num2
#     print("Sum",sum)
#     return
# addition()              #function call

#define a function to display a message "Hello Your name"

# def helloworld():
#     "printing HEllO YOUR NAME"
#     a=input("enter your name")
#     print("HELLO ",a)
#     return
# helloworld()
 #define a function to print the factorial of a number
# def factorial():
#     "FINDING FACTORIAL OF A NUMBER"
#     num=int(input("Enter a number"))
#     for i in range(num-1,0,-1):
#         num*=i
#     print(num)
#     return
# factorial()

#define a function to find the number of occurence of a particular character in a string
# def occurence():
#     "FINDING OF OCCURENCE"
#     string=input(("enter a string"))
#     num=input("enter a character")
#     count=0

#     for i in string:
#      if(i==num):
#        count=count+1
#     print(count)
#     return
# occurence()

#define a function to check the number is prime or not
# def prime():
#     "finding  prime number"
#     num=int(input("enter a number"))
#     for i in range(2,num):
#         if(num%i==0):
#             print("not prime number")
#             break
#     else:
#         print(" prime number")
#
# prime()
#define a function that takes 3 arguments(amount,rate,year)and find the simple interest value
# def interest(amount,year,rate):
#     "finding simple interest"
#     si=amount*year*rate/100
#     print(si)
#     return
# interest(5000,5,7)


#define a function that takes 3 arguments(amount,rate,year)and find the simple interest value using return statement
# def interest(amount,year,rate):
#     "finding simple interest"
#     si=amount*year*rate/100
#     print(si)
#     return si
# result=interest(5000,5,7)
# print(result)
#define a function that takes 3 numbers and returns the product of 3 number
# def product(num1,num2,num3):
#     "finding the product of 3 number"
#     p=num1*num2*num3
#     return p
# result=product(5,6,7)
# print(result)
#define the function that takes a string and a character and return the number of occurence of the character in the string
# def occurence(string,num):
#     "FINDING OF OCCURENCE"
#     count=0
#     for i in string:
#      if(i==num):
#        count=count+1
#     return count
# result=occurence("aadhil","d")
# print(result)
#define a function that  takes a list as argument and return new kist containing unique elements from the list
l=[12,34,78,12,67,34,90,23]
def unique(l):
    new = []
    for i in l:
        if i not in new:
            new.append(i)

    return(new)
print(unique(l))
#define a function that  takes 2 list as argument and print the common elements
# l1=[12,34,56,78,90]
# l2=[90,34,11,57,45]
# def common(l1,l2):
#     for i in l1:
#         if i in l2:
#          print(i)
#
#     return
# common(l1,l2)

# keyword arguments
# def nam(a,b):
#     print("Name",a)
#     print("age",b)
# nam(a="aadhil",b=12)


# default arguments
# def nam(a,b=23):
#     print("Name",a)
#     print("age",b)
# nam("aadhil")


# #arbitory positional arguments
# def nam(*args):
#     print(args)
# nam(23,46,77)
# nam(88,33,44)
# nam(100,1200,1300)

#arbitory keyword arguments
def nam(**args):
    print(args)
nam(name="adithyan",age=21,place="alappuzha")
nam(name="akhilesh",age=21,place="alappuzha")
nam(name="aadhil",age=20,place="alappuzha")
#define a function that  accept any number of numbers and return their sum
# def sum(*args):
#     sum=0
#     for i in args:
#         sum=sum+i
#     print(sum)
#
# sum(12,34,55)
# sum(100,200,400)
