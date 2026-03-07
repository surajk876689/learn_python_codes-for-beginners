grade=float(input('enter your grade: ')) # this line takes input from the user and converts it to a float, storing it in the variable grade
if grade>=90: # this line checks if the grade is greater than or equal to 90
    print('your grade is EXCELLENT.') # if the condition is true, it prints that the grade is EXCELLENT
elif grade>=80: # this line checks if the grade is greater than or equal to 80
    print('your grade is A')
elif grade>=70: # this line checks if the grade is greater than or equal to 70
    print('your grade is B')
elif grade>=60: # this line checks if the grade is greater than or equal to 60
    print('your grade is C')
elif grade>=50: # this line checks if the grade is greater than or equal to 50
    print('your grade is D')
elif grade>=40: # this line checks if the grade is greater than or equal to 40
    print('your grade is E')
elif grade>=0: # this line checks if the grade is greater than or equal to 0
    print('your grade is Fail')            