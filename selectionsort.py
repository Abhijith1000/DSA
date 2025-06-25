n=int(input("enter the no of elements"))
a=[]
temp=-1
for i in range(n):
    num=int(input())
    a.append(num)
for i in range (n-1):
    pos=i
    for j in range(i+1,n):
      
        if(a[j]<a[pos]):
            temp=j
    if(a[temp]<a[i]):
        t=a[i]
        a[i]=a[temp]
        a[temp]=t
        print(a)

print(a)