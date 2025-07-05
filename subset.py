class Solution:
    def isSubset(self, a, b):
        a_copy = a.copy()
        for element in b:
            if element in a_copy:
                a_copy.remove(element)
            else:
                return False
        return True
