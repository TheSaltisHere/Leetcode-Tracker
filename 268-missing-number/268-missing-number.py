class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        x=[i for i in range(len(nums)+1)]
        for i in x:
            if i not in nums:
                return i