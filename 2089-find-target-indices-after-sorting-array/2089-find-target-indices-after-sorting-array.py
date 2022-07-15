class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        final=[]
        while target in nums:
            final.append(nums.index(target))
            nums[nums.index(target)]="Fill"
        return final