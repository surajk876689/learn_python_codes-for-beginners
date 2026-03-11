#making of some random program using for loop in python
i=0
for i in range(100):
    print(i)
    i+=1
#make another program using for loop
j=1,2,3,4,5,6,7 
for a in j:
    print(a)
#this program is run beacuse in j variable comma made an tuple or for loop is work only with iterable objects and tple is an iterable object that cannot be change thats way it run . it we are not use comma and write simple 1 than this program ocurs syntax error because 1 is nat a iterable object.
#make another program using for loop
i=int(input('enter any number you need table'))
j=0
for j in range(0,11):
    print(i,'*',j,'=',i*j)