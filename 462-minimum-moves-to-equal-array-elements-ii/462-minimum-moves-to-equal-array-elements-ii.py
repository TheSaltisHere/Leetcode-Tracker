class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        if len(nums)%2==0:
            a=floor(len(nums)/2)
            median=int(nums[a-1]+nums[a])/2
        else:
            a=floor(len(nums)/2)
            median=nums[a]
            
        final=0
        for i in nums:
            final=final+abs(median-i)
        return int(final)
                
    
        