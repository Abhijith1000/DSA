class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        f=0
        if(n==1):
            return True
        elif(n==0):
            return False

        while n!=1:
            if(n%2==0):
                n=n/2
            else:
                f=1
                break
        if(f==0):
            return True
        else:
            return False
    