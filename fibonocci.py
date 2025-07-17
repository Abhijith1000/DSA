#User function Template for python3

class Solution:
    #Function to return list containing first n fibonacci numbers.
    def fibonacciNumbers(self,n):
        l=[0]
        if n==1:
            return l
        elif n==2:
            l=[0,1]
            return l
        l=[0,1]
        for i in range(3,n+1):
            l.append(l[i-2]+l[i-3])
        return l