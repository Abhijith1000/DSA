
class Solution:
    def intersectionWithDuplicates(self, a, b):
        l=[]
        for i in range(len(a)):
            for j in range(len(b)):
                if a[i]==b[j] and b[j] not in l:
                    l.append(b[j])
        return l