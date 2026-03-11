n=int(input('enter a number they you need factorial: '))
factorial=1
for i in range(1,n+1):
    factorial=factorial*i
print('Factorial of ',n,'Numbers is: ',factorial)