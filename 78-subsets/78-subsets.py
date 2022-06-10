from itertools import combinations
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        l=[]
        for i in range(len(nums)+1):
            t=combinations(nums,i)
            for i in t:
                l.append(list(i))
        return l
        