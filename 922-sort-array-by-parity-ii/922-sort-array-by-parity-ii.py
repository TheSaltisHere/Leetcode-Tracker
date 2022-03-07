class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        arr_odd=[]
        arr_even=[]
        for i in nums:
            if i%2==0:
                arr_even.append(i)
            else:
                arr_odd.append(i)
        final=[]
        while len(arr_odd)!=0 or len(arr_even)!=0:
            final.append(arr_even.pop())
            final.append(arr_odd.pop())
        return final
            
        