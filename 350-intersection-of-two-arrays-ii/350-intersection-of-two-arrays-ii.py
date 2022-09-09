class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        t=len(nums1)
        p=len(nums2)
        j=[]
        if t>=p:
            for i in nums2:
                if i in nums1:
                    j.append(i)
                    nums1.remove(i)
        else:
            for i in nums1:
                if i in nums2:
                    j.append(i)
                    nums2.remove(i)
            
        return j