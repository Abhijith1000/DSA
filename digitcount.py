class Solution:
    def countDigit(self, n):
        count=0

        while(n>0):    
            if(n%10<0):
                break
            else:
                count=count+1
                n=n//10
        return count
print(Solution().countDigit(340))
