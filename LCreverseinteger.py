class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        reverse=""

        if((x>=2**31) or (x<=-2**31)):

            op=0

        elif(x>0):
            y=str(x) 

            reverse=y[::-1] 
            op=int(reverse)

        else:

            y=abs(x)
            p=str(y)
            z=p[::-1] 
            reverse="-"+z
            op=int(reverse) 

        if((op>=2**31) or (op<=-2**31)):
            op=0

        return op