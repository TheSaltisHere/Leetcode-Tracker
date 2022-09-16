class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l=nums1
        l.extend(nums2)
        l.sort()
        print(l)
        t=len(l)
        if t%2==0:
            a=(t//2)-1
            ans=(l[len(l)//2]+l[a])/2
        else:
            a=t//2
            ans=l[a]
        
        ans=round(ans,4)
        print(ans)
        return ans