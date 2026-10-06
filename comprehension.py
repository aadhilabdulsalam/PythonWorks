# l=[1,2,3,4,5]
# new_list=[i**2 for i in l]
# print(new_list)                #this is only for simple program

# new_list=[5 for i in l]
# print(new_list)
#Given a list l=[12,45,34,67,90]
# create a new list with even values
#
# new=[i for i in l if i%2==0]
# print(new)


#create a new list with values greater than 50
# new=[i for i in l if i>50]
# print(new)

#Given  a list colors=['red','green','blue','orange']
# colors=['red','green','blue','orange']
# # create a new list with first letter of each color
# new=[i[0] for i in colors]
# print(new)

# create a new list with length of each color






# # #create a new list with square root of each element
# l=[25,16,9,36]
# new=[i**0.5 for i in l]
# print(new)
#
#
# # #Given a dictionary
# d={'arun':25,'amal':34,'akhil':26,'anu':21}
# # # create a list of names
# new=[i for i in d]
# print(new)
# # # create a list of marks
# new=[i for i in d.values()]
# print(new)
# #
# # #Given a list
# l=[23,56,12,89,-34,-23,-67,-43,9.7,4.5,'hello','world']
#
# # #create a list of string values
# new=[i for i in l if type(i)==str]
# print(new)
# # #create a list of floats
# new=[i for i in l if type(i)==float]
# print(new)
# # #create a list of positive numbers
# new=[i for i in l if(type(i)==int or type(i)==float)and i>0]
# print(new)
# #
# #
# # #Given a list
# fruits=['apple','orange','pineapple','avocado','grapes']
# # #create a new list with elements whose length is greater than 6
# new=[i for i in fruits if len(i)>6]
# print(new)
#
# # #create a new list with elements whose value is divisible by 3 in range(1,101)
# new=[i for i in range(1,101) if i%3==0]
# print(new)
#
# # Given
# s="python coding  is easy and fun"
# # # create a new list with only vowels
# vowels=('a','e','i','o','u')
# new=[i for i in s if i in vowels]
# print(new)


#                                                    SET COMPREHENSION
#create a new set with only letters
# s="python coding is easy and fun"
# new={i for i in s if i!=" "}
# print(new)
# #create a new set with only vowels
# new={i for i in s if i in "aeiouAEIOU"}
# print(new)
# #create a new set with length of each word
# new={len(i) for i in s.split()}
# print(new)
#
#
# #                                                DICTIONARY COMPREHENSION
#
# l=[1,2,3,4]
# new={i:i**2 for i in l}
# print(new)
#given a list
l=[10,20,30,40]
#create  a new dictionary where key are index of each number and values are number from not list
new={i:l[i]for i in range(len(l))}
print(new)
s="python coding is easy and fun"
#create a new dictionary where keys are word and values are length of each word
new={i:len(i) for i in s.split()}
print(new)