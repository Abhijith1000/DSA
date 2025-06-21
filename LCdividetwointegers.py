class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """

        d=int(abs(dividend)//abs(divisor))

        op=d
        if(((dividend < 0 )or(divisor <0)) and (dividend*divisor<0)):

            op=-d

        else:

            op=d

        if(dividend==-2**31 and divisor==-1):

            op=2**31-1

        return op


        