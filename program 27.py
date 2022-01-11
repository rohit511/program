x=int(input("enter the values"))
y=int(input("enter the vaalues"))
def lcm(x,y):
    if x>y:
        greater=x
    else:
        greater=y
    while(True):
        if((greater % x==0)and(greater % y==0)):
            lcm=greater
            break
        greater+=1
    return lcm

print("the lcm is",lcm(x,y))