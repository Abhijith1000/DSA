class Solution:
    def firstRepeated(self,arr):
        seen=set()
        
        index=-1
        
        for i in range (len(arr)-1,-1,-1):
        
            if arr[i] in seen:
                
                index=i
                
            else:
                
                seen.add(arr[i])
                
        return index+1 if index !=-1 else -1



arr = [2, 5, 3, 7, 4, 7]
print(Solution().firstRepeated(arr))