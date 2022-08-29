class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        sample=int(str(int(str(num)[::-1]))[::-1])
        if sample==num:
            return True
        else:
            return False
        
        
        