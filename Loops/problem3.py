#Write a program to find the sum of first n natural numbers using while loop. 
n=int(input('enter a number they you need sum of n numbers: '))
sum=0
i=1
while i<=n:
    sum=sum+i
    i+=1
print('Sum of first',n,'Natural numbers is: ',sum)