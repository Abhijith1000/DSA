class Solution:
    def printNos(self, n):
        op=""
        
        def recur(n):
            if n==1:
                print("1")
            else:
                print(n, end=" ")
                recur(n-1)


        recur(n)    