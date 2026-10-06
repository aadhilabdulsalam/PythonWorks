#find maximum of three number
# num=int(input("enter the first number"))
# num1=int(input("enter the second number"))
# num2=int(input("enter the third number"))
# if(num>num1 and num>num2):
#     print("first number is largest")
# elif(num1>num and num1>num2):
#     print("second number is largest")
# else:
#     print("third number is largest")
#find the maximum of four number
num=int(input("enter the first number"))
num1=int(input("enter the second number"))
num2=int(input("enter the third number"))
num3=int(input("enter the fourth number"))
if(num>num1 and num>num2 and num>num3):
    print("first number is largest")
elif(num1>num and num1>num2 and num1>num3):
    print("second number is largest")
elif(num2>num and num2>num1 and num2>num3):
    print("third number is largest")
else:
    print("fourth number is largest")