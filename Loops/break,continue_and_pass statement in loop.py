#use of break statement
'''break statement is use to exit the loop. 
means break the flow and exit freom loop.'''
#example
i=0
for i in range(10):
    print(i)
    break
#use of continue statement
'''continue statement is use to skip the
current iteration of loop'''
#example
a=1
for a in range(10):
    if(a==3):
       continue
    print(a)
#use of pass statement
'''Pass meaning do nothing.
it is used when python need 
a statement but you don't
want to execute any code yet'''
s=1
for s in range(10):
    if s==3:
       pass
    print(s)
