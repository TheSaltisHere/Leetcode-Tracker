class Solution:
    def sumZero(self, n: int) -> List[int]:
        array = []
        if n%2!=0:
            array=[0]
            
        for i in range(n//2):
            array.append(i+1)
            array.append(-i-1)
            
        return array
        
        