n=int(input("enter the number"))
rev=""
while(n>0):

     rev=rev+str(n%10)
     n=n//10


print(rev)




