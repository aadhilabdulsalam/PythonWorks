#declare a list 5 colours
l=["red","voilet","blue","green","white"]
#add a new color 'yellow' to the list
l.append("Yellow")
#change the second clour to black
l[1]="black"
#print the updated list
print(l)
#print the second last color
print(l[-2])
#print the number of color
print(len(l))
#print the reverse of list
print(l[::-1])