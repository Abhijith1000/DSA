#User function Template for python3

class Solution:
    #Complete the below function
    def countPairs(self,arr, target):
        count=0
        for i in range (len(arr)-1):
            for j in range(i+1,len(arr)):
                if(arr[i]+arr[j]==target):
                    count+=1
        return count