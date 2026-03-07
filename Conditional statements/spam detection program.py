spam=input('enter the comment: ') # this line takes input from the user and stores it in the variable spam
if "Make a lot of money" in spam or "buy now" in spam or "subscribe this" in spam or "click this" in spam:
    print(" \"Alert\": This is a spam comment.")
else:
    print("This is not a spam comment.")