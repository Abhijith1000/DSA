class Solution:
	def twoSum(self, arr, target):
	    f=0
        for i in range(len(arr)):
		    for j in range(1,len(arr)):
		        if arr[i]+arr[j]==target and i!=j:
		            f=1
		            break
	        if f==1:
		           break
		        
        if f==1:
		    return True
	    else:
	        return False