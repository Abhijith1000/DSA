class Solution:

	def findMaximum(self, arr):
		# code here
		max=arr[0]
		for i in range(0,len(arr),1):
		    if(arr[i+1]>=arr[i]):
		        max=arr[i+1]
		    else:
		        break
		return max