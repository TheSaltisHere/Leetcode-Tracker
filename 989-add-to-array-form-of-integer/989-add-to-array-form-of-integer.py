class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        t=""
        l=[]
        for i in num:
            t=t+str(i)
        t=int(t)+k
        for i in str(t):
            l.append(int(i))
        return l
            
            
            
        