from collections import Counter 
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        t=len(s1)
        count_s1=Counter(s1)
        
        for i in range(len(s2)-len(s1)+1):
            if Counter(s2[i:i+t])==count_s1:
                return True
            
        return False
        
        