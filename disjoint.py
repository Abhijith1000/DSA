#User function Template for python3
class Solution:
    # Function to check if two arrays are disjoint
    def areDisjoint(self, a, b):
        a=set(a)
        b=set(b)
        c=a.intersection(b)
        if len(c) !=0:
            return False
        else:
            return True