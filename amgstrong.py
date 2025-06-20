n=int(input("enter the number"))
l=len(str(n))
m=n
p=0
while(m>0):
    p=p+(m%10)**l
    m=m//10
if n==p:
    print("amgstrong")
else:
    print("not amgstrong")       