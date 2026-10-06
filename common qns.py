#
#
#                                      #prime or not
# from function import result
from itertools import product
from unittest import result


def prime(num):
    for i in range(2,num):
        if(num%i==0):
            break
        else:
            return num
result=prime(num=12)
print(result,"is a prime number")





#                                       pallindrome program
# def pallindrome(num):
#     if(num[::-1]==num):
#         return num
# result=pallindrome("aadhil")
# print(result,"pallindrome")

#                                      ARMSTRONG program
#
# def Armstrong(n):
#     s=str(n)
#     l=len(s)
#     sum=0
#     for i in s:
#         sum=sum+int(i)**l
#     if(sum==n):
#          return sum
# print(Armstrong(153),'is amstrong')
#
#
#
# #                                    FACTORIAL OF A NUMBER
# def fact(n):
#     product=1
#     for i in range(n,0,-1):
#         product*=i
#     return product
# print(fact(5))


# num=3
# for i in str(num):
#     print(i)
#     if(int(i)>2 and i%range(2,num)):
#         break
#
#     else:
#       print("prime ")



# l=[3,6,8,5,20,46]
# for num in l:
#     prime=True
#     if num<2:
#         prime=False
#     else:
#         for i in range(2,num):
#             if num%i==0:
#                 prime=False
#                 break
#     if prime:
#         print(num)

























# l=[3,5,8,6,19,21]
# for num in l:
#     prime=True
#     if num<2:
#         prime=False
#     else:
#         for i in range(2,num):
#             if num%i==0:
#                 prime=False
#                 break
#     if prime:
#         print(num)

# i=3
# while i<31:
#     if i%3==0:
#         print(i, end=" ")
#     i += 1




#0,1,2,3,5,8,13
# a,b=0,1
# for i in range(0,8):
#     print(a)
#     a,b=b,a+b

# n="python"
# for i in range(len(n)+1):
#     print(n[:i])











# l=[3,6,4,7,9,78]
# for num in l:
#     prime=True
#     if num<2:
#         prime=False
#     else:
#         for i in range(2,num):
#             if num%i==0:
#                 prime=False
#     if prime:
#         print(num)
#
# n="python"
# for i in range(len(n)+1):
#     print(n[:i])
# a,b=0,1
# for i in range(0,8):
#     print(a)
#     a,b=b,a+b


# for i in range(3,31):
#     if i%3==0:
#         print(i,end=",")



for i in range(1,6):
    for j in range(5,i-1,-1):
        print(j,end=" ")
    print()

