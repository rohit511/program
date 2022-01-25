string=input()
try:
    num=int(input())
    print(string+num)
except(Typeerror,Valueerror)as e:
    print(e)