class Solution(object):
    def isPalindrome(self, x):
        a=str(x)
        revs=a[::-1]
        if revs==a:
            return True
        else:
            return False
