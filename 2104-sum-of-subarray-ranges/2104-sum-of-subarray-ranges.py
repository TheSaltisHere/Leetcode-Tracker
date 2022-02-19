import math
class Solution:
    def subArrayRanges(self, l: List[int]) -> int:
        sum=0
        for i in range(len(l)):
            max_val=-math.inf
            min_val=math.inf           
            for j in range(i,len(l)):
                max_val=max(max_val,l[j])
                min_val=min(min_val,l[j])
                sum=sum+max_val-min_val
        return sum

                        
            
            
            
        