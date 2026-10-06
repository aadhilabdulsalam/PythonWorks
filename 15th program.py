#write a program to check whether an entered number is 2digit/3digit/4digit
# a=int(input("enter a number"))
# s=str(a)
# if(len(s)==3):
#     print("number is three digit")
# elif(len(s)==2):
#     print("number is two digit")
# elif(len(s)==4):
#     print("number is four digit")
# else:
#     print("number have more than four digit or less than 2 digit")
# #write a basic calcualtor program to perform arithematic operator(+*/-)
# num1=int(input("enter the first number"))
# num2=int(input("enter the second number"))
# op=input("enter the operator")
# if op=="+":
#     print("sum is",num1+num2)
# elif op=="*":
#     print("product  is",num1*num2)
# elif op=="-":
#     print(num1-num2)
# elif op=="/":
#     print(num1/num2)
# else:
#     print("invalid input")
#write a program to print the number of days in a month
# month=input("enter a month")
# l1=['januvary','march','may','july','august','october','december']
# l2=['april','june','september','november']
# l3=['feburary']
# if(month in l1):
#     print("31 days")
# elif(month in l2 ):
#     print("30 days")
# elif(month in l3):
#     print("28/29 days")
# else:
#     print("invalid input")
#write a program to print the grade of student based on entered score
mark=int(input("enter your mark"))
if(mark>=91 and mark<=100):
    print("A grade")
elif(mark>=81 and mark<=90):
    print("B grade")
elif(mark>=71 and mark<=80):
    print("C grade")
elif(mark>=61 and mark<=70):
    print("D grade")
elif(mark<61):
    print("E  grade")
else:
    print("ombbbbb")