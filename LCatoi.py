class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        f = ""
        s = s.lstrip()

        if not s:
            return 0

        n = 1
        i = 0

        if s[0] == '-':
            n = -1
            i = 1
        elif s[0] == '+':
            i = 1
        
        while (i < len(s) and s[i].isdigit()):
            f += s[i]
            i += 1

        if f == "":
            return 0

        op = int(f) * n
        if op >=2**31:

            op=(2**31)-1

        elif op <-2**31:

            op=-2**31
    

        return op
