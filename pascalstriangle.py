class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        o=[[1]]
        op=[[1],[1,1]]
        if numRows==1:
            return o
        elif numRows==2:
            return op
        else:
            for i in range(2,numRows):
                temp=[1]
                for j in range(1,i):
                    t=op[i-1][j-1]+op[i-1][j]
                    temp.append(t)
                temp.append(1)
                op.append(temp)
        return op
