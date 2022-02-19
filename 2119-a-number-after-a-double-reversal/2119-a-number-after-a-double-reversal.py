class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        a=str(num)[::-1]
        b=int(a)
        c=str(b)[::-1]
        d=int(c)
        
        if d==num:
            return True
        else:
            return False
        
    
    