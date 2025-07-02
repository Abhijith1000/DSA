
class Solution:
    
    #Function to check if a string is Pangram or not.
    def checkPangram(self,s):
        
        l=len(s)
        p=[]
        
        for i in range(l):
            if(s[i].isalpha() and s[i].lower() not in p):
                p.append(s[i].lower())
        if len(p)==26:
            return True
        else:
            return False