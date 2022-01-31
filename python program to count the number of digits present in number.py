num =3452
print(len(str(num)))
count=0
while num!=0:
    num= num//10
    count=count+1
    print("number of digit are ",str(count))

    