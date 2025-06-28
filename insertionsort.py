n=int(input("enter the no of elements"))
a=[]
temp=-1
for i in range(n):
    num=int(input())
    a.append(num)
for i in range(1,n):
    temp=a[i]
    for j in range(i-1,-1,-1):
        if(temp<a[j]):
            a[j+1]=a[j]
            a[j]=temp
        elif(temp>a[j]):
            a[j+1]=temp
            break
            
print(a)
    