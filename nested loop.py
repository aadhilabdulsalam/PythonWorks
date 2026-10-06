# for i in range(1,4):
#     for j in range(1,6):
#      print(i)
# for i in range(1,4):
#     for j in range(1,6):
#      print(j)
# for i in range(1,4):
#     for j in range(1,6):
#      print(i,j)
# l=["kelly","emy","alan"]
# for i in l:
#     for j in range(1,4):
#      print(i)
# no=[1,2,3]
# qns=['what','when','why']
# for i in no:
#     print(i)
#     for i in qns:
#         print(i)
# l=[[1,2,3,4],[5,6,7,8]]
# for i in l:
#     print(i)
#     for j in i:
#         print(j)
l=[{'id':101,'name':'arun','age':23},{'id':102,'name':'amal','age':24},
   {'id':103,'name':'anu','age':22}]
for i in l:
 print(i)
for j in i.values():
        print(j)
# pattern printing
# for i in range(1,5):
#     for j in range(1,5):
#         print(i,end="")
#     print()
# for i in range(1,5):
#     for j in range(1,5):
#         print('*',end="")
#     print()
# for i in range(1,5):
#     for j in range(1,5):
#         print('#',end="")
#     print()
# for i in range(1,5):
#     for j in range(1,5):
#         print('$',end="")
# #     print()
# for i in range(1,7):
#     for j in range(1,i+1):
#         print("*",end="")
#     print()
# for i in range(1,5):
#     for j in range(1,5):
#         if(i==j):
#             print(1,end="")
#         else:
#             print(0,end="")
#     print()
#1
#23
#4567
#891011
# k=1
# for i in range(1,5):
#     for j in range(1,i+1):
#         print(k,end="")
#         k = k + 1
#     print()
# for i in range(5,0,-1):
#     for j in range(i*1,1,-1):
#         print("*",end="")
#     print()
# k=2
# for i in range(1,4):
#     for j in range(1,i+1):
#         print(k,end=" ")
#         k = k + 2
#     print()
# k=1
# for i in range(1,5):
#     for j in range(1,i+1):
#         print(k,end=" ")
#         k = k + 2
#     print()
# for i in range(5,0,-1):
#     for j in range(1,i+1):
#         print(i,end=" ")
#     print()
# for i in range(1,5):
#     for j in range(i,0,-1):
#         print(j,end=" ")
#     print()
# for i in range(1,7):
#     for j in range(1,i*1):
#         if(j%2==0):
#             print(0,end=" ")
#         else:
#              print(1,end=" ")
#     print()

# for i in range(1,6):
#     k = 65
#     for j in range(1,i*1):
#         print(chr(k),end=" ")
#         k=k+1
#     print()

# k=65
# for i in range(1,6):
#     for j in range(1,i*1):
#         print(chr(k),end="")
#         k = k + 1
#     print()
# k=ord('A')
# for i in range(1,6):
#     for j in range(1,i*1):
#         print(chr(k),end=" ")
#         k=k+1
#     print()
# l=[12,34,56,78,13,87,5]
# for i in l:
#     for j in range(2,i):
#        if(i%j==0):
#         break
#     else:
#      print(i)
#print all prime number in the range(1,100)

# for i in range(1,100):
#     for j in range(2,i):
#        if(i%j==0):
#            break
#
#     else:
#            print(i)
# k=1
# for i in range(1,6):
#     for j in range(1,i+1):
#         print(k**2,end=" ")
# #         k=k+1
#     print()
# k=1
# for i in range (1,6,2):
#     for j in range(1,i+1):
#         print(i,end=' ')
#         k=k+1
#     print()
# k=1
# for i in range(1,6,2):
#     for j in range(1,i+1):
#         if(j%2==0):
#          print('A',end=' ')
#         else:
#             print(1,end=" ")
#     print()
# k=3*2
# for i in range(1,5):
#     for p in range(1,k+1):
#         print('',end=" ")
#     k=k-2
#
#     for j in range(1,i+1):
#         print("**",end="  ")
#     print()
# #
# k=3*2
# for i in range(1,5):
#     for p in range(1,k+1):
#         print('',end=" ")
#     k=k-2
#
#     for j in range(1,i+1):
#         print("5",end="   ")
#     print()
#

# k=3*2
# for i in range(1,5):
#     for p in range(1,k+1):
#         print('',end=" ")
#     k=k-2


#     for j in range(1,i+1):
#         print("*",end="   ")
#     print()
#
# k=0
# for i in range(4,1,-1):
#     for p in range(k+2):
#         print('',end=" ")
#     k=k+2
#     for j in range(1,i):
#         print("*",end="   ")
#     print()


# k=0
# for i in range(1,5):
#     for p in range(1,k+1):
#         print("",end=" ")
#     k=k-2
#     for j in range(1,i+1):
#
#         print('*',end=" ")
#     print()
# k=0
# for i in range(3,0,-1):
#     for p in range(k-1):
#         print("",end=" ")
#     k=k-2
#     for j in range(1,i+1):
#         print('*',end=" ")
#     print()
k=6
for i in range(2,9,2):
    for l in range(2):
        for p in range(1,k+1):
            print("",end=" ")
        for j in range(1,i+1):
            print("*",end=" ")
        print()
    k=k-2



















