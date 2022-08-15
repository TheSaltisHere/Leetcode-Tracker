class Solution:
    def climbStairs(self, n: int) -> int:
        l=[]
        for i in range(n+1):
            if i==0:
                l.append(1)
            elif i==1:
                l.append(1)
            else:
                l.append(l[len(l)-1]+l[len(l)-2])
        
        return(l[len(l)-1])
                
                
        