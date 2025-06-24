class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """   
        op=[]
        three=[]

        for i in range(0,len(nums),1):
            for j in range(1,len(nums),1):
                for k in range(2,len(nums),1):
                    if(((nums[i]+nums[j]+nums[k])==0) and  i != j and i != k and j != k):
                        three=sorted([nums[i], nums[j], nums[k]])
                        if three not in op:
                            op.append(three)
        return op
