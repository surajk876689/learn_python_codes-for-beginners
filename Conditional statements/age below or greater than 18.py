# Write a program to print yes when the age entered by the user is greater than or equal to 18.
age=int(input('enter your age: '))
if age>=18:
    print('You are eligible for our criteria and you can apply for the job\n Congratulations!')
elif age<18:
    print('You are not eligible for our criteria and you cannot apply for the job')
else:
    print('Invalid input. Please enter a valid age.')
    '''This code will take the age as input from the user, and then check if the age is greater than or equal to 18. If it is, it will print a message saying that the user is eligible for the criteria and can apply for the job. If the age is less than 18, it will print a message saying that the user is not eligible for the criteria and cannot apply for the job. If the input is invalid (not a number), it will print an error message asking for a valid age.'''
print('This line will be executed regardless of the age entered by the user, as it is outside the if-elif-else block. It demonstrates that the program continues to execute after the conditional statements, regardless of the outcome of those statements.')