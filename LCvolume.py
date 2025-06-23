class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        vol=0
        temp=0
        s=height
        n=len(height)
        if len(height)>10*5:
            s=s[1:10*5]
            n=len(s)
        for i in range(n):
            for j in range(1+i,n):
                temp=((min(s[i],s[j]))*(j-i))

                if(temp>vol):
                    vol=temp
                    
                
            
        return vol

    