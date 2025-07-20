def abc(arr,k):
    length=len(arr)
    l=0
    
    for i in range(length):
        sum=0
        for j in range(i+1,length):
            sum+=arr[j]
            if sum==k and j-1>=l:
                    l=j-i
    return l

