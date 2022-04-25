class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        index_value=nums.index(max(nums))
        array=[]
        duplicate=nums*2
        for i in range(len(nums)):
            if nums[i]==nums[index_value]:
                array.append(-1)
            else:
                for j in range(i+1,len(duplicate)):
                    if duplicate[j]>duplicate[i]:
                        array.append(duplicate[j])
                        break
        return array
        
  
                
        
        