class Solution:
    # Your task is to Complete this function
    # functtion should return an integer
    def maxDistance(self, arr):
        n=len(arr)
        d={}
        dist=0
        max=0
        for i, val in enumerate(arr):
            if val not in d:
                d[val]=i
            else:
                dist=i-d[val]
                if dist > max:
                    max=dist
        return max