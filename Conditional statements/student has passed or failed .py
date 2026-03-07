'''Write a program to find out whether a student has passed or failed if it requires a 
total of 40% and at least 33% in each subject to pass. Assume 3 subjects and 
take marks as an input from the user.'''
# taking input from the user for marks in three subjects
Subject1=float(input('enter your first subject marks: '))
Subject2=float(input('enter your second subject marks: '))
Subject3=float(input('enter your third subject marks: '))
print('Your marks in the three subjects are:', Subject1, Subject2, Subject3) # this line prints the marks entered by the user for the three subjects
if Subject1>=33 and Subject2>=33 and Subject3>=33 and (Subject1+Subject2+Subject3)/3 >= 40: # this line checks if the marks in each subject are greater than or equal to 33 and if the average of the three subjects is greater than or equal to 40
    print('Congratulations! You have passed.')
else:
    print('Sorry, you have failed.')