post=input('enter a post: ')# this line takes input from the user and stores it in the variable post
if 'suraj'in post:# this line checks if the string 'suraj' is present in the user's input (post)
    print('This post is talking about you')# if the condition is true, it prints a message indicating that the post is talking about you
else:# if the condition in the if statement is not satisfied, it means the post is not talking about you
    print('This post is not talking about you')# this line prints a message indicating that the post is not talking about you if the condition in the if statement is not satisfied.
print('Thank you for using this program!')# this line will be executed regardless of the outcome of the if-else block, as it is outside of it. It serves as a thank you message to the user for using the program.