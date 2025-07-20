class Solution(object):
    def findNumbers(self, nums):
        f=0
        for i in range(len(nums)):
            n=nums[i]
            count=0
            while n>0:
                n=n//10
                count+=1
            if count % 2==0:
                f+=1
        return f
        