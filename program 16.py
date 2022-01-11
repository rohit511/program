n=int(input("enter the number"))
fact=1
if n<0:
    print("factorial is not pssible")
elif n==0:
    print("factorial of number is one")
else:
    for i in range(1,n+1):
        factorial=fact*i
        print("factorial of the number is ",factorial)