class Solution(object):
    def intToRoman(self, num):
        s=""
        k=num/1000
        if k>=1:
            for i in range (k):
                s+="M"
        num=num%1000
        h=num/100
        if h>=1:
            if h==4:
                s+="CD"
            elif h==9:
                s+="CM"
            elif h>=5:
                s+="D"
                if h>5 and h!=9:
                    dif=h-5
                    for i in range (dif):
                        s+="C"
            elif h<4:
                for i in range (h):
                    s+="C"
        
        num=num%100
        h=num/10
        if h>=1:
            if h==4:
                s+="XL"
            elif h==9:
                s+="XC"
            elif h>=5:
                s+="L"
                if h>5 and h!=9:
                    dif=h-5
                    for i in range (dif):
                        s+="X"
            elif h<4:
                    for i in range (h):
                        s+="X"
        num=num%10
        h=num
        if h>=1:
            if h==4:
                s+="IV"
            elif h==9:
                s+="IX"
            elif h>=5:
                s+="V"
                if h>5 and h!=9:
                    dif=h-5
                    for i in range (dif):
                        s+="I"
            elif h<4 and h!=0:
                    for i in range (h):
                        s+="I"
       
        return s
