class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]

        for i=1
        """
        for i in range(0,len(nums),1):
            for j in range(1,len(nums),1):

                if((nums[i]+nums[j])==target):

                    if(i!=j):

                        op=[i,j]
                        break

        return op
