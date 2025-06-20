n=int(input("enter the number"))

flag=0
for i in range(n-1,2,-1):
    if (n%i==0):
        flag=1
        print("not prime")
        break;
if (flag==0):
    print("prime number")


    

