#find the greatest of four numbers entered by the user.
a=float(input('enter any number: '))# this line takes input from the user and converts it to a float, storing it in the variable a)
b=float(input('enter any number: '))# this line takes input from the user and converts it to a float, storing it in the variable b)
c=float(input('enter any number: '))# this line takes input from the user and converts it to a float, storing it in the variable c)
d=float(input('enter any number: '))# this line takes input from the user and converts it to a float, storing it in the variable d)
if a>b and a>c and a>d: # this line checks if a is greater than b, c, and d
    print('the greatest number is:',a) # if the condition is true, it prints that a is the greatest number
elif b>a and b>c and b>d: # this line checks if b is greater than a, c, and d
    print('the greatest number is:',b) # if the condition is true, it prints that b is the greatest number
elif c>a and c>b and c>d: # this line checks if c is greater than a, b, and d
    print('the greatest number is:',c) # if the condition is true, it prints that c is the greatest number
else: # if none of the above conditions are true
    print('the greatest number is:',d) # it prints that d is the greatest number
print('Congratulations! You have successfully found the greatest number among the four numbers you entered.') # this line will be executed regardless of the outcome of the if-elif-else block, as it is outside of it. It serves as a congratulatory message to the user for successfully finding the greatest number.