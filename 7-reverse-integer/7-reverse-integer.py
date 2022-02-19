class Solution:
    def reverse(self, x: int) -> int:
        if x >=0:
            t = (str(x))[::-1]
            if int(t)>=-2**31 and int(t)<=(2**31)-1:
                return (int(t))
            else:
                return(0)
        else:
            t = "-"+(str(x))[:0:-1]
            if int(t)>=-2**31 and int(t)<=(2**31)-1:
                return (int(t))
            else:
                return(0)
        
        