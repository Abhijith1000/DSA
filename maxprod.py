class Solution(object):
    def maxProduct(self, n):
        l=[]
        while n>0:
            s=n%10
            l.append(s)
            n=n//10
        l.sort()
        p=l[len(l)-2]*l[(len(l)-1)]
        return p