class Solution(object):
    def divideString(self, s, k, fill):
        """
        :type s: str
        :type k: int
        :type fill: str
        :rtype: List[str]
        """
        if(len(s)%k!=0):

            s=s + fill *(k-(len(s)%k))
        op=[]

        for i in range(0,len(s),k):
            op.append(s[i:i+k])

        return op