'''Allow 4 friends to enter their favorite language as 
value and use key as their names. Assume that the names are unique.'''
d={} # creating an empty dictionary and storing it in the variable d
n=input('enter your name')
v=input('enter your favorite language')
d[n]=v# taking input from the user for their name and favorite language and storing it in the dictionary d with the name as the key and the favorite language as the value
n1=input('enter your name')
v1=input('enter your favorite language')
d[n1]=v1# taking input from the user for their name and favorite language and storing it in the dictionary d with the name as the key and the favorite language as the value
n2=input('enter your name')  
v2=input('enter your favorite language')
d[n2]=v2# taking input from the user for their name and favorite language and storing it in the dictionary d with the name as the key and the favorite language as the value
n3=input('enter your name')
v3=input('enter your favorite language')
d[n3]=v3# taking input from the user for their name and favorite language and storing it in the dictionary d with the name as the key and the favorite language as the value
print(d) # printing the dictionary d, which now contains the names and their corresponding favorite languages entered by the users.
#If the names of 2 friends are same; what will happen to the program
s={
    'name':'suraj',
    'name':'suraj kumar'
}
print(s)

#If languages of two friends are same; what will happen to the program
s={
    'suraj':'python',
    'yo yo':'python'
}
print(s)