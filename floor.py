class Solution:
    #User function Template for python3
    
    #Complete this function
    def findFloor(self, arr, x):
        op=-1
        temp=0
        for i in range(0,len(arr),1):
            if(arr[i]<=x and arr[i]>=temp):
                temp=arr[i]
                op=i
        return op
        