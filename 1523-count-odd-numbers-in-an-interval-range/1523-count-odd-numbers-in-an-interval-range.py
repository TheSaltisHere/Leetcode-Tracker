import math
class Solution:
    def countOdds(self, low: int, high: int) -> int:
        if low%2==1 and high%2==0:
            count=((high-low-1)//2) +1
            
        elif low%2==1 and high%2==1:
            count=((high-low-1)//2) +2
            
        elif low%2==0 and high%2==0:
            count=(math.ceil((high-low-1)/2))
                
        elif low%2==0 and high%2==1:
            count=((high-low-1)//2) +1
            
        return count
            