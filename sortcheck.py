class Solution:
    def arraySortedOrNot(self, arr) -> bool:
        f=1
        for i in range(0,len(arr)-1):
            if(arr[i]>arr[i+1]):                
                f=0
                break
        if (f==0):
            return False
        else:
            return True