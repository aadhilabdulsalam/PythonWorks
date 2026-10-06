#check whether a number is postive odd/positive even/negative odd/negative even
# num=int(input("enter a number"))
# if(num>0):
#     print("positive")
#     if(num%2==0):
#         print("positive even")
#     else:
#         print("positive odd")
# else:
#     print('negative')
#     if(num%2==0):
#         print("negative odd")
#     else:
#         print("negative odd")
num=int(input("enter a number"))
if(num%2==0):
    print('divisible  two')
    if(num%3==0):
        print('divisible by three')

    else:
        print("not divisible by three")
else:
    print("not divisible by 2 ")
    if(num%3==0):
        print("divisible by three")
    else:
        print("not divisible by three")


