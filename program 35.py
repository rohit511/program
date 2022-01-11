def converttoBinary(n):
    if n>1:
        converttoBinary(n//2)
    print(n%2,end='')
    
dec=int(input("enter the number"))
converttoBinary(dec)
print()