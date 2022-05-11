class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        t=len(arr)
        for i in range (len(arr)):
            if arr[i]==0:
                arr.append(arr[i])
                arr.append(0)
            else:
                arr.append(arr[i])
                
        for i in range(t):
            arr.pop(0)
        
        if len(arr)>t:
            
            for i in range(t,len(arr)):
                arr.pop(t)
        
        