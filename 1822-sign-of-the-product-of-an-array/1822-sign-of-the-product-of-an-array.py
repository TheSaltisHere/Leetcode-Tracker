class Solution:
    def arraySign(self, nums: List[int]) -> int:
        count=0
        for i in nums:
            if i==0:
                return 0
            elif i<0:
                count=count+1
        
        if count==0:
            return 1
        
        else:
            if count%2==0:
                return 1
            else:
                return -1
                
        