from itertools import combinations
class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        l=[3**0,3**1,3**2,3**3,3**4,3**5,3**6,3**7,3**8,3**9,3**10,3**11,3**12,3**13,3**14,3**15,3**16]
        sum_array=[]
        for i in range(1,17):
            comb=combinations(l,i)
            
            for j in list(comb):
                sum_array.append(sum(j))
                
            if n in sum_array:
                return True
            
        return False
            
        
        
        