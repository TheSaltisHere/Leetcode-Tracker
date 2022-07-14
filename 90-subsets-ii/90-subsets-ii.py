from itertools import combinations
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        final=[]
        nums.sort()
        for i in range(0,len(nums)+1):
            combs=combinations(nums,i)
            
            for i in combs:
                if list(i) not in final:
                    final.append(list(i))
        
        return (final)
                
            
        