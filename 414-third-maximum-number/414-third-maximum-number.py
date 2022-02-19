class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        l=[]
        for i in nums:
            if i not in l:
                l.append(i)
                
        l.sort(reverse=True)
        a=len(l)
        if a>=3:
            return l[2]
        else:
            return l[0]
            
            
            