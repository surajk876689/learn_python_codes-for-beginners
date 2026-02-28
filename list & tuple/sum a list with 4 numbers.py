'''list=[1,2,3,4]
print(sum(list))'''
#sum of list with 4 numbers is take list elements from user
list1=[]
li=int(input("enter a element to add in list"))
list1.append(li)
li1=int(input("enter a element to add in list"))
list1.append(li1)
li2=int(input("enter a element to add in list"))
list1.append(li2)
li3=int(input("enter a element to add in list"))
list1.append(li3)
print(list1)
list1.sort()
print(list1)

print(sum(list1))