#while

#
# # # #1,2,3,4,5,.....100
# i=1
# while(i<=100):
#     print(i)
#     i=i+1
#
# # # #1,3,5,7,9,11,13,15
# i=1
# while(i<=15):
#     print(i)
#     i=i+2
# # #2,4,6,8,10,12
# i=2
# while(i<=12):
#     print(i)
#     i=i+2
#
# # #1,4,7,10,13,16
# i=1
# while(i<=16):
#     print(i)
#     i=i+3
# #10,20,30,40,50,60,70,80
# i=10
# while(i<=80):
#     print(i)
#     i=i+10
#
# #3,6,9,12,15,18,21
# i=3
# while(i<=21):
#     print(i)
#     i=i+3
#5,4,3,2,1
# i=5
# while(i>=1):
#     print(i)
#     i=i-1
#8,6,4,2,0
# i=8
# while(i>=0):
#     print(i)
#     i=i-2
#100,101,102,.....200
# i=100
# while(i<=200):
#         print(i)
#         i=i+1

#print all 4 digit numbers(1000-9999)
# i=1000
# while(i<=9999):
#         print(i)
#         i=i+1
#print all 3 digit number divisble by 3
# i=100
# while(i<=999):
#     if(i%3==0):
#         print(i)
#     i=i+1
#print those 4 digit number that contain digit 3
# i=1000
# while(i<=9999):
#     i=str(i)
#     if('3'in i):
#         print(i)
#     i=int(i)+1
#print those  number that are divisible by 3 and 5 in the range(1,100)
# i=1
# while(i<=100):
#     if(i%3==0 and i%5==0):
#         print(i)
#     i=i+1
#
#1,4,9,16,25,36,49,64,81,100
# i=1
# while(i<=10):
#     print(i**2)
#     i=i+1
#count of those 3 digit number that contains digit '3'
# count=0
# i=100
# while(i<=999):
#     if('3' in str(i)):
#         print(i)
#         count=count+1
#     i=i+1
# print(count)
#count of those number are divisible by 7 or 3 in the range(200,300)
# count=0
# i=200
# while(i<=300):
#     if(i%7==0 and i%5==0):
#         print(i)
#         count=count+1
#     i=i+1
# print(count)
# count of odd numbers that are divisible by 5 in range(1,100)
# count=0
# i=1
# while(i<=100):
#     if(i%5==0 and i%2!=0):
#         print(i)
#         count=count+1
#     i=i+1
# print(count)
#count all pallindrome numbers upto 1 to 1000
# count=0
# i=1
# while(i<=1000):
#     s=str(i)
#     if(s==s[::-1]):
#         # print(i)
#         count=count+1
#     i=i+1
# print(count)
#count of those number that are divisible by 3 in the range(1,50)
# count=0
# i=1
# while(i<=50):
#     if(i%3==0):
#         #print(i)
#         count=count+1
#     i=i+1
# print(count)
#sum of series 1,2,3,4,5
# sum=0
# i=1
# while(i<=5):
#     sum=sum+i
#     i=i+1
# print(sum)
#sum of those number that are divisible by 3 in the range(1,50)
# sum=0
# i=1
# while(i<=50):
#     if(i%3==0):
#      sum=sum+i
#     i=i+1
# print(sum)
#sum of all 3 digit numbers
# sum=0
# i=100
# while(i<=999):
#     sum=sum+i
#     i=i+1
# print(sum)
#sum of first 10 even numbers
# sum=0
# i=2
# while(i<=20):
#     sum=sum+i
#     i=i+2
# print(sum)
#product of series
# i=1
# product=1
# while(i<=5):
#     product=product*i
#     i=i+1
# print(product)
#product first 10 odd number
# i=1
# product=1
# while(i<=20):
#     product=product*i
#     i=i+2
# print(product)
#product of numbers that contains digit '3' in the range(1,50)
# i=1
# product=1
# while(i<=50):
#     if('3' in str(i)):
#        product=product*i
#     i=i+1
# print(product)
#factoiral of a number
# num=int(input("enter a number:"))
# fact=1
# i=1
# while(i<=num):
#     fact=fact*i
#     i=i+1
# print(fact)
#multiplication table of a number
num=int(input("enter a number: "))
fact=0
i=1
while(i<=10):
    print(num,'*',i,'=',num*i)
    i=i+1



