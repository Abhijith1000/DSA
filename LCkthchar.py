class Solution(object):
    def kthCharacter(self, k):
        s="a"
        n=0
        p=k
        alp=list(string.ascii_lowercase)
        while p >=1:
            n+=1
            p=p//2
        
        for i in range (n):
            temp=""
            for j in range(len(s)):
                for b in range(26):
                    if s[j]==alp[b]:
                        if alp[b]=="z":
                            temp=temp+alp[0]
                        else:
                            temp=temp+alp[b+1]
            s=s+temp
        return s[k-1]
