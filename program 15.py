n=int(input("Enter the number upto which you wish to find prime numbers"))
prime=True   
for i in range(0,n+1):
    if i<0:
        print("Please Enter proper number")
    elif i==1:
        print("1 is prime number")
    else:
        for j in range(2,i):
            if i%j==0:
                prime=False
                break
        if prime:
            print(i," is a prime number")
        else:
            print(i," is a non-prime number")
    prime=True
