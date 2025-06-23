class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        sum=0

        for i in range(0,len(s),1):

            if(s[i]=="I"):
                sum+=1
            elif(s[i]=="V"):
                sum+=5

            elif(s[i]=="X"):
                sum+=10
            
            elif(s[i]=="L"):
                sum+=50

            elif(s[i]=="C"):
                sum+=100
            elif(s[i]=="D"):
                sum+=500
            elif(s[i]=="M"):
                sum+=1000
        for i in range(0,len(s)-1,1):

            if(s[i]=="I" and s[i+1]=="V"):
                sum-=2
            elif(s[i]=="I" and s[i+1]=="X"):
                sum-=2
            elif(s[i]=="X" and (s[i+1]=="L" or s[i+1]=="C")):
                sum-=20
            elif(s[i]=="C" and (s[i+1]=="D" or s[i+1]=="M")):
                sum-=200
        return sum
