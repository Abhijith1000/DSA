class Solution:
    def mergeArrays(self, a, b):
        a.extend(b)
        n=len(a)
        for i in range(n):
            for j in range(n-1-i):
                if a[j]>a[j+1]:
                    a[j],a[j+1]=a[j+1],a[j]
        for i in range(n):
            print(a[i], end=" ")